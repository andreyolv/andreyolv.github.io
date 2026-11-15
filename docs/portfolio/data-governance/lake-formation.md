---
status: active
environment: production
kind: project
---

# Centralized Data Lake Permissions with AWS Lake Formation

## Problem
- Access Controlled through S3 and IAM Policies: Data lake access was granted with IAM policies on bucket prefixes. Policies grew with every new table and team, were hard to review, and could only express access to files, not to databases, tables or columns.

- All or Nothing per Table: Anyone who could read a table's prefix could read every column and every row, so sensitive columns (personal data, financial values) were either exposed or copied into separate sanitized tables that had to be maintained.

- Permissions Different in Every Engine: Athena, Glue jobs, EMR and the BI tool each relied on their own credentials and policies, so the same user could see different data depending on the tool, and nobody had a single answer to "who can read this table?".

- Hard to Audit and to Delegate: Reviewing access meant reading IAM policies across roles, and every request for access to a table needed the platform team to edit a policy.

## Solution
- Lake Formation as the Permission Layer: Registered the data lake S3 locations in AWS Lake Formation and moved authorization from S3 prefix policies to Lake Formation grants on Glue Data Catalog databases and tables, enforced for Athena, Glue, EMR and Redshift Spectrum.

- Hybrid Migration without Downtime: Migrated database by database, using hybrid access mode so existing IAM-based access kept working while Lake Formation grants were added and validated, and only then removing the broad S3 permissions and the `IAMAllowedPrincipals` default grants.

- Column and Row Level Security: Used Lake Formation data filters to hide sensitive columns and restrict rows per consumer, replacing sanitized copies of tables ([column-level security](column-level-security.md)).

- Tag-Based Access Control (LF-TBAC): Defined LF-Tags for domain, data layer (raw, trusted, refined) and sensitivity, assigned them to databases, tables and columns, and granted access by tag expression to roles and groups, so new tables inherit permissions from their tags instead of needing new grants.

- Access by Role, Not by Person: Granted permissions to IAM roles per team and per workload — including the [per-project roles of Airflow DAGs](../platform-engineering/terraform-module.md) and the users federated through [IAM Identity Center](../cloud-engineering/aws/iam-identity-center.md) — never to individual users.

- Delegated Administration: Made data domain owners Lake Formation administrators for their own databases with grantable permissions, so access requests are approved by the people who own the data rather than by the platform team.

- Cross-Account Sharing: Shared catalog resources with other accounts through Lake Formation and AWS RAM instead of bucket policies, keeping a single copy of the data and the permissions in one place.

- Auditing: Lake Formation and CloudTrail record every grant, revoke and data access request, giving a reviewable answer to who can access each table and who actually did ([data lake access auditing](lake-audience.md)).

- Permissions as Code: Managed LF-Tags, tag assignments, data filters and grants in Terraform, so access changes go through pull request review and are versioned.

## Skills
- Data Governance

- Security

- Data Engineering

- Cloud Engineering

## Tools
- AWS Lake Formation

- AWS Glue Data Catalog

- Amazon Athena

- Amazon EMR

- AWS RAM

- AWS CloudTrail

- Terraform
