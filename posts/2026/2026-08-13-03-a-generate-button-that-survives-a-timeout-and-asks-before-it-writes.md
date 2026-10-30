---
title: A Generate Button That Survives a Timeout and Asks Before It Writes
date: 2026-08-13 06:30:00 -0700
last_modified_at: 2026-08-10 23:20:16 -0700
permalink: /2026/08/13/03-a-generate-button-that-survives-a-timeout-and-asks-before-it-writes/
slug: 03-a-generate-button-that-survives-a-timeout-and-asks-before-it-writes
wp_id: 75021
original_url: https://compositecode.blog/2026/08/13/03-a-generate-button-that-survives-a-timeout-and-asks-before-it-writes/
categories:
- AI & AI Tooling
- interlinedlist
- Temporal
tags:
- interlinedlist
- temporal
excerpt: Part 3 of 8 discusses the development of a durable AI feature for generating lists within an application. The author emphasizes the importance of implementing a two-step process where users confirm outputs before any data is written. This design prevents timeouts and unauthorized data generation, ensuring reliability and user control.
image: /wp-content/uploads/2026/08/03-durable-generate-human-in-the-loop-hero-1.png
---

**Part 3 of 8: Durable AI for InterlinedList**

---

In Part 2 I talked myself into a durable worker sitting next to Vercel, reusing the `lib/` code the app already trusts. That was the plumbing. Now for the first feature I’d actually run through it, a Generate button, and the two things I won’t ship it without.

One: it has to survive a timeout. Two: it has to ask before it writes.

I keep calling those hard requirements because they are. They’re the reason this design points at a durable workflow instead of another `POST` handler. And to be clear up front, since AI assistance in the product is still marked Coming Soon: none of this exists yet. I’m brainstorming out loud before I hand pieces of it to Claude.

## Two Ways a Naive Generate Button Fails

Picture the obvious version. A route that takes a prompt, calls a model, writes the result. Works great in the demo. Then two things happen.

First, someone asks for a long document. Sixteen thousand tokens of generated Markdown streaming back through a serverless function that has a hard duration ceiling. The function dies mid-stream. The user gets nothing, and depending on where it died, maybe a half-written doc. That’s not a fluke. Any generation big enough to be worth doing is big enough to hit the ceiling.

Second, and this is the one that scares me, the model writes straight into your data. For a plain message, fine, you can delete it. For a **List schema**, that’s a slow-moving disaster. A list’s schema is a set of `ListProperty` rows parsed from the DSL, and once rows of data hang off those properties, unwinding a wrong guess gets expensive fast. An AI that invents seven columns and commits them before you’ve looked is a terrible first impression. Undoing a bad schema is the wrong goal. You want to never have written it in the first place.

So the design has to fix both: don’t let a long job die in a function, and don’t write anything the user hasn’t confirmed.

## Suggest, Then Generate: Two Endpoints on Purpose

The split I keep coming back to is two endpoints, and the difference between them carries the whole safety story.

`/suggest` returns a validated artifact and writes nothing. `/generate` writes.

`/suggest` is the default path. It produces the thing (a doc draft, a list schema, a set of rows), validates it, and hands it back to the UI for a human to look at. Nothing touches the database. `/generate` is the second half, and it only runs after a person confirms.

In the durable version, this isn’t two disconnected calls. It’s one workflow that pauses in the middle. The route starts a workflow and returns an id. The workflow generates the artifact, then **blocks on a Signal** (Temporal’s native “wait for an external event”) until a confirm arrives. Long documents don’t block a function while this happens; the UI polls the workflow and reads progress through a Query. The confirm route (`/generate/[workflowId]/confirm`) sends the signal, the workflow wakes up, and *then* it writes.

```
// Sketch of the workflow body (not shipped, this is the design I'd hand off).
export async function generateArtifactWorkflow(input: GenerateInput) {
  // 1. Draft on a cheap tier. Result is memoized by Temporal.
  const artifact = await generateArtifactActivity(input);   // Haiku/Flash draft
  const validated = await validateArtifactActivity(artifact); // untrusted, checked

  // 2. Pause here. No function held open. No tokens spent waiting.
  setHandler(confirmSignal, (decision) => { confirmation = decision; });
  await condition(() => confirmation !== undefined);

  if (confirmation === "reject") return { status: "discarded" };

  // 3. Only now do we write, reusing the same lib/ writers the app trusts.
  return await writeArtifactActivity(validated, input.userId);
}
```

