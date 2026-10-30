---
title: The Gap Is Widening and It’s Not Slowing Down
date: 2026-05-26 21:12:14 -0700
last_modified_at: 2026-05-26 23:13:58 -0700
permalink: /2026/05/26/the-gap-is-widening-and-its-not-slowing-down/
slug: the-gap-is-widening-and-its-not-slowing-down
wp_id: 74723
original_url: https://compositecode.blog/2026/05/26/the-gap-is-widening-and-its-not-slowing-down/
categories:
- AI & AI Tooling
- Programming
tags:
- ai
- claude
- coding
- gen ai
excerpt: Brendan O’Leary’s recent article highlights the slow adoption of AI coding tools among engineers, noting a widening gap between early adopters and others. Despite challenges like security concerns and past negative experiences, teams that integrate AI effectively gain significant advantages. Current adoption must be disciplined to avoid creating technical debt while enhancing productivity.
image: /wp-content/uploads/2024/07/exported2-multi-ethnic-programmers-checking-source-code-and-2023-11-27-05-17-47-utc.jpg
---

Brendan O’Leary wrote a piece this week titled “[The AI Coding Revolution Hasn’t Started Yet](https://blog.kilo.ai/p/the-ai-coding-revolution-hasnt-started)“. His headline observation: most professional engineers haven’t adopted AI coding tools in any meaningful way. Not even close.

In my experience too, he’s right. I’d push it further.

I’ve been deep in this work – helping companies actually get Generative AI tooling integrated into real development workflows, not just installed, not just “evaluated,” but *actually integrated*. Running sessions, doing the pairing, reviewing the setups, watching teams try to navigate the gap from “we have Copilot turned on” to “we’re doing something meaningfully different with how we build software.” and what I keep seeing isn’t just that most companies haven’t started. It’s that the gap between the teams that *have* started and everyone else is **compounding**. Every week that passes, that gap doesn’t hold steady. It widens.

## The Observation from the Inside

The conference Brendan was at, where he made this observation is a good one. You talk to staff engineers, architects, team leads – people who are not amateurs at this craft – and you find out they’re still in the “I’ve heard of Claude Code” phase. That’s a real data point and it matches what I’m seeing at companies I work with. More than a few times they haven’t even gotten to that point.

But here’s the wrinkle that the conference floor view doesn’t fully capture: the gap isn’t just about *adoption level*. It’s about *trajectory*. The practitioners who’ve gone deep aren’t standing still. They’re getting faster, refining workflows, building intuition about how to orchestrate agents, where to trust the output, where to keep a tighter leash, and where to let things run. They’re compounding their advantage *every single week*. Meanwhile, a team that’s still on “tab completion is the whole idea” isn’t sitting on a fixed baseline. They’re falling behind in a relative sense, even if their absolute productivity is unchanged.

That’s a slow-moving disaster in competitive terms.

## The Questions That Tell the Story

I’ve had almost the exact same hallway conversations described. The tells are in the questions:

*“Wait, so the agent actually runs the tests itself?”*

*“How are you keeping it from just rewriting everything it touches?”*

*“Our security team said no to all of this, so we haven’t tried anything.”*

None of these are dumb questions. In fact, they’re the *correct* questions — they mean the person is starting to actually reason about agentic tooling rather than dismissing it. But they’re also questions that someone who’s been working in this space for six months has already burned through, experimented on, and formed opinions about. There’s a widening experiential gap underneath the tooling gap and that part is harder to close quickly.

## Why the Lag Is Rational (But Costly)

The reasons Brendan lists for slow adoption from security lockdowns, bad early Copilot experiences, tool landscape churn, team skepticism are all real and I’ve run into every single one of them. Let me add a few more from what I’ve encountered.

The “we tried it and it wasn’t impressive” problem is particularly pernicious, because the delta between the experience of using autocomplete in 2023 and using an agentic coding workflow in 2026 is genuinely massive. But if you hit the bad experience first and walked away, you should probably revisit it now. I know demos that happen at conferences aren’t likely to convince. A well-produced YouTube video either. But get your hands dirty and use it, otherwise the lag is going to send you, or the group you work with into luddite land and made “redundant” as they say in some places (i.e. laid off, unemployed, etc).

That’s one of the core things I try to do when working with teams: get past the “is this real” phase as fast as possible by showing it working on their actual code. Because abstract capabilities don’t move people. Seeing an agent navigate through a service you wrote, flag something you’d have missed, and propose a coherent refactor in thirty seconds — *that* moves people.

The security lockdown problem is also real but I want to name it more precisely: what organizations actually mean when they say “we can’t use AI tools on our codebase” is usually *“we haven’t yet done the work to understand what the actual risk surface is.”* Which is a very different thing than a reasoned security position. It’s a deferral masquerading as a decision. And that deferral has a cost that most orgs aren’t properly accounting for on their risk register.

## The Vibe Coding Trap Is Real Too

Here’s where I’ll add some nuance that doesn’t always make it into the “you should adopt this” framing: adoption without discipline is its own problem.

There’s a Stanford study that just landed – [SWE-chat](https://arxiv.org/pdf/2604.20779), (which I have a lot of frustration with how it’s often mis-interpreted, for example the comment I’ve left [here](https://blog.kilo.ai/p/the-ai-coding-revolution-hasnt-started/comment/265670675) the post) looking at 6,000 real coding agent sessions from open-source developers in the wild – and the numbers are sobering. Only 44% of agent-produced code makes it into commits. Vibe-coded sessions (where the agent authors virtually all the code) burn roughly 3x more tokens and dollars per committed line than collaborative sessions. And vibe-coded code introduces about 9x more security vulnerabilities per committed line than code humans write themselves.

I’ve talked about this at length in [Hurting or Helping Devs](/2026/04/15/hurting-or-helping-devs/) and in my breakdown of [the types of code changes that AI agents produce](/2026/02/12/additive-vs-mutative-vs-destructive-code-changes-and-why-ai-agents-love-the-wrong-one-at-213am/). The tools are genuinely powerful. They’re also genuinely capable of quietly reshaping a codebase into something that *looks* correct but behaves like it was written by an overly confident intern with root access and no fear of consequences.

The right model isn’t “hand everything to the agent.” It’s orchestration with discipline – scoped prompts, diff limits, human gatekeeping on production deployments, and a clear-eyed understanding of where agent judgment is trustworthy and where it isn’t. That’s a craft skill that takes time to develop. It can’t be skipped.

So I’m not just saying *adopt*. I’m saying *adopt correctly* with discipline, which is harder, takes longer, and requires more deliberate investment. But the teams doing it right are building a durable advantage. The teams doing it sloppily are creating technical debt at a rate that will bite them in ways that are currently hard to see.

## The Compounding Problem

Here’s the thing about compounding gaps that I keep coming back to: they don’t feel urgent when you’re inside them.

If your team is shipping at more or less the same pace it shipped at a year ago, nothing feels broken. Nothing is on fire. You’re not obviously behind. The gap is invisible to you because the other side of it isn’t in your day-to-day view.

But a team that’s been running agentic workflows for six months has built intuition, muscle memory, and workflow patterns that can’t be copied in a week. They’ve figured out what to scope, what to constrain, where to trust, and where to verify. They’ve failed in some interesting ways and learned from it. They’re operating at a different surface area of the problem than a team that’s starting from scratch — even if both teams have access to the same models and tools.

That’s the part that concerns me most when I work with orgs that are still in “evaluation mode” two years into this transition. The tools aren’t the moat. The *practice* is the moat. And practice requires time.

The clock is running.

## What Needs to Happen

Brendan is optimistic about the diffusion curve tipping soon, and I think that’s probably right. The on-ramp needs to get lower – better model-agnostic tooling, less lock-in, less requirement to reconstruct your entire workflow to get started. Those are the right levers.

But I’d add one more: organizations need someone to physically show them what the other side looks like, in their context, with their problems. Not a demo environment. Not a benchmark. Their actual code. Their actual team. That’s the thing that moves the needle from “heard about it” to “we’re doing this.”

If you’re at a company still sitting on the sidelines on this – not because of a reasoned, deliberate decision, but because it hasn’t risen to the top of the priority stack yet – I’d genuinely encourage you to treat that as a risk and a significant one at that. Not a vague future risk. A significant present, compounding one.

The teams on the other side of that gap are not slowing down.
