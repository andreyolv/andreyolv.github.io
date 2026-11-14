# Preventive Cloud Guardrails Across AWS Accounts with Service Control Policies

## Problem
- IAM Alone Cannot Enforce Organizational Rules: Any principal with administrative permissions in an account can disable CloudTrail, open a bucket to the internet or create resources in an unapproved region. Least privilege inside the account depends on every policy being written correctly, and a single overly broad role undoes it.

- Detection Leaves an Exposure Window: Config rules, Security Hub and scanners report a misconfiguration after it exists. Even with automated remediation, a public bucket or a stopped audit trail is exposed for seconds to hours, which is enough for data to leak or for evidence to disappear.

- Security Tooling Can Be Switched Off from Inside: CloudTrail, AWS Config, GuardDuty and Security Hub are configured per account, so a compromised or careless administrator can disable the very controls that would detect the change.

- Unapproved Regions and Services: Resources launched in a region nobody monitors escape cost dashboards, network controls and inventory, and are a common pattern in compromised accounts used for crypto mining.

- Standards Defined but Not Enforced: The tagging standard, the "no long-lived IAM access keys" rule and the IMDSv2 requirement existed as documentation. Without enforcement at creation time, compliance depended on each team remembering them.

## Solution
- Organization-Level Deny Guardrails: Implemented Service Control Policies in AWS Organizations as the preventive layer: the API call itself fails, in every account under the OU, regardless of the permissions the principal holds. SCPs never grant access; they define the maximum that IAM policies inside the account can allow.

- Protection of the Audit and Detection Stack: Denied `StopLogging`, `DeleteTrail`, `UpdateTrail`, AWS Config recorder deletion, and GuardDuty and Security Hub disabling, so audit trails and detection cannot be switched off from inside a member account.

- Account Integrity: Denied `organizations:LeaveOrganization` and root user actions in member accounts, so an account cannot escape the guardrails and the root user is not usable for day-to-day work.

- Region Restriction: Denied actions outside the approved regions (`us-east-1` for production, `us-east-2` for development) using `aws:RequestedRegion`, with global services such as IAM, Organizations, Route 53, CloudFront and Support excluded through `NotAction`.

- Data Exposure Prevention: Blocked changes to the S3 account-level Block Public Access settings and the creation of unencrypted storage, so a public bucket or an unencrypted volume cannot be created, instead of being found and fixed afterwards.

- Enforcement of Existing Standards: Turned documented standards into denies. `iam:CreateAccessKey` and `iam:CreateUser` are denied outside the platform automation role, in line with the IAM Roles over access keys standard. `ec2:RunInstances` is denied without IMDSv2 (`ec2:MetadataHttpTokens`). Creation of cost-relevant resources is denied without the mandatory `team` and `project` tags (`aws:RequestTag`), which closes the loop on the tagging standard.

- Cost Guardrails: Restricted expensive instance families and services not approved for the platform, especially in development accounts, so experiments cannot silently create GPU fleets or reserved-capacity commitments.

- Controlled Exceptions: Every deny statement excludes the break-glass role and the Terraform deployment role through `aws:PrincipalArn` conditions, so emergency access and the platform pipeline keep working, and every exception is visible in the policy itself instead of being granted ad hoc.

- Policies as Code with a Staged Rollout: Managed SCPs in Terraform with pull request review. New policies are attached first to a sandbox OU, then to development, and only then to production OUs. CloudTrail `AccessDenied` events are monitored after each attachment to catch legitimate workloads that were blocked, because an SCP failure looks like a generic permission error to the team that hits it.

- Clear Division with Detection: SCPs cover what must never happen, while Config rules, Security Hub and Cloud Custodian keep covering what can only be detected. SCPs do not apply to the management account and are limited to 5,120 characters per policy, so the management account is kept free of workloads and the policies are split by concern: security baseline, regions, data protection and cost.

## Skills
- Security

- Cloud Governance

- Cloud Engineering

- FinOps

## Tools
- AWS Organizations

- Service Control Policies (SCP)

- AWS IAM

- AWS CloudTrail

- AWS Config

- Terraform
