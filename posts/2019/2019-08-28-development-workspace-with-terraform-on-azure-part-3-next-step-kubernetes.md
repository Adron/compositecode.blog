---
title: 'Development Workspace with Terraform on Azure: Part 3 – Next Step Kubernetes'
date: 2019-08-28 10:56:34 -0700
last_modified_at: 2019-08-28 10:56:34 -0700
permalink: /2019/08/28/development-workspace-with-terraform-on-azure-part-3-next-step-kubernetes/
slug: development-workspace-with-terraform-on-azure-part-3-next-step-kubernetes
wp_id: 16157
original_url: https://compositecode.blog/2019/08/28/development-workspace-with-terraform-on-azure-part-3-next-step-kubernetes/
categories:
- Azure
- How-to
- Infrastructure
tags:
- azure
- hashicorp
- infrastructure as code
- Kubernetes
- terraform
excerpt: In part 1 of this series I setup Terraform and put together a basic setup for ongoing use. In part 2 I setup Packer and got a template started that installs Apache Cassandra 3.11.4. In this part there’s one more key piece. Really key piece for iterating and moving quickly with development needs on a …
image: /wp-content/uploads/2019/08/allthebits.png
---

In [part 1](/2019/08/01/development-workspace-with-terraform/) of this series I setup Terraform and put together a basic setup for ongoing use. In [part 2](/2019/08/16/development-workspace-with-terraform-on-azure-part-2-packer-images/) I setup Packer and got a template started that installs Apache Cassandra 3.11.4.

In this part there’s one more key piece. Really key piece for iterating and moving quickly with development needs on a day to day basis. I need some development love with Kubernetes. Terraform is extremely well suited to spin this up in Azure! Since I setup [Terraform in part 1](/2019/08/01/development-workspace-with-terraform/) I’ll leave those specifics [linked here](/2019/08/01/development-workspace-with-terraform/).

## 1: Terraform ❤️ Kubernetes

There are a couple of different, and very important aspects to how and what can be done with Kubernetes with Terraform. First, which I’ll cover right here, is the creation of a Kubernetes Cluster. Later I’ll cover more material related to working with the cluster itself and managing the resources within the cluster. To a Kubernetes cluster running with Terraform there’s a singular resource we’ll need to use.

Opening up the project – same as in the previous two blog article in this series – and went straight into the main.tf file in the root and added the follow Kubernetes resource.

```javascript
resource "azurerm_kubernetes_cluster" "test" {
  name                = "acctestaks1"
  location            = "${azurerm_resource_group.adrons_resource_group_workspace.location}"
  resource_group_name = "${azurerm_resource_group.adrons_resource_group_workspace.name}"
  dns_prefix          = "acctestagent1"

  agent_pool_profile {
    name            = "default"
    count           = 1
    vm_size         = "Standard_D1_v2"
    os_type         = "Linux"
    os_disk_size_gb = 30
  }

  service_principal {
    client_id     = var.clientid
    client_secret = var.clientsecret
  }

  tags = {
    Environment = "Production"
  }
}

output "client_certificate" {
  value = "${azurerm_kubernetes_cluster.test.kube_config.0.client_certificate}"
}

output "kube_config" {
  value = "${azurerm_kubernetes_cluster.test.kube_config_raw}"
}
```

With that I immediately applied the changes to build the environment with `terraform apply` and confirming with a `yes`.

The agent pool profile is what sets up our virtual machines that will make up our Kubernetes Cluster. In this case I’ve selected the *Standard\_D1\_v2* just because that’s the default example, but depending on use case this may need to change. For more information about the various virtual machine sizes in Azure here are a few important links:

