# 学习任务: WebMCP — W3C Agent-Web 交互标准

- **创建时间**: 2026-06-06 15:00
- **来源**: 下午增量扫描 → MCP 协议进化主线
- **优先级**: P2
- **状态**: pending
- **关联主线**: MCP 协议进化 ([[00-Inbox-AI/learning-tasks/pending/2026-06-04-mcp-protocol-evolution]])

## 为什么值得研究

WebMCP 是 W3C Web Machine Learning Community Group 于 2026-06-05 发布的首个 Draft 规范。它定义了 JavaScript API 让网页应用将自身功能暴露为 Agent 工具——本质上每个网页都可以成为 MCP Server。这与 MCP 2026-07-28 Release Candidate 形成「后端标准化(MCP RC) + 前端标准化(WebMCP)」的双轮驱动。

**关键问题**:
1. WebMCP 与传统 MCP Server 的关系是什么？互补还是替代？
2. 如果网页原生支持 Agent 工具调用，浏览器的角色会从「渲染引擎」变成「Agent 运行环境」吗？
3. 安全模型：网页暴露工具给 Agent 意味着新的攻击面——权限边界在哪？
4. 与 Google/Apple 的 Agent 浏览器策略如何互动？

## 建议研究路径

1. 精读 WebMCP Draft 规范 (https://webmachinelearning.github.io/webmcp/)
2. 对比 MCP 2026-07-28 RC 的 Task/MCP Apps 扩展，看 WebMCP 的定位差异
3. 回顾 Chrome DevTools Protocol / Playwright 等现有 Agent-Web 交互方式
4. 产出：WebMCP vs MCP 定位对比 + Agent-Web 交互范式演进时间线

## 关联信号

- MCP 2026-07-28 RC (2026-05-21)
- MCP Streamable HTTP v2.1 (2026-06-04)
- OpenAI Lockdown Mode 禁用网页浏览 (2026-06-06)
