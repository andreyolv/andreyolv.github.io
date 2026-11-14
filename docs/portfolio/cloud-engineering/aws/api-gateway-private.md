# Private Amazon API Gateway with VPC Endpoint and Private DNS

## Problem
- Internal APIs Exposed to the Internet: Internal APIs consumed only by workloads and teams inside the company were published as regional or edge API Gateway endpoints, reachable from anywhere on the internet and protected only by authentication.

- Unfriendly and Unstable Addresses: Consumers called APIs through generated URLs (`https://<api-id>.execute-api.<region>.amazonaws.com/<stage>`) that changed whenever an API was recreated, so every redeploy risked breaking clients that had hardcoded them.

- Traffic Leaving the Network: Calls from private subnets to internal APIs went out through the NAT Gateway to the public endpoint and back, adding NAT processing cost and a dependency on internet egress for internal traffic.

- Access from Other Networks: Consumers in peered VPCs and on-premises networks needed to reach the same APIs, and resolving private endpoints from outside the VPC was not solved.

## Solution
- Private REST APIs: Changed internal APIs to the private endpoint type, so they are reachable only from inside the company's networks and never from the internet.

- Interface VPC Endpoint for `execute-api`: Created an interface VPC endpoint (PrivateLink) for API Gateway in the shared network VPC, deployed across availability zones, with a security group allowing HTTPS only from the company's private ranges.

- Resource Policies Bound to the Endpoint: Attached resource policies to each private API allowing `execute-api:Invoke` only through the approved VPC endpoint (`aws:SourceVpce`), denying everything else, so even a leaked URL is useless from any other network.

- Custom Domain Names for Private APIs: Configured private custom domain names (`<api>.internal.<company-domain>`) with ACM certificates and base path mappings, so consumers use stable, readable names that do not change when an API is redeployed, and several APIs can share one domain by path.

- Private DNS with Route 53: Created Route 53 private hosted zones associated with the consuming VPCs, with alias records pointing the custom domains to the VPC endpoint, so names resolve to private IPs only inside the company's networks.

- Resolution from Peered VPCs and On-Premises: Associated the private hosted zones with peered VPCs and configured Route 53 Resolver inbound endpoints with forwarding rules on the on-premises DNS servers, so the same names resolve correctly from every connected network.

- Traffic Kept off the NAT Gateway: Calls from private subnets now go to the VPC endpoint directly over the AWS network, without NAT Gateway processing or internet egress, in line with the [VPC endpoints work](../../finops/vpc-gateway-endpoints.md).

- Infrastructure as Code: Managed the VPC endpoint, resource policies, custom domains, certificates, base path mappings, hosted zones and resolver rules in Terraform, as part of the [network architecture](network.md).

## Skills
- Cloud Networking

- Cloud Engineering

- Security

- Software Engineering

## Tools
- Amazon API Gateway

- AWS PrivateLink (Interface VPC Endpoints)

- Amazon Route 53 (Private Hosted Zones and Resolver)

- AWS Certificate Manager

- Terraform
