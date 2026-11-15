---
kind: index
---

# DevOps

CI/CD, GitHub Actions automation, container builds, GitOps, and developer tooling. This area covers pipeline automation, repository governance, image lifecycle, and platform reliability from code commit to production deployment.

## GitHub Actions & CI/CD

- [Static Validation of GitHub Actions Workflows with actionlint](actionlint.md)
- [Reusable GitHub Actions Workflow Templates for Multi-Repository CI/CD Projects](actions-centralization/)
- [Automated Infrastructure Terraform Deployment with Github Actions](cicd-terraform/)
- [CI/CD Pipelines for Airflow Projects: DAG Code Releases and Image Build with GitHub Actions](cicd-airflow.md)
- [Automated Lambda Deployment via GitHub Actions](cicd-lambda.md)
- [Airflow DAG Quality Assurance in CI/CD with Custom GitHub Action](custom-action.md)
- [Automated Documentation Updates from Github to Confluence with Github Actions](doc-confluence-action.md)
- [Automated Release Versioning with GitHub Pull Requests](github-versioning.md)
- [Multi-Architecture Container Builds with GitHub Actions on Self-Hosted Runners](multi-arch-builds.md)
- [Pull Request Template Standardization](pullrequest-template.md)
- [Automated Pod Rollouts Triggered by ConfigMap and Secret Changes](reloader/1-resume.md)
- [GitHub Repository Templating for Automated Project Setup](repositories-templates.md)
- [Self-Hosted GitHub Actions on Kubernetes for Secure CI/CD](self-hosted-actions/)

## GitHub Governance & Administration

- [GitHub Administration and Security Governance](github-admin.md)
- [GitHub Organization Cleanup: Repository Archiving, Ownership and Access Governance](github-repos-cleanup.md)
- [Software Development Productivity with GitHub Copilot](github-copilot.md)
- [GitHub Repository Standardization as Code with Terraform](github-repos-terraform.md)
- [Github Repository Governance and Compliance with GitHub Rulesets](github-rulesets.md)
- [Standardized Technical Documentation Git-Integrated with MkDocs](mkdocs.md)
- [VSCode Extensions for Consistent Development Environments](vscode-extensions.md)

## Kubernetes GitOps & Delivery

- [Kubernetes Image Update Automation with Flux](flux-image-update.md)
- [Kubernetes Manifest and CRD Validation in CI with flux-schema](flux-schema.md)
- [Declarative Linux Package Management with Devbox and Nix](devbox.md)
- [Container Registry Insights and Image Lifecycle Management](container-registry.md)
- [Descheduler of Airflow Stuck Pods for Kubernetes Resource and Cost Optimization](descheduler.md)

---

> **See also:** [Platform Engineering](./../platform-engineering/README.md) for GitOps delivery and internal developer portals, [Site Reliability Engineering](./../site-reliability-engineering/README.md) for deployment resilience, and [Security](./../security/README.md) for supply chain and pipeline security.
