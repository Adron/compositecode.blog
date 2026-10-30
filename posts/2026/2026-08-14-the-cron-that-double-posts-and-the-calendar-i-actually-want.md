---
title: The Cron That Double-Posts and the Calendar I Actually Want
date: 2026-08-14 06:30:00 -0700
last_modified_at: 2026-08-14 09:51:45 -0700
permalink: /2026/08/14/the-cron-that-double-posts-and-the-calendar-i-actually-want/
slug: the-cron-that-double-posts-and-the-calendar-i-actually-want
wp_id: 75055
original_url: https://compositecode.blog/2026/08/14/the-cron-that-double-posts-and-the-calendar-i-actually-want/
categories:
- AI & AI Tooling
- interlinedlist
- Temporal
tags:
- interlinedlist
- programming
- temporal
excerpt: The post discusses a critical bug in a scheduled publishing feature used for cross-posting on various platforms. It details how the current system may lead to double posts due to timing issues between cross-posting and database updates. The author suggests a robust solution involving a new scheduling system to avoid such errors while emphasizing the importance of addressing underlying hazard classes rather than mere symptoms.
image: /wp-content/uploads/2026/08/04-scheduling-cron-double-post-calendar-hero-1.png
---

**Part 4 of 8: Durable AI for InterlinedList**

---

Most of this series is me thinking out loud about features that don’t exist yet. This post is different as the bug is real. It’s in the code today. 😬

Scheduled publishing is a Subscriber feature, and so is the cross-posting it rides on. You queue a post, set a time, and a cron fans it out to Bluesky, Mastodon, LinkedIn, and X when the moment arrives. Both sit behind the subscription, so this bug hits paying subscribers. The machinery that runs it has a hole in it I don’t love.

## The Cron That Can Post Twice

Walk through what the code does. `app/api/cron/publish-scheduled-messages/route.ts` runs every minute. It selects every message where `scheduledAt <= now`, then loops over them. For each one it fans out to whatever platforms the user configured, collects the resulting URLs, and then, as the last step, updates the message row to null out `scheduledAt` so the message is no longer “due.”

Read that ordering again. The cross-post happens first. The “mark it done” write happens second. No lock. No idempotency key. No transaction spanning the fan-out and the update. Those two operations are just sequential, and hopeful.

So picture the fan-out succeeding. Your post lands on Bluesky and Mastodon. Great. Now the `message.update` that’s supposed to clear `scheduledAt` hits a reaped Neon connection, or a transient network blip, or any of the ten boring things that make a database write fail once in a while. The update throws. The message row still has `scheduledAt <= now`.

One minute later the cron runs again. The message is still due. It fans out *again*. Same post, second time, to every platform. That’s your double-post.

The code isn’t naive about this: there’s a `withPrismaRetry` wrapper on that critical update and a comment that literally says “if this fails the message stays due and is re-published.” Someone saw the cliff and put up a guardrail. But a retry is a mitigation, not a fix. It narrows the window without closing it. If the retries exhaust, or the process dies between the fan-out and the update, you’re back on the cliff. And the fan-out itself is best-effort per platform (LinkedIn can fail while Bluesky succeeds, with no compensation), so a re-run doesn’t even cleanly re-do the same thing. It re-does *some* of it.

This is a slow-moving disaster. It doesn’t fire on every post. It fires on the unlucky ones, occasionally, in production, and it makes your platform look like it can’t be trusted to post your thing exactly once.

## The Working-With-Claude Lesson: Point at the Bug Class, Not the Bug

If you take one thing from this post, take this part, not the fix. It’s worth more.

If I open a session and say “fix the double-post in publish-scheduled-messages,” I get a patch that treats the symptom. Maybe it wraps more things in retries. Maybe it adds a `published` boolean and checks it. Narrow prompt, narrow fix, and I’ve probably left three other copies of the same hazard sitting in the codebase untouched.

So I don’t open it that way. I say: **“Audit this scheduled-publish path for concurrency and idempotency hazards.”**

That framing is doing real work. It doesn’t presume I already know what’s wrong. It asks the agent to reason about the *class* of failure: what happens under a partial failure, what happens if two invocations overlap, what’s the ordering of side effects versus state writes, where’s the operation that isn’t idempotent. The double-publish race falls out of that audit as one instance of a general pattern (side effect before commit, no dedup key). And the audit usually surfaces siblings I hadn’t thought to ask about.

