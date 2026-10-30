---
title: Focus, New Focus, More Focus
date: 2010-07-01 07:55:00 -0700
last_modified_at: 2010-07-01 09:14:59 -0700
permalink: /2010/07/01/focus-new-focus-more-focus/
slug: focus-new-focus-more-focus
wp_id: 117
original_url: https://compositecode.blog/2010/07/01/focus-new-focus-more-focus/
categories:
- Unknown Code Ramblings
tags: []
excerpt: Every few months I like to sit down and just figure out what technology I’m going to learn. Since I’ve just wrapped up a project and helped wrap up another project related to Windows Azure it seemed a good time for a review of my technology path. Projects There were two primary projects I just wrapped up. One was a Windows Azure Cloud based application. This one I came in on the tail end to help with some coding and fixes. We’ve officially rolled out the application and deployed it for use within Windows Azure. The Project That Involved Writing Code The application was a fairly straight forward WPF (Windows Presentation Foundation) Application that deploys via ClickOnce Technology and is stored in the Windows Azure BLOB Storage. The cloud aspect of the application also uses…
---

Every few months I like to sit down and just figure out what technology I’m going to learn.  Since I’ve just wrapped up a project and helped wrap up another project related to Windows [Azure](http://www.microsoft.com/windowsazure) it seemed a good time for a review of my technology path.

**Projects**

There were two primary projects I just wrapped up.  One was a Windows Azure Cloud based application.  This one I came in on the tail end to help with some coding and fixes.  We’ve officially rolled out the application and deployed it for use within Windows Azure.

**The Project That Involved Writing Code**

The application was a fairly straight forward WPF (Windows Presentation Foundation) Application that deploys via ClickOnce Technology and is stored in the Windows Azure BLOB Storage.  The cloud aspect of the application also uses [SQL Azure](http://www.microsoft.com/windowsazure/sqlazure/), Dynamic Data Services and Templates with ASP.NET for management.  This application provides the administration of the core data elements while a command line tool provides administration for certain data element generation.  The command line tool actually works against REST style services provided by the ASP.NET Application with WCF (Windows Communication Foundation) hosted REST Web Services.  The web services and the ASP.NET Application are hosted within a Windows [Azure](http://www.microsoft.com/windowsazure) Web Role.  That’s basically the overall architectural pieces without giving away any proprietary parts of what we worked on.  🙂

Overall the application uses a great slice of [Microsoft](http://www.microsoft.com) technology and has been a great experience to help out with.  I really enjoy digging into the latest technology and also really like building applications for the cloud.  I see fewer and fewer reasons for Enterprise or web application to be built outside of a cloud environment.  The reasons really are dwindling.

**The Project That Involved a Lot of Reading and Writing**

I’m glad I have decent writing and comprehension skills because this other project that I’m wrapping up has made extensive use of these skills.  Being able to work on white papers, research, or documents that require heavy research is always fun.  It gives me a chance to sit down and really dive into some of the reasons why things work the way they do.  This adds to my grasp beyond the “just write this code because it works” syndrome.  I’ve actually had time to sit down and discuss the inner workings of the technology.

So far on the project I’ve assisted with writing 3 white papers, and multiple other documents and snippets of code samples, technical parts, and more.  It’s been a lot of learning.  When they’re released I’ll be sure to link them here for anyone interested in the material.

The Next Project

The next project starts today, which [Sound Transit](http://www.soundtransit.org) #545 has me headed for as I finish this entry.  This project is out at Microsoft also.  I’m looking forward to finally getting a v-Dash on campus.

The only thing I can really mention so far is that the project includes parts of the following technology;  ASP.NET, JavaScript, jQuery, and will be web based.  There may be some chance to use ASP.NET MVC, which I’d be really stoked to do.  However, ASP.NET or ASP.NET MVC will be fine by me.  In addition there will be multiple databases and some custom framework engines to work with.

The soft skills side of this project should also be exciting.  It has been about a year plus since I’ve led others directly.  On this project I’ll be doing just that, leading and mentoring some great developers.  I really look forward to stepping back into this type of role again.

Windows Azure and Sketchflow are two things I may not get to use on this gig, but I hope that maybe I can bring their use in at various phases of the project.  I’ll see as time goes forward.

Addendum

What I intend to ramp up on a lot more are the [noSQL](http://en.wikipedia.org/wiki/NoSQL) options and also Java.  I’ve got to become at least familiar with building and deploying a basic project.  It is kind of funny that I say Java, when I really should state that I need to become familiar with Eclipse, or InelliJ for Java Development.  I’m familiar with the language, have even written some snippets and work toward SOLID, which is pretty much the same for Java as C# as what OOP Language.  However I am just not familiar with the IDEs, general stack tools, and libraries that are available for Java.

In addition to noSQL and Java, one of the other bits that I intend to familiarize myself with in these technology platforms is REST based web services.  I really dig REST (literally, figuratively, and technologically), and generally prefer it over SOAP for many things.  Yes, it has its disadvantages but there are more than a few work-arounds.

Last but not least, I hope to at least create a project or two over the next few months to gain some basic familiarity with Erlang and F#.  I want some familiarity with these primarily to figure out easier ways to develop parallel processing applications.  Writing those in C# or Java seem to be an excessive foray of work by comparison, and I’d really like to be able to code up a parallel processing application in short order, versus a long order.  😉

The last bit, and more important to me than the other tidbits here are two projects that I intend to kick off and get running.  One is using the [OneBusAway](http://www.onebusaway.org) services and the other is a website startup style project that I’m not saying a word about yet.  These two projects will include a number of cool technologies and more project entries.  I’m sure I’ll have a goldmine of information derived from these two projects.

So that’s my personal update on projects and such, I’m off to stick my nose back in the proverbial books and start coding.
