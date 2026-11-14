# PostgreSQL and MySQL Ingestion into the Data Lake with AWS DMS Full Load and CDC

## Problem
- Batch Extracts Overloading Production: Operational PostgreSQL and MySQL databases were extracted with full-table queries on a schedule, putting read load on production systems, taking longer as tables grew and delivering data hours old.

- Deletes and Updates Lost: Query-based extraction depends on an `updated_at` column that many tables did not have or did not maintain, and it never sees deleted rows, so the data lake drifted from the source.

- Custom Extraction Code per Source: Each source had its own scripts for connections, pagination, type mapping and retries, which broke on schema changes and had to be maintained by hand.

- No Managed Option for Simple Replication: For sources that only needed to land in S3, running and operating a Kafka and Debezium stack was more infrastructure than the use case justified.

## Solution
- AWS DMS as the Managed Ingestion Layer: Adopted AWS Database Migration Service to replicate PostgreSQL and MySQL databases into the S3 data lake, with no connector cluster to operate, using a [Debezium and Kafka](cdc-debezium.md) pipeline only where real-time streaming to several consumers was required.

- Full Load plus Ongoing CDC: Configured replication tasks as full load followed by change data capture from the database transaction log, so the initial snapshot and every later insert, update and delete arrive in the lake without querying production tables.

- Source Preparation: Prepared each engine for log-based CDC and created a dedicated least-privilege replication user per source:
  - PostgreSQL: logical replication enabled (`rds.logical_replication` / `wal_level = logical`) with DMS reading the WAL through a replication slot, monitored so an idle or failed task does not let the slot retain WAL until the disk fills.

  - MySQL: binary logging in `ROW` format with `binlog_row_image = FULL` and binlog retention long enough to cover task restarts and maintenance windows.

- S3 Target in Parquet: Wrote changes to S3 as Parquet, partitioned by date, with the `Op` column (insert, update, delete) and the commit timestamp on every record, so downstream jobs know the order and the type of each change.

- Merge into Lakehouse Tables: Processed the raw CDC files with Spark into lakehouse tables using `MERGE`, applying deletes and keeping only the latest version of each key, so analytics read a current copy of the source rather than a log of changes.

- Table Mappings and Transformations: Used selection and transformation rules to include only the required schemas and tables, rename objects to the lake's naming standard and drop sensitive columns before they ever reach S3.

- Secure Connectivity and Credentials: Replication instances run in private subnets with access to sources over private networking, source credentials come from AWS Secrets Manager, and DMS writes to S3 through a dedicated IAM role scoped to the target prefix.

- Monitoring and Validation: Monitored task state, CDC source and target latency and errors with CloudWatch metrics and alerts, and used DMS data validation on critical tables to compare row counts and contents between source and target.

- Infrastructure as Code and Sizing: Managed replication instances, endpoints and tasks in Terraform, and sized replication instances to their measured CPU, memory and throughput, resizing oversized instances as part of the [cost optimization program](../finops/aws-cost-optimization-program.md).

## Skills
- Data Engineering

- Data Streaming

- Databases

- Cloud Engineering

- Security

## Tools
- AWS Database Migration Service (DMS)

- PostgreSQL

- MySQL

- Amazon S3

- Apache Spark

- AWS Secrets Manager

- Amazon CloudWatch

- Terraform
