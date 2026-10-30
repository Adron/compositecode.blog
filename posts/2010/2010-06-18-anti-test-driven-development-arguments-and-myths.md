---
title: Anti-Test Driven Development Arguments and Myths
date: 2010-06-18 13:48:00 +0000
last_modified_at: 2014-12-04 09:35:57 -0800
permalink: /2010/06/18/anti-test-driven-development-arguments-and-myths/
slug: anti-test-driven-development-arguments-and-myths
wp_id: 13
original_url: https://compositecode.blog/2010/06/18/anti-test-driven-development-arguments-and-myths/
categories:
- Ideas
- Rants
- Testing
tags:
- myths
- tdd
excerpt: Ok, I have run into the anti-TDD arguments on and off over the years. Generally it comes from two primary sources. The person who doesn’t want to do TDD no matter what, nor test, nor learn anything about the latest and greatest tech, they simply want left in their corner of the universe to code whatever they are coding until they drop dead. Then there is the other individual who is a decent developer, but just has honest hesitations about the style. The developer who has honest hesitations I can understand, can talk to, and can usually at least get a “Well, that sounds reasonable, but I’m still not sure” response. Which is much better than the alternative of disregarding TDD outright. The hope, is that this individual can at least try out TDD and see if it would work for them. Even with the more open minded developer it is still difficult to put TDD into practice. Why? That’s simple, TDD is hard and forces a developer to step back into the basics and really think the problem through first. Most developers (at least currently, maybe it’ll change) have a very “just attack the problem with code” type of response. Often the way to break down problems is taught in computer science 101 level classes, but after that is often lost in all the cramming for math, algorithms, and other such material. But the core fundamental idea of thinking the problem through clearly still needs to be broached. TDD puts that idea forefront in the process by making a developer write the test to verify the problem statement first. With all this stated, there are a few myths that I’d like to bust. These myths are often what cause the first person to cringe away cowardly in their corner of the universe, and causes these hesitations in the second more open minded developer. After busting these myths I’d hope more of the open minded developers can use the power and thinking that TDD encourages. As for the first corner cringing coder, they’re a dying breed and I wouldn’t bet on their recovery.
---

Ok, I have run into the anti-TDD arguments on and off over the years.  Generally it comes from two primary sources.  The person who doesn’t want to do TDD no matter what, nor test, nor learn anything about the latest and greatest tech, they simply want left in their corner of the universe to code whatever they are coding until they drop dead.  Then there is the other individual who is a decent developer, but just has honest hesitations about the style.

The developer who has honest hesitations I can understand, can talk to, and can usually at least get a “Well, that sounds reasonable, but I’m still not sure” response.  Which is much better than the alternative of disregarding TDD outright.  The hope, is that this individual can at least try out TDD and see if it would work for them.

Even with the more open minded developer it is still difficult to put TDD into practice.  Why?  That’s simple, TDD is hard and forces a developer to step back into the basics and really think the problem through first.  Most developers (at least currently, maybe it’ll change) have a very “*just attack the problem with code*” type of response.  Often the way to break down problems is taught in computer science 101 level classes, but after that is often lost in all the cramming for math, algorithms, and other such material.  But the core fundamental idea of thinking the problem through clearly still needs to be broached.  TDD puts that idea forefront in the process by making a developer write the test to verify the problem statement first.

With all this stated, there are a few myths that I’d like to bust.  These myths are often what cause the first person to cringe away cowardly in their corner of the universe, and causes these hesitations in the second more open minded developer.  After busting these myths I’d hope more of the open minded developers can use the power and thinking that TDD encourages.  As for the first corner cringing coder, they’re a dying breed and I wouldn’t bet on their recovery.

**The Myths**

- **MYTH: But I can’t test every single thing that is written, so TDD just isn’t for me.** The reality is, you can’t test every single thing and you shouldn’t.  You should stick to the logic, business process, and other parts of the code.  Don’t worry about the configuration, individual database nodes, or other arbitrary or configuration based bits.  The idea is to make you think through the problem spaces and architecture needed to work through those problem spaces.  So TDD is still something you should try, but don’t try to test every single line of code.  Focus first just getting through the logical, flowing, business related bits of the code you are writing with tests first.  This will get you appropriately experienced with TDD.
- **MYTH: You can’t test against boundaries, that becomes an integration test, so why even mock/stub/fake if I’m not testing the real framework/parts/features?** Again, why worry about testing parts that you know or are not responsible for?  Don’t test the integration parts.  There is a reason QA exists, and defining and testing boundaries is what QA does great.  But you still need to test and confirm that your code works against those.  Mocking or stubbing against that gives you the confidence that your code logic will work against these integration points and also provides you a basis in which to work off of.  If you write the tests first, you also know you’ve thought through these integration points to a fairly thorough level.

Do you have anymore myths that should be burst?  Please feel free to toss a myth or two to burst in the comments, I’d love to hear others input on the matter.
