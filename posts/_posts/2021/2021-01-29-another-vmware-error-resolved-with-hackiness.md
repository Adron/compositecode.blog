---
title: Another VMWare Error Resolved with Hackiness!
date: 2021-01-29 17:24:22 -0800
last_modified_at: 2021-02-01 09:49:44 -0800
permalink: /2021/01/29/another-vmware-error-resolved-with-hackiness/
slug: another-vmware-error-resolved-with-hackiness
wp_id: 57433
original_url: https://compositecode.blog/2021/01/29/another-vmware-error-resolved-with-hackiness/
categories:
- Unknown Code Ramblings
tags: []
excerpt: I use VMWare Fusion for almost all of my VMs these days. Especially for the VMs I use for streaming via Twitch when I code. I always like to have good, clean, out of the box loads for the operating systems I’m going to use. That way, whatever I’m doing is in the easiest state …
image: /wp-content/uploads/2021/02/CleanShot-2021-02-01-at-09.49.06.png
---

I use VMWare Fusion for almost all of my VMs these days. Especially for the VMs I use for streaming via Twitch when I code. I always like to have good, clean, out of the box loads for the operating systems I’m going to use. That way, whatever I’m doing is in the easiest state for anyone viewing and trying to follow along to replicate.

With this great power, however comes great hackiness in keeping these images in a good state. Recently I’d been coding away on a Go project and boom, I killed the VM, likely because I was also running multiple videos processing with Adobe products, including Photoshop, and I had HOI4 running in the background. That’s a strategy game if you’re curious. The machine was getting a bit overloaded, but that’s fairly standard practice for me. Anyway, the VM just killed over.

I tried restarting it and got this message.

Something something proprietary to the whatever and,

***“Cannot open the disk ‘xxxxx.vmdk’ or one of the snapshot disks it depends on.”***

I started searching and didn’t find anything useful. So I went about trying some random things. It’s really crazy too, because usually I’d just forget it and trash the image. But ya see, I had code I’d actually *NOT COMMITTED YET*!!! I kept trying, and finally came to a solution, oddly enough, that seemed to work as if nothing odd had happened at all!

I opened up the contents of the virtual machine file and deleted the \*.lck files. Not sure what they were anyway, and kind of just frustrated, but hey, it worked like a charm!

So if you run into this problem, you may want to just nuke the \*.lck files and try to kick start it that way.
