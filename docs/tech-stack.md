---
hide:
- toc
---

# Tech Stack — Global Overview

Below is a map of the technologies, tools, and skills I work with, organized by domain. Levels indicate my familiarity and production usage:

<div class="stack-legend" markdown>
- <span class="stack-chip level-4">4</span> **4 — Expert:** I use it routinely in production and architect solutions with it.
- <span class="stack-chip level-3">3</span> **3 — Advanced:** I use it autonomously in real projects.
- <span class="stack-chip level-2">2</span> **2 — Intermediate:** I know it well, have used it in projects or advanced studies.
- <span class="stack-chip level-1">1</span> **1 — Knowledge:** I understand the concept and have had initial contact.
</div>

<style>
.stack-legend { display: flex; flex-wrap: wrap; gap: 1rem; margin: 1.5rem 0; font-size: 0.9rem; align-items: center; }
.stack-chip { width: 26px; height: 26px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 0.7rem; color: #fff; font-weight: 700; }
.level-4 { background: #6200ee; }
.level-3 { background: #03dac6; color: #000; }
.level-2 { background: #ffb74d; }
.level-1 { background: #9e9e9e; }

.stack-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; margin-top: 1.5rem; }
.stack-domain { border: 1px solid var(--md-default-fg-color--lighter, #e0e0e0); border-radius: 0.75rem; padding: 1rem 1.25rem; background: var(--md-default-fg-color--lightest, #fafafa); }
.stack-domain h3 { margin: 0 0 0.75rem 0; font-size: 1.05rem; border-bottom: 2px solid var(--md-primary-fg-color, #6200ee); padding-bottom: 0.4rem; }
.stack-list { list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(120px, 1fr)); gap: 0.6rem; }
.stack-item { display: flex; flex-direction: column; align-items: center; gap: 0.35rem; font-size: 0.8rem; }
.stack-item .chip { width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; color: #fff; font-weight: 700; }
.stack-item .name { text-align: center; line-height: 1.25; }
</style>

<div class="stack-legend" markdown>
<span class="stack-chip level-4">4</span> Expert
<span class="stack-chip level-3">3</span> Advanced
<span class="stack-chip level-2">2</span> Intermediate
<span class="stack-chip level-1">1</span> Knowledge
</div>

<div class="stack-grid">

<div class="stack-domain">
<h3>☁️ Cloud</h3>
<ul class="stack-list">
<li class="stack-item"><span class="chip level-4">4</span><span class="name">AWS</span></li>
<li class="stack-item"><span class="chip level-4">4</span><span class="name">Azure</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">GCP</span></li>
</ul>
</div>

<div class="stack-domain">
<h3>🚀 Platform &amp; GitOps</h3>
<ul class="stack-list">
<li class="stack-item"><span class="chip level-4">4</span><span class="name">Kubernetes</span></li>
<li class="stack-item"><span class="chip level-4">4</span><span class="name">Flux</span></li>
<li class="stack-item"><span class="chip level-4">4</span><span class="name">Argo CD</span></li>
<li class="stack-item"><span class="chip level-4">4</span><span class="name">Helm</span></li>
<li class="stack-item"><span class="chip level-4">4</span><span class="name">Terraform</span></li>
<li class="stack-item"><span class="chip level-4">4</span><span class="name">GitHub Actions</span></li>
<li class="stack-item"><span class="chip level-4">4</span><span class="name">Docker</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">OpenTofu</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Crossplane</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Kustomize</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">KEDA</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Karpenter</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Backstage</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">vCluster</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">YuniKorn</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">KRO</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">CNPG</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">VPA</span></li>
</ul>
</div>

<div class="stack-domain">
<h3>🌐 Networking</h3>
<ul class="stack-list">
<li class="stack-item"><span class="chip level-4">4</span><span class="name">NGINX</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Istio</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Envoy Gateway</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Gateway API</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Cilium</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Pomerium</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">MetalLB</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">Kong</span></li>
</ul>
</div>

<div class="stack-domain">
<h3>📊 Observability &amp; SRE</h3>
<ul class="stack-list">
<li class="stack-item"><span class="chip level-4">4</span><span class="name">Prometheus</span></li>
<li class="stack-item"><span class="chip level-4">4</span><span class="name">Grafana</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">OpenTelemetry</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Loki</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Tempo</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Fluent Bit</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Alertmanager</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Velero</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Flagger</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">OpenCost</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">Thanos</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">Litmus</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">Pyroscope</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">Retina</span></li>
</ul>
</div>

<div class="stack-domain">
<h3>🔐 Security</h3>
<ul class="stack-list">
<li class="stack-item"><span class="chip level-4">4</span><span class="name">HashiCorp Vault</span></li>
<li class="stack-item"><span class="chip level-4">4</span><span class="name">External Secrets</span></li>
<li class="stack-item"><span class="chip level-4">4</span><span class="name">Trivy</span></li>
<li class="stack-item"><span class="chip level-4">4</span><span class="name">OAuth 2 / OIDC</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Kyverno</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Gatekeeper</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Falco</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Cosign</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">cert-manager</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Kubescape</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">kube-bench</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">Tetragon</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">OpenSSF Scorecard</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">SAST/DAST</span></li>
</ul>
</div>

<div class="stack-domain">
<h3>📈 Data Engineering, Streaming &amp; Governance</h3>
<ul class="stack-list">
<li class="stack-item"><span class="chip level-4">4</span><span class="name">Airflow</span></li>
<li class="stack-item"><span class="chip level-4">4</span><span class="name">Spark</span></li>
<li class="stack-item"><span class="chip level-4">4</span><span class="name">Kafka</span></li>
<li class="stack-item"><span class="chip level-4">4</span><span class="name">dbt</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Trino</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Flink</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Airbyte</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Debezium</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Iceberg</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Delta Lake</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">OpenMetadata</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Metabase</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">DuckDB</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">ksqlDB</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">Schema Registry</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">OpenLineage</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">MLflow</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">Great Expectations</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">Soda</span></li>
</ul>
</div>

<div class="stack-domain">
<h3>🗄️ Databases</h3>
<ul class="stack-list">
<li class="stack-item"><span class="chip level-4">4</span><span class="name">PostgreSQL</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">MySQL</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">Redis</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">MongoDB</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">StarRocks</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">ClickHouse</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">MSSQL</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">Cassandra</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">Neo4j</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">Valkey</span></li>
</ul>
</div>

<div class="stack-domain">
<h3>💻 Languages</h3>
<ul class="stack-list">
<li class="stack-item"><span class="chip level-4">4</span><span class="name">Python</span></li>
<li class="stack-item"><span class="chip level-4">4</span><span class="name">Go</span></li>
<li class="stack-item"><span class="chip level-4">4</span><span class="name">Bash</span></li>
<li class="stack-item"><span class="chip level-4">4</span><span class="name">SQL</span></li>
<li class="stack-item"><span class="chip level-3">3</span><span class="name">HCL</span></li>
<li class="stack-item"><span class="chip level-2">2</span><span class="name">JavaScript</span></li>
</ul>
</div>

</div>

> Adjust the levels (`level-1` to `level-4`) according to your real experience. Later, I can help turn this into a circular radar chart summarized by domain.
