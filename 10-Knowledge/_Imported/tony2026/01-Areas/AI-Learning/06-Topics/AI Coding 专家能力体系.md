---
title: AI Coding 专家能力体系
type: topic
status: active
tags:
  - ai/topic
  - ai/coding-agent
  - ai/workbench
created: 2026-05-16
updated: 2026-05-16
---

# AI Coding 专家能力体系

## 一句话定位

`AI Coding 专家` 不是“很会让模型写代码的人”，而是能把 coding agent 放进真实软件工程体系，并让它可控、可验证、可复用、可治理、可规模化的人。

这类能力的核心不是 prompt，而是：

> 任务建模 + 上下文工程 + 工具面设计 + 扩展面沉淀 + 验证治理 + 团队落地。

## 六层能力

### 1. 任务建模

把模糊需求转成 agent 可执行任务：

- 目标：解决什么问题
- 范围：哪些文件、模块、接口可以动
- 约束：哪些行为、兼容性、性能、安全不能破
- 验证：用什么测试、日志、截图、CI、review 证明完成
- 交付：补丁、PR、文档、复盘、后续任务

### 2. 上下文工程

控制 agent 看到什么、忽略什么、保留什么：

- repo map
- task brief
- selected files
- issue / PR / CI / log
- `CLAUDE.md` / `AGENTS.md`
- session summary
- progress / resume notes

### 3. 工具面设计

知道给 agent 哪些动作能力：

- file edit
- shell / Git
- test / lint / build
- browser / UI
- MCP / external tools
- logs / observability
- read-only database / docs

专家判断不是“能接就接”，而是“接入后能否最小权限、可审计、可回滚”。

### 4. 扩展面沉淀

把一次成功经验沉淀成可复用能力：

- `skill`：沉淀专业方法
- `slash command`：沉淀固定入口
- `subagent`：沉淀专家角色
- `hook`：沉淀安全、质量、审计自动化
- `MCP`：沉淀外部工具和资料接入
- `plugin`：沉淀团队共享能力包

### 5. 验证治理

让 agent 的输出可以进入真实工程流：

- unit / integration / e2e
- typecheck / lint / build
- PR review
- security review
- release gate
- audit log
- rollback plan
- incident review

### 6. 团队落地

从个人提效升级到组织能力：

- 项目级规则
- 团队共享 skills / plugins
- 统一权限策略
- 统一评测任务包
- PR / CI 工作流接入
- 失败案例库
- 成本、质量、效率指标

## 三张关键图

- [[../07-Maps/AI Coding 专家能力图谱|AI Coding 专家能力图谱]]：回答“个人如何成为 AI Coding 专家”
- [[../../AI-Engineering/08-Maps/AI Coding 团队落地路线图|AI Coding 团队落地路线图]]：回答“团队如何从个人试用走向工程机制”
- [[../../AI-Engineering/08-Maps/AI Coding 安全治理决策图|AI Coding 安全治理决策图]]：回答“哪些权限、工具和自动化应该怎样治理”
- [[../../AI-Engineering/06-Projects/AI Coding Lab/项目总览|AI Coding Lab]]：回答“怎么把这套能力练出来，并用任务记录和验收矩阵证明”

## 推荐练习路径

1. 用一个真实 bug 做 `task brief -> repo map -> plan -> patch -> test -> review`
2. 把重复流程抽成一个 `skill`
3. 把审查角色抽成一个 `subagent`
4. 加一个最小 `hook` 做测试或危险命令提醒
5. 接一个只读 `MCP`，例如 GitHub issue、文档或 CI log
6. 把这套能力打包成项目级或团队级 plugin
7. 用 `Coding Agent Eval Pack` 评估是否真的提升质量和效率
8. 用 [[../../AI-Engineering/06-Projects/AI Coding Lab/AI Coding Lab 30 天训练路线|AI Coding Lab 30 天训练路线]] 跑一个完整月度练习

## 相关

- [[Coding Agents]]
- [[../09-Systems/Claude Code|Claude Code]]
- [[../09-Systems/Claude Code 生态全景|Claude Code 生态全景]]
- [[../09-Systems/Claude Code 能力安装清单|Claude Code 能力安装清单]]
- [[../09-Systems/Claude Code 自定义能力工作台：Skills、Plugins、Hooks、MCP|Claude Code 自定义能力工作台]]
- [[../../AI-Engineering/07-Topics/Claude Code Harness 工程实践|Claude Code Harness 工程实践]]
- [[../../AI-Engineering/04-Evaluation/Coding Agent Eval Pack：Repo 修复、测试与小型重构|Coding Agent Eval Pack]]
- [[../../AI-Engineering/04-Evaluation/AI Coding 专家能力验收矩阵|AI Coding 专家能力验收矩阵]]
- [[../../AI-Engineering/06-Projects/AI Coding Lab/项目总览|AI Coding Lab]]
