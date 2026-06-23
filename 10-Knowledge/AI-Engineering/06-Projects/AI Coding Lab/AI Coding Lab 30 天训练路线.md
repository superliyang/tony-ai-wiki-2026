---
title: AI Coding Lab 30 天训练路线
type: project-doc
status: active
created: 2026-05-16
updated: 2026-05-16
---

# AI Coding Lab 30 天训练路线

## 训练原则

30 天不是为了刷工具，而是为了建立稳定肌肉记忆：

> 每个任务都必须有 brief、计划、diff、验证、复盘和可沉淀项。

不要一上来挑战大型重构。先用低风险任务建立闭环，再逐步加入 skills、subagents、hooks、MCP 和团队门禁。

## Week 1：个人任务闭环

目标：能稳定完成小任务，不乱改、不越权。

### D1：环境与项目记忆

- 选择 1 个低风险 repo
- 写最小 `CLAUDE.md / AGENTS.md`
- 写清测试命令、启动命令、禁改区域
- 记录 agent 首次进入项目的误区

### D2：Repo Map

- 让 agent 输出项目结构、入口、模块边界
- 要求列出“应读文件”和“不应改文件”
- 记录上下文是否足够

### D3-D4：Bugfix

- 选 1 个小 bug
- 走 `brief -> plan -> patch -> test -> summary`
- 要求解释为什么改这些文件

### D5：Test 补全

- 选一个缺测试的行为
- 让 agent 补最小回归测试
- 检查是否为过测试而改坏测试语义

### D6-D7：复盘

- 复制 [[AI Coding Lab 实战任务记录模板]]
- 标注失败模式
- 抽出一个候选 skill

## Week 2：能力沉淀

目标：把高频流程从 prompt 升级成可复用能力。

### D8-D10：Skill

- 写一个 `repo-map skill`
- 写一个 `bugfix skill`
- 写一个 `test-writer skill`
- 每个 skill 都要有触发条件、流程、输出格式、验证要求

### D11-D12：Subagent

- 写一个 `code-reviewer subagent`
- 写一个 `test-engineer subagent`
- 明确每个 subagent 的工具边界和禁止事项

### D13-D14：Hook

- 加一个改动后测试提醒 hook
- 加一个危险命令提醒或阻断 hook
- 记录误报、漏报和实际体验

## Week 3：工具与评测

目标：把 coding agent 放进更真实的工程上下文。

### D15-D17：MCP / 外部上下文

- 先接只读上下文：issue、文档、CI log 任选其一
- 记录 agent 是否能引用来源
- 禁止直接写外部系统

### D18-D20：Eval Pack

- 使用 [[../../04-Evaluation/Coding Agent Eval Pack：Repo 修复、测试与小型重构|Coding Agent Eval Pack]]
- 至少跑 3 个任务：repo 理解、单文件修复、多文件联动
- 记录成功率、无关改动、危险命令尝试

### D21：复盘

- 更新 skill / hook / subagent
- 写出一个“下次默认流程”

## Week 4：团队试点

目标：从个人效率进入团队机制。

### D22-D24：试点设计

- 选择 1 个低风险 repo
- 定义试点范围、禁改目录、审批策略
- 明确哪些任务只能 comment，哪些允许 patch

### D25-D27：PR 工作流

- 让 agent 生成 PR summary
- 让 code-reviewer subagent 做二次审查
- 用测试记录和风险说明补 PR

### D28-D29：验收矩阵

- 使用 [[../../04-Evaluation/AI Coding 专家能力验收矩阵|AI Coding 专家能力验收矩阵]]
- 给个人能力、团队流程和安全治理打分
- 找出最低分项

### D30：最终复盘

- 输出一页 `AI Coding Lab 结论`
- 明确继续投入、暂停或扩大试点
- 把沉淀项回写到 skill / subagent / hook / project memory

## 完成标准

- 至少完成 5 个真实 repo 任务
- 至少沉淀 2 个 skills
- 至少沉淀 1 个 subagent
- 至少配置 1 个安全/质量 hook
- 至少跑过一次 eval pack
- 至少完成一份团队试点建议

## 关联

- [[项目总览]]
- [[AI Coding Lab 实战任务记录模板]]
- [[AI Coding Lab 专家验收清单]]
- [[AI Coding Lab 团队试点运行手册]]

