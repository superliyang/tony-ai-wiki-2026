---
name: knowledge-vault-research-sync
description: Maintain an Obsidian-style learning vault while researching topics, writing or restructuring notes, updating progress and resume pages, validating wikilinks, and safely checkpointing changes to GitHub. Use when Codex is working in a knowledge base or learning vault and needs to create or revise notes, refresh indexes and maps, keep study state current, or commit and push meaningful vault changes on demand or via automation.
---

# Knowledge Vault Research Sync

## Overview

Use this skill to work inside an Obsidian-style learning vault that is stored in Git. Follow one workflow that covers content research, note maintenance, state tracking, link validation, and safe GitHub checkpointing.

For Tony's current vault, assume these conventions unless the user says otherwise:

- Main content lives under `/Users/tony/Documents/vault/tony2026/01-Areas`
- Domain areas often keep `学习进度.md` and `恢复笔记.md` at the area root
- `.obsidian` is runtime/app state and should not be included in automatic checkpoints unless the user explicitly asks
- Index pages and map pages should be updated when new notes materially change the topology

## Autonomous Batch Mode

When the user wants steady progress without interruption, do not checkpoint every tiny edit. Work in coherent batches.

In this mode:

- inspect the current area and its state pages first
- choose one bounded slice that is worth a real checkpoint
- finish the slice end-to-end, including indexes, maps, and state pages when needed
- validate links only after the batch is coherent
- checkpoint once per meaningful batch, not once per file
- stop only when the batch is deliverable, Git is blocked, or a risky decision needs user approval

Read [references/autonomous-delivery-loop.md](references/autonomous-delivery-loop.md) when operating this way.

## Workflow

### 1. Identify the active area and note layer

Decide which layer the work belongs to before editing:

- `Foundations`: history, concepts, methods
- `Learning`: companies, people, models, systems, papers, topics, maps
- `Engineering`: runtime, training, deployment, evaluation, workflows
- `Applications`: business or industry use cases

Also decide whether the change belongs in:

- an entity page
- a topic page
- an index page
- a map page
- a progress/resume page

### 2. Make the content changes

When adding or expanding notes:

- keep the topology clean; do not mix abstract topics with concrete systems if the vault already separates them
- use the existing area conventions for naming, links, and frontmatter
- prefer updating the nearest relevant index or map when a new entity or topic is added
- keep writing concise but structured enough to teach from later

For this vault, prefer Chinese explanatory text with English technical terms preserved where useful.

### 3. Refresh study-state pages when the change is meaningful

Update `学习进度.md` and `恢复笔记.md` when the work changes the user's learning path, topology, or recommended restart point.

Typical triggers:

- a new sub-path or comparison line was added
- a new systems layer or company layer was introduced
- the recommended reading order changed
- a topic moved from sketch to usable study material

Skip state-page updates for tiny edits unless the user explicitly wants a running log.

### 4. Validate wikilinks before checkpointing

Run the bundled checker before committing substantial note changes.

Use:

```bash
python3 "$CODEX_HOME/skills/knowledge-vault-research-sync/scripts/check_obsidian_wikilinks.py" \
  "/Users/tony/Documents/vault/tony2026/01-Areas/AI-Learning" \
  "/Users/tony/Documents/vault/tony2026/01-Areas/AI-Engineering"
```

You can pass any area roots that are relevant to the current task.

If the checker reports missing links:

- fix the links when they were introduced by the current task
- if a missing target is intentional or pre-existing, call it out clearly before checkpointing

### 5. Create a safe Git checkpoint

Use the bundled Git helper instead of ad-hoc `git add` / `git push` for routine vault checkpoints.

Use:

```bash
"$CODEX_HOME/skills/knowledge-vault-research-sync/scripts/safe_git_checkpoint.sh" \
  --repo "/Users/tony/Documents/vault/tony2026" \
  --message "Your checkpoint message"
```

Default behavior of the script:

- fetch `origin/<current-branch>` first
- stop if the branch is behind or diverged
- stage meaningful changes while excluding `.obsidian`
- skip commit if nothing non-ignored is staged
- commit and push safely when the branch is in a good state

Never force-push automatically from this skill. If remote history diverges, stop and report.

## Automation Mode

When this skill is used from an automation:

- do the content maintenance first
- run link validation for the touched areas
- run the safe checkpoint script
- if there are no meaningful changes, do not create an empty commit
- if push is blocked because the branch is behind or diverged, stop and report the reason
- always produce a short inbox summary of what changed, what was skipped, and whether GitHub sync succeeded

## Tony Vault Conventions

For the current vault at `/Users/tony/Documents/vault/tony2026`:

- treat `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Learning/09-Systems` as concrete systems/products/platforms
- treat `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Learning/06-Topics` as abstract concepts
- when new AI systems are added, consider whether company pages, system indexes, and positioning maps also need updates
- when new engineering abstractions are added, consider whether `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Engineering/07-Topics/主题索引.md`, `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Engineering/08-Maps/地图索引.md`, and area `专题总览.md` should be refreshed

## Resources

### scripts/

- `check_obsidian_wikilinks.py`: validate wiki-style links within one or more vault roots
- `safe_git_checkpoint.sh`: create a safe non-force Git checkpoint that excludes `.obsidian`

### references/

- `workflow.md`: compact checklist for content updates, progress tracking, and commit message style
- `autonomous-delivery-loop.md`: batch-oriented delivery loop for uninterrupted knowledge-vault work
