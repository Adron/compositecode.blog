---
title: Austere Recondite
date: 2009-08-07 17:51:37 -0700
last_modified_at: 2009-08-07 17:51:37 -0700
permalink: /2009/08/07/austere-recondite/
slug: austere-recondite
wp_id: 658
original_url: https://compositecode.blog/2009/08/07/austere-recondite/
categories:
- Uncategorized Bits
tags: []
excerpt: Austere Recondite is the official name for my latest one off project. Click the links to check out the definition of each word, my intention being within the definitions themselves. I also intend to post the Silverlight app available via my domain http://www.adronbhall.com to provide a working example of the code in action. With that, I’ll …
---

[Austere](http://dictionary.reference.com/browse/austere) [Recondite](http://dictionary.reference.com/browse/recondite) is the official name for my latest one off project.  Click the links to check out the definition of each word, my intention being within the definitions themselves.  I also intend to post the [Silverlight](http://silverlight.net/) app available via my domain <http://www.adronbhall.com> to provide a working example of the code in action.  With that, I’ll get to rolling.

First I downloaded all the latest bits for [Silverlight 3](http://silverlight.net/) & [Silverlight 3 Toolkit](http://www.codeplex.com/Silverlight), because that?s what I intend for my interface.  Second I rolled straight into creating the solution, of course naming it AustereRecondite.  I added the projects I would need as shown in the image below, and then added the references as shown in the image below that.

![](/images/adronhall.smugmug.com/photos/613839869_XhmBY-S.png)

Red arrows pointing to the [NUnit](http://www.nunit.org/) references I added.  I placed these assemblies into a directory at the same level as the \*.sln file called *3rd Party Assemblies*.

![](/images/adronhall.smugmug.com/photos/613839871_k6F3K-S.png)

Now that I have some framework to start with I will jump right into the old standard TDD approach.
