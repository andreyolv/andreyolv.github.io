# Lakehouse Table Lifecycle: Data Retention, Snapshot Expiration and Table Maintenance with Apache Iceberg

## Problem
- Deleted Data That Never Left Storage: Rows and partitions were deleted from Iceberg tables, but every snapshot still referenced the old data files, so storage did not shrink and "deleted" data could still be read through time travel.

- S3 Lifecycle Cannot Manage Tables: Object lifecycle rules do not know which files a table's metadata references. Expiring or archiving files under a table prefix breaks the table, so the retention tools used for plain files could not be used for tables.

- Unbounded History: Tables with frequent appends and upserts accumulated thousands of snapshots and metadata files, with every snapshot pinning its own copy of rewritten data.

- Orphaned Files: Failed writes and interrupted jobs left data files that no snapshot referenced, invisible to the table and still billed.

- Personal Data Retention: Removing a person's data had to remove it physically from storage, not only from the current version of the table.

## Solution
- Retention Defined per Table: Defined with the data owners, for every table, how long its data is kept (row or partition retention) and how long its history is kept (time-travel window), by data layer — short history on raw and staging tables with heavy writes, longer on curated tables used for audits and reproducibility.

- Data Retention through the Table: Implemented data retention with SQL against the table — `DELETE` of partitions or rows older than the retention period — instead of deleting files. When the predicate matches whole partitions, the delete is a metadata-only operation.

- Snapshot Expiration: Scheduled `expire_snapshots` per table with its time-travel window and a minimum number of snapshots to keep (`history.expire.max-snapshot-age-ms`, `history.expire.min-snapshots-to-keep`), which is the step that physically deletes data files no longer referenced by any remaining snapshot.

- Metadata File Cleanup: Enabled `write.metadata.delete-after-commit.enabled` with a limit on previous metadata versions, so metadata JSON files do not grow without bound.

- Orphan File Removal: Scheduled `remove_orphan_files` with an age threshold longer than the longest running write, so files from failed jobs are removed without risking files of a commit in progress.

- Compaction and Manifest Rewrite: Ran `rewrite_data_files` to compact small files and apply merge-on-read delete files, and `rewrite_manifests` to keep planning fast ([small files](../data-engineering/small-files.md)). Compaction runs before expiration, so the files it replaces are cleaned up in the same cycle.

- Physical Deletion of Personal Data: Defined the purge sequence for personal data as `DELETE`, then compaction to rewrite files that still contain the rows under merge-on-read, then snapshot expiration, so the data is gone from storage and from time travel within a known period.

- Maintenance Driven by Table Health: Scheduled the procedures according to each table's state measured from Iceberg metadata ([lakehouse health monitoring](lakehouse-monitoring.md)) instead of running everything on every table at the same cadence.

- Boundary with Object Lifecycle: Table prefixes are excluded from S3 expiration and transition rules, which remain in charge of plain files only ([S3 object lifecycle](data-lifecycle.md)). The only S3 rules on table prefixes are the ones that never touch referenced data — aborting incomplete multipart uploads and expiring noncurrent versions.

## Skills
- Data Governance

- Data Engineering

- FinOps

## Tools
- Apache Iceberg (expire_snapshots, remove_orphan_files, rewrite_data_files, rewrite_manifests)

- Apache Spark

- Trino

- Amazon S3

- Apache Airflow
