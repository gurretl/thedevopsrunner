---
title: "Azure DevOps & Cloud-Native Updates - April 2024"
date: 2024-05-01
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
# Azure DevOps & Cloud-Native Updates - April 2024

## Introduction

**Welcome to our Monthly Azure DevOps and Cloud Tech Updates Series!**

Welcome to my monthly blog series where we bring you a concise roundup of significant Azure updates pertinent to DevOps, keeping you in the loop with the latest advancements.

Let's check what's new!

![](016_01.webp)

## ACR

### Infrastructure and quality enhancements for Azure Container Registry

We are excited to share the following significant enhancements to the Azure Container Registry (ACR) infrastructure:

Increased Registry Size: Previously capped at 20TiB, ACR’s registry size has now been auto-upgraded to 40TiB for all customers. This expanded capacity ensures that you can store more container images without constraints.
Geo-Replication Expansion: Geo-replication, a critical feature for redundancy and disaster recovery, can now be enabled for all registries over 20TiB. Additionally, we’ve optimized its performance, making it 10x faster than before.
We are actively working on further increasing the registry size to over 100TiB. This is in anticipation of the growing demand for larger workloads, especially those stemming from large language models (LLMs) and machine learning (ML) models.

These current and planned enhancements are designed to empower your container workflows and support your evolving needs.

[Learn more.](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-skus#service-tier-features-and-limits?wt.mc_id=MVP_357193)

## AKS

### GA: AKS cost views
The Kubernetes clusters and Kubernetes namespaces cost views are now generally available in Cost analysis within Azure portal. You can view the aggregated costs for all your AKS clusters and namespaces across a subscription and drill down into infrastructure and namespaces costs of a cluster. Having granular visibility will help you gain deeper insights into your infrastructure costs enabling you to allocate and optimize your AKS costs efficiently. 
Please refer to the articles below for instructions on installing the add-on and accessing the cost views.

[Learn more.](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/view-kubernetes-costs?wt.mc_id=MVP_357193)

### Public Preview: Azure HDInsight on AKS is now available for preview in 7 new regions

Azure HDInsight on AKS is now available for preview in seven new regions - East US 2 EUAP, West US, Japan East, Australia East, Canada Central, North Europe, Brazil South. Azure HDInsight on AKS is a modern, reliable, secure, and fully managed Platform as a Service (PaaS) that runs on Azure Kubernetes Service (AKS). HDInsight on AKS allows you to deploy popular Open-Source Analytics workloads like Apache Spark™, Apache Flink®️, and Trino without the overhead of managing and monitoring containers. For more information about Azure HDInsight on AKS, see the [documentation](https://learn.microsoft.com/en-us/azure/hdinsight-aks/?wt.mc_id=MVP_357193).

![](016_02.webp)

## App Service

### Preview: Run Azure Load Testing on Azure App Service web apps

You can now create and run load tests directly from App Service in Azure portal. Load test your web apps by simply selecting the deployment slot followed by specifying request parameters and load configuration. You will automatically gain access to client-side and server-side metrics, which will help in identifying performance bottlenecks. You can also view the test run history to continuously monitor their web app performance. [Learn more.](https://learn.microsoft.com/azure/load-testing/how-to-create-load-test-app-service?wt.mc_id=MVP_357193)

## Bastion

### GA: Azure Bastion Developer SKU
The new Bastion Developer SKU offers a convenient and secure solution for connecting to VMs in Azure at no extra cost. Bastion Developer allows users to establish a secure one-click connection to a single VM at a time without exposing public IPs on the VMs. Rather than deploying dedicated resources into the customer VNET like other Bastion SKUs, Bastion Developer utilizes a shared pool of resources managed internally by Microsoft for secure VM connectivity. Users can directly access their VMs through the connect experience on the VM blade in portal, with support for RDP/SSH on the portal and SSH-only for CLI sessions. Bastion Developer is perfect for Dev/Test users seeking secure VM connections without the need for additional features, configuration, or scaling.

At this time, Bastion Developer is limited to the following regions: Central United States EUAP, East United States 2 EUAP, West Central United States. North Central United States, West United States, and North Europe. Support for all public regions is coming soon. 

[Learn to configure Bastion Developer.](https://learn.microsoft.com/en-us/azure/bastion/quickstart-developer-sku?wt.mc_id=MVP_357193)

## OpenShift

### Azure Red Hat OpenShift April 2024 updates

Azure Red Hat OpenShift (ARO) provides highly available, fully managed OpenShift clusters on demand, monitored and operated jointly by Microsoft and Red Hat.

The latest Azure Red Hat OpenShift update delivers the following enhancements:

- ARO support in Azure Terraform Provider: The [AzureRM](https://registry.terraform.io/providers/hashicorp/azurerm/latest) Terraform provider now supports managing Azure Red Hat Openshift resources. Hashicorp Terraform is an infrastructure-as-code tool that lets you define infrastructure resources in human-readable configuration files that can be versioned, reused and shared.
- Bring your own Network Security Groups: You can now attach your own NSGs that include both your organization’s security rules and ARO service rules. This will be applied to both master and worker subnets before installing ARO clusters with a flag indicating the presence of the NSGs. 
- Azure Monitor Signals: You are able to provide ARO cluster Resource Health and integration with Azure Monitor Signals. Azure Monitor signals can be configured to generate alerts based on signals from Azure Red Hat OpenShift clusters. [Learn more.](https://learn.microsoft.com/en-us/azure/openshift/howto-monitor-alerts?wt.mc_id=MVP_357193)
- New GPU instance types for Day 2 operations: Azure Red Hat OpenShift now supports new GPU instance types that are aimed at Day 2 operations. The following GPU instance types are now supported: ND96asr_v4, NC24ads_A100_v4,NC48ads_A100_v4, NC96ads_A100_v4,and ND96amsr_A100_v4. [Learn more.](https://learn.microsoft.com/en-us/azure/openshift/support-policies-v4#gpu-workload?wt.mc_id=MVP_357193)
- ARO is now supported in the Taiwan Region: Azure Red Hat OpenShift is now supported in the Taiwan region providing more availability and fault tolerance to customers in this area. [Learn more.](https://azure.microsoft.com/en-us/explore/global-infrastructure/products-by-region/?wt.mc_id=MVP_357193)

## Sources
https://azure.microsoft.com/

[Microsoft Dev Blog](devblogs.microsoft.com)  
[Azure Website](https://azure.microsoft.com?wt.mc_id=MVP_357193)
