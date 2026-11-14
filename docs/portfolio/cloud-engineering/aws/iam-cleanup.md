# AWS IAM Cleanup, Organization and Governance: Unused Access Removal and Ownership

## Problem
- Accumulated IAM Sprawl: Years of ad-hoc work left hundreds of users, roles, groups and policies with no clear purpose. Former employees, finished projects, proofs of concept and tools that were replaced still had identities and credentials in the accounts.

- Unused and Long-Lived Credentials: Access keys that had not been used for months, keys never rotated, users with console passwords and no MFA, and service users whose application no longer existed. Every one of them was a credential that could leak and still work.

- Excessive Permissions: `AdministratorAccess` and `*:*` policies attached directly to users and roles "temporarily", wildcard actions and resources in custom policies, and permissions granted for services the principal had never called.

- No Ownership: Nothing recorded who owned an identity or why it existed, so nobody felt safe deleting anything. Cleanup stalled on the question "what breaks if we remove this?".

- Inconsistent Structure: Inline policies mixed with managed ones, permissions attached directly to users instead of through groups or roles, duplicated policies with slightly different statements, and no naming convention to tell a human from an application or a team from a project.

- Audit and Compliance Pressure: Access reviews were manual and slow, the credential report could not be read without context, and there was no evidence that access was reviewed periodically.

## Solution
- Full IAM Inventory: Built an inventory of every user, role, group, policy and access key across accounts from the IAM credential report and the IAM APIs, enriched with last-used dates for passwords, access keys and roles.

- Usage-Based Analysis: Used IAM Access Analyzer unused access findings and service last accessed data to identify unused identities, unused keys and permissions granted for services that were never called, so decisions were based on evidence instead of guesses. CloudTrail was queried to confirm the real callers before removing anything.

- Ownership Assignment: Required `owner`, `team` and `purpose` tags on every user and role. Identities without a declared owner after the review window were treated as candidates for removal.

- Safe Removal Process: Applied a staged process instead of deleting directly: deactivate access keys or attach an explicit deny policy, keep the identity in quarantine for an observation period while monitoring `AccessDenied` events in CloudTrail, and only then delete it. A blocked legitimate workload could be restored in minutes by reverting a single step.

- Least Privilege Refactoring: Replaced `AdministratorAccess` and wildcard policies with scoped policies, using Access Analyzer policy generation from CloudTrail activity as the starting point. Inline policies were converted to customer managed policies, and duplicated policies were consolidated.

- Standard Structure and Naming: Defined a naming convention that separates human access, application roles and automation (`<team>-<application>-<env>`), moved human permissions from users to groups and roles, and removed permissions attached directly to users.

- Roles over Users: Migrated applications from IAM users with access keys to IAM Roles with trust policies (EC2 instance profiles, EKS Pod Identity and IRSA, GitHub Actions OIDC), following the [AWS credential standard](iam-security.md), and removed the keys after each migration.

- IAM as Code: Imported the remaining IAM resources into Terraform, so new users, roles and policies are created only through pull requests with review, and drift from manual changes is visible.

- Continuous Governance: Scheduled recurring access reviews based on the credential report and Access Analyzer findings, alerts for access keys older than the rotation limit and for new users created outside the pipeline, and preventive guardrails through [Service Control Policies](scp.md) so the cleanup does not regress.

## Skills
- Security
- Cloud Governance
- Cloud Engineering
- Identity and Access Management

## Tools
- AWS IAM
- IAM Access Analyzer
- IAM Credential Report
- AWS CloudTrail
- AWS Organizations
- Terraform
