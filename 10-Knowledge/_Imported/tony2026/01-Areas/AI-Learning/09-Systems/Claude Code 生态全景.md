---
title: Claude Code 生态全景
type: system
status: active
tags:
  - ai/system
  - ai/coding-agent
  - ai/harness
  - ai/claude-code
created: 2026-05-15
updated: 2026-05-15
organization: "[[Anthropic]]"
related_systems:
  - "[[Claude Code]]"
  - "[[Codex]]"
  - "[[Cursor]]"
  - "[[Devin]]"
---

# Claude Code 生态全景

## 一句话定位

`Claude Code` 不是“命令行里的聊天机器人”，而是一个 `terminal-first AI coding harness`：它把模型能力、代码库上下文、命令执行、记忆、技能、插件、子代理、MCP、hooks、CI 和权限治理组合成一个可持续工作的开发者操作系统。

如果要成为 `AI Coding` 领域专家，不是背 Claude Code 命令，而是理解它背后的工程范式：

> 把软件开发任务拆成可表达、可执行、可验证、可复盘、可沉淀的 agent workflow。

## 生态分层

### 1. 入口层：Terminal / IDE / GitHub

- `terminal` 是最核心入口：适合 repo-local 修改、测试、提交、脚本化和长任务推进
- `IDE` 集成适合局部代码理解、编辑上下文和开发者手感
- `GitHub Actions / PR` 入口适合 review follow-up、issue 修复、CI 失败处理和自动化维护

判断标准：入口不是越多越好，而是每个入口是否有清晰的任务边界、权限边界和验证闭环。

### 2. 项目记忆层：`CLAUDE.md` / Memory

`CLAUDE.md` 是 Claude Code 最应该先用好的能力。它不是普通笔记，而是项目级工作契约：

- 项目结构、核心模块、启动方式
- 编码规范、测试命令、提交规范
- 业务词汇、架构边界、禁改区域
- 常见任务路径、排障流程、检查清单

专家级使用不是把 `CLAUDE.md` 写成长文档，而是把它写成“agent 进入项目后最少必须知道的操作规则”。

### 3. 方法层：Skills / Slash Commands

`Skills` 适合沉淀可复用任务方法：代码审查、重构套路、测试生成、迁移计划、安全排查、性能优化、知识库维护等。

`Slash commands` 更像轻量入口：适合触发某个固定流程、模板或命令式动作。

二者关系可以这样理解：

- `slash command`：我要 agent 现在做什么
- `skill`：这类任务应该按什么专业方法做

### 4. 专家分工层：Subagents

`Subagents` 适合把重复出现的专家角色固定下来：

- `code-reviewer`：审查缺陷、风险、可维护性
- `test-engineer`：补测试、定位 flaky、设计回归用例
- `security-reviewer`：审查注入、权限、依赖、secret、数据泄露
- `architect`：做模块边界、演进路径、技术债取舍
- `docs-maintainer`：维护文档、索引、变更记录

关键不是“多建几个角色”，而是给每个 subagent 明确：目标、输入、输出、工具权限、不可做事项。

### 5. 外部能力层：MCP

`MCP` 是 Claude Code 接外部系统的标准接口。它适合把 agent 从“只能看本地 repo”扩展到：

- GitHub / GitLab / issue tracker
- 内部知识库、文档、设计稿
- 数据库、日志、监控、CI
- 浏览器、测试平台、安全扫描

专家级原则：能只读就只读；能按项目隔离就不要全局授权；能通过审计日志追踪就不要黑盒调用。

### 6. 自动化层：Hooks / CI / SDK

`Hooks` 把 agent workflow 变成事件驱动系统：

- 在改文件前检查权限或路径
- 在改文件后自动跑格式化、lint 或局部测试
- 在停止前生成总结、待办和变更摘要
- 在危险命令前强制人工确认

`GitHub Actions / SDK` 则适合把 Claude Code 嵌入 PR、issue、CI 和后台任务。

### 7. 治理层：Settings / Permissions / Audit

真正的 AI Coding 专家一定要重视治理：

- 哪些工具可以自动执行
- 哪些路径禁止修改
- 哪些命令必须人工审批
- 如何记录 agent 做过什么
- 如何回滚、复盘和沉淀失败案例

没有治理的 agent 自动化，只是“跑得很快的不确定性”。

## 怎么才算用好 Claude Code

### 初级：会让它帮忙写代码

- 能解释代码、生成片段、修 bug
- 能给出清晰 prompt
- 能人工检查输出

### 中级：会把它放进真实工程流

- 能让它读 repo、定位问题、拆任务、改文件、跑测试
- 会维护 `CLAUDE.md`
- 会约束提交范围和验证方式
- 会在失败时让它复盘原因并缩小搜索空间

### 高级：会构建自己的 AI Coding Workbench

- 有项目级规则、个人工作流和团队共享规范
- 有专门的 skills、subagents、hooks 和 MCP 工具
- 有测试、CI、review、审计和回滚闭环
- 能把一次成功经验沉淀成可复用能力

### 专家：会设计团队级 AI Coding 操作系统

- 能为团队设计能力安装清单和权限模型
- 能判断 skill / plugin / hook / MCP / subagent 的取舍
- 能设计 agent eval、release gate 和 incident review
- 能把 AI Coding 从个人效率工具升级成工程组织能力

## 推荐能力安装顺序

1. 先打牢内建能力：`CLAUDE.md`、权限、常用命令、测试命令、Git 工作流
2. 再补个人技能：代码审查、测试、重构、文档、安全排查、性能分析
3. 再接外部系统：GitHub、issue tracker、知识库、CI、日志、只读数据库
4. 再上自动化：hooks、PR workflow、CI 失败处理、变更摘要
5. 最后做插件化：把团队通用能力打包成可安装、可版本化、可治理的 plugin

## 继续阅读路径

- [[Claude Code]]
- [[Claude Code 能力安装清单]]
- [[Claude Code 自定义能力工作台：Skills、Plugins、Hooks、MCP]]
- [[../07-Maps/Claude Code 生态能力图|Claude Code 生态能力图]]
- [[../../AI-Engineering/07-Topics/Claude Code Harness 工程实践|Claude Code Harness 工程实践]]
- [[../06-Topics/Coding Agents|Coding Agents]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../../AI-Engineering/07-Topics/扩展面设计：Skills、Plugins、Hooks、Apps 与 Automation|扩展面设计：Skills、Plugins、Hooks、Apps 与 Automation]]

## 官方资料

- [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code skills](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Claude Code plugins](https://code.claude.com/docs/en/plugins)
- [Claude Code subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Claude Code hooks](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Claude Code MCP](https://docs.anthropic.com/en/docs/claude-code/mcp)

