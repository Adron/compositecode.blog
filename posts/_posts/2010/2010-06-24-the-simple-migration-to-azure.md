---
title: The Simple Migration to Azure
date: 2010-06-24 16:13:17 -0700
last_modified_at: 2010-06-24 16:24:19 -0700
permalink: /2010/06/24/the-simple-migration-to-azure/
slug: the-simple-migration-to-azure
wp_id: 70
original_url: https://compositecode.blog/2010/06/24/the-simple-migration-to-azure/
categories:
- Azure
- Cloud Speak
- How-to
tags:
- asp.net
- azure
- cloud
- visual studio 2010
- windows
- windows azure
excerpt: This is a quick entry just to show how to migrate an existing ASP.NET (or ASP.NET MVC) Web Application to Windows Azure. Make sure you have the Azure Tools SDK installed before stepping through this, otherwise you’ll get an empty project folder and end up with web page in Visual Studio. With your existing solution/project open in Visual Studio 2010 right click on the solution and add a new project. You will see the dialog as shown in the image below (click for large full size image, same goes for subsequent images)
---

This is a quick entry just to show how to migrate an existing ASP.NET (or ASP.NET MVC) Web Application to Windows [Azure](http://www.microsoft.com/windowsazure).  Make sure you have the Azure Tools SDK installed before stepping through this, otherwise you’ll get an empty project folder and end up with web page in Visual Studio.  With your existing solution/project open in Visual Studio 2010 right click on the solution and add a new project.  You will see the dialog as shown in the image below (click for large full size image, same goes for subsequent images)

[![](/images/adronhall.smugmug.com/Software/Software-Development/Migrating-to-Azure/Azure-01/911217962_rveGk-M.png)](/images/adronhall.smugmug.com/Software/Software-Development/Migrating-to-Azure/Azure-01/911217962_rveGk-M.png)

Name your project and then click on OK.  The following secondary dialog will appear.  Since you want to use one of your existing web applications leave the “Cloud Service Solution:” section empty and click OK.

[![](/images/adronhall.smugmug.com/Software/Software-Development/Migrating-to-Azure/Azure-02/911217969_aW7zB-M.png)](/images/adronhall.smugmug.com/Software/Software-Development/Migrating-to-Azure/Azure-02/911217969_aW7zB-M.png)

You will then see the following project appear in your Visual Studio 2010 Solution.

[![](/images/adronhall.smugmug.com/Software/Software-Development/Migrating-to-Azure/Azure-03/911217970_NQ9Wv-M.png)](/images/adronhall.smugmug.com/Software/Software-Development/Migrating-to-Azure/Azure-03/911217970_NQ9Wv-M.png)

Right click on the Roles Folder in the new project as shown below.  You will get the following options as shown;  “New Web Role Project…”, “Web Role Project in solution…”, and “New Worker Role Project…” and select the “Web Role Project in solution…”.

[![](/images/adronhall.smugmug.com/Software/Software-Development/Migrating-to-Azure/Azure-04/911218028_kmvH6-M.png)](/images/adronhall.smugmug.com/Software/Software-Development/Migrating-to-Azure/Azure-04/911218028_kmvH6-M.png)

The following dialog will pop up with any available web applications, in my case there is a single ASP.NET Web Application that is listed.  Click OK and you now of a Windows Azure Cloud Deployable Application.  Complete a build and right click on the Cloud Deployment Project and click Publish for the next steps into the cloud.  But I’ll leave that particular exercise’s steps for another entry.

[![](/images/adronhall.smugmug.com/Software/Software-Development/Migrating-to-Azure/Azure-05/911218026_CfCtZ-M.png)](/images/adronhall.smugmug.com/Software/Software-Development/Migrating-to-Azure/Azure-05/911218026_CfCtZ-M.png)

[![Shout it](http://dotnetshoutout.com/image.axd?url=http%3A%2F%2Fcompositecode.com%2F2010%2F06%2F24%2Fthe-simple-migration-to-azure%2F)](http://dotnetshoutout.com/The-Simple-Migration-to-Azure-Loosely-Coupled-Human-Code-Factory)
