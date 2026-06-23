---
title: "MCP Server 安全控制清单"
created: 2026-06-21
updated: 2026-06-21
status: learning
as_of: 2026-06-21
tags:
  - knowledge
  - security
  - ai-security
  - mcp
  - controls
---

# MCP Server 安全控制清单

MCP server 是 agent 连接工具、数据和系统的边界。它不是普通 API wrapper，而是会进入模型上下文、影响工具选择和权限判断的执行面。

## 风险分层

| Layer | Risk | Control |
|---|---|---|
| Server Trust | 接入未知或被篡改 MCP server | allowlist、签名/来源记录、版本锁定 |
| Tool Definition | 工具描述诱导模型误用 | 工具 schema review、描述最小化、危险动词标记 |
| Context Injection | server 返回内容污染 agent prompt / memory | output sanitization、untrusted context 标记 |
| Authorization | 工具实际权限超过任务需要 | per-tool / per-scope token、最小权限凭证 |
| Data Exfiltration | server 可读敏感文件或外发数据 | path allowlist、egress control、secret scanner |
| Stateful Memory | server 持久化不该保留的上下文 | memory retention policy、清理机制 |
| Audit | 无法追踪 agent 为什么调用工具 | tool call trace、request/response log、approval record |

## 接入前检查

- 这个 MCP server 来自哪里？
- 它暴露哪些工具？
- 每个工具是否有最小参数 schema？
- 它能读写哪些路径、API、数据库或 SaaS？
- 是否需要联网？
- 是否会保存 memory、cache 或日志？
- 是否有测试用例和回滚方式？

## 运行时控制

| 场景 | 控制 |
|---|---|
| 读文件 | 限制目录；默认禁止读取 secrets、runtime state、系统钥匙串 |
| 写文件 | 只允许 workspace；重要文件需要 diff review |
| 执行命令 | shell 命令必须有 allowlist / approval |
| 调 SaaS API | 使用低权限 token；按 workspace / project 分 scope |
| 外发内容 | 默认不允许发送敏感信息；需要脱敏和记录 |

## 进入 Tony 系统的要求

1. MCP server 必须登记到 [[90-Agent-System/integrations/Hermes-Codex]] 或相关 integration note。
2. 高风险 MCP server 必须有 review gate。
3. 自动化任务不得默认启用新 MCP server。
4. 出现异常工具调用时，先暂停自动化，再复盘 trace。

## Sources

- OWASP MCP Top 10: https://owasp.org/www-project-mcp-top-10/
- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

