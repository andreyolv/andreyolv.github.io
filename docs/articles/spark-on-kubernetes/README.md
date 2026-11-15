# Spark on Kubernetes

How to run Spark on EKS from Airflow: the deploy modes, the available solutions, and what to choose. The concept pages end with a "when to use which" and the topic references; the decision closes at [conclusion](06-conclusion.md), with a decision tree. After that, two operations pages: sizing the session and the errors that show up when sizing is wrong.

## Concepts

1. [Spark Architecture](01-architecture.md) — driver, executors, cluster manager, and the glossary
2. [Cluster Managers](02-cluster-managers.md) — Standalone, YARN, Kubernetes, and why Kubernetes here
3. [Deploy Modes](03-deploy-modes.md) — `local`, `client`, `cluster` and the master of each
4. [Connection Models](04-connection-models.md) — traditional, Spark Connect and Livy

## Decision

5. [Solutions in Airflow](05-airflow-solutions.md) — one section per solution, with diagram, datasheet (operation, usage, cost, dependencies) and pros and cons; includes [DuckDB](05-airflow-solutions.md#duckdb)
6. [Conclusion](06-conclusion.md) — [decision tree](06-conclusion.md#decision-tree), the common cases and the recommendation for this scenario

## Operation

7. [SparkSession Sizing](07-sessionsizing.md) — memory, threads and the pod `request` in `local` and `client` mode
8. [FAQ](08-faq.md) — the esoteric errors (`OutOfMemoryError`, `Java gateway process exited`, `Answer from Java side is empty`) and where to look for memory bottlenecks

---

[Technical articles index](../README.md)
