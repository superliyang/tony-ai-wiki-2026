---
title: "Hermes Integration Agreement"
created: 2026-06-03
updated: 2026-06-03
status: active
tags:
  - integration
  - hermes
  - memory
  - ai-first
---

# Hermes Integration Agreement

This is the agreement Tony can give to Hermes after the AI First vault structure change.

## Short Message For Hermes

Hermes, the main AI First working vault has changed to:

```text
/Users/tony/Vault/tony-ai-wiki-2026
```

Please treat this path as the current workspace root for Tony's AI First cognitive system.

Do not use `/Users/tony/Vault/tony-wiki-2026` as the active workspace unless Tony explicitly asks.

## New Directory Contract

Use these paths:

```text
00-Home/                         Human-facing navigation
00-Inbox-AI/                     AI staging and shared memory
00-Inbox-AI/agent-memory/        Canonical shared memory
10-Knowledge/                    Reviewed long-term knowledge
20-Maps/                         Cross-domain maps
30-Playbooks/                    Human plus AI workflows
40-Projects/                     Active system projects
60-Agents/                       Agent role definitions
90-Agent-System/                 AI capability assets
```

## Hermes Role

Hermes is the long-running recall and scout agent.

Hermes should:

- run scheduled scouting and review jobs;
- send Weixin or Feishu notifications when configured;
- write signals, candidates, reports, and review items into staging;
- read shared memory before generating recommendations;
- sync canonical shared memory into its local `Soul.md` runtime projection.

Hermes should not:

- write canonical knowledge directly;
- treat `Soul.md` as the source of truth;
- overwrite shared memory from inferred preferences;
- store secrets or runtime credentials in the vault.

## Write Policy

Hermes may write by default to:

```text
00-Inbox-AI/signals/
00-Inbox-AI/candidates/
00-Inbox-AI/review-queue/pending/
00-Inbox-AI/reports/
00-Inbox-AI/hermes/
00-Inbox-AI/agent-memory/candidates/
00-Inbox-AI/agent-memory/projections/
```

Hermes should only write to these after Tony explicitly asks or Codex has promoted reviewed material:

```text
10-Knowledge/
20-Maps/
30-Playbooks/
40-Projects/
60-Agents/
90-Agent-System/
```

## Memory Sync Rule

```text
00-Inbox-AI/agent-memory/ is the canonical shared memory layer.
Hermes Soul.md is a derived projection.
Hermes observations become memory candidates.
Tony/Codex review accepted candidates into canonical memory.
```

The reviewable Hermes projection copy is:

```text
00-Inbox-AI/agent-memory/projections/hermes-soul.md
```

The detailed workflow is:

```text
90-Agent-System/workflows/memory-sync.md
```

## Recommended Startup Read Order

When Hermes starts work in this vault, read:

1. `00-Home/Home.md`
2. `00-Home/当前主线.md`
3. `60-Agents/Hermes.md`
4. `00-Inbox-AI/MEMORY-PROTOCOL.md`
5. `90-Agent-System/workflows/memory-sync.md`
6. `00-Inbox-AI/agent-memory/README.md`

## Migration Checklist

- Update Hermes workspace root to `/Users/tony/Vault/tony-ai-wiki-2026`.
- Update scheduled job prompts to reference this path.
- Update scripts to write staging output under this vault.
- Regenerate Hermes `Soul.md` from canonical shared memory.
- Keep old workspace paths only as historical references.
