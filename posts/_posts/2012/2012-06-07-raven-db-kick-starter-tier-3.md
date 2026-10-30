---
title: Raven DB, A Kick Starter using Tier 3 IaaS
date: 2012-06-07 17:37:23 -0700
last_modified_at: 2012-06-07 17:37:23 -0700
permalink: /2012/06/07/raven-db-kick-starter-tier-3/
slug: raven-db-kick-starter-tier-3
wp_id: 5702
original_url: https://compositecode.blog/2012/06/07/raven-db-kick-starter-tier-3/
categories:
- .NET Bits
- Architecture
- How-to
tags:
- big data
- database
- document database
- document store
- nosql
- raven
- raven database
- raven db
- tier 3
excerpt: I’m putting together a pretty sweet little application. It does some basic things that are slowly but surely expanding to cover some interesting distributed cloud computing business cases. But today I’m going to dive into my Raven DB experience. The idea is that Raven DB will act as the data repository for a set of …
---

I’m putting together a pretty sweet little application. It does some basic things that are slowly but surely expanding to cover some interesting distributed cloud computing business cases. But today I’m going to dive into my Raven DB experience. The idea is that Raven DB will act as the data repository for a set of API web services (that seems kind of obvious, I state the obvious sometimes).

The first thing we need is a server instance to get our initial node up and running. You can use whatever service, virtualization tools, or a physical server if you want. I’m going to use Tier 3’s Services in my example, so just extrapolate for your own situation.

First I’ve logged in to the Tier 3 Control Site and am going to create a server instance.

## Building the Tier 3 Node for Raven DB

