# Curriculum Vitae

**Andrey Gustavo de Oliveira** — Platform & Data Engineer
Curitiba, Paraná, Brazil · Remote

[GitHub](https://github.com/andreyolv) ·
[Kubestronaut profile](https://www.cncf.io/training/kubestronaut/?_sft_lf-country=br&p=andrey-gustavo-de-oliveira) ·
[Portfolio](https://andreyolv.github.io/)

---

## Summary

Specialist in **cloud-native data engineering platform and infrastructure on Kubernetes**.
Hands-on experience architecting, developing, optimizing, troubleshooting and sustaining
high-maturity, resilient, scalable and cost-efficient end-to-end data platforms.

Bridges best practices across Data Engineering, DevOps, Platform Engineering, Site
Reliability Engineering, Observability, Security, Cloud Computing and FinOps. Experienced
with open-source data tools such as Airflow, Spark, Kafka, Trino, dbt, OpenMetadata,
PostgreSQL, Iceberg and MLflow, integrated with cloud-native tooling like GitHub Actions,
Terraform, Flux, Crossplane, Backstage, Karpenter, KEDA, NGINX Ingress, Prometheus, Grafana,
External Secrets, Kyverno and Velero.

Problem-solver with a pragmatic mindset focused on real business value, and a strong
commitment to documentation, knowledge sharing and raising the engineering bar of the team.

---

## Experience

<div class="timeline-item" markdown>

### Data Reliability Engineer
<p class="timeline-meta">Clickbbus · Full-time · Current · Remote</p>

Lead the architecture of the data platform infrastructure, with ownership of scalability,
reliability, security, observability, modernization and cost efficiency on Kubernetes and
cloud.

- Lead platform evolution through technical planning, standards and documentation — ADRs,
  reference architectures, service catalog, operational processes and continuous operations.
- Modernize legacy data infrastructure into a cloud-native, Kubernetes-based platform using
  Airflow, Spark, OpenMetadata, Trino and dbt.
- Drive platform engineering through automation and standardization, enabling teams to
  self-serve infrastructure and operate autonomously at scale.
- Define, monitor and enforce SLOs for mission-critical data services; design disaster
  recovery plans and observability strategies for proactive detection and rapid response.
- Drive security best practices and frameworks (Zero Trust, CIS, MITRE ATT&CK, ISO/IEC),
  enforcing scans across cloud, clusters, containers and code, and hardening the platform
  with permissions, policies, SSO, workload identity, secrets, certificates, SAST,
  supply-chain controls and private network access.
- Drive FinOps practices and cost monitoring; optimize budgets, resources and processes for
  cost-efficient, well-governed cloud operations.
- Collaborate with MLOps, SRE, Security and FinOps partners to align platform strategy with
  organizational objectives, and mentor engineering teams through coaching and knowledge
  transfer.

</div>

<div class="timeline-item" markdown>

### Data Platform Engineer — DataOps · Cloud · DevOps · FinOps · Network · Observability · Platform · Security · SRE
<p class="timeline-meta">Raízen · Full-time · 2022 – 2025 · Remote</p>

Owned the data platform across its main disciplines, from Airflow at scale (+1,000 DAGs in
production) to cloud networking, security and cost.

- **Data Engineering** — ran Airflow, Spark, Kafka and dbt on Kubernetes for orchestration and
  distributed processing; built custom platform solutions in Python and Go; automated
  infrastructure and data-tool maintenance on Kubernetes.
- **Cloud** — designed and integrated managed Azure services (Synapse, Purview, AKS, ACR,
  PostgreSQL, DMS, Cost Management, Key Vault, Private Endpoints/Link, Databricks, Machine
  Learning, AI Services, Event Hubs, Container Apps, Entra ID, Defender for Cloud, Log
  Analytics), and provisioned them with Crossplane and Terraform following the Well-Architected
  Framework.
- **DevOps** — designed CI/CD for Airflow DAG releases and image builds with GitHub Actions;
  centralized reusable workflows across the organization; administered the GitHub organization
  with rulesets, branch standards and custom properties; built repository templates; and ran
  self-hosted Actions runners on Kubernetes inside the VPN.
- **Platform & GitOps** — implemented Flux for declarative, version-controlled delivery and
  multi-repository GitOps with tenant autonomy; built a development environment (Airflow,
  Jupyter, VS Code) templated with a custom Helm chart for dozens of users; delivered a
  Backstage IDP for self-service provisioning; wrote a custom Kubernetes operator for secret
  injection from Senha Segura; and built a governed Kafka topic/user platform.
- **FinOps** — built Grafana resource-efficiency dashboards (requests vs. usage), adopted
  Kubecost/OpenCost, implemented a custom `MostAllocated` scheduler, KEDA event-driven
  autoscaling and a spot-instance strategy that saved more than 50% on data workloads;
  automated cost allocation with Power BI reporting and planned cloud reservations.
- **Network** — designed subnets and CIDR allocation, Kubernetes network policies and
  ingress/egress rules, ingress controllers with TLS termination, and Pomerium access control
  integrated with Entra ID groups; used private endpoints and private links for internal-only
  access.
- **Observability** — collected metrics and logs with Prometheus, Fluent Bit, Elastic and Loki;
  built actionable dashboards and Alertmanager notifications; instrumented custom exporters;
  and created synthetic baseline workloads (Airflow DAGs, Kafka producers/consumers) for
  active infrastructure monitoring.
- **Security** — assessed Kubernetes posture with Kubescape and kube-bench; enforced policy
  with Kyverno and Gatekeeper; synchronized secrets with External Secrets from Azure Key Vault
  and HashiCorp Vault; automated image scanning with Trivy; internalized images; enforced SAST
  with GitHub Advanced Security/CodeQL; and integrated SSO (OAuth 2.0/OIDC) across Grafana,
  Backstage, Airflow, Kafka UI and Trino.
- **SRE** — deployed and managed Kubernetes clusters for high availability and resilience;
  managed tool lifecycle and upgrades without service impact; designed backup strategies;
  performed capacity planning; defined SLIs/SLOs/SLAs; responded to incidents and ran
  post-mortems.

</div>

<div class="timeline-item" markdown>

### Data Engineer
<p class="timeline-meta">Raízen · Full-time · Apr 2022 – Jan 2023 · 10 months</p>

- Designed, developed, optimized and maintained data architecture and pipelines integrating
  internal and external systems.
- Built cleansing, transformation and aggregation pipelines with Apache Spark, orchestrated
  with Apache Airflow, delivering business insights and reports.
- Built an end-to-end pipeline with Spark and Airflow that delivered data to a SOAP API.
- Implemented a CI/CD pipeline for Azure Synapse Analytics and Azure Purview with GitHub Actions.
- Added Apache Airflow metrics observability with Grafana.
- Containerized and validated applications with Docker Compose, Redis and MongoDB.
- Delivered a real-time streaming pipeline with Kafka on Kubernetes, using Kafka Connect
  Debezium for Change Data Capture and Delta Lake as sink.

</div>

<div class="timeline-item" markdown>

### Data Engineer / Data Scientist — Career Transition
<p class="timeline-meta">Andrey Olv · Self-employed · 2021 – 2022 · Remote</p>

- Data Engineer (Jan 2022 – Apr 2022) and Data Scientist (Sep 2021 – Dec 2021): structured
  career transition from telecommunications engineering into data engineering.

</div>

<div class="timeline-item" markdown>

### Telecommunications Engineer
<p class="timeline-meta">Abix Tecnologia Ltda · Full-time · Jan 2019 – May 2021 · Curitiba, Brazil</p>

- Radiofrequency coverage studies, site surveys and radiocommunication projects (DMR and TETRA).
- Electrical installations in explosive atmospheres (ABNT NBR IEC 60079 / ATEX / IECEx).
- Preventive maintenance and site validation (Motorola R56) and grounding/lightning protection
  (ABNT NBR 5419).
- Performance analysis of radiofrequency systems with Anritsu spectrum analyzers; radio-link
  projects with Cambium Networks, Ubiquiti and 4RF.
- Installation, configuration, testing and PoC of new products and solutions; support to field
  teams and remote equipment configuration.
- Human exposure compliance reports for electromagnetic fields (ANATEL Resolution 700, Acts
  458 and 1674).

**Highlights**

- First project as Project Manager.
- Engineer responsible for the radio communication system at **Rock in Rio 2019**.
- First company PoC of a PTT-over-cellular radio solution (Wi-Fi/4G) interoperable with TETRA.
- First company BDA (Bi-Directional Amplifier) solution to extend TETRA coverage.
- First company NLOS radio link (430 MHz, 2 Mbit/s, 22 km).

</div>

<div class="timeline-item" markdown>

### Telecommunications Technician
<p class="timeline-meta">Stalker Engenharia · Full-time · Feb 2017 – Jan 2019 · Curitiba, Brazil</p>

- Field leader for telecommunications site activities: installation, relocation, hot swap,
  uninstall and configuration of equipment.
- Installed antenna sectors, cabinets, BBU/RRU, AC/DC power, duplexers, battery banks and
  optical fiber for GSM, WCDMA and LTE (2G/3G/4G) base stations.
- Radio links with SIAE, Alcatel, Huawei and Nokia; outsourced service for Claro, TIM and Vivo.
- Work at height (NR35) and electrical services (NR10), with photographic quality reports.

**Highlight** — most productive team in the Huawei project, delivering 20–40% faster within
the required quality standards.

</div>

<div class="timeline-item" markdown>

### Electrical Engineer
<p class="timeline-meta">Andrey Olv · Contract · Jul 2016 – Dec 2018 · Greater Curitiba</p>

</div>

<div class="timeline-item" markdown>

### Trainee Electrical Engineer
<p class="timeline-meta">Mondelēz International · Full-time · Feb 2016 – Jun 2016 · Curitiba, Brazil</p>

</div>

---

## Education

<div class="timeline-item" markdown>

### Bachelor of Electrical Engineering
<p class="timeline-meta">Universidade Federal do Paraná (UFPR) · 2010 – 2015</p>

Emphasis on Electronics and Telecommunications.

</div>

---

## Core skills

- **Platform & GitOps** — Kubernetes, Flux, Argo CD, Helm, Kustomize, Crossplane, Terraform,
  Backstage, Karpenter, KEDA, vCluster, YuniKorn.
- **Data engineering** — Apache Airflow, Apache Spark, Apache Kafka, Flink, Trino, dbt, Airbyte,
  Debezium, Iceberg, Delta Lake, OpenMetadata, Great Expectations, Soda, MLflow.
- **Cloud** — AWS and Microsoft Azure (AKS, Synapse, Databricks, Key Vault, Entra ID, networking,
  governance and cost management).
- **Observability** — Prometheus, Grafana, Loki, Fluent Bit, OpenTelemetry, Tempo, Thanos,
  Alertmanager, Pyroscope.
- **Security** — Kyverno, Gatekeeper, External Secrets Operator, HashiCorp Vault, cert-manager,
  Trivy, Cosign, Falco, Tetragon, Kubescape, kube-bench, OpenSSF Scorecard, SAST/DAST.
- **FinOps** — Kubecost, OpenCost, Vertical Pod Autoscaler, KEDA, spot instances, reservations
  and cost-allocation reporting.
- **SRE** — Velero backups and recovery, Flagger progressive delivery, Litmus chaos engineering,
  high availability, SLOs and disaster recovery.
- **Databases** — PostgreSQL, MySQL, Redis, MongoDB, Cassandra, Neo4j.
- **Networking** — Cilium, NGINX Ingress, Gateway API, MetalLB, Istio, Pomerium, Kong.
- **Languages** — Python, Go, Bash, SQL, JavaScript, HCL.

---

## Certifications

**Golden Kubestronaut** — all 15 CNCF Kubernetes certifications, with **35+ certifications**
in total across Kubernetes, cloud, data and platform engineering.

Highlights: CKA, CKAD, CKS, KCNA, KCSA, CNPA, CGOA, CAPA, CBA, ICA, KCA, OTCA, CCA, PCA,
LFCS, AWS Solutions Architect – Associate, Azure Data Engineer Associate, HashiCorp Terraform
and Vault Associate, Confluent Kafka Developer, Databricks Data Engineer Associate.

---

## Awards & community

- **Kubestronaut** — Cloud Native Computing Foundation (CNCF), Jul 2024.
- **Golden Kubestronaut** — all 15 CNCF Kubernetes certifications maintained.
- Founder of [Universidade Livre de Dados](https://github.com/andreyolv/UniversidadeLivreDeDados),
  a free collection of 80+ academic disciplines on Big Data and AI.
- Speaker and community moderator in data and cloud-native communities.

---

## Selected work

- **Rock in Rio 2019** — responsible engineer for the TETRA trunked radio system, with
  technical responsibility (ART) at CREA-RJ.
- **Open-source contributions** — issues and discussions across Apache Airflow, Trino,
  ClickHouse, StarRocks, Redpanda, Velero, Backstage, Crossplane and External Secrets.

See the [portfolio](portfolio/README.md) for the full technical documentation.
