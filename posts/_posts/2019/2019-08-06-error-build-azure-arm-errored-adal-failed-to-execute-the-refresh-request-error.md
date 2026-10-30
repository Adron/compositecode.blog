---
title: 'Error “Build ‘azure-arm’ errored: adal: Failed to execute the refresh request. Error =…”'
date: 2019-08-06 13:50:08 -0700
last_modified_at: 2019-08-15 17:34:46 -0700
permalink: /2019/08/06/error-build-azure-arm-errored-adal-failed-to-execute-the-refresh-request-error/
slug: error-build-azure-arm-errored-adal-failed-to-execute-the-refresh-request-error
wp_id: 16163
original_url: https://compositecode.blog/2019/08/06/error-build-azure-arm-errored-adal-failed-to-execute-the-refresh-request-error/
categories:
- Infrastructure
tags:
- azure
- hashicorp
- infrastructure
- packer
excerpt: So I’ve been fighting through getting some Packer images built in Azure again. I haven’t done this in almost a year but as always I’ve just walked in and BOOM I’ve got an error already. This first error I’ve gotten is after I create an Resource Group and then a Service Principal. I’ve gotten all …
image: /wp-content/uploads/2019/08/ohgawd.jpg
---

So I’ve been fighting through getting some Packer images built in Azure again. I haven’t done this in almost a year but as always I’ve just walked in and BOOM I’ve got an error already. This first error I’ve gotten is after I create an Resource Group and then a Service Principal. I’ve gotten all the variables set and then I validated my json for the node I’m trying to build and then tried to build, which is when the error occurs.

The exact text of the error is “*Build ‘azure-arm’ errored: adal: Failed to execute the refresh request. Error = ‘Get <http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fmanagement.azure.com%2F>: dial tcp 169.254.169.254:80: connect: no route to host’*”

Now this leaves me with a number of questions. What is this 169.254.169.254 and why is that the IP for the attempt to communicate. That seems familiar when using Hashicorp tooling. Also, why is there no route to the host? This example (as I’ve pasted below) is the same thing as the example in the Microsoft [docs here](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/build-image-with-packer).

The JSON Template for Packer

```
{
  "variables": {
    "client_id": "{{env `TF_VAR_clientid`}}",
    "client_secret": "{{env `TF_VAR_clientsecret`}}",
    "tenant_id": "{{env `TF_VAR_tenant_id`}}",
    "subscription_id": "{{env `TF_VAR_subscription_id`}}"
  },

  "builders": [{
    "type": "azure-arm",

    "client_id": "{{user `client_id`}}",
    "client_secret": "{{user `client_secret`}}",
    "tenant_id": "{{user `tenant_id`}}",
    "subscription_id": "{{user `subscription_id`}}",

    "managed_image_resource_group_name": "myResourceGroup",
    "managed_image_name": "myPackerImage",

    "os_type": "Linux",
    "image_publisher": "Canonical",
    "image_offer": "UbuntuServer",
    "image_sku": "16.04-LTS",

    "azure_tags": {
        "dept": "Engineering",
        "task": "Image deployment"
    },

    "location": "East US",
    "vm_size": "Standard_DS2_v2"
  }],
  "provisioners": [{
    "execute_command": "chmod +x {{ .Path }}; {{ .Vars }} sudo -E sh '{{ .Path }}'",
    "inline": [
      "apt-get update",
      "apt-get upgrade -y",
      "apt-get -y install nginx",

      "/usr/sbin/waagent -force -deprovision+user && export HISTSIZE=0 && sync"
    ],
    "inline_shebang": "/bin/sh -x",
    "type": "shell"
  }]
}
```

