---
title: Claude Code 生态能力图
type: map
status: active
tags:
  - ai/map
  - ai/coding-agent
  - ai/claude-code
created: 2026-05-15
updated: 2026-05-15
---

# Claude Code 生态能力图

## 图谱

```mermaid
flowchart TB
  goal["成为 AI Coding 专家"]

  entry["入口层<br/>Terminal / IDE / GitHub"]
  memory["项目记忆层<br/>CLAUDE.md / Memory"]
  method["方法层<br/>Skills / Commands"]
  agents["专家分工层<br/>Subagents"]
  tools["外部能力层<br/>MCP / Tools"]
  automation["自动化层<br/>Hooks / CI / SDK"]
  governance["治理层<br/>Permissions / Audit / Release Gates"]

  outcome["团队级 AI Coding Workbench"]

  goal --> entry
  entry --> memory
  memory --> method
  method --> agents
  agents --> tools
  tools --> automation
  automation --> governance
  governance --> outcome

  method -.沉淀高频方法.-> memory
  automation -.生成复盘与规则.-> memory
  governance -.约束工具与权限.-> tools
  governance -.约束专家角色.-> agents

  classDef north fill:#e8f1ff,stroke:#3973d6,color:#111827
  classDef core fill:#edf7ed,stroke:#2f8f46,color:#111827
  classDef action fill:#fff4e5,stroke:#d97706,color:#111827
  classDef control fill:#f5e8ff,stroke:#7e22ce,color:#111827
  classDef result fill:#fee2e2,stroke:#dc2626,color:#111827

  class goal north
  class entry,memory core
  class method,agents,tools action
  class automation,governance control
  class outcome result
```

## 怎么读

- 从 `入口层` 到 `治理层` 是从个人使用到团队操作系统的升级路径
- `Skills / Commands` 解决“方法复用”
- `Subagents` 解决“专家分工”
- `MCP / Tools` 解决“外部上下文与动作”
- `Hooks / CI / SDK` 解决“自动化闭环”
- `Permissions / Audit / Release Gates` 解决“可控和可上线”

## 相关

- [[../09-Systems/Claude Code 生态全景|Claude Code 生态全景]]
- [[../09-Systems/Claude Code 能力安装清单|Claude Code 能力安装清单]]
- [[../09-Systems/Claude Code 自定义能力工作台：Skills、Plugins、Hooks、MCP|Claude Code 自定义能力工作台：Skills、Plugins、Hooks、MCP]]
- [[../../AI-Engineering/07-Topics/Claude Code Harness 工程实践|Claude Code Harness 工程实践]]

