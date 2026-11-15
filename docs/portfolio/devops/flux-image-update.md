# Kubernetes Image Update Automation with Flux

## Problem
- Manual Container Image Updates: In traditional workflows, container images are manually updated in Kubernetes deployments, leading to delays and operational inefficiencies.

- Limited Access to Kubernetes: Project teams often do not have direct access to Kubernetes clusters for security and operational reasons, making it hard for them to independently manage container image updates.

## Solution
- Automatic Image Build and Push: Set up a GitHub Actions pipeline to automatically build a new Docker image every time there is a commit to the repository and push image to private container registry. This ensures that every change is automatically built into a container image, ready for deployment.

- Image Update Automation: Configured Flux to monitor container registries for new image versions. This allows the automated and seamless update of container images without manual intervention, allowing the teams to focus on their application logic instead of worrying about deployment infrastructure.

- Declarative Image Management: The container image versions are managed declaratively using GitOps, where Flux pulls image updates directly from Git, ensuring that Kubernetes resources are updated consistently.

- Container Registry Cleanup: This process leads to frequent image builds, it is important to manage the number of images in the registry with an automatic cleanup routine that delete outdated images, ensuring efficient container registry storage and cost control.

## Architecture

```mermaid
graph TD

    subgraph ApplicationRepo[Application Repository]
        direction TB
        Code[Application Code]

        subgraph Actions[GitHub Actions]
            Build[Build Docker Image]
            Push[Push to Registry]
        end
    end

    subgraph Registry[Container Registry]
        Images[Container Images]
    end

    subgraph Kubernetes[Kubernetes]

        subgraph Flux[Flux]

            subgraph CRDs[Flux CRDs]
                IR[ImageRepository]
                IP[ImagePolicy]
                IA[ImageUpdateAutomation]
            end

            subgraph Controllers[Controllers]
                Reflector[Image Reflector]
                Automation[Image Automation]
            end
        end

    end

    subgraph DataOpsRepo[DataOps Repository]
        Manifests[Kubernetes Manifests]
    end

    %% -------- Flow with valid labels --------
    Code -->|commit| Build
    Build -->|artifact| Push
    Push -->|new image| Images

    Images -->|monitor| IR
    IR -->|reflect image tags| Reflector
    Reflector -->|evaluate policy| IP

    IP -->|trigger automation| Automation
    IA -->|automation rules| Automation

    Automation -->|update image| Manifests
```

## Skills
- DevOps

- Platform Engineering

- GitOps

## Tools
- Docker

- Flux

- Github Actions

- Azure Container Registry

- Kubernetes
