---
title: NxBRE Download, Installation, and Setup
date: 2007-02-21 07:59:00 -0800
last_modified_at: 2007-02-21 07:59:00 -0800
permalink: /2007/02/21/nxbre-download-installation-and-setup/
slug: nxbre-download-installation-and-setup
wp_id: 506
original_url: https://compositecode.blog/2007/02/21/nxbre-download-installation-and-setup/
categories:
- Uncategorized Bits
tags: []
excerpt: The NxBRE Application is available at the owner Agile Partner's Website. It is located in a sub path at http://www.agilepartner.net/oss/nxbre/. ; To the left of the page one can download the software package via the download link. The download is provided along with source control by SourceForge.Net. There are three primary packages to download. Click the …
---

The [NxBRE](http://www.agilepartner.net/oss/nxbre/) Application is available at the owner [Agile Partner's Website](http://www.agilepartner.net).  It is located in a sub path at [http://www.agilepartner.net/oss/nxbre/](http://www.agilepartner.net/oss/nxbre/ "http://www.agilepartner.net/oss/nxbre/").  To the left of the page one can download the software package via the download link.  The download is provided along with source control by [SourceForge.Net](http://sourceforge.net/projects/nxbre/).

There are three primary packages to download.  Click the NxBRE download button and you will find the IE-[Console](http://sourceforge.net/project/showfiles.php?group_id=97759&package_id=111399), [Miscellaneous](http://sourceforge.net/project/showfiles.php?group_id=97759&package_id=155961) ([Extra Documentation](http://sourceforge.net/project/showfiles.php?group_id=97759&package_id=155961)), and [NxBRE](http://sourceforge.net/project/showfiles.php?group_id=97759&package_id=104663) Packages available for download.  Personally I'd put each download into one directly.  Unzip each respective file into a respective directly within the single directory the files are placed into.

Once everything was downloaded, unzipped, and placed in their proper order I began opening each project/solution to organize them the way I wanted.  The first Visual Studio Solution I opened is 'RuleEngine' Solution.  This solution has an "Examples" solutions folder with a "SpeedTest" project in it and a "RuleEngine" and "UnitTests" project in the primary root of the solution.  Once these projects are opened do the ole' standard "build without errors" routine.  If you don't have NUnit installed the build will break so make sure to get it downloaded and installed.

One thing that is a pet peeve of mine is to have Visual Studio based unit tests for use against projects.  So with the inclusion of unit tests under the NUnit testing framework included, I started working on converting those to Visual Studio based tests.  These I'll post up in my file share section after I complete it.

For now, with the unit tests needing converted, I'm going to get the project building first.  What I did was remove any links to the NUnit testing framework so the solution could build.  I setup a second project that would store untouched, unedited, NxBRE Solution files.  I renamed the solution file specifcally to RuleEngineU.sln just to make sure that I didn't get confused.

After downloading and installing NUnit I set about making sure the project would build.  I wanted to get it to build to assure that I had a good working model to re-write the unit tests in VS against and also as reference for when I create the actual rules engine that I will be putting into production for the project.

At this point I got everything running, created a second solution copy of NxBRE and started converting the unit tests to Microsoft's Framework.  My progress in altering those will be in a follow up entry, for now, lunch calls out to me!  Grub time.
