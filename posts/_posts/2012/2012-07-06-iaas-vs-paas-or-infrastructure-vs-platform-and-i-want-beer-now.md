---
title: IaaS vs. PaaS or Infrastructure vs. Platform and I Want Beer NOW!
date: 2012-07-06 08:06:51 -0700
last_modified_at: 2012-07-06 08:24:24 -0700
permalink: /2012/07/06/iaas-vs-paas-or-infrastructure-vs-platform-and-i-want-beer-now/
slug: iaas-vs-paas-or-infrastructure-vs-platform-and-i-want-beer-now
wp_id: 5937
original_url: https://compositecode.blog/2012/07/06/iaas-vs-paas-or-infrastructure-vs-platform-and-i-want-beer-now/
categories:
- .NET Bits
- Cloud Speak
- How-to
- Infrastructure
tags:
- asp
- asp.net
- asp.net mvc
- aspnet
- aspnet mvc
- cloud foundry
- deployment
- dotnet
- iaas
- infrastructure
- infrastructure as a service
- iron foundry
- mvc
- paas
- platform as a service
- tier 3
- tier 3 web fabric
- web fabric
excerpt: A friend and now coworker of mine, Richard Seroter (@rseroter & Blog) decided to do a comparo. I took the infrastructure based deployment, ala IaaS and he took the platform based deployment, ala PaaS. What we’ve done is taken a somewhat standard ASP.NET MVC with Entity Framework, a SQL Server Database, a UX & UI design …
---

