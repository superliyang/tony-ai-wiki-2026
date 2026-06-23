---
title: "Hermes Codex Feishu Pipeline"
created: 2026-06-14
updated: 2026-06-16
status: active
tags:
  - workflow
  - hermes
  - codex
  - feishu
  - pipeline
---

# Hermes Codex Feishu Pipeline

这条 workflow 定义从 Hermes 生产信息，到 Codex 完善信息，再写入 Obsidian 知识库，最后输出到飞书的完整链路。

## Pipeline

```text
Hermes scout / recall / synthesis
  ↓
/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/20-Review-Queue/pending/
  ↓
Codex research / structure / crystallization
  ↓
working vault review queue or canonical vault
  ↓
10-Knowledge / 20-Maps / 30-Playbooks / 40-Projects
  ↓
output-feishu/
  ↓
飞书 CLI
  ↓
飞书知识库 / 云文档 / 云空间
```

## Roles

| Actor | Owns | Must Not Do |
|---|---|---|
| Hermes | discovery, recall, synthesis, Codex requests, reminders | write canonical knowledge directly |
| Codex | research, restructuring, crystallization, maps, Git checkpoint, Feishu preparation | silently promote unreviewed material |
| Tony | priority, approval, taste, final judgment | manually chase every raw signal |
| Feishu CLI | publishing executor | become source of truth |

## Can Hermes Drive Codex?

Yes, but in two levels.

### Level 1: Request-Driven

Hermes writes a Codex request:

```text
/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/20-Review-Queue/pending/YYYY-MM-DD-topic.md
```

Codex consumes it when Tony asks or during a Codex scheduled consumer run.

This is the default safe mode.

### Level 2: CLI-Triggered

Because both `hermes` and `codex` CLI exist on this machine, Hermes can theoretically trigger a Codex CLI run.

This should only happen through a narrow command wrapper that:

- reads one request file;
- limits output paths;
- blocks direct secret exposure;
- writes a run report;
- does not auto-publish to Feishu unless `publish_to_feishu: true` and the source is approved.

Until this wrapper is built and tested, Hermes should not directly launch arbitrary Codex prompts.

## Request Lifecycle

1. Hermes creates request in the working vault `20-Review-Queue/pending/`.
2. Codex processes one bounded request at a time.
3. Codex creates one or more outputs:
   - learning package;
   - review item;
   - canonical note / map / playbook / project update;
   - `output-feishu/` cleaned projection.
4. If Tony approval is needed, Codex writes or updates the working vault review queue.
5. If publishing is approved, Codex runs Feishu CLI and writes record under the working vault `40-Logs/` or `output-feishu/`.
6. Codex leaves output links or blocker reason in the review item.

## Promotion Rules

| Input Status | Codex May Write Canonical? | Notes |
|---|---|---|
| raw signal | No | create learning package / review item |
| Hermes synthesis | No by default | unless Tony explicitly delegates |
| accepted review item | Yes | update nearest maps |
| project companion request | Yes if Tony explicitly asked to run it | keep project pages current |
| Feishu publish request | Only `output-feishu/` first | Feishu is projection |

## Output Contract

Every completed request should leave:

- source request link;
- output links;
- whether review is required;
- whether Feishu publish happened;
- next action.

## Related

- [[90-Agent-System/integrations/Hermes-Codex]]
- [[90-Agent-System/workflows/hermes-codex-learning-chain]]
- [[90-Agent-System/workflows/feishu-publishing]]
- [[output-feishu/README]]
