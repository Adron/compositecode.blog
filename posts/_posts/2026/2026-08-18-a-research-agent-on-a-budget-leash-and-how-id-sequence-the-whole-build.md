---
title: A Research Agent on a Budget Leash, and How I’d Sequence the Whole Build
date: 2026-08-18 06:30:00 -0700
last_modified_at: 2026-08-10 23:23:10 -0700
permalink: /2026/08/18/a-research-agent-on-a-budget-leash-and-how-id-sequence-the-whole-build/
slug: a-research-agent-on-a-budget-leash-and-how-id-sequence-the-whole-build
wp_id: 75060
original_url: https://compositecode.blog/2026/08/18/a-research-agent-on-a-budget-leash-and-how-id-sequence-the-whole-build/
categories:
- AI & AI Tooling
- interlinedlist
- Temporal
- Unknown Code Ramblings
tags:
- interlinedlist
- programming
- temporal
excerpt: Part 8 emphasizes building a supervised AI agent within a structured workflow using Temporal, focusing on retrieval, reasoning, and drafting without overspending on model tokens. The author outlines the importance of sequencing the development, integrating guardrails like budget limits, and asserts that trust in the agent comes from structured testing and supervision, not vague prompts.
image: /wp-content/uploads/2026/08/08-agentic-research-on-a-budget-hero-1.png
---

**Part 8 of 8: Durable AI for InterlinedList**

---

Back in [Part 1](/wp-content/uploads/2026/08/01-why-temporal-durable-ai-hero-1.png), I said the whole series was one argument dressed up as eight posts. LLM tokens are the expensive thing, Temporal is not, and Temporal’s mechanics structurally push the token bill down. I also said the way I’d *build* it was to brainstorm against the real code first, then hand the agent structure instead of hope. This is where those two threads tie together.

The capstone I keep circling back to is the one that sounds the most like science fiction and is actually the most dangerous to ship carelessly: “research topic X from my saved links and draft a document with citations.” The agent retrieves. It reasons. It drafts. And if I’m not careful, it also burns through a month of my inference budget in one runaway loop while I’m asleep.

So this post is two things. The agent itself, and the playbook for building everything that came before it. The agent is the thing you build last, and the order it sits on top of is the part I actually want to argue for.

## The Capstone Is Just the Earlier Pieces, Composed

This part should feel earned by now. The agentic-research-to-draft phase, the last of the proposals, doesn’t invent anything. It *composes*.

The link content from Part 5 (the crawl-and-cache that turns your saved URLs into readable text) is the agent’s source material. The retrieval from Part 5’s second half, the pgvector search over your own docs, lists, and messages, is how the agent finds the relevant three paragraphs instead of stuffing forty links into context. And the durable generation from Part 3, the workflow that survives a timeout and asks before it writes, is the drafting step.

Compose those three and you get an agent loop: retrieve, reason, retrieve again, draft, cite. Each of those steps is already an activity I’d have built and tested for its own feature. The agent is a workflow that calls them in a loop the model steers.

Which is exactly where it gets scary. A loop the *model* steers has no natural stopping point. It’ll keep deciding it needs one more search, one more fetch, one more pass at the draft. That’s not a bug in the model. That’s what an agent *is*. The bug would be letting it run unsupervised.

## Temporal Supervising an LLM Agent Is a Nice Recursion

I like this framing because it’s a little bit funny. Temporal is an orchestrator whose entire job is supervising unreliable, long-running, retry-heavy work. An LLM agent is unreliable, long-running, retry-heavy work. So the agent runs *inside* a Temporal workflow, and the workflow is the adult in the room.

Three guardrails, all first-class workflow logic, none of them prompt-hope:

A **hard token budget.** Before every model call, the workflow calls `assertBudget`, the same primitive from Part 7 that reads the `AiGeneration` ledger and throws a non-retryable `BudgetExceeded` when the user’s daily or monthly ceiling is hit. The agent can *want* another search all it likes. If the budget’s gone, the call never fires.

A **max-step cap.** The loop counts its own iterations. Twelve steps, or whatever I tune it to, and it’s done. It drafts with what it has rather than spiraling.

A **wall-clock timeout.** Temporal’s workflow timeout means even a wedged agent eventually stops, cleanly, with whatever it produced so far.

And here’s the piece that makes the whole thing cost-sane instead of terrifying: **every step is memoized.** If the agent fails at step 9 of a 12-step loop (provider hiccup, worker restart, whatever) the workflow *resumes* at step 9. It does not re-run steps 1 through 8. It does not re-pay for the eight model calls it already made. In a serverless handler, a mid-loop failure means starting the whole expensive agent over. Here it means retrying one step.

Sketching the loop, this is the shape I’d hand Claude to fill in:

```
// Proposed: the supervised agent loop as a Temporal workflow.
export async function researchAgentWorkflow(input: ResearchInput): Promise<Draft> {
  const MAX_STEPS = 12;
  const context: Snippet[] = [];

  for (let step = 0; step < MAX_STEPS; step++) {
    // Governor first: a hard ceiling the agent cannot talk past.
    await assertBudget(input.userId);

    // Cheap model plans the next move over the small retrieved context.
    const move = await planNextStep({
      model: "claude-haiku-4-5",
      goal: input.topic,
      context,
    });

    if (move.type === "done") break;

    // Retrieval is mechanical and nearly free. No expensive tier here.
    const hits = await retrieveFromLinks(input.userId, move.query);
    context.push(...hits); // stays small: top-k snippets, not whole pages
  }

  // Expensive tier runs exactly once, on the final synthesis.
  return await draftWithCitations({
    model: "claude-opus-4-8",
    topic: input.topic,
    context,
  });
}
```

