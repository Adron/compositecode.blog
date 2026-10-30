---
title: The Exciting Nature of SLAs, A Comparison
date: 2012-06-30 09:01:04 -0700
last_modified_at: 2012-06-27 09:49:27 -0700
permalink: /2012/06/30/the-exciting-nature-of-slas-a-comparison/
slug: the-exciting-nature-of-slas-a-comparison
wp_id: 5874
original_url: https://compositecode.blog/2012/06/30/the-exciting-nature-of-slas-a-comparison/
categories:
- Cloud Speak
tags:
- service level agreement
- sla
excerpt: Ok, I’ll admit a secret. I haven’t read a single flippin’ SLA ever for cloud computing, hosting, managed hosting or other services. The main reason, is because it doesn’t matter unless you plan on prospectively suing or whining about your own bad architecture at some point. Sometimes, rarely, service is soooooo bad you have to pull out …
---

Ok, I’ll admit a secret.

I haven’t read a single flippin’ SLA ever for cloud computing, hosting, managed hosting or other services. The main reason, is because it doesn’t matter unless you plan on prospectively suing or whining about your own bad architecture at some point. Sometimes, rarely, service is soooooo bad you have to pull out of the service, but generally in the vast majority of situations you can find information regarding the quality of a service. Google, Bing, and Yahoo are your friends when it comes to this. Also don’t forget your own network (you do have a network of people right?) Ask around, look around, read, research and check out anyone your going with. SLAs are a LAST RESORT item and should be treated as such.

Simply, the only thing I want in the SLA is something that covers me if I need to pull my services out of somewhere. Especially with cloud computing services (and I mean real cloud computing services that meet my baseline of geographically distributed, highly available, etc., etc like: AWS (yes I’ve done work with them), Rackspace (collaborated with them), Tier 3 (yes, I work for them), Windows Azure (yup, worked for them too and with their services), Joyent (I’ve actually never touched their services but I know what they are and what they’re capable of, no problem putting them in this category), and a few others.

So I dragged a few SLAs together for a comparo to see if there were many real differences between them. Here’s what I found from the following SLAs.

## SLA Comparison Discussion

- [AWS SLS for EC2](http://aws.amazon.com/ec2-sla/) and for [AWS S3](http://aws.amazon.com/s3-sla/) and the [really simple FAQ summary of their SLAs](http://aws.amazon.com/ec2/faqs/#How_do_I_know_if_I_qualify_for_a_SLA_Service_Credit).
- [Windows Azure SLA Summaries](https://www.windowsazure.com/en-us/support/legal/sla/), and the [Word Doc Version of the full Compute SLA](http://www.microsoft.com/en-us/download/details.aspx?id=24434) (don’t ask me…) and click on the summaries links for each SLA for storage and other services.
- Heroku SLA => DOESN’T HAVE ONE THAT I COULD FIND! Wowzer, holy moly.
- [Engine Yard SLA](http://www.engineyard.com/legal/xcloud-sla)

A great comparison, with grade rating of various SLAs is also available at IT Knowledge Exchange titled “[A Tale of Three Cloud SLAs](http://itknowledgeexchange.techtarget.com/cloud-computing/the-tale-of-three-cloud-slas-2/)“. I got a few points from there in putting together this blog entry.

Overall it looks like AWS & Windows Azure both have fairly elaborate SLAs at first glance. However the company that really seems to have put together a solid [“honor” based SLA is EngineYard’s](http://www.engineyard.com/legal/xcloud-sla). AWS & Azure both read like a bunch of lawyers sat around in a big room, that don’t understand anything about computing, and had one engineer throw words out that actually mean something – and then they ran rampant with those terms spliced through a few thousand pages of material. However, to summarize…

Both of their agreements tend to state that if YOU can PROVE that the downtime was caused by them then you can get recouped with service credits for those hours. Note, that it is a remuneration in credits, not in cold hard cash or otherwise. This seems to continue in others that I read too. But let’s loop back around for a second…

## What do You REALLY Want?

Do you want an SLA or service? That’s the real quistion. If you want service and you actually have your systems put together well then moving infrastructure to the cloud or platform operations to the cloud is what you want. The fact of the matter, most of the cloud services by Windows Azure, AWS, EngineYard, Tier 3, Heroku, or otherwise have an extremely high uptime. Expectations can EASILY be in the five 9’s range. However, it is up to you to make sure that YOUR SOFTWARE is going to be able to handle that.

## The Real Problems…

One issue I have noticed is this expectation that you can put a traditional application in the cloud and then it magically has better high availability and such. This is absolutely WRONG. Cloud services give you the ability to build or expand “SCALABLE” applications to a higher uptime that can’t be achieved easily, or at all, with traditional hosting and data center operations. If you take SAP, Oracle’s Database, SQL Server, Exchange, or other NON-cloud type software and stick it in the cloud you’ll still have the traditional issues to deal with related to vertically designed software. These packages are not, nor were they intended to be run in geographically dispersed, fabric enabled, highly scaled, low cost cloud provisions. They don’t make use of map reduction, query enhancements, node based computing or storage integrity, or other characteristics that cloud computing brings to us.

So the real problem isn’t “is the cloud going to provide X 9’s of uptime…?” the real question is, “Will the software you’ve made, bought, or what to use going to take advantage of the features in the cloud that will allow it to have X 9’s of uptime?”

So really, focus the question around how your software works, not SLAs. That’s my two cents, maybe you still want that CYA in the SLA, but you won’t rest easy because there isn’t a whole lot of recourse if you stick crappy software in the cloud and then it falls over on you. So best of luck, but focus on that software, not on SLAs. Cheers!
