# Managed Package Repository for Internal Libraries and Upstream Caching with AWS CodeArtifact

## Problem
- Internal Libraries Shared Ad Hoc: Internal Python packages were installed from Git URLs, copied between repositories or vendored into images, with no versioned releases and no single place to find them.

- Direct Dependency on Public Registries: Builds pulled every dependency straight from PyPI and npm. An outage, a removed version or a malicious package published upstream affected every build immediately.

- Credentials and Network Access in Builds: Installing private packages required personal tokens in CI and on laptops, and builds running in private subnets needed internet access through the NAT Gateway to reach public registries.

- A Self-Hosted Registry to Operate: Running a registry ourselves meant storage, backups, upgrades and availability for a component every build depends on.

## Solution
- AWS CodeArtifact Domain and Repositories: Created a CodeArtifact domain for the organization with a repository for internal packages and upstream repositories connected to public PyPI and npm, so one endpoint serves both internal and public packages.

- Upstream Caching: Public packages are fetched once through the external connection and cached in CodeArtifact, so builds keep working during upstream outages, removed versions stay available, and a package version cannot change after it is first pulled.

- Publishing from CI: Internal libraries are built and published by GitHub Actions on release tags with semantic versioning, so consumers install `package==x.y.z` instead of Git references.

- Credential-Free Authentication: CI authenticates with short-lived CodeArtifact tokens obtained through GitHub Actions OIDC roles, engineers through their [IAM Identity Center](../cloud-engineering/aws/iam-identity-center.md) sessions with `aws codeartifact login`, and Kubernetes workloads through [workload identity](../security/workload-identity.md) — no long-lived tokens anywhere.

- Least-Privilege Access: Repository policies separate publishers (CI roles of each library) from readers (all build and runtime roles), so only the pipeline of a library can publish new versions of it.

- Private Connectivity: Interface VPC endpoints for CodeArtifact and S3 let builds in private subnets and on [self-hosted runners](../devops/self-hosted-actions.md) install packages without internet access.

- Standard Tooling: Configured `pip`, `uv`, `poetry` and `npm` to use the CodeArtifact endpoint through shared configuration in project templates, so teams use their usual tools unchanged.

- Infrastructure as Code: Managed the domain, repositories, upstream connections, policies and endpoints in Terraform.

## Skills
- Software Engineering

- DevOps

- Security

- Cloud Engineering

## Tools
- AWS CodeArtifact

- GitHub Actions (OIDC)

- pip, uv, poetry and npm

- AWS PrivateLink

- Terraform
