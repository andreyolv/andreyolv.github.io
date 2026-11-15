---
status: active
environment: production
kind: project
---

# Airflow DAG Cleanup, Organization and Ownership Governance

## Problem
- DAG Sprawl: Years of pipelines accumulated in Airflow — paused DAGs nobody remembered, DAGs that had not run successfully in months, proofs of concept left in production, and several versions of the same pipeline running side by side after rewrites.

- Wasted Compute and Query Cost: Forgotten DAGs kept running on schedule, launching Kubernetes pods, scanning data in Athena and Trino and writing tables nobody read, with their cost hidden inside the shared platform bill.

- No Clear Ownership: Many DAGs had a generic `owner`, the name of someone who had left, or no tags, so failures went to nobody and no one could decide whether a DAG was still needed.

- Noise in Operations: Failing DAGs that nobody fixed filled alert channels and dashboards, hiding the failures that mattered and making the scheduler slower to parse and schedule the whole DagBag.

- Inconsistent Organization: DAGs from different teams mixed in the same folders and repositories, with no naming convention, inconsistent tags, duplicated helper code and connections and variables that no DAG used anymore.

## Solution
- DAG Inventory from Metadata: Built an inventory of every DAG from the Airflow metadata database and REST API — paused state, schedule, last run, last success, failure rate, owner, tags and source repository — and joined it with Kubernetes and query cost per project.

- Classification for Decision: Classified each DAG as active, failing (runs but has not succeeded for a period), idle (no runs or paused for a long time), duplicated (replaced by a newer pipeline) or ownerless, because each class needs a different action and a different person to decide.

- Ownership Review with Teams: Sent each team the list of its DAGs with the evidence (last success, consumers of the output tables, cost) and assigned a real owner to every DAG kept, aligned with business areas.

- Safe Removal Process: Paused candidate DAGs first and kept them in quarantine for an observation period, checked that nobody depended on their output tables, then removed the code from the repository and cleaned their metadata, so any removal could be undone by unpausing during the window.

- Downstream Cleanup: Removed the Airflow connections, variables and pools no DAG referenced, and flagged the output tables of removed DAGs for the [Athena table cleanup](../finops/aws-cost-optimization-program.md) and data lake lifecycle policies.

- Standard Organization: Defined a naming convention (`<team>_<project>_<purpose>`), folder and repository structure per project, mandatory tags for data layer and sensitivity, and shared code moved to an internal library instead of copies in each DAG folder.

- Governance to Prevent Regression: The standards became mandatory through [Airflow cluster policies](airflow-policies.md) — owner, tags, timeout, project metadata and namespace enforced at parse time — and a recurring review of idle and failing DAGs was added to the platform routine.

## Skills
- Data Engineering

- Data Governance

- Platform Engineering

- FinOps

## Tools
- Apache Airflow

- Airflow REST API and metadata database

- Kubernetes

- Amazon Athena

- Python

- GitHub