The cost story lives in the model choices, not the prose. Retrieval and planning run on a cheap tier: Haiku for the “what should I look for next” decisions, which are frequent and small. Opus 4.8, the expensive tier, runs once, on the final synthesis, over a retrieval-augmented context that stayed deliberately small the whole way through. I’m not paying Opus prices to decide which link to read next. I pay them for the draft, and that’s the one thing in the loop I think is worth it.

No clever prompt is doing that. The structure is.

## How I’d Sequence the Whole Build

If you’ve read the series straight through, you might be tempted to build the shiniest thing first. Don’t. The agent ships *last*, and the ordering underneath it is the real deliverable of this post, because every step ships value on its own and nothing is a big-bang.

Here’s the order I’d hand myself:

**1. The foundation phase: the Temporal worker and the cost primitives.** The worker, the client wiring, the `llmCall` activity with the model cascade, `assertBudget`, the response cache. This is the groundwork everything else stands on, and nothing works without it. Mostly infra, not code, and it’s a week.

**2. The durable publish and idempotency fix, pure win, no LLM.** This is the one from Part 4: the every-minute cron that can double-publish because a partial failure re-runs on the next tick. Rebuild it as a Temporal Schedule with the message id as the workflow id, so a given message can never be published twice. Zero model tokens. It fixes a *current* production hazard. If I could only ship one thing from this whole series, it’d be this.

**3. Durable Generate plus confirm.** Part 3. Long docs stop blowing the function budget, and a wrong list schema never gets silently written because the workflow pauses on a signal and waits for a human. This is the in-product generate button, on solid footing.

**4. Link crawl, then retrieval.** Part 5. Crawl the links into a cache (the cheapest, highest-cache-value piece in the set) then layer pgvector retrieval on top. This is “where did I save that article?”

**5. Batch enrichment, then prompt-to-list.** Part 6. The fan-out that tags everything and expands anything without re-billing completed calls, then the “build a list from a sentence” flow composed on top of it.

**6. The AI calendar and digests.** Part 4’s second half. Now that publishing is durable, the calendar planner and the scheduled digests have solid ground to schedule onto.

**7. The cost dashboard, then the agent.** Part 7’s dashboard makes “cheap” *visible*: tokens, cache-hit rate, budget remaining. I want that governor on-screen *before* I ship the most token-hungry feature in the whole set. Then, and only then, the agentic capstone.

The rule underneath the whole ordering is that value ships at every step. The publish fix helps users who never touch AI. The link cache is useful before any retrieval sits on it. The dashboard is useful before the agent exists. I’m never in a state where I’ve spent three weeks and have nothing a user can hold.

## The Verification Is Where the Trust Actually Lives

The meta-point of the whole series is this one, so I’ll say it flat. You do not trust an autonomous agent because the prompt was good. You trust it because it runs inside guardrails, and because tests prove the properties you care about are there.

So the verification for the agentic capstone, and everything under it, is not an afterthought. It’s the thing that makes any of this shippable:

**Vitest unit tests** for the activity logic and the cost math. Does the cascade pick the cheap model for planning? Does `assertBudget` throw at the right ledger sum? Pure functions, no DB, fast.

**Temporal replay tests** that prove a workflow resumes correctly after a simulated worker crash. This is how I *prove*, not hope, that a retry doesn’t restart the expensive agent from step zero.

**An idempotency test** that starts two publish workflows with the same message id and asserts exactly one publish. That’s the double-post race, closed and locked.

**Cost-assertion tests**, the ones I care about most for the agent. Fail an activity mid-pipeline and assert the already-completed model calls are *not* re-invoked on retry. Memoization is money, and this test is how I know the money’s saved.

**Playwright E2E** for the generate to confirm to write flow, so the human-in-the-loop gate works in a real browser and not just in my head.

**A security pass** before any PR: SSRF on the crawler (everything through `safeFetch`), IDOR on every workflow write (`where: { id, userId }`), prompt-injection defaults (artifacts private by default so a poisoned link can’t publish on your behalf), and budget-bypass attempts.

And every schema change (the `LinkContent` table, the pgvector column, the response cache) goes through the strict additive migration workflow. Hand-written, idempotent, applied to both databases. No `prisma db push`, no shortcuts. That workflow has broken production before, precisely when someone skipped it.

## What I Actually Learned Working With Claude

The lesson closes the loop the series opened. Supervise the agent with structure, let the tests carry the trust, and it turns out that’s also how I’ve been building *with* Claude the whole time.

You don’t hand an agent a vague goal and hope. You hand it constraints: a budget it can’t exceed, a step count it can’t blow past, a timeout it can’t outlast. Then you make it write the tests that prove those constraints hold, the replay test, the idempotency test, the cost-assertion test. What makes the agent trustworthy is the wall around it, not how nicely I phrased the ask.

And that’s true one level up too, which I didn’t expect going in. Sequencing the build so each step is independently verifiable (the publish fix before the calendar, the cache before retrieval, the dashboard before the agent) is the same move as capping the agent’s steps. Give the work boundaries, make the boundaries checkable, prove them before moving on. Whether the thing on the leash is a research agent or my own plan to build one, the leash is what I trust.

I’ve been brainstorming this out loud for eight posts. The pieces are grounded in code that already exists: the `safeFetch` guards, the DSL, the crosspost fan-out, the cron that really does risk a double-post. None of it is shipped. All of it is buildable, in the order above, with value at every step. So I’m going to start at step one and build the durable publish fix, because it’s a pure win with no model tokens and it closes a real hazard. I’d love for you to follow along, as I am going to move forward now and implement this. If you’re interested, subscribe!

*[Adron](https://interlinedlist.com/user/adron) brainstorming and working on [InterlinedList](https://interlinedlist.com/).*
