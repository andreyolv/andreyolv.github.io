# 7. SparkSession Sizing

The previous chapters decide **where** the driver runs. This one decides **with how much**: how much memory and how many threads the session requests, and how that talks to the task pod's `request`. It is the difference between a job that fits on the worker and one that dies midway — and almost every error here comes from two mistakes: thinking allocated memory is needed memory, and thinking thread is core.

What changes by deploy mode: in `local` and `client` the driver lives **inside the task pod**, so it shares `request` with Airflow and whatever else the task does; in `cluster` it has its own pod and sizes itself, without touching the worker. The two sections below cover the first two.

## `local` mode

Do not know which mode — or which master — your process's Spark is using? Then it is probably `local`. It is the default of whoever configures nothing.

Apache does not recommend this mode for production, and the reason is the [deploy modes table](03-deploy-modes.md#comparative): without a separate executor, the ceiling is the memory of a single process. But the architecture here changes the account. Each Airflow task runs in its own pod and does not compete with another system — unlike a shared physical machine —, so driver and tasks in the same JVM save exactly the resource that would go to coordinating executors. The result is a simple, robust and relatively efficient mode for intermediate-sized data, viable even for small processing, where bringing up an executor would take as long as the whole job.

Not everything is roses, and `local` mode's limitations all come from the same origin: Spark was born for cluster.

### Allocated memory is not needed memory

Spark's optimizations are made to **use as much memory as available**, not to keep consumption low — that makes sense for an executor, which has 100% of its capacity dedicated to it. Applied to the driver, the effect is this: if `spark.driver.memory` says 10 GB for a processing that does not need 10 GB, the driver will speed up as much as it can and hold memory cache during the whole process (the same reasoning as [shuffle](02-cluster-managers.md#dynamic-allocation-and-the-shuffle) — local data in memory is data not recomputed).

The same job with less memory, still within the operational limit, discards unused cache and optimizes for the lower value, with or without increased execution time. That is: **the driver using more memory when it exists does not mean it needed it**. Reading a run's peak usage and turning it into `request` is the most common way to pay double for a job that runs the same on half.

### Competition inside the pod

Another problem is the driver competing with the rest of the process. A task written with Spark **and** Pandas uses the same pod resources for both — it can exceed the `request` sent to Kubernetes and the task becomes a candidate to be killed as an offender. In that case it is worth swapping Pandas for `pyspark.pandas`, which shares the same driver's resources with Spark instead of opening a parallel arena.

### Threads are not cores

Executors — and the driver in `local` mode — run each task on a **virtual thread**. It is not necessary to have one physical core per task: 2 to 4 threads per core are recommended.

The default is the trap. `local[*]` means "as many processors as the JVM sees", and the JVM sees the cgroup **limit**, not the `request`. Since `worker_resources` in [dag_sparksubmitoperator.py](../../dags/dag_sparksubmitoperator.py) declares only `requests`, there is no limit, and the JVM counts the EKS node's cores — 64, for example. That is 64 tasks disputing CPU time on a 1.5 `request`, each holding its memory slice.

That is not efficient because **CPU `request` is not a physical core, it is processing time**. The number of threads should come from the request:

```
threads = requestCPU × threadFactor
```

With a `request` of 1.5 CPU and factor 2, `local[3]`. A practical reference is keeping that ratio around 1.5 when there is no reason to calibrate differently.

Two notes: `spark.driver.cores` **has no effect in `local` mode** — per Spark docs it only works in `cluster` mode —, so parallelism here is defined by the `N` of `local[N]`, which in `SparkSubmitOperator` comes from the connection host and not from `conf`. And since `spark.sql.shuffle.partitions` default is 200, few threads with that value intact yield 200 tiny partitions: [see in the FAQ](08-faq.md#javalangoutofmemoryerror-java-heap-space).

### How to ask: exact memory, overallocated CPU

In a well-written job the Spark session is the task's biggest resource consumer. Hence the recommended asymmetry for `local` mode on Kubernetes:

| resource | how to ask | why |
|---|---|---|
| memory | **exact allocation**: pod `request` ≈ `spark.driver.memory` | excess (JVM metaspace, Python worker, Airflow itself) is small and the cluster absorbs it, because this is `request` and not `limit` |
| CPU | **overallocation**: ask less than the peak | Spark runs on virtual threads, not physical cores, and overallocating CPU degrades in time, not in failure |

The asymmetry is the same of the two failure modes: missing CPU makes the job slow, missing memory kills the JVM.

## `client` mode

The more advanced alternative, which asks for more calibration and holds larger volume. The mechanics are in [deploy modes](03-deploy-modes.md#client) — driver on the task pod, executors as pods in the cluster; here it matters only what that does to sizing.

Simplified, it is as if the `local` mode driver started using external executors instead of running tasks on its own JVM. What you gain and what you pay:

- **much higher overhead** than in `local` mode — coordination, network and pod startup that did not exist before;
- **much higher scalability**, because each executor can be born on a different node;
- **redundancy**: in `local` mode, missing memory breaks the whole process, since the driver is on the same JVM as tasks. In `client` mode, an executor that dies loses its processing, but the driver asks for another pod and replaces the dead one.

Who asks for executors is the driver, from `spark.executor.memory` and `spark.executor.cores` plus overhead — nothing of that goes through the task's `executor_config`. The **driver's** `request`, on the other hand, is sized just like in `local` mode, with the same rule of sharing the pod with the Airflow task. On `worker_resources` this shows up as a larger request in `client_mode` (3G) than in `cluster_mode` (1G), where it only supervises.

Careful with name collision: `spark.kubernetes.executor.request.cores` sizes the Spark **executor** pod; `executor_config` sizes the Airflow **executor** pod (the worker). Detail in `worker_resources` docstring.

## Summary

| question | `local` | `client` |
|---|---|---|
| who sizes the driver | task `executor_config` + `spark.driver.memory` | same |
| who sizes executors | none | `spark.executor.memory` / `.cores`, requested by the driver |
| parallelism | `N` of `local[N]`, ≈ 1.5 × CPU request | `spark.executor.cores` × instances |
| memory | request ≈ `spark.driver.memory` | same for the driver |
| CPU | overallocate | overallocate on driver |
| missing memory kills | the whole job | one executor, which is replaced |

## References

- [Application Properties](https://spark.apache.org/docs/latest/configuration.html#application-properties) — `spark.driver.memory`, `spark.driver.cores` and each one's scope
- [Master URLs](https://spark.apache.org/docs/latest/submitting-applications.html#master-urls) — `local`, `local[N]`, `local[*]`
- [Tuning Spark](https://spark.apache.org/docs/latest/tuning.html) — memory, serialization and parallelism level
- [Pandas API on Spark](https://spark.apache.org/docs/latest/api/python/user_guide/pandas_on_spark/index.html) — the `pyspark.pandas` mentioned above

---

[Conclusion ←](06-conclusion.md) · [Index](README.md) · [Next: FAQ →](08-faq.md)
