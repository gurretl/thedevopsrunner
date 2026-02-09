---
title: "Azure DevOps & Cloud-Native Updates - January 2024"
date: 2024-02-01
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
# Azure DevOps & Cloud-Native Updates - January 2024

## Introduction

**Welcome to our Monthly Azure DevOps and Cloud Tech Updates Series!**

In the fast-paced realm of DevOps and cloud technology, staying current with the latest advancements is essential. That's why we've embarked on a monthly journey to bring you a curated collection of updates, enhancements, and innovations from the Azure ecosystem and the world of DevOps and Cloud Computing. Whether you're a seasoned professional or just starting your cloud journey, my series provides a reliable source of information, sparing you the time and effort of scouring various channels for the freshest insights.

Welcome aboard, and let's explore the limitless possibilities with Azure together!

![](013_01.webp)

## Kubernetes

### General Availability: Azure Load Testing supports fetching secrets from Azure Key Vault with access restrictions (private AKV)

In Azure Load Testing, you can use secrets from Azure Key Vault to set up your load test. If access to the Key Vault is restricted by a firewall or virtual networking, you can now access secrets from such a Key Vault by granting access to Azure Load Testing as a trusted Azure service.

[Learn more.](https://learn.microsoft.com/azure/load-testing/how-to-parameterize-load-tests#secrets)

### Azure Red Hat OpenShift January 2024 updates

Azure Red Hat OpenShift now offers Resource Health for clusters with integration with Azure Monitor via Signals and Alerts. To learn more, please see:

- [Azure Resource Health overview - Azure Service Health | Microsoft Learn](https://learn.microsoft.com/en-us/azure/service-health/resource-health-overview)
- [Azure Red Hat OpenShift documentation - Azure Red Hat OpenShift | Microsoft Learn](https://learn.microsoft.com/en-us/azure/openshift/)
- [Create Azure Monitor alert rules - Azure Monitor | Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-new-alert-rule?tabs=metric)

![](013_02.webp)

## Networking
### General Availability: Azure Virtual Network encryption
With Virtual Network encryption, customers can enable encryption of traffic between Virtual Machines and Virtual Machines Scale Sets within the same virtual network and between regionally and globally peered virtual networks. This new feature enhances the existing encryption in transit capabilities in Azure.

Azure Virtual Network encryption is available in the following regions: UK South, Swiss North and West Central US.

[Learn more.](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-encryption-overview)

## Management and Governance
### GA: Azure Advisor integration with Azure Monitor Log Analytics Workspace

Introduced several cost optimization related recommendations and added Azure Advisor to the Log Analytics Workspace admin experience:
- Consider configuring the cost effective Basic logs plan on selected tables
- Consider Changing Pricing Tier
- Consider removing unused restored tables

Can be helpful for your logs and cost optimization!

## Preview : Azure Arc Visual Studio Code Extension
Public preview of the Azure Arc Visual Studio Code Extension. Whether you’re just starting your journey with Azure Arc, or you’re already in production with an Arc-enabled application, our extension can help streamline your developer experience. The Azure Arc Visual Studio Code extension is home for Enterprise and ISV developers alike. The features built into the extension can help you accelerate development for both workloads that you’re running on the Edge, as well as services that you’re building to publish on the Azure Marketplace. 

[Learn more.](https://techcommunity.microsoft.com/t5/azure-arc-blog/public-preview-of-the-arc-visual-studio-code-extension/ba-p/4006891)

## Sources

[John Savill's youtube channel](https://www.youtube.com/@NTFAQGuy)  
[Microsoft Dev Blog](devblogs.microsoft.com)  
[Azure Website](https://azure.microsoft.com)
