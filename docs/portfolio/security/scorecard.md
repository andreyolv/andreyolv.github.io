---
status: active
environment: production
kind: project
---

# Continuous Supply Chain Security Posture Assessment with OpenSSF Scorecard

## Problem
- Security Posture Judged by Impression: Whether a repository is well run — branch protection enabled, changes reviewed, workflows hardened, a security policy published — is asked during every security review and answered by opinion, because nobody checks each setting by hand across every repository.

- Repository Settings Drift Silently: Branch protection is relaxed for an urgent fix and never restored, a new workflow is added with a tag-referenced action, a job gets `write-all` to make something work. None of these changes fails a build, so the posture degrades without anyone noticing.

- Configuration Lives Outside Code Review: Branch protection rules, required reviews and token defaults are repository settings, not files. A pull request review never sees them, so the controls that protect the main branch are the least audited part of it.

- No Comparable Signal for Dependencies: Choosing between two libraries or actions that solve the same problem rarely includes any check of how their maintainers handle releases, reviews and pinning, even though a compromised upstream inherits every permission the consumer grants it.

## Solution
- Automated Posture Checks: Implemented the OpenSSF Scorecard GitHub Action to score the repository against supply chain practices — Branch-Protection, Code-Review, Pinned-Dependencies, Token-Permissions, Dangerous-Workflow, Security-Policy, Signed-Releases, Vulnerabilities and others — producing a score per check plus an overall number.

- Continuous Re-Evaluation: Runs on every push to `main`, on a weekly schedule, and on the `branch_protection_rule` event, so a change to repository settings is re-scored immediately and slower drift is caught by the schedule.

- Findings Where Engineers Already Look: Exported results as SARIF and uploaded them to GitHub code scanning, so each failing check appears in the Security tab with remediation guidance and alert history, next to the zizmor and SAST findings, instead of in a report run once and forgotten.

- Public, Verifiable Results: Since the repository is public, results are published to the OpenSSF Scorecard API through OIDC (`id-token: write`), which enables the public score badge and makes the posture verifiable by consumers of the repository without running anything themselves.

- Least-Privilege Workflow: The workflow itself follows the practices it measures — `read-all` by default with write access scoped to `security-events` and `id-token` on the single job, `persist-credentials: false` on checkout, and every action pinned to a commit SHA.

- Focus on Checks with Direct Security Content: Pinned-Dependencies and Token-Permissions are treated as the actionable findings, resolved at the source by Renovate's digest pinning and by explicit `permissions:` blocks; the remaining checks are read as health indicators, not as a score to maximise.

- Dependency Selection Input: Used Scorecard results, also exposed on deps.dev, as one comparative signal when adopting third-party libraries and actions — never as a hard gate with a minimum score, since small, well-maintained projects routinely score low for reasons that do not matter.

## Skills
- Security

- DevSecOps

- CI/CD

## Tools
- OpenSSF Scorecard

- Github Actions

- GitHub Advanced Security (SARIF)

- Renovate

- zizmor
