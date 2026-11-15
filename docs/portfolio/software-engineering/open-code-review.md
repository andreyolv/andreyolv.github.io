---
status: active
environment: production
kind: project
---

# Automated LLM Pull Request Review with Open Code Review and GitHub Actions

## Problem
- Mechanical First Pass Consumes Reviewer Time: Every pull request starts with the same reading — obvious bugs, missing error handling, unclear names, inconsistent patterns — before a reviewer can look at design and intent. That first pass is repetitive and depends on whoever happens to be available.

- Hosted AI Reviewers Lock in a Provider: Commercial review bots decide which model reads the code and where the diff goes. Switching models, using an internal gateway or an OpenAI-compatible endpoint is not an option, and cost follows the vendor's pricing rather than the team's.

- Review Bots Widen the CI Attack Surface: An LLM reviewer needs an API token in CI and has to see code from pull requests. The usual setup, `pull_request_target` with secrets, runs with credentials on changes from untrusted forks, and any comment can trigger a paid review.

- Unpinned Supply Chain in the Example Setup: Published examples reference the action by branch (`@main`) and install the CLI as `latest` from npm, so the code that holds the LLM token and writes to pull requests changes without review.

## Solution
- Open-Source Reviewer on Any LLM: Adopted Alibaba's Open Code Review through its reusable GitHub Action, which reviews the base-to-head diff and posts inline comments plus a sticky summary. The model is configuration — endpoint, token, model name, Anthropic or OpenAI-compatible protocol — so the team chooses the provider and can route through its own gateway.

- Trusted-Code-Only Execution: Verified in the action's source that it checks out the base branch and fetches the pull request head only as git objects, so no file from the pull request is written to the workspace or executed while the LLM token is in scope.

- Fork-Safe Trigger: Replaced the upstream `pull_request_target` trigger with `pull_request`, so secrets never reach pull requests from forks, while branches of the repository itself, including dependency-update bots, are reviewed on every push.

- Controlled On-Demand Re-Review: Re-review on a `/open-code-review` comment is limited to owners, members and collaborators and excludes bot authors, so outside comments cannot spend LLM quota. A conditional concurrency group cancels a stale review when a new one starts, without letting ordinary replies cancel a running review.

- Least Privilege and Pinned Dependencies: `permissions: {}` at workflow level with `contents: read` and `pull-requests: write` on the single job, every action pinned to a commit SHA, and the npm CLI pinned to the same release as the action.

- Runtime Visibility on the Runner: Added Harden-Runner in audit mode as the first step, recording every outbound connection of a job that holds an LLM token and sends source code to an external endpoint.

- Validated Before Adoption: Checked the workflow with actionlint and with zizmor in auditor mode, both clean, and documented every deviation from the upstream example together with the reason for it.

- Advisory, Never Blocking: Positioned as a first reader that comments, never as a required check. Formatting and lint findings stay in linters and pre-commit, and a person still approves the merge.

## Skills
- Software Engineering

- DevSecOps

- CI/CD

- AI Engineering

## Tools
- Open Code Review

- Github Actions

- Harden-Runner (StepSecurity)

- actionlint

- zizmor
