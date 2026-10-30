---
title: I’ve Been Brainstorming Durable AI for InterlinedList, and It Kept Pointing at Temporal
date: 2026-08-11 06:30:00 -0700
last_modified_at: 2026-08-10 23:22:34 -0700
permalink: /2026/08/11/durable-ai-for-interlinedlist-and-it-kept-pointing-at-temporal/
slug: durable-ai-for-interlinedlist-and-it-kept-pointing-at-temporal
wp_id: 74990
original_url: https://compositecode.blog/2026/08/11/durable-ai-for-interlinedlist-and-it-kept-pointing-at-temporal/
categories:
- AI & AI Tooling
- interlinedlist
- Temporal
tags:
- durable ai
- durable services
- interlinedlist
- programming
- temporal
excerpt: Adron explores the challenges of integrating durable AI features into InterlinedList, which is entirely serverless. Key obstacles include serverless limitations on memory, scheduling flexibility, and cost management. A proposed solution is to employ a durable-workflow engine, like Temporal, which enhances efficiency and reduces costs associated with AI token usage.
image: /wp-content/uploads/2026/08/01-why-temporal-durable-ai-hero-1.png
---

**Part 1 of 8: Durable AI for InterlinedList**

---

I’ve been chewing on a question for weeks. If InterlinedList is going to have real AI features (the “Coming Soon” ones on the pricing page, the ones I actually want to use myself) what does the plumbing behind them look like? Not the prompts. The plumbing. And every time I sketched it out, I hit the same wall in the same four places.

So I did the thing I’d tell anyone else to do. I stopped sketching in a vacuum and pointed Claude at the actual repository.

## The Wall Is Serverless, and I Put It There

InterlinedList is 100% serverless on Vercel. That was a deliberate choice and mostly a great one. It’s also the thing shaping every AI idea I have, whether I like it or not.

A serverless function has a duration ceiling. It has no durable memory between requests, it can’t pause and wait for you to click “yes,” and when it fails partway through expensive work, it has no idea what it already paid for. For a request/response app that serves pages, none of that matters. For anything that calls a language model, all of it matters. A lot.

Here are the four places I kept getting stopped.

**Scheduling is already fragile, and this one isn’t hypothetical.** InterlinedList has scheduled publishing today (a Subscriber feature). The cron at `app/api/cron/publish-scheduled-messages/route.ts` runs every minute. I checked `vercel.json`, it’s a literal `* * * * *`. It fans a due post out to Bluesky, Mastodon, LinkedIn, and X, then flips the message out of “scheduled” state. There’s no lock and no idempotency key. So if the cross-posts succeed but that final `UPDATE` fails (a reaped Neon connection, a cold-start hiccup) the message stays “due” and the *next* tick republishes it. To every platform. Again. That’s a slow-moving double-post waiting for a bad minute, a bug I already own, sitting in production, with zero AI anywhere near it.

**Long generation doesn’t fit.** A 16k-token document, streamed out of a model, will blow past a serverless function’s budget before it finishes. There’s no clean way to say “keep going, I’ll be back.”

**Batch and agentic work has nowhere to live.** “Tag every untagged message.” “Add twenty rows to this list matching these criteria.” “Research my saved links and draft a doc.” Those are multi-minute, multi-step, retry-heavy jobs. A function that dies at ninety seconds is the wrong shape for all of them.

**And there’s no cost governor.** This is the one that kept me up. Every retry re-bills the model. There’s no budget ceiling, no cheap-model-first policy, no response cache, no dedup. One runaway loop and you’ve torched real money.

## The Expensive Line Item Is Never the Infrastructure

Once I reframed the money question, the design mostly wrote itself. This reframe runs under the whole series, so it’s worth stating plainly.

The expensive thing about AI features is tokens, not servers. Basically never servers.

A durable-workflow engine (Temporal, in this case) costs on the order of tens of dollars a month, flat. One small always-on worker, maybe a managed namespace. That number does not move when your users get busy. The model bill does, and it moves a lot.

So the question isn’t “can I afford Temporal.” It’s “does Temporal make the model bill smaller.” And the reason it kept showing up in my brainstorm is that its mechanics do that, structurally:

- **Durable memoization.** A completed step is persisted. When a six-step pipeline fails at step five, the retry re-runs step five, *not* the four already-billed model calls before it. A retry never re-invokes an LLM call you already paid for. This is the single biggest saver in the whole list.
- **Model cascade.** Cheap model first (Haiku, Flash) and escalate to an expensive tier only when the work demands it, or the user explicitly asks for long-form.
- **Batching.** Tag fifty messages in one call instead of fifty calls. The per-request overhead and the duplicated context collapse.
- **Rate-limit obedience.** Cap concurrency to stay under provider limits, so you don’t trip a 429 storm whose retries waste both wall-clock and, on some providers, tokens.
- **Response and URL dedup.** Identical prompts get served from cache. A link that’s already been fetched isn’t fetched again. An embedding is computed once, ever.
- **A hard token-budget gate.** Check spend before each call and refuse to exceed a per-user ceiling. A leaked key or a runaway agent can’t burn unbounded credits.
- **Confirm-before-spend.** Pause and wait for the user to approve the plan before generating the expensive part. You don’t pay to build fifty list rows against a schema the model guessed wrong.

Every one of those pushes the bill down. The infrastructure that enables them is a rounding error against what it saves. And I want to be clear that “cheap as possible, relative to running raw Claude or ChatGPT calls” is why the architecture looks the way it does in the first place. I didn’t bolt cost control on at the end. I designed around it, and everything else grew out of that constraint.

## Brainstorm Against Your Real Code, Not a Whiteboard

Now the part about working with an LLM to build this, because that’s what this series is modeling.

I didn’t design this on a whiteboard. I opened Claude, gave it the real repo, and asked it to map the idea onto the code that already exists. It found the every-minute cron and traced the exact failure path where the double-post lives. It pointed at `lib/security/ssrf.ts` and the `safeFetch` guard that any link-crawling feature has to route through, and at the link detector and metadata fetcher already sitting in `lib/messages/`. It also noticed there’s no `lib/ai/` directory yet. Nothing generative is built, which lines up with AI being “Coming Soon” rather than shipped.

The output of that session was a grounded proposal (`temporal-solutions.md`) that complements an earlier BYO-key and MCP plan I’d written. That earlier plan covered *what* the AI produces and *who pays* for the tokens. It said nothing about orchestration, durability, or cost. This new one fills that gap, and it fills it against real file paths, not imagined ones.

Steal this if it’s useful. Don’t design architecture in a vacuum and then go hunting for where it fits. Let the agent read the actual repository first. Have it map your idea onto the code that exists, name the real hazards, and pressure-test it into something concrete *before* a single line of implementation. Explore first. The proposal you get back is grounded because the agent actually went and looked.

There’s a catch I want to name up front, because I try not to write brochure copy. Temporal has parts that fundamentally cannot run on Vercel serverless: a durable-state backend and long-lived worker processes that poll continuously. That’s a real new piece of always-on infrastructure in an app I deliberately built to have none. It’s the scariest unknown in the whole plan, and I’m not going to pretend it away.

Next post, I go straight at it: where Temporal actually runs when you’re all-in on serverless, and how the Vercel side stays a three-line client that just kicks off a workflow.

*[Adron](https://interlinedlist.com/user/adron) brainstorming and working on [InterlinedList](https://interlinedlist.com/).*
