---
title: A Cloudy Story
date: 2010-05-10 23:37:00 +0000
last_modified_at: 2010-05-10 23:37:00 +0000
permalink: /2010/05/10/a-cloudy-story/
slug: a-cloudy-story
wp_id: 27
original_url: https://compositecode.blog/2010/05/10/a-cloudy-story/
categories:
- Cloud Speak
tags: []
excerpt: I have tried to explain cloud computing in the past, but it never turns out well if I just explain what it is. So instead I have a few stories to tell instead, that provide reasons and why cloud model computing exists. I then have a bit to spin about why cloud computing is the future as well. The face of the Internet is quickly changing. It used to be this zit ridden, crude HTML spaghetti, user experience disaster where people would go and wonder aimlessly. Over time there has come to be a sort of cohesive gathering around certain websites. The websites have changed from time to time and today these websites include Myspace, Facebook, and Twitter as the premier gathering places. These sites each have had various amounts of horrendous downtime, lost user data, fail whales, and other fun implosions of their respective services. These implosions provide great empirical evidence why the Internet has been in desperate need of cloud infrastructure and architecture.
---

I have tried to explain cloud computing in the past, but it never turns out well if I just explain what it is.  So instead I have a few stories to tell instead, that provide reasons and why cloud model computing exists.  I then have a bit to spin about why cloud computing is the future as well.

The face of the Internet is quickly changing.  It used to be this zit ridden, crude HTML spaghetti, user experience disaster where people would go and wonder aimlessly.  Over time there has come to be a sort of cohesive gathering around certain websites.  The websites have changed from time to time and today these websites include [Myspace](http://www.myspace.com), [Facebook](http://www.facebook.com), and [Twitter](http://twitter.com) as the premier gathering places.  These sites each have had various amounts of horrendous downtime, lost user data, fail whales, and other fun implosions of their respective services.  These implosions provide great empirical evidence why the Internet has been in desperate need of cloud infrastructure and architecture.

**What is cloud computing?**  [Wikipedia](http://en.wikipedia.org) defines [cloud computing](http://en.wikipedia.org/wiki/Cloud_computing) as

> "Cloud computing is [Internet](http://en.wikipedia.org/wiki/Internet)-based [computing](http://en.wikipedia.org/wiki/Computing), whereby shared resources, software and information are provided to computers and other devices on-demand, like the electricity grid."

But what do [Myspace](http://www.myspace.com), [Facebook](http://www.facebook.com), and [Twitter](http://twitter.com) have to do with the cloud?  They have all had massive growing pains over the years.  These pains could have been alleviated with a good simple design in any of the modern cloud infrastructures.

So now, back to the stories of these gathering places on the web.  [Myspace](http://www.myspace.com) kicked off years ago in August of 2003.  The core team of eUniverse Employees copied the then popular Friendster Site.  The company supposedly had server capacity and other resources to spare.  However within a short period of time the site had hit limitations and users began to experience failures all the time.  Anyone that used [Myspace](http://www.myspace.com) during this time knows exactly what these were.  A lot of these issues derived from a not so scalable implementation of ColdFusion.  The errors during system failures were commonly the default errors one would see from a choking non-scalable ColdFusion Server.  It became apparent that [Myspace](http://www.myspace.com) had issues.

The simple fact of the matter was, [Myspace](http://www.myspace.com) was ill-prepared for the growth they were receiving.  The servers became overloaded, and could not feed the page requests in a reasonable amount of time.  The problem was the delivery and timeliness of additional server equipment, the [power outages](http://news.netcraft.com/archives/2006/07/24/power_outage_knocks_myspacecom_offline.html), the ability to redeploy fixes to the software architecture, and a host of other problems that kept resurfacing over and over again.

[Facebook](http://www.facebook.com) got started just after [Myspace](http://www.myspace.com) did.  It didn’t immediately have the same issues, but there were failures along the same lines.  One of the ways [Facebook](http://www.facebook.com) managed to hide some of the issues was to control the growth of its user base more.  In addition their architecture was a little ahead of the curve of growth.  But still, even with experiences of others to learn from, [Facebook](http://www.facebook.com) still ran into growth issues a number of times.

Again, the hardware and software were not able to be altered for scalable growth fast enough.  The users of the service got pages that weren’t available and the list of issues grew.  Eventually, [Facebook](http://www.facebook.com) grew itself a cloud of its own.  Just as [Myspace](http://www.myspace.com) had out of necessity.  They grew infrastructure that tied hardware and software together into a cloud of sorts, albeit it was too late to have alleviated the initial problems.  The main thing though, [Myspace](http://www.myspace.com) and [Facebook](http://www.facebook.com) have eliminated the vast majority of their problems by creating this type of infrastructure.

Now one may think, "Oh those nerds must have it down now, surely another high growth service wouldn’t dare not build directly into a cloud environment of some sort!"

WRONG.

Along comes [Twitter](http://twitter.com) in 2006.  Obliviously bounding along into the Internet.  At first it went almost unnoticed.  Around 2008 though this service started to have some heavy growth.  At this time a funny thing happened, the fail whale surfaced and blew its spout!  Immediately users took notice, and at first it became a laughable joke if one got the fail whale.  As time went by, and growth started to rapidly accelerate though the whale came back more and more frequently.  Often times users found it annoying, cursed the very existence of the poor fail whale, and became indignant about the beast from the sea of [Twitter](http://twitter.com).

What had [Twitter](http://twitter.com) failed to do?  They failed to plan or scale appropriately.  They failed because they didn’t setup an appropriate infrastructure.  They failed because they didn’t use a cloud model.  It really is as simple as that.  Sure there are tons of excuses, like those given by Twitter that *Om Malik* quotes, "[*Twitter is, fundamentally, a messaging system. Twitter was not architected as a messaging system, however. For expediency’s sake, Twitter was built with technologies and practices that are more appropriate to a content management system.*](http://gigaom.com/2008/05/25/in-twitters-scoble-problem-a-business-model/)*"*

Excuses, excuses, excuses.  Refactor, rebuild, redeploy.  Oh wait, it is harder than that because they didn’t build for the cloud.

To the point around what cloud computing is.  It really doesn’t matter.  What one needs to know from a business and user perspective is what problems it gets rid of and what power it gives us all.  The cloud has massive potential to remove almost entirely all of the issues that [Myspace](http://www.myspace.com), [Facebook](http://www.facebook.com), and especially [Twitter](http://twitter.com) has had.

Cloud Systems, within the infrastructure itself are the resources to handle systems that sites like [Myspace](http://www.myspace.com), [Facebook](http://www.facebook.com), and [Twitter](http://twitter.com) need.  Within good software architectural practices there are the solutions to get software built right for the cloud.  Within the components that put the software and hardware together the ability to deploy regularly, with accuracy, and almost zero downtime (maybe minutes per year) are available.  Going from development to staging to production are no longer a huge process as it has been in the past.

Now the real challenge is to get businesses to make smart architectural decisions about those systems and get them moved into the cloud!  If your site is intended for high capacity usage on the web or enterprise and legal restrictions don’t stand in your way, this really is a no-brainer for any new startup.  Why would future sites want to go through the same embarrassment, especially when just starting out!
