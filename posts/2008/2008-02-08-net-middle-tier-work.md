---
title: .NET Middle Tier Work
date: 2008-02-08 07:54:26 +0000
last_modified_at: 2008-02-08 07:54:26 +0000
permalink: /2008/02/08/net-middle-tier-work/
slug: net-middle-tier-work
wp_id: 337
original_url: https://compositecode.blog/2008/02/08/net-middle-tier-work/
categories:
- Uncategorized Bits
tags: []
excerpt: A recent topic that has come up in discussion is pieces of middle tier patterns and libraries. I decided I’d enumerate some of the pieces I’ve used in middle tier work throughout my career, then I thought, “why?” Instead, I’m going to scour the net and grab some current libraries, CTPs, patterns and practices, and …
---

A recent topic that has come up in discussion is pieces of middle tier patterns and libraries.  I decided I’d enumerate some of the pieces I’ve used in middle tier work throughout my career, then I thought, “why?”  Instead, I’m going to scour the net and grab some current libraries, CTPs, patterns and practices, and whatever else I could find that helps one build a nice solid middle tier to tie together the front and back ends of an application.

The current big players in the middle tier stack for .NET Technologies are the Windows Communication Foundation (WCF)) and the Enterprise Application Blocks.  These two pieces are huge in the maturing of Microsoft middle tier components.  Some of the secondary players at this point, but should in no way be less important are the various factories (Web Service Software Factory, Smart Client Software Factory), CTPs, libraries, and namely one that could be huge in the near future the ASP.NET MVC.  In this article I’m going to discuss some of the points of use and ideas for use of these various pieces of the Microsoft Technology Stack.

**Middle Tier WCF** (As if it would be an interface or a data storage mechanism?!)  ![Surprise [:O]](/emoticons/emotion-3.gif)

First the WCF, which I’ve been working with well since the beta, absolutely rocks.  Now some of you hard core WCF grognards might think, “[no it doesn’t, its slow](http://msdn2.microsoft.com/en-us/library/bb310550.aspx)” or “all it does it force coding to interfaces” and the list of gripes goes on.  But the list of advantages, like [it might be faster](http://msdn2.microsoft.com/en-us/library/bb310550.aspx) (toward the bottom), far outweighs the list of disadvantages.  In some cases the speed might be an issue, but probably not, and in some cases the coding to interfaces might be an issue for some, but I really hope it isn’t as that is a sign of other significant issues.

The WCF layer is very flexible, being that it is primarily a transport foundation, nothing more.  This opens up the ability for all types of SOA (Services Oriented Architecture) development that isn’t locked to a particular transport mechanism.  As has been written and spoken about before, web services does not equate to SOA, SOA is too high level to sync with the underlying transport mechanism.

The Windows Communication Foundation also works great when utilized merely as a transport mechanism with validation, authentication, and other pieces pushed off into [use with the Policy Injection Application Block](http://blogs.msdn.com/tomholl/archive/2008/01/13/a-follow-up-on-piab-wcf-integration.aspx) ([PIAB](http://msdn2.microsoft.com/en-us/library/bb410104.aspx)).  Also check out the [integration of the PIAB with WCF article](http://msdn.microsoft.com/msdnmag/issues/08/02/PIABWCFBehaviors/default.aspx).  With the validation or other pieces of the middle tier cleanly pushed off into the PIAB we get a better separation of concerns with the obvious increase in maintainable alterations down the road.  The validation layer could change via the way the PIAB access the rules and the WCF layer wouldn’t have to change one bit.

**Middle Tier Enterprise Application Blocks**

Speaking of the [PIAB](http://msdn2.microsoft.com/en-us/library/bb410104.aspx), the latest Enterprise Application Blocks are super sweet.  The new pieces, such as the [PIAB](http://msdn2.microsoft.com/en-us/library/bb410104.aspx), help increase the use of a peripheral components as well as the Enterprise Application Blocks themselves.  In a middle tier environment the business logic and crosscutting concerns make a tangled mess in code.  Maintenance and readability become a serious and expensive concern.  With the PIAB though, the separation of concerns allows a much cleaner break out of the tiers work so that maintenance and readability are exponentially increased, and thus time and costs decrease once implemented.

The crosscutting idea behind the PIAB sits outside of a particular code base and is implemented via a policy.  These policies are acted upon by a pipeline of handlers.  The way these policies are initiated is through mere applied attributes.  This makes the intrusion into other workflow, web services, or other code very minimal but still obvious.  Thus the simplification and separation of concerns into respective code areas causes a decrease in code spaghetti and the resultant nightmares.

So what about the other parts of the current EAB (Enterprise Application Blocks)?  The parts as I remember just off hand are; caching, cryptography, data access, exception handling, logging, security, and validation.  Each of these sections can have huge advantages in building out middle tier operations and assure good separation of concerns within the code base.

**Middle Tier – My Comments, Thoughts, and some other Ideas**

Generally speaking it is fairly easy, once one knows the proper tools and libraries, to get an architecture setup and ready to go for an enterprise application, the catch comes when actual implementation starts.  Knowing good pattern ideas and libraries only really gets the implementation *half baked*.  The need to be able to flex and bend the middle tier, and architecture in general is pivotal to success for a project.  With tools like the PIAB, WCF, and other new tools and such that I’ve mentioned, that flexibility for implementation is available to a project.

**Middle Tier – Last Thoughts and Unit Testing**

Another big plus, that I almost forgot to mention is the ability to test middle tier components.  This is an awesome part of middle tier code areas such as validation, policy injection, etc.  With the front end or even back end database it is somewhat difficult to test in isolation, in the middle tier however it is vastly simpler to turn out some unit test, either via TDD or test after development.  For testability within enterprise application development it is very important that a middle tier is developed with unit tests.  Sometimes this causes slight changes to middle tier architecture, such as interfaces being utilized where they might not have to increase the ability to mock various objects easier, but for the most part any middle tier is exponentially more testable and offers that much more integrity during deployment.  So with the middle tier always built with testing in mind – it’ll work better in the end.

For now, I’m off to write some view code and figure out associated unit tests for that layer, that will then be connecting to my middle tier.  I just wanted to ramble off a few of my thoughts on middle tier development and kind of discuss (yes, sort of like speaking to myself) the latest and greatest in middle tier tools and architecture components.

![Smile [:)]](/emoticons/emotion-1.gif)
