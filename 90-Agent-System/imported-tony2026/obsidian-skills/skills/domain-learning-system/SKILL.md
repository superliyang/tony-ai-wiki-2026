---
name: domain-learning-system
description: Build and maintain a reusable learning system in an Obsidian vault, including domain structure, progress tracking, interruption recovery, and cross-domain reuse. Use when the user wants to study a domain over time, pause and resume cleanly, or reuse the same learning workflow for a new topic such as AI, finance, or international payments.
---

# Domain Learning System Skill

Use this skill when the user wants a repeatable way to study a domain over time rather than just generate one-off notes.

## Core Goal

Turn a topic into a durable learning system with:

- a domain map
- a recommended reading path
- progress tracking
- interruption recovery
- reusable templates for new domains

## Workflow

1. Define the domain scope and split it into 3 to 5 major sections.
2. Create a domain `专题总览.md` that explains what the domain is, why it matters, and the recommended learning order.
3. Create topic indexes that answer "what should I learn first".
4. Create a progress note using [PROGRESS_TEMPLATE.md](references/PROGRESS_TEMPLATE.md).
5. Create a resume note using [RESUME_TEMPLATE.md](references/RESUME_TEMPLATE.md).
6. When bootstrapping a new domain, use [DOMAIN_BOOTSTRAP_TEMPLATE.md](references/DOMAIN_BOOTSTRAP_TEMPLATE.md).
7. When the user pauses or switches domains, update the progress and resume notes before moving on.

## Minimum Memory Contract

Every domain should keep three memory layers:

- map memory: structure, indexes, and learning order
- progress memory: current topic, completed topics, weak spots, next step
- resume memory: a short handoff note for restarting quickly

## Interruption Recovery Rules

Before ending a study session, always leave:

- `current_topic`
- `last_completed`
- `next_up`
- `open_questions`
- `resume_note`

The `resume_note` should be short enough to re-read in under 2 minutes.

## Status Model

Prefer simple note states:

- `seed`: only a starting frame exists
- `learning`: actively being expanded and studied
- `stable`: mature enough to rely on

## When Bootstrapping a New Domain

Start with:

- domain `专题总览.md`
- at least one `主题索引.md`
- one progress note
- one resume note
- one example path from beginner to intermediate

If the user names a new domain, reuse the same workflow rather than inventing a new learning structure from scratch.

## References

- Progress template: [PROGRESS_TEMPLATE.md](references/PROGRESS_TEMPLATE.md)
- Resume template: [RESUME_TEMPLATE.md](references/RESUME_TEMPLATE.md)
- Domain bootstrap template: [DOMAIN_BOOTSTRAP_TEMPLATE.md](references/DOMAIN_BOOTSTRAP_TEMPLATE.md)
- AI example: [AI_EXAMPLE.md](references/AI_EXAMPLE.md)
- International payments example: [INTERNATIONAL_PAYMENTS_EXAMPLE.md](references/INTERNATIONAL_PAYMENTS_EXAMPLE.md)
