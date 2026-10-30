---
title: Excel Development Notes
date: 2009-05-21 10:51:28 +0000
last_modified_at: 2010-09-03 14:43:06 -0700
permalink: /2009/05/21/excel-development-notes/
slug: excel-development-notes
wp_id: 635
original_url: https://compositecode.blog/2009/05/21/excel-development-notes/
categories:
- Unknown Code Ramblings
tags: []
excerpt: I’ve started working on some Excel Development efforts again, primarily focused on accessing Webtrends data. The primary methods that I’ve been using are ODBC and web services. The ODBC connection is based on a proprietary Webtrends ODBC Driver and the web services are the new REST based services the Data Exchange Team I was on …
---

I’ve started working on some Excel Development efforts again, primarily focused on accessing [Webtrends](http://www.webtrends.com) data.  The primary methods that I’ve been using are ODBC and web services.  The ODBC connection is based on a proprietary [Webtrends](http://www.webtrends.com) ODBC Driver and the web services are the new [REST based services](http://product.webtrends.com/RESTWebSvcsBeta/index.html) the Data Exchange Team I was on created.

Performance comparisons for the web services are about 2-6x faster than the ODBC Driver, which really rocks.  Using these connection mechanisms within Excel can sometimes be difficult and trial and error, per the Excel Model that is available for development.  However, once the trial and errors are rung out of the wrinkled framework things fit together rather well.  The following are a few notes I’ve made while building my latest Excel Add-in Project utilizing the above services.

**Getting Started Notes:**

1. Make sure all references for the interop, core office references, etc. are all set to *Copy Local*.  Do this by selecting the reference in Visual Studio, selecting the properties for the reference, and set *Copy Local* to true.
2. When testing, make sure not to install the add in and then try to run the project for the same add-in.  If so uninstall the add-in to run it from visual studio.  If the add-in gets stuck in Excel and executing even when VS is not used, install the component with the MSI installer project and then uninstall it again.  That should get it removed from Excel.  In this scenario the add/remove programs list often doesn’t show the add-in when it hasn’t actually been “installed” but only run from VS.
3. All projects that are referenced for the add-in project must be signed.

That’s just for starters, I’ll have more in the near future with actual example code snippets and more.
