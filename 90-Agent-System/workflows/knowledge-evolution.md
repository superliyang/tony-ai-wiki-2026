---
title: "Knowledge Evolution Workflow"
created: 2026-06-03
updated: 2026-06-03
status: active
tags:
  - agent-system
  - workflow
  - knowledge-evolution
---

# Knowledge Evolution Workflow

This workflow keeps the vault evolving instead of becoming a one-time cleanup artifact.

## Loop

```text
Capture -> Review -> Promote -> Connect -> Refactor -> Remember
```

## Steps

1. Capture new material in `00-Inbox-AI/`.
2. Review direction through `00-Inbox-AI/review-queue/`.
3. Promote accepted material into `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`, or `90-Agent-System/`.
4. Connect the promoted note to the nearest overview, map, or project.
5. Refactor only a bounded slice: one topic, one map, one workflow, or one project at a time.
6. Update shared memory or current status when the change affects future agent behavior.

## Merge And Deduplicate

When duplicate notes appear:

1. Choose the more canonical or more recent note as the target.
2. Preserve unique context from the other note.
3. Add source backlinks if the source is imported legacy material.
4. Update links from maps and overviews.
5. Leave an archive note only when the old title carries search value.

## Promotion Quality Gate

Before a note becomes canonical, check:

- Does it answer a reusable question?
- Is the source or context traceable?
- Is it connected to a map or overview?
- Does it belong in knowledge, playbook, project, or agent system?
- Would Tony or an Agent know the next action after reading it?

## Maintenance Rhythm

- Small changes: update the nearest map or overview.
- Meaningful domain changes: update learning path, progress, or resume note.
- AI behavior changes: update [[90-Agent-System/当前状态]], [[90-Agent-System/命名规范]], rules, or workflows.
- Migration changes: update [[20-Maps/旧库迁移地图]].
