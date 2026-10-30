---
title: Databases, Security, and the Chicken or the Egg and Application Architecture
date: 2006-12-20 13:21:55 +0000
last_modified_at: 2006-12-20 13:21:55 +0000
permalink: /2006/12/20/databases-security-and-the-chicken-or-the-egg-and-application-architecture/
slug: databases-security-and-the-chicken-or-the-egg-and-application-architecture
wp_id: 520
original_url: https://compositecode.blog/2006/12/20/databases-security-and-the-chicken-or-the-egg-and-application-architecture/
categories:
- Uncategorized Bits
tags: []
excerpt: Some math could be said to be derived from such things as databases, security, chickens, and eggs and their prioritization. But really, cryptic ramblings aside. What are really the first things that need done on a software project. There is the architecture which of course needs done, but before that, pieces need in place. One …
---

Some math could be said to be derived from such things as databases, security, chickens, and eggs and their prioritization.

But really, cryptic ramblings aside.  What are really the first things that need done on a software project.  There is the architecture which of course needs done, but before that, pieces need in place.  One piece of information that obviously needs to go first is some idea that a business process exists and needs modeled.  A business process also being a “need” or whatever one wants to call it.  But even BEFORE the needs of the business process are conerned one needs to consider one thing that is even more important to the business.

The security of the business, the roles of users within that security context, and how these things need broken down into logical units of organization.  If a business really doesn’t care and does not want security then great, just pass on the whole notion.

Security is so key though, that if held off until after the coding starts then there will be massive costs in time and effort along with cold hard cash in paying to get it fixed.  Waiting to fix security post project start is far worse than any other aspect of an application having scope creep within a domain.  The multiple in time consumed is massive.

So the next time one is on a project that doesn’t have the security model fleshed out, but is discussing “we’ll do it after the fact”, make changes immediately, be ready for a long battle, or leave.  **Generally** speaking it isn’t worth the fight later on, being that one might as well just re-write the entire application.