A friend and now coworker of mine, [Richard Seroter](http://seroter.wordpress.com/about/) ([@rseroter](https://twitter.com/#!/rseroter) & [Blog](http://seroter.wordpress.com/)) decided to do a comparo. I took the infrastructure based deployment, ala IaaS and he took the [platform based deployment, ala PaaS](http://seroter.wordpress.com/2012/07/06/iaas-vs-paas-deploying-a-web-application). What we’ve done is taken a somewhat standard ASP.NET MVC with Entity Framework, a SQL Server Database, a UX & UI design and got it running locally. From there we then deployed the same application the two respective ways to deploy the web application to a live environment. He took the Tier 3 PaaS ([Iron Foundry](http://ironfoundry.org/) + [Cloud Foundry](http://www.cloudfoundry.org/) for the win) and I took the tried and true method of deploying via Windows 2008 Server instances via the Tier 3 Infrastructure.

Here are the steps I went through and for his steps check out this blog article on the PaaS deployment.

## Part #1 – Get Some Servers Setup

First things first, I need two instances. If you’re following along, you can basically use whatever instances or server you want. [AWS](http://aws.rackspace.com), [Rackspace](http://www.rackspace.com), or [Windows Azure](https://www.windowsazure.com/en-us/). Based on that there may be a few steps here or there you may need to alter, add or subtract from the process. One for the ASP.NET MVC Application and one for the SQL Server Database. The web app server doesn’t need a ton of resources, so I built it and scaled back RAM and cores to a single core.

[![ASP.NET MVC Web Server](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-c4r27tF/0/M/Screen-Shot-2012-07-05-at-M.png "ASP.NET MVC Web Server")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1946876783&k=c4r27tF&lb=1&s=O)

*ASP.NET MVC Web Server (Click for full size image)*

In the next step here I’ve selected additional software to be installed on the instance. I’ll need .NET 4.0 so I’ve added this as shown.

[![Selecting .NET 4.0 for Addition to the Instance](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-6tPFft5/0/S/Screen-Shot-2012-07-05-at-S.png "Selecting .NET 4.0 for Addition to the Instance ")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1946876768&k=6tPFft5&lb=1&s=O)

*Selecting .NET 4.0 for Addition to the Instance (Click for full size image)*

After setting up the web server I also setup a database server. For the database server I made sure to allocate some decent resource, setting up 2 cores and 8 GB RAM. I also added the SQL Server installation based on Tier 3’s software packages so it would install automatically when the image is created.

[![All My Instances Running](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-pSGMQHj/0/M/Screen-Shot-2012-07-05-at-M.jpg "All My Instances Running")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1946882135&k=pSGMQHj&lb=1&s=O)

*All My Instances Building & Running (Click for full size image)*

When I setup the SQL Server instance, I used a blue print feature that allows the SQL Server to be installed directly on the image. This of course saved me a lot of time. But it does add to the deployment time of the instance in the cloud.

## Part #2 – Setting up Windows Server 2008

The first thing we’ll need to do is log into these machines and configure them, standard infrastructure stuff. Open up the Server Manager (which launches automatically on instances) and verify that we have IIS installed on the web server.

**Database Server**

[![Server Manager](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-PFnXsxC/0/M/Screen-Shot-2012-07-05-at-M.jpg "Server Manager")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1947624230&k=PFnXsxC&lb=1&s=O)

*Server Manager (Click for full size image)*

Next log into the database server and verify that the SQL Server is up, running and create the initial database.

Thusly…

![Using SQL Server Management Studio checking that the SQL Server Exists](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-pbHnD7L/0/O/Screen-Shot-2012-07-05-at.jpg "Using SQL Server Management Studio checking that the SQL Server Exists")

*Using SQL Server Management Studio checking that the SQL Server Exists*

Once I had both of the servers up and running I got the application ready to deploy. First a little schema generation to use to deploy the database.

![Don't Use "Script Database as..." option, use the "Tasks" option...](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-jVnwMFQ/0/O/Generate-Scripts.jpg "Don't Use \"Script Database as...\" option, use the \"Tasks\" option...")

*Don’t Use “Script Database as…” option, use the “Tasks” option…*

Once the script is generated then transfer it and execute it against the database on the database server.

[![Execute the SQL Schema Create Script](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-Z4H5MQt/0/M/Generate-Database-04-M.jpg "Execute the SQL Schema Create Script")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1947700261&k=Z4H5MQt&lb=1&s=O)

*Execute the SQL Schema Create Script (Click image for full size)*

Always a good thing, even if all green lights are seen on the SQL execution, go in and make sure the tables are all there.

**Web Server**

[![Publish](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-Cp9DnQ3/0/S/Generate-Database-06-S.jpg "Publish")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1947738467&k=Cp9DnQ3&lb=1&s=O)

*Publish (Click Full Image)*

Publish Application (click for full size image)For the web server, as long as IIS is already installed, the setup is fairly easy. First snag the compiled bits that need deployed. We’ll do a direct drop onto the server and get it running.

To get the compiled bits, right click on the Visual Studio Project and select publish. Add a deployment scenario, which I did and set it up to just spit the bits out to a directory. There of course a multiple options at this point to use FTP, WebDav or whatever your choice is. I’m not a particular fan of any of those in particular, they’re all fairly easy.

[![Deployment Publication Options](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-HqXN7wk/0/S/Generate-Database-07-S.jpg "Deployment Publication Options")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1947778791&k=HqXN7wk&lb=1&s=O)

*Deployment Publication Options (Click for full size image)*

**Interuption!!!**

At this point I actually got hit with the “.NET 4.0 isn’t installed…” which it should have been. I opened up windows update and realized that it had not successfully executed nor had the .NET 4.0 install. This happens with all sorts of instances, regardless of provider, so make sure that the bits we need are installed. Also, with Windows, it’s a really good idea to get windows update turned on.

**Back to Deployment**

Now that we have the built bits just copy them onto the web application server into the inetpub wwwroot directory. Once you have that copied over you would be able to navigate to the IP of the machine this is setup on. At this time you may also want to setup a cname or a-record to point to the IP, so you can use a friendlier URI.

**Retrospective**

Now think about what has just gone on for a moment. We had to literally build out machines, add software and more. There were a lot of steps. This takes anywhere from 30 minutes to a few hours of actual work. In a larger business or an enterprise environment it could get extended out even further. Because of the extra complexity it could also end up broken, requiring extra troubleshooting and coding. There could even be a host of odd one off configuration issues with the hosting software itself.

Imagine you wanted to host an ASP.NET, PHP, Ruby on Rails and a Node.js App on the Server. That would be almost impossible. Consider how much extra configuration knowledge an ops person would need to troubleshoot each one of those frameworks. Just sit back and contemplate the complexities involved for a moment. All the complexity goes away with something like Cloud Foundry or Open Shift. With someone managing that system for you, such as us here at Tier 3 with our Web Fabric PaaS, AppFog, Cloud Foundry, or one of the other providers even more of the complexities just disappear.

**Time for Summary & Beer**

With all the steps and individual tasks needed to get something running in an IaaS Environment, go check out how slick [getting something up and running with a PaaS style environment](http://seroter.wordpress.com/2012/07/06/iaas-vs-paas-deploying-a-web-application). The juxtaposition between what Richard had to go through versus what I had to go through is pretty significant. Simply put, for the vast majority of all application development can be done against a PaaS Environment and likely should. Digging deeper into the infrastruture elements is rarely needed except in rare scaling circumstances, such as the volume that Facebook, LinkedIn or Netflix deal with. Even then, as has been stated by these companies, they have a PaaS of their own they often build software to. So why not have this ability where you build software?

One of my key metrics, and I’ll be elaborating on this metric more in the future, is when I get to head out of the office for the day, relax, have a beer, and think about what I’ll get to create next. I call this my “***Beer Enabler Measure***“. PaaS technologies make it much easier for me to get to the relaxing part of my day a lot faster than IaaS technologies, and both of these make sure that I’m not pulling an all nighter without a beer like traditional hosting environments often do.

In the end, sure, infrastructure can be important and can help in transitioning legacy applications into an easier to manage environment. Today though, if you’re doing web application dev of any type, it should be deployed against a PaaS Environment either private or public.
