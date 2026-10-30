---
title: 'Cloud Throw Down:  Part 4 – Perspectives on PaaS'
date: 2010-11-29 05:15:44 -0800
last_modified_at: 2011-01-12 06:12:04 -0800
permalink: /2010/11/29/cloudthrowdown-part4/
slug: cloudthrowdown-part4
wp_id: 1689
original_url: https://compositecode.blog/2010/11/29/cloudthrowdown-part4/
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
- cloud storage
- ec2
- microsoft
- web role
- web services
- windows azure
excerpt: Alright, time for the battle o’ clouds to roll on. In this throw down I’m going to compare platforms from the infrastructure and platform perspective. Windows Azure takes a very distinctive, and unique, Platform as a Service (PaaS) model and Amazon Web Services takes a very Infrastructure as a Service (IaaS) model. Each of these things start at different architectural levels for applications and provide different architectural perspectives. Before jumping into the comparison let’s take a look at what a developer, IT, or network specialist has to consider when building and deploying an application into either environment. I’ve highlighted the following steps to the specific profession that each model would most likely involve.
---

|  |  |
| --- | --- |
| [Amazon Web Services](http://aws.amazon.com)  *Amazon Web Services* | [Windows Azure](http://www.microsoft.com/windowsazure)  *Windows Azure* |

[Previous Throw Down…](/2010/11/08/cloudthrowdown-part3-2/)

Alright, time for the battle o’ clouds to roll on. In this throw down I’m going to compare platforms from the infrastructure and platform perspective. Windows Azure takes a very distinctive, and unique, Platform as a Service (PaaS) model and Amazon Web Services takes a very Infrastructure as a Service (IaaS) model. Each of these things start at different architectural levels for applications and provide different architectural perspectives. Before jumping into the comparison let’s take a look at what a developer, IT, or network specialist has to consider when building and deploying an application into either environment.  I’ve highlighted the following steps to the specific profession that each model would most likely involve.

**PaaS, Platform as a Service development and deployment model**

Steps to Begin Building a Web Application or Service Application

1. Start a Project in your preferred development environment.
2. Build the code base.  (Such as a web application or service application)
3. Create the platform web or service role for hosting the web or service application.
4. Setup the project deployment with the role parameters.
5. Deploy the project to that location.
6. Setup an appropriate domain name and point it at the site via nameserver/DNS.

**IaaS, Infrastructure as a Service development and deployment model**

Steps to Begin Building a Web Application or Service Application

1. Start a Project in your preferred development environment.
2. Build the code base.  (Such as a web application or service application)
3. Start the OS Instance of your choice.
4. Install and configure the environment for hosting (IIS, Apache, or otherwise).
5. Setup the project deployment with the role parameters.
6. Deploy the project to that location.
7. Setup an IP address or externally accessible addressing for the instance.
8. Setup an appropriate domain name and point it at the site via nameserver/DNS.

As one can see there are more steps, and with reason, more costs to IaaS than to PaaS.  With IaaS more control and with PaaS less control, but with the lack of control comes lower costs and barriers for entry.  This is most likely, as I’ve heard more than a few times, why Microsoft has pushed the PaaS instead of going IaaS.

So how do each play out in offering the Platform as a Service?

First off, I have to point out that Amazon Web Services doesn’t really offer a PaaS.  So comparing them directly is almost impossible.  In addition, by not offerring a PaaS it sets up AWS at a disadvantage in this realm.  But that being the case, there are 3rd Party Software Companies that offer PaaS Solutions for AWS such as [Makara](http://www.makara.com/) and [Heroku](http://heroku.com/).  In addition there is rumor that [AWS may be heading for a PaaS Offering soon](http://gigaom.com/2010/05/16/are-the-stars-aligning-for-an-amazon-paas-offering/).

I’ve fought with this topic in regards to AWS & Azure.  It all really comes down to what your point of view is.  So that’s how I’m going to score each of the services.  I’ll layout a point of view (POV), which will be a simple description of the team that is building the cloud software, what the end goal is from the business in generic terms, then layout what would be a higher or lower cost, and finally which would provide the fastest time to market with the least amount of cost.  It’ll be complex on the back end, but I’ll work to lay it out as neatly as I can.

> POV:  A Small Business, less than 15 people, working toward a website style SaaS Product.
>
> 1. The team has enough experience and technical skills to develop the product from AWS’s IaaS or Azure PaaS.
> 2. The business wants the product out to market in 3 months.
> 3. The team & business knows which geographic regions they need to focus on specifically.
> 4. The team wants control over instances and has flexibility of server OS, preventing OS lock in. (i.e. they can use Windows or Linux)
> 5. Autoscaling must be robust as traffic is expected, hopefully, to skyrocket as the product becomes recognized and available.

In this situation, AWS wins because of items 1, 2, 3, 4, and especially 5.

> POV:  A small business, less than 15 people, working toward a website style SaaS Product.
>
> 1. The team has .NET and Windows deployment experience, but minimal experience around networking, hosting, or infrastructure experience.
> 2. The business wants the product out to market in 3 months.
> 3. The team & business don’t care what geographic region the website is focused in.
> 4. The team doesn’t care about server lock in, Windows is fine by them.
> 5. Autoscaling and controlling traffic bursts isn’t a high priority for the team or business.

In this situation, Azure wins hands down based on 1, 2, 3, 4, and 5.

> POV:  An enterprise team wants to create a high quality code base, utilizing SCRUM with test driven development practices.
>
> 1. The team knows .NET and Java very well and a little bit of networking, hosting, and infrastructure.
> 2. The enterprise wants a steady release cycle of tested, highly reliable code.
> 3. The enterprise isn’t worried about which OS the team uses.  Windows or a \*nix variant.
> 4. Autoscaling is irrelevant, as long as capacity can be brought up and down in a timely manner to extremely high counts exceeding 1000+ instances.

In this situation, AWS wins hands down on 1, 2, 3, and 4.

> POV:  An enterprise team wants to deploy regularly, maintain their existing .NET stack, and utilize existing SDKs to keep the ramp up time minimal.
>
> 1. The team wants to use a familiar stack based on .NET and use SDKs if available.
> 2. The team isn’t concerned heavily with testable code, mostly just have a framework to build around that is familiar.
> 3. The business just wants the team to maintain familiarity with what exists in the company already.
> 4. The team wants to provide a single sign on (SSO) security implementation, using the cloud if possible.

In this situation, Azure wins easily for reasons 1, 2, 3, and 4.

> POV: A Development team is putting together a public facing SaaS application.
>
> 1. The team wants to use whatever product has the best price point.
> 2. The team wants a strong enterprise style message bus to provide application messaging.
> 3. The business wants to deploy frequently and as soon as possible.
> 4. The team doesn’t care if the code is PHP, Java, .NET, or otherwise.
> 5. The team will create high quality code, and will build their own testing mocks, stubs, and other elements if need be.
> 6. The team doesn’t intend to use the SDKs from either AWS or Windows Azure, they want to keep lock in minimal so are building to services using good design patterns.

This situation is unique, and causes a tie between Azure and AWS for reasons 1 and 2 combined, 3, 4, 5, and 6.

[![Windows Azure](/images/adronhall.smugmug.com/Software/Software-Development/Technology-Company-Logos/windows-azure/1070206913_irzPH-O.gif "Windows Azure")](http://windows.azure.com)

*Windows Azure*

Based on these scorings, things might be a little confusing.  I’ll elaborate a bit on some key points in the next entry on AWS vs. Azure.  For now, I’m going to hand the victory to Windows Azure.  The reason is simple, the PaaS perspective, in a little more than 50% of situation where PaaS or IaaS can be used should go with Windows Azure.  In situations where a PaaS is desired then Windows Azure is pretty much the only serious option out there these days.  Simply, Windows Azure just offers a ton of really serious features via cloud services for a PaaS offering.  Stay tuned for the next grand battle between the cloud giants!
