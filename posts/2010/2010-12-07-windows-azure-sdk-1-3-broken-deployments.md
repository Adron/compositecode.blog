---
title: Windows Azure SDK 1.3 Broken Deployments
date: 2010-12-07 05:05:04 -0800
last_modified_at: 2010-12-06 23:14:46 -0800
permalink: /2010/12/07/windows-azure-sdk-1-3-broken-deployments/
slug: windows-azure-sdk-1-3-broken-deployments
wp_id: 1910
original_url: https://compositecode.blog/2010/12/07/windows-azure-sdk-1-3-broken-deployments/
categories:
- Azure
- Rants
tags: []
excerpt: 'I’ve been using the 1.3 SDK now for about a week. I have one single machine that can deploy an ASP.NET MVC Application to Windows Azure. The other 32 bit machine and 64 bit machine do not, fail pretty much every time I do a build on them. This is how it looks so far. Machine 1 is: 32 bit, 4 GB RAM with Win 7, .NET 4.0 with VS 2008 + 2010 individual installs of software over a period of about 10 months. In other words, it isn’t the cleanest installation anymore. Machine 2 is: 32 bit, 4 GB RAM with Win 7, .NET 4.0 with VS 2010. Relatively clean enterprise level installation of Windows. Machine 3 is: 64 bit, 8 GB RAM with Win 7, .NET 4.0 with VS 2010. The installation is literally 4 days old now.'
---

I’ve been using the 1.3 SDK now for about a week.  I have one single machine that can deploy an ASP.NET MVC Application to Windows Azure.  The other 32 bit machine and 64 bit machine do not, fail pretty much every time I do a build on them.  This is how it looks so far.

Machine 1 is: 32 bit, 4 GB RAM with Win 7, .NET 4.0 with VS 2008 + 2010 individual installs of software over a period of about 10 months.  In other words, it isn’t the cleanest installation anymore.

Machine 2 is: 32 bit, 4 GB RAM with Win 7, .NET 4.0 with VS 2010.  Relatively clean enterprise level installation of Windows.

Machine 3 is: 64 bit, 8 GB RAM with Win 7, .NET 4.0 with VS 2010.  The installation is literally 4 days old now.

Machine 3 fails to provide a build that is deployable every single time.  It creates what I call a “Ghost Deploy”.  See the video below:

<iframe allow="clipboard-write; presentation" allowfullscreen="" aria-label="VideoPress Video Player" data-resize-to-parent="true" frameborder="0" height="646" src="https://videopress.com/embed/FjFloe6A?hd=1&amp;cover=1&amp;loop=0&amp;autoPlay=0&amp;permalink=1&amp;muted=0&amp;controls=1&amp;playsinline=0&amp;useAverageColor=0&amp;preloadContent=metadata" title="VideoPress Video Player" width="862"></iframe>

Machine 2 actually completes a deployment after setting the assemblies in the ASP.NET MVC Web Application to local and removing the diagnostic configuration settings.  This is the only machine I’ve had successfully deploy a Windows Azure 1.3 SDK ASP.NET MVC Web Application in the last week.

Machine 1 actually just spools the deployment into the Web Role, but then it spins, busy without starting.  Once after about 45 minutes it did finally stop.

In the video I did not have a certificate added to the web role, but have since added one and tried to launch the web app (on Machine 2), still nothing.  It at least does not turn into a Ghost Deployment.  On machine 3 the deployment with the certificate still just dies.

I’ve tried to set all assemblies to local, I get no changes.  I’ve assured no configuration changes have diagnostics in them.

Machines 1 and 2 both deployed Windows Azure ASP.NET MVC Application without any issue before SDK 1.3.  Machine 3 I’ve just built, so certain issues may be inherent in the machine load itself, but with the other issues still rearing their heads, I doubt that Machine 3 is at fault but instead am leaning toward SDK 1.3.

Anyone else out there having any issues?  Seen the continual spooling?  Compared to SDK 1.2 (which I didn’t even have a single issue with) this is really disconcerting.  I encourage cloud technology use to major enterprises, and this type of mistake is worrisome.  Fortunately for me (or maybe I should say fortunately for Microsoft) I’m not pushing any efforts with the 1.3 SDK right now.  It has a few new features I’d really like to try out, but at the current time I can rarely get a decent deployment, let alone something that tests out the new features.  Plz fix k thx bye.  🙂
