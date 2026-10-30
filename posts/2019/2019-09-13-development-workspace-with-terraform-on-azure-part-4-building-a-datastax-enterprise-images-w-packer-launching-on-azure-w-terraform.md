---
title: 'Development Workspace with Terraform on Azure: Part 4 – DSE w/ Packer + Importing State 4 Terraform'
date: 2019-09-13 11:12:30 -0700
last_modified_at: 2019-09-18 15:26:28 -0700
permalink: /2019/09/13/development-workspace-with-terraform-on-azure-part-4-building-a-datastax-enterprise-images-w-packer-launching-on-azure-w-terraform/
slug: development-workspace-with-terraform-on-azure-part-4-building-a-datastax-enterprise-images-w-packer-launching-on-azure-w-terraform
wp_id: 16338
original_url: https://compositecode.blog/2019/09/13/development-workspace-with-terraform-on-azure-part-4-building-a-datastax-enterprise-images-w-packer-launching-on-azure-w-terraform/
categories:
- Azure
- How-to
- Infrastructure
tags:
- azure
- cloud
- cloud infrastructure
- datastax
- datastax enterprise
- hashicorp
- infrastructure
- infrastructure as code
- microsoft
- terraform
excerpt: The next thing I wanted setup for my development workspace is a DataStax Enterprise Cluster. This will give me all of the Apache Cassandra database features plus a lot of additional features around search, OpsCenter, analytics, and more. I’ll elaborate on that in some future posts. For now, let’s get an image built we can …
image: /wp-content/uploads/2019/08/terraform-azure.png
---

