---
title: Terraform “Invalid JWT Signature.”
date: 2018-10-12 11:40:18 -0700
last_modified_at: 2018-10-12 15:36:11 -0700
permalink: /2018/10/12/terraform-invalid-jwt-signature/
slug: terraform-invalid-jwt-signature
wp_id: 14589
original_url: https://compositecode.blog/2018/10/12/terraform-invalid-jwt-signature/
categories:
- Infrastructure
tags:
- cloud computing
- google
- Google Cloud Platform
- jwt
- jwt signature
- terraform
excerpt: I ran into this issue recently. The “Invalid JWT Signature.” error while running some Terraform. It appeared to occur whenever I was setting up a bucket in Google Cloud Platform to use for a back-end to store Terraform’s state. In console, here’s the exact error. My first quick searches uncovered some Github issues that looked …
image: /wp-content/uploads/2018/10/terraform-long-header.png
---

I ran into this issue recently. The “Invalid JWT Signature.” error while running some Terraform. It appeared to occur whenever I was setting up a bucket in Google Cloud Platform to use for a back-end to store Terraform’s state. In console, here’s the exact error.

![terraform-jwt-invalid.png](/wp-content/uploads/2018/08/terraform-jwt-invalid.png)

My first quick searches uncovered some Github issues that looked curiously familiar. [Invalid JWT Token when using Service Account JSON #3100](https://github.com/GoogleCloudPlatform/google-cloud-python/issues/3100) which was closed without any particular resolution. Upon further searching it didn’t help to much but I’d be curious as to what the resolution was. The second is [Creating GCP project in terraform #13109](https://github.com/hashicorp/terraform/issues/13109) which sounded much more on point compared to my issue. This appeared closer to my issue but it looked like I should probably just start from scratch, since this did work on one machine already but just didn’t work on this machine I shifted to. (Grumble grumble, what’d I miss).

## The Solution(s)?

In the end this is a message, if you work on multiple machines with multiple cloud accounts you might get the keys mixed up. In this particular case I reset my NIC (i.e. you can just reboot too, especially if on Windows it’s just easier to do that). Then everything just started working. In some cases however, the JSON with the gcloud/gcp keys needs to be regenerated as the old key was rolled or otherwise invalidated.
