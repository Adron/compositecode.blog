---
title: "AI agent collisions: Worktrees aren't enough"
date: 2026-11-02 04:00:00 -0800
categories: ["AI & AI Tooling", "Coding Patterns & Practices"]
tags: ["ai", "agents", "worktrees", "collaboration"]
image: /assets/agent-collisions-beyond-worktrees/hero.png
---
Two developers editing the same service at once is older than Git. One changes an API, the other writes a caller against the old shape. One migration lands, the other assumes the previous schema. The collision may wait until integration, but nobody invented it with coding agents.

Agents compress the timeline. They can start the overlapping work within seconds, finish competing implementations before either human sees a diff, and spend tokens repeatedly “fixing” each other's changes. A human collision can cost far more than the token bill, sometimes an order of magnitude more once meetings, rework, and a delayed release are counted. That is a scenario, not a universal ratio. The new problem is how quickly both kinds of cost can accumulate while everyone thinks parallel work is progress.

I have already written the case for [giving each agent its own worktree](https://compositecode.blog/2026/08/19/worktrees/). Set that option aside here. Even with separate directories, two agents can change the same behavior, rely on incompatible contracts, or point tests at the same database. We need ways to manage the work itself.

## Assign ownership at the level that matters

File ownership is a useful start, but interfaces are the real collision surface. If one agent changes the response shape of `GET /orders` and another changes the frontend that consumes it, they are collaborating on one contract. Give one task ownership of that contract and sequence the dependent implementation after the new shape is agreed. If parallel work is valuable, freeze the interface first and let both agents build against a shared contract test.

The same rule applies to domain terms, schemas, feature flags, and deployment configuration. A small task register can say: agent A owns the API contract and tests; agent B owns the UI after the contract is approved; agent C performs a read only review. It need not be a complicated scheduler. Its purpose is to stop two plausible plans from quietly disagreeing.

Use short leases on hot areas. A lease says who is editing a shared contract, when they expect to hand it off, and where the result will appear. It is a social protocol with a visible record, not a file lock that magically prevents bad code. If an agent exceeds the lease, review progress and renew or split the task. Do not let an abandoned session hold the architecture hostage all day.

## Choose the kind of parallelism deliberately

Some tasks are naturally parallel: read only investigation, documentation of settled behavior, tests for a frozen contract, or independent review. Others are sequential: a migration followed by code that assumes it, a public API change followed by client updates, or two fixes to the same state machine. Forcing the second group into parallel execution creates integration work disguised as speed.

When the work can be split, split by stable boundary. “Agent A handles orders, agent B handles billing” may work if the interface between them is already explicit. “Agent A edits the first half of the file, agent B edits the second half” probably will not. File lines are not architecture. A good boundary gives each agent a testable outcome and few shared assumptions.

Another option is a single writer with several readers. Ask separate agents to investigate edge cases, inspect the current behavior, or critique the plan. Feed those findings to the writer after a human checks them. That gets the benefit of parallel thought without parallel mutation. It is particularly useful in a sensitive area where three implementations would be hard to reconcile.

## Isolate the shared things that are not code

Separate branches do nothing for a shared development database, a common staging environment, one cloud account, or the same test tenant. Give agent runs separate databases or schemas where practical, unique test data, distinct ports, and credentials limited to their task. If isolation is not available, schedule the shared resource as a single writer and make its current owner visible.

Generated artifacts need the same care. Two agents can each pass tests locally, then regenerate the same client library from different versions of a schema. A dependency lockfile can change under both tasks. A shared cache can hide an integration failure. Decide which task owns generation, pin the input, and test the combined result after both changes are present.

## Detect conflict before merge time

At task start, have each writer declare the files, interfaces, and resources it expects to change. Recheck that declaration when the diff expands. If an agent discovers it needs a boundary owned by another task, it stops and asks. This is a cheap rule, and it prevents a lot of expensive “helpful” edits.

At integration time, do more than resolve text conflicts. Run contract tests and the affected application path against the combined code. Look for two implementations of the same behavior, changed assumptions about defaults, and migrations whose order matters. A clean merge only proves Git could combine the files. It says nothing about whether the resulting application makes sense.

When a collision does occur, preserve both task intents before choosing a fix. Ask what behavior each agent was trying to protect, then select the contract the product actually needs. Blindly asking agents to reconcile each other's diffs often creates a third implementation that nobody intended.

## Keep parallel work cheaper than serial work

A small number of clear assignments, visible ownership, bounded runs, and one integration pass will beat a large crowd of agents whose outputs need arbitration. Count rework and review time alongside token use. If adding another agent makes the queue of conflicting diffs longer, reduce concurrency or stabilize the interface first.

Collisions were always part of software development. Agents make them arrive while the coffee is still hot. The fix is to make the boundaries, contracts, and shared resources explicit before the work starts, then check the integrated behavior before calling it done.
