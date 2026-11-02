---
title: "AI code quality: Ship fast without the fires"
date: 2026-11-05 04:00:00 -0800
categories: ["AI & AI Tooling", "Coding Patterns & Practices"]
tags: ["ai", "code review", "quality", "testing"]
image: /assets/ai-code-needs-a-faster-quality-loop/hero.svg
---
The [October 2025 DynamoDB disruption](https://aws.amazon.com/message/101925/) spread through AWS after a race condition in automated DNS management erased the service's regional endpoint. Its published cause was an automation defect, not AI-written code. That distinction matters. If we blame every outage on an LLM, we miss the specific mechanisms that made the outage possible.

The AI-related cases are narrower and messier. Reporting connected an AI coding tool to an [AWS Cost Explorer interruption](https://www.aboutamazon.com/news/aws/aws-service-outage-ai-bot-kiro), while Amazon attributes that event to misconfigured access controls and disputes the reported cause. In separate [Amazon retail incidents](https://www.aboutamazon.com/news/company-news/amazon-outage-ai-financial-times-correction), the company says an engineer followed advice an AI tool inferred from an outdated internal wiki. These cases do not prove that faster AI development caused AWS's broad outage. They do show how stale context and excess authority can give an ordinary mistake operational reach.

There is a cleaner example. In 2025, [Replit acknowledged](https://replit.com/blog/doubling-down-on-our-commitment-to-secure-vibe-coding) that its agent deleted data from a user's application database while development and production data were insufficiently separated. The data was restored, but the production application could have been broken during the recovery window. Replit's response was to separate the databases by default and keep the agent away from production data during development. The system had given a development tool production reach.

Most failures look less dramatic. An agent adds a retry around a payment call without an idempotency key. It makes a slow query pass the unit suite by mocking the database. It replaces a boring, explicit validation rule with a generic helper that accepts an empty value. Each diff can look reasonable. Each can make the application worse. Generate enough of those diffs, and the review queue becomes an exercise in finding one dangerous sentence in a book that keeps rewriting itself.

## The old gate is getting squeezed

The traditional bargain was that a developer made a change, a reviewer read it, CI ran, and the team shipped. Those steps still matter. The trouble is the arrival rate. Agents can produce plausible changes faster than a team can understand them. A reviewer staring at a giant generated PR is likely to check syntax and style, then miss the changed behavior. A test suite assembled by the same agent can reinforce the same mistaken assumption.

The answer cannot be “add three more approvers.” That makes the queue longer without making anyone better informed. The real unit of review needs to get smaller, and the evidence attached to each change needs to get better. I argued for [small, scoped changes](https://compositecode.blog/2026/04/15/hurting-or-helping-devs/) before the current volume of agent output made the problem obvious. A reviewable diff has one job, names its expected behavior, and says which failure modes it considered. A generated feature that rewrites twelve unrelated files needs to be split before it reaches a reviewer.

## Put checks where mistakes enter

Start before code generation. Give the agent the current source of truth: the domain terms, the relevant files, the interface it must preserve, and the operations it may perform. If the design is unclear, ask for a plan and a list of unknowns first. My [ask, plan, confirm workflow](https://compositecode.blog/2026/08/20/plan-then-build/) is useful here because it makes a change in authority visible. A read only investigation should not quietly become a production edit.

Next, make every implementation change answer three concrete questions in its PR description:

1. What behavior changed for a user or another system?
2. What happens when the dependency is slow, unavailable, or returns an unexpected result?
3. How will we know the change is wrong after deployment, and how will we back it out?

Those questions are more valuable than a declaration that “all tests pass.” Tests need to exercise the behavior, including a failed request, a duplicate request, and a partially completed operation where those cases apply. A retry that works on the happy path can duplicate an order. A migration that passes locally can lock a table under production load. The test plan should follow the risk, not the quantity of generated code.

Then put hard boundaries around the places where a wrong answer is expensive. Development agents do not need production credentials. Migration agents do not need permission to destroy live data to draft a schema change. Deployments that alter durable state deserve a separate authorization step and a recovery rehearsal. The Replit incident makes that point more clearly than any policy memo.

## Review the behavior, then the shape of the code

“Clean code” is too easy to reduce to formatting. I want a reviewer to trace the new behavior through the caller, the domain rule, the persistence boundary, and the observable result. Does the code use the team's vocabulary? Does it duplicate a rule already implemented elsewhere? Does it leave a clear place for the next change? Is the error path understandable to someone on call at 2 a.m.?

An independent review helps when it has a specific lens. Ask one reviewer to look for changed invariants and another to check operational failure modes. Give both the actual diff and current contract. Do not ask the authoring agent to certify its own work with a cheerful paragraph. In [additive, mutative, and destructive changes](https://compositecode.blog/2026/02/12/additive-vs-mutative-vs-destructive-code-changes-and-why-ai-agents-love-the-wrong-one-at-213am/), I used those categories to make the impact of a diff easier to see. They also help decide how deep the review and rollout need to be.

Finally, use production as a feedback loop without treating customers as the test suite. Release behind a flag when practical. Start with a small cohort. Watch error rate, latency, saturation, and business outcomes. Have a known rollback path. If the change modifies data, confirm that rollback restores behavior even when old code meets new data. An automatic rollback triggered by a reliable signal beats a heroic incident call after everyone has gone home.

## Change the throughput target

The target is not generated lines per engineer or PRs merged per day. It is useful behavior delivered without borrowing trouble from next week. Track how often a change needs a follow-up fix, how long failures take to detect, and how easily the team can restore service. If those numbers get worse while code output rises, the pipeline is accelerating in the wrong direction.

AI can make the first draft cheap. Understanding the system, containing the blast radius, and learning from what shipped are still the work. A faster keyboard makes those jobs more urgent.
