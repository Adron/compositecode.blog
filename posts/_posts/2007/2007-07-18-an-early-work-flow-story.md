---
title: An Early Work Flow Story
date: 2007-07-18 18:22:53 -0700
last_modified_at: 2007-07-18 18:22:53 -0700
permalink: /2007/07/18/an-early-work-flow-story/
slug: an-early-work-flow-story
wp_id: 453
original_url: https://compositecode.blog/2007/07/18/an-early-work-flow-story/
categories:
- Uncategorized Bits
tags: []
excerpt: October 2003 I sat one day, arriving a few minutes early, at 7:48am. I’d spent the last few days tearing through tons of code and schema designs. I finally was at a point where the product was working. I looked across to my fellow associates’ seats and smiled. Today I was proud that I would have …
---

October 2003

I sat one day, arriving a few minutes early, at 7:48am.  I’d spent the last few days tearing through tons of code and schema designs.  I finally was at a point where the product was working.  I looked across to my fellow associates’ seats and smiled.  Today I was proud that I would have this to present to them once they arrived.  My boss had not arrived yet either, but I was going to be very stoked to present this to him.  Just a few days earlier I had been reprimanded for not cranking down hard enough and getting this done.

I’m going to roll this story back to when it all began.  I had just finished up assisting with another major software creation application and a new assignment had come up.  The company had been dumping large cash on paper trail work flows for years. With technology where it was, that was just not needed anymore.  What we needed was a good clean, easy to store, easy to track, easy to report on form processing work flow application.

With that boss man and I met to gather some requirements that this application needed to cover.  I needed to store the forms, I needed to be able to process and recall forms at any point in a workflow process, and I needed these to be able to be signed off over long segments of time.  I look back and think, “wow, WCF, WPF, and WF are all based entirely around this type of enterprise software application”.  Of course, the technology that was up for use was ASP.NET 1.0, not even 1.1 yet.  We had some Infragistics Controls and of course SQL Server 2000.  There was also the user repository that had been created within SQL Server 2000 to compensate for Windows NT 4.0’s lack of metadata storage on users.  The boss man and I sat down and started ironing out the technology path, ideas, and where we wanted to end up with this application.

After the meeting for the initial layout of the applications purpose I set about laying down some concrete database schema ideas, application design plans, and creating a scope list of exactly what I was going to create.  I also did some meager price and feature set comparison of tools that where on the market at the time.  Nothing really played out to do what we wanted to do at the price point we where willing to pay.  Thus I started designing and coding.

My first rendition was placing actual documents, image documents, and some other random files in the database repository, but as time went on this wasn’t going to well.  It seemed like the logical thing to do, make a document, get the signature, put it in the repository, keep track of it.  There where however all sorts of problems with the integrity of the documents and that problem didn’t even touch on the issue of when one got to the point of a few hundred thousand documents in the database server.  It got real nasty real fast.  Fortunately this didn’t take that long and back to the drawing board I went.

My next rendition, after a good discussion with the boss man, led me into the realm of dealing with XML documents, and keeping the XML stored that had the data separately, and the XSL visual markup separate from that.  I ended up with the visual markup, the actual xml form document, and then a signed copy with just the data in it.  The forms documents along with their respective visual markup where historically kept at each change so that each could be used to display any signed copy with data in it at any time.  It was a grand idea.  The only problem was designing the nasty XML and getting all those forms transferred into the system.  The only tools I had to do this with was Visual Studio and notepad.  We didn’t have anything cool like XML Spy so I dove into an endeavor to copy the various word, excel, pdf, and other documents into the XML forms schema that I had created.

After a diligent month, I was able to get all the existing documents, and build an interface for adding future documents.  Finally, I was done.  I did some testing.  This was before unit testing existed to me, so I went clicking away like a mad man.  Hoping to iron out any issues that might come up.  A few things where busted, but I got those wrapped ASAP!  Thus we’re back to the beginning of this short story.

I sat, pondering all of this, and just surfing some information and development sites.  This app was wrapped.  Finally I heard him greet a cohort out in the hallway.  He breached the door and I pounced with my great news!  “Hey Boss Man!  I’m done!”, I blurted out with exuberance.  He looked at me with a grin and stated, “it’s about damn time!”  We both kind of laughed and he came in to check out the app.  After a thorough display of the features and the interface tool for making documents, he seemed content.  He gave me one of those boss man smiles and walked back into the main office space.

Later that day he told me the presentation with the boss’s boss man went well.  They where happy with the tool.  Later that day he proffered mixed drinks at his house for the whole dev gang (He had a penchant for creating mixed drinks and had a whole stocked bar at his house).  At that point, I knew for sure, that the application was done!

![Big Smile [:D]](/emoticons/emotion-2.gif)
