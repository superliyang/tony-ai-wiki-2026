---
title: "Agent Skills 供应链控制清单"
created: 2026-06-21
updated: 2026-06-21
status: learning
as_of: 2026-06-21
tags:
  - knowledge
  - security
  - ai-security
  - agent-skills
  - supply-chain
  - controls
---

# Agent Skills 供应链控制清单

Agent skill 是可复用能力包，通常包含提示词、脚本、依赖、示例和权限假设。它的风险更像“代码供应链 + prompt 供应链”的混合体。

## 核心风险

| Risk | 表现 | 控制 |
|---|---|---|
| Malicious Skill | skill 内含危险脚本或诱导模型外发数据 | 来源审查、代码 review、权限隔离 |
| Prompt Injection in Skill | skill 指令覆盖系统边界 | skill instruction review、禁止越权指令 |
| Dependency Risk | skill 依赖包过期、恶意或不可复现 | lockfile、版本 pin、依赖扫描 |
| Over-Broad Permission | skill 默认要求 shell、网络、secret 访问 | 按能力拆分权限、默认最小权限 |
| Stale Skill | skill 过期但仍被自动化调用 | `as_of`、owner、review cadence |
| Hidden State | skill 写入缓存、memory 或外部系统 | 写入路径声明、日志声明 |

## Skill 接入清单

- skill 解决什么具体任务？
- 输入、输出、写入路径是什么？
- 是否需要联网？
- 是否执行脚本？
- 是否调用外部 API？
- 是否读取 secrets、tokens、浏览器状态、Obsidian runtime？
- 是否可以在无人工确认情况下改主库？

## Tony 系统规则

1. 个人 skill 可以先进入 `90-Agent-System/skills/` 或 working vault。
2. 进入自动化前必须经过一次人工 review。
3. 能写主库、发飞书、改 Git、调用外部 API 的 skill 都是高风险。
4. 高风险 skill 必须有 rollback 或 dry-run 模式。

## Sources

- OWASP Agentic Skills Top 10: https://owasp.org/www-project-agentic-skills-top-10/
- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

