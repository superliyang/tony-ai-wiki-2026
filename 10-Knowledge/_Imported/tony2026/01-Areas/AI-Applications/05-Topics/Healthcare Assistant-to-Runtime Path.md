---
title: Healthcare Assistant-to-Runtime Path
type: topic
status: learning
tags:
  - ai/applications
  - ai/healthcare
  - ai/high-trust
  - ai/migration
created: 2026-03-24
updated: 2026-03-24
---

# Healthcare Assistant-to-Runtime Path

## 推荐路径

1. 先从 documentation relief、claims support、internal knowledge assist 开始
2. 再进入 bounded workflow，例如 administrative triage、appeal draft、review packet
3. 然后才考虑 approval-gated actions，如 case routing 或低风险系统写入
4. 只有在隐私、审计和异常恢复都成熟时，才考虑更完整的 runtime

## 为什么医疗要更保守

- 医疗场景对隐私、误导和副作用的容忍度更低
- 很多任务表面看像文本处理，实际上会影响 patient outcome 或 payer outcome
- 所以更重要的是 bounded workflow，而不是过度自治

## 常见的迁移门槛

- 文档、claims、运营知识的 source-of-truth 已经稳定
- 输出有明确 reviewer，且能保留 evidence trail
- 对 PHI、访问控制和部署边界有成熟规范
- failure path 和 human override 已经设计好

## 产品角色

- `ChatGPT Agent`：适合 operator-facing assist 和 bounded admin workflow
- `OpenClaw`：适合更私有、更受控的内部 runtime 探索
- `Claude Code / Cursor / Codex`：适合构建医疗组织内部的 workflow tooling，而不是直接作为终端业务 surface

## 相关

- [[Migration-Stage Vendor Selection in High-Trust Domains]]
- [[Healthcare Agent Vendor Choice]]
- [[../03-Workflows/Healthcare Agent Workflow|Healthcare Agent Workflow]]
- [[../04-Case-Studies/Oscar Healthcare Operations Assistant|Oscar Healthcare Operations Assistant]]
- [[Assistant-to-Runtime Migration in High-Trust Domains]]
