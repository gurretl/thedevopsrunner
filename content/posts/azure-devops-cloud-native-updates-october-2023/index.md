---
title: "Azure DevOps & Cloud-Native Updates - October 2023"
date: 2023-11-01
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
# Azure DevOps & Cloud-Native Updates - October 2023

## Introduction

**Welcome to our Monthly Azure DevOps and Cloud Tech Updates Series!**

In the fast-paced realm of DevOps and cloud technology, staying current with the latest advancements is essential. That's why we've embarked on a monthly journey to bring you a curated collection of updates, enhancements, and innovations from the Azure ecosystem and the world of DevOps. Whether you're a seasoned professional or just starting your cloud journey, my series provides a reliable source of information, sparing you the time and effort of scouring various channels for the freshest insights.

Welcome aboard, and let's explore the limitless possibilities with Azure together!

![](007_01.webp)

## Azure Container App

### Azure Container Apps is now eligible for Azure savings plan for compute

Azure Container Apps can now **benefit** from the Azure Savings Plan for compute. This includes all Azure Container Apps regions and plans, which can enjoy a **15% discount** for a one-year commitment and a **17% discount** for a three-year commitment, as opposed to the pay-as-you-go pricing model. By committing to a fixed hourly expenditure for either one or three years, you can access reduced prices and save on your Azure Container Apps costs.

Get more infor through this [link](https://techcommunity.microsoft.com/t5/apps-on-azure-blog/azure-container-apps-eligible-for-azure-savings-plan-for-compute/ba-p/3941243).

![](007_02.webp)

## Azure Bastion

### Public preview: 

The Bastion Developer SKU introduces a fresh, **cost-effective**, and streamlined iteration of the Bastion service. Bastion Developer enables users to establish secure connections to individual virtual machines one at a time without the need for additional network configurations or exposing public IPs on VMs. Users can directly access their VMs through the connection experience on the VM blade in the portal, with RDP/SSH access already in place and CLI-based SSH access coming soon. Bastion Developer caters to Dev/Test users looking for secure VM connections without the requirement for additional features or scalability.

Here is a summary of each SKU :
| Feature                                           | Developer SKU | Basic SKU | Standard SKU |
|--------------------------------------------------|--------------|-----------|--------------|
| Connect to target VMs in same virtual network    | Yes          | Yes       | Yes          |
| Connect to target VMs in peered virtual networks | No           | Yes       | Yes          |
| Support for concurrent connections               | No           | Yes       | Yes          |
| Access Linux VM Private Keys in Azure Key Vault  | No           | Yes       | Yes          |
| Connect to Linux VM using SSH                   | Yes          | Yes       | Yes          |
| Connect to Windows VM using RDP                 | Yes          | Yes       | Yes          |
| Connect to Linux VM using RDP                   | No           | No        | Yes          |
| Connect to Windows VM using SSH                 | No           | No        | Yes          |
| Specify custom inbound port                      | No           | No        | Yes          |
| Connect to VMs using Azure CLI                  | No           | No        | Yes          |
| Host scaling                                     | No           | No        | Yes          |
| Upload or download files                         | No           | No        | Yes          |
| Kerberos authentication                          | No           | Yes       | Yes          |
| Shareable link                                   | No           | No        | Yes          |
| Connect to VMs via IP address                   | No           | No        | Yes          |
| VM audio output                                  | Yes          | Yes       | Yes          |
| Disable copy/paste (web-based clients)           | No           | No        | Yes          |

Check the documentation to try it !

![](007_03.webp)

## Azure Kubernetes

### In Preview: Regional Disaster Recovery by Azure Backup for AKS

[**Azure Backup for AKS**](https://learn.microsoft.com/en-us/azure/backup/azure-kubernetes-service-cluster-backup) enables customers to protect their containerized workloads along with application data deployed on AKS clusters. The solution allows you to configure scheduled backups of your AKS clusters and restore them in same or alternate cluster in the scenarios like **Operational Recovery**, **Accidental Deletion** and **Application Migration**. Customers are also looking to utilize their AKS backups to recover application during a **regional disaster recovery** and also follow industry-wide best practice of **3-2-1 backup strategy**.

With this intent, Azure Backup service is announcing **private preview** of **AKS Backup - Regional Disaster Recovery Capability**. Using this feature you can :

- Recover AKS cluster from your backups in a secondary region as an Azure **Paired Region** in case of a **regional disaster**.
- Store Backup Copy offsite i.e. a **Vault Store** as per **3-2-1 backup strategy** and have ability to restore in case your tenant gets compromised.
- Retain data for a long duration for **compliance purposes** in regulated industries.

### In Preview : Disable Secure Shell (SSH) support in AKS

Secure Shell (SSH) is currently on by default for AKS provisioned nodes, and you must disable SSH manually.  

This public preview feature allows you to disable or enable SSH. This gives you the ability to secure your cluster and reduce the attack surface.

![](007_04.webp)

## Sources

[John Savill's youtube channel](https://www.youtube.com/@NTFAQGuy)  
[Microsoft Dev Blog](devblogs.microsoft.com)  
[Azure Website](https://azure.microsoft.com)
