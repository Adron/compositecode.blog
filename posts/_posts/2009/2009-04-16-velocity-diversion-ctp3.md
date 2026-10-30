---
title: Velocity Diversion (CTP3)
date: 2009-04-16 06:54:00 -0700
last_modified_at: 2009-04-16 06:54:00 -0700
permalink: /2009/04/16/velocity-diversion-ctp3/
slug: velocity-diversion-ctp3
wp_id: 620
original_url: https://compositecode.blog/2009/04/16/velocity-diversion-ctp3/
categories:
- Uncategorized Bits
tags: []
excerpt: At work I’ve had a little effort put toward Velocity 3 CTP recently. Here’s what I’ve knocked out with the server so far. We’ve been using the CTP 2 of the cache server and it has been solid so far. I hear CTP 3 has quit a few method, namespace, and class name changes. Installation …
---

At work I’ve had a little effort put toward Velocity 3 CTP recently.  Here’s what I’ve knocked out with the server so far.  We’ve been using the CTP 2 of the cache server and it has been solid so far.  I hear CTP 3 has quit a few method, namespace, and class name changes.

**Installation of Velocity CTP3 (Click on any images for a larger view)**

1. Download the parts you need here:  [http://www.microsoft.com/downloads/details.aspx?FamilyId=B24C3708-EEFF-4055-A867-19B5851E7CD2&displaylang=en](http://www.microsoft.com/downloads/details.aspx?FamilyId=B24C3708-EEFF-4055-A867-19B5851E7CD2&displaylang=en "http://www.microsoft.com/downloads/details.aspx?FamilyId=B24C3708-EEFF-4055-A867-19B5851E7CD2&displaylang=en")- ![](/images/adronhall.smugmug.com/photos/513833551_xAeQG-S.png)I setup the configuration during install as such.  I created a folder on my local drive and then shared it, then set that as the location for the cache ConfigStore.sdf and ClusterCconfig.sdf files.  I left the ports as the default 22233 and 22234.  Click on the image to the right to see a larger shot of the configuration window.  Also make sure to have ***ADMINISTRATOR*** rights when you run this install.  If not the installation will not complete correctly.[![](/images/adronhall.smugmug.com/photos/513833557_XeRPd-XL.png)](http://adronhall.smugmug.com/gallery/7920671_mTd9a#513833557_XeRPd-A-LB)- Then I unzipped the velocity\_help.exe file to a location on my drive.  I just placed it right inside my share just to keep everything together, at this point, assuming this won’t cause any disruption to the actual cache server files.- I then downloaded [PowerShell 1.0](http://www.microsoft.com/windowsserver2003/technologies/management/powershell/download.mspx).  This download was rather annoying with the whole “validate” Windows and requirement to have IE.  I am not keen on needing to step out of FireFox or Chrome just to simplify the “validation” of my ***LEGALLY OWNED*** Operation System.  But I digress…- [![](/images/adronhall.smugmug.com/photos/513833564_hEyuy-O.png)](http://adronhall.smugmug.com/gallery/7920671_mTd9a#513833564_hEyuy-A-LB) With the icon placed on the desktop, I right clicked and selected ***Run As Administrator*** (see a theme here?).  It asked me if I wanted to run software from this untrusted publisher?  Type A and press Enter to allow it to always run.- I then set the signed assemblies policy via the command “`Set-ExecutionPolicy -ExecutionPolicy AllSigned`“.- I then started the server with the command “Start-CacheCluster“.- [![](/images/adronhall.smugmug.com/photos/513844548_7mLac-M.png)](http://adronhall.smugmug.com/gallery/7920671_mTd9a#513844548_7mLac-A-LB)I finished this part of the installation off with creation of my first cache with this command “New-Cache FirstCache” where FirstCache can be anything you want to name your cache (not sure about special characters and such, just use some common sense).

**Installation of Cache Client Assemblies**

1. First grab the cache assemblies and place them wherever you’d like.  You’ll just need to make sure they stay together as the two assemblies that are actually used for references reference the other two.  These assemblies are located in the installation directory:  *C:\Program Files\Microsoft Distributed Cache\V1.0* and include the following assemblies; CacheBaseLibrary.dll, ClientLibrary.dll, FabricCommon.dll, and CASBase.dll.
2. Now select CacheBaseLibrary.dll and ClientLibrary.dll as reference dlls by selecting the Browse option in the add references dialog.

…that’s it at this point.  For more just hit up the Velocity API and start coding away.
