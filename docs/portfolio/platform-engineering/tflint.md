---
status: active
environment: production
kind: project
---

# Credential-Free Terraform and OpenTofu Linting in CI with TFLint

## Problem
- Validation That Accepts Invalid Infrastructure: `terraform validate` and `tofu validate` only check that the configuration is well-formed and internally consistent. They never contact a provider, so a non-existent instance type, a misspelled region or an argument removed two provider versions ago all pass, and the mistake surfaces only at `plan` or, worse, at `apply`.

- Plan as the First Correctness Check: Relying on `plan` to catch typos means every check needs cloud credentials, network access and an API round trip. It is the slowest and most expensive feedback loop for the cheapest class of error, and on pull requests from forks or untrusted branches it is not available at all without handing out a key.

- Unattended Applies With No Gate in Front: GitOps-driven Terraform with automatic plan approval runs applies on an interval with no human reading the plan. In that model nothing stands between a merged commit and a change to a real cloud account except whatever ran in CI before the merge.

- Hygiene Enforced by Memory: Unpinned module sources, variables without types or descriptions, deprecated syntax and declarations nothing references are known problems that `validate` has no opinion about. Left to code review, they are caught inconsistently and accumulate across repositories.

- A Linter That Runs, Passes and Checks Nothing: TFLint ships only the language ruleset; the provider-aware rules live in separate plugins that must be declared and fetched explicitly. A pipeline that installs the binary but skips plugin initialisation stays green while verifying only generic rules — worse than no linter, because it creates false confidence.

- Rule Churn and Rule Floods: An unpinned linter adds rules between releases, so unrelated pull requests start failing for reasons nobody changed. Enabling every rule at once on an existing codebase produces a backlog large enough that the tool gets disabled instead of the findings fixed.

- Linting Mistaken for Security Scanning: Public buckets, unencrypted volumes and open security groups are policy questions, not correctness questions. Treating a linter as a security control leaves that gap in place while making it look covered.

## Solution
- Credential-Free Correctness Gate: Adopted TFLint as the step between `validate` and `plan`, embedding provider schemas through plugins so invalid values, deprecated arguments and out-of-range enums fail in seconds without any cloud credentials. Untrusted pull requests are checked thoroughly without ever receiving a key.

- Cheapest-First Pipeline Ordering: Standardised the pre-merge sequence as `fmt → validate → lint → policy scan → plan → review → apply`, keeping every step before `plan` credential-free. Each stage only runs once the cheaper one before it has passed.

- Provider Ruleset Declared and Pinned: Declared the AWS ruleset plugin with an explicit version and source in `.tflint.hcl`, fetched with `tflint --init`, turning TFLint from a style checker into a correctness checker that knows the provider's API surface. The same pattern applies to the Azure and Google rulesets.

- Initialisation Enforced in CI: Installed the engine on runners with the `setup-tflint` action and ran `tflint --init` as an explicit, mandatory step, so a missing plugin fails the job instead of silently reducing coverage to the generic rules.

- Authenticated Plugin Downloads: Passed a GitHub token to the plugin fetch so parallel jobs do not hit the anonymous GitHub releases rate limit at the moment several pipelines run at once.

- Supply Chain Pinning: Pinned the action to a commit SHA and the TFLint version explicitly, so new rules arrive through a deliberate upgrade rather than as unexplained failures on unrelated pull requests.

- Language Ruleset as the First Baseline: Enabled the bundled language rules first — pinned module sources, typed and described variables and outputs, deprecated syntax, unused declarations — because they concern hygiene rather than a cloud API and never produce findings that depend on credentials.

- Incremental Rule Rollout: Made correctness rules blocking from day one, and enabled the best-practice and naming rules (disabled by default in the provider ruleset) deliberately and in batches, with the fixes in the same pull request. Every enabled rule fails the build; everything else is explicitly off rather than advisory noise.

- Shift-Left Without Losing Enforcement: Ran TFLint as a pre-commit hook and in the editor for fast feedback, while treating only the pull request check as enforcement — the one place a hurried developer cannot bypass.

- Engine-Agnostic Coverage: Applied the same configuration to Terraform and OpenTofu code, since both share the same configuration language, so the choice of engine does not change the quality gate.

- Explicit Boundary With Policy Scanning: Documented that TFLint covers style and correctness only, and kept security and policy checks (Checkov, Trivy, Conftest/OPA) as a separate stage of the pipeline, so the gap is named rather than assumed covered.

## Skills
- Platform Engineering

- Infrastructure as Code

- DevOps

- CI/CD

## Tools
- TFLint

- Terraform

- OpenTofu

- GitHub Actions

- pre-commit

- AWS
