---
title: Making LLM Features Cheap Enough to Actually Ship
date: 2026-08-17 09:30:00 -0700
last_modified_at: 2026-08-10 23:18:16 -0700
permalink: /2026/08/17/making-llm-features-cheap-enough-to-actually-ship/
slug: making-llm-features-cheap-enough-to-actually-ship
wp_id: 75059
original_url: https://compositecode.blog/2026/08/17/making-llm-features-cheap-enough-to-actually-ship/
categories:
- AI & AI Tooling
- interlinedlist
- Temporal
tags:
- interlinedlist
- programming
- temporal
excerpt: In Part 7 of the series, the author emphasizes the significance of durability in AI to minimize costs, particularly focusing on memoization and caching techniques. They outline strategies to prevent unnecessary token expenses during retries and propose a structured approach to optimize budget management before any billing occurs, ensuring efficient usage of resources throughout the AI processing pipeline.
image: /wp-content/uploads/2026/08/07-the-cost-governor-hero-1.png
---

**Part 7 of 8: Durable AI for InterlinedList**

---

Six posts in, and I’ve been dancing around a number. Every proposal I’ve sketched (durable generate, the calendar planner, the link crawler, batch enrichment) carries a cost, and the expensive part is never Temporal. It’s the tokens. A worker box and a managed Temporal namespace run me on the order of tens of dollars a month (obviously at this time), flat, whether they process ten jobs or ten thousand. The model bill is the one that scales with usage. *It’s also the one that decides whether an AI feature is worth shipping or is a slow-motion budget fire*.

So this post is the payoff. Durability isn’t just nice, durability is *money*. The mechanics I keep reaching for aren’t in the plan because they’re clever. They’re there because each one structurally drives the token bill down, and does it in a way I can measure instead of squint at and hope for. Keeping this cheap relative to the Claude and ChatGPT APIs was never a footnote I tacked onto the series. It’s been the point the whole way through.

None of this is live yet. AI assistance in the product is still marked Coming Soon. This is me brainstorming the cost layer I’d build, and how I’d hand it to Claude to build with me.

## The Single Biggest Saver Is Not Re-Paying for Work You Already Did

Start with the one that matters most. Durable memoization.

When a Temporal workflow runs an activity (say, an `llmCall` that generates a document section) the result gets persisted the moment it completes. If the workflow later fails and retries, it does not re-run that activity. It replays the history, sees the completed result, and moves on.

Think about what that means on a six-step generation pipeline that dies at step five. Without durability, a retry starts over: steps one through four re-invoke the model, and you pay for all four again just to get back to where you already were. With Temporal, the retry re-runs step five and *only* step five. Steps one through four are already-billed calls that never happen twice.

That’s the difference between retries as a cost multiplier and retries that are free. On a batch enrichment job that fails at item 47 of 50, you re-bill item 47, not items 1 through 46. I wrote a whole post about that in Part 6, and it’s the same mechanic every proposal here leans on. Memoization is why a flaky provider or a worker restart doesn’t torch the budget.

## Cheapest Model First, Escalate Only on Demand

The next lever is refusing to reach for the expensive tier by default. The `llmCall` activity would run a **model cascade**: cheapest capable tier first (Haiku-class, Flash-class), escalating only when the task actually needs it.

Most of what these features do is mechanical. Tagging a message. Summarizing a row. Extracting a field. That work does not need a frontier model, and paying frontier rates for it is just lighting money on fire. So the cascade defaults to cheap, and it reserves the Opus-class tier for the thing the user explicitly asked for: long-form synthesis, a research draft, a document they told me they want written well.

Paired with that: per-target `max_tokens` ceilings, so a runaway generation can’t balloon. A message caps around 1k, a list around 4k, a document around 16k. The ceiling isn’t a polite suggestion the model is vaguely aware of. The activity enforces it as a hard cap. So you get the cheap tier by default, a small ceiling per target, and the expensive model only shows up when you asked for it.

## A Gate That Throws Before It Spends

Cascades and ceilings keep individual calls cheap. But the scenario that scares me is unbounded spend: a runaway agent loop, or a leaked user key someone else is now happily burning. So the plan puts a budget gate *before* every call, not after.

An `assertBudget` activity reads accumulated spend from the `AiGeneration` ledger and throws a **non-retryable** `BudgetExceeded` when the user is over their ceiling. Non-retryable is the important word. A normal failure retries; this one halts the workflow cold, because retrying a budget breach just tries again to spend money you’ve already said no to.

Roughly what I’d hand to Claude as the shape:

```
// activity: runs on the worker, before any billable llmCall
export async function assertBudget(userId: string, estimate: TokenEstimate): Promise<void> {
  const spent = await getSpendThisPeriod(userId); // counts only, from AiGeneration
  const remaining = budgetFor(userId) - spent;

  if (estimate.maxTokens > remaining) {
    // non-retryable: a budget breach must not loop and re-attempt the spend
    throw ApplicationFailure.nonRetryable(
      `Budget exceeded: need ${estimate.maxTokens}, have ${remaining}`,
      "BudgetExceeded",
    );
  }
}
```

A workflow calls `assertBudget` and then `llmCall`, in that order, every time. Worst case is a bounded overspend of one call, never an open tap.

