---
title: Cloud Failure, FUD, and The Whole AWS Oatage…
date: 2011-04-24 21:42:43 -0700
last_modified_at: 2011-04-25 13:52:06 -0700
permalink: /2011/04/24/cloud-failure-fud/
slug: cloud-failure-fud
wp_id: 2729
original_url: https://compositecode.blog/2011/04/24/cloud-failure-fud/
categories:
- Architecture
- AWS
- Azure
- Cloud Speak
- Infrastructure
- PSA
- Rants
tags:
- amazon web services
- aws
- cloud
- cloud computing
excerpt: 'Ok. First a few facts. AWS has had a data center problem that has been ongoing for a couple of days. AWS has NOT been forthcoming with much useful information. AWS still has many data centers and cloud regions/etc up and live, able to keep their customers up and live. Many people have NOT built their architecture to be resilient in the face of an issue such as this downtime. It all points to the mantra to the “keep a backup”, but many companies have NOT done that. Now a few personal observations and attitudes toward this whole thing. If you’re site is down because you had a single point of failure in one of the zones in one region at AWS. That’s your bad architectural design, plain and simple. You NEVER build a site like that if you actually expect to stay up with 99.99% or even 90% of the time. Anyone in the cloud business, SaaS, PaaS, or otherwise should know better than that. Everytime I hear someone from one of these companies whining about how it was AWSs responsiblity, I ask, is the auto manufacturer responsible for the 32k dead in 2010? How about the 50k dead in the year of peak automobile deaths? Nope, those deaths are the responsiblity of the drivers. When you get behind the wheel you need to, you MUST know what power you yield. You might laugh, you might jest that I use this corralary, but I wanted to use an example ala Frédéric Bastiat (if you don’t know who he is, check him out: Frédéric Bastiat). Cloud computing, and its use, is a responsibility of the user to build their system well. One of the common things I keep hearing over and over about this is, “…we could have made our site resilient, but it’s expensive…” Ok, let me think for a second. Ummm, I call bullshit. Here’s why. If you’re a startup of the most modest means, you probably need to have at least 100-300 dollars of services (EC2, S3, etc) running to make sure you’re site can handle even basic traffic and a reasonable business level (i.e. 24/7, some traffic peaks, etc). With just $100 bucks one can setup multiple EC/2 instances, in DIFFERENT regions, load balance between those, and assure that they’re utilizing a logical storage medium (i.e. RDS, S3, SimpleDB, Database.com, SQL Azure, and the list goes on and on). There is zero reason that a business should have their data stored ON the flippin’ EC2 instance. If it is, please go RTFM on how to build an application for the Internets. K Thx. Awesomeness!! 🙂 Now there are some situations, like when Windows Azure went down (yeah, the WHOLE thing) for about an hour or two a few months after it was released. It was, however, still in “beta” at the time. If ALL of AWS went down then these people who have not built a resilient system could legitimately complain right along with anyone else that did build a legitimate system. But those companies, such as Netflix, AppHarbor, and thousands of others, have not had downtime because of this data center problem AWS is having. Unless you’re on one instance, and you want to keep your bill around $15 bucks a month, then I see ZERO reason that you should still be whining. Roll your site up somewhere else, get your act together and ACT. Get it done. I’m honestly not trying to defend AWS either. On that note, the response time and responses have been absolutely horrible. There has been almost ZERO social media, forum, or other responses that remotely resemble some educated technical people working on this problem. In addition to this, Amazon has allowed the media to run wild with absolutely inane and sensational headlines about the whole incident. Not only are they not providing information to the customers, but whatever mechanisms are internal to the company that are supposed to manage this type of incident from a public relations aspect are acting morbidly slow. From a technology company, especially of Amazon’s capabilities and technical prowess (generally, they’re YEARS ahead others) this is absolutely unacceptable and disrespectful on a personal level.'
---

### *Ok.  First a few facts.*

- AWS has had a data center problem that has been ongoing for a couple of days.
- AWS has NOT been forthcoming with much useful information.
- AWS still has many data centers and cloud regions/etc up and live, able to keep their customers up and live.
- Many people have NOT built their architecture to be resilient in the face of an issue such as this.  It all points to the mantra to “keep a backup”, but many companies have NOT done that.
- Cloud Services are absolutely more reliable than comparable hosted services, dedicated hardware, dedicated virtual machines, or other traditional modes of compute + storage.
- Cloud Services are currently the technologically superior option for compute + storage.

