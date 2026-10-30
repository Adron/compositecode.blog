---
title: 'Cloud Throw Down:  Part 2 – Deployments and Instance Options'
date: 2010-11-03 00:01:12 -0700
last_modified_at: 2010-11-09 10:54:15 -0800
permalink: /2010/11/03/cloudthrowdown-part2/
slug: cloudthrowdown-part2
wp_id: 1533
original_url: https://compositecode.blog/2010/11/03/cloudthrowdown-part2/
categories:
- AWS
- Azure
- Tech Throw-down
tags:
- amazon web services
- aws
- azure
- cloud
- cloud computing
- ec2
- virtual
- web role
- windows azure
excerpt: Ok, in this edition the fight gets graphic! Let’s jump right into the bout. I’ve also been thinking about adding Rackspace or another cloud provider, so if you want me to add a comparison point, please let me know and I’ll get them added. Deploying .NET Web Application Code into AWS and Windows Azure is done in some distinctly different ways. There are two ways to look at this measurement; One is with a configured Web Role or VM Role in Windows Azure and already configured EC2 Instance for AWS or… A Web Role or VM Role as is and an EC2 Instance as is. The first scenario one can deploy .NET code directly to the Web Role by simply building the code, directly from Visual Studio and just clicking on publish. For simple web applications and even some complex ones, this is all that is required to get the app into the cloud and running. This takes about 1-5 minutes depending on your build time and bandwidth. I’ll measure this first method of deployment with the web role already started, so it is only the deployment being measured. For AWS I’m making the assumption that you’ve already got an EC2 instance running with either Linux + Mono or Windows with IIS Configured and ready. I’ll call it the…
---

|  |  |
| --- | --- |
| [Amazon Web Services](http://aws.amazon.com)  *Amazon Web Services* | [Windows Azure](http://www.microsoft.com/windowsazure)  *Windows Azure* |

[Previous Throw Down…](/2010/11/01/cloudthrowdown-part1/)

Ok, in this edition the fight gets graphic!  Let’s jump right into the bout. I’ve also been thinking about adding Rackspace or another cloud provider, so if you want me to add a comparison point, please let me know and I’ll get them added.

Deploying .NET Web Application Code into AWS and Windows Azure is done in some distinctly different ways.  There are two ways to look at this measurement;

1. One is with a configured Web Role or VM Role in Windows Azure and already configured EC2 Instance for AWS or…
2. A Web Role or VM Role as is and an EC2 Instance as is.

The first scenario one can deploy .NET code directly to the Web Role by simply building the code, directly from Visual Studio and just clicking on publish.  For simple web applications and even some complex ones, this is all that is required to get the app into the cloud and running.  This takes about 1-5 minutes depending on your build time and bandwidth.  I’ll measure this first method of deployment with the web role already started, so it is only the deployment being measured.  For AWS I’m making the assumption that you’ve already got an EC2 instance running with either Linux + Mono or Windows with IIS Configured and ready.  I’ll call it the…

**Deploying .NET Web Applications into Ready Environments**

With Windows Azure the deployment takes about 1-5 minutes from Visual Studio 2010.  With AWS EC2 using the FTP deployment it takes about 1-5 minutes.  In this particular situation, both cloud services are equal for deployment time and steps to deploy.

***Rating & Winner: Deploying .NET Web Applications into Ready Environments** is a tie.*

…the second situation though is where things get tricky and Windows Azure has some startling advantages.  I’ll call this deployment…

**Deploying a .NET Web Application into Environments As-is**

This is a trickier situation.  Setup and then deployment.  For a Web Role the setup is done almost entirely in the actual .NET Web Application Project.  So it is done if the project builds and runs locally.  Nothing available is as fast as a deployment from Visual Studio 2010 straight to a Web Role.  Of course the application has to be built with this specific scenario in mind.  Total deployment time for this is 1-5 minutes.

The AWS EC2 instance you have to configure the operating system and IIS.  Installation of this and setup for the FTP server, etc, often takes several minutes.  So the first time deployment onto an EC2 instance will take a good 5-15 minutes and often requires, as any deployment to a web server does, a few minutes just to make sure all the settings are right and setup just the way you want them.  Overall, this method is not as clean as the Windows Azure Web Role deployment method.

Windows Azure however has a VM Role, similar in many ways to an AWS EC2 instance, and it has the same issues and concerns as deploying to an AWS EC2 instance for the first time.  It requires manual intervention to setup, configure, and assure that all things are in order for the specific application.

Combining these facts for deploying a .NET web application as-is leaves a few odd points.  The VM Role and AWS EC2 instance is definitely more time consuming and prone to human error for deployment because of the additional control one can have.  However the Web Role limits the ability to control many variables of the serving of content from the Web Role, it absolutely is the fastest and cleanest way to deploy a .NET Web Application.

***Rating & Winner:  Deploying a .NET Web Application into Environments As-is** goes to Windows Azure.*

**Virtual Instance Options**

The next measurement is a simple one, virtual instance options.  Windows Azure has the following options available for virtual instances.

|  |  |  |
| --- | --- | --- |
| **Compute Instance Size** | **CPU** | **Memory** |
| Extra Small | 1.0 GHz | 768 MB |
| Small | 1.6 GHz | 1.75 GB |
| Medium | 2 x 1.6 GHz | 3.5 GB |
| Large | 4 x 1.6 GHz | 7 GB |
| Extra large | 8 x 1.6 GHz | 14 GB |

(reference:  <http://www.microsoft.com/windowsazure/compute/default.aspx>)

That gives us 5 different compute instance sizes to choose from.  Amazon Web Services provides the following compute instance sizes.

|  |  |  |
| --- | --- | --- |
| **Compute Instance Size** | **CPU** | **Memory** |
| Micro | Up to 2 EC2 Compute Units | 613 MB |
| Small | 1 Dedicated EC2 Compute Unit | 1.7 GB |
| Large | 4 EC2 compute units | 3.5 GB |
| Extra Large | 8 EC2 compute units | 7 GB |
| High Memory Extra Large | 6.5 EC2 compute units | 17.1 GB |
| High Memory Double Extra Large | 13 EC2 compute units | 34.2 GB |
| High Memory Quadruple Extra Large | 26 EC2 compute units | 68.4 GB |
| High CPU Medium | 5 EC2 compute units | 1.7 GB |
| High CPU Extra Large | 20 EC2 compute units | 7 GB |

Which provides us a diversified range of 9 different instance types.

***Rating & Winner:  Virtual Instance Options** goes to AWS.*

[![Amazon Web Services and Windows Azure](/images/adronhall.smugmug.com/Software/Software-Development/Technology-Company-Logos/azure-aws-logos/1071455180_FWu37-S.png "Amazon Web Services and Windows Azure")](http://compositecode.com/clouds)

*Amazon Web Services and Windows Azure*

***Today’s Winners is***…   **Windows Azure** and **AWS** in a tie.  The rest of my throw down series will be coming over the next week and few days.  If you have any ideas or things I should compare the two services on.

To check out more about either cloud service navigate over to:

- [Amazon Web Services](http://aws.amazon.com) or
- [Windows Azure](http://www.microsoft.com/windowsazure)

> **Disclosure:  I didn’t mention it in either of the previous throw down segments about any disclosure I need to make.  I’m a .NET programmer, love and hate Microsoft at the same time, but have no real honest preference toward either cloud service.  I’m just interested in and always learning more about each technology.  Using either service when their respective capabilities meet the price, feature, or other combination that I can use.  I also do not work directly for Microsoft or Amazon.  Again, thanks for reading.  🙂**
