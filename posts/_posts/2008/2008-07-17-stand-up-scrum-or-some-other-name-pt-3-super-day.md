---
title: Stand Up, SCRUM, or Some Other Name – Pt. 3 – Super Day
date: 2008-07-17 04:03:00 -0700
last_modified_at: 2008-07-17 04:03:00 -0700
permalink: /2008/07/17/stand-up-scrum-or-some-other-name-pt-3-super-day/
slug: stand-up-scrum-or-some-other-name-pt-3-super-day
wp_id: 263
original_url: https://compositecode.blog/2008/07/17/stand-up-scrum-or-some-other-name-pt-3-super-day/
categories:
- Uncategorized Bits
tags: []
excerpt: Yesterday was rough going, mainly just because there was so many topics to cover. Today I hope to nail a ton more functional code segments, requirements, and get some unit tests in my work. Yesterday Finished clarification of the task list and working to find the priorities for this iteration. Met to clarify design goals …
---

Yesterday was rough going, mainly just because there was so many topics to cover.  Today I hope to nail a ton more functional code segments, requirements, and get some unit tests in my work.

**Yesterday**

- Finished clarification of the task list and working to find the priorities for this iteration.
- Met to clarify design goals and functional requirements for new features.

**Today**

- Core focus will be on functional requirements and getting the respective unit tests, preferably via TDD for the interface based controller and presenter code.  I’ll be happy with test after for the UI elements since they’re all COM Interop.  i.e.,  today is code day.

**Tomorrow**

- Continue focus on functional specifications and respective tests.

**Road Blocks & Risks**

- Continued – Time constraints have all but eliminated efforts to research or implement a proof around the PIAB, limiting our exception handling, logging, and other cross cutting concerns we need to have in place.
- Continued – The IoC and DI architecture points have not been clarified.  The more UI work we do without these pieces in place the more tightly coupled, untested, and unworkable refactor efforts will be in the future.
- Continued – Significant risks include; lack of significant code coverage from unit tests, unclear way for testing the upper layers of Excel/UI functionality.
