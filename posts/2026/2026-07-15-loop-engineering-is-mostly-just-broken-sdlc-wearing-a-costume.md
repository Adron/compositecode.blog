---
title: “Loop Engineering” Is Mostly Just Broken SDLC Wearing a Costume
date: 2026-07-15 00:00:45 -0700
last_modified_at: 2026-07-15 00:00:45 -0700
permalink: /2026/07/15/loop-engineering-is-mostly-just-broken-sdlc-wearing-a-costume/
slug: loop-engineering-is-mostly-just-broken-sdlc-wearing-a-costume
wp_id: 74905
original_url: https://compositecode.blog/2026/07/15/loop-engineering-is-mostly-just-broken-sdlc-wearing-a-costume/
categories:
- AI & AI Tooling
tags:
- coding
- javascript
- programming
excerpt: Adron critiques the concept of “Loop Engineering,” arguing it merely retrofits outdated software development practices onto language models. This approach adds unnecessary complexity and coordination, hindering LLMs’ potential. Instead, the author advocates for creating efficient workflows that leverage LLM capabilities by improving input quality, structuring tasks by data flow, and integrating event-driven feedback mechanisms.
image: /wp-content/uploads/2026/07/two-women.jpg
---

I’ve been watching the “Loop Engineering” conversation build up steam for a while now and I keep landing in the same spot: I’m not buying it. Not the way it’s being sold, anyway.

The pitch is seductive. Wrap the LLM in a loop — plan, act, observe, correct, repeat — and you get an autonomous-ish thing that grinds away at your problem until it’s done. Everybody nods. It sounds rigorous. It sounds like engineering. And that’s exactly the part that’s bugging me, because the more of these “loop” architectures I look at, the more they look like something I’ve seen before. They look like the same slow, cumbersome, ceremony-laden SDLC that companies have been stuck in for thirty years — except now we’ve bolted it onto a language model and called it innovation.

Let me be blunt about the thing I actually think is happening here. We are not designing new ways to work with LLMs. We are retrofitting the broken software development lifecycle we already had onto a brand new kind of tool, and then acting surprised when the result is convoluted and bloated. The loop isn’t a breakthrough. In a lot of shops it’s a reskin of the ticket-grooming, status-meeting, hand-off-and-wait machine that made software slow in the first place. Largely, it defeats the entire advantage of using an LLM in the first place.

## The tell: it’s ceremony, not capability

Here’s what tips me off. Go look at a bunch of these “agentic loop” designs in some of the more advanced companies – the ones that are supposedly doing this right – and count the steps. Plan the plan. Break the plan into subtasks. Score the subtasks. Route the subtasks. Re-plan when a subtask fails. Reflect on the reflection. Summarize the reflection into a memory. Retrieve the memory to plan the next plan.

Squint! That’s not a novel machine intelligence workflow. That’s Scrum with a transformer in the standup. It’s the same “process as a substitute for thinking” instinct that gave us story points and RACI charts and forty-five minute refinement meetings. We took a slow, human, coordination-heavy process – one that mostly exists because humans forget things, go home at night, and don’t share memory – and we handed it, wholesale, to a system that doesn’t forget in the same way, doesn’t go home, and can share state instantly.

The loop, in a huge number of cases, is coordination overhead that the model doesn’t actually need. We’re paying for it in tokens, latency, and complexity, and calling the bill “engineering rigor.”

## Loops exist to cover for things LLMs shouldn’t need covered

[![Programmer looks at the loop getting errors.](/wp-content/uploads/2026/07/single.jpg)](/wp-content/uploads/2026/07/single.jpg)

*Programmer looks at the loop getting errors and the tears and pain of the absurdity of it is driven home! The horror, the nightmare!*

A loop is fundamentally an error-correction and coordination structure. You loop when you can’t get it right in one pass and you have no better way to make forward progress than to try, check, and try again. That’s a completely reasonable thing to do sometimes. But notice *why* the classic SDLC is so loopy: it’s loopy because the humans and systems in it have terrible, lossy interfaces to each other. Requirements get garbled on the way to the dev. Context evaporates between the ticket and the code. Nobody can see the whole thing at once, so we iterate blindly and use process to catch the drops.

When you lift that structure and drop it onto an LLM, you inherit all of those assumptions – lossy hand-offs, missing context, blind iteration – *even when they no longer apply.* The model can hold enormous context. It can be given the whole picture at once. It can be handed clean, structured inputs instead of a garbled ticket. So a lot of the loop is there to solve a problem you’ve already got the tools to eliminate. You’re building a bucket brigade next to a working fire hose.

That’s the reframe I want people chewing on: **don’t fit the LLM to the broken SDLC. Fix the SDLC around what the LLM is actually good at, and a lot of the loop – and the SDLC – just disappears.** Not all of it — some feedback is real and necessary — but a lot of it goes away.

## So what do you build instead? Workflows, not loops.

A workflow is a directed thing. It has a shape. It moves from a known input to a known output through steps that each do one clear job, and it only bends back on itself where a *real* signal says it must. Not on a fixed “reflect every turn” cadence because the architecture diagram had a box for it. Here are the approaches I’d actually reach for, and roughly in the order I’d reach for them.

