---
title: "Azure DevOps & Cloud-Native Updates - February 2024"
date: 2024-03-01
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
# Azure DevOps & Cloud-Native Updates - February 2024

## Introduction

**Welcome to our Monthly Azure DevOps and Cloud Tech Updates Series!**

Welcome to my monthly blog series where we bring you a concise roundup of significant Azure updates pertinent to DevOps, keeping you in the loop with the latest advancements.

Let's explore the limitless possibilities with Azure together!

![](014_01.webp)

## AKS

### GA: Application Gateway for Containers

Application Gateway for Containers is now generally available.

Application Gateway for Containers is the next evolution of Application Gateway + Application Gateway Ingress Controller, providing application (layer 7) load balancing and dynamic traffic management capabilities for workloads running in a Kubernetes cluster.  Application Gateway for Containers achieves near-to-real-time convergence times to reflect add/remove of pods, routes, probes, and other load balancing configuration within Kubernetes yaml configuration.

In addition to the numerous improvements announced at public preview, general availability brings several new additions:

Features - Public preview and GA has added support for Custom Health Probes, URL Redirect, URL / Header Rewrite.
Controller High Availability – Have peace of mind if a node goes down, changes within your cluster will continue to be propagated to the network.
Gateway API v1 – Bring the familiarity and role based access control provided by Gateway API to your network configuration.
Additional Region Availability – Take advantage of Application Gateway for Containers in a region closest to you.
SLA for Production Workloads – Feel confident in running your production workloads with Application Gateway for Containers.

