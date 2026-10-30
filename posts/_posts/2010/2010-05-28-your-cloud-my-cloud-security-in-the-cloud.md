---
title: Your Cloud, My Cloud, Security in the Cloud
date: 2010-05-28 13:23:00 -0700
last_modified_at: 2010-06-14 18:22:51 -0700
permalink: /2010/05/28/your-cloud-my-cloud-security-in-the-cloud/
slug: your-cloud-my-cloud-security-in-the-cloud
wp_id: 15
original_url: https://compositecode.blog/2010/05/28/your-cloud-my-cloud-security-in-the-cloud/
categories:
- Cloud Speak
tags:
- cloud
- google
- omniture
- security
- unica
- webtrends
- yahoo
excerpt: I had a great conversation the other night while at the Seattle Web Analytics Wednesday (#waw) with Carlos (@inflatemouse) and a dozen others. @inflatemouse brought up the idea that an analytics provider using the cloud, increases or at least possibly increases the risk of security breach to the data. This is, after all a valid point, but because of the inherent way web analytics works this is and is not a concern. Web Analytics is Inherently Insecure Web analytics data is collected with a Javascript Tag. Omniture, Webtrends, Google, Yahoo, and all of the analytics providers use Javascript. Javascript is a scripting language, which is not compiled, and stored in plain text in the page or an include, or passed into the URI when needed. This plain text Javascript is all over the place, and able to be read merely by looking at it. So the absolute first point of data collection, the Javascript tags, is 100% insecure.
---

I had a great conversation the other night while at the Seattle Web Analytics Wednesday ([#waw](http://search.twitter.com/search?q=%23waw)) with Carlos ([@inflatemouse](http://twitter.com/inflatemouse)) and a dozen others.  @[inflatemouse](http://twitter.com/inflatemouse) brought up the idea that an analytics provider using the cloud, increases or at least possibly increases the risk of security breach to the data.  This is, after all a valid point, but because of the inherent way web analytics works this is and is not a concern.

> **Web Analytics is Inherently Insecure**

Web analytics data is collected with a Javascript Tag.  [Omniture](http://www.adobe.com), [Webtrends](http://www.webtrends.com), [Google](http://www.google.com), [Yahoo](http://www.yahoo.com), and all of the analytics providers use Javascript.  Javascript is a scripting language, which is not compiled, and stored in plain text in the page or an include, or passed into the URI when needed.  This plain text Javascript is all over the place, and able to be read merely by looking at it.  So the absolute first point of data collection, the Javascript tags, is 100% insecure.

The majority of data is not private.  So this insecurity isn’t a huge risk or at least should not be.  If it is, you have larger issues before you even contemplate using an on-premise and cloud solution to bump up your compute and storage capabilities.  Collecting data that needs to be secure via web analytics is an absolute no.  Do NOT collect secure, private, or other important pieces of data this way.  If you have even the slightest legal breach in this context, your entire analytics provision could have this data scraped, possibly used in court in a class action suite, or in other ways even.

For the rest of this write up, I will assume that you?ve appropriately encrypted, or enabled SSL, or otherwise secured your analytics or data collection in some way.

> **Getting that Boost on Black Friday**

eE-commerce has gotten HUGE over the last decade.  The last Black Friday sales and holiday season saw the largest e-commerce activity in history.  [Omniture](http://www.adobe.com), [Webtrends](http://www.webtrends.com), and all of the other web analytics providers often see a ten fold increase in web traffic over this period of time.  Sometimes, for some clients, this traffic is handled flawlessly by racks and racks of computers sitting in multiple collocation facilities around the world.  However, for some clients that have exceedingly large traffic boosts, data is lost.  (yes, ALL the providers lose data, more so during these massive boosts)  The reason is simple, the machines can?t process in time or handle the incoming traffic because the extra throughput isn?t available to scale.

Enter the cloud.  The cloud has vastly more scalability, almost an infinite supply by comparison, to any of the infrastructure available to the analytics providers.  Matter of fact the cloud has more scale available than all of the analytics providers.  This is actually saying a lot, because [Webtrends](http://www.webtrends.com) (and maybe some of the others) I know does an amazing job with their scalability and data collection, arguably more accurate and consistent than any of the other providers (especially since many of them just sample and "guess" at the data).

So when you extend your capabilities to the cloud for web analytics do you really increase your security vulnerability?  Most of the providers of web analytics have their own array of security measures, that I won’t go into on levels of security.  However, does introducing the cloud change anything?  Does it alter the architecture so significantly as to introduce legitimate security concerns?

Immediately, from a functional point of view, assuming good architecture, intelligent system design, and good security practices are in use already, introducing the cloud should and is transparent to clients.  For the provider it should not increase legal concerns, functional concerns, or otherwise pending the aforementioned items are taken care of appropriately.  But that is just it, every single current provider has legacy architecture, various other elements that do not provide a solid basis for a migration to the cloud for that extra bump of power and storage.

So what should be done?  What if a provider wants that extra power?  Can the technical debts be paid to use the awesome promises of the cloud?  Is the security really secure enough?

***Probably not.  Probably so.  But . . .***

This provides a prospective opportunity for a new solution for web analytics to be provided.  It provides a great opportunity for a modern cloud based solution, that provides more than just a mere Javascript tag and insecure unencrypted data to be collected for analysis.  It provides the grand opportunity to design an architecture that could truly lead the industry into the future.  Will [Webtrends](http://www.webtrends.com), [Omniture](http://www.adobe.com), [Unica](http://www.unica.com/), or someone else step in to lead the analytics industry into the future?

At this point I’m not really sure, but it definitely is an interesting thought and a conversation that I have had a lot of people at #altnet meetings, cloud meetups, and with cloud architects, engineers, and others that have similar curiosities.  I await *impatiently* to see someone or some business take the lead!
