---
title: "AI Coding Agent 安全控制清单"
created: 2026-06-21
updated: 2026-06-21
status: learning
as_of: 2026-06-21
tags:
  - knowledge
  - security
  - ai-security
  - coding-agent
  - controls
---

# AI Coding Agent 安全控制清单

Coding agent 的风险来自“能读 repo、改代码、跑命令、写文件、可能发 PR”。它的控制重点不是禁止能力，而是让能力可审计、可回滚、可限制。

## 控制面

| Control | 要求 |
|---|---|
| Workspace Boundary | agent 只能在指定 workspace / worktree 操作 |
| Git Safety | 不允许自动 `reset --hard`、force push、删除未知改动 |
| Secret Protection | 禁止读取 `.env`、钥匙串、token 文件；diff 前做 secret scan |
| Command Approval | 高风险命令、网络写入、部署、删除需要 approval |
| Test Gate | 改代码后必须跑相关测试或解释无法测试 |
| Diff Review | 修改进入 commit/PR 前必须展示 diff summary |
| Rollback | 保留 Git checkpoint 或 worktree isolation |
| External Write | 发 PR、发飞书、改 issue、调用 SaaS API 前单独确认 |

## 适合 Tony 的默认策略

| 场景 | 默认 |
|---|---|
| 本地知识库维护 | 允许读写主库，但要保留 diff 和报告 |
| 代码项目修改 | 使用 Git branch / worktree，按测试风险决定验证深度 |
| 自动化任务 | 默认不允许删除、不允许发布、不允许外发敏感内容 |
| Hermes -> Codex handoff | Hermes 提需求，Codex 执行 bounded task，结果进入 review |

## Sources

- OpenAI GPT-5.5 agentic coding release context: https://openai.com/index/introducing-gpt-5-5/
- Anthropic Claude Opus 4.8 dynamic workflows context: https://www.anthropic.com/news/claude-opus-4-8
- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
