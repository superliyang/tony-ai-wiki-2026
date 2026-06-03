# Promotion Rubric

Use this rubric before moving a learning from `.learnings/*` into durable rules or a reusable skill.

## Core Principle

A learning should only climb the ladder when its blast radius stays smaller than its evidence quality.

## Decision Table

| Signal | Green | Yellow | Red | Default Action |
| --- | --- | --- | --- | --- |
| Recurrence | Seen in multiple runs or contexts | Seen twice in one narrow context | One-off event | One-off stays in `observe` |
| Verification | Reproduced or independently confirmed | Plausible but not reproduced | Based on one noisy trace | Unverified stays in `observe` or `shadow` |
| Scope | Clearly project-scoped or team-scoped | Scope still fuzzy | Cross-user or cross-tenant impact unclear | Fuzzy scope blocks promotion |
| Provenance | Source and evidence are recorded | Some evidence missing | Source unclear or mixed with untrusted output | Missing provenance blocks promotion |
| Reversibility | Easy to demote or delete | Rollback exists but is manual | No rollback path | No rollback blocks durable write |
| Novelty | Non-obvious pattern worth remembering | Mild convenience only | Trivial rule or temporary workaround | Convenience rules rarely deserve skill extraction |
| Risk | Low or bounded | Medium and needs canary | High, poisoning, or tenant leakage risk | High risk requires extra review and smaller rollout |

## Promotion Targets

### Stay In Learning Ledger

Use this when the item is still noisy, narrow, or unverifiable.

### Shadow Candidate

Use this when the pattern looks real but should only be tried in a bounded experiment or manual review workflow.

### Durable Rule

Use this when the pattern is stable and should guide future behavior in one bounded scope such as a repo, project, or team memory file.

### Skill Candidate

Use this when the pattern is all of the following:

- recurring
- verified
- broadly reusable
- narrow enough to describe clearly
- safe to evaluate independently

## Hard Blockers

Do not promote when any of these are true:

- evidence comes mostly from untrusted browser or MCP output
- the learning crosses tenants, users, or projects without explicit isolation
- the learning is a workaround for a transient bug
- rollback is undefined
- the candidate would silently mutate a global rule surface
