# AGENTS.md

This repository is an Obsidian-style knowledge vault. Treat it as a maintained learning system, not just a pile of Markdown files.

## Mission

- Evolve the vault so it is easy to learn from, restart, and maintain.
- Prefer improving retrieval, decision support, and study flow over adding isolated notes.
- Preserve broad coverage, but invest depth in the highest-leverage trunks rather than spreading effort evenly.

## Primary Structure

- Main content lives under `01-Areas/`.
- Each serious domain area should usually have:
  - `专题总览.md`
  - `学习进度.md`
  - `恢复笔记.md`
- Many mature areas also have layered subfolders such as:
  - `05-Topics`
  - `06-Maps`
  - `07-Templates`
  - `08-Onboarding` or `08-Playbooks`
  - other domain-specific layers

## Writing Conventions

- Write explanatory text primarily in Chinese.
- Preserve important English technical terms where they help precision.
- Keep notes concise but structured enough to teach from later.
- Prefer creating or strengthening:
  - problem-navigation pages
  - decision-navigation pages
  - index/map pages
  - progress/resume pages
  before expanding long tail content.

## Topology Rules

- Keep abstract topics separate from concrete systems, companies, people, and projects.
- Update the nearest relevant index or map when adding a meaningful new note.
- If a change alters how the user should enter or resume a domain, also update:
  - `专题总览.md`
  - `学习进度.md`
  - `恢复笔记.md`
- Favor “expert workbench” structure:
  - what problem am I solving
  - what decision am I making
  - where do I restart next time

## Files To Avoid

- Do not modify `.obsidian/*` unless explicitly asked.
- Do not modify `.p_obsidian/*` unless explicitly asked.
- Do not treat runtime/editor state files as meaningful knowledge content.

## Git Workflow

Before starting a meaningful batch of work:

1. Check workspace status with `git status --short`.
2. At the start of each new chat or meaningful batch, check the remote and run `git pull --ff-only` before editing when it is safe to do so.
3. If pull is blocked by network, SSH, local changes, or divergent history, do not overwrite local work; continue only after clearly noting the blocker.
4. Do not overwrite or discard existing local changes unless explicitly asked.

When finishing a meaningful batch:

1. Review changed files.
2. Stage only the files that belong to the task unless the user explicitly wants everything committed.
3. Commit with a clear batch-level message.

## Validation

- Validate wiki-links when you materially change vault topology.
- If a dedicated checker is unavailable in the current environment, at minimum inspect changed notes and linked indexes carefully for broken `[[wikilinks]]`.
- Call out any intentional or pre-existing missing links instead of silently ignoring them.

## Good Changes

High-value changes usually include one or more of these:

- turning a dense area into a clearer learning path
- adding problem/decision entry points
- connecting topic, map, and progress layers
- converting project-centric notes into reusable domain workbenches
- making the vault easier to resume after interruption

## When Unsure

- Prefer structure before coverage.
- Prefer restartability before completeness.
- Prefer linked systems of notes over isolated additions.
