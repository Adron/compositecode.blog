---
title: Additive vs. Mutative vs. Destructive Code Changes (and Why AI Agents Love the Wrong One at 2:13AM)
date: 2026-02-12 09:53:51 -0800
last_modified_at: 2026-02-20 11:03:17 -0800
permalink: /2026/02/12/additive-vs-mutative-vs-destructive-code-changes-and-why-ai-agents-love-the-wrong-one-at-213am/
slug: additive-vs-mutative-vs-destructive-code-changes-and-why-ai-agents-love-the-wrong-one-at-213am
wp_id: 74214
original_url: https://compositecode.blog/2026/02/12/additive-vs-mutative-vs-destructive-code-changes-and-why-ai-agents-love-the-wrong-one-at-213am/
categories:
- AI & AI Tooling
- Code Stories
- Programming
tags:
- agents
- ai agent
- ai agents
- ai assistants
- ai coding
- chatgpt
- claude code
- code changes
- coding
- cursor
- gemini
- programming
excerpt: The piece explores the unique challenges software developers face, particularly with the rise of AI tooling in coding practices. It highlights a specific “pain” associated with AI-generated code changes, which can introduce risks due to their propensity for errors and misunderstandings of existing systems. The author categorizes types of code changes—additive, mutative, destructive, transformative, cosmetic, and behavioral drift—emphasizing the potential hazards of AI’s approach to these changes. Recommendations for mitigating risks include prioritizing additive changes, enforcing strict testing and code review processes, and treating AI tools as assistants rather than co-authors in software development.
image: /wp-content/uploads/2020/04/devto-programming.jpg
---

There’s a particular kind of pain that only software developers know.

Not the “production is down” kind of pain.

Not the “we deployed on Friday” kind of pain.

No, I mean the slow creeping dread of pulling the latest changes, running the tests, and realizing the codebase has been “improved” in a way that feels like someone rearranged your entire kitchen… but left all the knives on the floor.

And lately, this pain has been supercharged by AI tooling. Cursor, Claude, Copilot, Gemini, ChatGPT-driven agents, whatever your poison is this week, all share a similar behavioral pattern:

> They can produce a stunning amount of output at an impressive speed… while quietly reshaping your system into something that looks correct but behaves like an alien artifact from a parallel universe.

The reason is simple: AI agents don’t “change code” the way humans do. They don’t naturally respect boundaries unless you explicitly enforce them. They operate like an overly enthusiastic intern with root access and no fear of consequences. To understand why this happens, we need to talk about the different *types of code changes*, and how AI tooling tends to drift toward the most dangerous ones.

So let’s name the beasts.

## The Four (Actually Six) Types of Code Changes

When most people talk about changes in code, they speak in vague language:

- “Refactor”
- “Cleanup”
- “Fix”
- “Update”
- “Improve”
- “Make it better”

These words are meaningless without a precise mental model.

Instead, we should talk about code changes in terms of *how they affect the system*.

Here are the major categories.

## Additive Changes

An additive change introduces new code without altering existing behavior.

It’s an extension. A new layer. A new function. A new class. A new endpoint. A new capability.

Examples:

- Adding a new API endpoint `/v2/orders`
- Adding a new feature flag
- Adding a new database migration that creates a table
- Adding a new logging wrapper (without changing logic)
- Adding a new event handler without touching the existing one

**Why additive changes are safe:**
Because they’re naturally reversible and tend to preserve the existing system. They can often be deployed alongside existing functionality without breaking things.

**Downside:**
Additive changes can cause bloat, duplication, and architectural sprawl if left unchecked.

But they rarely detonate your production system instantly.

## Mutative Changes

A mutative change modifies existing code behavior *in-place*.

This is when you touch something already working and alter it.

Examples:

- Changing the validation logic for a form field
- Updating a method signature and refactoring its callers
- Modifying a SQL query to include a new join
- Changing retry logic or timeouts
- Updating a shared library used by 12 services

**Why mutative changes are dangerous:**
Because the blast radius is often invisible. You are changing code that already has implicit contracts: other parts of the system rely on its current behavior, even if those contracts aren’t documented.

