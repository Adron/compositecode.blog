---
title: 'The Missing Pieces: What Online Tutorials and Docs Always Seem to Forget'
date: 2024-10-17 14:30:11 -0700
last_modified_at: 2024-10-17 14:30:18 -0700
permalink: /2024/10/17/the-missing-pieces-what-online-tutorials-and-docs-always-seem-to-forget/
slug: the-missing-pieces-what-online-tutorials-and-docs-always-seem-to-forget
wp_id: 70068
original_url: https://compositecode.blog/2024/10/17/the-missing-pieces-what-online-tutorials-and-docs-always-seem-to-forget/
categories:
- Coding Adventures
- Coding Patterns & Practices
- Writing
tags:
- aritcles
- blog posts
- documentation
- documentation writing
- tech tutorials
- tutorials
- writing
excerpt: The post addresses common shortcomings in online tutorials and documentation. It emphasizes the importance of clear prerequisites, context, real-world use cases, error handling, performance, security, integration, testing strategies, and attention to detail. The author urges tutorial creators to eliminate assumptions and provide comprehensive guidance for users of all skill levels.
image: /wp-content/uploads/2024/10/an-angry-beautiful-woman-coding-the-missing-pieces-what-online.png
---

Yo, fellow coders and tech enthusiasts! Adron here, and today we’re diving into a topic that’s been grinding my gears for ages – the stuff that’s always missing from online tutorials and docs. Buckle up, ’cause we’re about to get grumpy!

## 0. The Invisible Prerequisites

Before we even get to the main course, let’s talk about the appetizer that so many tutorials forget to serve – the damn prerequisites! I can’t tell you how many times I’ve started a tutorial only to find out halfway through that I needed some obscure tool or specific version of something that wasn’t mentioned upfront.

Here’s the deal, tutorial writers: lay out ALL the prerequisites clearly at the beginning. And I mean ALL of them. Don’t assume I have jq installed for your GraphQL tutorial. Don’t assume I’m running the latest version of Python (and for the love of code, specify ***WHICH*** Python – 2.x or 3.x?).

And here’s a novel idea: how about actually telling me where to find and install these prerequisites? Give me links, give me version numbers, give me command line instructions. Assume I’m starting from scratch on a fresh machine. Because guess what? Sometimes I am!

Even though this isn’t a tutorial, but just because I mentioned them here, check out jq [here](https://jqlang.github.io/jq/) and Python [here](https://www.python.org/downloads/).

## 1. The “Why” Behind the Code

Look, I get it. You’re excited to show off that sweet new framework or library. But for the love of all that is holy in the tech world, tell me WHY I should care! Too many tutorials jump straight into the how without explaining the why. Give me context, people! I get that jq is cool (yeah, that thing again!) but why do I want to mess with JSON from the command line, the ole’ terminal, or the bash or zsh, explain to me why it matters. I know it might seem to you to make sense, but often there is a lot of context missing up front, fill in the context.

## 2. Real-world Use Cases

Sure, your “Hello World” example is cute. But when am I ever gonna need to print that in production? Give me some meaty, real-world scenarios. Show me how your tool solves actual problems developers face in the trenches. This is of course hard, it is of course time consuming, and it can be painfully difficult to work up and example in a timely manner and actually finish a blog post on a particular piece of tech. It does take a lot of work, but if we want an article to be effective, readable, and usable over time it’s got to have some meat to it.

## 3. Error Handling and Debugging

Everything works perfectly in your tutorial? That’s adorable. In the real world, stuff breaks. A lot. Show me how to handle common errors, how to debug when things go sideways, and how to not lose my mind in the process.

One of the best ways I’ve found to add error handling and debugging is to work through the example I’m going to present from a fresh machine. It forces me to find the prerequisites but also run into all sorts of errors and what ifs. Presenting only the happy path just doesn’t always help, throw in some curve balls and at least talk through in a post what error handling or debugging might look like.

## 4. Performance Considerations

Yeah, your code runs. But will it scale? Will it choke when hit with real traffic? Don’t just show me how to implement something – show me how to implement it efficiently.

This is something, in my not humble opinion, every single database topic should start with and end with a performance conversation. The number of poorly designed databases I’ve fumbled upon out in the wild, once I’ve reverse engineered them and discovered the history I’ve found a single thing in common with poorly performing databases. Simply that, performance and end outcome wasn’t taken into account. This should be the first step of creating any data storage mechanism, but also any operations on data the code, database, cache, or other layer.

## 5. Security Implications

In this day and age, ignoring security is like leaving your front door wide open with a “Rob Me” sign. Walk me through the security considerations. What are the potential vulnerabilities? How do I protect against them?

But wait, maybe that analogy isn’t right. It’s the internet after all, maybe it’s more like installing a front porch on your house and taking off the front door and the entire front wall. Exposing your living room to the world and just offering to have the community stroll through it. That’s more like it, so yeah, security needs to be a high priority topic in most circumstances. Be thorough, be accurate, include a thought or three about how one locks down the topical tech bits you’re rambling on about.

## 6. Integration with Existing Systems

News flash: most of us aren’t working on greenfield projects. Show me how your shiny new tool plays nice with legacy systems. How do I integrate it into my existing stack without bringing down the whole house of cards? This could, like several of these suggestions, be merely a conversation paragraph or two about thoughts on integration with existing systems, to the ultimate by having examples of integrations.

## 7. Testing Strategies

Unit tests are great, but they’re just the tip of the iceberg. Give me the full testing spectrum – integration tests, end-to-end tests, performance tests. Show me how to sleep soundly knowing my code won’t implode in production.

At this point in time, this seems like something that shouldn’t even be mentioned. Kind of like showing an example of the actual thing you’re talking about in the first place. If you’re going to show how to implement X with Y library or something, we all need to see Y library under test with X implemented. A new drag and drop feature, “cool!”, but how the hell do you test that?

## 8. The Devil in the Details

Alright, let’s talk about something that drives me up the wall – the missing small steps. You know what I’m talking about. Those tiny, seemingly insignificant details that tutorial writers assume everyone knows. Newsflash: we don’t!

I can’t count the number of times I’ve been following a tutorial, feeling good about myself, when suddenly I hit a wall because the author skipped over some “obvious” step. Maybe it’s how to set up a virtual environment in Python. Maybe it’s how to properly configure your PATH. Or maybe it’s just how to navigate to the right directory in the terminal.

These might seem trivial to you, oh wise tutorial writer, but to a newbie or someone coming from a different tech stack, these small steps can be the difference between smooth sailing and a frustrating afternoon of Googling and hair-pulling. At least, if it seems somewhat unreasonable to add specific details, at least mention and link to where one might find the details. For example, as mentioned above, where is a tutorial getting a virtual environment setup for Python, like [this one](/2019/12/25/unbreaking-python-through-virtual-environments/), or the [step even before that one](/2019/12/23/getting-started-with-python-right/).

So here’s my plea: Don’t assume anything. Walk us through every. Single. Step. Even if it seems painfully obvious to you. Because what’s obvious to you might be a revelation to someone else. And isn’t that the whole point of a tutorial?

Look, I get it. Covering all this stuff is hard. It takes time, effort, and a deep understanding of your tool and its ecosystem. But that’s exactly what separates the mediocre docs from the stellar ones.

So, to all you documentation writers and tutorial creators out there: step up your game. Your users will thank you, and the coding world will be a better place for it.

Now, if you’ll excuse me, I’ve got some legacy code to wrangle and a cup of coffee with my name on it. Keep coding, keep learning, and for Pete’s sake, keep documenting – every single step of the way! 🤘🏻
