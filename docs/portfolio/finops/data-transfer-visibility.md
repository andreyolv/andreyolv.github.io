---
status: active
environment: production
kind: project
---

# AWS Data Transfer Cost Visibility and Reduction with CUR Data Exports

## Problem
- The Least Understood Line in the Bill: Data transfer is spread across services and usage types — cross-AZ, inter-region, internet egress, NAT Gateway processing, VPC endpoints, load balancers — and shows up in Cost Explorer mostly as EC2-Other, without saying which workload moved the data or where it went.

- No Owner for Network Cost: Because transfer is billed to the resource that sends or receives bytes, not to the application that caused it, no team saw network cost as theirs and nobody prioritized reducing it.

- Architecture Decisions Made Blind: Choices such as Multi-AZ databases, nodes spread across zones, a database in a different region from its consumers or data lake traffic through NAT were made without knowing their transfer cost, and the cost only appeared on the invoice.

- Console Views Too Coarse: Cost Explorer grouping by usage type showed that data transfer was growing, but not the source and destination regions, the resource, or the direction of the traffic needed to act.

## Solution
- CUR Data Export to S3: Enabled the AWS Cost and Usage Report through Data Exports with resource IDs, delivered as Parquet to S3 and partitioned by billing period, and exposed it as a table in the Glue catalog for Athena.

- Data Transfer Classification: Built Athena views that classify every data transfer line item by `line_item_usage_type`, `product_from_location` / `product_to_location` and `product_transfer_type` into clear categories — intra-region cross-AZ (`DataTransfer-Regional-Bytes`), inter-region, internet egress, NAT Gateway processing (`NatGateway-Bytes`), VPC endpoint and load balancer processing.

- Attribution to Resources and Projects: Joined the transfer cost with resource IDs and the `team` and `project` cost allocation tags ([tag policy](../cloud-engineering/tag-policy.md)), and with Kubernetes namespaces from [OpenCost](opencost.md), so each category points to a resource, a project and an owner.

- Data Transfer Dashboard: Published a dashboard with transfer cost by category, service, source and destination region, resource and project, with daily trends, so a new pipeline that starts moving data across zones or regions is visible within days instead of at the end of the month.

- Reduction Actions Driven by the Data: The breakdown turned into concrete actions, each one measured in the same views before and after:
  - [VPC gateway endpoints for S3 and DynamoDB](vpc-gateway-endpoints.md) to take data lake traffic off the NAT Gateway.

  - A database moved to the region of its consumers to remove inter-region transfer.

  - Multi-AZ removed from databases where the recovery objective allowed it.

  - EKS nodes kept in a single availability zone for data platform workloads to avoid cross-AZ traffic between Spark, Trino, Kafka and storage.

  - Legacy network components removed ([resource decommissioning](resource-reclamation.md)).

- Architecture Review Input: Made the expected data transfer cost part of design reviews — zone placement, region choice, NAT versus endpoints, replication — using the dashboard as the reference for what each pattern costs.

- Continuous Monitoring: Added data transfer categories to [budget alerts](budges-alerts.md) and to the monthly FinOps review in the [cost optimization program](aws-cost-optimization-program.md).

## Skills
- FinOps

- Cloud Networking

- Cloud Engineering

- Data Engineering

## Tools
- AWS Data Exports (Cost and Usage Report)

- Amazon S3

- AWS Glue Data Catalog

- Amazon Athena

- Amazon QuickSight

- OpenCost