Mutative changes are where regressions are born.

## Destructive Changes

A destructive change removes or breaks existing functionality, intentionally or unintentionally.

Sometimes destructive changes are explicit: you delete a module.

Sometimes they’re accidental: you “refactor” and suddenly a feature stops working.

Examples:

- Removing an endpoint and replacing it with a new one
- Deleting configuration keys or environment variables
- Removing database columns
- Deleting “unused” code that is actually used in production by a cron job nobody remembers exists
- Replacing a service layer with a new abstraction and losing business logic

**Why destructive changes are catastrophic:**
Because they don’t just introduce risk, they remove stability.

A destructive change is like cutting the brake lines on your car because you wanted to reduce weight for better fuel economy.

## Transformative Changes

This is the big one people don’t talk about enough.

A transformative change restructures the system without necessarily changing the *intended* behavior, but it changes *how the system works* internally.

This includes refactors, rewrites, architectural reorganizations, and “cleanups” that shuffle everything around.

Examples:

- Converting controllers into minimal routers and pushing logic into service layers
- Replacing synchronous logic with async pipelines
- Switching ORM patterns (Entity Framework → Dapper, Hibernate → jOOQ)
- Introducing CQRS/event sourcing into a CRUD app
- “Modernizing” a codebase from classes to functional patterns
- Renaming 40 files and moving folders

**Why transformative changes are risky:**
Because even if the outward behavior is supposed to remain the same, the *internal invariants change*. And that’s where subtle bugs appear.

Transformative changes are the ones that make you say:

> “It passes tests, but I don’t trust it.”

And you’re right not to trust it.

## Cosmetic Changes

Changes that affect formatting, naming, style, and readability without changing runtime behavior.

Examples:

- Renaming variables
- Reformatting code
- Updating linting rules
- Converting `var` to explicit types
- Adjusting whitespace and ordering imports

**Why cosmetic changes matter:**
Because they can create massive diffs and destroy blame history, while contributing almost nothing to functionality.

But they can also improve maintainability if controlled. Cosmetic changes are like repainting the house. Not inherently bad, but don’t pretend it’s structural engineering.

## Behavioral Drift Changes

This is the one that AI loves.

A behavioral drift change is when code is altered in a way that *seems equivalent*, but subtly changes behavior. This isn’t a deliberate rewrite. It’s a “close enough” modification.

Examples:

- Changing date parsing logic
- Adjusting rounding behavior in financial calculations
- Switching from `null` checks to default values
- Replacing `==` semantics with `.equals()` or vice versa in the wrong place
- Replacing an exception with a fallback
- Changing an error return to a success return with warnings

**Why drift is the most dangerous category:**
Because nobody notices until production data is corrupted, billing is wrong, or a customer loses their order history.

Drift is silent sabotage. And it happens constantly when AI is “helping.”

# How AI Tooling Tends to Make These Changes

Now we get to the meat of it.

Because AI tools don’t operate like careful engineers. They operate like probability engines trained on millions of codebases, many of which were written by maniacs.

When you ask Cursor or Claude to “fix this bug,” you aren’t hiring a developer.

You’re summoning a code-shaping entity that optimizes for *plausible output*, not correctness.

Let’s break down the patterns.

## AI Loves Additive Changes (Because They’re Easy)

When AI doesn’t fully understand the system, it tends to *add* code rather than modify existing logic.

This is why you’ll often see:

- New helper methods
- New wrappers
- New abstractions
- New DTOs
- New validation layers

Even when you didn’t ask for them.

This is AI’s instinct: it avoids touching the “unknown dangerous parts” by layering something on top.

Additive changes are the safest type of change AI can make, but also the fastest way to create redundancy and architectural sludge.

AI will happily create:

- `OrderService2`
- `OrderServiceNew`
- `OrderServiceRefactored`
- `OrderServiceImprovedFinal`

Like it’s naming files on your Desktop.

## AI Makes Mutative Changes Without Respecting Contracts

When AI does modify existing code, it tends to treat code as if it exists in isolation. It doesn’t “feel” the social weight of a public method signature. It doesn’t get nervous changing a shared interface. It doesn’t understand that a method returning `null` is a *feature*, not a mistake.

