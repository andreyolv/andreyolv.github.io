# AWS Data Platform Cost Optimization Program: Visibility, Rightsizing, Decommissioning and Governance

## Problem
- Cost Without Attribution: The AWS bill for the data platform was known only by service. Nobody could say which project, team, pipeline, user or dataset drove S3, Athena, RDS, EMR or network spend, so there was no one to ask for a decision and no way to prioritize.

- Waste Accumulated over Years: Legacy environments, oversized databases, Multi-AZ where it was not required, long snapshot and query-result retention, orphaned datasets and jobs kept running after their purpose ended.

- Expensive Defaults: Data lake traffic paid NAT Gateway processing, Athena workloads scanned far more data than needed, managed services were enabled account-wide without anyone using them, and nothing expired by default.

- One-Off Cost Campaigns: Previous reductions were reactions to a bill spike, without a backlog, without measured results and without the governance that would stop the waste from coming back.

## Solution
Ran cost optimization as a program with a backlog of more than 70 actions across 15 AWS services, each classified by outcome — **saving** (a direct cost reduction), **visibility** (attribution that enables future savings), **governance** (a process that prevents regression) or **delegated** (owned by the consuming team with the evidence attached).

### Visibility first
- Cost per Resource and per Project: Enabled a cost exporter for resource-level AWS cost, and standardized `team` and `project` tags in Terraform ([tag policy](../cloud-engineering/tag-policy.md)), involving the SRE team in tagging existing resources.
- S3: Enabled [S3 Inventory](../cloud-engineering/aws/s3-inventory.md) to map object count against storage per bucket and prefix — the input for [small files](../data-engineering/small-files.md) work — and server access logs on the main buckets to attribute cost to real operations (reads, writes, lists). Mapped the storage cost of the main data lake prefixes against missing cleanup policies.
- Athena: [Cost per user](../cloud-engineering/aws/athena.md) from CloudTrail and cost per BI dataset, which exposed orphaned datasets (no dashboard using them, still refreshing) and datasets on full refresh at short intervals.
- Kubernetes: Cost per namespace with [OpenCost](opencost.md), and one IAM role per Airflow DAG project ([workload identity](../security/workload-identity.md)) for least privilege and per-project attribution.
- Network and Monitoring: Traced NAT Gateway traffic by destination service, which sized the VPC endpoint saving, and used CloudTrail to find an anomaly in `GetMetricData` calls from an external security monitoring integration.
- Cost as a Product: Reported cost per data product, so product owners see what their product costs to run.

### Rightsizing and configuration
- RDS: Resized instances to measured usage, moved a database to the region of its consumers to cut data transfer, changed Multi-AZ to Single-AZ where the recovery objective allowed it, deleted unnecessary snapshots and reduced the data warehouse snapshot retention.
- DMS and EKS: Resized a DMS replication instance and the EKS add-on nodes.
- Athena Workloads: Found a monitoring DAG and an event ingestion deployment querying far more data than needed and optimized both, and cut the metadata-reading cost of the data observability tool by reading Iceberg metadata and the Glue catalog instead of scanning data.
- Retention: Reduced Athena query-result bucket retention from 3 days to 1, reviewed retention on transient buckets, and added lifecycle rules for incomplete multipart uploads.
- Managed Services Nobody Used: Disabled AWS Config and Systems Manager just-in-time node access where they brought no value, and purged unused BI user licences.
- Compute: Graviton nodes on EKS together with the Airflow upgrade ([ARM nodes](arm.md)), KEDA scaling development workloads to zero outside business hours ([KEDA](keda.md)). Spot nodes ([spot](spot.md)) and a single availability zone to avoid cross-AZ data transfer were already in place since the cluster was created.

### Architecture changes
- [VPC Gateway Endpoints for S3 and DynamoDB](vpc-gateway-endpoints.md), removing data lake traffic from the NAT Gateway.
- Airflow shared volumes moved from EFS to S3.
- Event-streaming route reviewed across Firehose, SQS and SNS.
- Modernization of a legacy data pipeline, reducing its S3, EMR and DMS footprint.
- Small files compacted in the main buckets and prefixes.

### Decommissioning
- [Legacy resource decommissioning](resource-reclamation.md): databases of a legacy EKS platform, the legacy data warehouse, a Pentaho (PDI) VM, Glue jobs and crawlers, Step Functions, Kinesis streams and legacy network components.

### Governance
- Data lifecycle policies for the data lake, Athena workgroups split by team, table ownership in the catalog and purge of unnecessary tables, unused DAGs removed, and a product lifecycle process that defines how a data product is deprecated — so decommissioning is planned instead of discovered.
- BI dataset cleanup (orphaned datasets, refresh type and frequency, most expensive queries, purge of unused dashboards) delegated to the BI team with the cost evidence for each item.

### Evaluated, with no action or not yet decided
Documented as decisions rather than dropped: EMR clusters had no room to reduce node count; the EMR log bucket cost could not be reduced without recreating clusters (changing the log level had no effect); Reserved Instances for EC2 and RDS, Intelligent-Tiering on the main buckets and the Amazon Q in QuickSight subscription were evaluated. Running Spark on Kubernetes instead of EMR is being tested as the largest open opportunity.

## Skills
- FinOps
- Cloud Engineering
- Data Engineering
- Cloud Governance

## Tools
- AWS Cost Explorer and Cost and Usage Report
- AWS CloudTrail
- Amazon S3 Inventory and Server Access Logs
- Amazon Athena
- Amazon RDS
- Amazon EMR
- Amazon QuickSight
- Amazon VPC Endpoints
- OpenCost
- KEDA
- Terraform
