---
title: Windows Azure v1.3 SDK Issues
date: 2010-12-03 15:10:56 -0800
last_modified_at: 2010-12-04 17:51:07 -0800
permalink: /2010/12/03/windows-azure-v1-3-sdk-issues/
slug: windows-azure-v1-3-sdk-issues
wp_id: 1899
original_url: https://compositecode.blog/2010/12/03/windows-azure-v1-3-sdk-issues/
categories:
- Azure
- Rants
tags:
- microsoft
- windows azure
excerpt: I’ve been having oodles of deployment issues with Windows Azure lately ever since upgrading to the 1.3 SDK. It seems on one machine (which is 32-bit) when I do a build and deploy it appears to word. On my 64-bit machine with a COMPLETELY clean load of Win 7 and VS 2010 + the Windows Azure SDK 1.3 it never deploys. Just keeps trying and eventually gives up after about 30-45 minutes. Very painful. So far I’ve had some twitter conversations and Eugenio Pace has helped a lot in trying to figure out what the problem is. At CloudCamp however I start an empty ASP.NET MVC 2 app and deployed it, as things go it worked flawlessly. I guess Eugenio scared it into operating properly! 🙂 Also Rinat Abdullin has run into some issues with the 1.3 drop also. Rinat’s entry is titled “Don’t Upgrade to Windows Azure SDK 1.3 Yet”, so you might get the vibe you may not want to upgrade yet. I also got this tweet from Eugenio on a troubleshooting page on the MSDN site. It may help if you’re slugging through some issues.
---

I’ve been having oodles of deployment issues with Windows Azure lately ever since upgrading to the 1.3 SDK.  It seems on one machine (which is 32-bit) when I do a build and deploy it appears to word.  On my 64-bit machine with a COMPLETELY clean load of Win 7 and VS 2010 + the Windows Azure SDK 1.3 it never deploys.  Just keeps trying and eventually gives up after about 30-45 minutes.  Very painful.

So far I’ve had some twitter conversations and Eugenio Pace has helped a lot in trying to figure out what the problem is.  At CloudCamp however I start an empty ASP.NET MVC 2 app and deployed it, as things go it worked flawlessly.  I guess Eugenio scared it into operating properly!  🙂

Also Rinat Abdullin has run into some issues with the 1.3 drop also.  Rinat’s entry is titled “[Don’t Upgrade to Windows Azure SDK 1.3 Yet](http://abdullin.com/journal/2010/12/3/dont-upgrade-to-windows-azure-sdk-13-yet.html)“, so you might get the vibe you may not want to upgrade yet.

I also got this tweet from Eugenio on a troubleshooting page on the MSDN site.  It may help if you’re slugging through some issues.

> ![Eugenio Pace](https://a2.twimg.com/profile_images/326986850/Eugenio_Pace_2009_01_normal.jpg) @[adronbh](http://twitter.com/adronbh) Latest list of deployment issues on Win [#Azure](http://twitter.com/#!/search?q=%23Azure "#Azure")[http://bit.ly/hTpEeN](http://bit.ly/hTpEeN "http://msdn.microsoft.com/en-us/library/gg465402.aspx/")
