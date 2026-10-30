---
title: Tag Everything, Expand Anything, Without Re-Billing the Model
date: 2026-08-16 09:30:00 -0700
last_modified_at: 2026-08-10 23:18:39 -0700
permalink: /2026/08/16/tag-everything-expand-anything-without-re-billing-the-model/
slug: tag-everything-expand-anything-without-re-billing-the-model
wp_id: 75057
original_url: https://compositecode.blog/2026/08/16/tag-everything-expand-anything-without-re-billing-the-model/
categories:
- Unknown Code Ramblings
tags: []
excerpt: 'Part 6 of 8: Durable AI for InterlinedList Every serverless AI feature I’ve built hits the same wall the second someone wants it at scale. “Can it tag all my untagged messages?” Sure, one message. “All of them?” Now we’re talking about a job that runs for minutes, touches hundreds of items, and will absolutely …'
image: /wp-content/uploads/2026/08/06-batch-enrichment-at-scale-hero-1.png
---

**Part 6 of 8: Durable AI for InterlinedList**

---

Every serverless AI feature I’ve built hits the same wall the second someone wants it at scale. “Can it tag all my untagged messages?” Sure, one message. “All of them?” Now we’re talking about a job that runs for minutes, touches hundreds of items, and will absolutely fall over partway through. And when it falls over, the naive version starts from zero and re-bills you for every item it already finished. Nobody wrote that behavior on purpose. It’s just what you get by default, and it’s expensive.