The part I like: while that workflow is parked on the signal, it costs nothing. No held-open request, no tokens burning, no worker thread stuck. Temporal parks it and moves on. You cannot do that inside a serverless handler, and it’s exactly the behavior a confirm gate needs.

## Prompt to List Is Where This Really Pays Off

The flagship case, the one I’d build the whole pattern around, is “build me a list from a sentence.”

You type *“a reading list with title, author, status, and a rating out of five.”* The workflow generates a **DSL schema**, not rows. It renders that schema for you to confirm. You look at it, maybe you fix the rating field, you say yes. Only *then* does it batch-generate rows to populate the list.

Two phases, and the confirm barrier sits between them for a reason: **no row-generation tokens get spent until the schema is confirmed.** If the model guessed the schema wrong, you caught it before paying to fill fifty rows into the wrong shape. So confirm-before-spend does double duty here, better UX and a cost control at once, which is the same thread running through this whole series. The cheapest token is the one you never send.

And I’m not inventing new validation to do this. The DSL already has the pieces. `validateDSLSchema` and `parseDSLSchema` both live in `lib/lists/dsl-parser.ts` today, and they’re what turns DSL into `ListProperty` rows for real, human-authored lists right now. The generated schema goes through the exact same door. Then `lib/materialize/build-list.ts` builds the actual list. The AI path reuses the trusted path; it doesn’t get a shortcut around it. (Lists are a Subscriber feature, so this whole flow lives behind that gate. The workflow checks it before writing, same as every other list-creating action.)

## Model Output Is Untrusted Input

One mental flip makes the rest of the design fall out easily. **Model output is untrusted input.** Treat it exactly like a request body from a stranger.

You’d never take a JSON blob off the wire and write it to your database without validating the envelope shape, checking the types, and confirming the user is allowed to do the thing. A model’s output gets the identical treatment: envelope shape first, then DSL validation, then per-row validation, then ownership and subscription gating. Only something that survives all four gates gets written. If the model hallucinates a field type the DSL doesn’t support, validation rejects it the way it’d reject any malformed request. The model doesn’t get trusted just because it’s ours.

## How I’d Hand This to Claude

If there’s one working-with-an-LLM lesson in this post, it’s this: **design the contract, delegate the wiring.**

There’s a trust boundary running through this feature, and I want to own every inch of it myself. Three pieces I write by hand: the typed artifact envelope (what a generated doc/list/schema/row is *shaped* like), the validators (envelope, then DSL, then per-row, then gating), and the ownership and subscription checks. That’s where a subtle mistake means a wrong schema gets written or a free user slips past a gate. I don’t delegate that. A plausible-looking version isn’t good enough. I want to have written it.

Everything *around* that contract is the kind of thing I’d hand to Claude. The workflow body. The signal handler and the `condition` wait. The polling glue and the Query that streams progress. The confirm route. It’s durable-execution boilerplate: Claude writes it well, and it’s fast to verify against a contract I already defined.

The hand-off is concrete. I give Claude the typed artifact schema and one rule stated plainly: *“validate model output like a request body (envelope, then DSL, then per-row, then gating) and never write it through raw. Here are the validators; call them, don’t reimplement them.”* Then I let it build the durable plumbing around that. I own the trust boundary, Claude owns the machinery that carries data across it, and the review stays easy because I already know where the sharp edge is. I made sure it’s mine.

A Generate button that can’t die mid-job and won’t write behind your back is the piece I want first. Next in Part 4, I’ll turn to the cron that already double-posts in production today, and the content calendar I actually want built on top of a scheduler that doesn’t.

*[Adron](https://interlinedlist.com/user/adron) brainstorming and working on [InterlinedList](https://interlinedlist.com/).*