[![Creating the Server Instance (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-NJPFrSJ/0/L/Building-Macross-001-L.jpg "Creating the Server Instance (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1887883570&k=NJPFrSJ&lb=1&s=O)

*Creating the Server Instance (Click for full size image)*

Next step is to assign resources. Since this is just a single Raven DB node, and I won’t have it under heavy load, I’ve minimized the resources. This is more of a *developers install*, but it could easily be a production deploy, just allocate more resources as needed. Also note, I’ve added 50 GB of storage to this particular instance.

[![Setting Resources (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-xQKKQgL/0/L/Building-Macross-002jpg-L.jpg "Setting Resources (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1887883571&k=xQKKQgL&lb=1&s=O)

*Setting Resources (Click for full size image)*

Now that we’ve set these, click next and on the next screen click on *server task*. Here add the public IP option and select the following services to open their ports.

[![Setting up a Public IP and the respective ports/services (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-GHMxfGm/0/L/Building-Macross-003jpg-L.jpg "Setting up a Public IP and the respective ports/services (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1887883592&k=GHMxfGm&lb=1&s=O)

*Setting up a Public IP and the respective ports/services (Click for full size image)*

The task will display once added as an item on the create server view. Once that is done, click *create server* so the server build out will start.

[![Creating the Server (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-RCwPZZ8/0/M/Building-Macross-004-M.jpg "Creating the Server (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1887883603&k=RCwPZZ8&lb=1&s=O)

*Creating the Server (Click for full size image)*

Now log in with RDP to start setting up the server in preparation of loading Raven DB. The first thing you’ll want to do is go ahead and get Windows Update turned on. My preference is to just turn it on and get every update that is available. Once that is done, make sure to get the latest .NET 4 download from Windows Update too.

[![Getting Windows Update Turned On (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-BjgFZNt/0/S/Building-Macross-006-S.jpg "Getting Windows Update Turned On (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1888099726&k=BjgFZNt&lb=1&s=O)

*Getting Windows Update Turned On (Click for full size image)*

Once all of the updates are finished and .NET 4 is installed we’ll get down to the business of getting Raven DB Installed. In this specific example I’ll be installing the Raven DB as a windows service, it however can be installed under IIS so there are many other options depending on how you need it installed.

## Installing Raven DB

To get the software to install, navigate over to the [Raven DB](http://ravendb.net/) site at <http://ravendb.net/> from the new instance we’ve just spun up. Click on the Download button and you’ll find the latest build over on the right hand side. Click to download the latest software package to a preferred location on the system.

[![Raven DB - Open Source 2nd Generation Document DB (Click to navigate to the site)](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-x6z6845/0/S/building-sdf-1-007-S.jpg "Raven DB - Open Source 2nd Generation Document DB (Click to navigate to the site)")](http://ravendb.net/)

*Raven DB – Open Source 2nd Generation Document DB (Click to navigate to the site)*

Once you’ve downloaded it (I’ve put my download in the root R:\ partition I created) unzip it into a directory (I’ve just unzipped it here into R:\ to make the paths easy to find, feel free to put it anywhere you would prefer. In our Tier 3 environment the R drive is on a higher speed, thus higher IOP drive system, thus the abilities exceed your standard EBS/AMI or S3 style storage mechanisms.).

[![Saving the Raven DB Download (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-ch4H3bC/0/S/building-sdf-1-008-S.jpg "Saving the Raven DB Download (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1891883814&k=ch4H3bC&lb=1&s=O)

*Saving the Raven DB Download (Click for full size image)*

[![Saving to R:/ (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-t5wt3kH/0/S/building-sdf-1-009-S.jpg "Saving to R:/ (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1891886053&k=t5wt3kH&lb=1&s=O)

*Saving to R:/ (Click for full size image)*

At this point, open a command prompt to install Raven DB as a service. Navigate to the drive and folder location you’ve saved the file to. Below I displayed a list of the folder and files in the structure.

[![CLI actions (click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-GHnGTbk/0/M/building-sdf-1-010jpg-M.jpg "CLI actions (click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1891889652&k=GHnGTbk&lb=1&s=O)

*CLI actions (click for full size image)*

Once you’re in the path of the Raven.Server.exe file then run a slash install on it to get a Windows Service of the Raven DB running.

[![Raven DB Installation results (click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-CQ5rb6K/0/M/raven-db-001jpg-M.jpg "Raven DB Installation results (click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1892316895&k=CQ5rb6K&lb=1&s=O)

*Raven DB Installation results (click for full size image)*

To verify that it is up and running (which if you’ve gotten these results, you can rest assured it is, but I always like to just see the services icon) check out the services MMC.

[![Launching services (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-NVrfZFJ/0/S/raven-db-002-S.jpg "Launching services (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1892195710&k=NVrfZFJ&lb=1&s=O)

*Launching services (Click for full size image)*

There it is running…

Now, you’re not complete yet. There are a few other things you may want to take note of to be sure you’re up and running in every way you need to be.

The management and http transport for Raven DB is done on port 8080. So you’ll have to open that port if you want to connect to the services of the database externally. On windows, open up the Windows Firewall. Right click on the Inbound Rules and click Add Rule.

[![Select Port (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-bFvJbp5/0/M/raven-db-010-M.jpg "Select Port (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1892378969&k=bFvJbp5&lb=1&s=M)

*Select Port (Click for full size image)*

[![Select the Raven.Server.exe (click to see full size)](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-82xjzMR/0/M/raven-db-007jpg-M.jpg "Select the Raven.Server.exe (click to see full size)")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1892337574&k=82xjzMR&lb=1&s=O)

*Select the Raven.Server.exe (click to see full size)*

[![Inbound Rule (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-JRpMCKJ/0/M/raven-db-011-M.jpg "Inbound Rule (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1892382368&k=JRpMCKJ&lb=1&s=O)

*Inbound Rule (Click for full size image)*

[![Open up however needed. (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-GmW257R/0/M/raven-db-012-M.jpg "Open up however needed. (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1892394005&k=GmW257R&lb=1&s=O)

*Open up however needed. (Click for full size image)*

[![Public Private etc. (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-GmW257R/0/M/raven-db-012-M.jpg "Public Private etc. (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1892394005&k=GmW257R&lb=1&s=O)

*Public Private etc. (Click for full size image)*

Enter a name and description on the next wizard dialog screen and click on Finish.

[![Displayed active firewall rule (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-VzKcjQs/0/M/raven-db-009-M.jpg "Displayed active firewall rule (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1892337583&k=VzKcjQs&lb=1&s=O)

*Displayed active firewall rule (Click for full size image)*

Now if you navigate to the IP of the instance with port 8080 you’ll be able to load the management portal for Raven DB and verify it is running and you have remote access.

[![Raven DB Management Screen](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-BKFWW5C/0/M/raven-db-013-M.jpg "Raven DB Management Screen")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1892480228&k=BKFWW5C&lb=1&s=O)

*Raven DB Management Screen (Click for full size image)*

At this point, if you’d like more evidence of success, click on the “Create Sample Data” button and the management screen will generate some data.

[![Raven DB Management console with data (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/i-56XHkvM/0/M/raven-db-014-M.jpg "Raven DB Management console with data (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Tier-3-IaaS/23377224_v76B8T#!i=1892480230&k=56XHkvM&lb=1&s=O)

*Raven DB Management console with data (Click for full size image)*

At this point you have a live Raven DB instance up and running in Tier 3. Next step is to break out and add nodes for better data integrity, etc.

**Summary**

In this write up I’ve shown a short how-to on installing and getting Raven DB ready for use on Windows Server 2008 in Tier 3’s Enterprise Cloud environment. In the very near future I’ll broach the topics of big data with Raven DB, and other databases like Riak and their usage in a cloud environment like Tier 3. Thanks for reading, cheers!
