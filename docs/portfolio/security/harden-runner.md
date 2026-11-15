---
status: active
environment: production
kind: project
---

# Runtime Security for GitHub Actions Runners with Harden-Runner

## Problem
- Static Controls Stop at the Workflow File: SHA-pinned actions, least-privilege `GITHUB_TOKEN` permissions and workflow SAST describe what a job is allowed to do. None of them observes what the job actually does once it runs, so a pinned dependency that turns malicious, or a build script that fetches and executes a remote payload, goes unnoticed.

- Unrestricted Egress from the Runner: A GitHub-hosted runner can reach any address on the internet. Every action, package install and test in a job shares that network access and the credentials in scope, which is exactly the channel a compromised dependency uses to exfiltrate secrets and tokens.

- No Record of Runtime Behaviour: After an incident such as the `tj-actions/changed-files` compromise, the question that matters is which workflows contacted which destinations and which processes touched the source tree. GitHub keeps step logs, not network or process activity, so that question has no answer after the fact.

- Unknown Baseline: Nobody knows the full set of endpoints a pipeline legitimately depends on — registries, module proxies, APIs called by actions. Without that list, restricting egress is guesswork and breaks builds.

## Solution
- Runtime Agent on Every Job: Added StepSecurity Harden-Runner as the first step of every job in `.github/workflows/` (Go lint and build, OpenSSF Scorecard), so network calls, process executions and file writes are recorded for each run, with a per-run insights page linked from the job summary.

- Staged Rollout, Audit First: Deployed with `egress-policy: audit`, which records outbound connections without blocking them. The recorded destinations become the baseline for `egress-policy: block` with an explicit `allowed-endpoints` list per job. Blocking is applied only after that list has been reviewed, never guessed.

- Compatible with Published Scorecard Results: Verified that `step-security/harden-runner` is on the approved list of actions for the job that runs `ossf/scorecard-action` with `publish_results: true`, so the Scorecard job is hardened without its results being rejected by the OpenSSF API.

- Supply Chain Hygiene on the Agent Itself: Pinned the action to a commit SHA like every other action in the repository, choosing a release at least 3 days old to match the cooldown the repository applies to dependency updates, so the runtime control does not become a mutable dependency itself.

- Layered with Static Controls: Complements, not replaces, the build-time controls already in place — `read-all` default permissions, `persist-credentials: false` on checkout, SHA pinning, zizmor analysis of the workflows and the Scorecard posture checks. Those define what a job may do. Harden-Runner shows what it did.

- No Cost for a Public Repository: The community tier covers public repositories on GitHub-hosted runners, so the control is adopted before any signing identity or deployment credential is placed in CI, the moment it becomes critical.

## Skills
- Security

- DevSecOps

- CI/CD

## Tools
- Harden-Runner (StepSecurity)

- Github Actions

- OpenSSF Scorecard

- Renovate

- zizmor
