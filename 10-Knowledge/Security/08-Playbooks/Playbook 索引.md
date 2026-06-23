---
title: "Security Playbook 索引"
created: 2026-06-18
updated: 2026-06-21
status: learning
tags:
  - knowledge
  - security
  - playbooks
---

# Playbook 索引

## Recommended Start

- [[10-Knowledge/Security/08-Playbooks/Playbook 索引 - 旧库]]
- [[10-Knowledge/Security/08-Playbooks/安全快速诊断 Playbook]]
- [[10-Knowledge/Security/08-Playbooks/应用与 API 安全评审 Playbook]]
- [[10-Knowledge/Security/08-Playbooks/供应链安全评审 Playbook]]
- [[10-Knowledge/Security/08-Playbooks/安全事件响应 Playbook]]
- [[10-Knowledge/Security/08-Playbooks/零信任落地 Playbook]]

## AI / Agent Security Playbooks

| 场景 | 先看 | 输出 |
|---|---|---|
| 一个 AI 产品要上线 | [[10-Knowledge/Security/03-Industry-Controls/AI 产品安全控制清单]] | 产品级安全控制差距 |
| 一个 MCP server 要接入 | [[10-Knowledge/Security/03-Industry-Controls/MCP Server 安全控制清单]] | tool permission / data access / audit checklist |
| 一个 Codex / Claude Code / Cursor 类 coding agent 要进项目 | [[10-Knowledge/Security/03-Industry-Controls/AI Coding Agent 安全控制清单]] | repo access、approval、test gate、secret boundary |
| 一个 Agent skill / plugin 要安装 | [[10-Knowledge/Security/03-Industry-Controls/Agent Skills 供应链控制清单]] | skill provenance、review、rollback、least privilege |
| AI 安全评估要系统化 | [[10-Knowledge/AI-Engineering/07-Topics/AI Security Evaluation 与 Red Teaming]] | eval cases、red-team prompts、release gate |

## Current Operating Rhythm

1. **评审前**：先用行业控制清单确定边界，不直接看工具宣传。
2. **上线前**：把控制项接到 release gate，不只写文档。
3. **运行中**：把 telemetry、告警、人工确认和事件复盘串起来。
4. **事故后**：把失败样本回灌到 eval harness 和案例复盘。

## Source Watch

- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- [OWASP Agentic Skills Top 10](https://owasp.org/www-project-agentic-skills-top-10/)
- [CISA BOD 26-04](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk)
