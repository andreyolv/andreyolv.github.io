# Metadata-Driven Health Monitoring and Maintenance for Iceberg Lakehouse Tables

## Problem
- Maintenance on a Fixed Schedule: Compaction and snapshot expiration ran on every table at the same cadence, wasting compute on healthy tables while degraded ones waited for the next window.

- Small-File Fragmentation: Streaming and frequent micro-batch writes produced thousands of small data files, slowing every query planner and inflating object storage request costs.

- Hidden Storage Cost of Old Snapshots: Snapshots kept alive by tables with upserts silently held several copies of the data, and nobody could say how many bytes the retained history was costing.

- Merge-on-Read Tax: Position delete files accumulated on frequently updated tables, making every read reconcile deletes until query latency degraded noticeably.

- Over-Partitioned Tables Mistaken for Fragmentation: Tables partitioned too finely were repeatedly compacted with no effect, because the real fix was a coarser partition spec, not another rewrite.

- No Evidence that Maintenance Worked: Maintenance jobs ran without measuring their effect, so there was no history showing whether a compaction or expiration actually improved a table.

## Solution
- Health Measured from Iceberg Metadata: Built a collector that reads each table's metadata tables (snapshots, files, partitions, manifests, all_data_files), so measuring a table costs a metadata read regardless of its size.

- Metric-to-Decision Mapping: Defined each metric by the maintenance action it drives — retained bytes and expirable snapshots gate expire_snapshots, compactable files gate rewrite_data_files, delete ratio drives rewrite_position_delete_files, manifest size drives rewrite_manifests, and partition skew flags a partition spec review.

- Health History as an Iceberg Table: Stored one row per table per run in monitoring.table_health, keeping the full history queryable with SQL instead of bounded by a metrics retention window.

- Recommendations Aligned with the Maintenance Policy: The collector only recommends what the maintenance job would actually do, avoiding endless recommendations for snapshots kept on purpose or for small partitions that are not fragmented.

- Automated, Measured Maintenance: A daily job executes the recommended actions and records their effect in monitoring.maintenance_log, so every run can be compared before and after.

- Kubernetes-Native Batch Jobs: Ran collection hourly and maintenance daily as Kubernetes CronJobs, with the Python code shipped as ConfigMaps and the PyIceberg SQL catalog backed by PostgreSQL.

- Production-Grade Supporting Services: Provisioned the catalog database with CloudNativePG, with a generated password rotated weekly through External Secrets and Postgres metrics scraped by Prometheus; MinIO credentials come from OpenBao.

- Reproducible Degradation Scenarios: Created three demo tables, each degraded in a different way (small files and too many manifests from frequent appends, old snapshots holding several times the live data after upserts, and an hourly partition spec that splits data into tiny files), to validate that every rule detects its case and that maintenance resolves it without losing rows.

## Skills
- Data Engineering
- Data Governance
- Lakehouse Architecture
- Platform Engineering
- Observability

## Tools
- Apache Iceberg
- PyIceberg
- DuckDB
- PostgreSQL
- CloudNativePG
- MinIO
- External Secrets
- OpenBao
- Kubernetes
- Prometheus
- Python
