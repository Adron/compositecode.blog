---
title: Security, A Rant Sort Of… and a shocker.
date: 2010-06-29 21:03:00 -0700
last_modified_at: 2013-09-06 00:01:19 -0700
permalink: /2010/06/29/security-a-rant-sort-of-and-a-shocker/
slug: security-a-rant-sort-of-and-a-shocker
wp_id: 110
original_url: https://compositecode.blog/2010/06/29/security-a-rant-sort-of-and-a-shocker/
categories:
- AWS
- Azure
- Cloud Speak
- Meetups n' Such
tags:
- '#aws'
- amazon web services
- aws
- azure
- cloud
- security
excerpt: Here’s a shocking statement for a lot of people in technology and especially outside of technology. “Your money is at greater risk because it isn’t in a cloud.” Here’s another shocker “Your medical information is at greater risk at your on-premises Doctor than if it were stored and protected by access control in the cloud.” Is that shocking to you? If you aren’t shocked you probably know a lot about cloud technology. The cloud is more secure than most of the IT Departments, physical server locations, secure Government installation, and other environments than one might imagine. Why Am I Writing This Blog Entry?
---

Here’s a shocking statement for a lot of people in technology and especially outside of technology.  “*Your money is at greater risk because it isn’t in a cloud.*”  Here’s another shocker “*Your medical information is at greater risk at your on-premises Doctor than if it were stored and protected by access control in the cloud.*”

Is that shocking to you?  If you aren’t shocked you probably know a lot about cloud technology.  The cloud is more secure than most of the IT Departments, physical server locations, secure Government installation, and other environments than one might imagine.

**Why Am I Writing This Blog Entry?**

While I was listening to [Steve Riley](http://stvrly.wordpress.com/)’s talk on [AWS](http://aws.amazon.com) Security I started this blog entry.  A few of the questions that were brought up made me realize how little of the physical and platform level security is actually understood.  Even though this was about AWS it also applies to [Azure](http://www.microsoft.com/windowsazure), [Google](http://www.google.com), and other cloud environments and platforms.  After several weeks of studying Azure and several years of working with Cloud type technology at [Webtrends](http://www.webtrends.com) this statement shocked me, “*A bank or a medical entity wouldn’t put its data in the cloud.*”\*  I couldn’t help but think that someone posing this statement as a fact (even though I know that it is absolutely not a fact) is sorely misinformed about cloud computing and technology.

Well, I wanted to retort this this statement myself, but Steve handled the question as a rock star presenter would.  But I still want to elaborate on this topic.  Also check my previous blog entry “[Your Cloud, My Cloud, Security in the Cloud](/2010/05/28/your-cloud-my-cloud-security-in-the-cloud/)” (**\* See Addendum)** as I touched on this topic from the vantage point of web analytics.  What we have here is the conversation of data that truly needs to be secure.

**Cloud Security – Physical**

The cloud environments has physical locations all over the world.  Each of these locations are not advertised or easily located.  They are obfuscated and not listed for the reasons of security.  Once you get to one of these facilities the location has numerous physical security restrictions including; time based access codes, security cards, some have retinal scanners, and the list goes on.  In addition, many of these security methods are used concurrently with others.

In addition to this, people maintaining the cloud technology centers don’t have access to the data.  They do not even know how, nor could someone specifically tell them how to gain access to specific drives or machines that have the data of specific instances without extensive work.  That alone provides an immediate level of security, both for data and physically.  That leads me to this next point.

**Data Security in the Cloud**

Having data spread across virtualized storage mediums is a step into another realm of security.  For more than just security reasons data is spread across multiple storage locations.  Because of the virtualized nature of this storage the actual data is located in a number of locations that is shared among machines.  These machines are not maintained in relation to these storage points.  The storage points are tracked by the machines, in secure ways, so that only an account can access that data.  In addition to this spread of the data, the storage is actually moved from point to point on machine at various times to maintain uptime and redundancy.  Because of this it also increases the complexity in finding this data by nefarious means.

One final point of physical security for data is that each customer, has completely segmented data stored in separate virtual instances.  This separation is equivalent to two storefront businesses side by side.  They are separated by a physical wall just like the manipulation of data in the cloud.  This is important to grasp on many levels as nobody would question placing one business next to another – entire cities have existed for hundreds of years that way – so can businesses within the cloud.

***Security at the Platform Level…***

…I wanted to continue on this topic but I’m going to hold off.  Right now for work and personally I’m researching a number of additional security ideas within the cloud.  It includes physical, data, access control and other security principles.  I’ll have that write up for for another day, inclusive of the platform level security.

…as for now, that wraps up this semi-ranting piece.