The next thing I wanted setup for my development workspace is a DataStax Enterprise Cluster. This will give me all of the [Apache Cassandra](http://cassandra.apache.org/) database features plus a lot of additional features around search, OpsCenter, analytics, and more. I’ll elaborate on that in some future posts. For now, let’s get an image built we can use to add nodes to our cluster and setup some other elements.

## 1: DataStax Enterprise

The general installation instructions for the process I’m stepping through here in this article can be found in [this documentation](https://docs.datastax.com/en/install/6.7/install/installDEBdse.html#installDEBdse__postreq). To do this I started with a Packer template like the one I setup in the [second part of this series](/2019/08/16/development-workspace-with-terraform-on-azure-part-2-packer-images/). It looks, with the installation steps taken out, just like the code below.

```javascript
{
  "variables": {
    "client_id": "{{env `TF_VAR_clientid`}}",
    "client_secret": "{{env `TF_VAR_clientsecret`}}",
    "tenant_id": "{{env `TF_VAR_tenant_id`}}",
    "subscription_id": "{{env `TF_VAR_subscription_id`}}",
    "imagename": "",
    "storage_account": "adronsimagestorage",
    "resource_group_name": "adrons-images"
  },

  "builders": [{
    "type": "azure-arm",

    "client_id": "{{user `client_id`}}",
    "client_secret": "{{user `client_secret`}}",
    "tenant_id": "{{user `tenant_id`}}",
    "subscription_id": "{{user `subscription_id`}}",

    "managed_image_resource_group_name": "{{user `resource_group_name`}}",
    "managed_image_name": "{{user `imagename`}}",

    "os_type": "Linux",
      "image_publisher": "Canonical",
      "image_offer": "UbuntuServer",
      "image_sku": "18.04-LTS",

    "azure_tags": {
        "dept": "Engineering",
        "task": "Image deployment"
    },

    "location": "westus2",
    "vm_size": "Standard_DS2_v2"
  }],
  "provisioners": [{
    "execute_command": "chmod +x {{ .Path }}; {{ .Vars }} sudo -E sh '{{ .Path }}'",
    "inline": [
        ""
    ],
    "inline_shebang": "/bin/sh -x",
    "type": "shell"
  }]
}
```

In the section marked “inline” I setup the steps for installing DataStax Enterprise.

```javascript
        "apt-get update",
        "apt-get install -y openjdk-8-jre",
        "java -version",
        "apt-get install libaio1",
        "echo \"deb https://debian.datastax.com/enterprise/ stable main\" | sudo tee -a /etc/apt/sources.list.d/datastax.sources.list",
        "curl -L https://debian.datastax.com/debian/repo_key | sudo apt-key add -",
        "apt-get update",
        "apt-get install -y dse-full"
```

The first part of this process the machine image needs Open JDK installed, which I opted for the required version of 1.8. For more information about the Open JDK check out this material:

- <https://openjdk.java.net/>
- <https://openjdk.java.net/install/> for more installation options.

The next thing I needed to do was to get everything setup so that I could use this Azure Image to build an actual Virtual Machine. Since this process however is built outside of the primary Terraform main build process, I need to import the various assets that are created for Packer image creation and the actual Packer images. By importing these asset resources into Terraform’s state I can then write configuration and code around them as if I’d created them within the main Terraform build process. This might sound a bit confusing, but check out this process and it might make more sense. If it is still confusing do let me know, ping me on Twitter [@adron](https://twitter.com/adron) and I’ll elaborate or edit things so that they read better.

**![check-box-64](/wp-content/uploads/2019/08/check-box-64.png)Verification Checklist**

- At this point there now exists a solidly installed and baked image available for use to create a Virtual Machine.

## 2: Terraform State & Terraform Import Resources

Ok, if you check out [part 1](/2019/08/01/development-workspace-with-terraform/) of this series I setup Azure CLI, Terraform, and the pertinent configuration and parts to build out infrastructure as code using HCL ([Hashicorp Configuration Language](https://github.com/hashicorp/hcl)) with a little bit of Bash as glue here and there. Then in Part 2 and Part 3 I setup Packer images and some Terraform resources like Kubernetes and such. All of that is great, but these two parts of the process are now in entirely two different unknown states. The two pieces are:

1. Packer Images
2. Terraform Infrastructure

The Terraform Infrastructure doesn’t know the Packer Images exist, but they are sitting there in a resource group in Azure. The way to make Terraform aware that these images exist is to import the various things that store the images. To import these resources into the Terraform state, before doing an apply, run the `terraform import` command.

In order to get all of the resources we need in which to operate and build images, the following import commands need issued. I wrote a script file to help me out with each of these, and used jq to make retrieval of the Packer created Azure Image ID’s a bit easier. That code looks like this:

```bash
BASECASSANDRA=$(az image list | jq 'map({name: "basecassandra", id})' | jq -r '.[0].id')
BASEDSE=$(az image list | jq 'map({name: "basedse", id})' | jq -r '.[0].id')
```

Breaking down the jq commands above, the following actions are being taken. First, the Azure CLI command is issued, `az image list` which is then piped `|` into the jq command of `jq 'map({name: "theimagenamehere", id})'`. This command takes the results of the Azure CLI command and finds the name element with the appropriate image name, matches that and then gets the id along with it. That command is then piped into another command that returns just the value of the id `jq -r '.id'`. The -r is a switch that tells jq to just return the raw data, without enclosing double quotes.

I also needed to import the resource group all of these are in too, which following a similar jq command style of piping one command’s results into another, issued this command to get the Resource Group ID `RG-IMPORT=$(az group show --name adronsimages | jq -r '.id')`. With those three ID’s there is one more element needed to be able to import these into Terraform state.

The Terraform resources that these imported pieces of state will map to need declared, which means the Terraform HCL itself needs written out. For that, there are the two images that are needed and the Resource Group. I added the images in an images.tf files and the Resource Group goes in the resource\_groups.tf file.

```javascript
resource "azurerm_image" "basecassandra" {
  name                = "basecassandra"
  location            = "West US"
  resource_group_name = azurerm_resource_group.imported_adronsimages.name

  os_disk {
    os_type  = "Linux"
    os_state = "Generalized"
    blob_uri = "{blob_uri}"
    size_gb  = 30
  }
}

resource "azurerm_image" "basedse" {
  name                = "basedse"
  location            = "West US"
  resource_group_name = azurerm_resource_group.imported_adronsimages.name

  os_disk {
    os_type  = "Linux"
    os_state = "Generalized"
    blob_uri = "{blob_uri}"
    size_gb  = 30
  }
}
```

Then the Resource Group.

```javascript
resource "azurerm_resource_group" "imported_adronsimages" {
  name     = "adronsimages"
  location = var.locationlong

  tags = {
    environment = "Development Images"
  }
}
```

Now, issuing these Terraform commands will pull the current state of those resource into the state, which we can then issue further Terraform commands and applies from.

```bash
terraform import azurerm_image.basedse $BASEDSE
terraform import azurerm_image.basecassandra $BASECASSANDRA
terraform import azurerm_resource_group.imported_adronsimages $RG_IMPORT
```

Running those commands, the results come back something like this.

![terraform-imports](https://compositecode.blog/wp-content/uploads/2019/09/terraform-imports.png)

**Verification Checklist**

- At this point there now exists a solidly installed and baked image available for use to create a Virtual Machine.
- Now there is also state in Terraform, that understands where and what these resources are.

## Summary, for now.

This post is shorter than I’d like it to be. But it was taking to long for the next steps to get written up – but fear not they’re on the way! In the coming post I’ll cover more of other resource elements we’ll need to import, what is next for getting a virtual machine built off of the image that is now available, some Terraform HCL refactoring, and most importantly putting together the actual DataStax Enterprise / Apache Cassandra Clusters! So stay tuned, subscribe to the blog, and of course follow me on the Twitters [@Adron](https://twitter.com/adron).
