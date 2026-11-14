# TLS Certificate Management for AWS Services with AWS Certificate Manager

## Problem
- Certificates Bought and Installed by Hand: TLS certificates for public endpoints were purchased, uploaded and replaced manually, with private keys passed around to whoever installed them.

- Expirations Discovered by Outages: Renewal depended on someone remembering a date. An expired certificate showed up as a broken site or failing integrations before anyone noticed.

- No Inventory: Nobody knew how many certificates existed, which domains they covered, where they were attached or when each one expired.

- Inconsistent Coverage: Some internal endpoints used self-signed certificates or plain HTTP because issuing a proper certificate was too much work.

## Solution
- ACM for AWS-Integrated Endpoints: Issued certificates in AWS Certificate Manager for load balancers, CloudFront distributions and API Gateway custom domains, where ACM manages the private key and AWS installs the certificate — no key ever leaves AWS.

- DNS Validation with Automatic Renewal: Validated every certificate through DNS records in [Route 53](route53.md), so ACM renews certificates automatically before they expire, as long as the validation record exists.

- Certificate Strategy by Scope: Used specific names for production endpoints and wildcard certificates only where many subdomains share one load balancer, and issued CloudFront certificates in `us-east-1` as the service requires.

- Private Endpoints Covered: Used ACM certificates on private API Gateway custom domains and internal load balancers ([private API Gateway](api-gateway-private.md)), so internal traffic is encrypted with trusted certificates instead of self-signed ones.

- Kubernetes Ingress Certificates: Certificates for Ingresses inside Kubernetes are issued and renewed by [cert-manager](../../security/tls-certs.md); ACM covers the AWS-managed endpoints in front of them, so both paths renew without manual work.

- Inventory and Expiration Monitoring: Built an inventory of all certificates per account and region with domain, attachment and expiration, removed unused and expired certificates, and alerted through EventBridge on ACM expiration events for any certificate that cannot renew (imported certificates or missing validation records).

- Certificates as Code: Managed certificate requests, validation records and attachments in Terraform.

## Skills
- Security
- Cloud Engineering
- Cloud Networking

## Tools
- AWS Certificate Manager (ACM)
- Amazon Route 53
- Elastic Load Balancing, CloudFront and API Gateway
- Amazon EventBridge
- cert-manager
- Terraform
