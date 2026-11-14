# S3 Object Lifecycle for the Data Lake: Retention, Storage Classes and Expiration Rules

## Problem
- Files Kept Forever by Default: Nothing in the data lake buckets expired. Landing files, intermediate processing outputs, exports, temporary query results and logs accumulated indefinitely, and storage cost grew every month.

- No Retention Rules per Area: Landing, raw files, temporary areas, query results and logs were all treated the same, although their value and the time anyone needs them are very different.

- Hidden Storage: Incomplete multipart uploads and noncurrent object versions consumed storage that did not appear in any listing and that nobody knew about.

- Tables and Files Mixed in the Same Rules: Object lifecycle rules can be safe on plain files and destructive on table storage. Without a clear boundary, a rule written for a bucket could expire or archive files that a lakehouse table still referenced.

## Solution
- Scope: Object Storage, Not Tables: This policy covers data that lives as plain objects in S3 — landing and raw files, temporary and transient areas, exports, query results and logs. Lakehouse tables have their own lifecycle, managed by the table format ([lakehouse table lifecycle](lakehouse-lifecycle.md)).

- Retention Policy by Area: Defined retention per bucket area and data type with the data owners — days for landing, temporary and transient areas, longer for raw files that are the source of truth for reprocessing, according to business and legal needs.

- S3 Lifecycle Rules: Implemented the policy as S3 lifecycle rules per bucket and prefix: expiration of temporary and transient data, and transition of rarely accessed raw files and archives to Infrequent Access and Glacier storage classes.

- Table Prefixes Excluded from Expiration and Transition: Table locations are explicitly left out of every expiration and storage-class transition rule. S3 does not know which files a table's metadata still references, so expiring or archiving them corrupts the table; their retention is done by the table format instead.

- Rules Safe Everywhere: Applied the rules that never remove referenced data to every prefix, tables included — aborting incomplete multipart uploads after a few days, and expiring noncurrent versions where versioning is enabled, so files the table format deletes really leave S3.

- Query Results and Logs: Reduced retention of Athena query-result buckets and set retention for access logs and service logs according to how long they are actually used.

- Intelligent-Tiering Where Access Is Unpredictable: Evaluated S3 Intelligent-Tiering for the main buckets. Its frequent and infrequent access tiers keep objects readable without any change, so it can be used on table prefixes too, while the opt-in archive tiers are never enabled there.

- Visibility to Prioritize: Used [S3 Inventory](../cloud-engineering/aws/s3-inventory.md) and storage cost per prefix to find the largest prefixes without lifecycle rules and to measure the effect of each rule.

- Lifecycle as Code: Managed lifecycle rules in Terraform alongside the buckets, with the retention of each prefix documented next to its owner ([data lake ownership](lake-owner.md)).

## Skills
- Data Governance

- FinOps

- Cloud Engineering

## Tools
- Amazon S3 Lifecycle and Storage Classes

- S3 Intelligent-Tiering

- S3 Inventory

- Amazon Athena

- Terraform
