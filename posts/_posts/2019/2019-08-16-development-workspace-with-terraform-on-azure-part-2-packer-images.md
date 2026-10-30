---
title: 'Development Workspace with Terraform on Azure: Part 2 – Packer Images'
date: 2019-08-16 18:23:18 -0700
last_modified_at: 2019-08-16 18:23:18 -0700
permalink: /2019/08/16/development-workspace-with-terraform-on-azure-part-2-packer-images/
slug: development-workspace-with-terraform-on-azure-part-2-packer-images
wp_id: 16137
original_url: https://compositecode.blog/2019/08/16/development-workspace-with-terraform-on-azure-part-2-packer-images/
categories:
- Azure
- How-to
- Infrastructure
tags:
- azure
- azure cli
- azure images
- hashicorp
- packer
- ubuntu
- virtual machines
excerpt: 'Series Links: 1, 2 (this entry) Today I’m going to walk through the install and setup of Packer, and get our first builds running for Azure. I started this work in the previous article in this series, “Development Workspace with Terraform on Azure: Part 1 – Install and Setup Terraform and Azure CLI“. This is …'
image: /wp-content/uploads/2019/08/packer-azure.jpg
---

Series Links: [1](/2019/08/01/development-workspace-with-terraform/), 2 (this entry)

Today I’m going to walk through the install and setup of Packer, and get our first builds running for Azure. I started this work in the previous article in this series, “[Development Workspace with Terraform on Azure: Part 1 – Install and Setup Terraform and Azure CLI](/2019/08/01/development-workspace-with-terraform/)“. This is needed to continue and simplify what I’ll be elaborating on in subsequent articles.

## 1: Packer

