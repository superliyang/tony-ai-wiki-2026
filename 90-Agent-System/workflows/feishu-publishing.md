---
title: "Feishu Publishing Workflow"
created: 2026-06-14
updated: 2026-06-14
status: active
tags:
  - agent-system
  - workflow
  - feishu
  - publishing
---

# Feishu Publishing Workflow

这个 workflow 定义如何把 vault 中已经 review 或明确可分享的内容清洗成 `output-feishu/`，再发布到飞书，作为 Tony 在公司电脑或移动端查看的在线回顾版。

## Principle

```text
Obsidian = 个人知识生产中心
GitHub private repo = 长期版本事实源
output-feishu = 可发布中间层
飞书知识库 = 任意地方访问 / 移动端阅读 / 分享协作
飞书 CLI = 自动同步执行器
```

飞书文档不是第二主库。飞书只承载方便在线阅读、手机回顾、临时分享的 projection。

## Publishable Content

适合发布：

- 项目阶段总结；
- 专题总览；
- 学习路径；
- playbook；
- review gate 决策面板；
- 周报 / 月报 / 复盘；
- 可对外分享的文章草稿。

不适合发布：

- `00-Inbox-AI/` 中未 review 的原始草稿；
- memory candidates；
- 账号、路径、token、OAuth、secret、cookie；
- 未校验的 benchmark、比例和行业数字；
- 含私人判断但没有明确发布意图的笔记。

## Pipeline

```text
Obsidian Vault
  ↓
导出 / 清洗 / 过滤
  ↓
output-feishu/
  ↓
飞书 CLI 上传
  ↓
飞书知识库 / 云文档 / 云空间
```

## Directory Contract

| Stage | Path | Meaning |
|---|---|---|
| Source vault | `00-Home/`, `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`, `90-Agent-System/` | Obsidian 本地学习、查看、回顾主库 |
| Feishu output | `output-feishu/` | 清洗、过滤后的飞书可发布 Markdown / assets |
| Publishing records | `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/40-Logs/feishu-publishing/` | 飞书 URL、doc token、来源和发布状态 |
| Pending / failed ops | `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/20-Review-Queue/pending/` | 发布操作队列和失败记录 |
| Workflow | `90-Agent-System/workflows/feishu-publishing.md` | 发布边界和操作流程 |

## Workflow

1. Choose a reviewed or explicitly approved source note.
2. Create a publish-ready Markdown under `output-feishu/`.
3. Strip or summarize sensitive local-only details.
4. Convert Obsidian wikilinks into readable text or keep as source-path references.
5. Delegate publishing execution to Hermes when the content is clean and approved.
6. Hermes publishes with `lark-cli docs +create --api-version v2 --doc-format markdown`.
7. Hermes writes a record under the working vault `40-Logs/feishu-publishing/`.
8. Codex adds the Feishu URL back to the source note only when the source note is stable and the URL should be durable.

## Hermes Delegation Rule

Hermes may call Feishu CLI only for:

- reviewed source notes;
- Codex-prepared `output-feishu/` Markdown;
- explicit Tony publish requests.

Hermes must not publish raw staging, private inbox material, unfinished review candidates, or content containing secrets.

## Metadata Shape

Published records should include:

```yaml
source_note:
feishu_doc_url:
feishu_doc_id:
published_at:
published_by: codex-via-lark-cli
sync_mode: one-way
status: published
```

## Guardrails

- Default to one-way publishing from vault to Feishu.
- Do not treat Feishu edits as canonical unless Tony explicitly asks to import them.
- Do not publish raw inbox material unless Tony explicitly approves that exact item.
- Do not publish directly from canonical notes when a cleaned `output-feishu/` version is needed.
- Do not publish secrets, credentials, local auth state, cookies, or private account files.
- For documents with uncertain factual claims, label them as `待校验` or publish only the decision summary.
