---
title: 'Source Control Best Practices List :: Tip o'' The Day'
date: 2008-06-18 12:41:37 -0700
last_modified_at: 2008-06-18 12:41:37 -0700
permalink: /2008/06/18/source-control-best-practices-list-tip-o-the-day/
slug: source-control-best-practices-list-tip-o-the-day
wp_id: 282
original_url: https://compositecode.blog/2008/06/18/source-control-best-practices-list-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: Subversion is in the entry title, but these really apply to just about any source control being used for almost any type of project. 1. Update every time a build is successfully completed on the server to assure you are using the latest and your code still builds locally. 2. Check in as frequently as …
---

Subversion is in the entry title, but these really apply to just about any source control being used for almost any type of project.

1. Update every time a build is successfully completed on the server to assure you are using the latest and your code still builds locally.

2. Check in as frequently as possible.  Every 30 minutes is a good standard.  Make sure to get an update before hand to assure a good build before checking in.

3. When making edits that cause \*.sln file changes make sure to check them in immediately before adding code files or anything else.

4. Keep in mind the virtual “state” and “revision” mind set that source control is built around.  It doesn’t work like the regular file structure, but pretends to act that way.

5. When the build is broken, everyone should STOP checking in code immediately until it is fixed.  If need be everyone should participate in the fix.

6. Do NOT commit (check in) when the build is broken.  This only compounds any prospective issues and possibly drags out the build resolution.

Technorati Tags: [Source Control](http://technorati.com/tags/Source%20Control),[Subversion](http://technorati.com/tags/Subversion),[SourceSafe](http://technorati.com/tags/SourceSafe),[CVS](http://technorati.com/tags/CVS),[Best Practices](http://technorati.com/tags/Best%20Practices)

del.icio.us Tags: [Source Control](http://del.icio.us/popular/Source%20Control),[Subversion](http://del.icio.us/popular/Subversion),[SourceSafe](http://del.icio.us/popular/SourceSafe),[CVS](http://del.icio.us/popular/CVS),[Best Practices](http://del.icio.us/popular/Best%20Practices)
