# Projects by Status

This catalog lists portfolio projects with their lifecycle status and, when applicable,
the environment where they run. Use the filters to show projects by lifecycle status
(active, POC, deprecated or planned) or by environment (production, non-production or
local).

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
