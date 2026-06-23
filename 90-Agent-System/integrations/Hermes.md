---
title: "Hermes Integration Agreement"
created: 2026-06-03
updated: 2026-06-16
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

Hermes, your active working vault has changed to:

```text
/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault
```

Please treat this path as your current workspace root for Tony's AI working system.

Do not write directly to the main knowledge vault unless Tony or Codex explicitly asks.

The main knowledge vault is now:

```text
/Users/tony/Vault/tony-wiki-space/tony-ai-wiki-2026
```

## New Directory Contract

Use these working-vault paths:

```text
00-Hermes-Inbox/                 Raw signals, source snapshots, temporary inputs
10-Generated/                    Drafts, digests, research candidates, learning tasks
20-Review-Queue/                 Review packages for Tony / Codex
30-Memory/                       Hermes working memory and boundaries
40-Logs/                         Automation logs and run records
90-System/                       Working-vault rules, workflows, templates
```

## Hermes Role

Hermes is the long-running recall and scout agent.

Hermes should:

- run scheduled scouting and review jobs;
- send Weixin or Feishu notifications when configured;
- write signals, candidates, reports, and review items into the working vault;
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
/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/00-Hermes-Inbox/
/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/10-Generated/
/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/20-Review-Queue/
/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/30-Memory/
/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/40-Logs/
```

Hermes should only write to these after Tony explicitly asks or Codex has promoted reviewed material:

```text
/Users/tony/Vault/tony-wiki-space/tony-ai-wiki-2026/10-Knowledge/
/Users/tony/Vault/tony-wiki-space/tony-ai-wiki-2026/20-Maps/
/Users/tony/Vault/tony-wiki-space/tony-ai-wiki-2026/30-Playbooks/
/Users/tony/Vault/tony-wiki-space/tony-ai-wiki-2026/40-Projects/
/Users/tony/Vault/tony-wiki-space/tony-ai-wiki-2026/60-Agents/
/Users/tony/Vault/tony-wiki-space/tony-ai-wiki-2026/90-Agent-System/
```

## Memory Sync Rule

```text
tony-ai-working-vault/30-Memory/ is Hermes' working memory layer.
Hermes Soul.md is a derived projection.
Hermes observations become memory candidates.
Tony/Codex review accepted candidates into canonical memory.
```

The reviewable Hermes projection copy is:

```text
30-Memory/hermes-soul.md
```

The detailed workflow is:

```text
90-System/workflows/hermes-to-main-vault-promotion.md
```

## Recommended Startup Read Order

When Hermes starts work in this vault, read:

1. `AGENTS.md`
2. `README.md`
3. `30-Memory/Hermes-Boundary-Contract.md`
4. `30-Memory/Hermes-Working-Memory.md`
5. `90-System/workflows/hermes-to-main-vault-promotion.md`

## Migration Checklist

- Update Hermes workspace root to `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault`.
- Update scheduled job prompts to reference this path.
- Update scripts to write staging output under the working vault.
- Regenerate Hermes `Soul.md` from canonical shared memory.
- Keep old workspace paths only as historical references.
