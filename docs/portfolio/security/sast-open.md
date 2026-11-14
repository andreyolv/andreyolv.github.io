# Code Security with SAST Open Source Tools

## Problem

- Manual and Inconsistent Security Checks: Image, dependency and code scanning were performed ad hoc, leaving gaps between repositories and teams.
- Limited Vulnerability Visibility: Findings from containers, dependencies and static analysis were scattered across tools, making prioritization and remediation difficult.
- Unmanaged Supply Chain Risk: Base images, dependencies and build artifacts lacked consistent provenance and update controls.

## Solution

- Automated image and dependency scanning with Trivy in GitHub Actions, while internalizing images for improved security.
- Implemented Static Application Security Testing (SAST) with GitHub Advanced Security and CodeQL to identify and minimize CVEs.
- Automated dependency updates with Renovate and Dependabot to reduce exposure to known vulnerabilities.
- Established security guidelines and monitoring practices across the organization for continuous improvement in code security.

## Skills

- Security
- DevSecOps
- Software Engineering
- Supply Chain Security


## Tools

- Trivy
- GitHub Actions
- GitHub Advanced Security
- CodeQL
- Renovate
- Dependabot
- Cosign