[View the gist on GitHub](https://gist.github.com/Adron/cce6b32a1e38197eaebac2b6bfc60cf5/416a7da09b6ec7b3caa1ac7e6dc21381fbbadab6/node.json)

Any ideas? Thoughts?

When I get this sorted, will update with answers!

## UPDATED @ 17:47 Aug 7th with 95% of the SOLUTION

Big shout out of thanks to Jamie Phillips [@phillipsj73](https://twitter.com/phillipsj73) for the direct assist and Patrick Svensson [@firstdrafthell](https://twitter.com/firstdrafthell) for the [ping connection](https://twitter.com/firstdrafthell/status/1158847158843531264) via the Twitter. Big props for the patience to dig through my template for Packer and figuring out what happened. On that note, a few things actually were wrong, here’s the run down.

## 1: Environment Variables, Oops

Jamie noticed after we took a good look. I hadn’t used the actual variable names of the environment variables nor assigned them correctly. Notice at the top, the first block is for variables. Each of the variables above is correct, for declaring the environment variables themselves. These of course are then set via my bash startup scripts.

```
{
  "variables": {
    "client_id": "{{env `TF_VAR_clientid`}}",
    "client_secret": "{{env `TF_VAR_clientsecret`}}",
    "tenant_id": "{{env `TF_VAR_tenant_id`}}",
    "subscription_id": "{{env `TF_VAR_subscription_id`}}"
  },
```

Which in turn, what this does is take the environment variables and passes them to what will be user variables for the builder block to make use of. Which at this point you may see what I did wrong. These variables are named client\_id, client\_secret, tenant\_id, and subscription\_id which means in the builders blog it needs to be assigned as such.

```
    "client_id": "{{user `client_id`}}",
    "client_secret": "{{user `client_secret`}}",
    "tenant_id": "{{user `tenant_id`}}",
    "subscription_id": "{{user `subscription_id`}}",
```

Notice in the original code above from the Github gist I re-assigned them back to the actual environment variables which won’t work. With that fixed the build almost worked. I’d made one other mistake.

## 2: Resource Groups != Managed Resource Groups

Ok, so Microsoft has an old way and a new way I’ve been realizing of how they want to build images. Has anyone realized they’ve had to reinvent their entire cloud offering from the back end up more than once? I’m… well, let’s just go with speechless. More on that later.

So creating a resource group by selecting resource groups in the interface and then creating a resource group had not appeared to work. Something was amiss still so I went a used the CLI command. Yes, it may be the case that the Azure CLI is not in sync with the Azure Console UI. But alas, this got it to work. I had to make sure that the Resource Group created is indeed a Managed Resource Group per [this](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-overview#resource-groups). It also left me pondering that maybe, even though they’re very minimalist and to the point, these [instructions here](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/build-image-with-packer) might need some updating with actual detailed specifics.

I got the correct Managed Resource Group and changed it to what I had just created, which is the `managed_image_resource_group_name` property and commenced a build again. It ran for many minutes, I didn’t count, and at the end BOOM! Another big error.

![explosion](/wp-content/uploads/2019/08/explosion.png)

This error actually stated that it was likely Packer itself. I hadn’t had one of these before! With that I’m wrapping up for today (the 6th of August) but will be back at it tomorrow to get this resolved.

## UPDATED @ 18:34 Aug 8th – Day 2 of A Solution?

Notice this title for this update is a question, because it’s a solution but it isn’t. I’ve fought through a number of things trying to get this to work but so far it seems like this. The Packer template is finishing to build on the creation side of things but when it is cleaning up it comes crashing down. It then requests I file a bug, which I did. The bug is listed here on the Packer repo on Github in the issues.

<https://github.com/hashicorp/packer/issues/7961>

Here is the big catch to this bug though. I went in and could build a VM from the image that is created even though Packer is throwing an error. I went ahead and created the [crash.log gist](https://gist.github.com/Adron/10e760980bef1663d52bf6240ed89fda) and requisite details so this bug could be further researched, but it honestly seems like Azure just isn’t reporting a cleanup of the resources correctly back to Packer. But at this point I’m not entirely sure. The current state of the Packer template file I’m trying to build is available via a [gist](https://gist.github.com/Adron/72ee2b01e15e400a505b423de6d7284f) too.

So at this point I’m kind of in a holding pattern waiting to figure out how to clean up this automation step. I need two functional elements, one is this to create images that are clean and primarily have the core functionality and capabilities for the server software – i.e. the Apache Cassandra or DSE Cluster nodes. The second is to get a Kubernetes Cluster built and have that run nodes and something like a Cassandra operator. With the VM route kind of on hold until this irons itself out with Azure, I’m going to spool up a Kubernetes cluster in Azure and start working on that tomorrow.

## UPDATED @ 16:02 Aug 14th – Solution is in place!

I filed the issue [#7961](https://github.com/hashicorp/packer/issues/7961) listed previously in the last update, which was different but effectively a duplicate of [#7816](https://github.com/hashicorp/packer/issues/7816) that is fixed with the patch in [#7837](https://github.com/hashicorp/packer/pull/7837). I rolled back to Packer version 1.4.1 and also got it to work, which points to the issues being something rooted in version 1.4.2. With that, everything is working again and I’ve got a good Packer build. The respective completed blog entry where I detail what I’m putting together will be coming out very soon now that things are cooking appropriately!

Also note that the last bug, file in [#7961](https://github.com/hashicorp/packer/issues/7961) wasn’t the bug that originally started this post, but was where I ended up with. The build of the image however, being the important thing, is working just fine now! Whew!
