---
title: Harness Lab 第一轮：Repo 修复、Browser 操作与 Daily Ops
type: project-doc
status: learning
created: 2026-03-28
updated: 2026-03-28
---

# Harness Lab 第一轮：Repo 修复、Browser 操作与 Daily Ops

## 目标

用三组最小实验，把 `Codex`、`Claude Code`、`OpenClaw` 的真实强项跑出来。

不是追求“全功能覆盖”，而是回答三个更实用的问题：

- 谁最适合 `repo-local coding`
- 谁最适合 `browser / desktop task`
- 谁最适合 `recurring assistant ops`

## 实验 A：Repo 修复实验

### 场景

给一个真实 repo 一个很小的任务：

- 修一个 bug
- 改 2 到 5 个文件
- 跑测试
- 给出 diff 解释

### 首选对照

- `Claude Code`
- `Codex`

### 观察点

- 项目规则文件是否真正生效
- 改动后测试和 diff 审查是否顺
- 多轮迭代里，context 是否稳定
- 是否容易加入 hooks / review gate

### 输出记录

- 完成总耗时
- 第一版改动质量
- 第一次失败后恢复速度
- 你的主观顺手度

## 实验 B：Browser / desktop task 实验

### 场景

做一个明显依赖 GUI 的任务：

- 打开网页
- 找指定信息
- 完成几步点击
- 回传结果与依据

### 首选对照

- `Codex` / OpenAI browser-computer line
- `OpenClaw`（如果你想看 node / browser / app-style 动作面）

### 观察点

- 开始行动前是否需要太多 setup
- 人工接管是否自然
- 截图 / 页面状态回流是否清楚
- approval / replay / trace 是否足够可读

### 输出记录

- 首次成功率
- 错点 / 误读页面的次数
- 从失败回到正轨的成本
- 你对“可托付程度”的判断

## 实验 C：Daily ops / recurring automation 实验

### 场景

做一个每天都该跑的小任务：

- 每日 issue / CI 摘要
- 每晚 release brief
- 每周仓库巡检
- 每日个人简报

### 首选对照

- `OpenClaw`
- `Claude Code`（GitHub Actions 线）
- `Codex`（automations 线）

### 观察点

- 触发机制是否统一
- 失败后是否能回放和重跑
- 输出会不会污染主会话
- 结果投递到哪里最自然

### 输出记录

- schedule setup 成本
- 结果可读性
- 失败定位成本
- 长期运行心智是否稳定

## 评分表

| 维度 | Repo 修复 | Browser 任务 | Daily Ops |
| --- | --- | --- | --- |
| 上手成本 | 1-5 | 1-5 | 1-5 |
| 成功率 | 1-5 | 1-5 | 1-5 |
| 恢复与回放 | 1-5 | 1-5 | 1-5 |
| 审批与治理 | 1-5 | 1-5 | 1-5 |
| 长期可复用性 | 1-5 | 1-5 | 1-5 |

## 第一轮结论模板

- `我最愿意拿来做 repo 修复的 harness`：
- `我最愿意拿来做 browser task 的 harness`：
- `我最愿意长期挂着跑 daily ops 的 harness`：
- `最像 team coding workbench 的系统`：
- `最像 personal assistant runtime 的系统`：

## 推荐顺序

1. [[项目总览|Harness Lab]]
2. [[多厂商 Harness 对照实验]]
3. [[Harness Lab 第一轮：Repo 修复、Browser 操作与 Daily Ops]]
4. [[../../07-Topics/Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel|Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel]]

## 关联

- [[项目总览|Harness Lab]]
- [[最小 Harness Lab：从 CLI 到 Browser 的学习计划]]
- [[多厂商 Harness 对照实验]]
- [[../../07-Topics/Harness 工程案例：Codex、Claude Code、OpenClaw、Gemini CLI|Harness 工程案例：Codex、Claude Code、OpenClaw、Gemini CLI]]
- [[../../07-Topics/Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel|Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel]]
