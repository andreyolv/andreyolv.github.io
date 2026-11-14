# AWS IAM Hardening: MFA Enforcement and Role-Based Workloads without Personal Credentials

## Problem
- Console and API Access without MFA: IAM users could sign in to the console and use their access keys with a password or key alone. A leaked password or key was enough to act as that user, with all of their permissions.

- Personal Credentials Running Workloads: Applications, scheduled jobs, CI/CD pipelines and tools such as Airflow connections ran with access keys that belonged to individual engineers. The workload's permissions were whatever that person had, usually far more than it needed.

- Access Tied to People, Not to Systems: When the owner of the key changed teams, left the company or rotated their key, production jobs broke. Offboarding a person meant risking an outage, so keys stayed active long after they should have been revoked.

- No Attribution: CloudTrail recorded every action as the engineer whose key was used, so a pipeline's calls and a person's calls were indistinguishable during audits and incident response.

- Long-Lived Secrets Everywhere: Keys were copied into environment variables, configuration files, CI secrets and connection strings, with no rotation and no inventory of where each one was used.

## Solution
- MFA Enforcement Policy: Attached a policy to every human IAM user that denies all actions unless `aws:MultiFactorAuthPresent` is true, with a narrow exception that lets users manage only their own MFA device, password and keys (`${aws:username}`), so they can enrol without administrator help.

- MFA for the CLI: Documented and supported `sts:GetSessionToken` and profile-based MFA for command-line access, so the policy covers access keys used by people and not only the console.

- Inventory of Workload Credentials: Mapped every access key to the workloads using it through the key's last-used service and CloudTrail `userIdentity.accessKeyId`, which revealed the jobs, pipelines and tools running on personal credentials.

- IAM Roles for Every Workload: Replaced each personal key with a dedicated role and a trust policy restricted to its exact origin, following the [AWS credential standard](iam-security.md):
  - Kubernetes workloads on EKS with Pod Identity and IRSA, bound to one ServiceAccount in one namespace ([workload identity](../../security/workload-identity.md)).
  - EC2 and EMR with instance profiles.
  - Lambda with execution roles.
  - GitHub Actions with OIDC federation, restricted by repository and branch in the trust policy, so CI/CD stores no AWS secret.

- Least Privilege per Workload: Each role received only the permissions its workload uses, so the blast radius of a compromised job is that job, not the engineer who used to own the key.

- Safe Cutover and Key Removal: Migrated workloads one at a time, confirmed in CloudTrail that the old key was no longer used, deactivated it, observed for a period and then deleted it. Personal users were left with console and CLI access protected by MFA, and no workload depends on them.

- Preventing Regression: New access keys for workloads are no longer issued; creating IAM users and keys is restricted to the platform automation through [Service Control Policies](scp.md), and key age and unused keys are monitored as part of the [IAM governance process](iam-cleanup.md).

## Skills
- Security
- Identity and Access Management
- Cloud Engineering
- DevOps

## Tools
- AWS IAM
- AWS STS
- Amazon EKS Pod Identity and IRSA
- GitHub Actions OIDC
- AWS CloudTrail
- Terraform
