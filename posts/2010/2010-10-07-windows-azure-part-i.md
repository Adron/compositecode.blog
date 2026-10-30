---
title: What You Need and Want With Windows Azure Part I
date: 2010-10-07 05:15:33 -0700
last_modified_at: 2010-10-07 00:16:52 -0700
permalink: /2010/10/07/windows-azure-part-i/
slug: windows-azure-part-i
wp_id: 1423
original_url: https://compositecode.blog/2010/10/07/windows-azure-part-i/
categories:
- Azure
- How-to
tags:
- appfabric
- azure
- cloud computing
- microsoft
- msdn
- windows azure
excerpt: 'The first thing needed is a Windows Azure Account, which is simply a Live ID. The easiest way to setup one of these is to navigate to http://www.live.com and click on the Sign Up button. If you have an existing account that you use to login it should display on this page also. Windows Live ID Sign Up After creating or logging in with an existing account let’s take a look at the various web properties Microsoft has dedicated to Windows Azure. This site is the quintessential Microsoft Windows Azure Marketing Site, geared toward decision makers in management and CTO or CIOs. There are links to many other web properties that Microsoft has setup from this page. It’s a great starting point to find management and executive selling points such as white papers, case studies, co-marketing, and more. Microsoft Windows Azure The MSDN Site is the central developer resource Microsoft provides online. The site recently underwent a massive redesign of almost every element. MSDN Site MSDN Developers site is a requirement to bookmark. This has the shortest navigation to all the sites and services you’ll need for Windows Azure Development. There is even a login link to the Site #4 below. In addition there are several key sections of this site; blogs, news, and more information. MSDN Windows Azure Site The Windows Azure Portal site is where we’ll be setting up the roles, storage, and other cloud computing mechanisms that we’ll be writing code against. Now that each of these sites is reviewed, let’s move forward. The Windows Azure Portal Site will prompt you to sign up for a cloud services plan. Signing up for a Windows Azure Service Click on next and you will be brought to a page related to which plans you can choose from. Depending on what specific focus you have for either development, dedicated services hosting, or otherwise you can choose from the multiple plans they have. I won’t go into them here, as Microsoft regularly changes the plans for specials and based on market demand and current costs. Signing up for a specific plan. After choosing which plan you will be redirected to the billing site, https://mocp.microsoftonline.com/ , to setup a line of credit, confirm the type of Windows Azure Subscription you want to start with, and other information as needed. Once this is setup, you most likely won’t need to look at this site again except to verify billing information, change billing information, or confirm cloud usage. Microsoft Billing Now that there is an account available, we’ll need to install the latest development tools for coding solutions for the cloud. This first example will be using Visual Studio 2010 with the Windows Azure SDK. If you don’t have Visual Studio 2010 installed yet, go ahead and install that. Open up Visual Studio 2010 next. We will use Visual Studio 2010 project templates to find out the latest Windows Azure SDK and download it. To download the latest Windows Azure SDK navigate to the MSDN Windows Azure Developers Site and click on the Downloads option at the top of the site. MSDN Windows Azure Download Section Once you have downloaded and installed the latest Windows Azure SDK we will download and install the Windows Azure AppFabric also. Scroll down midway on the MSDN Windows Azure Download page and the Windows Azure AppFabric SDK should be available for download. On the Windows Azure AppFabric SDK download page there should be a *.chm help file, two different AppFabric SDK Examples files one for VB and one for C#, and two installation packages one for 64-bit and one for 32-bit. Download and install the one for your particular system. I’d suggest downloading the samples also and giving each a good review. In What You Need and Want With Windows Azure Part II I will cover how to setup the Windows Azure Microsoft Management Console. So stay tuned, that coming tomorrow.'
---

