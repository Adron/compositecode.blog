---
title: HighBall Part Duex (#5) Oh Dear, Tests!
date: 2009-04-13 15:31:20 -0700
last_modified_at: 2009-04-13 15:31:20 -0700
permalink: /2009/04/13/highball-part-duex-5-oh-dear-tests/
slug: highball-part-duex-5-oh-dear-tests
wp_id: 619
original_url: https://compositecode.blog/2009/04/13/highball-part-duex-5-oh-dear-tests/
categories:
- Uncategorized Bits
tags: []
excerpt: Ok, I got this far, marked up some xaml, and got the boot strappers boot strapping some views view their respective presenters within the modules. Yeah! But really, what happens if I move forward now? Without tests I get myself into trouble. I could just move forward, but I?d have no regression, no ability to …
---

Ok, I got this far, marked up some xaml, and got the boot strappers boot strapping some views view their respective presenters within the modules.  Yeah!

But really, what happens if I move forward now?  Without tests I get myself into trouble.  I could just move forward, but I?d have no regression, no ability to cleanly refactor, and no ability to know if I broke things that already work!  So I?m heading into the world of unit tests and am going to figure out how to make future endeavors more TDD (or TAD ? Test After Development?).  Either way, this thing needs some tests before I bluntly slam into the next steps.

First off, make sure you have the appropriate equipment for the job.  The [Composite Application Guidance for WPF and Silverlight ? February 2009](http://www.microsoft.com/downloads/details.aspx?FamilyID=fa07e1ce-ca3f-4b9b-a21b-e3fa10d013dd&DisplayLang=en) link has the goods you?ll need.  The specific links are as follows;

- [Visual Studio 2008 SDK 1.1](http://www.microsoft.com/downloads/details.aspx?FamilyID=59ec6ec3-4273-48a3-ba25-dc925a45584d&DisplayLang=en)
- [Binaries for white](http://download.codeplex.com/Project/Download/FileDownload.aspx?ProjectName=white&DownloadId=43567&FileTime=128656758841700000&Build=14954) (they have source too, it is an open source project)
- [Silverlight Unit Test Framework](http://code.msdn.microsoft.com/silverlightut)

Install the SDK, then put those assemblies somewhere handy.  I nabbed a bit of [reference from Justin Angel](http://silverlight.net/blogs/justinangel/archive/2009/02/25/silverlight-unit-testing-rhinomocks-unity-and-resharper.aspx) at this juncture.  He has a great write up on getting these parts setup with the Silverlight Unit Testing Framework, [Rhinomocks](http://ayende.com/projects/rhino-mocks.aspx), Unity, and [ReSharper](http://www.jetbrains.com/resharper/index.html) ? exactly along the lines of what I wanted.  After a quick perusal of his blog entry I tore through a quick setup and first tests.

***?first tests.***

***?here?s the assemblies:***

***D:\Machine Load\Visual Studio 2008\All the Parts for UI Unit Tests w Silverlight and WPF\White-bin-11-9-2008***

***D:\Machine Load\Visual Studio 2008\All the Parts for UI Unit Tests w Silverlight and WPF\Unit test framework\Unit test framework***

Reference Posts:

- [Unit Testing with Silverlight 2](http://www.jeff.wilcox.name/2008/03/silverlight2-unit-testing/) ? [Jeff Wilcox](http://www.jeff.wilcox.name/)
- [Silverlight Unit Testing, Rhinomocks, Unity and ReSharper](http://silverlight.net/blogs/justinangel/archive/2009/02/25/silverlight-unit-testing-rhinomocks-unity-and-resharper.aspx) ? [Justin Angel](http://silverlight.net/blogs/justinangel/default.aspx)
