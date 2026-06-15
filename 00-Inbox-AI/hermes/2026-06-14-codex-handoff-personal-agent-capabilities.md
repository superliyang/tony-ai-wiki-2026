---
title: "Codex Handoff - Personal Agent Capabilities"
created: 2026-06-14
status: handoff
source: codex
target: hermes
tags:
  - hermes
  - codex
  - handoff
  - personal-agent-capabilities
---

# Codex Handoff - Personal Agent Capabilities

Hermes, Codex has updated Tony's AI First vault with a capability-alias layer for personal Agents.

## What Changed

- Added [[60-Agents/Personal-Agent-Capabilities]]
- Added [[90-Agent-System/workflows/project-companion]]
- Added [[00-Inbox-AI/project-companion/README]]
- Updated fixed entrances and maps so Agents can discover the new layer.

## Design Rule

```text
workflow first, persona second
```

Personal Agent names are aliases over existing Hermes / Codex workflows, not a second organizational layer.

## Hermes-Relevant Capability Aliases

| Alias | Hermes Role |
|---|---|
| `tony-research-scout` | core radar, topic scout, curated scout |
| `tony-learning-coach` | growth track and learning-task generation |
| `tony-reflection` | weekly synthesis and follow-up review |
| `tony-gardener` | memory review and review candidate generation, with Codex owning promotion |
| `tony-project-companion` | project-continuity signal detection only; Codex owns project page updates |

## New Writable Staging Area

Hermes may propose project continuity signals in:

```text
00-Inbox-AI/project-companion/
```

Hermes should not write directly into:

```text
40-Projects/
```

unless Tony explicitly asks.

## Suggested Next Hermes Behavior

When weekly synthesis or review scanning finds project-relevant signals, Hermes may create at most three project companion notes using:

- [[90-Agent-System/prompts/hermes-project-companion-scout]]
- [[90-Agent-System/workflows/project-companion]]

Good project signals include:

- an accepted learning package should turn into a build action;
- a project has not moved but still appears in weekly decisions;
- a review item needs a project-level decision;
- a tool/workflow change should update the AI First Cognitive System project.

Prefer no output over filler.

