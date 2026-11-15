# Self-Hosted LLM Inference on Kubernetes with llmkube and llama.cpp

## Problem
- Every Model Is a Hand-Written Deployment: llama.cpp ships a server image and nothing else — no chart, no operator. Serving a model on Kubernetes means writing a Deployment that downloads the weights, a volume to keep them, the right `llama-server` flags, probes that understand "still loading" and a Service, and repeating all of it for every model.

- Unverified Weights in Production: Model files are pulled from public hubs at runtime. Without a checksum, a changed, truncated or replaced file is served silently, and nobody can say which artefact answered a given request.

- Floating Runtime Versions: The upstream inference image is published under a moving tag, so a pod restart can change the llama.cpp build underneath a model without any change in Git.

- GPU-Centred Platforms for CPU Workloads: Most Kubernetes inference platforms assume NVIDIA GPUs and high-throughput engines. Small and quantised models that run well on CPU have no first-class path, and the cost of GPU nodes is paid for workloads that do not need them.

- Inference Without Observability: A self-hosted model is a production service with latency, throughput and memory behaviour of its own. Deployed by hand, it has no metrics, no dashboards and no readiness signal anyone else can consume.

- Direct Access to Models: Applications calling a model endpoint directly have no budgets, no rate limits and no attribution of usage per team, so cost and abuse are invisible until they become a problem.

## Solution
- Declarative Inference with Two Resources: Adopted llmkube, an operator that turns model serving into a `Model` (where the weights come from) and an `InferenceService` (how to serve them). The operator downloads the weights, creates the Deployment and Service, and reports readiness on the resource, so a new model is a pull request with two short manifests instead of a hand-written Deployment.

- GitOps Installation with Flux: Installed the operator, its CRDs and admission webhook through a Flux `HelmRelease` sourced from an `OCIRepository` pinned by tag and digest, so chart updates arrive as Renovate pull requests and what was reviewed is exactly what is installed. Scheduling follows the platform's namespace-level node pool policy, enforced by Kyverno, with no node selectors in the manifests.

- Verified Model Supply Chain: Declared every model with a direct URL to the GGUF file and its `sha256`, so the download is verified before anything is served, and a model is identified by the hash of its content rather than by a file name.

- Pinned Runtime Builds: Pinned the llama.cpp server image to an explicit build in every `InferenceService`, replacing the operator's floating default, so the runtime only changes through a reviewed change in Git.

- CPU-First, Cost-Aware Serving: Served quantised models (`Q4_K_M`) on CPU with explicit CPU, memory and context-size budgets, sized together because memory grows with the context window. Small models run on general-purpose nodes, and GPU capacity is reserved for the workloads that require it.

- Per-Service Model Cache: Configured the operator's model cache per `InferenceService`, giving each service its own volume in its own namespace instead of a single shared cache that requires RWX storage and cannot reach other namespaces. The trade-off — a model used by two services is downloaded twice — was accepted for namespace isolation and simpler storage requirements.

- Built-In Observability: Enabled the operator's `ServiceMonitor` and inference `PodMonitor` for the Prometheus Operator, and provisioned its Grafana dashboards as Grafana Operator resources in a dedicated folder, limited to the ones the cluster's hardware can populate. The llama.cpp runtime dashboard is published only while a llama.cpp service exists, so no dashboard renders empty.

- OpenAI-Compatible Endpoint Behind a Gateway: Exposed each model through an OpenAI-compatible API and placed it behind the LiteLLM gateway, where teams receive virtual keys with budgets and rate limits and every request is attributed to a team. Applications hold a scoped key, never direct access to the model.

- Documented Exit Path: Recorded the project's maturity (`v1alpha1` CRDs, single-company stewardship) as an explicit risk. What the operator generates is an ordinary Deployment running the upstream `llama-server` image, so leaving it means writing that Deployment by hand rather than re-platforming.

## Skills
- MLOps

- Platform Engineering

- Kubernetes

- GitOps

- Observability

## Tools
- llmkube

- llama.cpp

- Kubernetes

- Flux

- Helm

- Kyverno

- Prometheus Operator

- Grafana Operator

- LiteLLM

- Renovate

## Related
- [Local LLM Inference with llama.cpp on Constrained Hardware](local-llama-cpp.md) — the local counterpart and why it was not viable on laptop hardware.
