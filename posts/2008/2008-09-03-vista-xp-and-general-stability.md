---
title: Vista, XP, and General Stability
date: 2008-09-03 11:10:00 +0000
last_modified_at: 2008-09-03 11:10:00 +0000
permalink: /2008/09/03/vista-xp-and-general-stability/
slug: vista-xp-and-general-stability
wp_id: 239
original_url: https://compositecode.blog/2008/09/03/vista-xp-and-general-stability/
categories:
- Uncategorized Bits
tags: []
excerpt: I'm currently working extensively on a Windows Application that has a heavy Office Excel UI requirement. I've done a fair bit of work on XP with Visual Studio 2008 and a fair bit on Vista with Visual Studio 2008. The following are some of my current rants, about the completely asinine things that have happened …
---

I'm currently working extensively on a Windows Application that has a heavy Office Excel UI requirement.  I've done a fair bit of work on XP with Visual Studio 2008 and a fair bit on Vista with Visual Studio 2008.  The following are some of my current rants, about the completely asinine things that have happened with these operating systems and Visual Studio.  All of them, really have zero to do with Visual Studio, it just happens that it is kind of the messenger stuck in the **middle** of the operating systems and the user interfaces.

> The first issue popped up using Telerik Controls for Windows Apps.  Great controls, awesome graphics, etc, I can't really knock the controls themselves and Telerik has always done great work that I've seen, but something occurred that made me question this.  When I pulled the code base on XP I could see the grid on the design time form and all was great.  I then loaded the same form into design time on Vista and BOOM the grid is dropped down below the form on the space where dialog boxes and things go!  This makes it impossible to use the grids in design time while running Vista.  What gives?
>
> Needless to say, NOT impressed.
>
> Another problem is VB itself.  How the hell does one set an EventHandler object to the event?  In C# one just writes:
>
> ```
> 	 public event EventHandler Shell_Load;	protected virtual void RaiseShellView_Load()	{	EventHandler handlers = Shell_Load;	if (handlers != null)	{	handlers(this, EventArgs.Empty);	}	}
> ```

I've tried a dozen ways to setup the EventHandlers handlers = Shell\_Load; line up.

In VB it always starts displaying a compile error, something about not being able to raise the "Shell\_Load" event, which it I wasn't trying to do.  If anyone knows how to hook that up in VB I'd greatly appreciate a comment.

With all that said, I'm seriously thinking about jumping camps just to find all the reasons to bitch about Java or Ruby or Rails or something.  At least jump camps just to assure myself it really isn't all that sunnier on the other side.

I'm not 100% sold on it, but it also seems the Java camp seems to have a higher percentage of solid developers. Just an observation based on the fact that many .NETters are just now using patterns and other such notions in development that the Java crowd jump started years before it seeped its way over to the .NET world.
