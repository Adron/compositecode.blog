---
title: Windows Server 2008 Core, A Quick Run Down
date: 2012-01-16 15:01:26 -0800
last_modified_at: 2012-01-16 15:01:26 -0800
permalink: /2012/01/16/windows-server-2008-core-a-quick-run-down/
slug: windows-server-2008-core-a-quick-run-down
wp_id: 4753
original_url: https://compositecode.blog/2012/01/16/windows-server-2008-core-a-quick-run-down/
categories:
- .NET Bits
- How-to
tags:
- server core
- windows
- windows 2008
- windows 2008 server core
excerpt: 'I needed a Windows Server installation with low overhead, clean installation, that providing hosting and other features. I decided I would check out the Windows Server 2008 Core R2 installation and see how it stacked up. This is a quick run down of what is available on Technet and what I used to setup the server core for usage. First there is the getting started guide. This write up provides a basic description of what the Windows Server 2008 Core R2 is, laying out the services and other characteristics of the installation. Specifically for the R2 version of the core installation these services are available: Active Directory Certificate Services Active Directory Domain Services Active Directory Lightweight Directory Services (AD LDS) DHCP Server DNS Server File Services (including File Server Resource Manager) Hyper-V Print and Document Services Streaming Media Services Web Server (including a subset of ASP.NET) One of the first things you’ll need to do is administer the server core installation. This document details the ways a server core instance can be administered such as: Locally and remotely using a command prompt. Remotely using Terminal Server. Remotely using Windows Remote Shell. Locally or remotely using Windows PowerShell. Remotely using an MMC snap-in. Remotely using Server Manager.'
---

I needed a Windows Server installation with low overhead, clean installation, that providing hosting and other features. I decided I would check out the Windows Server 2008 Core R2 installation and see how it stacked up. This is a quick run down of what is available on [Technet](http://technet.microsoft.com/) and what I used to setup the server core for usage.

First there is the [getting started guide](http://technet.microsoft.com/en-us/library/cc753802(WS.10).aspx). This write up provides a basic description of what the Windows Server 2008 Core R2 is, laying out the services and other characteristics of the installation. Specifically for the R2 version of the core installation these services are available:

- Active Directory Certificate Services
- Active Directory Domain Services
- Active Directory Lightweight Directory Services (AD LDS)
- DHCP Server
- DNS Server
- File Services (including File Server Resource Manager)
- Hyper-V
- Print and Document Services
- Streaming Media Services
- Web Server (including a subset of ASP.NET)

One of the first things you’ll need to do is [administer the server core installation](http://technet.microsoft.com/en-us/library/ee441258(WS.10).aspx). This document details the ways a server core instance can be administered such as:

- Locally and remotely using a command prompt.
- Remotely using Terminal Server.
- Remotely using Windows Remote Shell.
- Locally or remotely using Windows PowerShell.
- Remotely using an MMC snap-in.
- Remotely using Server Manager.

Known Issue: There is also an issue with core installations that is brought up. Not all management tasks can be performed by the MMC snap-in. An included script can be used to configure the things unavailable via MMC. The script is in \Windows\System32 folder. The following command provides configuration options for the unavailable MMC features:

```bash
cscript scregedit.wsf /?
```

Three more cool things before moving on:

1. [Cheat Sheets](http://www.microsoft.com/download/en/details.aspx?displaylang=en&id=24099) or as they’re labeled “[Job Aids for Server Core Installations of Windows Server 2008 and Windows Server 2008 R2](http://www.microsoft.com/download/en/details.aspx?displaylang=en&id=24099)“.
2. [Additional References](http://technet.microsoft.com/en-us/library/ee441251(WS.10).aspx) for Installing a number of features including; Backup, Bitlocker, File Server, and a host of other features.
3. [Installing Server Roles](http://technet.microsoft.com/en-us/library/ee441260(WS.10).aspx) onto the server core. This section provides step by step instructions to get various roles setup on the server including file sharing, etc.

Now that I’ve covered the standard things the server does and can do when configured, there are a number of things that need installed to really make the server useful. At least, for what I need it for. The first thing I need is to get .NET 4.0 running on the server. Onwards!

# .NET 4.0 Standalone Installation for Server Core

I’ll admit right up front installing this shows a gross neglect that Windows 2008 Server Core has. First navigate, on a completely different machine, and download the [.NET Standalone Installation for Server Core](http://www.microsoft.com/download/en/details.aspx?id=22833). Now, this is one of those situations where it appears Microsoft just completely misses how the Internet might work or should work. Why is .NET 4.0 not provided via FTP or some way that I could actually download it from the actual server that needs it? No idea, but you can’t. Once you do have it downloaded on a completely different machine (in my case, I used trusty OS-X) you can then find a way to get it onto the machine. I used a FAT formatted (yeah, in this situation I’ve had to return back a couple decades to FAT technology to get a 2011 piece of technology to work) USB Stick. Once I got the installation file on the USB Stick I just mounted that up and copied the file over the machine and installed it.

**Instructions per the Download Page**

1. Important: Make sure that your computer has the latest Windows service pack and critical updates. To find security updates, visit Windows Update.  Including the following requirements (The image (Fig 1) shows what items I included – the extra items I included are unrelated to this blog entry):
   1. Turn on WoW64:

      ```bash
      Start /w ocsetup ServerCore-WOW64
      ```
   2. Turn on .NET 2.0 layer:

      ```bash
      Start /w ocsetup NetFx2-ServerCore
      ```
   3. Turn on .NET 2.0 layer for WoW64:

      ```bash
      Start /w ocsetup NetFx2-ServerCore-WOW64
      ```

      [![Installing Multiple Services/Roles for the Server Core](/images/adronhall.smugmug.com/Software/Software-Development/The-CloudFoundry-Story/i-gnHcF5j/0/S/Screen-Shot-2012-01-10-at-S.png "Installing Multiple Services/Roles for the Server Core")](http://adronhall.smugmug.com/Software/Software-Development/The-CloudFoundry-Story/20770354_nfqhGc#!i=1667688247&k=gnHcF5j&lb=1&s=O)

      *Installing Multiple Services/Roles for the Server Core*
2. On this page, locate the Download button and then click it to start the download.
3. To save the download to your computer so that you can install it later, click Save.
4. To cancel the download, click Cancel.
5. After installing .NET Framework 4 on Windows 2008 R2 SP1 Server Core, it is highly recommended you install critical .NET Framework 4 updates available on Windows Update.

[![Installing .NET 4.0 for Server Core](/images/adronhall.smugmug.com/Software/Software-Development/The-CloudFoundry-Story/i-z2dpCwR/0/S/Screen-Shot-2012-01-10-at-S.png "Installing .NET 4.0 for Server Core")](http://adronhall.smugmug.com/Software/Software-Development/The-CloudFoundry-Story/20770354_nfqhGc#!i=1667683367&k=z2dpCwR&lb=1&s=O)

*Installing .NET 4.0 for Server Core*

# PowerShell, Now We’re Getting Somewhere!

Alright, the server is starting to be useful now. We have various services and prospectively other networking capabilities, all depending on what we would have wanted to install during the first section  of material. We also have .NET 4.0, so we can run some honest to goodness useful .NET Applications, such as web apps, and more.

Now that we’re all wrapped up, it is always a good idea to give a Windows Server one more firm kick before we put it into production. To shutdown, restart or otherwise give the server that kick, just type shutdown and you’ll find all the switches available. The most common one I use is to just shutdown right away (relatively, it still takes its time shutting down).

```bash
shutdown -s
```
