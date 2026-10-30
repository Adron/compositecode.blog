---
title: OMFG, Please Make the Tests Work FIRST!
date: 2009-09-14 06:51:00 +0000
last_modified_at: 2009-09-14 06:51:00 +0000
permalink: /2009/09/14/omfg-please-make-the-tests-work-first/
slug: omfg-please-make-the-tests-work-first
wp_id: 82
original_url: https://compositecode.blog/2009/09/14/omfg-please-make-the-tests-work-first/
categories:
- Uncategorized Bits
tags: []
excerpt: Alright Mr & Ms Developer. This hasn't happened in a while, since most of my work as of late has been green field (i.e. brand new development). But in the past, oh boy have I gotten some pure crap. I am a bit arnery today, so just bare with me, I need to rant a …
---

Alright Mr & Ms Developer.  This hasn't happened in a while, since most of my work as of late has been green field (i.e. brand new development).  But in the past, oh boy have I gotten some pure crap.  I am a bit arnery today, so just bare with me, I need to rant a bit.

When I am handed code to fix, maintain, alter, or read for any reason I would love to have [unit tests](/blogs/technology__software_development/post/2007/06/20/Software-Development-Testing-Tip-O-The-Day.aspx) come along with it.  If someone then promises to provide unit tests for the code they are writing that is being handed off to me, I expect the unit tests to run, execute isolated, and throw green lights across the board.  However there are a billion different things I run into all the time that frustrate me to no end.  If you promise me unit tests, do NOT . . .

*[RANT ON]*

***DO NOT*** give me unit tests that take 13 steps to setup, fake data INSERTs against an un-configured or even pre-configured database.  That is NOT isolated and it makes them almost entirely useless to me.  It might be great for your own personal testing, but it doesn't help me understand the isolated unit of work, the separation of concern, or anything else about the actual code.

***DO NOT*** give me unit tests that outright fail immediately.  If they all fail that means you have NOT finished your work.  It means your code doesn't work.  Please, make the tests work right, make the code work right before passing the buck.  Note:  I said ***please! 🙂***

***DO NOT*** write a unit test for something that checks the length of a string when you need to check the content of the string.  Don't check that something is a number when the method adds two numbers, instead check to see if the numbers are aggregated correctly.

***DO NOT*** tell me you have 100% code coverage and then hand me tests that basically asset that a mocked method executes on an object.  OF COURSE THE METHOD EXECUTES, YOU ARE MOCKING IT!!!

***DO NOT*** give me unit tests that test so far across boundaries that isolation is lost by so many degrees it would take many minutes, if not hours, to figure out what the test doesn't work.

*[Rant Off]*

In all honesty I would rather get code and just be told the truth;  *?X tests do not work anymore?, ?I could not figure out a way to test this so I did this dumb partial test thing?, or simply ?I was screwing around so I didn?t get full coverage, to make management shush up I did a quick assert fake to get the rest of the coverage?.* I'm a developer too, I will understand and probably have no problem at all that something is not completely done, partially done, or you hit a stumbling block.  I do it all the time, I also make a point to lay it out the way it is.  No point in beating around the bush.

Keep in mind, if your management thinks you need to slave away and be forced to lie about things, you can probably go work somewhere else within a few weeks.  Even in this crappy market there is barely any reason to allow bad management to treat develops like crap or to mismanage projects.  So don't take the bull and just make sure to keep things on the up and up with your fellow developers.  i.e. ***DON'T*** lie about your unit tests!  Cheers!
