---
title: Wat?! Ugh Terraform State is Complicated Sometimes! ‘url has no host’
date: 2019-09-26 11:45:25 -0700
last_modified_at: 2019-10-21 21:57:19 -0700
permalink: /2019/09/26/wat-ugh-terraform-state-is-complicated-sometimes-url-has-no-host/
slug: wat-ugh-terraform-state-is-complicated-sometimes-url-has-no-host
wp_id: 16366
original_url: https://compositecode.blog/2019/09/26/wat-ugh-terraform-state-is-complicated-sometimes-url-has-no-host/
categories:
- Azure
- How-to
- Infrastructure
tags:
- iac
- infrastructure
- infrastructure as code
- infrastructure as config
- terraform
excerpt: As I’ve been working through the series (part 1, 2, 3, and 4 so far), a number of issues come up (like this one), and this seemed like a good one to post too. As I’ve been working through I started stumbling into this error around destroying images via terraform destroy . Now, I’m not just …
image: /wp-content/uploads/2019/08/device-login.png
---

As I’ve been working through the series (part [1](/2019/08/01/development-workspace-with-terraform/), [2](/2019/08/16/development-workspace-with-terraform-on-azure-part-2-packer-images/), [3](/2019/08/28/development-workspace-with-terraform-on-azure-part-3-next-step-kubernetes/), and [4](/2019/09/13/development-workspace-with-terraform-on-azure-part-4-building-a-datastax-enterprise-images-w-packer-launching-on-azure-w-terraform/) so far), a number of issues come up ([like this one](/2019/08/06/error-build-azure-arm-errored-adal-failed-to-execute-the-refresh-request-error/)), and this seemed like a good one to post too. As I’ve been working through I started stumbling into this error around destroying images via `terraform destroy` . Now, I’m not just creating them with `terraform apply` and then trying to destroy them. I’m creating the images via Packer, then importing the state (see [part 4](/2019/09/13/development-workspace-with-terraform-on-azure-part-4-building-a-datastax-enterprise-images-w-packer-launching-on-azure-w-terraform/) for the series for details) and then when I clean up the environment trying to `terraform destroy` which shows this error.

[…lost image…]

I had taken the default [azurerm\_image](https://www.terraform.io/docs/providers/azurerm/r/image.html) resource configuration from the Hashicorp docs site that I tweaked just a little bit.

```bash
resource "azurerm_image" "basedse" {
  name = "basedse"
  location = "West US"
  resource_group_name = azurerm_resource_group.imported_adronsimages.name

  os_disk {
    os_type = "Linux"
    os_state = "Generalized"
    blob_uri = "{blob_uri}"
    size_gb = 30
  }
}
```

The thing causing the error is the “{blog\_uri}”. Which in general, I’d assume that this should be pulled or derived from the existing image created by packer when imported. But the syntax above just doesn’t cut it for actions post-import of the image state.

## Time Consuming Troubleshooting

To troubleshoot and confirm this issue takes a long time. Create the image, which is ~15-20 minutes, then run an apply. The apply, even if most of the creation is minimized to imports and the few other things that are created, takes several minutes in Azure. Then a destroy takes several minutes. So all in all, one test cycle is about ~30 minutes.

## The First Tricky Fix

I went through several iterations of attempting to get that part of the import of the state pulled in. That didn’t work out so well. What did though, was the simplist of actions, I deleted `blob_uri = "{blog_uri}"`!  Then upon `terraform apply` or `terraform destroy` I got a full cycled application of changes, etc, after adding the state and on destroy terraform wiped out everything as expected!

## Problem Fixed, Problem Created

On to the next things! But oh wait, there is another problem. Now if I setup a VM to be created based off of the image, the state doesn’t have the `blog_uri`. Great, back to square one right? Not entirely, subscribe, keep reading and I’ll have the next steps for this coming real soon!