## Never Bill the Same Request Twice

Then there’s the plain-dumb-obvious saver: caching. A response cache keyed by `hash(system + prompt + model)`. If an identical request comes through (same system prompt, same user prompt, same model) it’s served from cache and never re-billed. Regenerate the same summary twice, pay once.

Same idea one layer down for link work: URL-hash dedup. When the crawler from Part 5 fetches and embeds a link, it keys on a hash of the URL. A link shared across ten messages, three docs, and a list row gets fetched, extracted, and embedded exactly once, ever. Embeddings are already orders of magnitude cheaper than generation, so computing them once and caching forever makes the cheapest part of the pipeline round down to nothing.

And to keep from wasting tokens on *retries you caused yourself*: worker concurrency and task-queue rate caps tuned to stay under provider limits. Blow past a rate limit and you get a 429 storm, and every retry in that storm is wall-clock and, on some providers, tokens down the drain. Obeying the limit is cheaper than fighting it.

One more, because it’s the most satisfying: confirm-before-spend. For the prompt-to-list flow, the workflow generates the schema, then pauses on a Signal and waits. It does not spend a single row-generation token until the user confirms the schema is right. Get the schema wrong and you’ve spent one cheap schema call, not fifty row calls against a shape nobody wanted. That pause is impossible in a serverless handler and native in Temporal.

## The Ledger Counts, It Doesn’t Read

Every one of these levers needs a source of truth, and that’s the `AiGeneration` ledger. Critical design decision: it records **counts and status only**. Tokens in, tokens out, which model, succeeded or failed. It never stores the prompt text or the model output.

That’s not laziness. One table does three jobs. Privacy, because I’m not warehousing what people wrote or what the model said back. The quota counter, because `assertBudget` reads its sums off it. And the cost dashboard, because those same rows drive a per-user “AI usage and spend” view: tokens, calls, cache-hit rate, budget remaining. When something looks expensive, the ledger doubles as the debugging trail. You can see *that* a workflow made forty calls without ever seeing *what* it said.

## Build the Guardrails With Claude, Then Make It Prove Them

Now the part I’ve been wanting to get to, because this is where working with an LLM changed how I’d approach any of it.

Memoization and caching only save money if they’re in the *right places*. Put a cache breakpoint one step too early and you re-bill everything after it. Miss a memoization boundary and a retry quietly re-runs a paid call. The savings are entirely a function of where the boundaries land, and eyeballing a six-step pipeline for those boundaries is the kind of thing I get wrong.

So the first move is a diagnostic question, not a code request. I’d point Claude at the actual workflow and ask: *“walk this pipeline and tell me exactly where a retry would re-bill the model.”* Then let its answer drive placement. It reads the activity boundaries, traces the retry path, and tells me which calls are already durably memoized and which ones a mid-pipeline failure would re-invoke. That answer is the map. The caching and memoization go where the map says, not where I guessed.

The second move matters more: make it prove the savings. Memoization you can’t prove is just a hope with good intentions. So I’d have Claude write a Temporal replay test (using `TestWorkflowEnvironment`) that fails an activity partway through the pipeline and then *asserts the already-completed LLM activities are not invoked again on retry*.

```
it("does not re-bill completed LLM activities on retry", async () => {
  const llmCall = vi.fn()
    .mockResolvedValueOnce("step-1 result")
    .mockResolvedValueOnce("step-2 result")
    .mockRejectedValueOnce(new Error("provider blip at step 3")) // fail mid-pipeline
    .mockResolvedValue("step-3 result (retry)");

  await worker.runUntil(client.workflow.execute(generatePipeline, { /* ... */ }));

  // steps 1 and 2 completed before the failure, so Temporal replays their
  // memoized results and MUST NOT call the model for them again.
  const stepsCalled = llmCall.mock.calls.map((c) => c[0].step);
  expect(stepsCalled.filter((s) => s === 1)).toHaveLength(1);
  expect(stepsCalled.filter((s) => s === 2)).toHaveLength(1);
  expect(stepsCalled.filter((s) => s === 3)).toHaveLength(2); // failed once, retried
});
```

That test is the proof. It fails loudly the day someone refactors the pipeline in a way that breaks memoization and starts silently re-billing steps one and two. The savings stop being a story I tell about the architecture and start being a property CI enforces. Same loop for the response cache: a test that fires two identical requests and asserts the second one hits cache and never reaches the model.

Ask the agent where the money leaks. Let its answer place the guardrails. Then make it write the test that locks them in. That loop works because a cost regression is invisible until the bill shows up weeks later, and a test drags it into the light on the exact commit that caused it, while you can still `git blame` your way back to it.

## Where This Lands

Part 8 is the capstone: the agentic research-to-draft flow, the single most token-hungry thing in the whole set. It’s the reason every governor in this post has to exist before it ships. I’ll also lay out how I’d sequence the entire build, starting from the foundation phase (the Temporal wiring and the shared cost primitives everything else reuses) and working all the way up to the agent, and how I’d verify each piece as it lands.

*[Adron](https://interlinedlist.com/user/adron) brainstorming and working on [InterlinedList](https://interlinedlist.com/).*
