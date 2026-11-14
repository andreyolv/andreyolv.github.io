# FinOps Strategy for the Data Platform: From Visibility to Governed Cost

## Context
- Cost Grew with the Platform: As more teams, pipelines and data moved to the platform, the cloud bill grew every month, and the growth could not be explained by service, project or team.

- Reactive Cost Work: Cost reductions happened after a bill spike, as one-off campaigns. Savings were not measured, waste came back, and nobody owned the result.

- Shared Infrastructure, No Attribution: Kubernetes clusters, the data lake, query engines and BI were shared by many teams, so the cost of each team's decisions was invisible to that team.

## Objectives
- Every cost attributable to a project, team or product.

- Waste found and removed continuously, not in campaigns.

- Cost as an input to architecture and product decisions, not only an output on the invoice.

- Teams accountable for the cost of what they own, with the platform team providing data and guardrails.

## Phases
The strategy followed the FinOps Foundation maturity model — crawl, walk, run — applied in order: optimizing without visibility targets the wrong things, and governance without optimization has nothing to protect.

### Crawl — Visibility
Know where the money goes before changing anything.

- Allocation standard: mandatory `team` and `project` tags and per-project roles ([tag policy](../../cloud-engineering/tag-policy.md), [workload identity](../../security/workload-identity.md)).

- Cost data as a dataset: CUR exported and queryable, with data transfer broken down by type and owner ([data transfer visibility](../../finops/data-transfer-visibility.md)).

- Shared platforms attributed: Kubernetes per namespace, Athena per role, user and dataset, BI per dataset, storage per prefix ([OpenCost](../../finops/opencost.md), [Athena cost attribution](../../cloud-engineering/aws/athena.md), [QuickSight governance](../../analytics-engineering/quicksight-governance.md), [S3 Inventory](../../cloud-engineering/aws/s3-inventory.md)).

- Budgets and alerts so surprises become notifications ([budget alerts](../../finops/budges-alerts.md)).

### Walk — Optimization
Act on the largest, safest opportunities first, measuring each one.

- Remove waste: legacy and orphaned resources, unused services and licences ([resource decommissioning](../../finops/resource-reclamation.md), [cost optimization program](../../finops/aws-cost-optimization-program.md)).

- Rightsize: databases, instances and Kubernetes requests to measured usage ([efficiency index](../../finops/kubernetes-efficiency-index.md), [VPA](../../finops/vpa.md)).

- Cheaper capacity: Spot, Graviton, autoscaling and scale-to-zero ([Spot](../../finops/spot.md), [ARM nodes](../../finops/arm.md), [Karpenter](../../finops/karpenter.md), [KEDA](../../finops/keda.md)).

- Cheaper architecture: VPC endpoints instead of NAT, single-AZ placement for data workloads, data lifecycle ([VPC endpoints](../../finops/vpc-gateway-endpoints.md), [S3 object lifecycle](../../data-governance/data-lifecycle.md), [lakehouse table lifecycle](../../data-governance/lakehouse-lifecycle.md)).

- Commitments last: Savings Plans and reservations evaluated only after rightsizing, so the commitment is sized to the optimized baseline ([reservations](../../finops/cloud-reservations.md)).

### Run — Governance
Keep the savings and make cost part of how the platform works.

- Prevention: guardrails that stop expensive patterns at creation ([SCP](../../cloud-engineering/aws/scp.md), [Airflow policies](../../data-engineering/airflow-policies.md)).

- Ownership and lifecycle: every resource, table, DAG and dataset has an owner and a deprecation path ([Glue metadata and ownership](../../data-governance/glue-metadata-owner.md), [Airflow DAG cleanup](../../data-engineering/airflow-dags-cleanup.md)).

- Cost as a product metric: cost per data product reported to product owners.

- Cost in design reviews: expected cost of placement, data transfer and storage discussed before building.

- Recurring cadence: a monthly FinOps review per team and a backlog of opportunities instead of one-off campaigns.

## Prioritization Criteria
- Expected saving against effort and risk — quick, reversible wins first, architectural changes when the evidence is clear.

- Recurring before one-off: a saving that repeats every month beats a one-time cleanup of the same size.

- Visibility items are valued as enablers: an action with no direct saving that makes many future savings visible is prioritized as an investment.

- Delegation when the owner is clear: optimizations inside a team's product are handed to that team with the evidence, and the platform team focuses on shared infrastructure.

## Execution and Governance
- Opportunities are tracked as a backlog with a classification per item — saving, visibility, governance or delegated — on [GitHub Projects](../projects/github-projects.md).

- Each optimization is measured in the same cost views before and after, and items evaluated with no action are recorded as decisions so they are not re-analysed every quarter.

- The strategy is reviewed together with the [platform roadmap](platform-roadmap.md), because the largest long-term savings come from architecture changes planned there.

## Risks
- Savings that hurt reliability: rightsizing, Single-AZ and Spot are applied according to each workload's recovery objective, never across the board.

- Optimization fatigue: teams receive a short list of high-value actions with evidence, not a long report.

- Allocation gaps: untagged and shared costs are tracked as a metric of their own and reduced over time, so attribution keeps improving.

## Skills
- FinOps

- Strategic Planning

- Cloud Architecture

- Stakeholder Management

## Tools
- OpenCost

- Karpenter

- KEDA

- VPA

- Athena

- QuickSight
