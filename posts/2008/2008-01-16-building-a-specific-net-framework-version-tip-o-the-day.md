---
title: 'Building a Specific .NET Framework Version :: Tip o'' The Day'
date: 2008-01-16 04:33:00 +0000
last_modified_at: 2008-01-16 04:33:00 +0000
permalink: /2008/01/16/building-a-specific-net-framework-version-tip-o-the-day/
slug: building-a-specific-net-framework-version-tip-o-the-day
wp_id: 350
original_url: https://compositecode.blog/2008/01/16/building-a-specific-net-framework-version-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: I was working through changing a web project from building to .NET 3.5 to just .NET 3.0. It was taking a little effort as I removed the .NET 3.5 features. During that time though I had a problem with System.Web and I realized a cool feature that Visual Studio 2008 has built in. When one …
---

I was working through changing a web project from building to .NET 3.5 to just .NET 3.0.  It was taking a little effort as I removed the .NET 3.5 features.  During that time though I had a problem with System.Web and I realized a cool feature that Visual Studio 2008 has built in.

When one selects a pervious build version, and you try to add a reference, the references that aren't available anymore are grayed out in the Add Reference dialog.

![](https://adronhall.smugmug.com/photos/242933017-O.png)
