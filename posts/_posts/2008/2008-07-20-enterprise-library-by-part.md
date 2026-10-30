---
title: Enterprise Library by Part
date: 2008-07-20 07:48:45 -0700
last_modified_at: 2008-07-20 07:48:45 -0700
permalink: /2008/07/20/enterprise-library-by-part/
slug: enterprise-library-by-part
wp_id: 262
original_url: https://compositecode.blog/2008/07/20/enterprise-library-by-part/
categories:
- Uncategorized Bits
tags: []
excerpt: 'Sometimes I want to use the enterprise library, but just not all 200+ MB of the thing. So I go about piecing together the pieces I want, by project, into the main solution. This can be troublesome as all the pieces don’t just drop in simply. First Bump in the Road :: GlobalAssemblyInfo.cs The first …'
---

Sometimes I want to use the enterprise library, but just not all 200+ MB of the thing.  So I go about piecing together the pieces I want, by project, into the main solution.  This can be troublesome as all the pieces don’t just drop in simply.

**First Bump in the Road :: GlobalAssemblyInfo.cs**

The first problem I’ve run into this time around was the GlobalAssemblyInfo.cs file wasn’t available.  After fiddling around a minute I realized this needed to be added to the solution at a global level.  The way to do this is to right click and add existing file to the actual Solution.  Unfortunately I had statically added a copy of this file to my projects I was adding and simply re-added those projects with the appropriate file mapping again.  Note to self, “If adding individual blocks from the enterprise library make sure to add the GlobalAssemblyInfo.cs file first and then the individual blocks”.

**Second Bump ::  The “Common” Project**

The common project is used in pretty much every single project in the enterprise library solution.  For some reason when I added all my projects, the common reference went away in numerous projects.  So this was a case of just adding the reference back to several of the projects.  Maybe I shouldn’t add them this way, but regardless, it gets the job done.

So far I’m now up and running, but just wanted to present a searchable note about these bumps I’ve hit.  Once these things are resolved the library blocks are flawless.
