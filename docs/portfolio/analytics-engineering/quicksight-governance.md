# Amazon QuickSight Metadata Extraction for BI Governance and Cost Visibility

## Problem
- No Inventory of the BI Layer: Hundreds of dashboards, analyses and datasets existed in QuickSight with no list of what existed, who owned it, what data it used or whether anyone still opened it.

- Orphaned Datasets Still Running: Datasets no longer used by any dashboard kept refreshing on schedule, querying Athena and consuming SPICE capacity for nobody.

- Expensive Refresh Patterns: Many datasets used full refresh at short intervals where an incremental refresh or a daily schedule would be enough, and their Athena cost was invisible because all queries ran under the QuickSight service role.

- Licences Without Review: Authors and readers kept their licences after they stopped using QuickSight or left the company, and paid add-ons were enabled without knowing who used them.

- No Lineage from Dashboard to Table: When a table changed or was removed, nobody knew which datasets and dashboards would break.

## Solution
- Scheduled Metadata Extraction: Built a scheduled extraction with the QuickSight API (`ListDashboards`, `DescribeDashboard`, `ListDataSets`, `DescribeDataSet`, `ListIngestions`, `ListUsers` and permissions) that stores the full inventory of dashboards, analyses, datasets, data sources, refresh schedules, ingestion history, users and owners as tables in the data lake.

- Dashboard-to-Dataset-to-Table Lineage: Parsed dashboard and dataset definitions to map which datasets each dashboard uses and which Athena tables or custom SQL each dataset reads, so the impact of changing or removing a table is known in advance.

- Orphaned Dataset Detection: Flagged datasets not referenced by any dashboard or analysis, and dashboards with no recent views, as candidates for removal with their owners.

- Refresh Review: Listed datasets by refresh type (full or incremental), frequency, SPICE size and ingestion duration, so teams could review whether each full refresh and short interval was really needed.

- Cost per Dataset: Joined the dataset and ingestion data with Athena query history and CloudTrail ([Athena cost attribution](../cloud-engineering/aws/athena.md)), giving the Athena cost of each dataset and showing the most expensive dataset queries to optimize.

- Licence Review: Combined users, roles and last activity to find authors and readers who no longer used QuickSight, purged unused users, and evaluated paid add-ons by actual usage.

- Ownership and Governance: Attached an owner and a project to every dashboard and dataset from their permissions and metadata, and handed the review of orphaned datasets, refresh patterns and expensive queries to the BI team with the evidence for each item, with a recurring purge process for unused dashboards and datasets.

- Governance Dashboard: Published the inventory, lineage, cost per dataset and licence usage in a dashboard, so BI governance is reviewed from data instead of opening each asset in the console.

## Skills
- Analytics Engineering

- Data Governance

- FinOps

- Data Engineering

## Tools
- Amazon QuickSight (API, SPICE)

- Amazon Athena

- AWS CloudTrail

- Amazon S3

- Python (boto3)
