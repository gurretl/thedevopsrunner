---
title: "Azure DevOps & Cloud-Native Updates - December 2023"
date: 2024-01-01
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
# Azure DevOps & Cloud-Native Updates - December 2023

## Introduction

**Welcome to our Monthly Azure DevOps and Cloud Tech Updates Series!**

In the fast-paced realm of DevOps and cloud technology, staying current with the latest advancements is essential. That's why we've embarked on a monthly journey to bring you a curated collection of updates, enhancements, and innovations from the Azure ecosystem and the world of DevOps. Whether you're a seasoned professional or just starting your cloud journey, my series provides a reliable source of information, sparing you the time and effort of scouring various channels for the freshest insights.

Welcome aboard, and let's explore the limitless possibilities with Azure together!

![](010_01.webp)

## Azure Kubernetes

### GA : AKS support for API breaking change detection

Azure Kubernetes Service (AKS) now supports fail fast on minor version change of Kubernetes cluster upgrades. This feature alerts you with an error message if it detects usage of deprecated Kubernetes standard APIs in the intended goal version provided you are using the latest API version. Detecting the change at this stage saves you from having to spend time on post upgrade workload troubleshooting. 

[Learn more.](https://learn.microsoft.com/en-us/azure/aks/upgrade-cluster?tabs=azure-cli)

### Public Preview: New AKS cost views for standard and premium tier clusters

You can now get **granular visibility into Kubernetes costs** in Cost analysis within Azure portal.  You can view the aggregated costs for all your clusters in a subscription and costs of all the namespaces for your clusters. All you need to do is to **enable the AKS cost analysis add-on** for your clusters. The AKS cost analysis add-on is built on top of OpenCost, an open-source Cloud Native Computing Foundation Sandbox project for usage data collection, which gets reconciled with your Azure billing data.  Please refer to the articles below for installation of the add-on and accessing the views.

[Learn more](https://learn.microsoft.com/en-us/azure/aks/cost-analysis)
[Learn more](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/view-kubernetes-costs)

### GA: Multi-line Logging Feature in Azure Monitor - Container Insights

Multi-line logging is a new feature in Azure Monitor - Container Insights that allows you to collect and store multiple lines of log data in a **single log entry**, making it easier to view and analyze logs. With this feature enabled, previously split container logs are stitched together and sent as single entries to the ContainerLogV2 table. This will also help customers **save on cost** as it is reducing the metadata added on multiple lines

[Learn more](https://techcommunity.microsoft.com/t5/azure-observability-blog/announcing-ga-multi-line-logging-in-azure-monitor-container/ba-p/3984289)

### GA : Azure Red Hat OpenShift v4.13 at install time

[Azure Red Hat OpenShift](https://azure.microsoft.com/en-us/products/openshift/) version **4.13** is now available at install time.

### Container insights recommended alerts (custom metrics) (preview) retirement moving up to 31 May 2024

To avoid or minimize disruption to your monitoring workflows setup using the custom metric alert (preview) feature, please refer to [migration guidance](https://learn.microsoft.com/en-us/azure/azure-monitor/containers/container-insights-metric-alerts?tabs=arm-template%2Cazure-portal#migrate-from-metric-rules-to-prometheus-rules-preview) and take the recommended actions before 31 May 2024. You will not be able to onboard additional monitored Kubernetes clusters to this feature using Azure Portal.

![](010_02.webp)

## Sources

[John Savill's youtube channel](https://www.youtube.com/@NTFAQGuy)  
[Microsoft Dev Blog](devblogs.microsoft.com)  
[Azure Website](https://azure.microsoft.com)
