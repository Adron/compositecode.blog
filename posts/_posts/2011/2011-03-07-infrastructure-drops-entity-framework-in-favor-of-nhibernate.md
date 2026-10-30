---
title: Infrastructure Drops Entity Framework in Favor of NHibernate
date: 2011-03-07 08:40:00 -0800
last_modified_at: 2011-03-07 08:40:00 -0800
permalink: /2011/03/07/infrastructure-drops-entity-framework-in-favor-of-nhibernate/
slug: infrastructure-drops-entity-framework-in-favor-of-nhibernate
wp_id: 2387
original_url: https://compositecode.blog/2011/03/07/infrastructure-drops-entity-framework-in-favor-of-nhibernate/
categories:
- Architecture
- How-to
- Software Projects
tags:
- css
- entity framework
- fluentnhibernate
- infrastructure
- nhibernate
- zen garden
excerpt: I did some searches for tutorials on Entity Framework (EF) + Code First. Most of the tutorials I found involved clicking on some design time view and right clicking to add columns, then clicking and right clicking to generate the code first SQL. It was neat, it was clean, and it was sort of fast. However, it didn’t beat FluentNHibernate in cleanliness. There still ended up being some huge and nasty generated (from the design time) file and some other things that just didn’t sit well with me. With the host of other things that are just now getting developed for EF that have been in NHibernate for ages I’ve decided to yank Entity Framework support for now and just stick to NHibernate + FluentNHibernate. Simply, it just works better and I have more immediate support, feedback, and input into what is available with NHibernate. For Entity Framework nobody really has any of that, one has to wait for the Microsoft machine to move forward on design decisions before something gets dropped either via a proper version or CTP. I’ll stick to the more responsive open source solution, k thx. 🙂 HOWEVER, In the future I do intend to add Entity Framework support, I’m just not spending the time right now. I’d be perfectly happy if someone else wants to do so, just let me know… In other news from the UI from of the Infrastructure Project, I’ve made another decision to use the Zen Garden CSS to setup the original layouts & such. Since it is the UI, I thought that going with something that designers are more familiar with instead of the ASP.NET MVC Themes oddities (which I don’t even really know where they’re hiding those these days) would make things even simpler from that aspect. A clear separation of concerns for devs vs. graphic artists & layout pros. Anyway, that’s all committed and I’ll be building a new template before the end of this week. As always, if you’re interested in adding to the project, or just using it, I’d love any and all feedback.
---

I did some searches for tutorials on Entity Framework (EF) + Code First.  Most of the tutorials I found involved clicking on some design time view and right clicking to add columns, then clicking and right clicking to generate the code first SQL.  It was neat, it was clean, and it was sort of fast.  However, it didn’t beat [FluentNHibernate](http://fluentnhibernate.org/) in cleanliness.  There still ended up being some huge and nasty generated (from the design time) file and some other things that just didn’t sit well with me.  With the host of other things that are just now getting developed for EF that have been in [NHibernate](http://nhforge.org) for ages I’ve decided to yank Entity Framework support for now and just stick to [NHibernate](http://nhforge.org) + [FluentNHibernate](http://fluentnhibernate.org/).  Simply, it just works better and I have more immediate support, feedback, and input into what is available with [NHibernate](http://nhforge.org).  For Entity Framework nobody really has any of that, one has to wait for the Microsoft machine to move forward on design decisions before something gets dropped either via a proper version or CTP.  I’ll stick to the more responsive open source solution, k thx.  🙂

***HOWEVER***, In the future I do intend to add Entity Framework support, I’m just not spending the time right now.  I’d be perfectly happy if someone else wants to do so, just let me know…

In other news from the UI from of the [Infrastructure Project](https://github.com/Adron/infrastructure), I’ve made another decision to use the [Zen Garden CSS](http://www.csszengarden.com/) to setup the original layouts & such.  Since it is the UI, I thought that going with something that designers are more familiar with instead of the ASP.NET MVC Themes oddities (which I don’t even really know where they’re hiding those these days) would make things even simpler from that aspect.  A clear separation of concerns for devs vs. graphic artists & layout pros.

Anyway, that’s all committed and I’ll be building a new template before the end of this week.  As always, if you’re interested in adding to the project, or just using it, I’d love any and all feedback.