[Packer](https://www.packer.io/) is another great Hashicorp tool that is available to build virtual machine and related images for a wide range of platforms. Specifically this article is going to cover Azure but the list is long with AWS, GCP, Alicloud, Cloudstack, Digital Ocean, Docker, Hyper-V, Virtual Box, VMWare, and others!

**Download & Setup**

To download Packer navigate over to the Hashicorp [download page](https://www.packer.io/downloads.html). Currently it is at version 1.4.2. I installed this executable the same way I installed Terraform, by untar or unzipping the executable into a path I have setup for all my executable CLI’s. As shown, I simply open up the compressed file and pulled the executable over into my Apps directory, making it immediately executable just like Terraform from anywhere and any path on my system. If you want it somewhere specific and need to setup a path, refer to the [previous blog entry](/2019/08/01/development-workspace-with-terraform/) for details and links to where and how to set that up.

![packer-apps.png](/wp-content/uploads/2019/08/packer-apps.png)

If the `packer` command is executed, which I’ve done in the following image, it shows the basic commands as a good CLI would do (cuz Hashicorp makes really good CLI tools!)

![packer-default-response](/wp-content/uploads/2019/08/packer-default-response.png)

The command we’ll be working with mostly to get images setup is the `build` command. The `inspect`, `validate`, and `version` commands however will become mainstays of use when one really gets into Packer, they’re worth checking out further.

**![check-box-64](/wp-content/uploads/2019/08/check-box-64.png)Verification Checklist**

- Packer is now setup and can be executed from any path on the system.

## 2: Packer Azure Setup

The next thing that needs to be done is to setup Packer to work with Azure. To get these first few images building the Device Login will be used for authorization. Eventually, upon further automation I’ll change this to a Service Principal and likely recreate images accordingly, but for now Device Login is going to be fine for these examples. Most of the directions are available via HashiCorp Docs located [here](https://www.packer.io/docs/builders/azure-setup.html). As always, I’m going to elaborate a bit beyond the docs.

The *Device Login* will need three pieces of information: A *SubscriptionID*, *Resource Group*, and *Storage Account*. The Resource Group will be used in Azure to maintain this group of resources created specific to the Resource Group that live around a particular life-cycle of work. The Storage Account is just a place to store the images that will be created. The SubscriptionID is the ID of your account with Azure.

**NOTE:** To enable this mode, simply don’t set client\_id and client\_secret in the Packer build provider.

To get your SubscriptionID just type `az login` at the terminal. The response will include this value designated simply as “id”. Another value that you’ll routinely need is displayed here too the “tenant\_id”. Once logged in you can also get a list of accounts and respective SubscriptionID values for each of the accounts you might have as I’ve done here.

![cleanup.png](/wp-content/uploads/2019/08/cleanup-1.png)

Here you can see I’ve authenticated against and been authorized in two Azure Accounts. Location also needs to be determined, and can be done so with `az account list-locations`.

![locations.png](/wp-content/uploads/2019/08/locations-2.png)

This list will continue and continue and continue. From it, a singular location will be chosen for the storage.

In a bash script, I go ahead and assign these values that I’ll need to build this particular image.

```
GROUPNAME="adrons-images"
LOCATION="westus2"
STORAGENAME="adronsimagestorage"
```

Now the next step is to create the Resource Group and Storage. With a few `echo` commands to print out what is going on to the console, I add these commands as shown.

```
echo 'Creating the managed resource group for images.'

az group create --name $GROUPNAME --location $LOCATION

echo 'Creating the storage account for image storage.'

az storage account create \
 --name $STORAGENAME --resource-group $GROUPNAME \
 --location $LOCATION \
 --sku Standard_LRS \
 --kind Storage
```

The final command here is another `echo` just to identify what is going to be built and then the Packer build command itself.

```
echo 'Building Apache cluster node image.'

packer build node.json
```

The script is now ready to be run. I’ve placed the script inside my packer phase of my build project (see previous [post](/2019/08/01/development-workspace-with-terraform/) for overall build project and the [repository here](https://github.com/Adron/terraformer-todo-list) for details). The last thing needed is a Packer template to build.

**![check-box-64](/wp-content/uploads/2019/08/check-box-64.png)Verification Checklist**

- Packer is now setup and can be executed from any path on the system.
- The build has been setup for use with Device Login for this first build.
- A script is now available to execute Packer for a build without needing to pass parameters every single time and simplifies assurances that the respective storage and resource groups are available for creation of the image.

## 3: Azure Images

The next step is getting an image or some images built that are needed for further work. For my use case I want several key images built around various servers and their respective services that I want to use to deploy via Terraform. Here’s an immediate shortlist of images we’ll create:

1. [Apache Cassandra](http://cassandra.apache.org/) Node – An image that is built with the latest Apache Cassandra installed and ready for deployment into a cluster. In this particular case that would be Apache Cassandra v4, albeit I’m going to go with 3.11.4 first and then work on getting v4 installed in a subsequent post. The installation instructions we’ll mostly be following can be found [here](http://cassandra.apache.org/download/).
2. [Gitlab](https://about.gitlab.com/) Server – This is a product I like to use, especially for pre-rolled build services and all of those needs. For this it takes care of all source control, build services, and any related work that needs to be from inside the workspace itself that I’m building. i.e. it’s a necessary component for an internal corporate style continuous build or even continuous integration setup. It just happens this is all getting setup for use internally but via a public cloud provider on Azure! It can be done in parallel to other environments that one would prospectively control and manage autonomous of any cloud provider. The [installation instructions](https://about.gitlab.com/install/) we’ll largely be following are also available via Gitlab [here](https://about.gitlab.com/install/).
3. [DataStax Enterprise 6.7](https://www.datastax.com/products/datastax-enterprise) – DataStax Enterprise is built on Apache Cassandra and extends the capabilities of that database with multi-model options for graph, analytics, search, and many other capabilities and security. For [download](https://downloads.datastax.com/#enterprise) and installation most of the instructions I’ll be using are located [here](https://docs.datastax.com/en/install/6.7/install/installTOC.html).

**![check-box-64](/wp-content/uploads/2019/08/check-box-64.png)Verification Checklist**

- Packer is now setup and can be executed from any path on the system.
- The build has been setup for use with Device Login for this first build.
- A script is now available to execute Packer for a build without needing to pass parameters every single time and simplifies assurances that the respective storage and resource groups are available for creation of the image.
- Now there is a list of images we need to create, in which we can work from to create the images in Azure.

## 4: Building an Azure Image with Packer

The first image I want to create is going to be used for an Apache Cassandra 3.11.4 Cluster. First a basic image test is a good idea. For that I’ve used the example below to build a basic Ubuntu 16.04 image.

In the code below there are also two environment variables setup, which I’ve included in my bash profile so they’re available on my machine whenever I run this Packer build or any of the Terraform builds. You can see they’re setup in the variables section with a `` "{{env ​`​TF_VAR_tenant_id`}}" ``. Not that the TF\_VAR\_tenant\_id is prefaced with TF\_VAR per Terraform convention, which in Terraform makes the variable just “tenant\_id” when used. Also note that things that might look like single quotes are indeed back ticks, not single quotes around TF\_VAR\_tenant\_id. Sometimes the blog formats those oddly so I wanted to call that out! (For example of environment variables, I set up all of them for the Service Principal setup below, just scroll further down)

```
{
  "variables": {
    "tenant_id": "{{env `TF_VAR_tenant_id`}}",
    "subscription_id": "{{env `TF_VAR_subscription_id`}}",
    "storage_account": "adronsimagestorage",
    "resource_group_name": "adrons-images"
  },

  "builders": [{
    "type": "azure-arm",

    "tenant_id": "{{user `tenant_id`}}",
    "subscription_id": "{{user `subscription_id`}}",

    "managed_image_resource_group_name": "{{user `resource_group_name`}}",
    "managed_image_name": "base_ubuntu_image",

    "os_type": "Linux",
    "image_publisher": "Canonical",
    "image_offer": "UbuntuServer",
    "image_sku": "16.04-LTS",

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
      "echo 'does this even work?'"
    ],
    "inline_shebang": "/bin/sh -x",
    "type": "shell"
  }]

}
```

[View the gist on GitHub](https://gist.github.com/Adron/1abebf4da0604a6f30e885cc4b717886/ad2ee8e13196499fec12114aad61185da4a67a2a/packer_ubuntu.json)

During this build, when Packer begins there will be several prompts during the build to authorize the resources being built. Because earlier in the post Device Login was used instead of a Service Principal this step is necessary. It looks something like this.

![device-login](/wp-content/uploads/2019/08/device-login.png)

You’ll need to then select, copy, and paste that code into the page at <https://microsoft.com/devicelogin>.

![logging-in-code-ddevice-login](/wp-content/uploads/2019/08/logging-in-code-ddevice-login.png)

This will happen a few times and eventually the build will complete and the image will be available. What we really want to do however is get a Service Principal setup and use that so the process can be entirely automated.

**![check-box-64](/wp-content/uploads/2019/08/check-box-64.png)Verification Checklist**

- Packer is now setup and can be executed from any path on the system.
- The build has been setup for use with Device Login for this first build.
- A script is now available to execute Packer for a build without needing to pass parameters every single time and simplifies assurances that the respective storage and resource groups are available for creation of the image.
- We have one base image building, to prove out that our build template we’ll start with is indeed working. It is always a good idea to get a base build image template working to provide something in which to work from.

## 5: Azure Service Principal for Automation

Ok, a Service Principal is needed now. This is singular command, but it has to be very specifically the command from what I can tell. Before running that though, know where you are going to store or how you will pass the client id and client secret that will be provided by the principal when it is created.

The command for this is `az ad sp create-for-rbac -n "Packer" --role contributor --scopes /subscriptions/00000000-0000-0000-0000-000000000` where all those zeros are the Subscription ID. When this executes and completes all the peripheral values that are needed for authorization via Service Principal.

![the-rbac](/wp-content/uploads/2019/08/the-rbac-1.png)

One of the easiest ways to keep all of the bits out of your repositories is to setup environment variables. If there’s a secrets vault or something like that then it would be a good idea to use that, but for this example I’m going to setup use of environment variables in the template.

Another thing to notice, which is important when building these systems, is that the “Retrying role assignment creation: 1/36″ message. Which points to the fact there are 36 retries built into this because of timing and other irregularities in working with cloud systems. For various reasons, this means when coding against such systems we routinely will have to put in timeouts, waits, and other errata to ensure we get messages we want or mark things disabled as needed.

After running that, just for clarity, here’s what my .bashrc/bash\_profile file looks like with the added variables.

```
export TF_VAR_clientid="00000000-0000-0000-0000-000000000"
export TF_VAR_clientsecret="00000000-0000-0000-0000-000000000"
export TF_VAR_tenant_id="00000000-0000-0000-0000-000000000"
export TF_VAR_subscription_id="00000000-0000-0000-0000-000000000"
```

With that set, a quick `source ~/.bashrc` or `source ~/.bash_profile` and the variables are all set for use.

**![check-box-64](/wp-content/uploads/2019/08/check-box-64.png)Verification Checklist**

- Packer is now setup and can be executed from any path on the system.
- The build has been setup for use with Device Login for this first build.
- A script is now available to execute Packer for a build without needing to pass parameters every single time and simplifies assurances that the respective storage and resource groups are available for creation of the image.
- We have one base image building, to prove out that our build template we’ll start with is indeed working. It is always a good idea to get a base build image template working to provide something in which to work from.
- The Service Principal is now setup so the image can be built with full automation.
- Environment variables are setup so that they won’t be checked in to the code and configuration repository.

## 6: Apache Cassandra 3.11.4 Image

Ok, all the pieces are in place. With confirmation that the image builds, that Packer is installed correctly, with Azure Service Principal, Managed Resource Group, and related collateral setup now, building an actual image with installation steps for Apache Cassandra 3.11.4 can now begin!

First add the client\_id and client\_secret environment variables to the variables section of the template.

```
    "client_id": "{{env `TF_VAR_clientid`}}",
    "client_secret": "{{env `TF_VAR_clientsecret`}}",
    "tenant_id": "{{env `TF_VAR_tenant_id`}}",
    "subscription_id": "{{env `TF_VAR_subscription_id`}}",
```

Next add those same variables to the builder for the image in the template.

```
    "client_id": "{{user `client_id`}}",
    "client_secret": "{{user `client_secret`}}",
    "tenant_id": "{{user `tenant_id`}}",
    "subscription_id": "{{user `subscription_id`}}",
```

That whole top section of template configuration looks like this now.

```javascript
{
  "variables": {
    "client_id": "{{env `TF_VAR_clientid`}}",
    "client_secret": "{{env `TF_VAR_clientsecret`}}",
    "tenant_id": "{{env `TF_VAR_tenant_id`}}",
    "subscription_id": "{{env `TF_VAR_subscription_id`}}",
    "imagename": "something",
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
```

Now the image can be executed, but let’s streamline the process a little bit more. Since I won’t want but only one image at any particular time from this template and I want to use the template in a way where I can create images and pass in a few more pertinent pieces of information I’ll tweak that in the Packer build script.

Below I’ve added the variable name for the image, and dubbed in Cassandra so that I can specifically reference this image in the bash script with `IMAGECASSANDRA="basecassandra"`. Next I added a command to delete an existing image that would be called this with the `az image delete -g $GROUPNAME -n $IMAGECASSANDRA` line of script. Finally toward the end of the file I’ve added the variable to be passed into the template with `packer build -var 'imagename='$IMAGECASSANDRA node-cassandra.json`. Note the odd way to concatenate imagename and the variable of the passed in variable from the bash script. This isn’t super clear which way to do this, but after some troubleshooting this at least works on Linux! I’m assuming it works on MacOS, if anybody else tries it and it doesn’t please let me know.

```bash
GROUPNAME="adrons-images"
LOCATION="westus2"
STORAGENAME="adronsimagestorage"
IMAGECASSANDRA="basecassandra"

echo 'Deleting existing image.'

az image delete -g $GROUPNAME -n $IMAGECASSANDRA

echo 'Creating the managed resource group for images.'

az group create --name $GROUPNAME --location $LOCATION

echo 'Creating the storage account for image storage.'

az storage account create \
 --name $STORAGENAME --resource-group $GROUPNAME \
 --location $LOCATION \
 --sku Standard_LRS \
 --kind Storage

echo 'Building Apache cluster node image.'

packer build -var "'imagename=$IMAGECASSANDRA'" node-cassandra.json
```

With that done the build can be run things without needing to manually delete the image each time since it is part of the script now. The next part to add to the template is more of the needed [installation steps](http://cassandra.apache.org/download/) for Apache Cassandra. These steps can be found on the Apache Cassandra site [here](http://cassandra.apache.org/download/).

Under the *provisioners* section of the Packer template I’ve added the installation steps and removed the *sudo* part of the commands. Since this runs as root there’s really no need for *sudo*. The inline part of the *provisioner* when I finished looks like this.

```
    "inline": [
      "echo 'Starting Cassandra Repo Add & Installation.'",
      "echo 'deb http://www.apache.org/dist/cassandra/debian 311x main' | tee -a /etc/apt/sources.list.d/cassandra.sources.list",
      "curl https://www.apache.org/dist/cassandra/KEYS | apt-key add -",
      "apt-get update",
      "apt-key adv --keyserver pool.sks-keyservers.net --recv-key A278B781FE4B2BDA",
      "apt-get install cassandra"
    ],﻿
```

With that completed we now have the full workable template to build a node for use in starting or using as a node within an Apache Cassandra cluster. All the key pieces are there. The finished template is below, with the build script just below that.

```
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
      "echo 'Starting Cassandra Repo Add & Installation.'",
      "echo 'deb http://www.apache.org/dist/cassandra/debian 311x main' | tee -a /etc/apt/sources.list.d/cassandra.sources.list",
      "curl https://www.apache.org/dist/cassandra/KEYS | apt-key add -",
      "apt-get update",
      "apt-key adv –keyserver pool.sks-keyservers.net –recv-key A278B781FE4B2BDA",
      "apt-get -y install cassandra"
    ],
    "inline_shebang": "/bin/sh -x",
    "type": "shell"
  }]

}
```

[View the gist on GitHub](https://gist.github.com/Adron/de993a7053bbd8f27aa850b16b279d57/c3b615b997be2922e50860a988df195322499cec/node-cassandra.json)

```
GROUPNAME="adrons-images"
LOCATION="westus2"
STORAGENAME="adronsimagestorage"
IMAGECASSANDRA="basecassandra"

echo 'Deleting existing image.'

az image delete -g $GROUPNAME -n $IMAGECASSANDRA

echo 'Creating the managed resource group for images.'

az group create –name $GROUPNAME –location $LOCATION

echo 'Creating the storage account for image storage.'

az storage account create \
 –name $STORAGENAME –resource-group $GROUPNAME \
 –location $LOCATION \
 –sku Standard_LRS \
 –kind Storage

echo 'Building Apache cluster node image.'

packer build -var 'imagename='$IMAGECASSANDRA node-cassandra.json
```

[View the gist on GitHub](https://gist.github.com/Adron/f99ab85c58d341199de69ec85d101d7d/bc855544c895a1e5dbca713d3717441250fe416f/build.sh)

**![check-box-64](/wp-content/uploads/2019/08/check-box-64.png)Verification Checklist**

- Packer is now setup and can be executed from any path on the system.
- The build has been setup for use with Device Login for this first build.
- A script is now available to execute Packer for a build without needing to pass parameters every single time and simplifies assurances that the respective storage and resource groups are available for creation of the image.
- We have one base image building, to prove out that our build template we’ll start with is indeed working. It is always a good idea to get a base build image template working to provide something in which to work from.
- The Service Principal is now setup so the image can be built with full automation.
- Environment variables are setup so that they won’t be checked in to the code and configuration repository.
- Packer add package repository and installs Cassandra 3.11.4 on Ubuntu 18.04 LTS in Azure.

I’ll get to the next images real soon, but for now, go enjoy the weekend and the next post will be up in this series in about a week and a half!
