---
status: active
environment: production
kind: project
---

# AWS Cloud Alerting as Code with Datadog Monitors

## Problem
- Unmonitored Managed Services: AWS managed services (RDS, ALB, SQS, Lambda, NAT Gateway, DynamoDB) had no consistent alerting, so issues like database storage exhaustion, growing queue backlogs or load balancer 5xx spikes were found by users before the team.

- Console-Created Alarms: The few existing CloudWatch Alarms were created by hand in the AWS Console, per account and per region, with no review, no history and different thresholds for the same kind of resource.

- New Resources Without Coverage: Every new database, queue or load balancer needed someone to remember to create its alarms, so monitoring always lagged behind the infrastructure.

- Alert Fatigue and Poor Routing: Alerts went to a single shared channel regardless of severity or owning team, with flapping thresholds and no context, so real incidents were lost among noise.

- Multi-Account Blind Spots: With workloads spread across several AWS accounts, there was no single place to see which resources were alerting and which were not covered at all.

## Solution
- Datadog AWS Integration: Connected every AWS account to Datadog through a cross-account IAM role with read-only permissions, and streamed CloudWatch metrics with CloudWatch Metric Streams and Kinesis Data Firehose for lower latency than API polling.

- Monitors as Code: Defined all monitors in Terraform with the Datadog provider, reviewed through pull requests and applied by the CI/CD pipeline, so every threshold change is versioned and auditable.

- Tag-Based Coverage: Scoped monitors by AWS tags (`env`, `team`, `service`) and used multi-alert monitors grouped by resource, so a new RDS instance or SQS queue is covered automatically as soon as it is tagged, following the [tag policy](../cloud-engineering/tag-policy.md).

- Standard Monitor Catalog per Service:
  - RDS / Aurora: CPU, free storage space, freeable memory, connections, replica lag.

  - ALB / NLB: 5xx rate, target response time, unhealthy hosts.

  - SQS: age of oldest message, visible messages, dead-letter queue not empty.

  - Lambda: error rate, throttles, duration close to the timeout.

  - EC2 / EKS nodes: status check failures, CPU credits, disk usage.

  - NAT Gateway: dropped packets and port allocation errors.

  - DynamoDB: throttled requests and consumed capacity.

- Smarter Thresholds: Used anomaly and forecast monitors where static thresholds do not fit (traffic with daily seasonality, disk filling up), recovery thresholds and evaluation windows to stop flapping, and composite monitors to alert only when related symptoms happen together.

- Severity-Based Routing: Routed notifications by tag and priority — critical alerts page the on-call engineer through PagerDuty/Opsgenie, warnings go to the owning team's Slack channel — and every message carries the affected resource, a dashboard link and the runbook link.

- Planned Maintenance Downtimes: Scheduled Datadog downtimes for maintenance windows and deployments, so expected disruptions do not page anyone.

## Skills
- Observability

- Site Reliability Engineering

- Cloud Engineering

- Infrastructure as Code

## Tools
- Datadog

- AWS CloudWatch

- Amazon Kinesis Data Firehose

- Terraform

- PagerDuty

- Slack
