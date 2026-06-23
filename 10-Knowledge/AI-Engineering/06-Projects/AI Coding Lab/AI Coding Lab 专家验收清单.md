---
title: AI Coding Lab 专家验收清单
type: checklist
status: active
created: 2026-05-16
updated: 2026-05-16
---

# AI Coding Lab 专家验收清单

## 使用方式

这张清单用来判断：你是不是已经从“会用 AI 写代码”进入“能设计 AI Coding 工作方式”。

每项按 `0 / 1 / 2` 评分：

- `0`：没有稳定做到
- `1`：个人能做到
- `2`：能沉淀为团队机制

## 1. 任务建模

- 能把模糊需求写成 `Task Brief`
- 能限定可改范围和禁改范围
- 能写出验证方式
- 能识别高风险任务并请求澄清
- 能判断任务是否适合交给 agent

## 2. 上下文工程

- 能维护项目级 `CLAUDE.md / AGENTS.md`
- 能让 agent 先做 repo map
- 能控制上下文输入，不一次塞满所有文件
- 能让 agent 引用文件、issue、CI log 等依据
- 能用 session summary 支持任务恢复

## 3. 工具面设计

- 能区分只读工具和写入工具
- 能控制 shell / Git / filesystem 权限
- 能设计测试、lint、build 的默认命令
- 能识别 MCP 的数据和权限边界
- 能为危险命令设置审批或阻断

## 4. 扩展面沉淀

- 至少有 2 个可用 skills
- 至少有 1 个专用 subagent
- 至少有 1 个质量或安全 hook
- 能判断何时用 skill、subagent、hook、MCP、plugin
- 能把团队共享能力打包成项目级规范或 plugin

## 5. 验证与治理

- 能运行或说明测试结果
- 能做 diff review
- 能记录未覆盖风险
- 能设计回滚方式
- 能把失败案例写入复盘

## 6. 团队落地

- 能设计低风险试点范围
- 能制定权限策略和敏感路径策略
- 能定义 PR / CI / review 接入方式
- 能设计 adoption 指标：效率、质量、风险、成本
- 能向团队解释为什么某些能力不能直接开放

## 分级标准

| 总分 | 等级 | 含义 |
|---:|---|---|
| 0-20 | 使用者 | 能让 agent 帮忙，但机制不稳定 |
| 21-40 | 熟练者 | 个人闭环稳定，有初步沉淀 |
| 41-55 | 专家候选 | 能设计项目级能力和门禁 |
| 56-60 | 团队专家 | 能把 AI Coding 变成团队工程机制 |

## 下一步动作

- 如果低于 20 分：先补 [[AI Coding Lab 30 天训练路线]]
- 如果 21-40 分：重点补 skills、subagents、hooks
- 如果 41-55 分：重点补 eval、权限、团队试点
- 如果 56 分以上：开始做跨 repo 的插件化和治理模型

## 关联

- [[项目总览]]
- [[AI Coding Lab 30 天训练路线]]
- [[../../04-Evaluation/AI Coding 专家能力验收矩阵|AI Coding 专家能力验收矩阵]]

