# Centralized AWS API Auditing and Investigation with CloudTrail and Athena

## Problem
- Fragmented Audit Logs: CloudTrail was configured differently per account — some with trails, some relying only on the 90-day event history in the console — so answering "who did this?" depended on the account and on how old the event was.

- Logs Stored Where They Could Be Changed: Trails wrote to buckets in the same account as the workloads, without encryption with a dedicated key or integrity validation, so anyone with enough permissions there could disable logging or delete evidence.

- Data Events Either Missing or Too Expensive: Without S3 and Lambda data events nobody could tell who read or deleted data in the data lake; enabling them for everything would generate a large and costly volume of logs.

- Logs Collected but Not Queried: Raw JSON files in S3 were impractical to search. Investigations, cost attributions and access reviews took hours of manual work, so the logs were rarely used for anything beyond compliance.

- No Alerting on Sensitive Actions: Root logins, console logins without MFA, IAM policy changes, security group openings or attempts to stop logging were only discovered, if at all, after the fact.

## Solution
- Organization Trail: Created a multi-region organization trail in AWS Organizations covering every current and future account, with management events enabled everywhere, so no account can be created or left without auditing.

- Central Log Archive Account: Delivered all logs to an S3 bucket in a dedicated log archive account, encrypted with a customer managed KMS key, with log file integrity validation, a bucket policy that only allows CloudTrail to write, and lifecycle rules that move older logs to cheaper storage classes and expire them after the retention period.

- Tamper Protection: Protected the trail with [Service Control Policies](scp.md) denying `StopLogging`, `DeleteTrail` and `UpdateTrail` in member accounts, so auditing cannot be switched off from inside an account.

- Selective Data Events: Used advanced event selectors to record S3 data events only for sensitive data lake buckets and prefixes, and only the operations that matter (writes and deletes everywhere, reads on sensitive data), keeping the cost proportional to the value.

- Queryable with Athena: Exposed the logs as an Athena table with partition projection by account, region and date, so queries scan only the relevant partitions, and built saved queries for common investigations — actions by principal, by access key, by source IP, failed calls (`AccessDenied`) and changes to IAM, networking and security services.

- CloudTrail Insights: Enabled Insights on management events to detect unusual API call volumes and error rates, which surfaced, for example, an abnormal rate of CloudWatch `GetMetricData` calls from an external monitoring integration that was driving cost.

- Real-Time Alerts on Sensitive Actions: Created EventBridge rules for root account usage, console sign-in without MFA, IAM user and access key creation, policy changes, security group rules opened to the internet and changes to CloudTrail itself, routed to the security and platform teams.

- Foundation for Other Projects: The centralized trail became the data source for [Athena cost per user](athena.md), the evidence behind the [IAM cleanup](iam-cleanup.md) and [MFA and roles migration](iam-mfa-roles.md), the attribution of personal access to people after the [Identity Center migration](iam-identity-center.md), and the monitoring of `AccessDenied` events after each SCP rollout.

- Infrastructure as Code: Managed the organization trail, the log archive bucket, KMS key, Athena table and EventBridge rules in Terraform.

## Skills
- Security

- Cloud Governance

- Cloud Engineering

- Data Engineering

## Tools
- AWS CloudTrail and CloudTrail Insights

- AWS Organizations

- Amazon S3 and AWS KMS

- Amazon Athena

- Amazon EventBridge

- Terraform
