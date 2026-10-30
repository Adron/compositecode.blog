---
title: Introducing Junction
date: 2013-08-20 01:07:08 -0700
last_modified_at: 2013-09-06 11:13:33 -0700
permalink: /2013/08/20/introducing-junction/
slug: introducing-junction
wp_id: 8756
original_url: https://compositecode.blog/2013/08/20/introducing-junction/
categories:
- .NET Bits
- Basho
- Community
- Junction Project
- Riak
tags:
- .NET
- apache 2.0
- c#
- corrugated iron
- corrugatediron
- junction
- windows 8
excerpt: Today I’ve officially kicked off a new project from my notebook of projects based around building a Riak admin, data manipulation, reporting and news tool for Windows 8. If you want to jump right to the project, here’s the Github Pages Site, the Github Junction Repo and eventually I’ll have it listed in the Windows …
---

[![](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-3Xxk8NH/0/O/Dashboard%20Goodness.jpg)](http://adron.github.io/junction/)Today I’ve officially kicked off a new project from my [notebook of projects](/2013/08/19/farewell-basho-its-been-swell-yo/) based around building a *Riak admin, data manipulation, reporting and news tool for Windows 8*. If you want to jump right to the project, here’s the [Github Pages Site](http://adron.github.io/junction/), the [Github Junction Repo](https://github.com/Adron/junction) and eventually I’ll have it listed in the Windows 8 Store for download. Yes, it’ll be ***free*** as in beer, it’ll all be [Apache 2.0 Licensed](http://www.apache.org/licenses/LICENSE-2.0.html) and the project is open to contributors and others that want to jump into things. There’s also a quick intro for how I setup the “[Windows 8 Logos, Badges & Splash Screens of Riak](/2013/08/09/windows-8-logos-badges-spash-screens-of-riak/)“.

So now that I’ve provided the links, here’s a quick intro to each of the application sections, what this application is for, where the workflow for contributions will be and what the next steps are. Trust me, I roll easy, I’ll be working as hard as I can to make pull requests easy peasy, keep the issues down to workable contributions and the whole “this is a good OSS project”.

[![Riak Junction Application rocking on the Windows 8 desktop with a full tile!](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-QLMdvNJ/0/M/Junction002-M.png)](http://adron.github.io/junction/)

*Riak Junction Application rocking on the Windows 8 desktop with a full tile!*

## Juncture Divisions

The juncture application should be split into several key components, or application divisions of functionality. I’ve broken each out with a basic description. If you just want to watch a video where I outline each division, play the video below for a quick 5 minute intro to the application and the idea behind it all.

<iframe allowfullscreen="" frameborder="0" height="360" loading="lazy" mozallowfullscreen="" src="https://player.vimeo.com/video/72575375" webkitallowfullscreen="" width="640"></iframe>

A quick run through of the first sample UI.

<iframe allowfullscreen="" frameborder="0" height="360" loading="lazy" mozallowfullscreen="" src="https://player.vimeo.com/video/72716828" webkitallowfullscreen="" width="640"></iframe>

**[![](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-QsrBDtc/0/S/diagnose-S.png)](http://adron.github.io/junction/)Call the Doctor! (Administration & Maintenance)**

This part of the application would provide an interface for all the general administration and maintenance needs around individual nodes and around the overall cluster of nodes. The ability to add, remove and generally administer everything that is available via the [riak-admin command line interface](http://docs.basho.com/riak/latest/ops/running/tools/riak-admin/).

**[![](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-LL6Hp4z/0/S/drwho-S.png)](http://adron.github.io/junction/)Time Travel That Data (Performance Benchmarking)**

This section of the application will provide the ability to benchmark the timing of data in and out of a cluster. In addition it should show standard benchmarking similar to that which is offered with the [basho\_bench project](http://docs.basho.com/riak/latest/ops/building/benchmarking/).

**[![](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-XV9pDs7/0/S/hugs-S.png)](http://adron.github.io/junction/)Love of the Data (Reporting)**

This division of the application would be focused on reporting. I’m not sure what exactly that would entail, but something with charts, graphs and pulling together trending points of some sort. If you have ideas and want to work on this part of the application, weigh in!

**[![](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-q8qtfJV/0/S/golfer-S.png)](http://adron.github.io/junction/)Golfing With Your Data (Query, Put, Deletes, Etc. Handling the CRUD)**

The application will have an interface to provide access to add and remove data, as well as viewing the data that is available within a cluster. The primary means for implementing this part of the application will be with the CorrugatedIron Project. It’s a library available via Nuget that [@peschkaj](https://twitter.com/peschkaj) and [@TheColonial](http://twitter.com/thecolonial) have put together.

**[![](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-cWdT8qq/0/S/kimono-S.png)](http://adron.github.io/junction/)News! News! News! (News…  RSS Feed Reader)**

The idea is that this will provide a quick and easy way to get familiar with Windows 8 dev and the project overall. I’m aiming to eat the Basho blog feed and provide it as key highlights for the application with future abilities around mining other RSS feeds or such and having those fed into a ??  Riak Cluster? Again, everything is open to change, addition or removal! So jump into the project and let me know your thoughts.

Cheers & Happy Hacking!
