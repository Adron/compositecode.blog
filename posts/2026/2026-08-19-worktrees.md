---
title: 'Giving Every Agent Its Own Branch: Git Worktrees for Parallel AI Work'
date: 2026-08-19 08:00:00 -0700
last_modified_at: 2026-08-17 14:42:09 -0700
permalink: /2026/08/19/worktrees/
slug: worktrees
wp_id: 75161
original_url: https://compositecode.blog/2026/08/19/worktrees/
categories:
- AI & AI Tooling
- Coding Adventures
- Coding Patterns & Practices
- Programming
tags:
- agentic
- agents
- ai
- coding
- gen ai
- git
- llms
- multiple agents
- programming
- worktrees
excerpt: The text discusses challenges faced when using multiple coding agents on a single Git working tree, leading to merge conflicts and lost edits. It emphasizes the need for independent work environments through Git worktrees, which allow each agent to operate in its own directory while sharing an object store. The author details a structured solution to managing these worktrees, outlining scripts for creation, management, and cleanup while acknowledging remaining pitfalls such as shared databases and overlapping edits that could still lead to conflicts.
image: /wp-content/uploads/2026/08/parallel-agents-with-git-worktrees-hero.png
---

Run two coding agents against a single working tree and they will fight. One is halfway through editing `app/api/messages/route.ts` while the other checks out a different branch underneath it. The index lock flickers. A `git stash` from one session swallows the other’s uncommitted work. I have lost real edits this way, and every time the root cause was the same: one working tree, one `HEAD`, two writers.

The InterlinedList repo already had matching agents for the jobs I hand off most: a Next.js implementer, a migrations specialist, unit and e2e testers, a docs writer, security and UX reviewers. They are good at their lanes. What they were missing was a lane in the literal sense. They all drove on one road.

