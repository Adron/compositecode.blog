---
title: 'Ask, Plan, Confirm: Making Agents Stop Before They Start'
date: 2026-08-20 08:00:00 -0700
last_modified_at: 2026-08-20 11:58:12 -0700
permalink: /2026/08/20/plan-then-build/
slug: plan-then-build
wp_id: 75178
original_url: https://compositecode.blog/2026/08/20/plan-then-build/
categories:
- Unknown Code Ramblings
tags:
- agentic
- agents
- ai
- coding
- gen ai
- llms
- multiple agents
- programming
excerpt: The text emphasizes the importance of a structured workflow for coding agents to prevent unintended changes. By introducing a three-step gating process—Ask, Plan, and Confirm—developers can ensure that agents check for ambiguities, outline necessary changes, and obtain explicit approval before implementation. This approach mitigates risks and enhances code quality.
image: /wp-content/uploads/2026/08/agents-that-plan-before-they-code-hero.png
---

The scariest thing about a genuinely capable coding agent is how quickly it commits. You type two sentences, and forty seconds later there are changes across nine files, half of which you did not want and one of which quietly changed a query you spent a week hardening. The agent was not wrong about how to implement the thing. It was wrong about what the thing was, and it never stopped to check.

I have watched this happen enough times that I stopped treating it as a prompting problem and started treating it as a workflow problem. A better one-shot prompt is not the fix. A gate is: the agent is not allowed to edit files until it has asked what it needs to ask, shown me a plan, and gotten a yes.

## Why speed is the problem

Human engineers have a built-in pause. Before a senior developer touches your codebase they ask a couple of questions, sketch the approach, maybe drop a comment on the ticket. That pause is where the wrong-work gets caught, cheaply, in a sentence, instead of expensively, in a diff you have to read and reject.

Agents removed the pause. That is most of their value and most of their danger in the same motion. An agent that implements immediately optimizes for the wrong thing: it treats “produce a diff” as the goal, when the goal was “produce the diff we agreed on.” The gap between those two is where the deleted work and the silent scope creep live.

That gap is not a knowledge problem. The agent knows how to write the code. It just never checked that it was writing the right code.

[![Diagram explaining the importance of speed in work processes, contrasting 'no gate' and 'the gate' approaches. It highlights potential problems and costs associated with each method.](/wp-content/uploads/2026/08/plan-first-fig2-why-speed.png)](/wp-content/uploads/2026/08/plan-first-fig2-why-speed.png)

*The same task, gated and ungated. Skipping the pause trades a small, predictable cost for a large, unpredictable one.*

So I gave the pause back, deliberately, as a standing instruction on every agent in the InterlinedList repo.

## The three beats

The workflow is written down in `.claude/workflows/plan-first.md` and every agent links to it. It is three beats, in order, and implementation is gated behind all three.

[![A flowchart titled 'The Gate' illustrating a process for implementation that requires three steps: Prompt, Ask, Plan, Confirm, and Implement. It emphasizes the sequence and conditions under which implementation occurs, highlighting the need for clarification and approval before proceeding.](/wp-content/uploads/2026/08/plan-first-fig1-the-gate.png)](/wp-content/uploads/2026/08/plan-first-fig1-the-gate.png)

*The three beats, in order. Nothing is edited until all three pass, and work that grows past the approved plan loops back to re-plan rather than quietly expanding.*

**Ask.** Surface what the prompt left open before committing to an approach. Ambiguous scope, unstated edge cases, a product decision hiding inside a technical request, whether a feature should be tier-gated. The migrations agent asks about column types and nullability and whether anything destructive is implied. The Next.js agent asks which surfaces are in and out. The rule has an escape hatch, because asking three questions about a one-line copy fix is its own kind of annoying: skip the questions only when the request is genuinely unambiguous and low-risk. When in doubt, ask. A pointed question is cheaper than a wrong build every single time.

**Plan.** Before touching files, lay out the shape of the change: the files and routes and components you will touch, the ones you will deliberately leave alone, the approach, any migration (additive, always), the tests the change needs, and anything risky. In this repo “risky” has a specific meaning: auth, IDOR, subscription gating, SSRF, secret handling, anything destructive or hard to reverse. The plan is a decision aid, not a document. It should be short enough to read in one breath and specific enough that approving it means something.

**Confirm.** Implement only after an explicit yes. If the plan changes in the back-and-forth, restate the revised version and get the yes again. And the part that actually matters over a long session: approval is scoped to the plan that was approved. If the work grows past it, the agent stops and re-plans instead of quietly expanding. That last clause is what keeps a “small fix” from turning into an afternoon of changes I never signed off on.

## What it looks like per agent

I did not want one generic paragraph pasted eight times. The gate is the same, but what you ask about depends on the job, so each agent got the beats written for its lane.

[![A diagram featuring multiple lanes labeled with different topics: Migrations, Next.js, End-to-end, Docs, Unit testing, and Blog. Each lane has brief descriptions of its scope, accompanied by specific tags.](/wp-content/uploads/2026/08/plan-first-fig3-per-agent.png)](/wp-content/uploads/2026/08/plan-first-fig3-per-agent.png)

*One gate, written for each lane. The two read-only reviewers pick the full gate back up the moment they move from finding to fixing.*

The **migrations** agent plans the exact idempotent `migration.sql` and confirms it is purely additive before it applies anything. The **unit-testing** agent asks which behaviors to lock in and which boundaries to mock, then lists the cases each test file will assert. The **e2e** agent names the flows, the auth and seed prerequisites, and the breakpoints that matter. The **docs** agent confirms which of the three docs is in scope and whether a new page is needed. The **blog** agent (yes, this one) settles the angle and the section arc and which real code it will verify claims against before drafting a word.

The two read-only reviewers are the interesting edge. Security and UX do not implement, so there is no edit to gate. For them the gate degrades to its first beat: confirm the review scope if it is ambiguous (which routes, how deep, which breakpoints), then produce findings. But the moment the user says “now fix what you found,” they are implementers, and the full ask-plan-confirm gate snaps back on before they touch code. The reviewer does not get to slide from “here is a finding” into “and I fixed it” without crossing the same line everyone else crosses.

## The obvious objection

This is slower. That is the point, and it is also not as true as it sounds. The plan step costs you a few seconds and one read. Rejecting a forty-second nine-file diff that went the wrong direction costs you the read plus the reject plus the re-prompt plus the nagging worry about what it touched that you did not catch. The gate front-loads a small, predictable cost to avoid a larger, unpredictable one. Over a day of handoffs it is not close.

It also composes with the other habit I built into these agents: every one of them does its work in an isolated [git worktree](/2026/08/19/worktrees/), on its own branch, torn down when the task lands. Plan first, then do the approved work in a sandbox that cannot collide with anyone else. The worktree contains the blast radius. The plan makes sure there is not supposed to be a blast in the first place.

The pause was always the expensive part of good engineering. Worth teaching the machines to keep it.

*I’m [Adron](https://interlinedlist.com/user/adron), brainstorming and building [InterlinedList](https://interlinedlist.com/).*
