# Projects by Status

This catalog lists portfolio projects with their lifecycle status and, when applicable,
the environment where they run. Use the filters to show projects by lifecycle status
(active, POC, deprecated or planned), by environment (production, non-production or
local), or by discipline (Network, DevOps, Cloud Engineering, etc.).

The catalog is generated from the frontmatter of each project page. The Network section is
the first pilot; more disciplines will appear as their pages receive status metadata.

## Status definitions

| Status | Meaning |
| --- | --- |
| **Active** | Current approach, in use and maintained. It can run in production or in a local/lab environment. |
| **POC** | Validated in a proof of concept or lab, but not adopted as the standard yet. |
| **Deprecated** | No longer current. It may be superseded by another project or approach, or simply discontinued. The page is kept for historical context and to document the migration. |
| **Planned** | Design, RFC or roadmap only; not implemented yet. |

## Environment definitions

| Environment | Meaning |
| --- | --- |
| **Production** | Runs in production with real workloads or users. |
| **Non-production** | Runs in development, staging or another non-production environment. |
| **Local** | Runs on a local cluster, home lab or learning environment. It is not intended for production. |

## Discipline definitions

| Discipline | Meaning |
| --- | --- |
| **Network** | Networking, ingress, load balancing, service mesh and DNS projects. |
| **DevOps** | CI/CD, GitHub Actions, GitOps, container registry and developer tooling. |
| **Cloud Engineering** | AWS, Azure, Terraform, multi-cloud and cloud infrastructure. |
| **Data Engineering** | Batch processing, orchestration, query engines and data pipelines. |
| **Data Streaming** | Event streaming, CDC and real-time ingestion. |
| **Databases** | Database deployment, migration and monitoring on Kubernetes and cloud. |
| **Data Governance** | Data catalog, contracts, lineage, quality and lakehouse governance. |
| **Analytics Engineering** | BI, transformation and analytics tooling. |
| **FinOps** | Cloud cost optimization, rightsizing and resource efficiency. |
| **Observability** | Monitoring, alerting, logging, metrics and tracing. |
| **Platform Engineering** | Internal developer platform, GitOps, operators and developer environments. |
| **Security** | Runtime security, secrets, compliance, scanning and supply chain security. |
| **Site Reliability Engineering** | Backups, HA, disaster recovery and SRE tooling. |
| **Software Engineering** | Package repositories, messaging and code quality. |
| **AI** | LLM inference, AI-native development and MCP pipelines. |
| **Management** | Roadmap, FinOps strategy, service catalog and agile planning. |
| **MLOps** | Machine learning lifecycle and model deployment. |

## Project catalog

<!-- portfolio-catalog -->

## Maintaining the catalog

Project pages declare their metadata in the frontmatter:

```yaml
---
status: active          # active | poc | deprecated | planned
environment: production # production | non-production | local
kind: project           # project | standard | rfc | guide | index | subpage
---
```

For deprecated projects that were replaced, add the replacement page. The
`superseded_by` field is optional; omit it when the project was discontinued without a
direct replacement:

```yaml
---
status: deprecated
environment: production
kind: project
superseded_by: gateway-api.md
superseded_by_label: Gateway API and Envoy Gateway
---
```

`environment` is required for `active` and `poc` projects. Deprecated and planned projects
may omit it when they no longer run anywhere or were never implemented.

Pages with `kind: project` are listed here. Category indexes (`kind: index`) and project
subpages (`kind: subpage`) do not declare a status and are excluded from the catalog.
Standards, RFCs and guides are also excluded.
