# Public and Private DNS Management with Amazon Route 53

## Problem
- DNS Spread Across Providers and Consoles: Public records lived in different places, created by hand, with no history of who changed what and no clear owner for each zone.

- Internal Services Addressed by AWS Endpoints: Applications connected to databases, load balancers and APIs through generated AWS hostnames, so recreating a resource meant updating every consumer.

- No Internal Name Resolution Standard: There was no private domain for internal services, and resolving names between VPCs, accounts and on-premises networks was solved case by case.

- Risky Manual Changes: A wrong record or a deleted zone could take services offline, and dangling records pointing to deleted resources were a subdomain takeover risk.

## Solution
- Public Hosted Zones: Consolidated the company's public domains and subdomains into Route 53 public hosted zones, with delegated subdomains per environment or team where independent ownership was needed.

- Private Hosted Zones: Created a private internal domain in Route 53 private hosted zones associated with the VPCs that consume it, so internal services have stable names that resolve only inside the company's networks.

- Stable Names over AWS Endpoints: Put databases, load balancers and private APIs behind CNAME and alias records, so migrations and recreations change one record instead of application configuration ([RDS migrations](../../databases/rds-migration.md), [private API Gateway](api-gateway-private.md)).

- Multi-Account and Hybrid Resolution: Shared private zones across accounts through VPC associations, and used Route 53 Resolver inbound and outbound endpoints with forwarding rules shared through AWS RAM, so names resolve consistently between VPCs, accounts and on-premises networks.

- Records from Kubernetes: Let [ExternalDNS](../../network/external-dns.md) manage the records of Kubernetes Ingresses and Services in their own zones, with ownership records so it never touches records it did not create.

- Certificate Validation: Used Route 53 DNS validation for [ACM certificates](acm.md), so certificates are issued and renewed without manual steps.

- Safety and Hygiene: Removed dangling records pointing to deleted resources, used alias records for AWS resources so they follow the target, and enabled query logging on public zones for investigation.

- DNS as Code: Managed hosted zones, records and resolver rules in Terraform with pull request review, so every change is reviewed and versioned and a zone can be rebuilt from code.

## Skills
- Cloud Networking
- Cloud Engineering
- Security
- Platform Engineering

## Tools
- Amazon Route 53 (Public and Private Hosted Zones, Resolver)
- AWS RAM
- ExternalDNS
- AWS Certificate Manager
- Terraform
