---
title: 5 Ways to Learn & Improve Your Programming Language Use
date: 2020-04-20 12:06:41 -0700
last_modified_at: 2020-04-20 12:20:27 -0700
permalink: /2020/04/20/5-ways-to-learn-improve-your-programming-language-use/
slug: 5-ways-to-learn-improve-your-programming-language-use
wp_id: 16840
original_url: https://compositecode.blog/2020/04/20/5-ways-to-learn-improve-your-programming-language-use/
categories:
- Ideas
- Unknown Code Ramblings
tags:
- coding
- getting started
- programming
- programming language
- skills improvement
- softwaredevelopment
- tips
- tricks
excerpt: Posed the question, What to write when starting to learn and programming language? I started an answer to the question in this video. But read on for more extensive list and details! I’ve written up this article. It started last week when I wrote up “Top 5 Ways to get the coding basics down!” This …
image: /wp-content/uploads/2020/04/devto-programming.jpg
---

Posed the question,

> What to write when starting to learn and programming language?

I started an answer to the question in this video. But read on for more extensive list and details!

<iframe allowfullscreen="allowfullscreen" class="fluidvids-elem" data-mce-fragment="1" height="399" loading="lazy" src="https://www.youtube.com/embed/-NuZhoApxYw" width="710"></iframe>

I’ve written up this article. It started last week when I wrote up “[Top 5 Ways to get the coding basics down!](/2020/04/17/top-5-ways-to-get-the-coding-basics-down/)” This week I wanted to delve deeper into a specific item on that list and provide what I came up with, which is this List of 10 things to write in order to effectively learn a programming language.

## 1. Find a Known Domain

What I mean by this is to find a domain that you personally know. It seemed the 80’s generation of programmer dorks wrote role playing game character generators for Dungeons & Dragons. I did myself but for Robotech. But there’s a million other domains that you would know, and those domains are what you should pick and find data and actions in that domain you could implement with code.

Two examples I’ve used recently includes the made up e-commerce store of Better Botz, a store that works with the domain of robots and mecha, and Railroads such as Union Pacific, Norfolk Southern, Amtrak, and the respective domain around that. Many of the other things you could use might be transportation, automotive, health care, or more specific the universe of Harry Potter, Star Wars, Tumble Leaf, Sesame Street, style and fashion trends,

## 2. Model a Domain According to the Language

Let’s say you’re learning JavaScript. Whatever the domain you’ll want to find actions and data to implement and use specificly to how the language is best used. With JavaScript that would be to use the language features and design to build a working application, like; perform mathematical calculations, such as with bigint, using dynamic import, chaining, promises, async and await, global variables, arrow functions, inheritence through prototyping, and how the properties and methods, or functions, for starters work best for the application domain.

In C#, Java, Rust, Go, Erlang, F#, and other languages these features and characteristics would be different. Whatever the language, make a list of the features and characteristics that are widely used and work with those to best implement the application domain.

## List Interupt: Refactoring

I’ve written this list in order of what I personally have found the easiest path in gaining a high level of profiecience with a programming language. You could however mix the list to your preferred style. However at this point between the first two item efforts and the next a new skill will be learned both out of necessity and intent: refactoring.

> “*Code Refactoring* is the process of restructuring existing computer code—changing the factoring—without changing its external behavior. Refactoring is intended to improve the design, structure, and/or implementation of the software (its non-functional attributes), while preserving the functionality of the software. Potential advantages of refactoring may include improved code readability and reduced complexity; these can improve source code maintainability and create a simpler, cleaner, or more expressive internal architecture or object model to improve extensibility.”

## 3. Learn to Test

Learning to test an application will help you tremendously in writing better code. If you’ve committed the actions of the first two items in this list, this is an opportunity to significantly refactor the application you’ve built around your known domain. You’ll need to break apart existing functions so that they’re bit size enough to test. Sometimes you’ll need to differentiate between making some testable at a small *unit* size versus across an application’s hard boundaries, like an *integration* test between a database and the application’s data access code.

Pushing for testing the core domain functionality of the application is the best thing to focus on. Don’t worry about the specifics of testing if data is written to the database, or data is retrieved from the database, as much as testing that a function returns the specific answer you expected based on passing it the specific parameters you’ve assumed it would be given. This isn’t to say sometimes you may want to test what you’ve written to the database, so sure, that is something that you can test. But focusing on the core application domain functionality will ensure the best return on your investment of time!

## 4. Clean Coding Practices

Once you’ve gained familiarity with the language by building an application or two using the features, rooted in a known domain that you understand well, and have some test coverage of the application, refactor that application using clean coding practices. Clean code is often described using the SOLID principles:

- Single Responsibility Principle
- Open / Closed Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principle

See also: KISS (Keep It Simple Stupid), DRY (Don’t Repeat Yourself), YAGNI (You Aint Gonna Need It), and others.

The idea behind these, is to keep the application code regardless of languages as simple as it can possibly be. With a secondary effect that once software becomes painful to modify, it should be changed as to make modification simpler. Thus the idea of refactoring to the SOLID principles listed, and doing so continuously will keep software in a usable, maintainable, and one could arguable say even a *performant* state.

## 5. The Hardest Suggestion: Naming & Thinking

It is often stated, “The hardest problem in computer science is naming things.” to which I, not in jest, whole heartedly agree. Elements in programming, programming design, programming implementation, and every permeable space around programming is littered with poorly named things. I don’t blame anybody because it is damned hard to get a good name for features and functionality, and have truth in the naming of those features and functionality remain throughout the course of its lifetime.

Naming is hard, which I’d combine to say stop programming regularly and think about your naming. Think about refactoring to names that are more accurate to the intent. Stop and ponder what a good name would be, and if the function or feature will replication what that name implies. Add in some metaphysical thought to the whole effort, talk it through with someone you know (or a stranger, it’s a good skill for debuggin!), but think, think, ponder, analyze, and think some more.

The short of the long part of this suggetion can simply be summarized as: Practice naming things, think a bunch, then rename things, and repeat this cycle.

## In Summary

To really get a programming language down by heart, be able to readily implement pretty much anything, this is my go to list of actions and practices to follow. Hopefully, it’ll provide you with some ideas to explore how best you would also like to go about learning a programming language. I’m always open to suggestions, comments, thoughts, and discussions on the topic, so feel free to ping me via the Twitters [@Adron](https://twitter.com/Adron).

## Search Words

Type in any of the following, in pretty much any search engine, like [duckduckgo](https://duckduckgo.com/) to dig up the latest and greatest on this topic.

- Single Responsibility Principle
- Open / Closed Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principle
- How to Model a Domain
- Clean Coding Practices
- Unit Testing
- Unit Testing Practices
- SOLID Principles
- Package Principles (REP, CRP, CCP, ADP, SDP, SAP)
- Don’t Repeat Yourself (DRY)
- Keep It Simple Stupid (KISS)
- You Aint Gonna Need It (YAGNI)
