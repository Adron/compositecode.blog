---
title: Stand Up, SCRUM, or Some Other Name – Pt. 2 – The Wash
date: 2008-07-16 03:12:55 -0700
last_modified_at: 2008-07-16 03:12:55 -0700
permalink: /2008/07/16/stand-up-scrum-or-some-other-name-pt-2-the-wash/
slug: stand-up-scrum-or-some-other-name-pt-2-the-wash
wp_id: 265
original_url: https://compositecode.blog/2008/07/16/stand-up-scrum-or-some-other-name-pt-2-the-wash/
categories:
- Uncategorized Bits
tags: []
excerpt: We scrummed, but then kind of fell of into planning today. Thus no real serious throughput was achieved. We did rectify many questions and clarify what was meant for many of the specifications for the application. It was a very productive day, just not in code productivity. Yesterday Finished clarification of the task list and …
---

We scrummed, but then kind of fell of into planning today.  Thus no real serious throughput was achieved.  We did rectify many questions and clarify what was meant for many of the specifications for the application.  It was a very productive day, just not in code productivity.

**Yesterday**

1. Finished clarification of the task list and working to find the priorities for this iteration.- Met to clarify design goals and functional requirements for new features.

**Today**

1. Finish clarification of the iteration priorities.  Break items down to more specific functional goals.- Met with others on other functional topics to provide consult on my functional task topics.- Started some code clean up, minor change requests, and another refactor effort against some of the existing UI Views.

**Tomorrow**

1. Begin research of the PIAB (Policy Injection Application Block).- Figure out where and how our IoC (Inversion of Control) and DI (Dependency Inversion) architecture points will meet.- Implement the beginnings of a vertical integration with these concepts.

**Road Blocks & Risks**

1. Time constraints have all but eliminated efforts to research or implement a proof around the PIAB, limiting our exception handling, logging, and other cross cutting concerns we need to have in place.- The IoC and DI architecture points have not been clarified.  The more UI work we do without these pieces in place the more tightly coupled, untested, and unworkable refactor efforts will be in the future.- Significant risks include; lack of significant code coverage from unit tests, unclear way for testing the upper layers of Excel/UI functionality.
