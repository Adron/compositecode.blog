---
title: Gritty Technical Info on Windows Azure Web Roles
date: 2011-01-14 05:44:21 -0800
last_modified_at: 2011-01-17 15:28:05 -0800
permalink: /2011/01/14/gritty-technical-info-on-windows-azure-web-roles/
slug: gritty-technical-info-on-windows-azure-web-roles
wp_id: 2093
original_url: https://compositecode.blog/2011/01/14/gritty-technical-info-on-windows-azure-web-roles/
categories:
- Azure
- How-to
tags:
- cloud
- cloud computing
- microsoft
- web role
- web services
- windows azure
- worker role
excerpt: This is a follow up to the previous blog entry I wrote pertaining to Windows Azure Roles. I wanted to cover the bases on the various technical aspects of creating a Windows Azure Web Role & Worker Role in Visual Studio 2010. Without interruption let’s just dive right in. Start Visual Studio 2010 and initiate a new project. File, new, and then project will open the new project dialog…
---

This is a follow up to the previous blog entry I wrote pertaining to Windows Azure Roles.  I wanted to cover the bases on the various technical aspects of creating a Windows Azure Web Role & Worker Role in Visual Studio 2010.  Without interruption let’s just dive right in.  Start Visual Studio 2010 and initiate a new project. File, new, and then project will open the new project dialog.

[![Windows Azure Project](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/Windows-Azure-Web-Role-01/1155222934_zPr9o-S.png "Windows Azure Project")](http://adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/15431091_6D8HE#1155222934_zPr9o-O-LB)

*Windows Azure Project*

Select a cloud template type and name your project.  Click OK and the New Windows Azure Project Dialog will appear to select the role types you can choose from.

[![Windows Azure Project Templates](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/Windows-Azure-Web-Role-02/1155222825_oBaUd-S.png "Windows Azure Project Templates")](http://adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/15431091_6D8HE#1155222825_oBaUd-O-LB)

*Windows Azure Project Templates*

Select an ASP.NET MVC Web Application, name it appropriately, and then click OK.  When prompted for a test project select yes and click OK.  When the solution is finished generating from the chosen templates there will be a SampleWebRole ASP.NET MVC Web Application, the test project titled SampleWebRole.Tests, and a Windows Azure Project titled Windows Azure Web Role Sample.

[![Solution](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/Windows-Azure-Web-Role-03/1156514682_YVsjF-O.png "Solution")](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/Windows-Azure-Web-Role-03/1156514682_YVsjF-O.png)

*Solution*

After that run the application to assure that the Development Fabric & other parts of the web application startup appropriately.

With the web application still running, click on the Development Fabric Icon in the status bar of Windows 7 and select the Show Computer Emulator UI.

[![Show Compute Emulator UI](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/Windows-Azure-Web-Role-05/1155222834_gRbar-O-1.png "Show Compute Emulator UI")](http://adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/15431091_6D8HE#1155222834_gRbar-A-LB)

*Show Compute Emulator UI*

The Windows Azure Compute Emulator will display. Click on the Service Deployments tree until you can see each individual instance (the little green lights should be showing). Figure 4.6 shows this tree opened with one of the instances selected to view the status trace.

[![Windows Azure Compute Emulator](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/Windows-Azure-Web-Role-06/1155222837_H6SFz-S.png "Windows Azure Compute Emulator")](http://adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/15431091_6D8HE#1155222837_H6SFz-O-LB)

*Windows Azure Compute Emulator*

Select Shift + F5 to stop the web application from running.  In the Solution Explorer right click on the SampleWebRole under the Windows Azure Web Role Sample Project and select Properties.

[![Properties for SampleWebRole](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/Windows-Azure-Web-Role-07/1155222836_jukX3-S.png "Properties for SampleWebRole")](http://adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/15431091_6D8HE#1155222836_jukX3-O-LB)

*Properties for SampleWebRole*

Under the configuration tab of the SampleWebRole Properties set the Instance Count to 6 and the VM Size to Extra Large.

[![Windows Azure Instance Properties](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/Windows-Azure-Web-Role-08/1155222867_Gvbwh-S.png "Windows Azure Instance Properties")](http://adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/15431091_6D8HE#1155222867_Gvbwh-O-LB)

*Windows Azure Instance Properties*

Now select F5 to run the web application again in the Windows Azure Development Fabric.  The Windows Azure Compute Emulator (if it is closed right click back on the status icon to launch it again) will now display each of the 6 instances launching under the SampleWebRole.

[![Windows Azure Compute Emulator](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/Windows-Azure-Web-Role-09/1155222887_PxcVx-S.png "Windows Azure Compute Emulator")](http://adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/15431091_6D8HE#1155222887_PxcVx-O-LB)

*Windows Azure Compute Emulator*

Click on one of the green lights to show that specific instance status in the primary window area.

[![Windows Azure Compute Instance 2](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/Windows-Azure-Web-Role-10/1155222892_F4iKX-S.png "Windows Azure Compute Instance 2")](http://adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/15431091_6D8HE#1155222892_F4iKX-O-LB)

*Windows Azure Compute Instance 2*

When you select the specific instance the status of that instance is displayed. The instance that is displayed in figure 4.10 has a number of events being recorded with the diagnostics, MonAgentHost, and the runtime. This particular instance had gone through a rough start. During the lifecycle of a Windows Azure Web, Worker, or CGI Role there are a number of events similar to these that can occur.

Read through the first few lines. These lines show that another agent was running, which could be a number of things that conflicted with this web role starting up cleanly. Eventually the web role was able to startup appropriately as shown in the runtime lines stating that the OnStart() is called and then complete, with the Run() executing next.

Reading further through the diagnostics the web role eventually requests a shutdown and then prepares for that shutdown pending the exit of the parent process 6924.

These types of events are common place when reviewing the actions a web role will go through; generally, don’t get too alarmed by any particular set of messages. As long as the role has green lights on the instances, things are going swimmingly. When the lights change to purple or red then it is important to really start paying attention to the diagnostics.

**Windows Azure Worker Roles**

In the next blog entry ([Part II](2011/01/17/gritty-technical-info-on-windows-azure-worker-roles/)) I want to show is how to add a worker role and how to analyze the activities within the role. The worker role is somewhat different than a web role. The primary difference between a web role and a worker role is that one is built around providing compute work, while one is built around providing web compute. Think of the worker role as something similar to a Windows Service, which runs ongoing to execute jobs & other processes, often backend type processes. A web role is what is built to host Silverlight and web applications such as ASP.NET or ASP.NET MVC.

[Part II published](2011/01/17/gritty-technical-info-on-windows-azure-worker-roles/) on Monday the 17th.

[![Shout it](http://dotnetshoutout.com/image.axd?url=http%3A%2F%2Fcompositecode.com%2F2011%2F01%2F14%2Fgritty-technical-info-on-windows-azure-web-roles%2F)](http://dotnetshoutout.com/Gritty-Technical-Info-on-Windows-Azure-Web-Roles-Composite-Code)
