---
title: Unit Testing and Decisions on BAD Data
date: 2007-10-31 18:37:00 +0000
last_modified_at: 2007-10-31 18:37:00 +0000
permalink: /2007/10/31/unit-testing-and-decisions-on-bad-data/
slug: unit-testing-and-decisions-on-bad-data
wp_id: 406
original_url: https://compositecode.blog/2007/10/31/unit-testing-and-decisions-on-bad-data/
categories:
- Uncategorized Bits
tags: []
excerpt: I was having a conversation with a friend about their particular predicament and how they got fussed at for taking time, after being directed to, to write unit tests for someone else’s code. Not only had this individual been directed to do these tests, but after providing estimates based on the idea that the application …
---

I was having a conversation with a friend about their particular predicament and how they got fussed at for taking time, after being directed to, to write unit tests for someone else’s code.  Not only had this individual been directed to do these tests, but after providing estimates based on the idea that the application already was complete, or at least in a testing state.  So with the idea that the application was more complete than it was, unit test writing initiated only to find that the application needed major fixes.

Now correct me if I am wrong, but unit testing is done to find these issues and errors.  Sometimes, most of the time, almost all of time, unit testing is going to take longer than writing the application straight.  But the application will be more solid, have better integrity, the ability for regressions, faster future development, less crashing, better organization, and assuredly better meet the requirements the application is designed to meet.  So when someone takes the time to assure this level of integrity, the last thing a manager or anyone should do is to not realize what is going on when unit tests are being created.  Writing a unit test, especially under a TDD process, is NOT JUST WRITING CODE!

Rant Number 345,251,090,253.

So, to all the managers in the world, please read and focus on what a unit test is.  The reason and purpose of a unit test is vital to getting the results of what is promised from unit testing.

So don’t ask your developers to go and unit test applications that they did not write unless you expect them to go through and literally verify every single “unit” of work that is being performed.  They have to write a “unit test” for each “unit” of work so they must understand each “unit”.  That means, for all practical purposes, learning the entire use case and application in detail.  Remember, if done properly, this will probably take almost as much time as actually writing the application did.  It’ll be worth it, but make sure to have good expectations of what kind of resources and effort this will take!

Writing unit tests after the fact like this is not a good way to go about coding, but sometimes it needs to be done.  It is definitely good to do test driven development instead of the post test development style.

So please stop expecting the market this mythical hype, get rid of the pointy hair boss syndrome, and start dealing with reality.
