---
title: Why F#, and Why Not Windows
date: 2015-05-10 11:38:57 -0700
last_modified_at: 2015-08-17 18:28:57 -0700
permalink: /2015/05/10/why-f-and-why-not-windows/
slug: why-f-and-why-not-windows
wp_id: 11016
original_url: https://compositecode.blog/2015/05/10/why-f-and-why-not-windows/
categories:
- .NET Bits
tags:
- f#
- functional
- languages
- windows
excerpt: I posted my previous entry and got a few retweets and favorites. One reply came back and made me think, “ah, it might not be obvious why I’d like to have F# on something besides Windows.” Well, here’s a list of why I want to use F# on non-Windows platforms. F# is a good language. I can’t …
---

I posted my previous entry and got a few retweets and favorites. One reply came back and made me think, “ah, it might not be obvious why I’d like to have F# on something besides Windows.” Well, here’s a list of why I want to use F# on non-Windows platforms.

1. F# is a good language. I can’t say the best, since I honestly don’t have enough experience with it or other functional languages to really declare a victory in my opinion. However I’ll be doing some work with Scala, Haskell, and Erlang in the next couple of weeks for testing and use with some upcoming projects.
2. There are only two technology stacks that will let one spin up an actual application on all of these technologies: OS-X Cocoa, Windows, Linux, Android, and iOS. These two tech stacks are .NET and than the Node.js JavaScript stack – with the latter being purely web based. (Yes, some could argue Adobe’s tools or the Java stack, but I’m not going down that route right now, as both are somewhat bloated and convoluted in ways we can go into at some other time)
3. With F# I get a clean functional language that I can build native mobile, tablet, or OS apps and all the web services that I want with two advantages over Node.js. The first is the performance edge and can likely be tuned more anyway. Being paired with [SignalR](http://signalr.net/) one can even get some wicked simple and fast real-time capabilities with minimal code. The second is it takes less F# code to do similar JavaScript things and compute, let me tell you about compute with F#. F# can run things that JavaScript just really can’t measure up to when it comes to compute. But aside from these things, they’re both excellent tools and I wanted to have F# in my tool belt.
4. There’s always the backup plan of just converting to JavaScript too, if I needed that sort of thing. Check out [FunScript](http://funscript.info/).
5. The community around F# is actually pretty cool, there are good, solid, intelligent, and friendly people in that community. Having a good community of people always makes getting into a new language or related tech much better then when the community consists of asshats or jack ass savants.

Other great things that add to the usefulness of F# include [WebSharper](http://www.websharper.com/), [.NET MVC 5 and Web API](http://bloggemdano.blogspot.com/2013/12/a-new-f-aspnet-mvc-5-and-web-api-2.html), [Nancy API](http://nancyfx.org/), [Suave.io](http://suave.io/), and there are others.

So those are the reasons I decided to move forward with F#: solid language, provides a solid technical stack with options, it’s functional and clean with extra compute power, and a kick ass community. Of course F# came from the land of Windows and Softies (that’s short for Microsofties, and I didn’t make that up). But F# was handed over to the open source community and currently moves forward autonomously of Microsoft. By proxy of this event, and other culminating events of late, F# can easily run on operating systems besides Windows. I’m not a fan of Windows, and here’s a few snarky (yet very real) reasons why I don’t even want to mess with Windows (except in the situation where I really do want to or need to use Visual Studio).

1. Windows is still slow. I could go into the reasons, but it tends to build slow, behave slow, be prone to the attention of spammers and such, only in the last X years has it managed security in a half ass decent way, which also leads to slowness, and … oh you get the idea. It’s a slow OS.
2. It’s flippin’ humongous. Now is this really a problem? Not really, but it’s annoying to force fit it in when I’m doing DevOps work or actually attempting to load Windows related images with it. The OS itself is still a nightmare of gigantic proportions compared to spooling up other systems. If one wants to fight with it, that’s great, I don’t really feel a keen desire to fight with it.
3. Linux == Smaller footprint, more features, let’s not bring up security, is actually used on major systems, large scale systems and super-computers. Windows has less than 2% market share in that space. Even Microsoft is decreasing their reliance on Windows, offering oodles of Linux options.
4. Windows doesn’t tend to get, run, or have the bleeding edge tech options built for it. Go look at the open source massive distributed systems applications and other excellent leading platforms and tooling that are leading companies into the future. If Windows is involved at all, it’s often an afterthought. :-/
5. Windows 8 interface. I’m just going to leave that one right there. I like a lot about it, but I’m with Microsoft, even with Windows 10 they’re not trying to push this UI/UX catastrophe any longer.
6. SSH not built in. End of story.

Don’t get me wrong, the tooling on Windows for doing Windows specific development and even doing crud apps with lots of business rules is spectacular. I’d even bet that the .NET ecosystem does a better job, sometimes dramatically better, than the Java ecosystem when it comes to those types of applications. I however, haven’t built these style of applications in a long while. Whenever I do, Windows might be a prime option, but otherwise I’ll stick to the operating systems that get me into the coding faster, sooner, and with less resistance.

Outside of Windows there are a lot of great Microsoft tools and technologies that I’d love to have on non-Windows operating systems. One of those is F#. Another is Visual Studio, which I’m betting will continue to get better and better. I’d like to have C# (which I do with Xamarin and such) and a whole ton of other scaffolding and crud tools and other things that are available. I just prefer them without Windows.

As I often say, to each their own. Mine just isn’t Windows these days.
