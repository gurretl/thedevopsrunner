---
title: "Azure DevOps & Cloud-Native Updates - November 2023"
date: 2023-12-01
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
# Azure DevOps & Cloud-Native Updates - November 2023

## Introduction

**Welcome to our Monthly Azure DevOps and Cloud Tech Updates Series!**

In the fast-paced realm of DevOps and cloud technology, staying current with the latest advancements is essential. That's why we've embarked on a monthly journey to bring you a curated collection of updates, enhancements, and innovations from the Azure ecosystem and the world of DevOps. Whether you're a seasoned professional or just starting your cloud journey, my series provides a reliable source of information, sparing you the time and effort of scouring various channels for the freshest insights.

Welcome aboard, and let's explore the limitless possibilities with Azure together!

![](009_01.webp)

## Azure Kubernetes

### GA: Cost views for Azure Kubernetes service (AKS)

Unveiling a game-changer for Kubernetes cost management: Azure Kubernetes Service (AKS) introduces cost views in preview from November 14, 2023. This feature allows users to effortlessly track costs at the namespace level and gain an aggregate view of cluster assets. Accessible through the Azure portal's Cost analysis, it promises to streamline and simplify cost analysis and allocation within Kubernetes clusters.

Source : [Microsoft Cost Management updates—November 2023](https://azure.microsoft.com/en-us/blog/microsoft-cost-management-updates-november-2023/#Introducing)

### GA: Kubernetes 1.28 support in Azure Kubernetes Service (AKS)

AKS support for Kubernetes version 1.28 is now generally available!

[Changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md)

### GA: Kube-reserved resource optimization in Azure Kubernetes Service (AKS)

Azure Kubernetes Service (AKS) ensures node stability by **enforcing reserved space**, preventing competition between pods and system daemons. This is governed by the Kube-reserved flag, specifying resource reservations for critical Kubernetes system components. The optimized AKS reservation logic **reduces Kube-reserved memory by up to 20%**, offering improved efficiency for all users.

### GA: Application routing add-on for Azure Kubernetes Service (AKS)

The **Application Routing add-on** for Azure Kubernetes Service (AKS) is now generally available, providing a streamlined approach to deploy web applications securely. This **eliminates the need for setting up an ingress controller, certificate, and DNS management complexities**. App routing, supported and managed, utilizes the ingress-nginx project to establish a robust foundation for enterprises as their requirements expand.

[Learn more.](https://aka.ms/aks/docs/app-routing)

### GA: Provider for running Karpenter on Azure Kubernetes Service (AKS)

Karpenter's Advantages:

- Efficiency Boost: Karpenter enhances both the efficiency and cost-effectiveness of running workloads on Kubernetes clusters.
- Smart Monitoring: It intelligently monitors pods marked as unschedulable by the Kubernetes scheduler.
- Constraint Evaluation: Karpenter evaluates various scheduling constraints, including resource requests, nodeselectors, affinities, tolerations, and topology spread constraints requested by the pods.
- Dynamic Node Provisioning: It dynamically provisions nodes tailored to meet the specific requirements of the pods.
- Seamless Scheduling: Karpenter orchestrates the scheduling of pods on the new nodes.
- Resource Optimization: Removes unnecessary nodes efficiently when they are no longer in use.
- With this latest development, managing workloads on Azure Kubernetes Service is poised to become even more seamless and resource-efficient.

[Learn more.](https://github.com/Azure/karpenter)

### GA - Azure Backup for AKS

**Azure Backup for AKS** simplifies the task for IT administrators by offering application-centric automated backups and straightforward restores for AKS clusters. All of this can be managed within a unified dashboard, providing a comprehensive view for monitoring, governance, and administration.

This latest release introduces several enhancements:

1. **Application-Consistent Snapshots:** For applications utilizing databases such as MySQL and MongoDB within AKS clusters, AKS Backup now supports application-consistent snapshots through custom hooks.

2. **Cross-Subscription Restores:** You can now seamlessly restore backups to AKS clusters located in different subscriptions. This feature proves valuable in scenarios like application migration.

3. **Enhanced BYO Model Support:** AKS Backup now extends support for the Bring Your Own (BYO) model. This includes the ability to back up statically provisioned Azure Disks and clusters using a User Identity for RBAC operations.

[Learn more](https://learn.microsoft.com/en-us/azure/backup/azure-kubernetes-service-backup-overview).

### GA: Kubernetes Event-driven Autoscaling (KEDA) Add-on for AKS

The **Kubernetes Event-driven Autoscaling (KEDA)** add-on for AKS (Azure Kubernetes Service) is now available for general use !
KEDA is a lightweight component dedicated to simplifying application **autoscaling**. It's a CNCF Incubation project that enables event-driven autoscaling, allowing your application to scale efficiently and cost-effectively, **even down to zero when not in use**.

The KEDA add-on further streamlines the process by offering a managed KEDA installation and a comprehensive [catalog](https://keda.sh/docs/2.12/scalers/) of over 60 KEDA scalers for scaling applications on your AKS cluster.

To learn more about the KEDA add-on for AKS, click [here](https://learn.microsoft.com/en-us/azure/aks/keda-about).

![](009_02.webp)

### GA: Azure App Configuration Kubernetes Provider

Azure App Configuration Kubernetes Provider is an **App Configuration add-on** for Kubernetes to provide the centralized configuration data for applications and services running in Kubernetes clusters. It can be really helpful with :

- Dynamic refresh of the Configuration key-values
- Periodic refresh of the Key-vault referenced secrets
- Workload identity authentication
- Consumption of the generated ConfigMap as a mounted file in addition to the environment variables

[Learn more.](https://mcr.microsoft.com/product/azure-app-configuration/kubernetes-provider/about)

### GA: Kubernetes AI toolchain operator

Run large language models (LLMs) on Azure Kubernetes Service (AKS) more cost-effectively with automated deployment using the **Kubernetes AI toolchain operator**. It optimizes infrastructure, distributes inferencing across lower-GPU count VMs, expands workload availability, reduces wait times, and lowers overall costs. Choose from preset models with hosted images on AKS for faster inference service setup.

[Learn more.](https://github.com/Azure/kaito/tree/main)

### GA: Azure Kubernetes Fleet Manager

**Azure Kubernetes Fleet Manager (Fleet)** is now generally available, facilitating multi-cluster management for Azure Kubernetes Service (AKS). Admins can orchestrate updates across clusters using update runs, stages, and groups. The new update orchestration feature includes templates for update runs and allows setting node image consistency as a desired outcome.

[Learn more.](https://learn.microsoft.com/azure/kubernetes-fleet/)

### GA: Azure Red Hat OpenShift November 2023 updates

The latest Azure Red Hat OpenShift update delivers the following enhancements:

- Extended support: OpenShift 4.12 now offers extended 14-month support lifecycle for users.
- Larger cluster size: Customers can now deploy Azure Red Hat OpenShift clusters with a larger number of worker nodes. The new limit is up to 120 nodes, up from the previous limit of 62 nodes.
- Tagging: You can now use Azure Policy to tag resources in an ARO cluster's resource group. The process creates a policy assignment and an ARO cluster through the Azure CLI.

[Learn more](https://cloud.redhat.com/blog/whats-new-with-azure-red-hat-openshift-4.12-is-released-and-more)

### GA: Collect Syslog from AKS nodes using Azure Monitor Container Insights

The ability to **collect Syslog** from Linux-based host nodes in AKS is now generally available! The GA release comes with reliability improvements, an out-of-box dashboard in Azure Managed Grafana, and the ability to send Syslog data to Microsoft Sentinel.

[Learn more.](https://techcommunity.microsoft.com/t5/azure-observability-blog/announcing-ga-collect-syslog-from-your-aks-nodes-using-container/ba-p/3980648)

### Preview: Azure Container Storage in AKS

Azure Container Storage offers highly **scalable and cost-effective persistent volumes** specifically designed for **containers**. Now, seamlessly deploy and utilize Azure Container Storage through the Azure Kubernetes Service (AKS) cluster create or update preview experience across 26 regions. This simplifies the provisioning of volumes and management of stateful container applications on AKS. Azure Container Storage enables swift scaling of volumes, reduces pod failover time, and minimizes total cost of ownership consistently across various block storage options, including ephemeral disks, Azure Disks, and Azure Elastic SAN.

In this preview update, you can now:

- Configure **multi-zone storage pools** to enhance high availability and redundancy.
- Secure storage pools using **server-side encryption** with customer-managed keys.
- **Dynamically resize volumes**.
- **Protect and recover volumes** within a storage pool using **snapshot and clone** features.

### Public Preview: Azure integration with Canonical’s Snapshot Service for safe deployment

Microsoft and Canonical have partnered to simplify Linux operating system updates and enhance the security and resilience of Canonical workloads on Azure.

Azure is the first cloud provider to collaborate with Canonical in integrating its **snapshot service**.
Azure Guest Patching Service (AzGPS) and Azure Kubernetes Service (AKS) will use this new capability to **consistently apply updates** across your fleet in various regions through safe deployment principles (SDP).

Links :
- [Announcement blog](https://techcommunity.microsoft.com/t5/linux-and-open-source-blog/increased-security-and-resiliency-of-canonical-workloads-on/ba-p/3970623)
- [Azure Guest Patching documentation](https://learn.microsoft.com/en-us/azure/virtual-machines/automatic-vm-guest-patching#how-does-automatic-vm-guest-patching-work)
- [Azure Kubernetes Service documentation](https://learn.microsoft.com/en-us/azure/aks/intro-kubernetes)

### Public preview: Image integrity support in Azure Kubernetes Service (AKS)

Leveraging signed container images serves to ensure the credibility of your deployments, guaranteeing they originate from a trusted source and remain unaltered since creation.

For AKS, image integrity is maintained through the incorporation of an Azure Policy built-in definition. This ensures that **only signed images** undergo deployment to your AKS clusters, reinforcing the security and reliability of your containerized applications.

Check the [documentation](https://learn.microsoft.com/en-us/azure/aks/image-integrity?tabs=azure-cli)!

### Public preview: Artifact streaming support in Azure Kubernetes Service (AKS)

Facilitate the **acceleration** of your containerized workloads on Azure Kubernetes Service (AKS) with the introduction of Azure Container Registry (ACR) **artifact streaming**. This feature enables you to scale your workloads without the need to wait for images to be entirely pulled into the clusters.

Currently accessible for **Linux-based** container images through the ACR and AKS Preview API, Artifact Streaming is set to receive CLI and Portal support within the next two weeks.

For additional information, visit this [link](https://aka.ms/artifactstreaming).

### Public preview: Enhancements for Istio-based service mesh add-on for AKS

The Istio-based service mesh add-on for AKS, currently in public preview, introduces new features for enhanced functionality:

1. **Minor Version Upgrade:**
   - Explicitly upgrade from one Istio minor version/release to the next.
   - Deploy a canary version of Istio control plane, control sidecar proxies rollover, and finalize or rollback the canary deployment based on mesh performance.

2. **Bring Your Own Certificate Authority (CA):**
   - Support for bringing your own CA by inputting data via Azure Key Vault.
   - Reference the CA in the service mesh profile for added flexibility.

3. **Egress Support:**
   - Introduces egress gateways for configuring load balancers at the mesh edge.
   - Enables applying Istio features to traffic exiting the mesh, such as monitoring and route rules.

For more details, visit this [link](https://aka.ms/asm-aks-addon-docs).

### Public preview: Dual-stack networking in Azure CNI Overlay for AKS

Azure CNI Overlay for AKS introduces **dual-stack** support in public preview. This enhancement **allows both IPv4 and IPv6 addresses to coexist** within the same cluster, offering greater flexibility. The Azure CNI Overlay model's performance benefits now extend to dual-stack networking, facilitating seamless communication with external systems on either IP address family. This feature addresses the demand for IPv6 support and aids enterprises in transitioning to evolving network standards.

![](009_03.webp)

## Sources

[John Savill's youtube channel](https://www.youtube.com/@NTFAQGuy)  
[Microsoft Dev Blog](devblogs.microsoft.com)  
[Azure Website](https://azure.microsoft.com)
