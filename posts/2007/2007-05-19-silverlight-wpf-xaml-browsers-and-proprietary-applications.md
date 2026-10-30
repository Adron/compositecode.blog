---
title: Silverlight, WPF, XAML, Browsers, and Proprietary Applications
date: 2007-05-19 18:27:19 +0000
last_modified_at: 2007-05-19 18:27:19 +0000
permalink: /2007/05/19/silverlight-wpf-xaml-browsers-and-proprietary-applications/
slug: silverlight-wpf-xaml-browsers-and-proprietary-applications
wp_id: 483
original_url: https://compositecode.blog/2007/05/19/silverlight-wpf-xaml-browsers-and-proprietary-applications/
categories:
- Uncategorized Bits
tags: []
excerpt: As I sat in the Silverlight session this morning in Vancouver, Washington for the Portland area’s Code Camp I stumbled on some odd thoughts and questions. The more I hear about Silverlight, XAML, and these other things that Microsoft is pushing the less I see this promised code once and start deploying to web or …
---

As I sat in the Silverlight session this morning in Vancouver, Washington for the Portland area’s Code Camp I stumbled on some odd thoughts and questions.  The more I hear about Silverlight, XAML, and these other things that Microsoft is pushing the less I see this promised code once and start deploying to web or windows.

But then of course that was the promise of Java too, which sorta, kinda, in a way works right?  So where is the big picture these days from Microsoft?  Where are they heading with these tools?

Silverlight uses XAML and so does the Windows Presentation Foundation.  The XAML for Silverlight is however a subset of the XAML for the Windows Presentation Foundation. So “maybe” a WPF XAML file will work within a Silverlight application?  Something doesn’t seem to be properly connected with this paradigm.

Instead of a resolution, these tools/foundations just seem to be providing band aids to minor incompatibilities Microsoft proprietary files and tools have with other applications.  Which is nice, but is in no way a real solution to the bigger picture.

…BUT…

as the class went on a major key item was brought up.  Silverlight is multi-browser, multi-OS compatible.  The stuff can run on any system.  So if one actually writes some managed code, compiles it into a dll, and executes it via Silverlight one can execute actual dlls on a Macintosh, Linux, or in Firefox or Safari.  Now that is actually powerful!

With this last covet, which took some time to point out, Silverlight really points out its value.  With .NET on the client, we now have a real programming model, debugging capabilities, and it’s vastly faster than AJAX stuff.

In the end, back to my first point, it still seems like there is a large part of the Java paradigm here, except Microsoft actually has the power, market, and momentum now to push something like Java, except it is wrapped into the whole Silverlight/.NET/ASP/AJAX technology bundles.
