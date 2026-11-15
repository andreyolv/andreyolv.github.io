# Project

## Context
GitHub Actions workflows running on GitHub-hosted runners could not securely access internal services available only through private endpoints. This prevented CI/CD workflows that require private network access and introduced security/compliance concerns.

## Goals
- Run CI/CD workloads inside the private network.

- Allow secure access to internal/private endpoints.

- Improve compliance posture by keeping sensitive tasks inside controlled infrastructure.

- Scale runners based on demand.

- Reduce per-run setup time by using a prebuilt execution image.

## High-Level Architecture
- GitHub Actions workflows target self-hosted runners.

- Runners are deployed on Kubernetes in the private network.

- Actions Runner Controller (ARC) manages runner lifecycle.

- Runner Scale Sets provide autoscaling/high availability for runner capacity.

- Workflows run in a custom Docker image that includes required tools/dependencies.

## Architecture

```mermaid
graph TD
    subgraph GitHub_App[Application GitHub Repository]
        Caller[Caller Workflow]
    end

    subgraph GitHub_DataOps[dataops-actions GitHub Repository]
        Reusable[Reusables Workflows<br/>- deploy-dags<br/>- build-docker-image<br/>- terraform]
        Dockerfile[Dockerfile<br/>with workflow dependencies]
    end

    subgraph Update
        Releases[Releases actions/runner] -- when --> Dockerfile
    end

    subgraph Container Registry
        Image[Docker Image]
    end

    subgraph Kubernetes
        ARC[Actions Runner Controller]
        ScaleSet[Runner Scale Set]
        Listener[Listener]
        Pods[Ephemeral Pods Runners]

        ARC --> ScaleSet
        ScaleSet --> Listener
        Listener --> Pods
    end

    subgraph Internal Resources
        APIs[APIs]
        DBs[Databases]
        Airflow[Airflow]
        AWS[AWS]
    end

    %% Connections between the blocks
    Caller -- uses --> Reusable
    
    Reusable --> ScaleSet
    
    Dockerfile -- repo tag build --> Image
    Image --> ScaleSet
    
    Pods --> APIs
    Pods --> DBs
    Pods --> Airflow
    Pods --> AWS
```

## Key Components
- Actions Runner Controller (ARC)

- Runner Scale Set

- Kubernetes Cluster (private network)

- Custom Docker Image for workflow execution

- Private connectivity (private endpoints / internal DNS / internal routing)

## Security Considerations
- Network boundary: workflow traffic to internal services stays within the private network.

- Credential handling: prefer short-lived credentials and scoped permissions.

- Image provenance: ensure the custom runner image is built from trusted sources and scanned.

- Least privilege: runner service accounts and any cloud identities should be tightly scoped.

## Operational Notes
- Capacity is managed via Scale Sets to match workload demand.

- Custom image reduces time spent installing dependencies at runtime.
