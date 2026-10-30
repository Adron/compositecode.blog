---
title: .netTiers Code Generation
date: 2007-10-02 01:22:15 +0000
last_modified_at: 2007-10-02 01:22:15 +0000
permalink: /2007/10/02/nettiers-code-generation/
slug: nettiers-code-generation
wp_id: 423
original_url: https://compositecode.blog/2007/10/02/nettiers-code-generation/
categories:
- Uncategorized Bits
tags: []
excerpt: A tip for code generation. When reading through various patterns based development books, working on my current gig, and just trying to make code more readable without adding too much headache, I’ve stumbled on a few tips. Name those entities! Instead of “Address” or “User” you would then have AddressEntity or UserEntity. This is very …
---

A tip for code generation.  When reading through various patterns based development books, working on my current gig, and just trying to make code more readable without adding too much headache, I’ve stumbled on a few tips.

1. Name those entities!  Instead of “Address” or “User” you would then have **AddressEntity** or **UserEntity**.  This is very helpful when you are using domain objects at a higher layer than your entity objects.  It is also helpful in the case of a WCF Facade layer that steps back through via reflection to find what entities it needs to get for data contract purposes!- In the code generation properties there is a **IncludeUnitTests** property.  As in regular code as in generated code, if you can have tests, have them!  There is a choice between **NUnit** and **VSTS** tests even, so it isn’t like there are test framework conflicts!

Well, that’s it for today.  Just a few ideas to keep locked away for future use.  For now, published via car #402 on Sounder Train #1501, I’m diving back into my code.
