---
title: 'Deploy a Framework Friday #2 with ASP.NET MVC 4'
date: 2012-07-20 04:01:57 -0700
last_modified_at: 2012-07-20 15:40:11 -0700
permalink: /2012/07/20/deploy-a-framework-friday-2-with-asp-net-mvc-4/
slug: deploy-a-framework-friday-2-with-asp-net-mvc-4
wp_id: 5991
original_url: https://compositecode.blog/2012/07/20/deploy-a-framework-friday-2-with-asp-net-mvc-4/
categories:
- .NET Bits
- Cloud Foundry
- Cloud Speak
- How-to
- Iron Foundry
- Platform (as a Service)
tags:
- asp.net
- asp.net mvc
- cloud foundry
- deploy
- deployment
- iron foundry
- mvc
- paas
- platform as a service
excerpt: First let’s build a standard ASP.NET MVC Application (yes, you can do the same without the MVC Project, but I STRONGLY recommend never creating a standard ASP.NET application again, EVER). This quick run through assumes you’ve already setup a Cloud Foundry enabled PaaS w/ your already installed Iron Foundry components for .NET development. Get an …
---

First let’s build a standard ASP.NET MVC Application (yes, you can do the same without the MVC Project, but I STRONGLY recommend never creating a standard ASP.NET application again, EVER). This quick run through assumes you’ve already setup a Cloud Foundry enabled PaaS w/ your already installed [Iron Foundry components for .NET development](http://ironfoundry.org/download). Get an Iron Foundry enabled account here, it’s [100% free](http://ironfoundry.org/signup), so no reason not to give it a go.

There are a few ways to do this. One, the click on the start page new project option.

![Click on the start page new project option...](/images/adronhall.smugmug.com/Software/Software-Development/Cloud-Foundry-Iron-Foundry/i-Qxmh56v/0/O/CloudFoundry-NET-Bits-03.jpg "Click on the start page new project option...")

*Click on the start page new project option…*

Two, the menu based selection option.

![Menu based new project option...](/images/adronhall.smugmug.com/Software/Software-Development/Cloud-Foundry-Iron-Foundry/i-9xH3Lp9/0/O/CloudFoundry-NET-Bits-02.jpg "Menu based new project option...")

*Menu based new project option…*

Three, the command button option.

![Click on the command button new project option](/images/adronhall.smugmug.com/Software/Software-Development/Cloud-Foundry-Iron-Foundry/i-Q527XfK/0/O/CloudFoundry-NET-Bits-01.jpg "Click on the command button new project option")

*Click on the command button new project option*

So pick your poison and then select the ASP.NET MVC 4 Project Template. On the next dialog, you’ll enter the information of where the project will go and choose the ASP.NET MVC 4 Web Application Project Template.

[![Selecting the ASP.NET MVC 4 Web Application (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Cloud-Foundry-Iron-Foundry/i-TJfsWmg/0/M/CloudFoundry-NET-Bits-04-M.jpg "Selecting the ASP.NET MVC 4 Web Application (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Cloud-Foundry-Iron-Foundry/24136014_3SDDwg#!i=1961706314&k=TJfsWmg&lb=1&s=O)

*Selecting the ASP.NET MVC 4 Web Application (Click for full size image)*

The next dialog select the Basic template, leave Razor selected, and I always leave the unit tests project there also. Once this is done we’re now ready to give our project a little taste of deployment.

Since we’re working in the land of GUIs and .NET, I’ll keep this to a completely GUI based deployment. However, don’t forget that the vmc-IronFoundry is available for pushing also. So don’t fear the CLI, but we’ll skip it for now (tip: It’s practically the same as the other deploys).

On the project in Visual Studio right click and select Push to Cloud Foundry.

[![Publish option on the context menu (click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Cloud-Foundry-Iron-Foundry/i-nHbR3rh/0/O/Cloud-Deployment-01.jpg "Publish option on the context menu (click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Cloud-Foundry-Iron-Foundry/24136014_3SDDwg#!i=1976874846&k=nHbR3rh&lb=1&s=O)

*Publish option on the context menu (click for full size image)*

A dialog will appear for the basic parameters needed for the deployment. Enter information that you need for your application and click ok.

[![Setting the parameters (click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Cloud-Foundry-Iron-Foundry/i-gZMWPtm/0/S/Cloud-Deployment-02-S.jpg "Setting the parameters (click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Cloud-Foundry-Iron-Foundry/24136014_3SDDwg#!i=1976863767&k=gZMWPtm&lb=1&s=O)

*Setting the parameters (click for full size image)*

Now when you navigate to your cloud in the Cloud Explorer UI (Start -> All Programs -> Iron Foundry -> Cloud Explorer) you’ll see the application running under that cloud environment.

As always, it is indeed THAT easy when using a Platform as a Service to deploy to!