So AI mutates logic aggressively:

- Reorders parameters
- Changes return types
- Adds exception throws
- Removes “redundant” branches
- Replaces explicit logic with generalized patterns

AI doesn’t see the difference between:

- “This is redundant”
- “This is a business rule”
- “This is legacy behavior required by a client integration”

It just sees tokens.

## AI Produces Destructive Changes as “Cleanup”

This is where the bodies start piling up.

AI agents are incredibly prone to destructive changes when given vague prompts like:

- “Simplify this”
- “Refactor this”
- “Remove duplication”
- “Modernize this”
- “Make it clean”

Because AI interprets these requests literally. It will delete things that appear unused. It will remove error handling because “it’s too verbose.” It will remove fallback logic because “it’s redundant.”

And then it will confidently declare:

> “The code is now simpler and easier to maintain.”

Sure. It’s also missing half the business logic. But it’s definitely simpler!

## AI Is Addicted to Transformative Changes

This is the Cursor/Claude special.

AI tooling, especially when running in agent mode, tends to make **transformative** changes by default.

Why?

Because transformative changes look impressive. Maybe? Often times, who really knows!

When an AI “fixes” a problem by rewriting 18 files, it *feels* like it did real work. It generates a huge diff, which satisfies the human brain’s bias that “more change means more progress.” Really of course, this is the manager’s brain going “ooo changes!” meanwhile any seasoned veteran of coding wars knows, less is more, being able to delete code and maintaining functionality is a pinnacle unto itself!

But in reality, transformative changes are where AI is most likely to introduce drift, regressions, and architectural incoherence.

AI’ list of transgressions:

- Restructure entire folder hierarchies
- Rename modules
- Replace existing patterns with new ones
- Introduce dependency injection frameworks
- Add middleware layers
- “Improve” the architecture

Without any understanding of why the existing structure exists.

AI agents treat your codebase like a sandbox project.

You treat it like your livelihood.

## AI Generates Cosmetic Noise Constantly

This is the “diff pollution” problem.

AI loves to:

- Reformat everything
- Alphabetize imports
- Rename variables
- Normalize spacing
- Adjust indentation

Sometimes because your tooling triggers it, sometimes because it’s “cleaning up.” This creates massive pull requests where 80% of the changes are irrelevant. The worst part? It makes code review nearly impossible. That’s how destructive or drift changes slip through unnoticed.

## AI Causes Behavioral Drift as a Side Effect of “Being Helpful”

Behavioral drift is the true danger of AI agents.

AI will often “improve” code by introducing assumptions:

- “If the value is missing, default to empty string”
- “If the call fails, just retry”
- “If the user is null, create a new user”
- “If parsing fails, ignore the record”

These changes *sound reasonable*.

But in production systems, they often violate business requirements.

A missing value might indicate fraud.
A parsing failure might indicate corrupted data.
A null user might indicate authentication failure.
A failed call might require escalation, not retry.

AI doesn’t know that. It just wants the code to run.

# The Agent Problem: AI Doesn’t Think in Diffs, It Thinks in Outcomes

A human developer usually thinks like this:

> “I need to make the smallest possible change that fixes the issue.”

AI agents think like this:

> “I need to output something that looks like the issue is resolved.”

That’s a fundamental mismatch.

Humans optimize for minimizing blast radius.
AI optimizes for plausibility and completeness.

Which is why agents tend to do one of two things:

- **Under-change:** add a workaround that doesn’t solve the root problem
- **Over-change:** rewrite everything until the problem disappears

Neither is what you want.

# How to Shield Your Codebase From AI’s Worst Instincts

If you’re using Cursor, Claude agents, Copilot Workspace, or anything similar, you need to treat it like a junior developer with unlimited confidence.

You don’t “ban” them. You constrain them. Here’s how.

## Force Additive-First Behavior

When possible, require AI changes to be additive instead of mutative.

Instead of:

> “Update the order validation logic”

Try:

> “Add a new validator class and wire it in behind a feature flag.”

Instead of:

> “Refactor this service”

Try:

