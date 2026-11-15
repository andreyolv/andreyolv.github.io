---
kind: subpage
---

# Data Platform Roadmap: Medium and Long-Term Planning for Building the Platform

## Context
- A Platform Built on Top of Legacy: The data platform grew from isolated initiatives — databases, EMR clusters, scripts and manually created cloud resources — owned by different people, with no shared foundation for networking, identity, delivery or governance.

- Demand Growing Faster than the Team: More teams needed pipelines, analytics and environments every quarter. Answering each request by hand did not scale, and every new project added more infrastructure to operate.

- Short-Term Work Crowding Out Foundations: Incidents, requests and cost spikes always looked more urgent than the foundations that would prevent them, so the same problems kept returning.

## Objectives
- A secure and reproducible foundation: every resource defined as code, every access through roles and SSO, every network planned.

- One platform for data workloads on Kubernetes, replacing per-project infrastructure.

- Self-service for teams: environments, pipelines and data access without a ticket for each request.

- Governance by default: ownership, lifecycle and cost visible for everything the platform runs.

- A platform whose cost grows slower than its usage.

## Horizons
The roadmap was organized in three horizons. Each horizon depends on the previous one, and items move between horizons as priorities change; the order matters more than the dates.

### Horizon 1 — Foundation (0 to 6 months)
Make what exists safe, known and reproducible before building on it.

- Identity: IAM cleanup, MFA everywhere, workloads on roles and people on SSO ([IAM cleanup](../../cloud-engineering/aws/iam-cleanup.md), [MFA and roles](../../cloud-engineering/aws/iam-mfa-roles.md), [IAM Identity Center](../../cloud-engineering/aws/iam-identity-center.md)).

- Audit and guardrails: organization CloudTrail and Service Control Policies ([CloudTrail](../../cloud-engineering/aws/cloudtrail.md), [SCP](../../cloud-engineering/aws/scp.md)).

- Infrastructure as code: legacy Terraform refactored and every change through a pipeline ([IaC refactoring](../../cloud-engineering/iac-legacy-refactor.md), [Terraform CI/CD](../../devops/cicd-terraform.md)).

- Standards: mandatory tags, naming and ownership ([tag policy](../../cloud-engineering/tag-policy.md)).

- Visibility: cost per project and per resource, security findings triaged ([FinOps strategy](finops-strategy.md), [security findings remediation](../../security/security-findings-remediation.md)).

- Hygiene: removal of legacy and unused resources so the next horizons start from a known inventory ([resource decommissioning](../../finops/resource-reclamation.md), [network hygiene](../../cloud-engineering/aws/network-cleanup.md)).

### Horizon 2 — Platform (6 to 12 months)
Consolidate data workloads on one Kubernetes-based platform, operated through GitOps.

- Kubernetes platform: EKS with node pools by criticality, GitOps with Flux and policies as code ([EKS](../../cloud-engineering/aws/eks.md), [node pools](../../site-reliability-engineering/node-pools.md), [GitOps](../../platform-engineering/gitops.md), [Kyverno](../../security/kyverno.md)).

- Data engines on the platform: Airflow, Spark, Trino and Kafka on Kubernetes ([Airflow](../../data-engineering/airflow.md), [Spark](../../data-engineering/spark-k8s.md), [Trino](../../data-engineering/trino.md), [Kafka](../../data-streaming/kafka-k8s.md)).

- Lakehouse: Iceberg as the table standard with a governed catalog and permissions ([Iceberg](../../data-governance/iceberg.md), [Lake Formation](../../data-governance/lake-formation.md)).

- Ingestion: managed CDC and continuous pipelines replacing batch extracts ([DMS](../../data-streaming/cdc-dms.md), [Spark Declarative Pipelines](../../data-streaming/spark-declarative-pipelines.md)).

- Operations: observability, alerting and standard failure notifications ([metrics](../../observability/metrics.md), [Alertmanager](../../observability/alertmanager.md), [Airflow notifications](../../data-engineering/airflow-failure-notifications.md)).

- Delivery: self-hosted multi-architecture CI and reusable workflows ([self-hosted runners](../../devops/self-hosted-actions.md), [multi-arch builds](../../devops/multi-arch-builds.md), [reusable workflows](../../devops/actions-centralization.md)).

### Horizon 3 — Self-Service and Scale (12 to 24 months)
Let teams use the platform without the platform team in the loop, and prepare it to grow.

- Self-service: internal developer portal, service catalog and infrastructure through platform APIs ([Backstage](../../platform-engineering/idp-backstage.md), [service catalog](../documentation/service-catalog.md), [Crossplane](../../platform-engineering/crossplane.md)).

- Environments on demand: preview environments and isolated clusters for teams ([preview environments](../../platform-engineering/preview-environments.md), [vCluster](../../platform-engineering/vcluster.md)).

- Data governance at scale: catalog, ownership, contracts, quality and lineage ([OpenMetadata](../../data-governance/openmetadata.md), [Glue metadata and ownership](../../data-governance/glue-metadata-owner.md), [data contracts](../../data-governance/data-contract.md), [data quality](../../data-governance/data-quality.md)).

- Network for growth: multi-account hub-and-spoke architecture ready for Transit Gateway ([network architecture](../../cloud-engineering/aws/network-transit-gateway.md)).

- Modernization: EMR workloads evaluated for Spark on Kubernetes ([EMR on EKS](../../cloud-engineering/aws/emr-k8s.md)).

- Reliability: service levels, high availability and disaster recovery for the platform itself ([service levels](../../site-reliability-engineering/service-level.md), [disaster recovery](../../site-reliability-engineering/disaster-recovery.md)).

## Prioritization Criteria
- Risk first: security and audit gaps are fixed before new capabilities are built on top of them.

- Foundations before features: nothing in a later horizon starts while what it depends on is still manual or unknown.

- Leverage: items that remove a recurring request or a recurring incident for many teams come before items that help one team.

- Cost of delay: items whose cost grows every month (legacy resources, inefficient workloads) are pulled forward.

- Reversibility: decisions that are hard to undo (network addressing, table format, identity model) are made early and deliberately; easy ones are deferred until they are needed.

## Execution and Governance
- The roadmap is broken into epics and sprint items on [GitHub Projects](../projects/github-projects.md), so every horizon item traces to delivered issues and pull requests.

- Reviewed every quarter: horizons are re-prioritized with stakeholders, delivered items are linked to their project documentation, and items that lost relevance are dropped explicitly instead of lingering.

- Architecture decisions taken along the way are recorded as ADRs next to the projects that implement them.

## Risks
- Urgent work consuming the roadmap: mitigated by reserving capacity for roadmap items in every sprint, separate from operations and support.

- Adoption: a platform nobody migrates to is cost without value; each capability ships with documentation, templates and migration support for the first teams.

- Dependency on few people: knowledge transfer, runbooks and code review across the team are part of the definition of done.

- Overbuilding: capabilities are built when there is demand from more than one team, not in anticipation.

## Skills
- Platform Strategy

- Technical Planning and Roadmapping

- Cloud Architecture

- Stakeholder Management

## Tools
- Terraform

- Kubernetes

- Flux

- Airflow

- Spark

- Trino
