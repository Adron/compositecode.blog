---
title: Notes Repos as Shared Project Context
date: 2026-09-25 15:01:30 -0700
last_modified_at: 2026-09-24 14:27:26 -0700
permalink: /2026/09/25/notes-repos-as-shared-project-context/
slug: notes-repos-as-shared-project-context
wp_id: 75338
original_url: https://compositecode.blog/2026/09/25/notes-repos-as-shared-project-context/
categories:
- AI & AI Tooling
tags:
- as
- coding
- gen ai
- llms
- programming
excerpt: Creating a notes repository alongside code repositories enhances project clarity and continuity. It serves as a durable knowledge base for plans, decisions, and team structures, accessible to both human team members and agents. This organized approach minimizes miscommunication and maintains project focus, ensuring everyone stays aligned and informed throughout the development process.
image: /wp-content/uploads/2026/09/hero-notes-repos-as-shared-project-context.jpg
---

The first thing most people put in a new repository is code. That is fine. It is also incomplete.

When I start a real project these days, something I expect Cursor, Claude, Codex, and I to grind on together for more than an afternoon, I create a notes repo early. Sometimes it sits beside the product repo. Sometimes it lives inside the product repo as a deliberate `notes/` or `docs/project/` tree. Either way, the job is the same: give the humans and the agents one durable place to put the stuff that does not belong in source files but absolutely belongs in the work.

This is not documentation for show. It is shared working memory.

## Why a notes repo, not a pile of chat

Chat is ephemeral. Agent transcripts are useful, but they are not a system of record. Plans get buried. Decisions get restated wrong three sessions later. Somebody new (human or model) shows up and has to rediscover who owns what, what “done” means, and which external systems are in play.

A notes repo fixes that by making the context something you can open and search. Cursor can open it. Claude can read it. Codex can search it. I can edit it when the plan changes. Everyone is looking at the same markdown, not reconstructing the project from memory and half-remembered Slack threads.

I treat it as the base layer under the code. The product repo holds the build. The notes repo holds the thinking that keeps the build pointed in the right direction.

## What actually goes in it

I keep the structure boring on purpose. Fancy wikis rot. Flat, named markdown files get used.

**Project brief.** What we are building, who it is for, what it is not. One page. If you cannot say it in a page, you do not have a project yet. You have a mood.

**Current plan.** The active plan, not a museum of every plan that ever existed. Short enough to approve in one breath. Specific enough that “yes” means something. When the plan changes, rewrite it. Do not append a novel of abandoned approaches unless those approaches teach a real constraint.

**Decisions.** Lightweight ADRs, or just dated notes: we chose X because Y, and Z is explicitly out of scope. Agents love to re-litigate settled choices. Write the settlement down.

**Team map.** Who is who. Humans, roles, ownership. Which agent lanes exist if you have specialized agents. Who reviews security. Who can approve schema changes. “The team” includes the tools now, so name them and their jobs.

**Glossary.** Product words, domain words, the three acronyms everybody uses differently. Cheap insurance against confident mistakes.

**Working notes.** Scratch space for the current thread of work: open questions, links to tickets, sketches, “we tried this and it failed because…”. This is the joint notebook Cursor, Claude, Codex, and I write into while we work.

**Pointers out.** Links to the product repos, design files, staging URLs, runbooks, and the environment/setup notes. The notes repo should know where the rest of the world lives without trying to duplicate it.

I do not put secrets here. I put the names of secrets and where they are supposed to live. That distinction matters.

## How I use it with agents

The pattern is simple: before an agent starts implementing, it reads the brief, the current plan, and the relevant decision notes. After a meaningful chunk of work, it updates the working notes or the plan so the next session does not start from zero.

That pairs cleanly with the ask-plan-confirm habit I already use. The notes repo is where the approved plan lives between sessions. The agent does not get to invent a new goal because the chat scrolled away.

A few practical rules that hold up:

- One current plan file. Archive old plans if you must, but do not make the agent guess which file is live.
- Prefer short files with clear names over one giant `NOTES.md`.
- Write for the next reader who was not in the room. That reader might be you in two weeks, or an agent with a fresh context window.
- Update notes as part of the work, not as a cleanup chore after merge. If it is optional, it will not happen.

## What this saves

It saves re-explaining the project every morning. It saves the “wait, who owns auth?” loop. It saves agents from optimizing the wrong goal because the real goal lived in a Slack thread from Thursday.

It also saves *me* from being the only continuity process on the team. Continuity is a file. Version it. Diff it. Argue with it in a pull request if the decision is big enough.

## Start smaller than you think

You do not need a knowledge management platform. You need a repo, a README that says what the repo is for, and a handful of markdown files that stay honest.

Create it when the project becomes real. Keep it next to the code in your mental model. Make every agent treat it as required reading before they touch the product tree.

Code is the artifact. Notes are the shared brain that keeps the artifact from wandering off.
