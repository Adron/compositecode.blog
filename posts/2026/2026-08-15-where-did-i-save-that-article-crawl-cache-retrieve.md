---
title: Where Did I Save That Article? Crawl, Cache, Retrieve
date: 2026-08-15 06:30:00 -0700
last_modified_at: 2026-08-10 23:19:25 -0700
permalink: /2026/08/15/where-did-i-save-that-article-crawl-cache-retrieve/
slug: where-did-i-save-that-article-crawl-cache-retrieve
wp_id: 75056
original_url: https://compositecode.blog/2026/08/15/where-did-i-save-that-article-crawl-cache-retrieve/
categories:
- AI & AI Tooling
- interlinedlist
- Temporal
tags:
- interlinedlist
- programming
- temporal
excerpt: The post explores improvements to an AI tool for managing saved links, addressing challenges in retrieval. It proposes creating a durable cache for links and enhancing search functionality with vector embeddings. The author emphasizes the need for security in URL fetching and systematic database migrations. The goal is easy access to previously saved articles and improved content management.
image: /wp-content/uploads/2026/08/05-find-content-in-your-links-hero-1.png
---

**Part 5 of 8: Durable AI for InterlinedList**

---

I have a problem, and I bet you have it too. I read something good, I drop the link into a post or a document or a row in some list, and then three weeks later I want it back and I have no idea where it went. Was it a message? A doc? A row in that reading-list I built? So I scroll my own feed like an archaeologist. It’s a slow-moving disaster. The whole point of writing something down is being able to get it back, and I’d built the writing-down part beautifully while ignoring the getting-it-back part entirely.

