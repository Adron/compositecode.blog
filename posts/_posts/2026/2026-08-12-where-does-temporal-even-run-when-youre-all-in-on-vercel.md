---
title: Where Does Temporal Even Run When You’re All-In on Vercel?
date: 2026-08-12 06:30:00 -0700
last_modified_at: 2026-08-12 01:21:47 -0700
permalink: /2026/08/12/where-does-temporal-even-run-when-youre-all-in-on-vercel/
slug: where-does-temporal-even-run-when-youre-all-in-on-vercel
wp_id: 75020
original_url: https://compositecode.blog/2026/08/12/where-does-temporal-even-run-when-youre-all-in-on-vercel/
categories:
- AI & AI Tooling
- interlinedlist
- Temporal
tags:
- interlinedlist
- programming
- temporal
excerpt: The content discusses integrating Durable AI into a serverless application, InterlinedList. The challenge arises from needing persistent components, like Temporal services and workers, which conflict with the serverless model. The solution involves adding one always-on worker to manage tasks while reusing existing codebase and maintaining app structure, ensuring budget control and process integrity.
image: /wp-content/uploads/2026/08/02-where-temporal-runs-vercel-hero-1.png
---

**Part 2 of 8: Durable AI for InterlinedList**

---

In [Part 1](https://github.com/CompositeCode/interlinedlist/blob/develop/blog/i-ve-been-brainstorming-durable-ai) I talked myself into Temporal as the orchestration layer for the AI features I want to build. Durable memoization, a model cascade, a hard budget gate: all the mechanics that push the LLM bill down. Good story. Then I hit the question that stops most “let’s just add Temporal” plans cold, and it stopped me too.

Where does it actually run?

InterlinedList is 100% serverless on Vercel. Every route is a function that spins up, does its thing, and gets torn down. That model is wonderful right up until you need something that never stops running. And Temporal needs exactly that.

## The Two Parts That Don’t Fit

Temporal has two moving pieces, and neither of them is a serverless function.

The first is the **Temporal Service**, the durable-state backend. It’s the thing that remembers where every workflow is, what’s completed, what’s pending, and what to retry. It’s stateful infrastructure. You don’t invoke it and let it die.

The second is the **Worker**. A worker is a long-lived process that polls a task queue, picks up work, and runs your activities. Polls it continuously. As in, forever. A Vercel function that shuts down after a request cannot be a Temporal worker, because the polling loop dies the instant the function returns. You can’t flag your way out of this in a config file. It’s a straight-up mismatch between “poll a queue for hours” and “respond in seconds then vanish.”

So for a while this felt like a dead end. Adding Temporal seemed to mean un-serverless-ing the whole app, and I did not build InterlinedList on Vercel just to go stand up a fleet of always-on boxes.

## One New Always-On Thing. That’s It.

The resolution I kept circling back to is smaller than the fear suggested. I introduce **exactly one** new always-on component: a small `@temporalio/worker` process running somewhere cheap and boring, like Fly.io, Railway, or a small VM. Something in the five-to-twenty-dollars-a-month range. Alongside it, either self-hosted Temporal OSS or a low-tier Temporal Cloud namespace for the service.

That’s the entire footprint. One worker, one service. Vercel doesn’t change shape at all.

What *does* change is what the Vercel routes do. They stop doing work and become thin clients. Authenticate with the `getCurrentUser` / `getCurrentUserOrSyncToken` helpers I already have, gate with `isSubscriber`, start a workflow, then hand the UI a workflow id to poll. The route never does the long-running work itself. It just points at it.

The route sketch is almost embarrassingly short:

```
export async function POST(request: NextRequest) {
  const user = await getCurrentUserOrSyncToken(request);
  if (!user) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  if (!isSubscriber(user.customerStatus)) return NextResponse.json({ error: "Forbidden" }, { status: 403 });

  const handle = await client.workflow.start(generateArtifactWorkflow, {
    taskQueue: "ai",
    workflowId: `gen-${user.id}-${crypto.randomUUID()}`,
    args: [{ userId: user.id, prompt }],
  });
  return NextResponse.json({ workflowId: handle.workflowId });
}
```

Auth, gate, start the workflow, return the id. That 16k-token document generation that would blow right past the function’s duration budget? It never runs *in* the function. The function kicks it off and gets out of the way.

## The Reuse Win: No Second Codebase

This is the part that made me stop worrying. The worker is not a new codebase. It imports the same `lib/` code the app already runs.

The activities (the actual units of work Temporal executes) call into modules that already exist or are already planned. `safeFetch` from `lib/security/ssrf.ts` for any link crawling, so the SSRF guards apply exactly as they do today. `detectLinks` from `lib/messages/link-detector.ts`. The `post-status.ts` modules under `lib/bluesky/` and `lib/mastodon/` for cross-post fan-out. The DSL parser and validator in `lib/lists/dsl-*.ts` for anything list-shaped. And the AI writer library from the companion genai plan, `lib/ai/`, which doesn’t exist yet but will be wrapped as activities rather than rewritten.

Zero business-logic duplication. That matters more than it sounds. It means the IDOR checks and subscription gating I already trust stay exactly where they live. A worker activity that writes a list row runs through the same `where: { id, userId }` ownership filter as the web route. I’m not maintaining two versions of “can this user do this” and praying they stay in sync. There’s one version, and the worker just calls it.

## What the Foundation Actually Contains

Before any feature ships, there’s a foundation phase, the groundwork everything else in the plan stands on. It’s the worker, the service, the client wiring, and then a small set of cost-control primitives that every later proposal reuses:

- An `llmCall` activity with a **model-cascade policy** (cheap model first, escalate only when the work demands it) and per-target `max_tokens` ceilings: roughly 1k for a message, 4k for a list, 16k for a document.
- An `assertBudget` activity that reads spend before it lets a call through, so a runaway job throws instead of burning credits.
- A **response cache** keyed by `hash(system + prompt + model)`, so identical requests never re-bill.
- Task queues with **rate limits** tuned to whatever the provider or the user’s BYO key allows.

Net-new dependencies are modest: `@temporalio/client` on the Vercel side, the `@temporalio/worker` / `workflow` / `activity` trio on the worker host, and one LLM SDK. That’s the whole shopping list. (AI assistance in the product is still Coming Soon. This is me brainstorming the machine that would power it, not shipping it.)

## Scaffold the Unfamiliar, Own the Verification

I’ve been doing a lot of this alongside Claude lately, and one lesson keeps repeating.

A durable-execution worker is new territory for me. When something’s unfamiliar the instinct is either to avoid it or to throw the whole thing at the model and hope. Both are wrong. What works is to **spec the seams and delegate the boilerplate**.

I give Claude the hard constraints, not vibes. “The app is serverless on Vercel and stays that way. Reuse this `lib/` code, here are the exact modules. Here are the auth and gating seams. The worker imports, it does not reimplement.” With those rails, Claude is great at generating the worker scaffold and the client wiring, the boilerplate I’d get subtly wrong on the first pass because the framework is new to me.

But I do not let it hand me generated infrastructure and call it done. I own correctness, and for a durable workflow, correctness has a specific proof: a **Temporal replay test** using `TestWorkflowEnvironment` that simulates a worker crash mid-workflow and asserts the workflow resumes deterministically, picking up from the last completed activity instead of re-running (and re-billing) the ones already done.

That test does the real work. It’s how “a retry doesn’t re-pay for the LLM call” stops being a claim in a blog post and turns into something I’ve watched go green in CI. The model writes the code I don’t know how to write yet, and I write the test that proves it’s right.

With the foundation standing and provably resumable, Part 3 turns it into the first real feature: a Generate button that survives a timeout and asks before it writes a single thing.

*[Adron](https://interlinedlist.com/user/adron) brainstorming and working on [InterlinedList](https://interlinedlist.com/).*