This is the two-step I keep coming back to with Claude on anything gnarly. **Audit for the class, then delegate the conversion.** First get the agent to characterize the whole shape of the problem. Then, once you both understand it, hand over the mechanical rewrite. Collapse those into one “fix it” prompt and you’ll get a bandage every time.

Most of the value is in the audit. The conversion is mostly typing, and Claude is very good at the typing once you’ve done the thinking with it.

## The Fix: A Schedule, a Workflow ID, and a Saga

So this is the conversion I’d delegate. It’s a proposal. None of it is built yet.

Replace the every-minute cron with a Temporal Schedule that starts **one workflow per due message**. The whole trick is what you use for the workflow ID.

```
// Proposed: the message id IS the workflow id.
// Temporal refuses to start a second workflow with an id that's
// already running or already completed. That's the dedup.
await client.workflow.start(publishScheduledMessage, {
  workflowId: `publish-message:${message.id}`,
  taskQueue: "publishing",
  args: [{ messageId: message.id }],
});
```

Temporal deduplicates by workflow ID. If a workflow with `publish-message:abc123` has already run (or is running right now), a second `start` with that same ID is rejected or returns the existing handle, depending on the reuse policy you pick. The message *cannot* be published twice, because you cannot start its publish workflow twice. The race doesn’t get narrower. It closes. There’s no second racer allowed on the track, so there’s nothing left to race.

That’s a different guarantee than “we retried hard enough that it usually works.” One is a hope with good odds. The other is impossible by construction, and I’ll take impossible.

Then model the fan-out as a **saga** instead of a hopeful loop. One activity per platform: `postToBluesky`, `postToMastodon`, `postToLinkedIn`, `postToTwitter`, the exact `post-status.ts` functions the cron already calls, plus the same `splitTextForPlatform` and `resolveLinkedInTarget` logic. Each activity retries independently with backoff, and each one’s success is durably recorded before the next runs. If LinkedIn fails after Bluesky succeeded, the workflow *knows* Bluesky is done and won’t re-do it. It records the half-failure coherently and runs compensation, instead of silently re-posting the whole set on a blind re-run.

And the thing that makes this an easy call: **publishing uses zero LLM.** No model in this loop at all. No tokens, no inference cost, nothing to govern with a budget. It’s pure durability engineering, a straight win against a present-day production hazard with no ongoing cost attached. If anything in this series jumps the queue, it’s this.

## The Calendar I Actually Want

Once publishing is durable, the thing I’ve wanted for ages becomes buildable. This part is squarely future, gated behind AI assistance that’s still marked Coming Soon.

I want to type “give me a month of posts about distributed systems, three a week” and get a filled calendar back. Not a wizard. Not twelve separate button clicks. A month.

The cheap way to build that leans on batching. **One** LLM call produces all N drafts at once, and batching many items into a single prompt is dramatically cheaper than N separate calls (the cost thesis that runs through this whole series). The workflow takes those drafts, schedules them across the month, and fills the gaps. Then, to keep it cheap, you can reject or regenerate an **individual** slot. Don’t like Thursday’s post? Regenerate just that one. Only the rejected slot re-bills. You never repay for the twelve you kept.

The same shape covers scheduled digests: a Temporal Schedule that drafts you a weekly summary doc from the week’s messages. But put a cheap guard *before* the model runs. Did this user post anything this week? If not, skip the LLM entirely. You never pay to generate an empty digest for a quiet week. The guard is a database count. The model is the expensive part. You gate the expensive part behind the cheap check, which is the move I keep making all through this series: spend tokens last, and only when there’s something worth spending them on.

The calendar is the feature I daydream about. The double-publish fix is the one I’d ship first, because it’s a real hole in production right now and closing it costs nothing but the work.

Part 5 goes hunting through everything you’ve saved: the links buried in your messages, docs, and list rows, and how I’d crawl and cache them so “where did I save that article?” finally has an answer.

*[Adron](https://interlinedlist.com/user/adron) brainstorming and working on [InterlinedList](https://interlinedlist.com/).*
