# Amazon RDS Migrations: Region, Version and Topology Changes with Minimal Downtime

## Problem
- Databases in the Wrong Place: Some RDS instances ran in a different region from the applications and pipelines that used them, paying inter-region data transfer on every query and adding latency.

- Outdated Engine Versions: Instances ran PostgreSQL and MySQL major versions approaching end of standard support, which means forced upgrades on AWS's schedule and paid Extended Support if nothing is done.

- Topology that No Longer Fit: Instance classes, storage types and Multi-AZ settings chosen years earlier no longer matched the real workload, in both directions — oversized for some databases, missing protection for others.

- Migration Risk: Production databases could not afford long downtime, and previous changes had been done ad hoc, without a rehearsed plan, validation or rollback.

## Solution
- Standard Migration Runbook: Defined one process for every RDS migration — assessment, rehearsal in a non-production copy, replication or snapshot, validation, cutover and rollback plan — so each migration followed known steps instead of being improvised.

- Cross-Region Migration: Moved databases to the region of their consumers using cross-region read replicas (or encrypted snapshot copies for smaller databases), let the replica catch up, then promoted it during a short write freeze and switched applications to the new endpoint, removing inter-region transfer cost.

- Major Version Upgrades with Blue/Green Deployments: Used RDS Blue/Green Deployments to create a synchronized green environment on the new version, ran application tests against it, and switched over in about a minute with the same endpoint names, keeping the blue environment available as a fallback.

- Upgrade Readiness: Checked extensions, deprecated parameters, parameter groups and query plans on the target version before each upgrade, and ran `ANALYZE` after it so the planner had fresh statistics.

- Topology Changes: Changed instance classes to measured CPU and memory usage, moved storage to gp3 with provisioned IOPS only where needed, and set Multi-AZ according to each database's recovery objective, removing it where a single AZ plus backups was enough.

- DMS for Engine or Account Changes: Used AWS DMS full load plus CDC ([DMS ingestion](../data-streaming/cdc-dms.md)) for the cases replicas and Blue/Green cannot cover, such as moving between accounts.

- Connection Endpoints Behind DNS: Pointed applications at Route 53 CNAMEs instead of instance endpoints ([Route 53](../cloud-engineering/aws/route53.md)), so cutovers changed one record instead of every application's configuration.

- Validation and Monitoring: Compared row counts and checksums on critical tables, monitored replica lag, connections and errors in CloudWatch during and after each cutover, and kept final snapshots of the source before decommissioning it.

## Skills
- Databases
- Cloud Engineering
- FinOps
- Site Reliability Engineering

## Tools
- Amazon RDS (PostgreSQL and MySQL)
- RDS Blue/Green Deployments
- RDS Read Replicas and Snapshots
- AWS DMS
- Amazon Route 53
- Amazon CloudWatch
- Terraform
