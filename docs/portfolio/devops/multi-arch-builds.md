---
status: active
environment: production
kind: project
---

# Multi-Architecture Container Builds with GitHub Actions on Self-Hosted Runners

## Problem
- Images Built for One Architecture: Container images were built only for `amd64`, which blocked moving workloads to ARM-based Graviton nodes, cheaper for the same performance.

- Slow Emulated Builds: Building `arm64` images on `amd64` runners through QEMU emulation was many times slower and made some builds — Python wheels with native extensions, compiled tools — time out or fail.

- Duplicated Workflow Logic: Each repository that tried to support two architectures wrote its own workflow, with different tags, caching and manifest handling.

- Builds Needing Private Access: Image builds needed internal package repositories and private registries that GitHub-hosted runners could not reach.

## Solution
- Native Runners per Architecture: Added `arm64` runner scale sets on Graviton nodes next to the existing `amd64` ones in the [self-hosted runners on Kubernetes](self-hosted-actions.md), so each architecture builds natively instead of through emulation.

- Parallel Build and Manifest Merge: Workflows build each architecture in parallel on its own runner with Docker Buildx, push architecture-specific images by digest, and a final job creates a multi-architecture manifest list under the release tag, so a single image reference works on both node types.

- Reusable Workflow: Packaged the pattern as a [centralized reusable workflow](actions-centralization.md) with inputs for image name, platforms and build arguments, so any repository adopts multi-arch builds with a few lines.

- Build Cache per Architecture: Used registry-backed Buildx cache per platform, so incremental builds on both architectures reuse layers instead of starting from scratch.

- Private Dependencies: Runners run inside the private network, so builds pull internal packages from [CodeArtifact](../software-engineering/codeartifact.md) and push to the private registry without exposing either to the internet.

- Enabling ARM Adoption: With every platform image available for both architectures, workloads moved to Graviton nodes on EKS ([ARM-based nodes](../finops/arm.md)) without per-image work, and mixed node pools schedule pods on either architecture.

## Skills
- DevOps

- Platform Engineering

- FinOps

## Tools
- GitHub Actions

- Actions Runner Controller (runner scale sets)

- Docker Buildx

- Amazon EKS with Graviton

- Amazon ECR
