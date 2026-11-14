# Legacy Infrastructure as Code Refactoring and Modernization with Terraform

## Problem
- Outdated Terraform and Providers: Legacy code was pinned to old Terraform versions and old AWS provider majors, or not pinned at all. It used deprecated resources and arguments, could not use current features, and every upgrade was postponed because nobody knew what it would change.

- Monolithic States: Large root modules held unrelated infrastructure from several teams and environments in a single state. A plan took minutes, a small change risked touching unrelated resources, and one broken resource blocked everyone.

- Copy-Paste Instead of Modules: The same S3 bucket, IAM role or security group pattern was duplicated across repositories with small differences, so fixing a standard meant editing dozens of copies and missing some.

- Hardcoded Values and Hidden Coupling: Account IDs, ARNs, subnet IDs and environment names were written inline, and one stack depended on another through copied IDs instead of explicit outputs or data sources.

- Code That No Longer Matched Reality: Resources had been changed in the console, some were created by hand or by CloudFormation, and plans showed changes nobody dared to apply. The code had stopped being the source of truth.

- No Standards or Quality Checks: No common structure, naming, tagging or formatting, no validation in CI, and local state files or manual `terraform apply` from laptops in older projects.

## Solution
- Inventory and Prioritization: Mapped every Terraform repository and state with its Terraform and provider versions, size, owners and drift, and prioritized refactoring by risk and by how often each stack changes.

- Zero-Diff Refactoring Rule: Every refactoring step had to end with a `terraform plan` showing no changes to real infrastructure. Structure changed; resources were never destroyed and recreated to make the code look better.

- Version Upgrades in Steps: Upgraded Terraform and the AWS provider one major version at a time, following the upgrade guides, replacing deprecated resources and arguments — such as splitting inline S3 bucket configuration into the dedicated `aws_s3_bucket_*` resources — and pinning versions with `required_version`, `required_providers` and a committed lock file.

- Refactoring without Recreation: Used `moved` blocks to rename resources and move them into modules, `import` blocks to bring console-created and CloudFormation resources under Terraform, `removed` blocks and `terraform state mv` to split states, and kept these blocks in the code review so every state change was visible and reviewed.

- State Split by Domain and Environment: Broke monolithic states into smaller stacks by domain, team and environment, with remote state in S3 and locking, so plans are fast, blast radius is small and ownership is clear.

- Reusable Modules: Extracted the repeated patterns into versioned internal modules (storage, IAM roles for workloads, networking, databases) with secure defaults and mandatory tags built in ([example module](../platform-engineering/terraform-module.md)), and replaced the copies with module calls.

- Parameterization and Explicit Dependencies: Replaced hardcoded IDs with variables, `tfvars` per environment, data sources and outputs, so dependencies between stacks are explicit and environments differ only in configuration.

- Drift Reconciliation: Reviewed each pending diff with the owners and decided case by case whether to bring the console change into the code or to revert it, until plans were clean and Terraform was again the source of truth.

- Standards and Quality Gates: Standardized directory structure, naming and the `team` and `project` tags ([tag policy](tag-policy.md)), and added `terraform fmt`, `validate` and [TFLint](../platform-engineering/tflint.md) to pre-commit and CI, with deployments only through the [Terraform CI/CD pipeline](../devops/cicd-terraform.md) instead of local applies.

## Skills
- Cloud Engineering

- Infrastructure as Code

- Platform Engineering

- DevOps

## Tools
- Terraform

- AWS Provider

- Amazon S3 and DynamoDB (remote state and locking)

- TFLint

- pre-commit

- GitHub Actions
