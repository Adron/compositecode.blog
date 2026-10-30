---
title: Windows Vista Developer Installation Notes
date: 2007-04-20 10:56:20 +0000
last_modified_at: 2007-04-20 10:56:20 +0000
permalink: /2007/04/20/windows-vista-developer-installation-notes/
slug: windows-vista-developer-installation-notes
wp_id: 499
original_url: https://compositecode.blog/2007/04/20/windows-vista-developer-installation-notes/
categories:
- Uncategorized Bits
tags: []
excerpt: Well I’m on round two of installing Windows Vista. The main reason being that McAffee Anti-Virus, if the wrong version, which I thought I purchased the right one, blows the hell out of the OS. I had memory messages displaying and this and that and this and that… blagh blagh blagh. Needless to say I …
---

Well I’m on round two of installing Windows Vista.  The main reason being that McAffee Anti-Virus, if the wrong version, which I thought I purchased the right one, blows the hell out of the OS.   I had memory messages displaying and this and that and this and that… blagh blagh blagh.

Needless to say I uninstalled it and it wasn’t all gone, it instead continued to act as a virus itself causing havoc with the memory.  So reload I did.

Now with a clean load of Vista I went about troubleshooting some other issues I’ve had.  Nothing out of the ordinary with a major operating system upgrade.  The first thing was the attempt at installing the correct components with IIS 7 so that I could then install the development tools I needed.

One of the problems I ran into was the inability to install reporting services.  So after a quick internet search via Google I came up with some answers in this [kb article](http://support.microsoft.com/kb/920201). This [same issue](http://blogs.msdn.com/williaml/archive/2006/09/22/767255.aspx) is brought up over on [William Li’s Blog](http://blogs.msdn.com/williaml/default.aspx).  He has the list of required IIS parts along with some SP2 notes and errata.

After I got it installed I couldn’t login to the blasted server.  I then went searching in regards to that and found a blog entry by [Robert Burke](http://blogs.msdn.com/robburke/default.aspx) pointing out that [SP2 is required for SQL Server 2005 to work under Vista](http://blogs.msdn.com/robburke/archive/2007/02/20/sql-server-2005-sp2-released-and-is-vista-ready.aspx).

Now that I have been through the installation strangeness that SQL Server 2005 has put before me I am going to embark on Team Foundation Server (Hopefully) and finally Visual Studio Team Developer Edition!  So stay tuned!
