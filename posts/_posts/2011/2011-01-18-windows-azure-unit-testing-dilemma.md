---
title: Windows Azure SDK Unit Testing Dilemma — F5DD Plz K Thx Bye
date: 2011-01-18 04:18:32 -0800
last_modified_at: 2011-01-18 16:26:03 -0800
permalink: /2011/01/18/windows-azure-unit-testing-dilemma/
slug: windows-azure-unit-testing-dilemma
wp_id: 2145
original_url: https://compositecode.blog/2011/01/18/windows-azure-unit-testing-dilemma/
categories:
- Azure
- Rants
tags:
- bdd
- behavior driven development
- rest web services
- restful
- software development
- tdd
- test driven development
- unit test
- unit testing
- web services
- windows azure
excerpt: I’m a huge advocate for high quality code. I will admit I don’t always get to write, or am always able to write high quality code. But day in and out I make my best effort at figuring out the best way to write solid, high quality, easy to maintain, easy to read code. Over the last year or so I’ve been working with Windows Azure (Amazon Web Services and other Cloud/Utility Platforms & Infrastructure also). One of the largest gaps that I’ve experienced when working with Windows Azure is the gross disregard for unit testing and especially unit testing in a Test Driven Development style way. The design of the SDK doesn’t make unit testing a high priority, and instead focuses mostly on what one might call F5 & Run Development.
---

I’m a huge advocate for high quality code. I will admit I don’t always get to write, or am always able to write high quality code. But day in and out I make my best effort at figuring out the best way to write solid, high quality, easy to maintain, easy to read code.

Over the last year or so I’ve been working with Windows Azure (Amazon Web Services and other Cloud/Utility Platforms & Infrastructure also). One of the largest gaps that I’ve experienced when working with Windows Azure is the gross disregard for unit testing and especially unit testing in a Test Driven Development style way. The design of the SDK doesn’t make unit testing a high priority, and instead focuses mostly on what one might call F5 & Run Development.

I’ll be the first to stand up and point out why F5 Driven Development (for more on this, check out [Jeff Schumacher](http://codingreflection.wordpress.com/about/)‘s [Blog Entry](http://codingreflection.wordpress.com/2011/01/09/how-f5-driven-development-contributes-to-getting-distracted/)) is the slowest & distracting ways to build high quality code. I’d also be one to admit that F5 Development encourages poor design and development. A developer has to juggle far too many things to waste time hitting F5 every few seconds to assure that the build is running and code changes, additions, or deletions have been made correctly. If a developer disregards running the application when forced to do F5 Development the tendancy is to produce a lot of code, most likely not refactored or tested, during each run of the application. The list of reasons to not develop this way can get long pretty quick. A developer needs to be able to write a test, implement the code, and run the test without a framework launching the development fabric, or worse being forced to not write a test and running code that launches a whole development fabric framework.

Now don’t get me wrong, the development fabric is freaking AWESOME!! It is one of the things that really sets Windows Azure apart from other platforms and infrastructure models that one can develop to. But the level of work and effort makes effectively, cleanly, and intelligently unit testing code against Windows Azure with the development fabric almost impossible.

But with that context, I’m on a search to find some effective ways, with the current SDK limitations and frustrations, to write unit tests and encourage test driven design (TDD) or behaviour driven design (BDD) against Windows Azure, preferably using the SDK.

So far I’ve found the following methods of doing TDD against Windows Azure.

- Don’t use the SDK. The easiest way to go TDD or BDD against Windows Azure and not being tightly bound to the SDK & Development Fabric is to ignore the SDK altogether and use regular service calls against the Windows Azure service end points. The problem with this however, is that it basically requires one rewrite all the things that the SDK wraps (albeit with better design principles). This is very time consuming but truly gives one absolute control over what they’re writing and also releases one from the issues/nuances that the Windows Azure SDK (1.3 comes to mind) has had.
- Abstract, abstract, and abstract with a lock of stubbing, mocking, more stubbing, and some more abstractions underneath all of that to make sure the development fabric doesn’t kick off every time the tests are run.  I don’t want to abstract something just to fake, stub, or mock it.  The level of indirection needed gets a bit absurd because of the design issues with the SDK.  The big problem with this design process to move forward with TDD and BDD is that it requires the SDK to basically be rewritten as a whole virtual stubbed, faked, and mocked layer. Reminds me of many of the reasons the Entity Framework is so difficult to work with for testing (has the EF been cleaned up, opened up, and those nasty sealed classes removed yet??)

Now I’ll admit, sometimes I miss the obvious things and maybe there is a magic “build tests real easy right here” button for Windows Azure, but I haven’t found it.  I’d love to hear what else people are doing to enable good design principles around Windows Azure’s SDK. Any thoughts, ideas, or things I ought to try would be absolutely great – I’d love to read them. Please do comment!
