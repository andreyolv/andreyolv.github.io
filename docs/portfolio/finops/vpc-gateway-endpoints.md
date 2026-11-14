# NAT Gateway Cost Reduction with VPC Gateway Endpoints for S3 and DynamoDB

## Problem
- Data Lake Traffic Paying NAT Processing: Workloads in private subnets — Spark on EKS and EMR, Airflow tasks, Trino, Kafka Connect and ingestion jobs — read and wrote the data lake in S3 through the NAT Gateway. Every gigabyte was billed as NAT data processing (about $0.045/GB in `us-east-1`), on top of the NAT hourly charge, for traffic that never left AWS.

- Cost That Scales with Data Volume: Data platform workloads move terabytes per day between compute and S3. NAT processing grew with every new pipeline and every backfill, and became one of the largest line items under EC2-Other with no obvious owner.

- Hidden in the Bill: The cost appeared as `NatGateway-Bytes` in the Cost and Usage Report, not as S3 or as the workload that generated it, so teams did not connect their jobs to the NAT bill.

- Unnecessary Internet Path: Traffic to S3 and DynamoDB left the VPC through the NAT Gateway and the Internet Gateway to reach public service endpoints, adding a shared bottleneck, NAT bandwidth limits and a dependency on the NAT's availability zone.

- No Network Control over Data Access: Buckets could be reached from anywhere with valid credentials; there was no way to require that data lake access come from the company's VPCs.

## Solution
- Diagnosis with Billing and Flow Data: Used the Cost and Usage Report (`NatGateway-Bytes` by NAT Gateway) and VPC Flow Logs on the NAT interfaces to identify the destinations of the traffic, confirming that S3 and DynamoDB accounted for most of the processed bytes.

- S3 and DynamoDB Gateway Endpoints: Created VPC gateway endpoints for S3 and DynamoDB in every VPC with private workloads and associated them with all private route tables. Gateway endpoints have no hourly or per-GB charge, so the traffic moved off the NAT Gateway at zero cost.

- Transparent for Applications: The endpoints add a route to the service prefix list (`pl-xxxx`) in the route tables, so the AWS SDKs, Spark's S3A connector, Trino and Airflow kept using the same S3 and DynamoDB addresses with no code or configuration change.

- Endpoint Policies: Attached endpoint policies that allow access only to the organization's buckets and tables (`aws:ResourceOrgID`), so the endpoint cannot be used to copy data to buckets outside the company.

- Bucket Policies Restricted to the VPC: Added `aws:SourceVpce` / `aws:SourceVpc` conditions on sensitive data lake buckets, so data is reachable only from the company's VPCs, with exceptions for the services and roles that legitimately access it from outside.

- Gateway vs Interface Endpoints: Kept gateway endpoints for in-VPC traffic, which is free. Interface endpoints (PrivateLink), billed per hour and per GB, were reserved for the cases gateway endpoints do not cover — access from on-premises over VPN or Direct Connect and from peered or transit-attached VPCs — and for other services such as ECR, STS and CloudWatch only where their NAT traffic justified the cost.

- Infrastructure as Code: Managed the endpoints, route table associations and policies in Terraform as part of the [VPC network module](../cloud-engineering/aws/network.md), so every new VPC gets them by default.

- Cost Tracking: Followed `NatGateway-Bytes` before and after the change in Cost Explorer, and kept a budget alert on NAT processing so a new workload that bypasses the endpoints — such as cross-region S3 access, which gateway endpoints do not cover — is visible quickly.

## Skills
- FinOps

- Cloud Engineering

- Cloud Networking

- Security

## Tools
- Amazon VPC Gateway Endpoints

- AWS NAT Gateway

- Amazon S3

- Amazon DynamoDB

- VPC Flow Logs

- AWS Cost and Usage Report and Cost Explorer

- Terraform