The first thing needed is a Windows Azure Account, which is simply a [Live ID](http://www.live.com).  The easiest way to setup one of these is to navigate to <http://www.live.com> and click on the Sign Up button.  If you have an existing account that you use to login it should display on this page also.

[![Windows Live ID Sign Up](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-001-suggested-cropping/1037109894_pGGMj-S.png "Windows Live ID Sign Up")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-001-suggested-cropping/1037109894_pGGMj-O.png)

*Windows Live ID Sign Up*

After creating or logging in with an existing account let’s take a look at the various web properties Microsoft has dedicated to Windows Azure.

This site is the quintessential [Microsoft Windows Azure Marketing Site](http://www.microsoft.com/windowsazure/), geared toward decision makers in management and CTO or CIOs.  There are links to many other web properties that Microsoft has setup from this page.  It’s a great starting point to find management and executive selling points such as white papers, case studies, co-marketing, and more.

[![Microsoft Windows Azure](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-005-suggested-cropping/1037109899_8wc4F-M.png "Microsoft Windows Azure")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-005-suggested-cropping/1037109899_8wc4F-O.png)

*Microsoft Windows Azure*

The [MSDN Site](http://msdn.microsoft.com/) is the central developer resource Microsoft provides online.  The site recently underwent a massive redesign of almost every element.

[![MSDN Site](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-002-suggested-cropping/1037109827_iuBeT-M.png "MSDN Site")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-002-suggested-cropping/1037109827_iuBeT-O.png)

*MSDN Site*

[MSDN Developers site](http://msdn.microsoft.com/en-us/windowsazure/) is a requirement to bookmark.  This has the shortest navigation to all the sites and services you’ll need for Windows Azure Development.  There is even a login link to the Site #4 below.  In addition there are several key sections of this site; blogs, news, and more information.

[![MSDN Windows Azure Site](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-003-suggested-cropping/1037109853_TXhHV-M.png "MSDN Windows Azure Site")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-003-suggested-cropping/1037109853_TXhHV-O.png)

*MSDN Windows Azure Site*

The [Windows Azure Portal site](https://windows.azure.com/) is where we’ll be setting up the roles, storage, and other cloud computing mechanisms that we’ll be writing code against.  Now that each of these sites is reviewed, let’s move forward.

The [Windows Azure Portal Site](https://windows.azure.com/) will prompt you to sign up for a cloud services plan.

[![Signing up for a Windows Azure Service](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-004-suggested-cropping/1037109953_ELLc9-S.png "Signing up for a Windows Azure Service")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-004-suggested-cropping/1037109953_ELLc9-O.png)

*Signing up for a Windows Azure Service*

Click on next and you will be brought to a page related to which plans you can choose from.  Depending on what specific focus you have for either development, dedicated services hosting, or otherwise you can choose from the multiple plans they have.  I won’t go into them here, as Microsoft regularly changes the plans for specials and based on market demand and current costs.

[![Signing up for a specific plan.](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-005-suggested-cropping/1037109899_8wc4F-M.png "Signing up for a specific plan.")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-005-suggested-cropping/1037109899_8wc4F-O.png)

*Signing up for a specific plan.*

After choosing which plan you will be redirected to the billing site, <https://mocp.microsoftonline.com/>, to setup a line of credit, confirm the type of Windows Azure Subscription you want to start with, and other information as needed.  Once this is setup, you most likely won’t need to look at this site again except to verify billing information, change billing information, or confirm cloud usage.

[![Microsoft Billing](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-006-suggested-cropping/1037109893_XrDE2-S.png "Microsoft Billing")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-006-suggested-cropping/1037109893_XrDE2-O.png)

*Microsoft Billing*

Now that there is an account available, we’ll need to install the latest development tools for coding solutions for the cloud.  This first example will be using Visual Studio 2010 with the Windows Azure SDK.  If you don’t have Visual Studio 2010 installed yet, go ahead and install that.  Open up Visual Studio 2010 next.  We will use Visual Studio 2010 project templates to find out the latest Windows Azure SDK and download it.
To download the latest Windows Azure SDK navigate to the [MSDN Windows Azure Developers Site](http://msdn.microsoft.com/en-us/windowsazure/) and click on the Downloads option at the top of the site.

[![MSDN Windows Azure Download Section](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-003-suggested-cropping/1037109853_TXhHV-M.png "MSDN Windows Azure Download Section")](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Getting-Started/IMAGE-003-suggested-cropping/1037109853_TXhHV-O.png)

*MSDN Windows Azure Download Section*

Once you have downloaded and installed the latest Windows Azure SDK we will download and install the Windows Azure AppFabric also.  Scroll down midway on the MSDN Windows Azure Download page and the Windows Azure AppFabric SDK should be available for download.  On the Windows Azure AppFabric SDK download page there should be a \*.chm help file, two different AppFabric SDK Examples files one for VB and one for C#, and two installation packages one for 64-bit and one for 32-bit.  Download and install the one for your particular system.  I’d suggest downloading the samples also and giving each a good review.

In What You Need and Want With Windows Azure Part II I will cover how to setup the Windows Azure Microsoft Management Console.  So stay tuned, that is coming tomorrow.
