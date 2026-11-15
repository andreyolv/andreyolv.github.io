# 1. Spark Architecture

A Spark application is three pieces:

- **Driver** — runs your code, builds and optimizes the plan, divides the work into tasks and distributes them. It holds the `SparkSession`. One per application, and if it dies the application dies.
- **Executors** — processes that run tasks and keep data in cache. N per application, and they exchange data with each other in the shuffle.
- **Cluster manager** — allocates the resources where driver and executors will run. It understands nothing about Spark: it only delivers process and memory.

![Driver, cluster manager and executors](https://spark.apache.org/docs/latest/img/cluster-overview.png)

<sub>Source: [Cluster Mode Overview](https://spark.apache.org/docs/latest/cluster-overview.html)</sub>

Two consequences that explain almost everything in this documentation:

1. **Executors connect back to the driver.** It is not only the driver talking to them. That is why the driver needs a reachable address and open ports.
2. **The three pieces can run in different places.** Where the driver runs is the [deploy mode](03-deploy-modes.md). Who delivers the resources is the [cluster manager](02-cluster-managers.md). The rest of the documentation is just combinations of that.

## Glossary

| term | what it is | in Kubernetes |
|---|---|---|
| **Application** | your Spark program: a driver plus its executors | the pods that come up for that job |
| **Driver** | runs the `main()` and holds the `SparkSession` | a pod (cluster mode) or the process inside the Airflow worker (client and local) |
| **Executor** | runs tasks and keeps data in memory or disk | a pod |
| **Cluster manager** | obtains the resources where driver and executors run | Kubernetes itself, addressed via `k8s://` |
| **Deploy mode** | where the driver runs: inside the cluster (`cluster`) or outside it (`client`) | see [deploy modes](03-deploy-modes.md) |
| **Node** (*worker node*) | machine that executes application code | an EKS node |
| **Application package** | the `.py`, `.zip` or `.jar` with your code. It should not include Spark libraries — they come from the runtime | comes from the image via `local://`, or from S3 |
| **Job** | parallel computation triggered by an action (`save`, `collect`), made of several tasks | — |
| **Stage** | set of tasks within a job; the boundary between stages is the shuffle | — |
| **Task** | unit of work sent to an executor | — |

Careful with the word **worker**, which here means three different things: the Spark *worker node* (the node), the Airflow *worker* (the pod that runs the task) and the Spark Standalone *worker* (the JVM that hosts executors). In this documentation "worker" alone is always the Airflow one.

A **job** in Spark vocabulary is not the whole application: an application fires several jobs, one per action. In daily life we also call the application a "job" — driver logs use the strict sense.

## References

- [Cluster Mode Overview](https://spark.apache.org/docs/latest/cluster-overview.html) — driver, executors and cluster manager, and the source of the diagram above
- [apache/spark](https://github.com/apache/spark)

---

[Technical articles index](../README.md) · [Index](README.md) · [Next: Cluster Managers →](02-cluster-managers.md)