This is the post in the [Durable AI series](https://github.com/CompositeCode/interlinedlist/blob/develop/docs/plans/blogs/00-series-index.md) where durability pays off the most. Not “nice to have.” It’s the biggest cost saver in the whole series, and I’m putting that up front so you don’t skim past it.

## The Jobs That Don’t Fit in a Request

There’s a whole class of work InterlinedList can’t do today and won’t be able to do inside a Vercel function, no matter how the AI plan lands. It’s the bulk stuff:

- “Add 20 rows to this list matching X.”
- “Tag every untagged message.”
- “Summarize each finished book in my reading list into its own document.”
- “Backfill link previews across all my docs.”

What these share is that they’re multi-minute, many-item, and retry-heavy. A serverless handler has a hard duration ceiling and no durable state between invocations. If item 34 of 50 throws a 429 from the model provider, the whole request dies and there’s no clean way to pick up at 35. So you either don’t offer the feature, or you ship a fragile version that quietly loses work and double-charges for the rest.

Today’s ground truth matters here, so let me be precise. Lists are a Subscriber feature. A list’s row data is stored as JSONB in `ListDataRow.rowData`, validated against a user-defined schema. The validator that gates every row lives in `lib/lists/dsl-validator.ts`. None of the batch AI machinery below exists yet: this is a brainstorm I’d hand to Claude to build, and AI assistance in the product is still “Coming Soon.” I’m designing it out loud.

## The Shape: Fan Out, Cap Concurrency, Track Progress

The design I keep landing on is a generic fan-out workflow. One workflow supervises the whole batch; **one item equals one activity.** Each activity is independent and idempotent. It does its work, writes its result, and doesn’t care whether its neighbors succeeded or failed.

Temporal is the durable engine underneath, for reasons that are specific and not hand-wavy:

**Partial progress is preserved.** A completed activity’s result is persisted. When the workflow retries after a failure at item 47 of 50, it re-runs item 47 and only item 47. Items 1 through 46 already succeeded and their results are memoized, so it doesn’t touch them. On a batch of 50 LLM calls where one flakes, you re-bill one item, not fifty. This is the money argument, and I like it because it’s structural. You get it from the shape of the thing, not from remembering to code it.

**Concurrency is capped.** You don’t fire 50 model calls at once and trigger a 429 storm. A 429 storm is expensive twice over: the retries burn wall-clock, and on some providers they burn tokens too. Cap concurrency to a small number and you respect the provider’s rate limit (and your own BYO-key limit), so the retries never happen at all.

**The job survives a worker restart.** Deploy mid-batch, crash the worker, whatever. The workflow resumes from where it was, not from zero.

Here’s the constraint made concrete: a generic `batchEnrich` workflow that fans out over items with a bounded concurrency window.

```
// Workflow: supervises the batch, never touches the model or the DB directly.
export async function batchEnrich(input: BatchEnrichInput): Promise<void> {
  const { items, concurrency } = input; // e.g. concurrency = 5
  const running: Promise<void>[] = [];

  for (const item of items) {
    // enrichItem is an ACTIVITY: its result is durably memoized.
    // On a workflow retry, already-completed items are NOT re-invoked.
    // Temporal replays their recorded results instead of re-billing them.
    const p = enrichItemActivity(item).then(() => {
      recordProgress(item.id); // drives the live progress UI
    });
    running.push(p);

    // Cap in-flight work so we never exceed the provider / BYO-key rate limit.
    if (running.length >= concurrency) {
      await Promise.race(running);
      // prune settled promises so the window stays at `concurrency`
    }
  }

  await Promise.all(running);
}
```

The per-item activity is where the real work (and the idempotency) lives. It reuses code that already ships in the repo:

```
// Activity: one item. Independent, idempotent, individually retryable.
export async function enrichItemActivity(item: EnrichItem): Promise<void> {
  // 1. Cheap-model call for the mechanical part (tag / summarize).
  const enriched = await llmCall(item.prompt, { model: "cheap" });

  // 2. Validate against the list's real schema before writing anything.
  //    validateFormData lives in lib/lists/dsl-validator.ts, the same gate
  //    the app uses for every human-entered row.
  const result = validateFormData(item.fields, enriched.rowData);
  if (!result.isValid) throw new NonRetryableError(result.errors);

  // 3. Write through the existing materialize helpers, not raw Prisma.
  //    lib/materialize/build-list.ts / build-doc.ts already know how to
  //    turn structured data into rows and documents with ownership intact.
  await writeThroughMaterialize(item.target, enriched);
}
```

Nothing here reinvents validation or writing. `validateFormData` is the existing row validator. `lib/materialize/build-list.ts` and `build-doc.ts` are the existing builders that turn structured content into lists and documents. The persistence writers I sketched back in the foundation phase, the groundwork everything in this series stands on, handle the actual writes with IDOR checks intact. The workflow’s only job is orchestration: fan out, cap, track, resume.

## The Cost Levers, Stacked

Cost is the spine running through this whole series, so let me connect the dots. Three levers push the LLM bill down, and this one feature stacks all three:

**Batching.** Tagging is mechanical and small. Instead of N calls to tag N messages, one call tags a batch of them: you collapse the per-request overhead and the token duplication of repeating the same system prompt N times over. Fan-out doesn’t have to mean one-model-call-per-item. The fan-out unit can itself be a batch.

**A cheap-model default.** Tagging and summarizing don’t need a frontier model. They need a competent, fast, cheap one. Claude Haiku 4.5 runs at $1 per million input tokens and $5 per million output; Opus 4.8 is $5 and $25. That’s a 5x swing for mechanical work where the cheap tier does the job fine. The default model for a batch-tag job should be the cheap one, and you escalate only for the rare task that needs it.

**No redo on retry.** Memoization again: the durable engine never re-invokes an already-billed call on a retry. This is the lever that costs you nothing to pull, because it’s baked into how the workflow resumes.

Put those together and a “tag everything” run over a few hundred messages costs cents instead of dollars, and a mid-run failure costs you one retry instead of a full re-run.

## What I’d Tell Claude Before It Writes Anything

There’s a “working with Claude” lesson buried in all this, and honestly it’s why I wanted to write this post at all.

**Resumability is a design constraint, not a feature you bolt on later.** Ask an agent to “write a batch tagging job” and say nothing else, and you get a `for` loop that calls the model N times and stores results at the end. It works in the demo. Then it falls over on the first real batch, loses partial work, and re-bills everything on retry. Now you’re spending a day retrofitting durability into code that was never shaped for it, and durability doesn’t retrofit cleanly, because it changes what a “unit of work” even is.

So I state the constraints before the code, right in the prompt:

> Each item is an independent, idempotent activity. The workflow must resume mid-batch without re-running finished items: a failure at item 47 of 50 re-processes only item 47. Cap concurrency at N to stay under the provider rate limit. Validate every item against the list schema before writing, and write through the existing materialize helpers, not raw Prisma.

Hand it *that*, and Claude generates the right thing: the generic `batchEnrich` workflow, the per-target activity adapters (list rows go through `build-list`, documents through `build-doc`, message tags through the tag writer), and the batched prompt that tags many items in one call. The constraints do the architectural work; the agent fills in the wiring. I own the seam (what’s an activity, what’s idempotent, where the concurrency cap lives) and let it own the code.

The failure mode I’m avoiding is the one where the constraint shows up *after* the code. State “don’t re-bill completed items” up front and it shapes the whole structure. State it after, and you’re rewriting.

## The Surface

On the product side this becomes a “run a bulk action” panel: pick a target (a list, your messages, a set of docs), describe the enrichment, and watch live progress as items complete. Cancel is a Temporal Signal, a real mid-flight stop rather than a “please ignore the results” fiction. The workflow receives the signal, stops fanning out new items, lets the in-flight ones finish or abort, and reports what it got done. Progress and cancel both fall out of a workflow that already tracks per-item state.

Part 7 is the payoff post: the cost governor, where all of these levers get formalized into a budget ledger, a model cascade, and the response cache that make “cheap enough to ship” measurable instead of hoped-for.

*[Adron](https://interlinedlist.com/user/adron) brainstorming and working on [InterlinedList](https://interlinedlist.com/).*
