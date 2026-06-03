---
title: "Legacy Vault Migration Workflow"
created: 2026-06-03
updated: 2026-06-03
status: active
tags:
  - agent-system
  - workflow
  - migration
---

# Legacy Vault Migration Workflow

This workflow tells Codex, ChatGPT, Hermes, and future agents how to work with imported `tony2026` material.

## Boundary

Imported material is source context, not disposable draft text.

Agents may read and summarize it freely, but should not rewrite imported notes in bulk unless Tony explicitly asks for a migration batch. New synthesized notes should usually be created in the current formal layer and link back to imported sources.

## Current Import Layout

| Layer | Path |
|---|---|
| Knowledge assets | `10-Knowledge/_Imported/tony2026/` |
| AI inbox history | `00-Inbox-AI/imported-tony2026/` |
| Agent capability history | `90-Agent-System/imported-tony2026/` |
| Imported project material | `40-Projects/imported-tony2026/` |

Runtime state and sensitive files were intentionally excluded from the import: `.git`, `.obsidian`, `.p_obsidian`, `.space`, `.makemd`, `node_modules`, `.venv`, `.env`, `.env.local`, and `.DS_Store`.

The old `.github/`, `.learnings/`, `copilot/`, `requirements.txt`, and `.gitignore` were imported as historical AI collaboration assets under `90-Agent-System/imported-tony2026/`.

## Promotion Protocol

When asked to migrate or refine part of the old vault:

1. Read the imported area's `专题总览.md`, `学习进度.md`, and `恢复笔记.md` first.
2. Identify the target current layer: knowledge domain, map, playbook, project, inbox, or agent workflow.
3. Preserve the old note when it carries narrative context; create a new crystallized note only for a clearly bounded topic.
4. Add concrete source backlinks to the imported source note.
5. Update the nearest human navigation page: domain overview, [[20-Maps/旧库迁移地图]], or [[20-Maps/总地图]].
6. For meaningful changes, update `00-Home/当前主线.md` if the active focus changes.

## Do Not

- Do not flatten old folders into a single topic dump.
- Do not remove imported files just because a summary exists.
- Do not copy old `.env.local` or runtime app state into the current vault.
- Do not assume a missing current-domain folder means the old area is unimportant.

## Good First Migration Batches

| Batch | Reason |
|---|---|
| AI-Learning control tower and maps | Highest leverage for human navigation |
| AI-Engineering AgentOps notes | Directly supports Codex/Hermes/ChatGPT collaboration |
| International-Payments runbooks | Preserves strong domain operating knowledge |
| Security maps and playbooks | Useful as reusable governance/control assets |
| Skills-Gaming project plus domain notes | Bridges knowledge assets and active project material |
