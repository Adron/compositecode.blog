---
title: 'Visual SVN & Database Projects in VS.NET :: Tip o'' The Day'
date: 2008-06-17 09:54:51 +0000
last_modified_at: 2008-06-17 09:54:51 +0000
permalink: /2008/06/17/visual-svn-database-projects-in-vs-net-tip-o-the-day/
slug: visual-svn-database-projects-in-vs-net-tip-o-the-day
wp_id: 284
original_url: https://compositecode.blog/2008/06/17/visual-svn-database-projects-in-vs-net-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: In Visual Studio 2008 when using Visual SVN there is a slight issue when using database projects. Visual SVN doesn’t know to check in the database project file itself so it will lose the database project whenever a fresh checkout is done against the repository. So if you are using Visual SVN & VS.NET make …
---

In Visual Studio 2008 when using Visual SVN there is a slight issue when using database projects.  Visual SVN doesn’t know to check in the database project file itself so it will lose the database project whenever a fresh checkout is done against the repository.

So if you are using Visual SVN & VS.NET make sure to go into the actual directory structure and “Add” the database project file into the overall committed solution.

Technorati Tags: [Visual SVN](http://technorati.com/tags/Visual%20SVN),[Visual Studio](http://technorati.com/tags/Visual%20Studio),[VS.NET](http://technorati.com/tags/VS.NET),[VS](http://technorati.com/tags/VS),[Subversion](http://technorati.com/tags/Subversion),[Database Project](http://technorati.com/tags/Database%20Project)

del.icio.us Tags: [Visual SVN](http://del.icio.us/popular/Visual%20SVN),[Visual Studio](http://del.icio.us/popular/Visual%20Studio),[VS.NET](http://del.icio.us/popular/VS.NET),[VS](http://del.icio.us/popular/VS),[Subversion](http://del.icio.us/popular/Subversion),[Database Project](http://del.icio.us/popular/Database%20Project)
