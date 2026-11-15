---
status: active
environment: production
kind: project
---

# GitHub Organization Cleanup: Repository Archiving, Ownership and Access Governance

## Problem
- Repository Sprawl: The organization held hundreds of repositories, many of them abandoned — finished projects, experiments, forks, copies of templates never used and repositories of people who had left — with nothing distinguishing them from the ones in production.

- No Ownership: Repositories had no `CODEOWNERS`, no team responsible and often no description, so nobody could answer who maintained a repository or whether it could be removed.

- Access Granted to People, Not Teams: Over the years, individual users and outside collaborators were added directly to repositories with write or admin permissions. Access stayed after people changed teams or left, and reviewing it meant checking each repository one by one.

- Stale Secrets and Integrations: Old repositories kept Actions secrets, deploy keys, webhooks and GitHub App installations that pointed to systems no longer in use, each one a credential that could still leak.

- Noise and Risk in Security Tooling: Dependabot and code scanning alerts piled up in unmaintained repositories, hiding the alerts in active ones and inflating the organization's security backlog.

- Inconsistent Naming and Discovery: No naming convention, topics or descriptions, so finding the repository for a service or a pipeline relied on asking around.

## Solution
- Repository Inventory: Built an inventory of every repository through the GitHub API — last push, open pull requests, Actions activity, visibility, teams and direct collaborators, secrets, webhooks and open security alerts.

- Classification and Owner Review: Classified repositories as active, inactive (no activity for a long period), template, fork or ownerless, and reviewed the list with each team to assign an owning team to every repository kept.

- Archive Instead of Delete: Archived inactive repositories instead of deleting them, keeping history read-only and reversible, and deleted only empty repositories, unused forks and confirmed duplicates.

- Access Cleanup: Removed direct user and outside collaborator permissions in favour of GitHub teams mapped from the identity provider, reduced admin permissions to repository owners, and removed access of people who had left.

- Secrets and Integrations Cleanup: Removed unused Actions secrets, deploy keys and webhooks, and reviewed GitHub App and OAuth App installations, keeping only the ones with an owner and a purpose.

- Standard Organization: Defined a naming convention by team and purpose, mandatory description and topics, and a `CODEOWNERS` file in every active repository, so ownership is visible in the repository itself and reviews are routed automatically.

- Governance to Prevent Regression: After the cleanup, the remaining repositories were adopted into [repository management with Terraform](github-repos-terraform.md) and protected by [GitHub Rulesets](github-rulesets.md), new repositories are created only from [templates](repositories-templates.md), and organization settings restrict repository creation, deletion and visibility changes ([GitHub administration](github-admin.md)). A periodic review archives repositories that become inactive.

## Skills
- DevOps

- Security

- Governance

- Platform Engineering

## Tools
- GitHub

- GitHub REST and GraphQL API

- GitHub Teams and CODEOWNERS

- Microsoft Entra ID

- Terraform (integrations/github provider)

- Python