### 1. Front-load context so the first pass is the good pass

The single biggest source of looping is a bad first attempt caused by starved input – a barren prompt that is missing context, scope, and specifics. So stop starving it. Instead of a thin prompt and a correction loop to claw the quality back, spend your engineering effort *upfront* assembling everything the model needs: the relevant code, the schemas, the conventions, the prior decisions, the actual constraints. Curate it. Structure it. Hand the model the whole board. Give it a specific thing to do with plenty of reference (MCP/RAG, etc) to get what it needs to get the job done right from inception.

This is a workflow move, not a loop move. You’re not iterating toward context — you’re delivering it before step one. The payoff is enormous, because every loop you avoid is latency and tokens and a chance to go off the rails that you never spent. A well-fed single pass beats a starved five-pass loop most of the time, and it’s cheaper and easier to reason about. Put the work where it compounds: the input.

### 2. Decompose along data flow, not along a status board

When a task genuinely is too big for one pass, the instinct from SDLC-brain is to break it into “tickets” and manage them in a loop. Don’t. Break it along the *data* instead – a pipeline where each stage has a typed input and a typed output, and stages connect because one’s output is literally the next one’s input.

Extract, then transform, then validate, then render. Parse, then plan, then generate, then check. Each stage is a small, boring, testable unit that does one thing to a known input. This is the old Unix-pipe wisdom, and it holds up beautifully with LLMs: small components with sharp interfaces that you can compose, test, and swap. The magic is that a clean pipeline *removes* the reason to loop – you’re not re-planning the whole job when stage three hiccups, you’re re-running stage three. The blast radius of a failure is one stage, not the entire task. That’s the difference between a workflow and a loop: the workflow contains failure; the loop lets it slosh around the whole system.

### 3. Make feedback event-driven, not clock-driven

Here’s where I think the loop crowd goes most wrong. In a canonical loop, you reflect and re-plan *every iteration*, on a cadence, whether or not anything happened worth reflecting on. That’s the transformer equivalent of a daily standup where nothing changed but everyone talks anyway. Pure ceremony.

Flip it. Don’t loop on a clock – react to events. Wire the model into a workflow where a *specific, real signal* triggers a *specific* corrective action. Tests failed? Route the failing output and the error back for a targeted fix – not a full re-plan, just “fix this.” Schema validation rejected the payload? Send it back with the exact violation. A confidence or a guard check tripped? Escalate that one thing. Everything else flows straight through.

The behavior looks loop-like from a distance, sure – things sometimes go back around. But the structure is completely different, and the difference is the whole point. Correction happens because something concrete demanded it, scoped to exactly what broke, instead of on a blind fixed schedule that burns tokens re-litigating work that was already fine. Nine times out of ten nothing needs to go back, and your workflow should sail straight through when that’s the case.

### 4. Push determinism to the edges and let the model do the fuzzy middle

A ton of what gets stuffed inside these loops is stuff the model has no business doing repeatedly – running code, hitting an API, checking a value against a rule, formatting an output. Every time you make the LLM babysit that inside a reasoning loop, you’ve added a slow, nondeterministic, expensive step to do a job that a plain function does perfectly, instantly, and the same way every time.

So carve it out. Let deterministic code own everything that *can* be deterministic: the tool calls, the validation, the I/O, the formatting, the branching on hard rules. Let the model own the genuinely fuzzy judgment in the middle – the part that actually needs a language model. When you draw that line cleanly, the “loop” collapses into a mostly-straight workflow with the LLM as one well-scoped component inside a larger deterministic system, instead of the LLM being the anxious general contractor re-checking every subcontractor’s work on every pass. Less looping, more determinism, and the model spends its cycles on the one thing only it can do.

## Pulling it together

Put those four together and look at the shape you get. You front-load context so the first pass lands. You decompose along data flow so failures stay contained. You make correction event-driven so you only bend back when something real demands it. And you push everything deterministic out to the edges so the model isn’t looping over work a function should own. What’s left is a workflow – directed, inspectable, cheap, testable – with the LLM doing the fuzzy judgment it’s uniquely good at and *nothing else.*

Compare that to the canonical loop: an undirected grind, re-planning and re-reflecting on a cadence, coordination overhead standing in for capability, the whole thing shaped by the assumption that every hand-off is lossy and every input is garbled – assumptions that came straight out of the broken SDLC and mostly don’t apply here.

I want to be fair about it: loops aren’t *always* wrong. There are open-ended, genuinely exploratory problems where you can’t shape the path in advance and try-check-try is honestly the best you’ve got. Fine. But that’s the exception, and right now the industry is treating it as the default. We’re reaching for the loop reflexively because it *feels* like the rigorous, grown-up, “real engineering” thing to do – when a lot of the time it’s just the old ceremony in new clothes.

There’s more going on with LLMs than the loop. A lot more. The loop is one tool, and it’s become a bit of a security blanket for people who’d rather port their existing broken process than sit down and design a new one. My request is simple: before you wrap your model in yet another plan-act-reflect grinder, ask what the loop is actually *for* in your case. If the honest answer is “to cover for lossy hand-offs and missing context,” then you don’t have a loop problem. You have an SDLC you never cleaned up – and the fix is a workflow, not another lap.