[Learn more.](https://aka.ms/appgwcontainers/docs)

### GA: Capacity Reservations support in AKS

You can now create capacity reservation groups and assign them to node pools.
As your workload demands change, you can associate existing capacity reservation groups to node pools to guarantee allocated capacity for your node pools.

### GA: Istio-based service mesh add-on for Azure Kubernetes Service

Azure Kubernetes Service (AKS) addon for service mesh based on Istio is now generally available. Istio addresses the challenges developers and operators face with a distributed or microservices architecture and can be used to streamline traffic management, security, and observability for service-to-service communication scenarios.
The AKS addon for service mesh builds on top of open source Istio and provides additional benefits such as compatibility testing done between Istio with supported versions of AKS, minor/patch version upgrades, plugin Certificate Authority (CA), managed external/internal ingresses, and scaling of Istio control plane components.
To learn more about this addon and get started, visit: [https://aka.ms/asm-aks-addon-docs](https://aka.ms/asm-aks-addon-docs)
To learn more about the roadmap for service mesh area, visit: [https://aka.ms/asm-roadmap](https://aka.ms/asm-roadmap)

### Public Preview: Regional Disaster Recovery by Azure Backup for AKS

In today's dynamic landscape, safeguarding containerized workloads and application data is paramount. That's why Azure Backup for AKS provides comprehensive protection for your AKS clusters, enabling scheduled backups and seamless restoration in scenarios like Operational Recovery, Accidental Deletion, and Application Migration.

Now, we're excited to highlight a key addition: the Regional Disaster Recovery Capability, available in public preview. With this feature, you can proactively prepare for and mitigate the impact of regional disasters by:

- Recovering AKS clusters from backups stored in a secondary region, leveraging Azure Paired Regions, ensuring business continuity even in the face of regional disruptions.
- Storing Backup Copies offsite, adhering to the 3-2-1 backup strategy, and having the resilience to restore them in case of tenant compromise.
- Retaining data for extended periods to meet compliance requirements in regulated industries, ensuring data integrity and security.

[Learn more.](https://learn.microsoft.com/en-us/azure/backup/whats-new#vaulted-backup-and-cross-region-restore-for-support-for-aks-preview) 

### Public preview: AKS cluster control plane metrics in managed Prometheus

AKS cluster control plane metrics in managed Prometheus is a new feature that automatically scrapes the control plane – API server and etcd metrics and send them to a Azure Monitor workspace via managed Prometheus. With this, you are able monitor the API server traffic and load along with the etcd size, object count to understand the state of the control plane and tune Kubernetes application client behavior to optimize for performance and reliability. AKS clusters with managed Prometheus get these new metrics automatically once the subscription has been enabled for the preview feature.

[Learn more.](https://aka.ms/aks/controlplanemetrics)

### Public preview: Azure Application Gateway introduces support for TLS and TCP protocols

Azure Application Gateway introduces support for TLS and TCP protocol termination in public preview. This feature lets you use Application Gateway for non-HTTP applications based on protocols like SQL, MQTT, AMQP, etc. It enables you to use a custom domain with Application Gateway's TLS certificate management capability to provide a secure connection to your clients and access any backend service. Additionally, it offers a single endpoint for all your clients as a single Application Gateway resource can support Layer 7 (HTTP/S) to Layer 4 (TCP and TLS) protocols.

The feature is available for Standard V2 and Web Application Firewall V2 SKUs.

[Learn more](https://azure.microsoft.com/en-us/updates/tls-tcp-proxy-preview/).

### Public preview: Kubernetes 1.29 support in AKS

AKS now supports the latest Kubernetes 1.29 preview release (mandala) that has some much-awaited features such as ReadWriteOncePod, PersistentVolume access mode, Node volume expansion Secret support for CSI drivers and more.

[Learn more.](https://azure.microsoft.com/fr-fr/updates/public-preview-kubernetes-129-support-in-aks/)

### Public preview: OS SKU in-place migration for Linux nodes

Today, traditional OS SKU migration involves creating a new node, cordoning and draining existing nodes, and then deleting existing nodes. This can involve a large surge of core count as new nodes are added, as well as manual intervention to cordon and drain.  
The OS SKU in-place migration feature, now in public preview, allows you to trigger a node image upgrade between one Linux SKU (i.e. Ubuntu) to another (i.e. Azure Linux) on an existing nodepool.

[Learn more.](https://aka.ms/aks/OSSKUMigration)

### Public preview: Disable network policy in AKS for migration

You can now use AKS update to temporarily disable your network policy engine for two migration scenarios

- Migration to Azure CNI overlay – Migration to overlay was limited because network policy needed to be disabled before migration could take place.
- Migration to other network policy engines – You can now migrate to other network policy engines. (e.g. Calico to Cilium)

### Public preview: AKS support for node soak duration for upgrades

Azure Kubernetes Service (AKS) now supports node soak duration to help stagger node upgrades in a controlled manner and minimize application downtime during an upgrade.
The period can range from a default of 0 to a maximum of 30 minutes. Node soak time works together with the max surge and node drain timeout properties available in the node pool to deliver more refined control of upgrade speed and application availability.

[Learn more.](https://learn.microsoft.com/en-us/azure/aks/upgrade-aks-cluster?tabs=azure-cli#set-node-soak-time-value-preview)

## Azure Container App

### GA: Azure Container Apps supports additional TCP ports

Azure Container Apps now supports additional TCP ports, enabling applications to accept TCP connections on multiple ports. This feature is generally available.

[Learn more.](https://aka.ms/aca/additional-tcp-ports)

![](014_02.webp)

## AppService

### GA: Mount Azure Storage as a local share in App Service Linux Now supports NFS

**NFS support** is now available for **App Service Linux** code and container when mounting a **Azure File share** as a local share for the web app. 

[Learn more.](https://learn.microsoft.com/en-us/azure/app-service/configure-connect-to-azure-storage?tabs=basic%2Cportal&pivots=container-linux)

## Azure Backup & Storage

### GA: Support for Azure VMs using Ultra disks in Azure Backup

Ultra disks enable customers to run mission critical, I/O demanding, enterprise applications on the cloud including applications like SAP HANA, top tier SQL databases, as well as NoSQL databases. With this feature, we aim to address a key ask from customers, who are looking to enable Azure Backup on Azure VMs running on Ultra disks. It will allow you to ensure business continuity for your virtual machines and to recover from any disasters or ransomware attacks.

### GA: Azure Elastic SAN

First fully-managed and cloud-native storage area network (SAN) offering that simplifies deploying, scaling, managing, and configuring a SAN in the cloud. Azure Elastic SAN responds to the vital need for seamless migration of extensive SAN environments to the cloud, bringing a new level of efficiency and ease. This enterprise-class offering stands out by adopting a SAN-like resource hierarchy, provisioning resources at the appliance level, and dynamically distributing these resources to meet the demands of diverse workloads across databases, virtual desktop infrastructure (VDIs), and business applications. Beyond that, it delivers cloud native benefits with scale on demand, policy-based service management, and cloud native security enforcements across encryption and network access. It's a thoughtful innovation combining the efficiency at scale of on-prem SAN systems and the flexibility of cloud storage.

### Public preview: Configuration-as-code customizations in Microsoft Dev Box

The configuration-as-code customization feature in Microsoft Dev Box is now in public preview.   
Speed up developer onboarding by further automating the setup of development environments on Dev Box. Defining what’s needed on a dev box can now be as easy as submitting a code change.
Customization enables developers to efficiently configure workstations to their exact project requirements, within guardrails set by admins that enforce governance and security policies.
Customization now also supports the use of secrets from a private Azure Key Vault in a configuration-as-code file.  

[Learn more.](https://aka.ms/devbox/customizations)

## Azure Functions

### Public preview: Azure Functions Support for HTTP Streams in Node.js

Azure Functions support for HTTP streams in Node.js is now in preview. With this feature, you can now stream HTTP requests to, and responses from, your Functions Apps.
This release makes scenarios like processing large data, streaming OpenAI responses, delivering dynamic content etc. possible. You can leverage this feature for use cases where real time exchange and interaction between client and server over HTTP connections is needed. We recommend using streams to get the best performance and reliability for your apps.
HTTP Streams in Node.js is supported only in the Azure Functions Node.js v4 programming model. 

[Learn more.](https://aka.ms/AzFuncNodeHttpStreams)

## Sources

[Microsoft Dev Blog](devblogs.microsoft.com)  
[Azure Website](https://azure.microsoft.com)
