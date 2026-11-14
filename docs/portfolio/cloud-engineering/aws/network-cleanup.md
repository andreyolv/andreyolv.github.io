# AWS Network Hygiene: Cleanup of Unused Network Components and Security Groups

## Problem
- Leftover Network Components: Years of projects left VPCs, subnets, route tables, NAT Gateways, Elastic IPs, VPC peerings, VPN and Transit Gateway attachments, endpoints and load balancers that no workload used anymore — some of them billed every hour.

- Security Group Sprawl: Hundreds of security groups with generic names (`launch-wizard-*`, `default`, copies of copies), many attached to nothing, others attached to resources long gone through network interfaces left behind, and no way to tell which ones were still needed.

- Overly Permissive Rules: Rules opening SSH, RDP and database ports to `0.0.0.0/0`, wide CIDR ranges "for testing", and rules referencing deleted security groups or IP ranges of partners and offices that no longer existed.

- Hard to Reason About the Network: With unused routes, peerings and rules mixed with real ones, every network change and every security review started by figuring out what was actually in use.

- Findings that Never Closed: Security scanners kept reporting open ports, unused Elastic IPs and the default security group allowing traffic, with no process to resolve them.

## Solution
- Network Inventory: Inventoried every VPC, subnet, route table, gateway, Elastic IP, peering, endpoint, load balancer, network interface and security group across accounts and regions, with their attachments and tags.

- Usage Evidence: Used network interface attachments to find security groups and subnets associated with nothing, VPC Flow Logs and CloudWatch metrics to confirm that gateways, load balancers, peerings and endpoints carried no traffic, and CloudTrail to see when each component was last changed and by whom.

- Removal in Dependency Order: Removed unused components from the leaves up — orphaned network interfaces, unassociated Elastic IPs, idle load balancers and NAT Gateways, unused endpoints and peerings, empty subnets and route tables, and finally entire legacy VPCs — with owners notified and a quarantine period before each deletion.

- Security Group Hygiene: Deleted security groups not attached to any network interface, removed rules that referenced deleted groups or obsolete CIDRs, and replaced rules open to the internet with references to other security groups or to private ranges, keeping public exposure only on load balancers that need it.

- Default Security Groups Locked: Removed all inbound and outbound rules from the default security group of every VPC, so a resource launched without an explicit group gets no access instead of the default one.

- Naming and Ownership Standard: Defined naming and mandatory `team` and `project` tags for security groups and network components ([tag policy](../tag-policy.md)), and rules described with their purpose, so the next review starts from known ownership.

- Managed as Code: Brought the remaining network and security group definitions into Terraform, as part of the [network architecture](network.md), so new rules go through pull request review instead of console edits.

- Continuous Checks: Prowler findings for unused security groups, open administrative ports, unattached Elastic IPs and default security groups allowing traffic are tracked in the [security findings remediation](../../security/security-findings-remediation.md) process, and unused network resources are part of the [resource decommissioning](../../finops/resource-reclamation.md) routine.

## Skills
- Cloud Networking
- Security
- Cloud Engineering
- FinOps

## Tools
- Amazon VPC and Security Groups
- VPC Flow Logs
- AWS CloudTrail
- Amazon CloudWatch
- Prowler
- Terraform
