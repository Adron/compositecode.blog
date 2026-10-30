---
title: A Short Introduction to Windows Azure AppFabric
date: 2011-02-17 05:42:47 -0800
last_modified_at: 2011-02-16 20:50:06 -0800
permalink: /2011/02/17/a-short-introduction-to-windows-azure-appfabric/
slug: a-short-introduction-to-windows-azure-appfabric
wp_id: 2325
original_url: https://compositecode.blog/2011/02/17/a-short-introduction-to-windows-azure-appfabric/
categories:
- Unknown Code Ramblings
tags:
- appfabric
- cloud computing
- microsoft
- paas
- windows azure
- windows azure appfabric
excerpt: Windows Azure AppFabric is arguably the main feature set that truly sets Windows Azure apart from any cloud services on the market today. The AppFabric allows cloud users to hookup on-premises services to their cloud services, to secure cloud & on-premises services with new or existing security measures, cache Internet or other content, and on top of all that build out and enable composite application integration. At the same time that Windows Azure AppFabric is one of the main features that sets Windows Azure apart from the competition, it is often one of the most misunderstood or unknown part of the entire offering. In this chapter I’ll cover the main parts of the AppFabric including the service bus, access control, caching, integration, and patterns for integrating composite applications. Home of Windows Azure AppFabric The first thing to do in order to begin building with the Windows Azure AppFabric is to download the SDK, check out the various Windows Azure AppFabric Sites, and familiarize yourself with what it is and how it works into the Windows Azure Platform.
---

Windows Azure AppFabric is arguably the main feature set that truly sets Windows Azure apart from any cloud services on the market today. The AppFabric allows cloud users to hookup on-premises services to their cloud services, to secure cloud & on-premises services with new or existing security frameworks (identity based, active directory, or otherwise), cache Internet or other content, and on top of all that build out and enable composite application integration.

At the same time that Windows Azure AppFabric is one of the main features that sets Windows Azure apart from the competition, it is often one of the most misunderstood or unknown parts of the entire offering. In this chapter I’ll cover the main parts of the AppFabric including the service bus, access control, caching, integration, and patterns for integrating composite applications.

**Home of Windows Azure AppFabric**

The first thing to do in order to begin building with the Windows Azure AppFabric is to download the SDK, check out the various Windows Azure AppFabric Sites and familiarize yourself with what it is and how it works into the Windows Azure Platform.

The main web presence is located at <http://www.microsoft.com/windowsazure/AppFabric/Overview/default.aspx>

[![Windows Azure AppFabric Site](/images/adronhall.smugmug.com/Software/Reviews/Windows-Azure-AppFabric/08fig01/1189953613_dH3oo-L.png "Windows Azure AppFabric Site")](http://www.microsoft.com/windowsazure/AppFabric/Overview/default.aspx)

*Windows Azure AppFabric Site*

On the main site you will primarily find a marketing presence, but with links to many locations with useful architectural, development, and related technical information.  On the left hand side of the site there is a navigation bar that provides access to specific information describing the service bus, access control, and other features of the Windows Azure AppFabric.

The next major web presence that is extremely useful for Windows Azure AppFabric is the Windows Azure AppFabric Team Blob. It is located at <http://blogs.msdn.com/b/windowsazureappfabric/>. This site is regularly updated with development tips, patterns and practices, related MVP and Microsoft Enangelist links, updates on the SDK, CTPs, and other technical information.

The last major link that should be reviewed and checked often in relation to Windows Azure AppFabric Development is the Windows Azure AppFabric Developers’ Center located at <http://msdn.microsoft.com/en-us/windowsazure/appfabric.aspx>. Next to the blog, which often links to this page, this site is probably the most useful in relation to AppFabric Development. There are headlines, quick starts, and other documentation related to AppFabric Development with Ruby, Java, and other languages and technology stacks.

I don’t want to provide a direct link to the SDK. The reason is that Microsoft’s method for tracking and providing download links to SDKs, CTPs, and other related software often changes. The best way to find the current download location for the Windows Azure AppFabric SDK is to use a search engine and enter the keywords “[Windows Azure AppFabric SDK](http://www.google.com/search?aq=f&sourceid=chrome&ie=UTF-8&q=Windows+Azure+AppFabric+SDK)” (click the link as I setup the search for you). The first links provided will get you to the current location to download the SDK & other related files discussed below.

As of the current v1.0 release of the SDK there are several downloads that are matched along with it for documentation and samples. There is also a specific WindowsAzureAppFabricSDK-x64.msi and a WindowsAzureAppFabricSDK-x86.msi.  Each of these are different and specific to the 32 or 64 bit architecture. Along with the SDK there is a v1.0 C# and Visual Basic file available for download that includes multiple examples of how Windows Azure AppFabric works. The last file that is included with the Windows Azure AppFabric download page is the WindowsAzureAppFabric.chm. This is simply a documentation file for the Windows Azure AppFabric SDK.

**What Exactly is Windows Azure AppFabric?**

Windows Azure AppFabric can be seen as the all encompassing fabric that interconnects on-premises solutions to Windows Azure solutions, and even Windows Azure solution to other solutions within the cloud. Windows Azure AppFabric is broken down into two main feature offerings simply called the service bus and access control. Some new features are coming online in the very near future; the main one I’ll discuss is the Windows Azure AppFabric Caching.

[![Windows Azure AppFabric](/images/adronhall.smugmug.com/Software/Reviews/Windows-Azure-AppFabric/08fig02/1189953593_yosR7-S-1.jpg "Windows Azure AppFabric")](http://adronhall.smugmug.com/Software/Reviews/Windows-Azure-AppFabric/15869341_YnvEJ#1189953593_yosR7-O-LB)

*Windows Azure AppFabric*

That’s all I have right now, and would love any feedback on things I should mention, discuss or otherwise add to this write up.  I’m thinking of using it as an intro to AppFabric in some of the pending presentations I have coming up.  So please throw in some feedback on what else you might like.  -thanks
