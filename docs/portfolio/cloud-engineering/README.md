---
kind: index
---

# Cloud Engineering

Cloud infrastructure, governance, and networking across AWS and Azure. This area covers Infrastructure as Code (IaC), account organization, networking, identity, and cost guardrails for cloud environments.

## AWS

- [TLS Certificate Management for AWS Services with AWS Certificate Manager](aws/acm.md)
- [Private Amazon API Gateway with VPC Endpoint and Private DNS](aws/api-gateway-private.md)
- [Athena Cost Attribution by IAM Role, User and QuickSight Dataset with CloudTrail](aws/athena.md)
- [Centralized AWS API Auditing and Investigation with CloudTrail and Athena](aws/cloudtrail.md)
- [Shared Storage for Airflow & OpenMetadata via Amazon EFS](aws/efs.md)
- [Kubernetes Cluster Provisioning in Cloud Environments](aws/eks.md)
- [Cost-Resilient EMR Clusters with Instance Fleets and Spot Diversification](aws/emr-fleet.md)
- [EMR on EKS](aws/emr-k8s.md)
- [Scalable Event-Driven Architecture for Data Enrichment and Integration](aws/event-driven-enrichment.md)
- [AWS IAM Cleanup, Organization and Governance: Unused Access Removal and Ownership](aws/iam-cleanup.md)
- [AWS IAM Governance: Tag-Based Access Control (ABAC) & Security Enforcement](aws/iam-core.md)
- [Centralized Human Access to AWS with IAM Identity Center Single Sign-On](aws/iam-identity-center.md)
- [AWS IAM Hardening: MFA Enforcement and Role-Based Workloads without Personal Credentials](aws/iam-mfa-roles.md)
- [AWS Credential Governance and Standardization](aws/iam-security.md)
- [Cloud Network Architecture for Kubernetes Clusters](aws/network.md)
- [AWS Network Hygiene: Cleanup of Unused Network Components and Security Groups](aws/network-cleanup.md)
- [Multi-Account AWS Network Architecture Planning Ready for Transit Gateway](aws/network-transit-gateway.md)
- [VPC Peering Cross-Account Connectivity for Data & Tech Networks](aws/peering.md)
- [Provisioning Amazon Redshift Serverless with Public Access Control](aws/redshift.md)
- [Public and Private DNS Management with Amazon Route 53](aws/route53.md)
- [S3 Inventory: Data Lake Audit and Cost Allocation](aws/s3-inventory.md)
- [Secure S3 Bucket Data Sharing via Partner IP Whitelisting](aws/s3-public-audit.md)
- [Preventive Cloud Guardrails Across AWS Accounts with Service Control Policies](aws/scp.md)

## Azure

- [Azure Cost Optimization and Performance Improvement with Azure Advisor](azure/azure-advisor.md)
- [Azure Security Visibility and Response with Microsoft Defender for Cloud](azure/azure-defender.md)
- [Cloud Governance in Azure (Resource Naming, Cost Allocation Tags, and Ownership)](azure/azure-governance.md)
- [Cloud Infrastructure Provisioning](azure/cloud-provisioning.md)
- [Provisioning Azure Databricks with Security Best Practices](azure/databricks.md)
- [Azure Event Hubs for Data Lake Access Auditing](azure/event-hubs.md)
- [Network Security and Private Connectivity with Private Endpoints](azure/private-endpoints.md)

## Cross-Cloud & IaC Foundations

- [Legacy Infrastructure as Code Refactoring and Modernization with Terraform](iac-legacy-refactor.md)
- [Cloud Infrastructure as Code Provisioning with Terraform](iac-terraform.md)
- [Cloud Resource Tag Standardization and Governance](tag-policy.md)
- [Local Multi-Cloud Emulation for AWS, Azure and GCP Development with Floci](floci.md)

---

> **See also:** [Networking](./../network/README.md) for Kubernetes ingress and service mesh, [FinOps](./../finops/README.md) for cloud cost optimization, and [Security](./../security/README.md) for cloud posture and compliance.
