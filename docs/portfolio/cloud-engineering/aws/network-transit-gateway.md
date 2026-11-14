# Multi-Account AWS Network Architecture Planning Ready for Transit Gateway

## Problem
- Point-to-Point Connectivity: VPCs were connected through individual VPC peerings that grew with every new account. Peering is not transitive, so each new connection needed new peerings, routes and security rules on both sides.

- Overlapping CIDRs: VPCs had been created with default or repeated ranges, so some networks could never be connected to each other or to on-premises without readdressing.

- No Central Point for Shared Services and Egress: Every VPC had its own NAT Gateways, endpoints and DNS configuration, multiplying cost, and there was no single place to inspect or control traffic between environments.

- Growth Without a Plan: New accounts and clusters were created with whatever network was convenient at the time, which made future consolidation harder each time.

## Solution
- Target Architecture: Designed a hub-and-spoke architecture with AWS Transit Gateway as the hub, connecting workload VPCs (spokes) per account and environment, a shared services VPC and the on-premises connection, replacing the mesh of peerings.

- IP Address Plan: Defined a company-wide, non-overlapping CIDR plan per region, environment and account with room for growth, aligned with the [Kubernetes subnet sizing](network.md), and planned AWS VPC IPAM to allocate ranges so new VPCs cannot overlap.

- Compatibility First: Any new VPC is created from the plan with a non-overlapping range and dedicated small subnets for Transit Gateway attachments in every availability zone, so it can be attached later without readdressing, even before the Transit Gateway exists.

- Segmentation with Route Tables: Planned separate Transit Gateway route tables for production, non-production and shared services, so environments are isolated by routing and only reach the shared services and on-premises routes they need.

- Centralized Shared Services: Planned interface VPC endpoints, DNS resolution through [Route 53 Resolver](route53.md) and, where it pays off, centralized egress through the shared services VPC, reducing duplicated NAT Gateways and endpoints across VPCs.

- Hybrid Connectivity: Designed the on-premises connection to terminate on the Transit Gateway (VPN, with Direct Connect as the growth path), so every spoke reaches on-premises through one attachment instead of individual tunnels.

- Inspection Path: Left room in the design for a centralized inspection VPC (AWS Network Firewall) between spokes and for egress, to be added without changing the spokes.

- Cost and Migration Plan: Compared Transit Gateway attachment and data processing costs with the current peering and NAT costs using [data transfer visibility](../../finops/data-transfer-visibility.md), and defined a phased migration — new VPCs first, then legacy VPCs as they are cleaned up ([network hygiene](network-cleanup.md)) — with Terraform modules for every component.

## Skills
- Cloud Networking
- Cloud Architecture
- Cloud Engineering
- FinOps

## Tools
- AWS Transit Gateway
- Amazon VPC and VPC IPAM
- AWS Site-to-Site VPN and Direct Connect
- Amazon Route 53 Resolver
- AWS Network Firewall
- AWS RAM
- Terraform
