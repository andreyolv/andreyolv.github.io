---
kind: index
---

# AWS

Amazon Web Services infrastructure, governance, networking, identity, and data services. This area covers cloud provisioning, security hardening, cost optimization, and operational guardrails across AWS accounts.

## Certificates & DNS

- [TLS Certificate Management for AWS Services with AWS Certificate Manager](acm.md)
- [Public and Private DNS Management with Amazon Route 53](route53.md)

## API & Eventing

- [Private Amazon API Gateway with VPC Endpoint and Private DNS](api-gateway-private.md)
- [Scalable Event-Driven Architecture for Data Enrichment and Integration](event-driven-enrichment.md)

## Auditing & Cost Attribution

- [Athena Cost Attribution by IAM Role, User and QuickSight Dataset with CloudTrail](athena.md)
- [Centralized AWS API Auditing and Investigation with CloudTrail and Athena](cloudtrail.md)
- [S3 Inventory: Data Lake Audit and Cost Allocation](s3-inventory.md)

## Storage & Shared File Systems

- [Shared Storage for Airflow & OpenMetadata via Amazon EFS](efs.md)
- [Secure S3 Bucket Data Sharing via Partner IP Whitelisting](s3-public-audit.md)

## Kubernetes (EKS)

- [Kubernetes Cluster Provisioning in Cloud Environments](eks.md)
- [EMR on EKS](emr-k8s.md)

## Big Data (EMR)

- [Cost-Resilient EMR Clusters with Instance Fleets and Spot Diversification](emr-fleet.md)
- [Provisioning Amazon Redshift Serverless with Public Access Control](redshift.md)

## Identity & Access Management (IAM)

- [AWS IAM Cleanup, Organization and Governance: Unused Access Removal and Ownership](iam-cleanup.md)
- [AWS IAM Governance: Tag-Based Access Control (ABAC) & Security Enforcement](iam-core.md)
- [Centralized Human Access to AWS with IAM Identity Center Single Sign-On](iam-identity-center.md)
- [AWS IAM Hardening: MFA Enforcement and Role-Based Workloads without Personal Credentials](iam-mfa-roles.md)
- [AWS Credential Governance and Standardization](iam-security.md)

## Networking

- [Cloud Network Architecture for Kubernetes Clusters](network.md)
- [AWS Network Hygiene: Cleanup of Unused Network Components and Security Groups](network-cleanup.md)
- [Multi-Account AWS Network Architecture Planning Ready for Transit Gateway](network-transit-gateway.md)
- [VPC Peering Cross-Account Connectivity for Data & Tech Networks](peering.md)

## Guardrails & Governance

- [Preventive Cloud Guardrails Across AWS Accounts with Service Control Policies](scp.md)

---

> **See also:** [Azure](../azure/README.md) for Azure cloud projects, [Cloud Engineering](../README.md) for the parent overview, [FinOps](../../finops/README.md) for cloud cost optimization, and [Security](../../security/README.md) for cloud posture and compliance.
