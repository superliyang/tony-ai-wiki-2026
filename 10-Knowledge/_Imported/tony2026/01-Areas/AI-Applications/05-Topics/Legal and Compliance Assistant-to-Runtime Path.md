---
title: Legal and Compliance Assistant-to-Runtime Path
type: topic
status: learning
tags:
  - ai/applications
  - ai/legal
  - ai/high-trust
  - ai/migration
created: 2026-03-24
updated: 2026-03-24
---

# Legal and Compliance Assistant-to-Runtime Path

## 推荐路径

1. 从 document-heavy assist 开始，如 clause summary、source-backed comparison、research assist
2. 再进入 workflow assistant，如 review packet、issue list、compliance memo、obligation extraction
3. 之后才进入 approval-gated action，例如 case routing、ticket creation、workflow handoff
4. 最后才是私有 runtime 和更深的 system orchestration

## 为什么法律与合规的迁移节奏特殊

- 这个领域最看重的往往不是自治，而是 citation discipline、source grounding 和 review handoff
- 只要引用链不稳，再强的动作能力都不会被信任
- 所以这条路径通常会在 workflow-assistant 阶段停留很久

## 常见的迁移门槛

- 文档来源受控且能被引用
- reviewer 愿意在 agent 生成的 packet 上工作
- action layer 被限制在 routing、tracking、handoff，而不是高风险判断自动化
- 组织愿意投入到私有 workflow 设计和审计能力建设中

## 产品角色

- `ChatGPT Agent`：适合文档密集型的 assist 和 review prep
- `OpenClaw`：适合进入更私有的 legal/compliance runtime 场景
- `Claude Code / Cursor / Codex`：适合内部 legal tooling 和 compliance workflow system 的构建层

## 相关

- [[Migration-Stage Vendor Selection in High-Trust Domains]]
- [[Legal and Compliance Agent Vendor Choice]]
- [[../03-Workflows/Legal and Compliance Agent Workflow|Legal and Compliance Agent Workflow]]
- [[../04-Case-Studies/Harvey Legal Work Platform|Harvey Legal Work Platform]]
- [[Assistant-to-Runtime Migration in High-Trust Domains]]
