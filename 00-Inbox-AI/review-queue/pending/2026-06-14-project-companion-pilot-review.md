---
title: "Tony Review: Project Companion Pilot"
created: 2026-06-14
updated: 2026-06-14
status: pending
type: project-companion-review
source: "00-Inbox-AI/project-companion/2026-06-14-ai-first-cognitive-system-pilot-result.md"
project: "AI First Cognitive System"
tags:
  - review
  - project-companion
  - ai-first
  - codex
---

# Tony Review: Project Companion Pilot

## Review Summary

Codex ran the first manual `tony-project-companion` pilot on:

[[40-Projects/AI-First-Cognitive-System/README]]

Result:

[[00-Inbox-AI/project-companion/2026-06-14-ai-first-cognitive-system-pilot-result]]

## Recommendation

Recommended decision: `manual-on-demand`

Reason:

- The Project Companion workflow is useful, but still new.
- The system already has review backlog pressure.
- A live Hermes oneshot test already ran successfully and chose not to create duplicate output.
- Turning on another scheduled Hermes job now may create more candidates before Tony's review gate is flowing.

## Decision Options

Tony can choose one:

```text
manual-on-demand: 需要时手动触发 Hermes/Codex Project Companion scout
activate-hermes-weekly: 启用 hermes-project-companion-scout 周扫
defer: 暂缓 Project Companion，先清 review backlog
discard: 不继续 Project Companion workflow
```

## Suggested Follow-Up

If `manual-on-demand`:

- Codex or Hermes can run a narrow Project Companion pass whenever Tony asks.
- Hermes project scout remains `paused`.

If `activate-hermes-weekly`:

- Change `hermes-project-companion-scout` from `paused` to `active`.
- Keep output cap at 3 project signals.
- Review after one week.

## Live Test Result

Codex triggered a Hermes oneshot live test on 2026-06-14 with strict boundaries:

- read project companion context;
- write at most one note under `00-Inbox-AI/project-companion/`;
- do not modify canonical project/system files.

Hermes returned: no new file needed, because [[00-Inbox-AI/project-companion/2026-06-14-ai-first-cognitive-system-pilot-result]] already captured the current project-continuity signal.
