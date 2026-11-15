---
status: active
environment: production
kind: project
---

# Athena Cost Attribution by IAM Role, User and QuickSight Dataset with CloudTrail

## Problem

- Untraceable Cloud Spend: Athena costs were aggregated at the account level, making it impossible to identify which specific team, query, or application was driving the bill.

- Lack of Granular Visibility: Standard AWS Billing logs do not provide the link between a specific SQL execution and the IAM User/Role that triggered it.

- Shared Roles Hiding the Real Consumer: Most queries ran under assumed roles — Airflow workers, BI service roles, SSO permission sets — so even CloudTrail showed a role session, not the project, person or dashboard behind it.

- BI as a Black Box: QuickSight ran its queries through a single service role, so all BI cost looked like one consumer, with no way to tell which dataset or refresh schedule was expensive.

- Hidden Inefficient Queries: High-cost, unoptimized queries were being executed without accountability, leading to budget overruns.

- Audit Gaps: Difficulty in correlating Athena QueryID with the originating IP or service, complicating security and financial audits.

## Solution
- Query Extraction: Built a scheduled extraction that lists every Athena query execution per workgroup through the Athena API (`ListQueryExecutions` / `BatchGetQueryExecution`), with its SQL, state, workgroup, timings and `DataScannedInBytes`, and stores it as a table in the data lake.

- CloudTrail Data Mapping: Integrated AWS CloudTrail logs with Amazon Athena to capture StartQueryExecution events and extract the metadata of every request.

- Query-to-Principal Correlation: Joined the query history with CloudTrail's `StartQueryExecution` events by query execution ID, mapping every query and every dollar spent to its `userIdentity`.

- Role Session Resolution: Resolved assumed-role sessions to their real owner — per-project Airflow DAG roles to the project and team, IAM Identity Center permission set sessions to the person who signed in, and application roles to their service through role tags — so cost is attributed to projects and people, not to generic roles.

- QuickSight Dataset Attribution: Correlated queries made by the QuickSight service role with the dataset definitions and refresh history extracted from the QuickSight API ([QuickSight governance extraction](../../analytics-engineering/quicksight-governance.md)), attributing Athena cost to each dataset and exposing expensive full refreshes and short refresh intervals.

- Automated Cost Dashboarding: Calculated cost from `DataScannedInBytes` (at the $5.00 per TB rate, with the 10 MB minimum per query) to provide daily spending insights per role, project, user and dataset.

- Usage Attribution by Team: Grouped costs by tags and IAM roles, allowing for accurate "Chargeback" or "Showback" reports for different departments.

- Top-Talker Identification: Identified the most expensive queries, users, roles and datasets, enabling targeted optimizations — such as an inefficient monitoring DAG and an unoptimized event ingestion deployment — and the implementation of Athena Workgroups quotas to prevent runaway costs.

- Historical Auditing: Built a long-term cost history repository in S3, allowing the finance team to track spending trends and anomalies over time.

## Skills
- FinOps

- Data Engineering

- Cloud Governance

- Security

## Tools
- Amazon Athena (API and Workgroups)

- AWS CloudTrail

- Amazon QuickSight API

- AWS IAM and IAM Identity Center

- Amazon S3

- Python (boto3)
