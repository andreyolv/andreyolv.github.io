# Data Platform Portfolio

Projects and professional experience in platform, data and cloud engineering, organized by
discipline.

Project pages can carry a lifecycle status (`Active`, `POC`, `Deprecated`, `Planned`) and,
when applicable, an environment (`Production`, `Non-production`, `Local`). Use
[Categories](categories.md) to browse by discipline and
[Projects by Status](catalog.md) to filter across all disciplines.
The Network section is the first pilot.

As a living portfolio, it is expected to be continuously reviewed, refined, and naturally evolved over time.

For the documentation structure and writing conventions used in this repository, see [docs-standard.md](docs-standard.md).

## Summary
- [AI](#ai)
- [Analytics Engineering](#analytics-engineering)
- [Cloud](#cloud)
- [Data Engineering](#data-engineering)
- [Data Governance](#data-governance)
- [Data Streaming](#data-streaming)
- [Databases](#databases)
- [DevOps](#devops)
- [FinOps](#finops)
- [Management](#management)
- [MLOps](#mlops)
- [Network](#network)
- [Observability](#observability)
- [Platform Engineering](#platform-engineering)
- [Security](#security)
- [Site Reliability Engineering](#site-reliability-engineering)
- [Software Engineering](#software-engineering)

---

## AI
- [AI-Native Development with OpenCode as an AI IDE](ai/opencode-ai-ide.md)
- [Self-Hosted LLM Inference on Kubernetes with llmkube and llama.cpp](ai/llmkube.md)
- [Local LLM Inference with llama.cpp on Constrained Hardware](ai/local-llama-cpp.md)
- [Centralized Pipeline Management and Execution with MCPServer](ai/mcpserver.md)

---

## Analytics Engineering
- [Data Ingestion with Airbyte for Small Distributed Teams](analytics-engineering/airbyte.md)
- [Orchestrated dbt Transformations with Airflow on Kubernetes](analytics-engineering/dbt.md)
- [Lightweight Cost-Effective Data Processing for Analytics with DuckDB](analytics-engineering/duckdb.md)
- [Cost-Effective Open-Source Data Visualization with Metabase](analytics-engineering/metabase.md)
- [Amazon QuickSight Metadata Extraction for BI Governance and Cost Visibility](analytics-engineering/quicksight-governance.md)

---

## Cloud
- [Legacy Infrastructure as Code Refactoring and Modernization with Terraform](cloud-engineering/iac-legacy-refactor.md)
- [Cloud Infrastructure as Code Provisioning with Terraform](cloud-engineering/iac-terraform.md)
- [Cloud Resource Tag Standardization and Governance](cloud-engineering/tag-policy.md)
- [Local Multi-Cloud Emulation for AWS, Azure and GCP Development with Floci](cloud-engineering/floci.md)

### Azure
- [Azure Cost Optimization and Performance Improvement with Azure Advisor](cloud-engineering/azure/azure-advisor.md)
- [Azure Security Visibility and Response with Microsoft Defender for Cloud](cloud-engineering/azure/azure-defender.md)
- [Cloud Governance in Azure (Resource Naming, Cost Allocation Tags, and Ownership)](cloud-engineering/azure/azure-governance.md)
- [Cloud Infrastructure Provisioning](cloud-engineering/azure/cloud-provisioning.md)
- [Provisioning Azure Databricks with Security Best Practices](cloud-engineering/azure/databricks.md)
- [Azure Event Hubs for Data Lake Access Auditing](cloud-engineering/azure/event-hubs.md)
- [Network Security and Private Connectivity with Private Endpoints](cloud-engineering/azure/private-endpoints.md)

### AWS
- [TLS Certificate Management for AWS Services with AWS Certificate Manager](cloud-engineering/aws/acm.md)
- [Private Amazon API Gateway with VPC Endpoint and Private DNS](cloud-engineering/aws/api-gateway-private.md)
- [Athena Cost Attribution by IAM Role, User and QuickSight Dataset with CloudTrail](cloud-engineering/aws/athena.md)
- [Centralized AWS API Auditing and Investigation with CloudTrail and Athena](cloud-engineering/aws/cloudtrail.md)
- [Shared Storage for Airflow & OpenMetadata via Amazon EFS](cloud-engineering/aws/efs.md)
- [Kubernetes Cluster Provisioning in Cloud Environments](cloud-engineering/aws/eks.md)
- [Cost-Resilient EMR Clusters with Instance Fleets and Spot Diversification](cloud-engineering/aws/emr-fleet.md)
- [EMR on EKS](cloud-engineering/aws/emr-k8s.md)
- [Scalable Event-Driven Architecture for Data Enrichment and Integration](cloud-engineering/aws/event-driven-enrichment.md)
- [AWS IAM Cleanup, Organization and Governance: Unused Access Removal and Ownership](cloud-engineering/aws/iam-cleanup.md)
- [AWS IAM Governance: Tag-Based Access Control (ABAC) & Security Enforcement](cloud-engineering/aws/iam-core.md)
- [Centralized Human Access to AWS with IAM Identity Center Single Sign-On](cloud-engineering/aws/iam-identity-center.md)
- [AWS IAM Hardening: MFA Enforcement and Role-Based Workloads without Personal Credentials](cloud-engineering/aws/iam-mfa-roles.md)
- [AWS Credential Governance and Standardization](cloud-engineering/aws/iam-security.md)
- [Cloud Network Architecture for Kubernetes Clusters](cloud-engineering/aws/network.md)
- [AWS Network Hygiene: Cleanup of Unused Network Components and Security Groups](cloud-engineering/aws/network-cleanup.md)
- [Multi-Account AWS Network Architecture Planning Ready for Transit Gateway](cloud-engineering/aws/network-transit-gateway.md)
- [VPC Peering Cross-Account Connectivity for Data & Tech Networks](cloud-engineering/aws/peering.md)
- [Provisioning Amazon Redshift Serverless with Public Access Control](cloud-engineering/aws/redshift.md)
- [Public and Private DNS Management with Amazon Route 53](cloud-engineering/aws/route53.md)
- [S3 Inventory: Data Lake Audit and Cost Allocation](cloud-engineering/aws/s3-inventory.md)
- [Secure S3 Bucket Data Sharing via Partner IP Whitelisting](cloud-engineering/aws/s3-public-audit.md)
- [Preventive Cloud Guardrails Across AWS Accounts with Service Control Policies](cloud-engineering/aws/scp.md)

---

## Data Engineering
- [Data Batch Workflow Orchestration with Apache Airflow on Kubernetes](data-engineering/airflow.md)
- [Airflow DAG Cleanup, Organization and Ownership Governance](data-engineering/airflow-dags-cleanup.md)
- [Standardized Airflow Failure Notifications through Cluster Policy Mutation](data-engineering/airflow-failure-notifications.md)
- [Airflow DAG Migration & Pipeline Modernization](data-engineering/airflow-dags-migration.md)
- [Airflow DAGs Quality and Governance Policies](data-engineering/airflow-policies.md)
- [Small Files Monitoring and Optimization for Data Lakes Cost Performance](data-engineering/small-files.md)
- [Scalable Big Data Processing Batch Workloads on Kubernetes with Apache Spark](data-engineering/spark-k8s.md)
- [Centralized Query Routing Across Multiple Trino Clusters with Trino Gateway](data-engineering/trino-gateway.md)
- [Distributed Analytics Query Engine with Trino on Kubernetes](data-engineering/trino.md)

---

## Data Governance
- [Column-Level Security for Fine-Grained Data Access Control](data-governance/column-level-security.md)
- [Data Catalog GitHub Abstraction Layer](data-governance/data-catalog-agnostic.md)
- [Data Catalog & Data Governance with OpenMetadata](data-governance/data-catalog.md)
- [Data Contracts for Reliable and Scalable Data Products](data-governance/data-contract.md)
- [Data Lake Governance Standardization](data-governance/data-lake-governance.md)
- [S3 Object Lifecycle for the Data Lake: Retention, Storage Classes and Expiration Rules](data-governance/data-lifecycle.md)
- [Data Lineage for End-to-End Data Visibility and Governance](data-governance/data-lineage.md)
- [Standardization of Data Products for Scalable Analytics Platforms](data-governance/data-products.md)
- [Data Quality Management and Monitoring for Analytics Platforms](data-governance/data-quality.md)
- [Glue Data Catalog Metadata Standardization and Table Ownership](data-governance/glue-metadata-owner.md)
- [Standardization of Apache Iceberg Table Format for Lakehouse](data-governance/iceberg.md)
- [Lakehouse Table Lifecycle: Data Retention, Snapshot Expiration and Table Maintenance with Apache Iceberg](data-governance/lakehouse-lifecycle.md)
- [Metadata-Driven Health Monitoring and Maintenance for Iceberg Lakehouse Tables](data-governance/lakehouse-monitoring.md)
- [DataLake Access Auditing and Governance](data-governance/lake-audience.md)
- [Centralized Data Lake Permissions with AWS Lake Formation](data-governance/lake-formation.md)
- [Data Lake Ownership and Accountability Framework](data-governance/lake-owner.md)
- [Data Lake Policy Lifecycle Management](data-governance/lake-policy-lifecycle.md)
- [REST Iceberg Metadata Catalog with Lakekeeper](data-governance/lakekeeper.md)
- [Unified Metadata Management for Data Products](data-governance/metadata.md)
- [Data Governance and Data Metadata Platform with OpenMetadata](data-governance/openmetadata.md)

---

## Data Streaming
- [Real-Time SQL Server Data Ingestion with Debezium Change Data Capture](data-streaming/cdc-debezium.md)
- [PostgreSQL and MySQL Ingestion into the Data Lake with AWS DMS Full Load and CDC](data-streaming/cdc-dms.md)
- [Real-Time Data Streaming with Confluent Cloud](data-streaming/confluent.md)
- [Kafka to Delta Lakehouse: Real-Time Data Ingestion with PySpark Consumer](data-streaming/consumer-delta.md)
- [Streaming Data Ingestion from Kafka into Iceberg Lakehouse with Kafka Connect](data-streaming/consumer-iceberg.md)
- [Real Time Streaming Processing on Kubernetes with Apache Flink](data-streaming/flink.md)
- [Event Streaming Platform on Kubernetes with Apache Kafka and Strimzi](data-streaming/kafka-k8s.md)
- [Spark Streaming for Temporal Data Lake Access Auditing](data-streaming/lake-logs-processing.md)
- [Continuous Data Ingestion into the Lakehouse with Spark Declarative Pipelines](data-streaming/spark-declarative-pipelines.md)
- [Direct Database CDC to Iceberg Lakehouse without Kafka using OLake](data-streaming/olake.md)
- [Real-Time User-Facing Analytics with StarRocks](data-streaming/user-facing-analytics.md)

---

## Databases
- [PostgreSQL on Kubernetes with CloudNativePG](databases/cnpg.md)
- [Declarative PostgreSQL Operations with Crossplane SQL Provider](databases/db-gitops-manage.md)
- [Standardized MongoDB Deployment on Kubernetes](databases/mongo.md)
- [Standardized Neo4j Database Deployment on Kubernetes](databases/neo4j.md)
- [Performance Dashboard Monitoring for Postgres](databases/pghero.md)
- [PostgreSQL Database Migration Process on Kubernetes](databases/postgres-migration.md)
- [Amazon RDS Migrations: Region, Version and Topology Changes with Minimal Downtime](databases/rds-migration.md)
- [Standardized Redis Deployment on Kubernetes](databases/redis.md)
- [SQL Exporter for Prometheus Metrics](databases/sql-exporter.md)

---

## DevOps
- [Static Validation of GitHub Actions Workflows with actionlint](devops/actionlint.md)
- [Reusable GitHub Actions Workflow Templates for Multi-Repository CI/CD Projects](devops/actions-centralization.md)
- [Automated Infrastructure Terraform Deployment with Github Actions](devops/cicd-terraform.md)
- [CI/CD Pipelines for Airflow Projects: DAG Code Releases and Image Build with GitHub Actions](devops/cicd-airflow.md)
- [Container Registry Insights and Image Lifecycle Management](devops/container-registry.md)
- [Airflow DAG Quality Assurance in CI/CD with Custom GitHub Action](devops/custom-action.md)
- [Automated Lambda Deployment via GitHub Actions](devops/cicd-lambda.md)
- [Descheduler of Airflow Stuck Pods for Kubernetes Resource and Cost Optimization](devops/descheduler.md)
- [Declarative Linux Package Management with Devbox and Nix](devops/devbox.md)
- [Automated Documentation Updates from Github to Confluence with Github Actions](devops/doc-confluence-action.md)
- [Kubernetes Image Update Automation with Flux](devops/flux-image-update.md)
- [Kubernetes Manifest and CRD Validation in CI with flux-schema](devops/flux-schema.md)
- [GitHub Administration and Security Governance](devops/github-admin.md)
- [GitHub Organization Cleanup: Repository Archiving, Ownership and Access Governance](devops/github-repos-cleanup.md)
- [Software Development Productivity with GitHub Copilot](devops/github-copilot.md)
- [GitHub Repository Standardization as Code with Terraform](devops/github-repos-terraform.md)
- [Github Repository Governance and Compliance with GitHub Rulesets](devops/github-rulesets.md)
- [Automated Release Versioning with GitHub Pull Requests](devops/github-versioning.md)
- [Standardized Technical Documentation Git-Integrated with MkDocs](devops/mkdocs.md)
- [Multi-Architecture Container Builds with GitHub Actions on Self-Hosted Runners](devops/multi-arch-builds.md)
- [Pull Request Template Standardization](devops/pullrequest-template.md)
- [Automated Pod Rollouts Triggered by ConfigMap and Secret Changes](devops/reloader/1-resume.md)
- [GitHub Repository Templating for Automated Project Setup](devops/repositories-templates.md)
- [Self-Hosted GitHub Actions on Kubernetes for Secure CI/CD](devops/self-hosted-actions.md)
- [VSCode Extensions for Consistent Development Environments](devops/vscode-extensions.md)

---

## FinOps
- [AWS Data Platform Cost Optimization Program: Visibility, Rightsizing, Decommissioning and Governance](finops/aws-cost-optimization-program.md)
- [Cost-Effective Kubernetes Compute Optimization with ARM-Based Nodes](finops/arm.md)
- [Budget-Based Cost Alerting and Governance for Cloud & Data Platform](finops/budges-alerts.md)
- [Cloud Cost Savings with SavingPlans & Instance Reservation](finops/cloud-reservations.md)
- [Optimizing Kubernetes Resource Allocation to VMs with Custom Kubernetes Scheduler](finops/custom-kubernetes-scheduler.md)
- [Data Lake Cost Division by Project](finops/datalake-cost-division.md)
- [AWS Data Transfer Cost Visibility and Reduction with CUR Data Exports](finops/data-transfer-visibility.md)
- [Memory & CPU Resources Advisor for Kubernetes Workloads with Grafana Dashboards](finops/grafana-resource-advisor.md)
- [Kubernetes Cost Savings with Dynamic NodePools Autoscaling and Right-Sizing with Karpenter](finops/karpenter.md)
- [Event-Driven Autoscaling in Kubernetes Using KEDA for Resource and Cost Optimization](finops/keda.md)
- [Kubernetes Resource Efficiency Index per Namespace and Workload](finops/kubernetes-efficiency-index.md)
- [Traffic-Based Pod Autoscaling with KubeElasti](finops/kubelasti.md)
- [Scheduled Kubernetes Cluster Shutdown for Cost Optimization](finops/kubernetes-shutdown.md)
- [Kubernetes Cost Allocation by Project with OpenCost](finops/opencost.md)
- [Legacy and Orphaned AWS Resource Decommissioning with AWS Resource Explorer](finops/resource-reclamation.md)
- [Kubernetes Cost Optimization with Spot Instances](finops/spot.md)
- [Dynamic Kubernetes Resource Optimization with Vertical Pod Autoscaler](finops/vpa.md)
- [NAT Gateway Cost Reduction with VPC Gateway Endpoints for S3 and DynamoDB](finops/vpc-gateway-endpoints.md)

---

## Management
- [Data Platform Roadmap: Medium and Long-Term Planning for Building the Platform](management/planning/platform-roadmap.md)
- [FinOps Strategy for the Data Platform: From Visibility to Governed Cost](management/planning/finops-strategy.md)
- [Platform Service Catalog with GitHub Issue Templates and Projects](management/documentation/service-catalog.md)
- [Scrum and Agile Activity Management with GitHub Projects](management/projects/github-projects.md)

---

## MLOps
- [Machine Learning Lifecycle Management with MLflow](mlops/mlflow.md)
- [Interactive Machine Learning Model Deployment with Streamlit](mlops/streamlit.md)

---

## Network
- [Kubernetes Ingress Traffic on AWS with AWS Load Balancer Controller](network/aws-load-balancer-controller.md)
- [Automated DNS Records Management in Kubernetes with ExternalDNS](network/external-dns.md)
- [Kubernetes Network Ingress Traffic with Gateway API and Envoy Gateway](network/gateway-api.md)
- [User Access Audience Monitoring at the Gateway with Envoy Gateway](network/ingress-controller-audience.md)
- [Kubernetes Network Ingress Traffic with NGINX Ingress Controller](network/ingress-controller.md)
- [Kubernetes Service-to-Service Traffic Security and Control with Istio](network/istio.md)
- [Load Balancer for On-Prem Kubernetes with MetalLB](network/metallb.md)
- [Troubleshooting Network Issues in Kubernetes with Netshoot](network/netshoot.md)
- [Network Isolation and Traffic Control in Kubernetes with Network Policies](network/network-policies.md)
- [Granular Access for Ingress Controller via Identity Provider Groups with Pomerium](network/pomerium.md)

---

## Observability
- [Alerting Kubernetes Infrastructure and Critical Applications Issues with Alertmanager](observability/alertmanager.md)
- [Standardized Monitoring and Alerting for Airflow & Kafka Applications](observability/data-platform-applications.md)
- [Data Infrastructure Monitoring with Synthetic Baseline Workload](observability/data-platform-infrastructure.md)
- [AWS Cloud Alerting as Code with Datadog Monitors](observability/datadog-aws-alerts.md)
- [Software Delivery Performance Metrics (DORA) with Apache DevLake](observability/devlake.md)
- [Federated Prometheus for Long-Term Metrics Retention](observability/federated-prometheus.md)
- [Kubernetes Log Collection with Fluent Bit and Loki Ingestion](observability/fluentbit.md)
- [Monitoring Software Delivery and Security Signals using Git Data](observability/git-export.md)
- [Declarative Monitoring and Observability Dashboards with Grafana Operator](observability/grafana.md)
- [Custom Metrics for Crossplane Composite Resources with Kube Metrics Server](observability/kube-metrics-server-custom.md)
- [Kubernetes Security and Compliance with Audit Log](observability/kubernetes-audit-logs.md)
- [Kubernetes Log Centralized Storage with Loki](observability/logs.md)
- [Kubernetes Metrics Collection and Storage with Prometheus](observability/metrics.md)
- [Observability for Kubernetes with OpenTelemetry](observability/open-telemetry.md)
- [Continuous CPU & Memory Profiling using Pyroscope](observability/pyroscope.md)
- [Network Observability in Kubernetes with Retina and Hubble](observability/retina.md)
- [Query Performance Monitoring for Azure Synapse Analytics using a Custom Prometheus Exporter](observability/synapse-prometheus-exporter.md)
- [Long-Term Prometheus Metrics Retention with Thanos](observability/thanos.md)
- [Distributed Tracing of Microservice Request Flows on Kubernetes with Grafana Tempo](observability/tracing.md)
- [AWS Infrastructure Observability with YACE and Prometheus](observability/yace.md)

---

## Platform Engineering
- [Custom Helm Chart for Airflow Deployment Across Multiple Namespaces](platform-engineering/airflow-multinamespace-chart.md)
- [Self-Service Infrastructure Platform Engineering with Crossplane](platform-engineering/crossplane.md)
- [Data Development Environment on Kubernetes with Custom Helm Chart](platform-engineering/dev-env-k8s.md)
- [Cost-Efficient Local Development Environment for Data Engineering Teams](platform-engineering/dev-env-local.md)
- [Automated Version and Digest Updates for Flux OCIRepository Artifacts with Renovate](platform-engineering/flux-ocirepository-updates.md)
- [Multi-Repository GitOps for Safe Team Autonomy in Kubernetes](platform-engineering/gitops-multirepo.md)
- [Declarative GitOps Infrastructure Delivery on Kubernetes with Flux](platform-engineering/gitops.md)
- [User-Friendly Kubernetes UI for Logs and Pod Monitoring with Headlamp](platform-engineering/headlamp.md)
- [Cluster Homepage with Automatic Ingress URL Discovery](platform-engineering/homepage-ingress-discovery.md)
- [Service Catalog and Internal Developer Portal for Kubernetes with Backstage](platform-engineering/idp-backstage.md)
- [Productive Local Kubernetes Cluster with GitOps](platform-engineering/kind-kustomize.md)
- [Ephemeral Pull Request Preview Environments on Kubernetes with Flux ResourceSet](platform-engineering/preview-environments.md)
- [Virtualized Kubernetes Clusters for Multi-Team Isolation with vCluster](platform-engineering/vcluster.md)
- [Terraform Module: Automated IAM for Airflow via EKS Pod Identity](platform-engineering/terraform-module.md)
- [Credential-Free Terraform and OpenTofu Linting in CI with TFLint](platform-engineering/tflint.md)
- [Intelligent Resource Scheduling with Apache YuniKorn on Kubernetes](platform-engineering/yunikorn.md)
- [Custom Kubernetes Operator for Continuous Secret Synchronization with SenhaSegura](platform-engineering/senhasegura-kubernetes-operator.md)

---

## Security
- [Ensuring Trusted Container Images with Cosign and Kyverno](security/cosign.md)
- [Dynamic Application Security Testing (DAST) with ZAP Proxy](security/dast-api.md)
- [Kubernetes Secret Synchronization between Azure Key Vault and External Secrets Operator](security/external-secrets-vault.md)
- [Kubernetes Runtime Threat Detection with Falco](security/falco.md)
- [GitHub Credentials Policy: Authentication Standards & Governance](security/github-credentials.md)
- [Runtime Security for GitHub Actions Runners with Harden-Runner](security/harden-runner.md)
- [Kubernetes Security and Compliance with Kubescape](security/kubescape.md)
- [Security and Compliance Policy as Code for Kubernetes with Kyverno](security/kyverno.md)
- [Rate Limiting in Nginx Ingress Controller for API Security](security/nginx-rate-limit.md)
- [Cloud Security & Compliance Auditing with Prowler](security/prowler.md)
- [Automated Dependency and Supply Chain Updates with Renovate](security/renovate.md)
- [Code Security with SAST Open Source Tools](security/sast-open.md)
- [Code Security with SAST and GitHub Advanced Security](security/sast.md)
- [Software Bill of Materials (SBOM) for Supply Chain Security](security/sbom.md)
- [Remediation of AWS and GitHub Security Findings from Prowler Scans](security/security-findings-remediation.md)
- [Continuous Supply Chain Security Posture Assessment with OpenSSF Scorecard](security/scorecard.md)
- [Encrypted Kubernetes Secrets for GitOps Workflows with Sealed Secrets](security/sealed-secrets.md)
- [Centralizing Authentication Across Data and DevOps Tools with Entra ID Single Sign-On (SSO)](security/sso.md)
- [Automated TLS Certificate Management for Ingress Controller](security/tls-certs.md)
- [Container Vulnerability Scanning and Security Compliance with Trivy](security/trivy.md)
- [Secretless Workload Authentication in Kubernetes with Workload Identity](security/workload-identity.md)
- [Static Application Security Testing for GitHub Actions Workflows with zizmor](security/zizmor.md)

---

## Site Reliability Engineering
- [Resilient Persistent Volume Backup and Recovery for Kubernetes with Velero](site-reliability-engineering/backup-k8s.md)
- [Progressive Canary Deployments in Kubernetes with Flagger](site-reliability-engineering/canary-flagger.md)
- [Kubernetes Resilience using Chaos Engineering Experiments with Litmus](site-reliability-engineering/chaos-engineering.md)
- [Disaster Recovery Strategy for Kubernetes and Cloud Infrastructure](site-reliability-engineering/disaster-recovery.md)
- [Kubernetes High Availability: Topology Spread, Anti-Affinity, and Disruption Budgets](site-reliability-engineering/high-availability.md)
- [Docker Image Internalization from Public Container Registry to Private Container Registry](site-reliability-engineering/image-proxy.md)
- [Kubernetes Node Pools Segmentation by Infrastructure Criticality](site-reliability-engineering/node-pools.md)
- [Cross-Cluster PVC/PV Migration on Kubernetes with Velero](site-reliability-engineering/pvc-cluster-migration.md)
- [Service Level Indicators for Data Platforms on Kubernetes and Cloud](site-reliability-engineering/service-level.md)
- [StorageClass Migration for Persistent Volumes on Kubernetes with Velero](site-reliability-engineering/storageclass-migration.md)
- [Kubernetes & Cloud Tools Lifecycle and Update Management](site-reliability-engineering/update-tools.md)

---

## Software Engineering
- [Managed Package Repository for Internal Libraries and Upstream Caching with AWS CodeArtifact](software-engineering/codeartifact.md)
- [Code Quality Standardization with Linters and Pre-Commit](software-engineering/linters.md)
- [Automated LLM Pull Request Review with Open Code Review and GitHub Actions](software-engineering/open-code-review.md)
- [Python Artifact Repository for Internal Libraries on Kubernetes](software-engineering/python-artifact-repo.md)
- [RabbitMQ Messaging Topology Kubernetes Operator](software-engineering/rabbitmq.md)
- [Python Dependency and Environment Management with UV](software-engineering/uv.md)

---
