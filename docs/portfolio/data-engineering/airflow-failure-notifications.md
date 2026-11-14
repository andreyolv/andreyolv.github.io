# Standardized Airflow Failure Notifications through Cluster Policy Mutation

## Problem
- Every DAG Notified Differently: Each team wrote its own failure callbacks — some sent email, some posted to chat, some did nothing — with different formats and different levels of detail.

- Notifications Without Context: Many alerts said only that a task failed, without the DAG owner, the project, the execution date, the error or a link to the logs, so the first minutes of every incident were spent finding basic information.

- Silent Failures: DAGs without callbacks failed with nobody notified, and the problem was discovered when a downstream consumer complained about missing data.

- Copy-Pasted Callback Code: The same notification code was duplicated in hundreds of DAG files, so improving the message or changing the destination meant editing every repository.

## Solution
- Cluster Policy Mutation: Used Airflow cluster policies (`task_policy`) to inject a standard `on_failure_callback` into every task at parse time, so all DAGs notify the same way without any code in the DAG files.

- One Standard Message: Defined a single failure message with the DAG and task IDs, owner, project, logical date, try number, the error summary and direct links to the task log and the DAG in the Airflow UI.

- Routing by Owner and Project: The callback reads the `owner` and the project metadata that the [Airflow cluster policies](airflow-policies.md) already make mandatory, and routes each notification to the channel of the team that owns the DAG, with email as fallback.

- Respecting Existing Callbacks: The mutation chains the standard callback with any callback a DAG already defines instead of replacing it, so teams with specific needs keep their behaviour.

- Noise Control: Notifications are sent only on the final failure after retries, not on every retry, and repeated failures of the same task are grouped, so alerts stay actionable.

- Central Maintenance: The callback lives in the platform's shared Airflow package, so changing the message, adding a link or moving to another channel is one change deployed with the Airflow image.

## Skills
- Data Engineering

- Platform Engineering

- Observability

## Tools
- Apache Airflow (cluster policies, callbacks)

- Python

- Kubernetes