> “Create a new service and leave the existing one untouched. Then call the new one from a single entry point.”

Additive-first strategies keep the blast radius small and allow rollback.

## Use Feature Flags Like a Civilized Person

AI agents are great at building functionality.

They are terrible at understanding deployment environments. So if you let them directly mutate production behavior, you’re gambling. Wrap AI-driven changes in feature flags:

- Config toggles
- Environment-based switches
- Percentage rollouts

This lets you deploy safely and progressively. If the AI broke something, you turn it off, not scramble for a hotfix at midnight.

## Require Tests Before Accepting Any Mutative Change

This is non-negotiable.

If AI modifies behavior, you should require:

- Unit tests for the modified logic
- Regression tests for the bug it claims to fix
- Integration tests if boundaries are crossed

If the AI can’t produce tests, the change is not trustworthy. AI without tests is basically just autocomplete with better marketing.

## Use Diff Discipline: No “Mega PRs”

AI agents love to generate 2,000-line diffs. That is poison. Your review process cannot survive that.

Set a hard limit:

- If the diff is too large, reject it.
- Split the work.
- Require smaller incremental commits.

The goal is to keep changes reviewable. Because if you can’t review it, you can’t trust it and if you can’t trust it, you shouldn’t merge it.

## Lock Down Public Interfaces

AI agents are particularly reckless with interfaces.

So you need guardrails:

- Treat public interfaces as immutable
- Require explicit approval to change method signatures
- Require explicit approval to change API contracts
- Require explicit approval to change database schema

This can be enforced with:

- OpenAPI contract tests
- GraphQL schema checks
- Migration approval workflows
- CI checks for breaking changes

## Gatekeep With CI Like You Actually Mean It

If you’re using AI agents without strict CI, you are essentially YOLO-ing your production system.

Good CI isn’t optional anymore. It’s the immune system.

At minimum:

- Build must pass
- Tests must pass
- Lint must pass
- Static analysis must pass
- Dependency scanning must pass

If AI is writing code, CI is your last line of defense against nonsense.

## Establish “Architectural No-Fly Zones”

Some parts of the codebase should not be touched by agents without human supervision.

Examples:

- Authentication
- Payments
- Authorization policies
- Billing
- Schema migrations
- Distributed locking logic
- Retry/backoff code
- Anything involving money or identity

AI can help explore or suggest changes. But merging autonomous edits in these zones is just irresponsibility wearing a hoodie.

## Require Explanations in Plain English

AI should be able to explain:

- What changed
- Why it changed
- What behavior is now different
- What the risk is
- How to rollback

If the agent can’t produce that narrative clearly, it doesn’t understand the change. If it doesn’t understand the change, you shouldn’t merge it.

# The Reality: AI Is a Power Tool, Not a Teammate

Cursor and Claude agents are incredible at generating scaffolding, filling in boilerplate, and accelerating the “typing” part of development. But they are not good at respecting system constraints unless those constraints are enforced. AI is not a senior engineer. It’s a high-speed code generator that must be constrained by process, testing, and review. Otherwise it will absolutely turn your codebase into a chaotic haunted house.

# Summary: Good Practices for AI Tooling in Real Codebases

Here’s the blunt checklist. If you want to use AI agents without wrecking your system, do this:

- **Prefer additive changes over mutative changes**
- **Avoid destructive changes unless explicitly planned**
- **Treat transformative refactors as high-risk operations**
- **Reject PRs with massive diffs**
- **Require unit and regression tests for every behavioral change**
- **Use feature flags for AI-driven modifications**
- **Lock down public API and schema contracts**
- **Enforce strict CI gates (build, tests, lint, security scans)**
- **Define “no-fly zones” (auth, billing, payments, migrations)**
- **Demand plain-English explanations of what changed and why**
- **Never merge code you cannot review**
- **Assume AI introduces behavioral drift unless proven otherwise**
- **Use AI for scaffolding, not architecture rewrites**
- **Keep rollbacks easy and cheap**

If you treat AI like a disciplined assistant, it can make you dramatically faster. If you treat it like a co-author of your system design…

well.

Enjoy your new microservice architecture built entirely out of vibes and false confidence.
