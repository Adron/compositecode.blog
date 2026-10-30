---
title: 'Under the Reigns of Security :: Tip O'' The Day'
date: 2008-06-05 08:01:00 -0700
last_modified_at: 2008-06-05 08:01:00 -0700
permalink: /2008/06/05/under-the-reigns-of-security-tip-o-the-day/
slug: under-the-reigns-of-security-tip-o-the-day
wp_id: 292
original_url: https://compositecode.blog/2008/06/05/under-the-reigns-of-security-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: Often when developing software the software developers just work on machines that are administrators in every aspect. Very little consideration is given to this, as developers usually know what they're doing. In a larger corporate environment though we developers often end up pushed into a corner with security considerations. Even at smaller companies sometimes they …
---

Often when developing software the software developers just work on machines that are administrators in every aspect.  Very little consideration is given to this, as developers usually know what they're doing.  In a larger corporate environment though we developers often end up pushed into a corner with security considerations.  Even at smaller companies sometimes they have things that need to be locked away from the developers.  In those cases, which recent scenarios have made me think of again, I've worked in security paradigms as follows.

The first thing you want to do is to setup a domain (of course, this is the Microsoftie world I live in).  With a domain you can really lock things down and still maintain some autonomy for the individual systems in the network if need be.

The second thing is to setup a box and assure admin access before adding one self to the domain.  Then after the local account is setup log off and add yourself to the domain.

Once that is done use the limited domain account to do work that requires membership to the domain (like Outlook, pushed software, etc) but use the local admin account to do all installations and other such things.

This way you work with a much higher level of security, you prevent a LOT of viruses, bugs, spyware, and other such things that commonly plague a user, but still all the benefits of admin are right there via the command prompt or "run as" on the context (right click) menus.

Technorati Tags: [tip o' the day](http://technorati.com/tags/tip%20o'%20the%20day),[security](http://technorati.com/tags/security)

del.icio.us Tags: [tip o' the day](http://del.icio.us/popular/tip%20o'%20the%20day),[security](http://del.icio.us/popular/security)
