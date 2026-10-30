---
title: Security Was Already a Mess. Generative AI Is About to Prove It.
date: 2026-03-09 13:27:36 -0700
last_modified_at: 2026-03-09 13:27:36 -0700
permalink: /2026/03/09/security-was-already-a-mess-generative-ai-is-about-to-prove-it/
slug: security-was-already-a-mess-generative-ai-is-about-to-prove-it
wp_id: 74350
original_url: https://compositecode.blog/2026/03/09/security-was-already-a-mess-generative-ai-is-about-to-prove-it/
categories:
- AI & AI Tooling
- Conferences
tags:
- ai
- ai tooling
- generative ai
- infosec
- security
excerpt: Adron discusses the rising security risks associated with generative AI tools, highlighting how they can inadvertently expose confidential information like API keys and passwords. While AI enhances productivity, it also amplifies existing security issues in corporate environments, necessitating stricter operational discipline in managing sensitive information during AI interactions.
image: /wp-content/uploads/2026/03/security-protection-anti-virus-software-60504.jpeg
---

I was thinking about some of the points from the [Polyglot Conf](/2025/10/13/polyglot-conference-vancouver-2024-real-talk-about-ai-industry-hubris-and-the-art-of-unconferencing/) list of predictions for Gen AI, titled “[Second Order Effects of AI Acceleration: 22 Predictions from Polyglot Conference Vancouver](/2025/10/12/the-second-ofrder-effects-of-ai-acceleration-22-predictions-from-polyglot-conference-vancouver/)“. One thing that stands out to me, and I’m sure many of you have read about the scenario, of misplaced keys, tokens, passwords and usernames, or whatever other security collateral left in a repo. It’s been such an issue orgs like AWS have setup triggers that when they find keys on the internet, they trace back and try to alert their users (i.e. if a user of theirs has stuck account keys in a repo). It’s wild how big of a problem this is.

Once you’ve spent any serious amount of time inside corporate IT, you eventually come to a slightly uncomfortable realization. Exponentially so if you focus on InfoSec or other security related things. ***Security, broadly speaking, is not in a particularly great state.***

That might sound dramatic, but it’s not really. It is the standard modus operandi of corporate IT. The cost of really good security is too high for more corporations to focus where they should and often when some corporations focus on security they’ll often miss the forrest for the trees. There are absolutely teams doing excellent security work, so don’t get the idea I’m saying there aren’t some solid people doing the work to secure systems and environments. There are some organizations that invest heavily in it. There are people in security roles who take the mission extremely seriously and do very good engineering.

A lot of what passes for security is really just a mixture of documentation, policy, and a little bit of obscurity. Systems are complicated enough that people assume things are protected. Access is restricted mostly because people don’t know where to look. Credentials are hidden in configuration files or environment variables that nobody outside the team sees.

And that becomes the de facto security posture.

Not deliberate protection.

Just… quiet obscurity.

I’ve lost count of the number of times I’ve been pulled into a system review, or some troubleshooting session, where a secret shows up in a place it absolutely shouldn’t be. An API key sitting in a script. A database password in a config file. An environment file committed to a repository six months ago that nobody noticed.

That sort of thing happens constantly. Not out of malice. Out of convenience. But now we’ve introduced something new into the environment.

Generative AI.

More importantly though, the agentic tooling built around it. Tooling that literally takes actions on your behalf. Tools that can read entire repositories, analyze logs, scan infrastructure configuration, generate code, and help debug systems in seconds. Tools that engineers increasingly rely on as a kind of external thinking partner while they work through problems.

All that benefit is coming with AI tools. However AI doesn’t care about the secret. It’s just processing text. But the act of pasting it there matters. Because the moment that secret leaves your controlled environment, you no longer know exactly where it goes, how it’s stored, or how long it persists in the LLM.

The mental model a lot of people are using right now is wrong. They treat AI like a scratch pad or an extension of their own thoughts.

It isn’t.

The more accurate model is this: an AI tool is another resource participating in your workflow. Another staff member, effectively.

Except instead of being a person sitting at the desk next to you, it’s a system operated by someone else, running on infrastructure you don’t control, processing information you send to it. Including keys and secrets.

Once you start looking at it that way, a few things become obvious. You wouldn’t casually hand a contractor your production API keys while asking them to help debug something. You wouldn’t drop a full `.env` file containing service credentials into a conversation with someone who doesn’t actually need those values.

Yet that is exactly the pattern that is quietly emerging with generative AI tools. Especially among new users of said tools! Developers paste configuration files, snippets of infrastructure code, environment variables, connection strings, and logs directly into prompts because it’s the fastest way to get an answer.

It feels harmless. But secrets have a way of spreading through systems once they start moving.

The real issue here is that generative AI doesn’t create security problems. It amplifies the ones that already exist. Problems that the industry has failed (miserably might I add) at solving. If an organization already has sloppy credential management, AI just gives those credentials another place to leak. If engineers already pass secrets around informally to get work done, AI becomes another convenient channel for that behavior.

And because AI tools accelerate everything, they accelerate the consequences too. What used to take hours of searching through documentation can now happen instantly. A repository full of configuration files can be analyzed in seconds. Systems that were once opaque are now far easier to reason about.

The Takeaway (Including secrets!)

The practical takeaway here isn’t that people should stop using AI tools. That’s not realistic and frankly a career limiting maneuver at this point. The tools are genuinely useful and they’re going to become a permanent part of how software gets built.

***What needs to change – desperately – is operational discipline.***

Secrets should never be treated casually, and that includes interactions with generative systems. API keys, tokens, passwords, certificates, environment files, connection strings—none of those belong in prompts or screenshots or debugging sessions with external tools.

If you need to ask an AI for help, scrub the sensitive pieces first. Replace real values with placeholders. Remove anything that grants access to a system. Setup ignore for the env files and don’t let production env values (or vault values, whatever you’re using) leak into your Generative AI systems.

Treat every AI interaction the same way you would treat a conversation with another engineer outside your organization, or better yet outside the company (or Government, etc) altogether.

But not someone you hand the keys to the kingdom. Don’t give them to your AI tooling.
