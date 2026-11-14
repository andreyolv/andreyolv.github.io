# Continuous Data Ingestion into the Lakehouse with Spark Declarative Pipelines

## Problem
- Streaming Jobs Written by Hand: Each continuous ingestion was a Structured Streaming application with its own `readStream`, `writeStream`, trigger, checkpoint path and restart logic. Most of the code was plumbing, repeated in every job with small differences.

- Dependencies Orchestrated Outside the Code: A raw ingestion fed a cleaned table, which fed aggregates. The order between them lived in Airflow DAGs and in people's heads, so a change in one step meant checking every job downstream by hand.

- Fragile Checkpoint Management: Reprocessing a table required finding and deleting the right checkpoint directory and the right data, and a mistake there either duplicated data or silently skipped it.

- Batch and Streaming Written Differently: Incremental tables and periodically recomputed aggregates were built with different APIs and different jobs, although they were parts of the same flow of data.

## Solution
- Spark Declarative Pipelines: Adopted Spark Declarative Pipelines (SDP), the declarative framework in open-source Apache Spark, to define continuous ingestion as datasets and flows instead of streaming jobs. Engineers declare what each table contains; Spark resolves the dependency graph, the execution order, parallelism, checkpoints and retries.

- Streaming Tables for Continuous Ingestion: Defined the ingestion layer as streaming tables (`@dp.table` in Python or `CREATE STREAMING TABLE ... FROM STREAM` in SQL) reading continuously from Kafka topics and from files landing in S3, so only new data is processed on each update.

- Materialized Views for Derived Tables: Defined cleaned, joined and aggregated tables as materialized views (`@dp.materialized_view` / `CREATE MATERIALIZED VIEW`) on top of the streaming tables, kept up to date by the pipeline instead of separate batch jobs.

- Several Sources into One Table: Used append flows (`@dp.append_flow`) to write several sources — for example the same event from different topics or regions — into a single streaming table, without union jobs.

- Pipeline Projects as Code: Each pipeline is a project with a `spark-pipeline.yml` spec (name, source libraries, target catalog and database, checkpoint storage in S3 and Spark configuration) and its transformations in Python or SQL files, versioned and reviewed like any other code.

- Validation Before Running: Ran `spark-pipelines dry-run` in CI on every pull request to catch syntax, analysis and dependency-graph errors without reading or writing data, before anything reaches the cluster.

- Controlled Reprocessing: Replaced manual checkpoint surgery with `spark-pipelines run --full-refresh <datasets>` to recompute specific tables and their state, or `--refresh` to update without clearing data, so reprocessing is one explicit, reviewable command.

- Lakehouse Tables as Target: Wrote streaming tables and materialized views to the lakehouse catalog as Iceberg tables ([Iceberg standard](../data-governance/iceberg.md)), registered in the catalog for Trino and Athena consumers.

- Running on Kubernetes: Pipelines run on Kubernetes with the same Spark images and infrastructure as the [Spark batch workloads](../data-engineering/spark-k8s.md), deployed through the existing CI/CD and monitored with Spark metrics in Prometheus, replacing a set of hand-written streaming consumers ([Kafka to Iceberg](consumer-iceberg.md)).

## Skills
- Data Engineering
- Data Streaming
- Platform Engineering

## Tools
- Apache Spark (Spark Declarative Pipelines, Structured Streaming)
- Apache Kafka
- Apache Iceberg
- Amazon S3
- Kubernetes
- GitHub Actions
