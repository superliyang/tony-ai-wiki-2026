---
title: "Feishu Integration"
created: 2026-06-14
updated: 2026-06-16
status: active
tags:
  - integration
  - feishu
  - publishing
---

# Feishu Integration

Feishu is Tony's online reading and temporary review surface for selected `output-feishu/` projections generated from the vault.

## Role

```text
Obsidian = 个人知识生产中心
GitHub private repo = 长期版本事实源
output-feishu = 可发布中间层
飞书知识库 = 任意地方访问 / 移动端阅读 / 分享协作
飞书 CLI = 自动同步执行器
```

Use Feishu for:

- mobile review;
- online reading;
- temporary sharing;
- weekly/monthly reports;
- project summaries;
- decision panels.

Do not use Feishu as:

- canonical memory;
- primary knowledge store;
- unreviewed AI inbox;
- secret/config storage.

## Tooling

Primary tool:

```text
lark-cli
```

Default create command:

```bash
lark-cli docs +create --api-version v2 --as user --doc-format markdown --parent-position my_library --content @output-feishu/path/to/publish-ready.md
```

For CLI operations, follow embedded `lark-cli` skills:

```bash
lark-cli skills read lark-doc
```

## Publishing Workflow

- [[90-Agent-System/workflows/feishu-publishing]]
- [[output-feishu/README]]

Publishing records after 2026-06-16 should live in the working vault:

`/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/40-Logs/feishu-publishing/`