I found the pattern I wanted written up in [Augment’s guide to git worktrees for parallel AI execution](https://www.augmentcode.com/guides/git-worktrees-parallel-ai-agent-execution), and it maps almost one to one onto how I already think about agents. This is the writeup of what I built on top of it for this repo: the directory convention, the seven scripts that manage the lifecycle, and the wiring that makes every agent use them without being reminded.

## The one-tree problem

A normal clone gives you a single working directory backed by one `.git`. That is fine for one person doing one thing. The moment you parallelize, the shared mutable state (the working files, the index, the current branch) becomes the bottleneck. You cannot have the migrations agent on `agent/add-webhooks` and the docs agent on `agent/help-refresh` at the same instant, because “the branch” is a property of the whole checkout.

[![Diagram illustrating 'The one-tree problem' in software development with two agents, A and B, interacting with a mutable checkout and related issues like index.lock flicker and checkout thrash.](/wp-content/uploads/2026/08/worktrees-fig1-one-tree-problem.png)](/wp-content/uploads/2026/08/worktrees-fig1-one-tree-problem.png)

*Two writers, one mutable checkout. The collisions have nothing to do with the work: an index lock flickers, a `git stash` swallows the other session’s edits, `HEAD` thrashes between branches.*

Git solved this in 2015 with `git worktree`. A worktree is a second (third, fourth) working directory attached to the same repository. Each one has its own files, its own index, and its own checked-out branch, while sharing one object store on disk. The object store is the expensive part, so you share it. A directory of files is cheap, so you duplicate it per task. That is exactly the tradeoff you want for parallel agents.

[![Diagram illustrating a Git object store with multiple worktrees, highlighting shared storage and individual configurations for each task.](/wp-content/uploads/2026/08/worktrees-fig2-architecture.png)](/wp-content/uploads/2026/08/worktrees-fig2-architecture.png)

*Share the expensive part, duplicate the cheap part. The object store lives on disk once; the working files, the index, the checked-out branch, and even the dev-server port are private to each worktree.*

## The convention

Every agent works in `.trees/<task-id>` on a branch named `agent/<task-id>`, cut from `origin/develop` (this repo integrates on `develop`, not `main`). So a task called `add-list-webhooks` lives at `.trees/add-list-webhooks` on branch `agent/add-list-webhooks`. The directory name and the branch name always agree because both are derived from the same sanitized slug.

The `.trees/` container is gitignored. Worktrees are workspace, not history:

```
# .gitignore
# Agent worktrees (see scripts/worktrees/)
.trees/
```

That single ignore line is the whole footprint the pattern leaves in the tracked tree. Everything else is scripts and instructions.

## The scripts

I did not want agents (or me) typing raw `git worktree` incantations and getting the branch name wrong, or forgetting to copy `.env.local`, or leaving stale metadata behind. So the lifecycle lives in `scripts/worktrees/` as a small set of focused shell scripts. Here is every one of them.

[![Diagram illustrating the worktree lifecycle in Git, detailing steps for creating, inspecting, removing, and cleaning worktrees. Sections include 'STEP 1' for branch creation, 'WHILE WORKING' for listing and locking, 'WHEN IT LANDS' for removing branches, and 'DAILY SWEEP' for cleanup processes.](/wp-content/uploads/2026/08/worktrees-fig3-lifecycle.png)](/wp-content/uploads/2026/08/worktrees-fig3-lifecycle.png)

*The whole lifecycle before the per-script detail. Create, inspect while working, remove when it lands, sweep the merged trees on a schedule.*

**`_lib.sh`** is the shared library the others source. It holds the functions that keep conventions consistent: `wt_repo_root` resolves the primary checkout even when you call it from inside a linked worktree (it reads `git rev-parse --git-common-dir` and walks up), `wt_sanitize` lowercases a task id and strips it to `[a-z0-9._-]`, `wt_resolve_base` fetches and prefers `origin/<base>` over a local branch, `wt_port_for` hashes a branch name into a stable dev port, and `wt_is_locked` reads the porcelain worktree list to check lock state. Nothing in it is clever. It exists so the clever bits are written once.

**`wt-create.sh <task-id> [base]`** is the one agents call first. It creates the worktree and makes it ready to work in, in one shot:

```
scripts/worktrees/wt-create.sh add-list-webhooks
```

Under the hood it resolves the base ref (default `develop`), ensures `.trees/` is in `.gitignore`, turns on `git rerere` so repeated conflict resolutions replay across parallel merges, runs `git worktree add -b agent/<slug> .trees/<slug> origin/<base>`, copies the root `.env.local` into the worktree, appends a deterministic `DEV_PORT` derived from the branch name, runs `npm ci --prefer-offline`, and finally locks the worktree so other sessions can see it is in use. Flags let you opt out where it makes sense: `--no-install` skips the dependency install for a quick plumbing check, `--no-lock` leaves it unlocked, and `--baseline` runs the test suite right after setup so a green baseline proves any later failure came from the agent’s change rather than a pre-existing break.

The port assignment is worth a sentence. Two agents both running `next dev` on 3000 is another collision, a quieter one. `wt_port_for` runs the branch name through `cksum` and maps it into the 3100 to 9998 range, so each worktree gets a stable, distinct port written into its own `.env.local`. Start the server with `npm run dev -- -p "$DEV_PORT"` and two dev servers coexist.

**`wt-list.sh`** answers “what is running right now.” It prunes stale metadata, then prints one row per worktree with path, branch, lock state, and short HEAD:

```
PATH                                    BRANCH                LOCKED  HEAD
/Users/adron/Codez/interlinedlist       feature/fix-blog-image  -     58afa91562
/Users/adron/Codez/interlinedlist/.trees/add-list-webhooks  agent/add-list-webhooks  yes  b78faf9e21
```

Before an agent touches a shared file, it can look here and see who else is holding what. Git will not warn you about two branches editing the same file, so this list plus discipline about non-overlapping file domains is the actual safety mechanism.

**`wt-lock.sh <task-id> [reason]`** and **`wt-unlock.sh <task-id>`** are thin wrappers over `git worktree lock`/`unlock`. A lock is advisory: it resists prune and move, and it is the signal in `wt-list.sh` that says “an agent is live in here, do not reap this.”

**`wt-remove.sh <task-id>`** is the teardown. It unlocks if needed, runs `git worktree remove`, and prunes. This matters more than it looks: deleting a worktree with `rm -rf` leaves dangling metadata in `.git/worktrees/` that haunts you until the next prune. The script never does that. `--force` discards uncommitted changes on purpose, and `--delete-branch` drops `agent/<task-id>` in the same step when the work has landed.

**`wt-cleanup.sh [base]`** is the bulk sweep. It walks every worktree physically under `.trees/`, and for each one whose branch is already an ancestor of `origin/develop` (in other words, merged), it removes the worktree and deletes the branch. It deliberately skips anything outside `.trees/`, so the primary checkout and any sibling worktrees I keep elsewhere on disk are never touched. This is the script you point a daily cron or a post-merge hook at.

Each of these is also exposed as an npm script, so `npm run wt:create -- add-list-webhooks`, `npm run wt:list`, and `npm run wt:remove -- add-list-webhooks` all work if you prefer that entry point. There is a `scripts/worktrees/README.md` documenting the whole set alongside the code.

## Wiring it into the agents

Scripts nobody runs are decoration. The point was to make every agent reach for a worktree by default, so I added the instruction in three places at three levels of specificity.

At the top, `CLAUDE.md` now states the standing rule: every agent works in an isolated worktree, torn down with the lifecycle scripts. That is the repo-wide contract.

In the middle, two shared protocol docs under `.claude/workflows/` hold the full detail: `worktrees.md` spells out the create-work-remove lifecycle, the boundaries (shared object store, non-overlapping files, and the important caveat that the database is shared even though the files are not), and `plan-first.md` covers the companion habit I wrote about separately. Every agent and skill links to these rather than repeating them.

At the leaf, each of the eight agent definitions in `.claude/agents/` got a “Work in an isolated git worktree (required)” section written for its job. The implementers (Next.js, migrations, tests, docs, blog) get the full create-work-remove flow. The two read-only reviewers (security, UX) get a variant that tells them to `cd` into the worktree under review and read its diff, and explicitly not to create, lock, or remove anything. The migrations agent gets an extra warning in bold, because the worktree isolates `schema.prisma` and the migration files but not the Postgres instance: `db:migrate` still hits localhost and `db:migrate:deploy` still hits production from any worktree. That is the one place the isolation is a lie, and the agent needs to know it.

The five paired skills in `.claude/skills/` (the ones that back the implementer agents) got a short “Worktree-first, plan-first” block near the top pointing at the same protocol docs, so whether the work comes in through the agent or the skill, the instruction is there.

## Proving it works

I ran the whole lifecycle before committing any of it. Create a worktree from `develop`, confirm it is locked and has its port, unlock and re-lock it, remove it with the branch, and verify the cleanup pass leaves the sibling worktrees alone:

```
scripts/worktrees/wt-create.sh wt-smoke-test --no-install
scripts/worktrees/wt-list.sh          # shows agent/wt-smoke-test, LOCKED yes
scripts/worktrees/wt-unlock.sh wt-smoke-test
scripts/worktrees/wt-lock.sh wt-smoke-test "smoke re-lock"
scripts/worktrees/wt-remove.sh wt-smoke-test --delete-branch
scripts/worktrees/wt-cleanup.sh develop   # safe no-op, siblings untouched
```

Every step did what it said, the `.gitignore` guard refused to duplicate the `.trees/` line it found already present, and the sibling worktree I keep for feed-perf work was never in scope for cleanup. That last part was the thing I most wanted to confirm, because a cleanup script that reaches outside its sandbox is worse than no cleanup script.

## Where agents still get confused

Isolating the filesystem fixes the filesystem. It does nothing about the fact that the work itself overlaps, and there are a handful of ways an agent still gets lost.

**The database is one instance, and every worktree writes to it.** I flagged this to the migrations agent in bold, but it deserves more than a warning. If the migrations agent adds a column on `agent/add-webhooks`, that column now exists in the same localhost Postgres every other worktree points at. The docs agent three trees over never sees the changed `schema.prisma`, yet its queries hit the mutated database anyway. Additive-only migrations keep this survivable most of the time, since an extra column nobody reads is harmless. But the moment two agents touch the same table, or one runs `db:migrate:deploy` and reaches production from what looked like a sandbox, the isolation is a fiction. The files are private. The database is not.

**Green in isolation, red on merge.** This is the one that bites. Agent A changes a function signature in `lib/lists/queries.ts`. Agent B, on its own branch, calls that function from a route it owns. Their files never overlap, so `wt-list.sh` shows no conflict and git stays quiet. Both test suites pass, because A’s worktree still holds B’s old caller and B’s worktree still holds A’s old signature. It’s all green right up until both branches land on `develop`, and then the integration is broken in a way neither agent could see from inside its own tree. Worktrees convert a loud, immediate collision into a quiet one that surfaces later. Often a fair trade, but a trade.

**Stale base drift.** Every worktree is cut from `origin/develop` the moment it’s created. Agents aren’t always short-lived. Let one run for a few hours while three others merge back, and it’s now building on a `develop` that no longer exists. It will reintroduce a helper that got deleted upstream, or write against an API another agent already reshaped. The worktree has no idea the ground moved under it. Nothing in the create-work-remove loop forces a re-fetch, so a long-running agent drifts out of date without noticing.

**“Does this already exist?” stops having one answer.** With five branches in flight, whether feature X is “already built” depends on which tree you grep. An agent that checks the primary checkout won’t see work-in-progress on another branch, and it will happily build a second copy. I’ve watched two sessions independently implement overlapping halves of the same feature, each sure it was first, because neither branch was visible to the other and neither said up front what it was about to touch. `wt-list.sh` tells you which branches exist. It says nothing about what each one intends to change.

**The lock is a suggestion.** `wt-lock` resists prune and move, and it flags a tree as live in the list, but it will not stop another agent from opening the same file on its own branch and editing away. The real guard against two agents clobbering one file is the up-front decomposition plus the discipline to run `wt-list.sh` and honor what it shows. An agent that skips the check has no seatbelt, just the shape of one.

**Abandoned trees pile up.** `wt-cleanup.sh` only sweeps branches already merged into `develop`. A worktree from a crashed or cancelled session is unmerged, still locked, and invisible to the sweep. It sits on disk with a full `node_modules` until someone removes it by hand. And an agent resuming a task can trip over a half-finished tree from an earlier run and read its stale state as current work.

**Losing the current directory.** The workflow says `cd .trees/<task-id>` and do everything there. Shell state doesn’t always survive between tool calls, and an absolute path into the primary checkout looks identical to one into a worktree. An agent that loses track of where it is can read the main checkout’s copy of a file, reason about it as though it were its branch’s version, and edit the wrong tree. The isolation holds only as long as the agent keeps its bearings.

## What this buys

The honest version: worktrees do not make independent tasks independent. If two agents both need to edit the same route, isolating their filesystems just delays the merge conflict, it does not prevent it. The decomposition still has to be real. What the pattern removes is the accidental collision, the kind that has nothing to do with the work and everything to do with sharing one mutable checkout. Those were most of my pain, and now they are gone by construction.

## Advantages and disadvantages

**Advantages**

- Accidental collisions disappear. Each agent gets its own files, index, and `HEAD`, so index-lock flicker, a stray `git stash` eating another session’s edits, and checkout thrash stop happening.
- Every task lands on its own `agent/<task-id>` branch, which keeps review and merge clean and stops one task’s half-finished mess from bleeding into another’s diff.
- The object store is shared, so the costly part of the repo lives on disk once and spinning up another tree is cheap.
- Each worktree gets a deterministic `DEV_PORT`, so several `next dev` servers run side by side instead of fighting over 3000.
- The lifecycle is scripted and wired into every agent definition, so the right setup and teardown happen without anyone remembering the incantation.
- `git rerere` is on by default, so a conflict you resolve once replays across the parallel merges that hit it again.
- Cleanup is fenced to `.trees/`, so the bulk sweep never reaches the primary checkout or the sibling worktrees I keep elsewhere.

**Disadvantages**

- The database isn’t isolated, and neither is anything else global (production through `db:migrate:deploy`, OAuth apps, third-party rate limits). File isolation quietly implies an isolation that isn’t there.
- Overlapping edits on separate branches turn into silent, deferred conflicts and semantic breakage that pass every isolated test and only show up at integration.
- A long-running worktree drifts from a moving `develop`, and nothing in the loop forces the re-fetch that would catch it up.
- Locks are advisory, so the actual protection against two agents editing one file is decomposition plus discipline, not anything git enforces.
- With several branches live, “does this already exist” has no single answer, and agents duplicate each other’s work when branches can’t see one another.
- Every worktree carries a full `node_modules`, so disk use and `npm ci` time multiply with each active task.
- Crashed or abandoned sessions leave locked, unmerged trees that the merged-only cleanup won’t reap, so someone clears them by hand.
- Coordination is still manual: the tooling shows which branches exist, not which files each agent means to touch.

The next habit I want in every agent sits upstream of all of this: stop and plan before touching a single file. That one is worth its own post.

More solutions to the confusion above are coming in the next few posts. Subscribe so you don’t miss ’em: drop your email into the box just below this post, or grab the [RSS feed](https://interlinedlist.com/blog/rss.xml).

*I’m [Adron](https://interlinedlist.com/user/adron), brainstorming and building [InterlinedList](https://interlinedlist.com/).*
