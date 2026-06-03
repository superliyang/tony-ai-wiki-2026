---
title: Claude Code 能力安装清单
type: checklist
status: active
tags:
  - ai/coding-agent
  - ai/claude-code
  - ai/workbench
created: 2026-05-15
updated: 2026-05-15
related_systems:
  - "[[Claude Code]]"
  - "[[Claude Code 生态全景]]"
---

# Claude Code 能力安装清单

## 使用原则

不要一上来疯狂装插件。正确顺序是：

1. 先用内建能力跑通真实项目
2. 再把高频任务沉淀为 `skills`
3. 再把专家角色沉淀为 `subagents`
4. 再用 `MCP` 接外部数据和工具
5. 再用 `hooks` 做安全、质量和自动化闭环
6. 最后把团队共用能力打包成 `plugins`

## 基础必装 / 必配

### 项目规则

- `CLAUDE.md`：项目结构、启动方式、测试命令、提交规范、禁改区域
- 权限设置：哪些命令可自动执行，哪些命令必须确认
- Git 规范：分支、提交信息、PR 描述、review follow-up
- 常用任务模板：bugfix、refactor、test、docs、security review

### 本地工程能力

- `ripgrep / fd / jq`：快速搜索与结构化数据处理
- 项目包管理器：`npm / pnpm / yarn / uv / pip / poetry / cargo / go`
- 测试与格式化命令：让 Claude Code 能稳定验证自己的修改
- 诊断脚本：启动、健康检查、日志查看、局部回归

## 能力分类清单

### 1. 代码库理解

目标：让 agent 快速知道“这个项目怎么工作”。

- repo map skill：扫描目录、入口、依赖、模块边界
- architecture explainer skill：解释核心链路、关键抽象、数据流
- legacy code reader subagent：专门读复杂旧代码，不急着改

适合沉淀为：`skill + subagent`。

### 2. 编码与重构

目标：让 agent 能做受控修改，而不是到处乱改。

- bugfix skill：复现、定位、最小修改、验证
- refactor skill：行为保护、测试优先、分阶段迁移
- migration skill：接口兼容、灰度路径、回滚策略
- code-reviewer subagent：审查质量、边界、可维护性

适合沉淀为：`skill + subagent + hooks`。

### 3. 测试与质量

目标：让 agent 的输出可验证。

- test-writer skill：根据行为补单测、集成测试、回归测试
- flaky-test investigator subagent：定位不稳定测试
- post-edit hook：改文件后提示或自动运行局部测试
- CI failure triage skill：读日志、定位失败、提出最小修复

适合沉淀为：`skill + hook + CI workflow`。

### 4. 安全与合规

目标：避免 agent 把安全风险写进代码。

- security-review skill：注入、鉴权、越权、secret、依赖风险
- dependency-audit skill：依赖升级、CVE、license 检查
- secret guard hook：阻止提交密钥、token、证书
- sensitive-path permission：生产配置、支付、安全模块默认更严格

适合沉淀为：`skill + hook + permission policy`。

### 5. GitHub / PR 工作流

目标：让 Claude Code 接入日常工程协作。

- PR summary skill：生成变更说明、风险点、验证记录
- review-follow-up skill：逐条处理 review comment
- issue-to-PR workflow：从 issue 拆任务、实现、验证、写 PR
- CI triage workflow：自动分析失败日志并提出修复方案

适合沉淀为：`plugin + GitHub Actions + skill`。

### 6. 知识库与文档

目标：让 agent 不只改代码，也维护知识资产。

- docs-maintainer skill：代码变更后同步 README / ADR / changelog
- architecture-decision skill：生成 ADR、方案对比、迁移计划
- knowledge-base MCP：接内部文档、设计稿、API 规范
- changelog hook：停止前产出变更摘要和未完成事项

适合沉淀为：`skill + MCP + hook`。

### 7. 外部系统集成

目标：让 agent 能读取真实上下文，但不越权。

- issue tracker MCP：读取 Jira / Linear / GitHub Issues
- observability MCP：只读日志、trace、metrics
- database MCP：只读查询，禁止写生产
- browser / e2e MCP：跑 UI 检查、截图、端到端测试

适合沉淀为：`MCP + permission policy`。

## 选择能力形态

| 需求 | 首选形态 | 原因 |
|---|---|---|
| 高频任务方法 | `Skill` | 可复用、可渐进加载、适合沉淀专业流程 |
| 固定命令入口 | `Slash command` | 触发简单、适合模板化动作 |
| 专家角色分工 | `Subagent` | 有独立上下文、目标和工具边界 |
| 外部系统连接 | `MCP` | 标准化暴露工具、资源和 prompts |
| 事件驱动自动化 | `Hook` | 适合质量、安全、审计和工作流闭环 |
| 团队共享能力包 | `Plugin` | 可打包、可版本化、可分发、可治理 |

## 安装前安全检查

- 插件来源是否可信
- 是否请求过宽工具权限
- 是否会读取敏感文件、密钥或生产数据
- 是否会执行 shell 命令、网络请求或写外部系统
- 是否有版本、更新记录和回滚方式
- 是否能在项目级而不是全局级启用

## 最小推荐套装

个人学习阶段：

- `CLAUDE.md`
- bugfix / refactor / test / docs / security-review skills
- code-reviewer / test-engineer subagents
- GitHub 或本地 Git 工作流
- 改动后测试提醒 hook

团队落地阶段：

- 项目级 `CLAUDE.md`
- 团队共享 skills
- 受控 MCP：GitHub、issue、docs、CI、logs
- 安全 hooks：secret、dangerous command、sensitive path
- PR workflow plugin
- agent 变更审计、失败复盘和 release gate

## 相关

- [[Claude Code 生态全景]]
- [[Claude Code 自定义能力工作台：Skills、Plugins、Hooks、MCP]]
- [[../../AI-Engineering/07-Topics/Claude Code Harness 工程实践|Claude Code Harness 工程实践]]
- [[../../AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]