- [Virtual Machine Series](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/series/)
- [General Purpose Compute Machines](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes-general)
- [Memory Optimized Virtual Machines](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes-memory)
- [Storage Optimized Virtual Machines](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes-storage)
- [Azure Virtual Machines](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes)
- [Virtual Machines – List Available Sizes](https://docs.microsoft.com/en-us/rest/api/compute/virtualmachines/listavailablesizes)

The Service Principal as shown is pulled from variable, as setup in part 1 and part 2 of this series.

The two output variables in the section of configuration above will print out the client cert and raw configuration which we’ll need for other uses in the future. Be sure to put both of those somewhere that can be retrieved for future use. Ideally, keep them secure! I’ll speak to this more in future posts, but for now I’m going to focus on this Kubernetes Cluster.

**![check-box-64](/wp-content/uploads/2019/08/check-box-64.png)Verification Checklist**

- Based on the infrastructure in [part 1](/2019/08/01/development-workspace-with-terraform/) and [part 2](/2019/08/16/development-workspace-with-terraform-on-azure-part-2-packer-images/) and this addition, there is now the Packer image for the Apache Cassandra 3.11.4 image, in Azure the Service Principal, Resource Group, and related collateral, and now a Kubernetes Cluster to work with.

## 2: Kubernetes ❤️ Terraform

Alright, with a Kubernetes (K8s) done, we can now add some more elements to it via Terraform in which to work with. Specifically let’s add a [pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/) and then get an [Nginx](https://github.com/nginx/nginx) container up and running.

The first thing we need however is a connection to the cluster that is created in the previous step. In the HCL (HashiCorp Configuration Language) above we setup two output variables. The data in those variables is needed for our ongoing connection to Kubernetes, however we don’t particularly need to pass them via output variables. The reason we don’t need to pass them via variables into another phase of deployment is because Terraform can handle the creation of a Kubernetes cluster and the post-creation processing of creating pods and related collateral in the order it needs to occur. Since Terraform knows how to do this, there is a way to setup the connection information for the Kubernetes Provider that prevents us from needing to post output variables. Before moving on those should be removed. Once that is done add the follow provider for Kubernetes.

```javascript
provider "kubernetes" {
  host                   = "${azurerm_kubernetes_cluster.test.kube_config.0.host}"
  username               = "${azurerm_kubernetes_cluster.test.kube_config.0.username}"
  password               = "${azurerm_kubernetes_cluster.test.kube_config.0.password}"
  client_certificate     = "${base64decode(azurerm_kubernetes_cluster.test.kube_config.0.client_certificate)}"
  client_key             = "${base64decode(azurerm_kubernetes_cluster.test.kube_config.0.client_key)}"
  cluster_ca_certificate = "${base64decode(azurerm_kubernetes_cluster.test.kube_config.0.cluster_ca_certificate)}"
}
```

In this section of configuration the host is set from the previously created Kubernetes Cluster, then the username and password, then the certificates, and key. Each of these, as you can see, is pulled from the Kubernetes Cluster resource (azurerm\_kubernetes\_cluster) and then from the test cluster that was created. With this addition run `terraform init` to get the provider downloaded and ready for use.

With the connection now set, the provider downloaded, the next step is to add the Kubernetes Pod that we’ll need to run the Nginx container. Hat tip to the HashiCorp docs for this specific example.

```javascript
resource "kubernetes_pod" "nginx" {
  metadata {
    name = "nginx-example"
    labels = {
      App = "nginx"
    }
  }

  spec {
    container {
      image = "nginx:1.7.8"
      name  = "example"

      port {
        container_port = 80
      }
    }
  }
}
```

This will setup a pod that uses and runs a nginx:1.7.8 container image and makes it available on port 80. To make this container available as a service however there is one more step, to create a Kubernetes Service that’ll make port 80 available and mapped to the container within Kubernetes.

```javascript
resource "kubernetes_service" "nginx" {
  metadata {
    name = "nginx-example"
  }
  spec {
    selector = {
      App = kubernetes_pod.nginx.metadata[0].labels.App
    }
    port {
      port        = 80
      target_port = 80
    }

    type = "LoadBalancer"
  }
}
```

Alright, now the setup is almost 100% complete. The last step is to create another output variable that’ll provide a way for us to navigate to and make requests against the Nginx service, we’ll need either the IP or the hostname. Depending on the cloud provider one or other other can be retrieved by asking for the load\_balancer\_ingress[0].ip value or the load\_balancer\_ingress[0].hostname. For Azure and GCP, one can retrieve the IP, for AWS you’d want to specifically get the hostname.

In the end the HCL looks like this.

```javascript
provider "azurerm" {
  version = "=1.27.0"

  subscription_id = var.subscription_id
  tenant_id       = var.tenant_id

}

provider "kubernetes" {
  host                   = "${azurerm_kubernetes_cluster.test.kube_config.0.host}"
  username               = "${azurerm_kubernetes_cluster.test.kube_config.0.username}"
  password               = "${azurerm_kubernetes_cluster.test.kube_config.0.password}"
  client_certificate     = "${base64decode(azurerm_kubernetes_cluster.test.kube_config.0.client_certificate)}"
  client_key             = "${base64decode(azurerm_kubernetes_cluster.test.kube_config.0.client_key)}"
  cluster_ca_certificate = "${base64decode(azurerm_kubernetes_cluster.test.kube_config.0.cluster_ca_certificate)}"
}

resource "azurerm_resource_group" "adrons_resource_group_workspace" {
  name     = "adrons_workspace"
  location = "West US 2"

  tags = {
    environment = "Development"
  }
}

resource "azurerm_kubernetes_cluster" "test" {
  name                = "acctestaks1"
  location            = "${azurerm_resource_group.adrons_resource_group_workspace.location}"
  resource_group_name = "${azurerm_resource_group.adrons_resource_group_workspace.name}"
  dns_prefix          = "acctestagent1"

  agent_pool_profile {
    name            = "default"
    count           = 1
    vm_size         = "Standard_D1_v2"
    os_type         = "Linux"
    os_disk_size_gb = 30
  }

  service_principal {
    client_id     = var.clientid
    client_secret = var.clientsecret
  }

  tags = {
    Environment = "Production"
  }
}

resource "kubernetes_pod" "nginx" {
  metadata {
    name = "nginx-example"
    labels = {
      App = "nginx"
    }
  }

  spec {
    container {
      image = "nginx:1.7.8"
      name  = "example"

      port {
        container_port = 80
      }
    }
  }
}

resource "kubernetes_service" "nginx" {
  metadata {
    name = "nginx-example"
  }
  spec {
    selector = {
      App = kubernetes_pod.nginx.metadata[0].labels.App
    }
    port {
      port        = 80
      target_port = 80
    }

    type = "LoadBalancer"
  }
}

output "lb_ip" {
  value = kubernetes_service.nginx.load_balancer_ingress[0].ip
}
output "lb_hostname" {
value =
}
```

You can also check out this specific iteration of my developer workspace project on Github at the [example-nginx-pod-on-kubernetes](https://github.com/Adron/terraformer-todo-list/tree/example-nginx-pod-on-kubernetes) branch.

**Verification Checklist**

- Based on the infrastructure in [part 1](/2019/08/01/development-workspace-with-terraform/) and [part 2](/2019/08/16/development-workspace-with-terraform-on-azure-part-2-packer-images/) and this addition, there is now the Packer image for the Apache Cassandra 3.11.4 image, in Azure the Service Principal, Resource Group, and related collateral, and now a Kubernetes Cluster to work with.
- With this second segment done, there is now a pod running an nginx container. The container is then running as a service with a port mapping for port 80.

## Summary

At this point in the series there are enough elements to really start to get some work done deploying, building some applications, and getting some databases deployed! So *subscribe* here to the blog, follow me at [@Adron](https://twitter.com/adron) on Twitter, @[adronhall](https://twitch.tv/adronhall) on Twitch (for even more coding), and subscribe to my YouTube channel here. More material coming about how to get all of this wired together and running, until next post, cheers!
