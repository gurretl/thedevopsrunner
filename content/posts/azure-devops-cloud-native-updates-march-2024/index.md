---
title: "Azure DevOps & Cloud-Native Updates - March 2024"
date: 2024-04-01
draft: false
description: "Get all last updates related to Kubernetes, DevOps and containers on Azure Cloud."
tags: ['DevOps', 'Kubernetes', 'AKS']
categories: ['Azure']
showAuthor: true
authors:
  - "lionelgurret"
---

------------------------------------------------------------------------------------
---
# Azure DevOps & Cloud-Native Updates - March 2024

## Introduction

**Welcome to our Monthly Azure DevOps and Cloud Tech Updates Series!**

Welcome to my monthly blog series where we bring you a concise roundup of significant Azure updates pertinent to DevOps, keeping you in the loop with the latest advancements.

Let's explore the limitless possibilities with Azure together!

![](015_01.webp)

## AppService

### GA: Automatic Scaling for App Service Web Apps

Azure App Service is pleased to announce general availability of the "Automatic Scaling" feature. We received important feedback about the Automatic Scaling feature during the preview phase and have made following enhancements to the Automatic Scaling feature.  

[Learn more.](https://learn.microsoft.com/en-us/azure/app-service/manage-automatic-scaling?tabs=azure-portal)

## AKS

### GA: Cost analysis add-on for AKS

Cost analysis add-on for AKS is now Generally Available. This Azure-native experience provides visibility into underlying cluster infrastructure costs associated with your AKS workloads. Costs are broken down by Kubernetes constructs such as cluster and namespace in addition to Azure asset categories. View cost allocation data directly in the Cost Management blade of Azure portal.

Cost analysis add-on for AKS helps you tackle everyday cost monitoring, allocation, and cost optimization scenarios.

[Learn more.](https://aka.ms/aks/docs/cost-analysis)

### GA: Windows Gen 2 VM support in AKS

Gen 2 VM SKUs are now generally available for Windows on AKS. Azure Generation 2 (Gen2) virtual machines (VMs) support key features not supported in generation 1 VMs (Gen1). This enables you to bring Windows workloads to the cloud native platform more easily.

Key features for Gen 2 VMs include increased memory, Intel Software Guard Extensions (Intel SGX), and virtualized persistent memory (vPMEM). Generation 2 VMs use the new UEFI-based boot architecture rather than the BIOS-based architecture used by generation 1 VMs.

Only specific SKUs and sizes support Gen2 VMs. Check the list of supported sizes, to see if your SKU supports or requires Gen2. Gen2 VMs on Windows are supported for WS2022 only.

[Learn more.](https://aka.ms/aks/windowsgen2vm)

### GA: Kubernetes 1.29 support in AKS

AKS now supports the latest Kubernetes 1.29 preview release (mandala) that has some much-awaited features such as ReadWriteOncePod, PersistentVolume access mode, Node volume expansion Secret support for CSI drivers, and more.

### GA: Custom kubelet configuration for Windows in AKS

Custom kubelet configuration for Windows is now generally available in AKS. It allows you to modify certain default supported kubelet parameters for your Windows nodepools.

Currently supported parameters can be found in the AKS documentation. If you’d like additional parameters supported, make a request on our [AKS Github](https://github.com/Azure/AKS/issues).

[Learn more.](https://aka.ms/aks/customnodeconfiguration)

### GA: Azure CNI overlay dual stack Support in AKS (Linux only)

This feature introduces dual stack networking in AKS using overlay networking, allowing nodes and pods to have both IPv4 and IPv6 addresses, enhancing connectivity and application compatibility.

[Learn more.](https://learn.microsoft.com/azure/aks/azure-cni-overlay?tabs=kubectl%23dual-stack-networking)

### GA: VM IP based load balancer in AKS

VM IP based load balancer feature, now generally available, introduces the capability to switch the inbound pool type in AKS, improving update and provisioning efficiency for services utilizing load balancers, particularly beneficial for clusters with large numbers of nodes.

[Learn more.](https://learn.microsoft.com/azure/aks/load-balancer-standard%23change-the-inbound-pool-type)

### GA: Host Network Security Group (NSG) control in AKS

You can now specify allowed host ports on node pools and add these pools to Application Security Group by directly configuring allowed ports in your node pool settings.

For AKS nodes with public IPs hosting services, you must add a Network Security Group (NSG) rule to allow traffic. When you specify ports in the node pool configuration, it automatically creates "allow" rules in the cluster's NSG. This enhances security and traffic management for AKS nodes using public IPs.

[Learn more.](https://learn.microsoft.com/azure/aks/use-node-public-ips#allow-host-port-connections-and-add-node-pools-to-application-security-groups)

### GA: HostPort auto assign in AKS

HostPort auto assign feature in AKS, now generally available, enables the automatic assignment of host ports for pod workloads, streamlining the deployment process for services requiring direct access to a node's public IP without an intermediary like a load balancer.

[Learn more.](https://learn.microsoft.com/azure/aks/use-node-public-ips%23automatically-assign-host-ports-for-pod-workloads)

### GA: Azure Kubernetes Service (AKS) support for 5K Node limit by default for standard tier clusters

Azure Kubernetes Service (AKS) now supports up to 5000 Node limit by default in the Standard and Premium Pricing. This feature allows large workloads such as batch processing Jobs, Machine learning, simulations and multi-tenanted clusters to run at large scale with greater performance as AKS will Automatically scale up the Kubernetes control plane based on the load in the cluster.

This feature enhances not just the number of nodes you can run in a cluster but increases the overall scale envelope (number of pods, services, CRDs) of AKS clusters in accordance with the upstream kubernetes scale limits.

Both existing and new AKS clusters using the standard tier now get greater scalability and performance for Kubernetes control plane, up-to a maximum of 5,000 nodes and 200,000 pods per cluster.

[Learn more.](https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-run-at-scale)

## Azure Container Apps

### GA: Free managed certificates on Azure Container Apps

Free managed certificates on Azure Container Apps is now generally available!

Getting a certificate free of cost for your apps and without having to worry about the management of the certificate’s life cycle has now become a standard that customers expect from services. Azure Container Apps now provides a free managed certificate for your custom domain. Without any action required from you, this TLS/SSL server certificate is automatically renewed as long as your app continues to meet the requirements for managed certificates.

[Learn more.](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates?pivots=azure-portal)

### Public Preview: Tomcat support in Azure Container Apps

Azure Container Apps now supports Apache Tomcat in the code-to-cloud build process.  This means that you can use your existing code, and configuration, to create a cloud-native container app without the hassle.

This feature is currently available in public preview.

### Public preview: Support for Key Vault Certificates in Azure Container Apps

You can now use Azure Key Vault to store and manage your own TLS/SSL certificates for use with Azure Container Apps at the app and environment level. This follows security best practices by leveraging managed identities and simplifies management tasks like auto-rotation.

This feature is currently available in the Azure CLI and ARM, with some support for portal. Full portal support will be added over the next few months.

[Learn more.](https://aka.ms/aca/keyvault)

[Learn more.](https://learn.microsoft.com/en-us/azure/container-apps/java-deploy-war-file)

### Public Preview: JVM memory fit in Azure Container Apps

Default JVM settings are not optimal for the container environment. Under and overallocated JVM memory can both play a heavy toll on Java application health.  
All Java apps are now calibrated with JVM memory defaults for better performance and reliability in container environment.  
This feature is now available in public preview.

[Learn more.](https://aka.ms/JVM-memory-fit)

### Public Preview: Managed Java components in Azure Container Apps

You can use managed Java components to access platform features for your apps that you would otherwise have to manage yourself. Azure Container Apps now offers Spring Cloud Eureka and Spring Cloud Config server for service registration and externalized application settings in all environments.

This feature is available in public preview.

![](015_02.webp)

## App Gateway

### Retirement: Support for Application Gateway Web Application Firewall v2 Configuration is ending

On 15 March 2027, the Application Gateway WAF v2 Configuration will be retired. To continue using this service, switch to the Application Gateway WAF v2 Policy before the retirement date.

[Learn more.](https://azure.microsoft.com/fr-fr/updates/retirement-support-for-application-gateway-web-application-firewall-v2-configuration-is-ending/)

## Azure Monitor

### Azure Monitor managed service for Prometheus now supports TLS & mTLS based scraping

Azure Monitor managed service for Prometheus now supports TLS & mTLS based scraping for Prometheus instance served with TLS. To enable TLS and mTLS based scraping, you can configure the TLS settings in the ConfigMap, and provide a CA certificate to verify the authenticity of the server’s certificate. 
[Learn more.](https://learn.microsoft.com/azure/azure-monitor/containers/prometheus-metrics-scrape-configuration#tls-based-scraping)

## Azure Functions

### GA: Azure Functions Support for Node.js 20

Azure Functions support for Node.js 20 is now Generally Available.
You can now develop functions using Node.js 20 locally and deploy them to all Azure Functions plans on Linux and Windows.

## Network

### GA: Application Gateway (v2) IPv6 support

We are announcing that IPv6 support for Azure Application Gateway (v2) is now generally available.

With the addition of IPv6 support, you can take advantage of the increased address space and improved routing efficiency that IPv6 provides. This is especially important for customers who are running out of IPv4 addresses or who need to support IPv6 clients. To get started with IPv6 support for Azure Application Gateway (v2), simply create a new Application Gateway and select both IPv4 and IPv6 frontends during the creation process.

[Learn more.](https://learn.microsoft.com/en-us/azure/application-gateway/ipv6-application-gateway-portal)

## FinOps

### You can now opt in automatically renew your reservation at time of purchase.

You can now opt in automatically renew your reservation at time of purchase. You can renew reservations to automatically purchase a replacement when an existing reservation expires. Automatic renewal provides an easy way to continue getting reservation discounts. It also saves you from having to closely monitor a reservation's expiration. With automatic renewal, you prevent savings benefits loss by not having to manually renew. The renewal setting is turned off by default. Enable or disable the renewal setting anytime, up to the expiration of the existing reservation. 

Learn more here: [Automatically renew Azure reservations - Microsoft Cost Management | Microsoft Learn](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/reservation-renew)

### Now available: Free data transfer out to internet when leaving Azure

We support customer choice, including the choice to migrate your data away from Azure.  

Azure now offers free egress for customers leaving Azure when taking their data out of the Azure infrastructure via the internet to switch to another cloud provider or an on-premises data center. Azure already offers the first 100GB/month of egressed data for free to all customers in all Azure regions around the world. If you need to egress more than 100GB/month, please follow these steps to claim your credit.  Contact Azure Support for details on how to start the data transfer-out process. Please comply with the instructions to be eligible for the credit. Azure Support will apply the credit when the data transfer process is complete and all Azure subscriptions associated to the account have been canceled. 

The exemption on data transfer out to the internet fees also aligns with the European Data Act and is accessible to all Azure customers globally and from any Azure region. 

[Learn more.](https://learn.microsoft.com/azure/cost-management-billing/manage/cancel-azure-subscription#what-data-transfer-fees-are-applied-when-moving-all-data-off-azure)https://learn.microsoft.com/azure/cost-management-billing/manage/cancel-azure-subscription#what-data-transfer-fees-are-applied-when-moving-all-data-off-azure

## Sources

[Microsoft Dev Blog](devblogs.microsoft.com)  
[Azure Website](https://azure.microsoft.com)
