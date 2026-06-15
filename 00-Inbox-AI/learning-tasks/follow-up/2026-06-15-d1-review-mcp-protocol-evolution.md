---
title: "Day-1 复习：MCP 协议演进 — Streamable HTTP 与无状态化"
review_date: 2026-06-15
review_stage: "day-1"
source_package: "00-Inbox-AI/learning-tasks/accepted/2026-06-05-mcp-protocol-evolution-package.md"
accepted_date: 2026-06-14
created: 2026-06-14
type: follow-up-review
---

# D+1 复习：MCP 协议深度研究 — Streamable HTTP 与无状态化演进

## 为什么现在应该复习

MCP 正从本地工具协议走向生产基础设施。码农出身的你应该关注的是：新旧 transport 差异、为什么 stateless 是正确方向、header 标准化带来了什么安全风险、以及 Hermes 当前 MCP 依赖会不会被 breaking change 影响。首次复习检验你到底能不能说清楚 Streamable HTTP 替代 HTTP+SSE 的动机。

## 3 个复习问题

1. **Streamable HTTP 替代 HTTP+SSE 解决了哪 3 个核心问题？** (提示：负载均衡、故障恢复、版本协商)
2. **`Mcp-Method` / `Mcp-Name` 映射到 HTTP headers 的好处和风险分别是什么？**
3. **2026-07-28-RC 是 final spec 吗？Hermes 现在应该切换吗？为什么？**

## Obsidian 动作

在 `00-Inbox-AI/` 里新建 `MCP D+1 自测.md`，列出 Hermes 当前正在使用的所有 MCP servers（如 exa、camofox 等），并标注每个 server 是否依赖 session affinity，换 Streamable HTTP 后是否会受影响。

## 建议 Codex 更新

- 暂不建议生成任何 canonical/playbook — 等 2026-07-28 final spec 后再评估
- 建议 Codex 留意 Hermes MCP 配置中是否有 token/API key 被打进 header 的风险
