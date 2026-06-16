---
title: "让 Hermes 创建飞书讨论 Agent 的操作说明"
created: 2026-06-15
updated: 2026-06-15
status: ready
author: codex
tags:
  - hermes
  - feishu
  - discussion
  - prompt
---

# 让 Hermes 创建飞书讨论 Agent 的操作说明

这份说明的目标是：

```text
让 Hermes 在 inbox 层创建 5 个讨论角色 draft
而不是直接修改 canonical agent system
```

## 推荐路径

先让 Hermes 创建 **draft agent files**，位置限定在：

```text
00-Inbox-AI/hermes/discussion-pilot/
```

不要一上来让 Hermes 写：

- `60-Agents/`
- `90-Agent-System/`
- `10-Knowledge/`

原因：

- 现在是在试点；
- 需要先验证飞书讨论效果；
- 讨论层还不应该直接进入 canonical system。

## 创建目标

让 Hermes 创建或更新这 6 个文件：

```text
00-Inbox-AI/hermes/discussion-pilot/README.md
00-Inbox-AI/hermes/discussion-pilot/信号员-Hermes.md
00-Inbox-AI/hermes/discussion-pilot/工程师-Hermes.md
00-Inbox-AI/hermes/discussion-pilot/运营官-Hermes.md
00-Inbox-AI/hermes/discussion-pilot/策略官-Hermes.md
00-Inbox-AI/hermes/discussion-pilot/主持人-Hermes.md
```

## 详细步骤

### 方式 A：在飞书里直接发给 Hermes

1. 给 Hermes 发一条单独消息。
2. 让它先读现有 draft 和 prompt。
3. 让它只在 `00-Inbox-AI/hermes/discussion-pilot/` 下创建或更新文件。
4. 要求它输出一份 run summary。
5. 不允许它直接 promote 到正式系统层。

### 方式 B：在 Hermes CLI / gateway 里作为一次明确任务执行

1. 把下面的 prompt 作为单次任务发给 Hermes。
2. 要求它先读指定文件。
3. 要求它创建/更新上面的 6 个 draft 文件。
4. 要求它完成后写一个简短总结到：

```text
00-Inbox-AI/hermes/YYYY-MM-DD-discussion-agent-creation-summary.md
```

## 主 Prompt

下面这段可以直接复制给 Hermes：

```text
你是 Hermes，Tony 的长期运行 scout / recall / reminder agent。

## 任务
为飞书多 Agent 讨论组创建一套 inbox-layer draft agent files。

## 目标
创建或更新一套“讨论层角色定义”，用于飞书群内多角色讨论，不进入 canonical system。

## 先读这些文件
- AGENTS.md
- 90-Agent-System/仓库地图.md
- 90-Agent-System/当前状态.md
- 60-Agents/Hermes.md
- 90-Agent-System/integrations/Hermes-Codex.md
- 00-Inbox-AI/hermes/2026-06-15-feishu-multi-agent-discussion-pilot.md
- 90-Agent-System/prompts/hermes-feishu-discussion-moderator.md

## 创建或更新这些文件
- 00-Inbox-AI/hermes/discussion-pilot/README.md
- 00-Inbox-AI/hermes/discussion-pilot/信号员-Hermes.md
- 00-Inbox-AI/hermes/discussion-pilot/工程师-Hermes.md
- 00-Inbox-AI/hermes/discussion-pilot/运营官-Hermes.md
- 00-Inbox-AI/hermes/discussion-pilot/策略官-Hermes.md
- 00-Inbox-AI/hermes/discussion-pilot/主持人-Hermes.md

## 每个角色文件至少要包含
1. 角色职责
2. 只回答什么问题
3. 输入来源
4. 输出风格
5. 推荐输出模板
6. 禁止事项

## 命名要求
使用以下中文名字：
- 信号员 Hermes
- 工程师 Hermes
- 运营官 Hermes
- 策略官 Hermes
- 主持人 Hermes

## 主持人要求
主持人 Hermes 必须包含：
- 讨论开场模板
- 角色发言顺序
- Tony 可用控制词：继续 / 反方 / 收口
- 群里短版收口格式
- YAML-first 的结构化收口模板
- 下游路由规则：watch / study / build / publish / ignore

## 写入边界
你只允许写：
- 00-Inbox-AI/hermes/discussion-pilot/
- 00-Inbox-AI/hermes/YYYY-MM-DD-discussion-agent-creation-summary.md

你不允许写：
- 60-Agents/
- 90-Agent-System/
- 10-Knowledge/
- 20-Maps/
- 30-Playbooks/
- 40-Projects/

## 风格
- 中文为主
- 英文 technical terms 保留
- 用 Obsidian wikilinks when useful
- 保持简洁、可执行

## 完成后
写一个简短 summary 文件到：
00-Inbox-AI/hermes/YYYY-MM-DD-discussion-agent-creation-summary.md

summary 至少包含：
1. 创建了哪些文件
2. 每个角色的一句话定位
3. 是否发现边界冲突
4. 建议 Tony 下一步做什么
```

## 更保守的 Prompt

如果你想让 Hermes 只“复核并补全”我已经写好的 draft，而不是从头生成，用这版更稳：

```text
请不要从零发明一套新角色。

请读取：
- 00-Inbox-AI/hermes/discussion-pilot/README.md
- 00-Inbox-AI/hermes/discussion-pilot/信号员-Hermes.md
- 00-Inbox-AI/hermes/discussion-pilot/工程师-Hermes.md
- 00-Inbox-AI/hermes/discussion-pilot/运营官-Hermes.md
- 00-Inbox-AI/hermes/discussion-pilot/策略官-Hermes.md
- 00-Inbox-AI/hermes/discussion-pilot/主持人-Hermes.md

你的任务不是重写系统，而是：
- 检查是否缺少关键字段
- 补充不清楚的边界
- 改善可执行性
- 保持现有命名和结构

不要新增新的角色名字。
不要把这些 draft promote 到 canonical system。
```

## 我对你的建议

如果你现在只是想让 Hermes “真正参与这套机制”，我建议你用：

- 第一轮：`更保守的 Prompt`

原因：

- 我已经把骨架搭好了；
- Hermes 更适合“补全、复核、收口”，而不是在这一步重新发明一套角色；
- 这样系统更稳，也更容易比较“我的设计”和“Hermes 的微调”之间的差异。
