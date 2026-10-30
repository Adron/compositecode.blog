---
title: Windows 10’s Path of Destruction and Garbage Support for Linux from Dell
date: 2019-02-04 14:18:30 -0800
last_modified_at: 2019-02-04 15:07:50 -0800
permalink: /2019/02/04/windows-10s-path-of-destruction-and-garbage-support-for-linux-from-dell/
slug: windows-10s-path-of-destruction-and-garbage-support-for-linux-from-dell
wp_id: 15302
original_url: https://compositecode.blog/2019/02/04/windows-10s-path-of-destruction-and-garbage-support-for-linux-from-dell/
categories:
- Containers
- Linux
tags: []
excerpt: At this point, I’d say do not buy a Dell XPS 15 unless you are only going to use Windows 10 apps and such on the machine. Linux runs like garbage on the machine. The generic drivers that allow one to sort of load Linux onto the machine work mediocre at best, with lot’s of …
---

At this point, I’d say [**do not** buy a Dell XPS 15](/2018/12/30/got-a-new-laptop-heres-the-review/) unless you are only going to use Windows 10 apps and such on the machine. Linux runs like garbage on the machine. The generic drivers that allow one to sort of load Linux onto the machine work mediocre at best, with lot’s of crashes, kernel panics, and related wrecks within seconds and minutes (if you get that far) after starting the machine with Linux. So that the situation there.

## Docker, Hyper-V, and VirtualBox Conflict

As I’ve used Windows 10 I keep hitting hard roadblocks on getting things done. After years of MacOS and Linux usage it’s kind of an ongoing, slow motion, insulting train wreck how monopolistic a lot of their applications are still built to run. For example, the latest application that I’ve tried to use that is effectively disabled is Virtual Box. Upon further research I realized I can’t used Virtual Box if I have Hyper-V installed. But that means if I want to use the latest and greatest Docker software then I either have to enable Hyper-V and use Docker or disable Docker and Hyper-V and use Virtual Box. Which means I could go back a version or two of this and that and use Docker-machine with Virtual Box, but, seriously, that’s ridiculous.

The way, from what I understand so far, is that they’ve built the operation of Hyper-V to work on Windows 10 in a way that it effectively prevents Virtual Box, and I suppose VMWare, from actually operating. So one has to go and disable Hyper-V in order to be able to run Virtual Box.

## Enabling / Disabling VirtualBox and Hyper-V

Ok, here’s one way to do this with Powershell. Open up Powershell with the “Run As Administrator” option. You’ll have to do that by clicking the start menu (or whatever it’s called these days) and typing “power” which brings up the Powershell application icon. Right click on it and select “Run as Administrator”.

```
# Remember, all of these commands need executed via Powershell that is started/opened with "Run As Administrator".

# Disabling Hyper-V

Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Hypervisor

# Enabling Hyper-V

Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All

# You may also want DSIM enabled with all this, here's that detail.

DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V
```

[View the gist on GitHub](https://gist.github.com/Adron/85f9b7530c330d4e68d24cd062780c56/910a0191e089f6305b6ab5ec3035c886f78f61cf/disable-hyper-v.ps1)

![dism_upd](/wp-content/uploads/2019/02/dism_upd.png)

![hyper-v](/wp-content/uploads/2019/02/hyper-v-1.png)Here’s the dialog where one can disable Hyper-V to run VirtualBox too. One this is run, or disabled, Windows 10 will likely want you to restart your computer. You’ll actually need to do this too, because VirtualBox will still die out without a clean OS launch for the base underlying operating system.

Once the restart is complete however, VirtualBox should start up and run virtual machines just fine. Emphasis as usual for Windows on the keyword of *should*.

## Virtual Machine SITREP Resolved Poorly

At this point I’m moderately ok with this solution. It just means that I need to re-create all of my images in Hyper-V and nuke VirtualBox though. I’m really indifferent on which one I need to use, but would have liked to have RTFM’ed the docs before so I had realized upgrading to Windows 10 and using Hyper-V for Docker would kill off my VirtualBox images that I’ve been using for months. Oh well, onward!

The other thing that I find horrifying about this though, is as I’ve learned why and how Hyper-V disabled VirtualBox from running side by side, it seems like 90’s era monopolistic Microsoft building something in a way that disables competition. Ok, so I know it isn’t really because of that, but it’s close enough that it just seem dirty, nasty, and all around kind of disingenuous on Microsoft’s part. Especially considering they neglected Hyper-V for so many years and of course now are all like, “*hey, Hyper-V is the way the future, nobody uses it outside of the Windows camp, but it’s the way of the future so bow down and use it Windows users!!*” But whatever, I’m at least back in business to get some things done and get some development images put together in Hyper-V.

## Hyper-V plus Docker for Windows 10

At this point, since Linux has such poor support on the Dell XPS 15 I’m just sticking with Windows 10 and going the Hyper-V + Docker + Virtual Machines path for what I’m working on. More on this soon, and I’ll be mentioning various things on Twitch soon too. When I get back around to getting the Linux + XPS 15 situation sorted out and tried out again I’ll be sure to blog that too!
