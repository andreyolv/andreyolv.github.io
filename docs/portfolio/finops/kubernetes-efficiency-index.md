# Kubernetes Resource Efficiency Index per Namespace and Workload

## Problem
- Dashboards Without a Number to Act On: Teams had dashboards comparing requests and usage, but a page of graphs does not say which team is wasteful, whether things are getting better, or where to start.

- Requests Far Above Usage: Workloads requested CPU and memory "just in case", reserving node capacity that sat idle, so the cluster scaled out nodes for resources nobody used.

- No Shared Target: Without a common metric, efficiency discussions were opinions, and there was no way to set a goal or to recognise teams that improved.

## Solution
- Efficiency Index: Defined a resource efficiency index as actual usage divided by requested resources, calculated separately for CPU and memory over a rolling window (using a high percentile of usage instead of the average, so bursty workloads are not penalised for headroom they need).

- Calculated per Level: Computed the index per container, workload, namespace and project from Prometheus metrics (`container_cpu_usage_seconds_total`, `container_memory_working_set_bytes` and the requests from kube-state-metrics), with recording rules so dashboards stay fast.

- Weighted by Cost: Combined the index with cost per namespace from [OpenCost](opencost.md), so the ranking shows idle capacity in money and the largest absolute waste is fixed first, not just the lowest percentage.

- Efficiency Bands: Classified workloads into bands — overprovisioned, healthy and underprovisioned (usage above requests, at risk of throttling, OOM kills or eviction) — so the index points to both waste and reliability risk.

- Dashboards and Ranking: Extended the [resource advisor dashboards](grafana-resource-advisor.md) with the index per team and its trend over time, and a ranking of the workloads with the most idle requested capacity and a suggested request based on observed usage.

- Targets and Review: Set a target index per environment, reviewed it in the monthly FinOps routine with each team, and tracked improvement after rightsizing.

- From Index to Action: Rightsizing recommendations from [VPA](vpa.md) in recommendation mode and the dashboards guided teams to lower requests, which let [Karpenter](karpenter.md) consolidate workloads on fewer nodes.

## Skills
- FinOps

- Kubernetes

- Observability

- Platform Engineering

## Tools
- Prometheus and kube-state-metrics

- Grafana

- OpenCost

- Vertical Pod Autoscaler

- Karpenter
