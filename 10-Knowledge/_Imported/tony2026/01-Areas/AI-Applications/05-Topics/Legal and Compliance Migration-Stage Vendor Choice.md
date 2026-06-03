---
title: Legal and Compliance Migration-Stage Vendor Choice
type: topic
status: learning
tags:
  - ai/applications
  - ai/legal
  - ai/high-trust
  - ai/vendor-selection
  - ai/migration
created: 2026-03-24
updated: 2026-03-24
---

# Legal and Compliance Migration-Stage Vendor Choice

## 一句话结论

法律与合规场景通常会在 `document-heavy assist -> workflow assistant` 两个阶段停留很久，因为 citation、source grounding 和 review handoff 通常比自治更重要。

## 阶段 1：Read-only assistant

- 更适合：`ChatGPT Agent`
- 原因：最早的价值来自 clause summary、research assist、document comparison
- 代表案例：[[../04-Case-Studies/Harvey Legal Work Platform|Harvey Legal Work Platform]]

## 阶段 2：Workflow assistant

- 更适合：`ChatGPT Agent` 或私有 workflow prototype
- 原因：review packet、issue list、obligation extraction 和 compliance memo 是天然的 workflow-assistant 任务
- 判断重点：citation discipline 和 reviewer trust 是否已经稳定

## 阶段 3：Approval-gated action

- 更适合：routing、handoff、tracking 级别的受控 action
- 原因：大部分法律/合规团队不会先追求高自治动作
- 判断重点：哪些 action 真的是流程动作，哪些 still require expert judgment

## 阶段 4：Runtime with control plane

- 更适合：私有 workflow system 和 internal runtime
- 原因：如果走到这一步，组织通常已经在自己构建更深的 compliance tooling
- `Claude Code / Cursor / Codex` 在这里更像 build layer

## 相关

- [[Legal and Compliance Agent Vendor Choice]]
- [[Legal and Compliance Assistant-to-Runtime Path]]
- [[Migration-Stage Vendor Selection in High-Trust Domains]]
- [[../04-Case-Studies/Harvey Legal Work Platform|Harvey Legal Work Platform]]
