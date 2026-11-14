# Remediation of AWS and GitHub Security Findings from Prowler Scans

## Problem
- Findings Without Resolution: The [Prowler scans](prowler.md) produced a clear picture of the security posture of the AWS accounts and the GitHub organization, but a scan only reports. Thousands of findings accumulated, and without a process the report was the same every week.

- No Prioritization: Critical exposures (public buckets, administrative ports open to the internet, root without MFA) were mixed with low-risk best practices, so the team did not know where to start and the volume itself discouraged action.

- No Owner per Finding: Findings pointed to resources, not to teams. Resources without ownership tags or in shared accounts had nobody responsible for fixing them.

- Fixes that Regressed: Configurations corrected by hand in the console were undone by the next Terraform apply or reappeared in the next resource someone created.

## Solution
- Triage and Prioritization: Consolidated findings from AWS and GitHub, grouped them by check instead of by resource, and prioritized by severity, exposure (internet-facing, sensitive data) and effort, so one fix often closed dozens of findings.

- Ownership and Tracking: Assigned each group of findings to an owning team using resource tags and repository ownership, and tracked remediation as issues with due dates per severity, so progress was visible and measured scan over scan.

- AWS Remediations: Resolved the main AWS finding categories:
  - Identity: MFA enforced on users, root without access keys and with MFA, unused users, keys and roles removed, wildcard policies scoped ([IAM cleanup](../cloud-engineering/aws/iam-cleanup.md), [MFA and roles](../cloud-engineering/aws/iam-mfa-roles.md)).

  - Logging: organization CloudTrail with integrity validation and KMS encryption ([CloudTrail](../cloud-engineering/aws/cloudtrail.md)), S3 access logging on sensitive buckets, VPC Flow Logs.

  - Data: S3 Block Public Access at account level, default encryption on buckets, EBS volumes, snapshots and RDS, and RDS instances not publicly accessible.

  - Network: security groups open to the internet on administrative ports closed, default security groups locked down and unused ones removed ([network hygiene](../cloud-engineering/aws/network-cleanup.md)).

  - Compute: IMDSv2 required on EC2 instances, outdated runtimes and engine versions upgraded.

- GitHub Remediations: Resolved the main GitHub organization and repository findings:
  - 2FA required for all members, and outside collaborators and direct user permissions reviewed ([GitHub administration](../devops/github-admin.md)).

  - Branch protection through [Rulesets](../devops/github-rulesets.md) — required reviews, no force pushes, signed or status-checked merges on default branches.

  - Secret scanning with push protection and Dependabot alerts enabled, and leaked or unused secrets rotated or removed.

  - `CODEOWNERS` added and inactive repositories archived ([organization cleanup](../devops/github-repos-cleanup.md)).

  - GitHub Actions hardened: least-privilege `GITHUB_TOKEN` permissions and actions pinned ([zizmor](zizmor.md)).

- Fixed in Code, Not in the Console: Applied every remediation through Terraform for AWS and for GitHub repository settings ([repositories as code](../devops/github-repos-terraform.md)), so fixes survive the next apply and new resources are compliant from the start.

- Prevention at the Source: Turned the most common findings into preventive controls — [Service Control Policies](../cloud-engineering/aws/scp.md) that block public buckets, unencrypted storage and IMDSv1, and organization-level GitHub settings and rulesets — so the same finding cannot be created again.

- Accepted Risks Documented: Findings that did not apply or whose fix was not worth the cost were muted in Prowler with a documented justification and an owner, so the report shows only what still needs action.

## Skills
- Security

- Cloud Governance

- DevOps

- Cloud Engineering

## Tools
- Prowler

- AWS IAM, CloudTrail, S3, KMS, EC2, RDS

- GitHub

- AWS Organizations (SCP)

- Terraform
