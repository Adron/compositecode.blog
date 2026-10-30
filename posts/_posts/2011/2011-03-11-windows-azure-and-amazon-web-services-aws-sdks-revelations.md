---
title: Git Rid of Windows Azure and Amazon Web Services (AWS) SDKs with .NET + Git + AppHarbor Deployment Revolution
date: 2011-03-11 20:10:59 -0800
last_modified_at: 2011-03-11 17:36:03 -0800
permalink: /2011/03/11/windows-azure-and-amazon-web-services-aws-sdks-revelations/
slug: windows-azure-and-amazon-web-services-aws-sdks-revelations
wp_id: 2398
original_url: https://compositecode.blog/2011/03/11/windows-azure-and-amazon-web-services-aws-sdks-revelations/
categories:
- .NET Bits
- AWS
- Azure
- Cloud Speak
- Ruby on Rails Bits
tags:
- .NET
- amazon web services
- appharbor
- asp.net
- asp.net mvc
- aws
- cloud
- cloud computing
- engineyard
- git
- heroku
- mercurial
- microsoft
- paas
- ruby on rails
- software development
- software project
- windows azure
excerpt: First a few tidbits on the latest SDKs. For the latest Windows Azure SDK go check out the Microsoft MSDN Site. For the latest for AWS (Amazon Web Services) SDK check out the AWS .NET Site. These two SDKs are great for customers who want to build on the bare bones X platform. Now whatever language & stack one builds in they are tied to that. Ruby on Rails, .NET, Java, PHP, or whatever. But getting tied to the stack is kind of like breathing air, one has to live with what air they have. You can’t exactly get a refund very easily on that. The Cloud SDKs though for Azure & AWS provide a certain amount of lock in, in addition to the stack lock in you’re using. One of the easiest ways to prevent this lock in is to use a general deployment method backed by source control on something like Git or Mercurial. So far though, .NET has been left out the cold. There has been almost zero support for pushing .NET via Git or Mercurial into a cloud.
---

I’ve been wanting to do a quick write up on the state of cloud apps from my perspective.  What’s my perspective?  Well I’m keeping up with  the SDKs from the big players; AWS and Windows Azure.  I’m also working on several cloud applications and providing consulting for some people and companies when approached related to which stack to go with, how to apply their current stacks (such as Ruby on Rails or .NET) in migrating to a cloud service provider.  Cloud services, or really more accurately utility computing has my personal and professional interest.  Above all, I keep trying to stay informed and know what the best path is for anyone that seeks my advice for moving into hosting & working in the SaaS, PaaS, or IaaS Space.  Feel free to contact me in regards to cloud questions:  adronhall at the famous gmail dot com.  🙂

Now on to the good tidbits that have been released lately.

The latest Microsoft ***goodies*** area available.  For the [Windows Azure SDK](http://msdn.microsoft.com/en-us/windowsazure) go check out the [Microsoft MSDN Site](http://msdn.microsoft.com/en-us/windowsazure).

For the latest ***awesome*** from [AWS (Amazon Web Services) SDK](http://aws.amazon.com/) check out the [AWS .NET Site](http://aws.amazon.com/net/).

These two SDKs are great for customers who want to build on the bare bones X platform.  Now whatever language & stack one builds in they are tied to that.  Ruby on Rails, .NET, Java, PHP, or whatever.  But getting tied to the stack is kind of like breathing air, one has to live with what air they have.  You can’t exactly get a refund very easily on that.

The Cloud SDKs though for Azure & AWS provide a certain amount of lock in, in addition to the stack lock in you’re using.  One of the easiest ways to prevent this lock in is to use a general deployment method backed by source control on something like Git or Mercurial.  So far though, .NET has been left out the cold.  There has been almost zero support for pushing .NET via Git or Mercurial into a cloud.

[![Heroku](/images/adronhall.smugmug.com/Software/Software-Development/Technology-Company-Logos/Latest-Bits-01/1213259251_7sKb5-O.png "Heroku")](http://www.heroku.com)

*Heroku*

Ruby on Rails however has had support for this since…  well since the idea popped into the minds of the people at [Heroku](http://heroku.com/), [EngineYard](http://www.engineyard.com), and the other companies that are pushing this absolutely amazing and powerful technology pairing.

[![Engine Yard](/images/adronhall.smugmug.com/Software/Software-Development/Technology-Company-Logos/Latest-Bits-03/1213259252_9QGV9-O.png "Engine Yard")](http://www.engineyard.com)

*Engine Yard*

Again, for .NET, the problem is it has been left in the dust.  Smoked.  It has left a lot of .NET Developers moving to Ruby on Rails (which isn’t new, this is just one more thing that has pulled more developers away from the .NET stack).

Well, that’s changed a bit.  FINALLY someone has gotten the Git + .NET Pairing in the Cloud put together!  FINALLY you can get a cloud application running in a minute or two, instead of the absolutely inane amount of time it takes on Windows Azure (15+ minutes most of the time).  So who has done something about this?

AppHarbor is the first fully deployable solution for the cloud that allows Git + .NET to get going FAST!  I don’t work for these guys at all, so don’t think I’m shilling for them.  I’m just THAT happy that .NET has been pulled out of the dust bins and the community has this option.  I am flippin’ stoked matter of fact.

Currently, because of pricing and ease of deployment, I’ve been solely using AWS.  I can have a .NET MVC app running in AWS in about 5-10 minutes.  Between that speed of setup and the pricing, I pay 2/3 as much as Azure would be and can deploy much fast with a completely traditional .NET deployment.  No special project type needed, no extra configs, just a straight deployment with full control over the server (i.e. I can RDP in with no problem).  Anyway, the list of reasons I went with AWS over Azure really deserve an entire blog entry unto themselves.

[![AppHarbor](/images/adronhall.smugmug.com/Software/Software-Development/Technology-Company-Logos/Latest-Bits-02/1213259278_CFZar-S.png "AppHarbor")](http://appharbor.com/)

*AppHarbor*

With [AppHarbor](http://appharbor.com/) though I can step into the realm of doing exactly the same thing a Ruby on Rails Developer would do with [Heroku](http://heroku.com/) or [EngineYard](http://www.engineyard.com).  Fully PaaS Capable with the scalability and features without needing to port or migrate to an entirely new stack!  I’ll probably keep a number of things running on AWS (such as the pending WordPress Websites I am about to push up to AWS), but will absolutely be starting up some applications to run in AppHarbor.

If you’re a .NET Developer and you’ve been wanting, looking for, and frustrated that the .NET Community didn’t have a Git + Cloud Deployment option for .NET, wait no longer.  Give [AppHarbor](https://appharbor.com) a look ASAP!

Anyway… off to do a little work on my [infrastructure project](https://github.com/Adron/infrastructure/).  Cheers!
