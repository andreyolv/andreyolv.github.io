# Airflow on Kubernetes

Apache Airflow workflow orchestration running on Kubernetes. This area covers DAG lifecycle, quality assurance, observability, migration, and operational governance for data batch workflows.

## Orchestration & Pipelines

- [Data Batch Workflow Orchestration with Apache Airflow on Kubernetes](../airflow.md)
- [CI/CD Pipelines for Airflow Projects: DAG Code Releases and Image Build with GitHub Actions](cicd-airflow.md)
- [Airflow DAG Migration & Pipeline Modernization](migration.md)

## DAG Quality & Governance

- [Airflow DAG Cleanup, Organization and Ownership Governance](../airflow-dags-cleanup.md)
- [Standardized Airflow Failure Notifications through Cluster Policy Mutation](../airflow-failure-notifications.md)
- [Airflow DAGs Quality and Governance Policies](policies.md)

## Observability & Operations

- [Standardized Monitoring and Alerting for Airflow & Kafka Applications](../../observability/data-platform-applications.md)
- [Airflow Observability](observability.md)

## Infrastructure & Resources

- [Airflow on Kubernetes](kubernetes.md)
- [Airflow Operator](airflow-operator.md)
- [Airflow API](api.md)
- [DAGs Maintenance](dags-maintenance.md)
- [Shared Storage via Amazon EFS](efs.md)
- [Airflow Resources](recursos.md)
- [Airflow Secret Backend](secret-backend.md)
- [Airflow Spot Instances](spot.md)
- [Airflow SSO](sso.md)
- [Other Airflow Topics](others.md)

## Architecture

```mermaid
graph TD
    subgraph AirflowNamespace[Airflow Namespace]
        subgraph AirflowCore[Airflow Core]
            DAGProcessor[DAG Processor]
            Scheduler[Scheduler]
            APIServer[API Server]
        end

        StatsD[StatsD]
        PostgresDB[Postgres Metadata DB]

        subgraph EFS[Shared EFS Volumes]
            EFS_DAGs[EFS DAGs]
            EFS_Logs[EFS Logs <br/><b>TTL: 15 Days</b>]
            
        end

        subgraph Configurations[Configurations]
            ConfigMap[ConfigMap]
            Secrets[Secrets]
        end
    end

    Users[Users]

    subgraph Ingress[Ingress]
        Nginx
    end

    %% Core connections to infrastructure
    AirflowCore --> EFS
    AirflowCore -- "push metrics" --> StatsD
    AirflowCore --> PostgresDB
    AirflowCore --> Configurations
    Users -- "only VPN" --> Nginx
    Nginx -- "SSO" --> APIServer
    %% GitHub repository and Actions
    subgraph GitHub[Project GitHub Repository]
        DAG[DAG Code]
        subgraph GitHubActions[GitHub Actions]
            WorkflowDeployDAG[Deploy DAG]
            WorkflowBuildImage[Build Image]
        end
        DAG -- "Commit" --> WorkflowDeployDAG
        subgraph DockerfileProject[Dockerfile]
            ImageBase[Base Image]
            project-deps[Project Dependencies]
        end

        DockerfileProject -- "tag"--> WorkflowBuildImage
    end

    subgraph AirflowImage[Airflow Image GitHub Repository]
        subgraph Dockerfile
            airflow-providers
            dbt-adapters
        end
        subgraph GA[GitHub Actions]
            WorkflowBuildBaseImage[Build Image]
        end

        Dockerfile -- "tag"--> GA
    end

    %% Connection to the requested text
    WorkflowDeployDAG -- "copy code" --> EFS_DAGs

    %% Project namespace
    subgraph ProjectNamespace[Project Namespace]
        Worker[Worker Pod]

        subgraph ProjectEFS[Shared EFS Volumes]
            ProjectEFS_DAGs[EFS DAGs]
            ProjectEFS_Logs[EFS Logs]
        end

        subgraph ProjectConfigurations[Configurations]
            ProjectConfigMap[ConfigMap]
            ProjectSecrets[Secrets]
        end
    end

    Worker --> Scheduler

    %% AWS block split out with the IAM role
    subgraph AWS[AWS]
        IAMRole[IAM Role]
        SecretsManager[SecretsManager]
        Snapshot[PVC Snapshot]
        EFSBackup[EFS Backup] 
        subgraph ECR[ECR]
            BaseImage[Airflow Image]
            ProjectImage[Project Image]
        end
    end

    GA --> BaseImage
    BaseImage --> AirflowCore
    ImageBase --> BaseImage
    WorkflowBuildImage -- "build"--> ProjectImage
    Worker --> IAMRole
    Worker --> ProjectImage
    Worker --> ProjectEFS
    Worker --> ProjectConfigurations

    AirflowCore -- "Vars & Conns" --> SecretsManager
    PostgresDB -- "Backup" --> Snapshot
    EFS_DAGs --> EFSBackup

    %% Kyverno
    Kyverno[Kyverno]
    EFS --> Kyverno
    Configurations --> Kyverno
    ProjectEFS -- "namespace label \n airflow: true" --> Kyverno
    ProjectConfigurations -- "namespace label \n airflow: true" --> Kyverno

    subgraph Monitoring[Monitoring]
        Prometheus
    end

    StatsD -- "collect metrics" --> Prometheus
```

---

> **See also:** [Data Engineering](../README.md) for the parent data engineering overview, [DevOps](../../devops/README.md) for CI/CD pipelines, [Observability](../../observability/README.md) for monitoring, and [Platform Engineering](../../platform-engineering/README.md) for Helm charts and cluster tooling.
