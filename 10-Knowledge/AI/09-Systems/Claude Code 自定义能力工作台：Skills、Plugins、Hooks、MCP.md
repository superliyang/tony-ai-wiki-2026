---
title: Claude Code 自定义能力工作台：Skills、Plugins、Hooks、MCP
type: workbench
status: active
tags:
  - ai/coding-agent
  - ai/claude-code
  - ai/skills
  - ai/plugins
created: 2026-05-15
updated: 2026-05-15
related_systems:
  - "[[Claude Code]]"
  - "[[Claude Code 生态全景]]"
---

# Claude Code 自定义能力工作台：Skills、Plugins、Hooks、MCP

## 核心判断

自定义 Claude Code 能力时，不要问“我要写一个什么插件”，先问：

> 这个能力到底是在沉淀方法、固定角色、接外部系统、做自动化，还是要打包分发？

不同答案对应不同能力形态。

## 能力演进阶梯

### 1. Prompt Pattern

适合：还不确定是否高频复用的个人经验。

例子：

- “先读测试，再改实现”
- “先输出风险清单，再动文件”
- “先画模块边界，再做重构计划”

如果重复出现 3 次以上，就可以沉淀。

### 2. `CLAUDE.md`

适合：项目级稳定规则。

例子：

- 项目启动命令
- 测试命令
- 代码风格
- 架构边界
- 不要修改的目录
- 常见任务路径

`CLAUDE.md` 是默认记忆，不适合塞太多长流程。长流程应该进入 skill。

### 3. Skill

适合：可复用专业方法。

一个好的 skill 通常包含：

- `name`：稳定、短、语义明确
- `description`：什么时候应该触发
- 任务边界：适合做什么、不适合做什么
- 操作流程：先看什么、怎么判断、怎么改、怎么验证
- 输出格式：总结、风险、验证、下一步
- 可选脚本 / 模板 / 参考资料

适合做成 skill 的能力：

- 安全代码审查
- 单测补全
- 重构计划
- PR 总结
- CI 失败分析
- 性能排查
- Obsidian 知识库维护

### 4. Slash Command

适合：固定触发入口。

例子：

- `/review-pr`
- `/explain-module`
- `/write-tests`
- `/prepare-release`

如果只是“一键触发一段流程”，slash command 足够；如果包含专业知识、脚本、模板和可扩展资源，应该升级成 skill。

### 5. Subagent

适合：固定专家角色。

一个好的 subagent 应该写清楚：

- 它是什么专家
- 它什么时候被调用
- 它能用哪些工具
- 它输出什么
- 它不能越过哪些边界

推荐角色：

- `architect`：架构边界、模块拆分、演进路线
- `code-reviewer`：缺陷、可维护性、复杂度
- `test-engineer`：测试策略、回归用例、flaky 定位
- `security-reviewer`：注入、权限、依赖、secret、数据泄露
- `docs-maintainer`：README、ADR、迁移说明、知识库索引

### 6. MCP

适合：把外部系统变成 agent 可用的工具和资源。

推荐接入顺序：

1. GitHub / GitLab：issue、PR、diff、review comment
2. 文档 / 知识库：设计文档、API 文档、规范
3. CI / 日志：构建失败、测试日志、运行指标
4. 浏览器 / E2E：页面检查、截图、自动化测试
5. 数据库：只读查询、脱敏视图、禁止生产写入

设计 MCP 时要优先定义：

- 只读还是可写
- 访问哪些项目 / 环境
- 是否脱敏
- 是否记录审计日志
- 失败时如何降级

### 7. Hook

适合：事件驱动的质量、安全和流程控制。

推荐 hooks：

- `PreToolUse`：危险命令确认、敏感路径检查
- `PostToolUse`：格式化、lint、局部测试提醒
- `UserPromptSubmit`：补充上下文、检查任务表达是否清晰
- `Stop`：生成变更摘要、验证记录、未完成事项

不要把 hook 写成不可控的黑盒自动化。它应该短、小、可审计、可关闭。

### 8. Plugin

适合：团队共享的能力包。

一个 plugin 可以打包：

- commands
- agents
- hooks
- MCP servers
- skills
- LSP servers
- monitors

什么时候应该做 plugin：

- 同一组能力要在多个项目复用
- 需要版本管理和发布节奏
- 需要团队统一安装和治理
- 需要把 skill、hook、MCP、command 组合成一个产品化能力

## 取舍表

| 问题 | 应该用什么 |
|---|---|
| 只是项目规则 | `CLAUDE.md` |
| 重复任务方法 | `Skill` |
| 固定命令入口 | `Slash command` |
| 固定专家角色 | `Subagent` |
| 要访问外部工具 / 数据 | `MCP` |
| 要在某个事件自动触发 | `Hook` |
| 要团队分发一组能力 | `Plugin` |

## 示例：安全代码审查能力

最小形态：

- prompt pattern：每次让 Claude Code 检查鉴权、注入、secret、依赖

项目形态：

- `CLAUDE.md`：写明安全敏感模块、禁止自动修改生产配置
- skill：定义安全 review 检查清单和输出格式
- subagent：固定 `security-reviewer`
- hook：检测 secret、危险命令和敏感路径
- MCP：接只读依赖扫描、SAST、issue tracker
- plugin：打包成团队共享安全审查能力

## 示例：PR 工作流能力

最小形态：

- slash command：`/prepare-pr`

专业形态：

- skill：生成 PR 摘要、风险、验证记录、回滚方案
- subagent：`code-reviewer` 和 `test-engineer` 分别审查
- hook：停止前提醒未运行测试
- MCP：读取 issue、PR diff、CI log
- plugin：团队统一安装 PR workflow pack

## 能力验收标准

一个自定义能力值得留下，至少满足：

- 高频：一个月内多次使用
- 可验证：输出能被测试、review 或 checklist 检查
- 可迁移：不是只对一个临时任务有效
- 可治理：权限、日志、失败和回滚清楚
- 可维护：说明短、边界清晰、版本可追踪

## 相关

- [[Claude Code 生态全景]]
- [[Claude Code 能力安装清单]]
- [[../../AI-Engineering/07-Topics/扩展面设计：Skills、Plugins、Hooks、Apps 与 Automation|扩展面设计：Skills、Plugins、Hooks、Apps 与 Automation]]
- [[../../AI-Engineering/07-Topics/Plugin 安装、发现与 Runtime Reality|Plugin 安装、发现与 Runtime Reality]]
- [[../../AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]

