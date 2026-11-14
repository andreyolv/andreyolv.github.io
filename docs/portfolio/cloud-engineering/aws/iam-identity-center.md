# Centralized Human Access to AWS with IAM Identity Center Single Sign-On

## Problem
- One IAM User per Person, per Account: Every engineer had an IAM user with a password and access keys in each AWS account they needed. Access was created by hand, account by account, and nobody could answer "what can this person access?" without checking each one.

- Offboarding Depended on Memory: Disabling someone in the corporate directory did not touch their IAM users. Former employees kept working AWS passwords and keys until someone remembered to remove them.

- Long-Lived Keys on Laptops: CLI access relied on static access keys stored in `~/.aws/credentials`, the most common way AWS credentials leak.

- Separate Passwords and MFA: Users managed one more password and one more MFA device per account, outside the company's identity provider and its policies for password strength, MFA and conditional access.

- Inconsistent Permissions: The same role in two accounts had different policies, because each was written separately, and permissions drifted with every manual change.

## Solution
- IAM Identity Center as the Single Entry Point: Enabled IAM Identity Center in the AWS Organizations management account and made it the only way people sign in to AWS, through the access portal, for every account in the organization.

- Corporate Identity Provider Federation: Connected Identity Center to the corporate identity provider through SAML, so authentication, MFA and conditional access are enforced by the same provider that protects the other company tools ([SSO across data and DevOps tools](../../security/sso.md)).

- Automatic User and Group Provisioning: Enabled SCIM provisioning so users and groups are synchronized from the identity provider. Disabling a person in the directory removes their AWS access in every account, without anyone touching AWS.

- Permission Sets by Role: Defined permission sets for the real job functions (read-only, data engineer, platform engineer, administrator), each with a session duration suited to its risk, and assigned them to directory groups per account. Access is granted by adding a person to a group, not by writing policies.

- Short-Lived CLI Credentials: Replaced static keys with `aws configure sso` and `aws sso login`, so the CLI, SDKs and tools such as Terraform use temporary credentials that expire on their own.

- Gradual Migration from IAM Users: Migrated team by team: assigned the permission sets, confirmed in CloudTrail that the person was working through Identity Center roles, then disabled and removed their IAM user, password and keys. Break-glass IAM access was kept, documented and monitored for emergencies only.

- Assignments as Code: Managed permission sets and account assignments in Terraform with pull request review, so who can access which account is versioned and auditable.

- Clear Audit Trail: Every action in CloudTrail now carries the person's identity from the directory through the Identity Center role session, so audits and incident response map actions to people across accounts.

## Skills
- Security
- Identity and Access Management
- Cloud Governance
- Cloud Engineering

## Tools
- AWS IAM Identity Center
- AWS Organizations
- SAML 2.0 and SCIM
- Microsoft Entra ID
- AWS CLI
- AWS CloudTrail
- Terraform
