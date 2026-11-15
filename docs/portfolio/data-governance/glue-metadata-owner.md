---
status: active
environment: production
kind: project
---

# Glue Data Catalog Metadata Standardization and Table Ownership

## Problem
- Tables Without Context: Thousands of tables in the Glue Data Catalog had no description, no column comments and no indication of what they contained or which pipeline produced them.

- No Owner per Table: When a table broke, was expensive to query or looked unused, there was nobody to ask. Tables accumulated because nobody felt authorized to remove them.

- Catalog Out of Sync with Reality: Tables from removed pipelines and test tables stayed in the catalog, pointing to empty or deleted S3 locations, making discovery harder and searches noisy.

- Governance Tools Without Input: Access control, cost attribution and data catalogs need ownership and classification metadata, and it did not exist in a consistent form.

## Solution
- Metadata Standard: Defined the mandatory metadata for every table — description, owner team, project, data layer, source pipeline and sensitivity — and column comments for business-relevant columns.

- Metadata Stored in Glue: Recorded the standard as Glue table parameters and descriptions, so it lives with the table and is read by Athena, Lake Formation and the data catalog without a separate system.

- Populated from the Pipelines: Pipelines that create or update tables write the metadata as part of their deployment, using the project metadata that [Airflow policies](../data-engineering/airflow-policies.md) already require, so metadata stays correct without manual updates.

- Ownership Backfill: Assigned owners to existing tables using the producing DAG, the S3 prefix ownership and CloudTrail evidence of who writes to each table, and reviewed the result with the teams ([data lake ownership](lake-owner.md)).

- Catalog Cleanup: Identified tables with no queries, no writes, or pointing to empty locations, confirmed with their owners and removed them from the catalog, together with unnecessary Athena tables.

- Used by Governance: The metadata feeds [Lake Formation tags](lake-formation.md) for access control, cost attribution per team in Athena, and the data catalog ([OpenMetadata](openmetadata.md)), so discovery shows each table's owner and context.

- Continuous Checks: A scheduled check reports tables missing mandatory metadata or owner, so gaps are fixed by the owning team instead of accumulating.

## Skills
- Data Governance

- Data Engineering

- Cloud Engineering

## Tools
- AWS Glue Data Catalog

- Amazon Athena

- AWS Lake Formation

- Apache Airflow

- OpenMetadata

- Python (boto3)
