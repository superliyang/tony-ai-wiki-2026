---
title: Claude Code Harness 工程实践
type: topic
status: active
tags:
  - ai/engineering
  - ai/harness
  - ai/coding-agent
  - ai/claude-code
created: 2026-05-15
updated: 2026-05-15
related_systems:
  - "[[../../AI-Learning/09-Systems/Claude Code|Claude Code]]"
---

# Claude Code Harness 工程实践

## 核心观点

从工程视角看，`Claude Code` 值得研究的不是“它会不会写代码”，而是它如何把 agent 放进真实软件工程闭环：

> 任务表达 → repo 理解 → 计划 → 修改 → 验证 → review → 提交 → 复盘 → 能力沉淀。

这条链路就是 `AI Coding Harness` 的基本形态。

## 标准任务闭环

### 1. Intake：定义任务

好的任务输入应包含：

- 目标：要解决什么问题
- 范围：哪些文件 / 模块可以改
- 验证：跑什么测试或检查
- 约束：不能破坏哪些行为
- 输出：需要 PR 摘要、风险说明还是文档同步

如果任务表达不清，Claude Code 会放大不确定性，而不是自动消除不确定性。

### 2. Repo Map：建立代码库地图

进入陌生项目时，先让 agent 做：

- 目录结构扫描
- 入口文件定位
- 核心模块和依赖关系
- 测试结构和运行方式
- 最近相关变更和风险区域

这一步适合沉淀成 `repo-map skill`。

### 3. Plan：拆成可验证步骤

计划不是形式主义，而是让 agent 的搜索空间变窄：

- 先复现还是先读代码
- 是最小修复还是结构性重构
- 哪些文件先读、哪些文件后改
- 每一步如何验证
- 如果失败如何回退

### 4. Edit：最小可控修改

好的 agent 修改应该：

- 只改任务相关文件
- 优先修根因，不做无关重构
- 保持现有风格
- 每轮修改后尽快验证
- 能解释为什么改这里而不是那里

### 5. Verify：验证闭环

Claude Code 的专业使用一定要把验证前置：

- 单测 / 集成测试 / E2E
- lint / typecheck / build
- 快速 smoke test
- 对关键路径补回归用例
- 对不可运行测试说明原因和风险

验证命令应写进 `CLAUDE.md` 或相关 skill。

### 6. Review：审查与风险说明

review 不只是让 agent “看看有没有问题”，而要分角色：

- `code-reviewer`：代码质量、复杂度、边界
- `test-engineer`：用例覆盖、回归风险
- `security-reviewer`：权限、注入、依赖、secret
- `architect`：模块边界、演进一致性

### 7. Commit / PR：协作交付

交付输出至少包含：

- 变更摘要
- 验证记录
- 风险和回滚方式
- 未覆盖项
- 与 issue / review comment 的对应关系

这部分适合做成 `PR workflow skill` 或团队 plugin。

### 8. Retrospective：沉淀能力

每次任务结束后问三个问题：

- 哪个步骤下次可以变成 skill
- 哪个失败模式需要 hook / permission 约束
- 哪个上下文应该写回 `CLAUDE.md`

这就是从“会用工具”到“建设 AI Coding 能力”的分界线。

## 团队级落地架构

### 个人层

- 个人常用 skills
- 个人 subagents
- 个人命令习惯
- 本地项目记忆

### 项目层

- 项目级 `CLAUDE.md`
- 项目级 testing / lint / build 入口
- 项目级敏感路径和禁止动作
- 项目级 docs / ADR / release 规范

### 团队层

- 共享 skills
- PR workflow plugin
- GitHub / issue / docs / CI MCP
- security hooks
- coding agent eval pack
- agent incident review

### 组织层

- 插件来源治理
- 权限分层和审计
- 模型与供应商策略
- 合规、数据边界和生产访问策略
- AI Coding ROI、质量和风险指标

## 专家能力标准

### 能力 1：任务建模

能把模糊需求转成可执行任务：

- 目标清楚
- 范围清楚
- 验证清楚
- 风险清楚

### 能力 2：上下文工程

能控制 agent 看到什么、忽略什么、记住什么：

- `CLAUDE.md`
- repo map
- selected files
- issue / PR / logs
- 任务阶段性总结

### 能力 3：工具面设计

能判断哪些工具应该给 agent：

- shell
- Git
- browser
- MCP
- database
- CI
- observability

### 能力 4：扩展面设计

能选择正确扩展形态：

- skill 沉淀方法
- subagent 沉淀角色
- MCP 接系统
- hook 做自动化和控制
- plugin 做团队分发

### 能力 5：验证与治理

能让 agent 的结果可上线：

- test gate
- eval pack
- release gate
- permission policy
- audit log
- rollback plan

## 常见失败模式

- 把 `CLAUDE.md` 写成大杂烩，导致规则不可执行
- 只装插件，不设计权限和使用场景
- 让 agent 一次性做太大范围修改
- 没有测试命令，却要求 agent 保证正确
- 把 MCP 接得过宽，造成数据和权限风险
- hooks 过度自动化，调试困难且不可审计
- 没有复盘机制，导致每次都从零开始

## 相关

- [[../../AI-Learning/09-Systems/Claude Code|Claude Code]]
- [[../../AI-Learning/09-Systems/Claude Code 生态全景|Claude Code 生态全景]]
- [[../../AI-Learning/09-Systems/Claude Code 能力安装清单|Claude Code 能力安装清单]]
- [[../../AI-Learning/09-Systems/Claude Code 自定义能力工作台：Skills、Plugins、Hooks、MCP|Claude Code 自定义能力工作台：Skills、Plugins、Hooks、MCP]]
- [[Harness Engineering]]
- [[扩展面设计：Skills、Plugins、Hooks、Apps 与 Automation]]
- [[Agent Security、Sandbox 与 Approval Architecture]]
- [[Eval Harness 与 Regression Suites]]

