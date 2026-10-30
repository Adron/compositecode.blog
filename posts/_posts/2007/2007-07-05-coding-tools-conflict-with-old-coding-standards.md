---
title: Coding Tools Conflict With Old Coding Standards
date: 2007-07-05 20:11:00 -0700
last_modified_at: 2007-07-05 20:11:00 -0700
permalink: /2007/07/05/coding-tools-conflict-with-old-coding-standards/
slug: coding-tools-conflict-with-old-coding-standards
wp_id: 458
original_url: https://compositecode.blog/2007/07/05/coding-tools-conflict-with-old-coding-standards/
categories:
- Uncategorized Bits
tags: []
excerpt: 'WARNING: This is not a jab at Lowy‘s Standards, I’m just picking on his stuff. So don’t take it to heart, it’s just code. So I’ve been creating tips o’ the day recently and I started reading through some of Juval Lowy’s C# Coding Standards. I’m a follower of Microsoft’s & the Code Analysis/FxCop …'
---

WARNING:  This is not a jab at [Lowy](http://www.idesign.net/idesign/DesktopDefault.aspx?tabid=5&tabindex=3)‘s Standards, I’m just picking on his stuff.  ![Smile [:)]](/emoticons/emotion-1.gif)  So don’t take it to heart, it’s just code.  ![Stick out tongue [:P]](/emoticons/emotion-4.gif)

So I’ve been creating [tips o’ the day](/blogs/technology__software_development/archive/category/1087.aspx) recently and I started reading through some of [Juval Lowy’s C# Coding Standards](http://www.idesign.net/idesign/download/IDesign%20CSharp%20Coding%20Standard.zip).  I’m a follower of Microsoft’s & the [Code Analysis/FxCop](http://blogs.msdn.com/fxcop/) school of code creators.  I also tend to follow the idea that if it is generated, it should generate to specification with no bad code in there.  Sometimes I let things slide if the code base is really trustworthy, such as the [Enterprise Application Blocks](http://www.microsoft.com/downloads/details.aspx?familyid=4c557c63-708f-4280-8f0c-637481c31718&displaylang=en).  The reasons are long that I go by current code standards, the main reasons boil down to plain, cold, hard cash.

The simple fact is, if you don’t follow current standards it exponentially makes it more difficult to use all of the code generators, shortcuts (like [ReSharper](http://www.jetbrains.com/resharper/)), and the legion of tools that are available for enhancing one’s ability to create good code.  While I was digging through [Lowy](http://www.idesign.net/idesign/DesktopDefault.aspx?tabid=5&tabindex=3)‘s Coding Standards from [IDesign](http://www.idesign.net/) I noticed a few standards that I have issue with.  If for any other reason than it costs more money, because it takes time to make changes to the tools, and thus, time is money.  Every machine one has to touch using standards that deviate from tool usage is lost time.

I know, I know, you’re probably thinking, “Adron!  How insanely obsessive compulsive!”  Yeah, well, I am.  It makes me good at what I do, it also makes me entertaining when I speak, drink, or randomly start conversations.  Let’s take a few examples just to prove my point.

In [Lowy](http://www.idesign.net/idesign/DesktopDefault.aspx?tabid=5&tabindex=3)‘s Standards Document #4 is “*Prefix private member variable with m\_.  Use Pascal casing for the rest of the member variable name following the m\_.*“

**public class SomeClass { private int m\_Number }**

The sample above is all fine and dandy, but seriously, why go old school C++ and use the m\_ when one can just use the current Microsoft P&P [Code Analysis/FxCop](http://blogs.msdn.com/fxcop/) standard of just “number” or “someNumber”?  Because if you use m\_, you have to alter your [ReSharper](http://www.jetbrains.com/resharper/) template and when generating documentation it confuses some tools and in general, and when generating document it appears busy as if to add complexity where none is needed.

#20 is another item that just doesn’t really work.  It states “*All member variables should be declared at the top, with one line seperating them from the properties or methods.*”  This one I don’t have “that” much of a problem with, but there is a serious issue.  If you have a bunch of private members, do you know if you’ve created the appropriate respective public properly getter and setter?  Can you easily use the “prop” macro function that will allow you to generate the private and public property and all that is left is merely filling in the member name, type, and public property name?  Does it simplify what [ReSharper](http://www.jetbrains.com/resharper/) does?  My simple rule of thumb is that you do what makes since for the file.  If you do heavy [ReSharper](http://www.jetbrains.com/resharper/) and gen the properties then do split them as [Lowy](http://www.idesign.net/idesign/DesktopDefault.aspx?tabid=5&tabindex=3) says.  But if you don’t have [ReSharper](http://www.jetbrains.com/resharper/) than be sure to keep the private member with the public property it is for.  It is easier then to find your member and its associative property.

The last one I’m going to harp on is #10.  When doing Agile and TDD there is major emphasis that the tests are documentation.  “Use extensive external documentation for API documentation.” is somewhat counter to a live, actively changing, and readily maintained system.  I tend toward the TDD and tests are documentation approach because of the larger return on the investment developers get from this.  If the product is a software tool for other software purchasers, then yeah, create API documentation.  Otherwise keep a minimal amount of API documentation and test, test, test.

But I must say, in the end, the [Lowy](http://www.idesign.net/idesign/DesktopDefault.aspx?tabid=5&tabindex=3) Standards document is some great stuff.  If you aren’t following extensive standards as he has laid out, his or Microsoft’s or whoever’s, it doesn’t matter.  To create great software one has to have good standards in place.  To have good change management and good process (Agile or otherwise) one needs good standards.

So hats off to Mr. [Lowy](http://www.idesign.net/idesign/DesktopDefault.aspx?tabid=5&tabindex=3), great job.  I just don’t agree 100%, but we wouldn’t be very good developers if we didn’t disagree on things sometimes.  ![Smile [:)]](/emoticons/emotion-1.gif)

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http://adronbhall.com/blogs/technology__software_development/archive/2007/07/06/4933.aspx)](http://www.dotnetkicks.com/kick/?url=http://adronbhall.com/blogs/technology__software_development/archive/2007/07/06/4933.aspx)
