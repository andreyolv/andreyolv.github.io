# Local Multi-Cloud Emulation for AWS, Azure and GCP Development with Floci

## Problem
- Every Test Needed a Cloud Account: Engineers tested Terraform modules, SDK code, Lambda functions and data pipelines against shared development accounts, which meant credentials on laptops, waiting for access, and changes colliding with other people's work.

- Cost and Clutter in Development Accounts: Experiments created buckets, queues, databases and functions that were billed and frequently forgotten, adding to the waste the FinOps work later had to clean up.

- Slow Feedback Loop: Every change required a deploy to the cloud to be tested, so a typo in an IAM policy or an event payload took minutes to discover instead of seconds, and CI pipelines depended on cloud credentials and network access.

- LocalStack Community Edition Sunset: The local AWS emulation was built on LocalStack, whose community edition was sunset in March 2026 — an auth token became mandatory and security updates stopped on the last free build. Staying on it meant either a paid licence or an unmaintained image.

- AWS Only: The platform also runs on Azure and has GCP workloads, but local emulation covered only AWS. Azure development had Azurite for storage and nothing for Service Bus, Event Hubs, Key Vault or Cosmos DB; GCP depended on separate per-service emulators.

## Solution
- Migration from LocalStack to Floci: Replaced LocalStack with Floci, an MIT-licensed AWS emulator that needs no account or auth token and listens on the same port (`4566`). For applications, SDKs, the AWS CLI and Terraform the migration was an endpoint change and nothing else.

- One Local Stack for Three Clouds: Extended local emulation to all three providers with the Floci runtimes, each on its own port:
  - AWS — `floci` on `4566`: S3, DynamoDB, SQS, SNS, Lambda, Kinesis, IAM, RDS, ECS, EKS, MSK and more.
  - Azure — `floci-az` on `4577`: Blob, Queue and Table, Cosmos DB, Service Bus, Event Hubs, Key Vault, Functions, Azure SQL and PostgreSQL flexible server.
  - GCP — `floci-gcp` on `4588`: Cloud Storage, Pub/Sub, Firestore, Secret Manager, Cloud Run, Cloud Functions and Cloud SQL.

- Single Console: Added `floci-ui`, an AWS-Console-style web UI that reads the real state of the three runtimes at once, so engineers can inspect buckets, queues and messages without CLI commands.

- Realistic Behaviour: Services such as Lambda, RDS, ECS, EKS, Azure Functions and Cloud SQL run as real containers instead of in-process mocks, with persistent or memory storage per use case, so tests exercise behaviour close to the cloud.

- Standard Developer Setup: Packaged the multi-cloud environment as a `docker compose` profile, part of the [local development environment](../platform-engineering/dev-env-local.md), with SDK, CLI and Terraform provider configuration pointing at the local endpoints per cloud.

- Terraform and Pipelines Tested Locally: Terraform modules are applied against the emulators before reaching a cloud account, and data pipelines and event-driven code are tested end to end on the laptop.

- CI without Cloud Credentials: Integration tests run in CI against Floci through Testcontainers modules (Java, Node and Python) or the compose profile, so pipelines need no cloud credentials and leave no resources behind.

- Clear Limits: Emulators are used for development and integration tests, not as proof that something works in the cloud. IAM evaluation, quotas, networking and newer services (several GCP services, BigQuery in particular, are still early) are validated in a real development account before production.

## Skills
- Cloud Engineering
- Software Engineering
- DevOps
- FinOps

## Tools
- Floci (AWS), Floci-AZ (Azure), Floci-GCP (GCP)
- Floci UI
- LocalStack (replaced)
- Docker Compose
- Testcontainers
- Terraform
- AWS CLI and SDKs
