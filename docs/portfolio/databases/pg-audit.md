# PostgreSQL Audit Logging with pgAudit

## Problem

- Missing Audit Trail: Database activity was not captured in a structured, compliance-ready form, making investigations and regulatory audits difficult.
- Inconsistent Logging Configuration: Audit settings varied across PostgreSQL clusters, leaving gaps in coverage and making retention unpredictable.

## Solution

- pgAudit on CloudNativePG: Enabled the pgAudit extension on CloudNativePG clusters with declarative audit settings for statements, roles, relations and parameters.
- Centralized Audit Logs: Shipped PostgreSQL audit logs to the platform log stack for retention, search and correlation with other security signals.
- Compliance and Investigation Readiness: Provided a consistent, queryable audit trail for access reviews, incident investigations and compliance requirements.

## Skills

- Databases
- Security
- Data Governance
- Observability

## Tools

- PostgreSQL
- pgAudit
- CloudNativePG
- Fluent Bit
- Grafana Loki
- Prometheus
