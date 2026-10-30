---
title: Rocking the Code @Webtrends
date: 2009-10-23 00:30:00 +0000
last_modified_at: 2009-10-23 00:30:00 +0000
permalink: /2009/10/23/rocking-the-code-webtrends/
slug: rocking-the-code-webtrends
wp_id: 669
original_url: https://compositecode.blog/2009/10/23/rocking-the-code-webtrends/
categories:
- Uncategorized Bits
tags: []
excerpt: Ok, I have some cool code bits, announcements, and other such things. Some of the code bits will be here "Developer Document", the blog entry for the first example I've written up is here "SDK, ADO.NET DataTable/DataSet, and Code Bits", and then of course the regular sundry of my writings. There has been an on …
---

Ok, I have some cool code bits, announcements, and other such things.  Some of the code bits will be here "[Developer Document](http://developer.webtrends.com/docs/DOC-1182)", the blog entry for the first example I've written up is here "[SDK, ADO.NET DataTable/DataSet, and Code Bits](http://bit.ly/4hbz2l)", and then of course the regular sundry of my writings.

There has been an on and off demand internally for some additions to the [Webtrends](http://www.webtrends.com/) SDK for our DX Web Services offerings, so I added some bits.  The following are a list of the features:

- Map to [DataTable](http://msdn.microsoft.com/en-us/library/system.data.datatable.aspx)/[DataSet](http://msdn.microsoft.com/en-us/library/system.data.dataset.aspx) from [Data Transfer Object](http://en.wikipedia.org/wiki/Data_Transfer_Object).  Alright, I'm going to do a little explaining on this topic.  The [DataTable](http://msdn.microsoft.com/en-us/library/system.data.datatable.aspx) is the standard, years old ADO.NET [DataTable](http://msdn.microsoft.com/en-us/library/system.data.datatable.aspx) that someone can put in with other [DataTable](http://msdn.microsoft.com/en-us/library/system.data.datatable.aspx)s in the [DataSet](http://msdn.microsoft.com/en-us/library/system.data.dataset.aspx).  It basically provides the data pulled from the DX web services in a flattened easy to use [DataTable](http://msdn.microsoft.com/en-us/library/system.data.datatable.aspx) format.
- Profile & Report Listing Factory.  I added a profile and report listing factory for pulling lists from the DX web services.  This seemed like a no brained, it just needed to be available.
- I also refactored the Report Factory Methods to accept a string or Uri Object Parameter to retrieve a report from.  This way, if another tool creates a Uri then it can be used directly instead of parsing it apart only to hand of the values to have the factory parse it back together.
- Last but not least, available in bite size assembly format.  Check out the [Webtrends Developers' Website](http://developer.webtrends.com/docs/DOC-1182) for the bits.
