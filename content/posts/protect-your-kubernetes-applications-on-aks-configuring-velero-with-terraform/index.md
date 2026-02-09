---
title: "Protect your Kubernetes Applications on AKS: Configuring Velero with Terraform"
date: 2023-07-15
draft: false
description: ""
tags: ['Terraform', 'Kubernetes', 'Azure', 'Infrastructure as Code']
categories: ['DevOps']
showAuthor: true
authors:
  - "lionelgurret"
---

------------------------------------------------------------------------------------

---

## Introduction

In this article, we will explore how to provision an Azure infrastructure to enable backing up an AKS cluster. While services like [Azure Backup](https://learn.microsoft.com/en-us/azure/backup/azure-kubernetes-service-backup-overview) can be used, they do not allow for automating the creation of different resources via Terraform or remain in "preview." For these reasons, we will learn how to define our infrastructure using [Terraform](https://www.terraform.io/) and then deploy the Velero backup solution using [Helm](https://helm.sh/).

**Attention: Contrary to what is provided in the official VMware documentation for Velero, the solution does not allow the use of Workload Identities (refer to [GitHub issue](https://github.com/vmware-tanzu/velero/issues/6510)).**

![](004_velero.webp)

## Setting up the Infrastructure with Terraform

### Prerequisites

In our context, the [AKS](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/kubernetes_cluster) cluster and its [*resource group*](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/resource_group.html) have already been provisioned. Refer to the official Terraform documentation for this part.

Here are the names of our resources to help you better understand the rest of this article:

```hcl
resource "azurerm_resource_group" "rg" {
  ...
}
resource "azurerm_kubernetes_cluster" "k8s" {
  ...
}
```

*Of course, in our repository, we have other Terraform files for declaring providers, variables, the backend, etc.*
*These Terraform manifests, along with the Azure DevOps provisioning pipeline for the infrastructure, will not be covered in this blog article.*

### Creating the Storage Space for Backups

To store our backups and snapshots, it is necessary to set up a *storage account* and a container.
You can choose to create it in the same *resource group* as the AKS cluster, or as explained in the documentation (see [sources](https://github.com/vmware-tanzu/velero-plugin-for-microsoft-azure/blob/main/README.md)), use a dedicated *resource group* for backups.

Here's the Terraform code used in our case:

```hcl
resource "azurerm_storage_account" "storaccbackup" {
  name                     = "storaccbackup01"
  account_replication_type = "LRS"
  account_tier             = "Standard"
  location                 = azurerm_resource_group.rg.location
  resource_group_name      = azurerm_resource_group.rg.name
}

resource "azurerm_storage_container" "storcontbackup" {
  name                 = "velero"
  storage_account_name = azurerm_storage_account.storaccbackup.name
}
```

*You can add the access_tier parameter and set it to "Cool" if your backups will not be frequently accessed.*

![](004_backup01.webp)

### Creating the Service Principal and Application

To establish a connection between our AKS cluster and our *storage account*, we will rely on a *[service principal](https://learn.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals?tabs=browser)*. As explained earlier, the use of Managed Identity is unfortunately not yet available.

Here's an example of code for creating this *service principal* and its associated resources:

```hcl
data "azuread_client_config" "current" {}

resource "azuread_application" "this" {
  display_name = "aks-backup-${local.basename}"
  owners       = [data.azuread_client_config.current.object_id]
}

resource "azuread_service_principal" "this" {
  application_id = azuread_application.this.application_id
}

resource "azuread_service_principal_password" "this" {
  service_principal_id = azuread_service_principal.this.object_id
}
```

### RBAC Configuration

This *service principal* needs access to the *storage account*, so we will add the Contributor role to it:

```hcl
resource "azurerm_role_assignment" "contributor_velero" {
  principal_id         = azuread_service_principal.this.object_id
  scope                = azurerm_storage_account.storaccbackup.id
  role_definition_name = "Contributor"
}
```

*It's possible to define a custom role to limit the permissions granted to our service principal (see [sources](https://github.com/vmware-tanzu/velero-plugin-for-microsoft-azure/blob/main/README.md)).*

### Storing IaC Generated Variables in a Key Vault

Certain parameters will need to be used by Helm when we install Velero on our AKS cluster. Therefore, it's important to store the following information in an *Azure Key Vault*:

```hcl
resource "azurerm_key_vault" "aks_kv" {
  ...
}

locals {
  keyvault_secrets = {
    aks-backup-resource-group-name = azurerm_storage_account.storaccbackup.resource_group_name
    aks-backup-storage-account-name = azurerm_storage_account.storaccbackup.name
    azure-tenant-id = data.azuread_client_config.current.tenant_id
    azure-backup-sp-client-id = azuread_application.this.application_id
    azure-backup-sp-client-secret = azuread_service_principal_password.this.value
  }
}

resource "azurerm_key_vault_secret" "keyvault_secrets" {
  for_each     = local.keyvault_secrets
  name         = each.key
  value        = each.value
  key_vault_id = azurerm_key_vault.aks_kv.id
}
```

These variables can be retrieved through an Azure DevOps variable group linked to our *Azure Key Vault* and used in our Helm pipelines.

### Provisioning the Azure Architecture

The entire infrastructure has been defined; now we can provision it using the well-known Terraform commands:

```bash
terraform init
terraform plan
terraform apply
```

![](004_backup02.webp)

## Installing Velero with Helm

In another Azure DevOps *repository*, we will now prepare our deployment pipeline and Velero configuration files.

### credentials-velero File

Firstly, we need to create a *credentials-velero* file containing the following information:

```bash
AZURE_SUBSCRIPTION_ID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXXX
AZURE_TENANT_ID=#{azure-tenant-id}#
AZURE_CLIENT_ID=#{azure-backup-sp-client-id}#
AZURE_CLIENT_SECRET=#{azure-backup-sp-client-secret}#
AZURE_RESOURCE_GROUP=MC_XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
AZURE_CLOUD_NAME=AzurePublicCloud
```

Make sure to adapt the variable for the subscription ID and the Azure *resource group*. **This is the auto-generated *resource group* created during the AKS cluster setup!**
The variables between tags will be modified by our Azure DevOps pipeline. This allows us to avoid displaying sensitive data in our code.

### Helm values File: velero-values.yaml

We will also pass our various values to Helm before installing the Velero helm chart. For this, we create the *velero-values.yaml* file in our *repository*:

```yaml
configuration:
  backupStorageLocation:
    - name: azure
      bucket: velero
      provider: azure
      config:
        resourceGroup: #{aks-backup-resource-group-name}#
        storageAccount: #{aks-backup-storage-account-name}#
  volumeSnapshotLocation:
    - name: azure
      provider: azure
      config:
        resourceGroup: #{aks-backup-resource-group-name}#
        storageAccount: #{aks-backup-storage-account-name}#

snapshotsEnabled: true
deployNodeAgent: true

image:
  repository: velero/velero
  pullPolicy: Always

initContainers:
  - name: velero-plugin-for-microsoft-azure
    image: velero/velero-plugin-for-microsoft-azure:master
    volumeMounts:
      - mountPath: /target
        name: plugins
```

You can refer to the [following documentation](https://github.com/vmware-tanzu/helm-charts/blob/main/charts/velero/values.yaml) for other configurations.

### azure-pipelines.yml File

Here's a part of the content of our Azure DevOps pipeline file that we'll use to install Velero on our AKS cluster:

```yaml
...
# We load our variable from our Azure Key Vault
variables:
  - group: vargroup-k8s-kv
...
          # We install Helm
          - task: HelmInstaller@0
            displayName: Install helm
            inputs:
              helmVersion: '3.12.2'
              installKubectl: true
          
          # We add the necessary helm repository for Velero
          - task: CmdLine@2
            displayName: Add helm repos
            inputs:
              script: |
                helm repo add vmware-tanzu https://vmware-tanzu.github.io/helm-charts
                helm repo update
          
          # We replace our variables from our "KeyVault vargroup"
          - task: replacetokens@5
            displayName: Replace tokens in Velero config files
            inputs:
              rootDirectory: './'
              targetFiles: '**/*'
              encoding: 'auto'
              tokenPattern: 'default'
              writeBOM: true
              actionOnMissing: 'warn'
              keepToken: true
              actionOnNoFiles: 'continue'
              enableTransforms: false
              enableRecursion: false
              useLegacyPattern: false
              enableTelemetry: true

          # We install Velero !
          - task: HelmDeploy@0
            displayName: Helm Velero
            inputs:
              connectionType: 'Kubernetes Service Connection'
              kubernetesServiceConnection: 'XXXXXXXXXXXXXXXXXX'
              namespace: 'velero'
              command: 'upgrade'
              chartType: 'Name'
              chartName: 'vmware-tanzu/velero'
              releaseName: 'velero'
              valueFile: 'velero-values.yaml'
              arguments: "--create-namespace --set-file credentials.secretContents.cloud=./credentials-velero"
```

Once the pipeline is launched and executed, we can verify if the storage space is properly connected to our AKS cluster:

```bash
$ kubectl get BackupStorageLocation -n velero
NAME    PHASE       LAST VALIDATED   AGE   DEFAULT
azure   Available   0s               26m
```

We have successfully installed Velero and its infrastructure!

## Backup and Restore Testing

### Velero CLI Installation

To create our backups, we will need to use the Velero CLI.
Here's how to install it ([documentation](https://velero.io/docs/v1.8/basic-install/)):

```bash
wget https://github.com/vmware-tanzu/velero/releases/download/v1.11.1/velero-v1.11.1-linux-amd64.tar.gz
tar -xzvf velero-v1.11.1-linux-amd64.tar.gz
sudo chmod +x ~/velero-v1.11.1-linux-amd64/velero
sudo cp ~/velero-v1.11.1-linux-amd64/velero /usr/local/bin/
velero version
```

### Setting Up a Test Application

With the backup in place, we need to validate its functionality. To do so, we will use a [test application](https://github.com/vmware-tanzu/velero/tree/main/examples/nginx-app) provided by Velero.

Let's start by downloading and installing the application on our AKS server:

```bash
cd ~/velero-v1.11.1-linux-amd64/examples/nginx-app
kubectl apply -f base.yml
```

Let's verify that the application has been successfully deployed:

```bash
$ kubectl -n nginx-example get all
NAME                                    READY   STATUS    RESTARTS   AGE
pod/nginx-deployment-747864f4b5-8cwv2   1/1     Running   0          22h
pod/nginx-deployment-747864f4b5-w8d48   1/1     Running   0          22h

NAME               TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)        AGE
service/my-nginx   LoadBalancer   10.0.24.168   20.250.58.191   80:30605/TCP   22h

NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/nginx-deployment   2/2     2            2           22h

NAME                                          DESIRED   CURRENT   READY   AGE
replicaset.apps/nginx-deployment-747864f4b5   2         2         2       22h
```

### Creating Our First Velero Backup

To initiate our first backup, we execute the following command:

```bash
$ velero backup create test-backup --include-namespaces nginx-example --wait --storage-location azure
Backup request "test-backup" submitted successfully.
Waiting for backup to complete. You may safely press ctrl-c to stop waiting - your backup will continue in the background.
.....
Backup completed with status: Completed. You may check for more information using the commands `velero backup describe test-backup` and `velero backup logs test-backup`.
```

We can verify that the backup has been successfully executed and that files have been added to our storage container:

![](004_storage_account.webp)

We can also view our backup on the server directly:

```bash
$ velero backup get
NAME          STATUS      ERRORS   WARNINGS   CREATED                         EXPIRES   STORAGE LOCATION   SELECTOR
test-backup   Completed   0        0          2023-08-15 08:36:58 +0000 UTC   29d       azure              <none>
```

### Restoration Test

We will start by deleting all resources in our nginx-example namespace to simulate a data loss:

```bash
$ kubectl -n nginx-example delete service my-nginx
service "my-nginx" deleted

$ kubectl -n nginx-example delete deployment nginx-deployment --force --grace-period=0
Warning: Immediate deletion does not wait for confirmation that the running resource has been terminated. The resource may continue to run on the cluster indefinitely.
deployment.apps "nginx-deployment" force deleted

$ kubectl -n nginx-example get all
No resources found in nginx-example namespace.
```

We can initiate the restoration:

```bash
$ velero restore create --from-backup test-backup
Restore request "test-backup-20230815084245" submitted successfully.
Run `velero restore describe test-backup-20230815084245` or `velero restore logs test-backup-20230815084245` for more details.
```

As indicated by the output message, we can track the restore process using the following command as instructed:

```bash
$ velero restore logs test-backup-20230815084245
time="2023-08-15T08:42:46Z" level=info msg="starting restore" logSource="pkg/controller/restore_controller.go:458" restore=velero/test-backup-20230815084245
time="2023-08-15T08:42:46Z" level=info msg="Starting restore of backup velero/test-backup" logSource="pkg/restore/restore.go:396" restore=velero/test-backup-20230815084245
time="2023-08-15T08:42:46Z" level=info msg="Resource 'customresourcedefinitions.apiextensions.k8s.io' will be restored at cluster scope" logSource="pkg/restore/restore.go:2030" restore=velero/test-backup-20230815084245
time="2023-08-15T08:42:46Z" level=info msg="Getting client for apiextensions.k8s.io/v1, Kind=CustomResourceDefinition" logSource="pkg/restore/restore.go:918" restore=velero/test-backup-20230815084245
time="2023-08-15T08:42:46Z" level=info msg="restore status includes excludes: <nil>" logSource="pkg/restore/restore.go:1189" restore=velero/test-backup-20230815084245
time="2023-08-15T08:42:46Z" level=info msg="Executing item action for customresourcedefinitions.apiextensions.k8s.io" logSource="pkg/restore/restore.go:1196" restore=velero/test-backup-20230815084245
...
```

Finally, we observe that our resources are available again:

```bash
$ kubectl -n nginx-example get all
NAME                                    READY   STATUS    RESTARTS   AGE
pod/nginx-deployment-747864f4b5-8cwv2   1/1     Running   0          15s
pod/nginx-deployment-747864f4b5-w8d48   1/1     Running   0          15s

NAME               TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)        AGE
service/my-nginx   LoadBalancer   10.0.196.243   20.250.76.149   80:31188/TCP   15s

NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/nginx-deployment   2/2     2            2           15s

NAME                                          DESIRED   CURRENT   READY   AGE
replicaset.apps/nginx-deployment-747864f4b5   2         2         2       15s
```

Everything is now in place to automate the creation of backups!

![](004_backup03.webp)

### Sources

**/!\ Don't follow the documentation related to Workload Identities (yet)**

[VMWare Tanzu](https://github.com/vmware-tanzu/velero-plugin-for-microsoft-azure/blob/main/README.md)
[Velero Documentation](https://velero.io/docs/v1.11/)
