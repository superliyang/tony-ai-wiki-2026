---
name: ai-open-source-research-system
description: Build or evolve an AI open-source project knowledge system in an Obsidian vault by separating categories, organizations, projects, reusable engineering patterns, watchlists, and intake workflows. Use when Codex needs to study AI open-source projects systematically instead of collecting repos, compare open-source stacks, keep a project watchlist, and maintain a restartable knowledge graph with progress and Git-backed sync.
---

# AI Open Source Research System

## Overview

Use this skill when the user wants to build a durable AI open-source control tower rather than a loose repo bookmark list.

Pair this skill with [$obsidian-domain-research-graph](/Users/tony/.codex/skills/obsidian-domain-research-graph/SKILL.md) when the area topology still needs shaping, with [$knowledge-vault-research-sync](/Users/tony/.codex/skills/knowledge-vault-research-sync/SKILL.md) when the vault needs indexes, maps, progress updates, wikilink validation, and Git checkpoints, and with [$self-improving-learning-ledger](/Users/tony/.codex/skills/self-improving-learning-ledger/SKILL.md) when repeated research judgments should be captured as bounded learnings.

## Core Outcome

A good run of this skill should leave behind:

- a clearer open-source area boundary
- categories, organizations, projects, and patterns kept separate
- a useful watchlist instead of a random star list
- repeatable intake and refresh workflows
- progress and resume pages that make the area restartable

## Default Topology

For Tony's current vault, prefer this split under `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Open-Source`:

- `01-Categories`: stable project classes such as local runtime, serving, agent runtime, memory, eval, and AI platform
- `02-Organizations`: the organizations or communities behind clusters of projects
- `03-Projects`: one note per repo or flagship project
- `04-Patterns`: reusable engineering patterns extracted from multiple projects
- `05-Case-Studies`: stack combinations or real adoption examples
- `06-Maps`: maps, Base files, and Canvas navigation
- `07-Templates`: reusable intake templates
- `08-Workflows`: intake, watchlist, and maintenance workflows
- `09-Watchlist`: the active watchlist and update cadence

## Workflow

### 1. Decide whether the project deserves entry

Do not add every repo. First decide whether it has:

- engineering value
- learning value
- migration value
- stable enough signals to justify attention

Read [references/watchlist-rules.md](references/watchlist-rules.md) when deciding whether something belongs in the control tower.

### 2. Place it in the right layer

Before writing, decide whether the new information belongs in:

- a category note
- an organization note
- a project note
- a pattern note
- a watchlist note

Do not mix these layers casually.

### 3. Use stable intake dimensions

When creating or updating a project note, answer at least:

- what problem it solves
- why it matters now
- what layer of the stack it belongs to
- whether it is a `底座`、`壳层`、`平台` or `子系统`
- what its core architecture or operating model looks like
- what objects, components, or abstractions matter most
- what it is adjacent to and how it differs from nearby projects
- whether it fits local experiments, production study, or both
- what the next experiment should be
- what risks, boundaries, or hidden costs deserve attention
- how the project works internally
- what its main request or data path looks like
- what architecture or dataflow diagram should be drawn

Read [references/project-intake-checklist.md](references/project-intake-checklist.md) for the checklist.

### 4. Always extract one level up

Whenever a project note is added, ask whether it should also update:

- a category note
- an organization note
- a pattern note
- the watchlist
- the map / base / canvas navigation

A good open-source knowledge base is not just repo pages. It must also contain the engineering patterns that the repos represent.

### 5. Keep the watchlist small and useful

Prefer a watchlist with explicit cadence, such as weekly, biweekly, or stable monitoring.

### 6. Preserve restartability

Update:

- `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Open-Source/学习进度.md`
- `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Open-Source/恢复笔记.md`

whenever the recommended study path or active watchlist changes meaningfully.

## Working Rules

- Do not organize by GitHub stars alone.
- Prefer official docs and repository sources.
- Separate repo facts from your own engineering judgment.
- Keep project notes concise but decision-useful; deep project cards should usually include stack position, architecture, operating model, work principle, main flow, diagrams, comparisons, risks, and next experiments rather than stopping at one-paragraph summaries.
- Use Chinese explanatory text with English project names preserved where helpful.
- When a judgment becomes stable and repeated, consider capturing it through bounded learnings instead of baking it directly into global rules.

## References

- Taxonomy: [references/taxonomy.md](references/taxonomy.md)
- Intake checklist: [references/project-intake-checklist.md](references/project-intake-checklist.md)
- Watchlist rules: [references/watchlist-rules.md](references/watchlist-rules.md)
- Pattern extraction: [references/pattern-extraction.md](references/pattern-extraction.md)
