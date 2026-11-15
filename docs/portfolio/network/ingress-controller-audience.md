---
status: active
environment: production
kind: project
---

# User Access Audience Monitoring for Envoy Gateway

## Problem
- Access Auditing at the Gateway: With SSO enforced at the gateway, every request carries an authenticated identity, but the platform still needed to know which users and groups were accessing which applications and how often. Without that visibility, unused or low-value services stayed exposed and kept consuming infrastructure and support effort.

- Previous Approach Did Not Scale: The earlier Pomerium-based setup stored access events in its own PostgreSQL database. After the platform standardized ingress on Gateway API and Envoy Gateway, maintaining a separate identity-aware proxy and audit database became unnecessary operational overhead.

- Cost and Lifecycle Decisions: Identifying underused services required joining access data with the service catalog and ownership information, so the platform could decide whether to keep, optimize, or decommission each application.

## Solution
- Centralized OIDC SSO at the Gateway: Envoy Gateway enforces authentication through an OIDC SecurityPolicy integrated with Microsoft Entra ID, so every request that reaches an application has already been authenticated at the edge.

- Identity-Aware Access Logs: Envoy Gateway access logs record the requested host and path together with the authenticated user and group obtained from the OIDC/JWT claims. Logs are shipped to Loki, where they can be queried by application, user, group, and time window.

- Per-Route Traffic Metrics: Envoy exposes request metrics such as `envoy_http_downstream_rq_total` per route and response code. Prometheus stores them and Grafana combines request volume with the identity-aware logs.

- Audience Dashboard: A Grafana dashboard shows requests per application and per authenticated user or group, highlighting services with no access or very low usage over a defined period.

- Decommissioning and Cost Optimization: The dashboard feeds a recurring review of unused or underused services. Applications with no audience are candidates for decommissioning, reducing infrastructure cost and the externally reachable surface.

- No Sidecar or Separate Audit Database: Because identity and traffic data are collected at the gateway, applications do not need sidecars or their own audit database, and the Pomerium/PostgreSQL audit stack is no longer required.

## Skills
- DevOps

- FinOps

- Observability

- Security

## Tools
- Envoy Gateway

- Gateway API

- Microsoft Entra ID (OIDC)

- Prometheus

- Grafana

- Loki

- Kubernetes