### *Now a few personal observations and attitudes toward this whole thing.*

If you’re site is down because of a single point of failure that is ***your*** bad architectural design, plain and simple. You ***never*** build a site like that if you actually expect to stay up with 99.99% or even 90% of the time. Anyone in the cloud business, SaaS, PaaS, hosting or otherwise should know better than that. Everytime I hear someone from one of these companies whining about how it was AWSs responsiblity, I ask, is the auto manufacturer responsible for the 32,000 innocent dead Americans in 2010? How about the 50,000 dead in the year of peak automobile deaths? Nope, those deaths are the responsiblity of the drivers. When you get behind the wheel you need to, you MUST know what power you yield. You might laugh, you might jest that I use this corralary, but I wanted to use an example ala Frédéric Bastiat (if you don’t know who he is, check him out: [Frédéric Bastiat](http://en.wikipedia.org/wiki/Fr%C3%A9d%C3%A9ric_Bastiat)). Cloud computing, and its use, is a responsibility of the user to build their system well.

One of the common things I keep hearing over and over about this is, “…we could have made our site resilient, but it’s expensive…”  Ok, let me think for a second.  Ummm, I call bullshit.  Here’s why.  If you’re a startup of the most modest means, you probably need to have at least 100-300 dollars of services (EC2, S3, etc) running to make sure you’re site can handle even basic traffic and a reasonable business level (i.e. 24/7, some traffic peaks, etc).  With just $100 bucks one can setup multiple EC/2 instances, in DIFFERENT regions, load balance between those, and assure that they’re utilizing a logical storage medium (i.e. RDS, S3, SimpleDB, Database.com, SQL Azure, and the list goes on and on).  There is zero reason that a business should have their data stored ON the flippin’ EC2 instance.  If it is, please go RTFM on how to build an application for the Internets.  K Thx. Awesomeness!!  🙂

Now there are some situations, like when Windows Azure went down (yeah, the WHOLE thing) for about an hour or two a few months after it was released.  It was, however, still in “beta” at the time.  If ALL of AWS went down then these people who have not built a resilient system could legitimately complain right along with anyone else that did build a legitimate system. But those companies, such as Netflix, AppHarbor, and thousands of others, have not had downtime because of this data center problem AWS is having.  Unless you’re on one instance, and you want to keep your bill around $15 bucks a month, then I see ZERO reason that you should still be whining.  Roll your site up somewhere else, get your act together and ACT. Get it done.

I’m honestly not trying to defend AWS either.  On that note, the response time and responses have been absolutely horrible. There has been zero legitimate social media, forum, or responses that resemble an solid technical answer or status of this problem. In addition to this Amazon has allowed the media to run wild with absolutely inane and sensational headlines and often poorly written articles.  From a technology company, especially of Amazon’s capabilities and technical prowess (generally, they’re ***YEARS*** ahead others) this is absolutely unacceptable and disrespectful on a personal level to their customers and something that *Amazon should mature their support and public interaction along with their technology*.

Now, enough of me berating those that have fumbled because of this. Really, I do feel for those companies and would be more than happy to help straighten out architectures for these companies (not for free). Matter of fact, because of this I’ll be working up some blog entries about how to put together a geographically resilient site in the cloud.  So far I’ve been working on that instead of this rant, but I just felt compelled after hearing even more nonsense about this incident that I wanted to add a little reason to the whole fray.  So stay tuned and I’ll be providing ways to make sure that a single data-center issues doesn’t tear down your entire site!

***UPDATE***:  If you know of a well written, intelligent response to this incident, let me know and I’ll add the link here.  I’m not linking to any of the FUD media nonsense though, so don’t send me that junk.  🙂  Thanks, cheers!

- [Bob Warfield](http://smoothspan.wordpress.com/) – [People Using Amazon Cloud:  Get Some Cheap Insurance At Least](http://smoothspan.wordpress.com/2011/04/23/people-using-amazon-cloud-get-some-cheap-insurance-at-least/)
- [Rightscale – Amazon EC2 Outage:  summary and lessons learned](http://blog.rightscale.com/2011/04/25/amazon-ec2-outage-summary-and-lessons-learned/)
- [Smugmug – How SmugMug survived the Amazonpocalypse](http://don.blogs.smugmug.com/2011/04/24/how-smugmug-survived-the-amazonpocalypse/)
- [Mr Jassy, Tear Down This Wall](http://roman.stanek.org/2011/04/21/mr-jassy-tear-down-this-wall/)
