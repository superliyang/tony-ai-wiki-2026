---
title: "Memory Changelog"
created: 2026-06-03
updated: 2026-06-14
status: active
tags:
  - agent-memory
  - changelog
---

# Memory Changelog

## 2026-06-14 (access-layer split)

- Recorded Tony's access-layer split: Obsidian is the personal knowledge production center; GitHub private repo is the long-term versioned fact source; `output-feishu/` is the publishable intermediate layer; Feishu knowledge base / docs provide anywhere access, mobile reading, sharing, and collaboration; Feishu CLI is the automated sync executor.
- Added [[00-Home/今日入口]] as the preferred Obsidian opening page to reduce navigation friction.
- Updated Feishu publishing language from `output-public/feishu` to `output-feishu/`.

## 2026-06-03 (Hermes write boundary)

- Added Hermes write boundary to shared memory: Hermes may write staging, reports, review items, candidates, and memory projections; Hermes must not write canonical knowledge layers or canonical `agent-memory/*.md` files by default.
- Updated `60-Agents/Hermes.md` to use the new vault layers: `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`, `60-Agents/`, and `90-Agent-System/`.

## 2026-06-03 (language preference)

- Added Tony's documentation language preference: vault documentation should be primarily Chinese, with important English technical terms preserved; simple short labels, command snippets, and tool-native names may remain in English.

## 2026-06-03 (clean slate)

- Cleaned all staging directories: review-queue (0 pending, 0 accepted), candidates (0), signals (0).
- Old vault tasks (Security Round 1-3, Codex audit, memory review) discarded — start fresh.
- Vault migration complete, all scripts and cron jobs updated to `tony-ai-wiki-2026`.

## 2026-06-03 (vault migration)

- Migrated canonical shared memory from `/Users/tony/Vault/tony-wiki-2026` to `/Users/tony/Vault/tony-ai-wiki-2026`.
- Updated vault root path references: `wiki/` → `10-Knowledge/`, `wiki/hot.md` → `00-Home/当前主线.md`.
- Created staging subdirectories under `00-Inbox-AI/`.
- Regenerated Hermes Soul.md projection from canonical memory.
- Old vault `/Users/tony/Vault/tony-wiki-2026` is now deprecated.

## 2026-06-03 (initial)

- Established `00-Inbox-AI/agent-memory/` as the canonical shared memory layer.
- Established Hermes `Soul.md` as a derived runtime projection, not a source of truth.
- Added memory sync workflow under `90-Agent-System/workflows/memory-sync.md`.
