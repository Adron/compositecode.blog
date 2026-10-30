---
title: WCF, Certificate Issues, and Stackoverflow
date: 2008-10-19 06:50:00 -0700
last_modified_at: 2008-10-19 06:50:00 -0700
permalink: /2008/10/19/wcf-certificate-issues-and-stackoverflow/
slug: wcf-certificate-issues-and-stackoverflow
wp_id: 205
original_url: https://compositecode.blog/2008/10/19/wcf-certificate-issues-and-stackoverflow/
categories:
- Uncategorized Bits
tags: []
excerpt: I've been working on getting certificates setup for development with the WCF Web Services I'm building for the High Ball Project. On a few topics I'm just completely new, like messing with the Certificates, X.509 and SSL and such. I'm getting there, but road blocks are stopping me every once in a while. One of my recent issues …
---

I've been working on getting certificates setup for development with the WCF Web Services I'm building for the [High Ball Project](http://www.codeplex.com/highball).  On a few topics I'm just completely new, like messing with the Certificates, [X.509](/blogs/technology__software_development/page/X509.aspx) and SSL and such.  I'm getting there, but road blocks are stopping me every once in a while.  One of my recent issues was how to view the values that the certificate has.  I searched and searched, for some reason I couldn't find something on MSDN or via Google that would do what I wanted it to do.  In addition to that, the reason I was looking for this application to begin with, I was having issues with getting my web.config settings correct for finding the local certificate I had created with [makecert.exe](/blogs/technology__software_development/page/makecert.aspx).

## Stack Overflow!

That's when it clicked in my head, hey, I should try this [stackoverflow](http://stackoverflow.com) site out!  So I shot over there and posed these two questions and within less than a 24 hr period on the WEEKEND, I got some solid answers.  I gotta say the guys over at [stackoverflow](http://stackoverflow.com) are onto something here!

My first question, "[Cannot find the X.509 Certificate using the following search criteria:…](http://stackoverflow.com/questions/216109/cannot-find-the-x509-certificate-using-the-following-search-criteria)" and second question "[Tool for Viewing X.509 Certificates?](http://stackoverflow.com/questions/216110/tool-for-viewing-x509-certificates)" have two great answers.  So check em' out, and if you aren't signed up with an OpenID get one and go log into the site!  It rocks.  In addition, for you dot netters out there like me, know that the site is built on ASP.NET MVC!  It's solid and FAST!