So this is the post where I brainstorm fixing that. Two pieces come from [the Temporal plan](https://github.com/CompositeCode/interlinedlist/blob/develop/docs/plans/temporal-solutions.md), and they run in order. First, the link-crawl-and-cache phase turns saved links into a real cache. Then the retrieval phase makes that cache searchable, semantic *and* keyword, with cited snippets, so “where did I save that article about X” actually returns the article about X. None of this is shipped. AI assistance in the product is still “Coming Soon.” This is me thinking out loud with the intent to build.

## What Actually Exists Today (Less Than You’d Hope)

Before I design anything, I made myself write down what the codebase does *right now*, because designing against a fantasy version of your own product is how you build the wrong thing.

Today, link metadata gets fetched for messages only. When you post something with a URL, `lib/messages/metadata-fetcher.ts` pulls the Open Graph tags and the result gets stored inline on the message as a JSONB blob: `Message.linkMetadata`. That’s it. There’s no cache table. There’s no dedup, so if you and forty other people all post the same great article, that URL gets fetched forty-one times. Documents and list rows (both Subscriber features) don’t get scanned for links at all. And search? Search today is Postgres `ILIKE` substring matching across three separate routes: messages, lists, documents. It’s a `contains` query. Type “kubernetes” and you get rows where the literal string “kubernetes” appears. Miss the spelling, miss the synonym, miss the concept, and you get nothing. There is zero vector infrastructure anywhere in the repo. I checked.

That’s the honest starting line. It’s also a decent starting line, because two of the hard parts are already solved and I’d be a fool to rewrite them.

## The Crawler: Reuse the Fetcher, Reuse the Guard

So, the caching step. A durable workflow scans a user’s messages, documents, and list rows for URLs, fetches each one, extracts the readable content, and stores it in a new `LinkContent` cache table keyed by a hash of the URL. Deduplicated across all your content, and optionally across all users. It runs incrementally: only new or changed URLs get fetched, so the second run is nearly free.

The building blocks already exist. `lib/messages/link-detector.ts` gives me `extractUrls` and `detectLinks`. `lib/messages/metadata-fetcher.ts` gives me `fetchLinkMetadata`. And critically, `lib/security/ssrf.ts` gives me `safeFetch` and `assertUrlAllowed`, the SSRF guard the codebase already fought to get right. This work is mostly *generalizing* the message-only path to also cover docs and list rows, then bolting a real cache behind it so a URL is fetched once and never again.

This is the single most important thing to say to Claude when you hand it this task, so I’ll say it here first: **build on `safeFetch` and `assertUrlAllowed`. Do not write a new `fetch()`.**

I cannot overstate this. Left to its own devices, an LLM asked to “write a crawler that fetches URLs and extracts content” will cheerfully write you a fresh `fetch(url)` with a nice timeout and some error handling, and it’ll look completely reasonable, and it’ll have reintroduced the server-side request forgery hole this codebase already closed. It won’t check whether the URL resolves to `169.254.169.254` and hands back your cloud metadata. It won’t block the redirect that bounces from a public host to `localhost`. The existing `safeFetch` does all of that, and it re-validates on every redirect hop. A brand-new fetcher is a security regression wearing the costume of a feature.

So the instruction isn’t “write a crawler.” The instruction is:

```
// Crawler activity: the reuse contract, spelled out for the agent.
// 1. detectLinks/extractUrls from lib/messages/link-detector.ts to find the URLs
// 2. hash each URL, check the LinkContent cache, skip if already fetched & unchanged
// 3. fetch ONLY through safeFetch from lib/security/ssrf.ts (never a raw fetch)
// 4. extract readable text mechanically (HTML to text), NO LLM in this path
// 5. upsert into LinkContent keyed by urlHash; dedup means fetch-once-ever
async function crawlUserLinks(userId: string) {
  const urls = await collectUrlsFromMessagesDocsAndRows(userId); // reuse extractUrls
  for (const url of dedupeByHash(urls)) {
    if (await cacheHasFresh(url)) continue;         // incremental: skip known URLs
    const html = await safeFetch(url);              // SSRF guard, NOT a new fetch()
    await upsertLinkContent(url, extractReadableText(html));
  }
}
```

Note what’s *not* in there: a language model. HTML-to-readable-text is mechanical. You strip the tags, you pull the article body, you’re done, no tokens spent. An optional cheap-model summary of each page could sit on top later, opt-in, for people who want it, but the base extraction costs nothing per link beyond the fetch. Pair that with URL-hash dedup (a shared link is fetched once, ever, across the whole system) and this becomes the cheapest proposal in the whole plan for what you get out of it. Which is why I like it. It’s mostly plumbing, mostly reuse, and it barely touches an LLM.

## Retrieval: The Part That Needs New Ground

The crawl phase gives me the cache. The search-over-my-links phase is what makes it findable. This is “search over my link index *and* my own docs, lists, and messages, returning cited snippets.”

And I have to be honest that this one needs real new infrastructure, because the vector story doesn’t exist yet: not partially, not disabled behind a flag, not anywhere. So the retrieval phase needs a `pgvector` extension, an embedding column or table, an embed activity that turns text into vectors, and a search route that ranks by both vector similarity *and* the existing `ILIKE` match. Hybrid. It **supplements** today’s substring search rather than ripping it out. Keyword matching is still the right answer for exact-string lookups, and it needs no model at all.

The cost math here is the reassuring part. Embeddings are orders of magnitude cheaper than text generation: you’re paying to turn text into a vector, not to write prose. You compute each embedding once and cache it, sharing the same cache the crawl phase already built. And because retrieval comes *first*, any eventual answer-synthesis step runs over a small, already-narrowed set of retrieved snippets instead of dumping your whole corpus into a prompt. Keep the expensive context small and this stays affordable.

The incremental pipeline is what keeps it fresh without a nightly full re-scan: on every content write (new post, edited doc, added row) enqueue a re-embed activity for just that thing. Batch the embeddings for throughput. The index stays current, and you never re-embed the 99% of your corpus that didn’t change.

## The Second Lesson: Don’t Let the Agent Touch the Database Directly

The `pgvector` migration is where the *other* working-with-Claude lesson lives, and it’s a governance one.

This repo has a strict database workflow, and it’s strict for a reason the CLAUDE.md states plainly: violating it has broken production before. Additive-only. Idempotent SQL. Hand-written migration files applied to both databases. No `prisma db push`, no `prisma migrate dev`, no raw DDL fired at the database from a script.

An LLM does not know this in its bones. Ask it to “add a vector column and an embeddings table” and its instinct (a perfectly good instinct in most repos) is to edit the schema and run `prisma db push` to sync it. In *this* repo that’s a loaded gun. So the instruction to the agent isn’t just “add the schema.” It’s: **route this through the db-migrations workflow. Write an idempotent, additive migration file (`CREATE EXTENSION IF NOT EXISTS vector`, `CREATE TABLE IF NOT EXISTS`, the column adds guarded) and do not run `db push` or `migrate dev` against the database.** The good news is the migration is cleanly additive: there’s no existing vector infra to alter or drop, so it’s all new tables and columns, which is exactly the shape this workflow handles best.

Two guardrails, then, and I’d hand both to the agent up front rather than catch them in review: reuse `safeFetch` instead of writing a fetcher, and route the schema change through the migration workflow instead of letting it push. Both are cases where the model’s default behavior looks reasonable and is wrong for this codebase. Tell it about the thing that already exists, and tell it not to reinvent it.

The payoff, if I build it, is the thing I wanted in the first place. I type “that article about durable execution I saved somewhere,” and I get it back with the snippet and a link to wherever I stashed it, whether that was a throwaway post or a row buried in a list. My scattered links stop being a graveyard I dig through and turn into something I can actually ask questions of. Subscriber-gated, computed once and cached, and cheap enough that I’d leave it running without watching the bill.

Next up in Part 6, I want to point this same durable-fan-out machinery at bulk work: tag every untagged message, add twenty rows matching a criterion, backfill previews across everything, and do it without re-billing the model for the forty-six items that already succeeded before item forty-seven fell over.

*[Adron](https://interlinedlist.com/user/adron) brainstorming and working on [InterlinedList](https://interlinedlist.com/).*
