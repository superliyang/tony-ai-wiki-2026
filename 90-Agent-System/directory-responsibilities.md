---
title: "目录职责说明"
created: 2026-06-21
updated: 2026-06-21
status: active
tags:
  - agent-system
  - repo-map
  - directory
  - governance
---

# 目录职责说明

这页定义当前主知识库里每个目录的职责、内容边界和写入规则。

> [!important] 当前原则
> 主库是长期知识和入口系统，不是 AI 原始产物堆放区。Hermes / Codex 的新生成内容默认先进 working vault，经 review 后再进入这里。

## 顶层目录

| 目录 | 职责 | 应该放什么 | 不应该放什么 |
|---|---|---|---|
| `00-Home/` | 人类入口层 | 今日入口、入口总台、当前主线、下一步、旧库工作台历史入口 | 大量正文知识、AI 原始草稿 |
| `00-Inbox-AI/` | 历史 AI staging 层 | 旧的 Hermes/Codex 记录、历史 review queue、历史 memory、飞书发布记录 | 2026-06-16 之后的新任务原始产物 |
| `10-Knowledge/` | 正式知识资产层 | 领域知识、学习路径、专题总览、地图、模板、案例、playbook 型知识 | 未审阅聊天记录、一次性任务草稿 |
| `20-Maps/` | 人类导航和跨领域地图 | 知识门户、领域入口、核心知识网络、迁移地图、Canvas 入口 | 某个领域内部的大量正文 |
| `30-Playbooks/` | 可复用方法层 | 学习法、工作法、操作手册、跨领域可复用流程 | 临时想法、未验证流程 |
| `40-Projects/` | 项目资产层 | 项目 README、下一步、阶段总结、项目产物链接 | 泛知识卡片、系统协议 |
| `60-Agents/` | Agent 能力和角色层 | 个人 Agent 能力映射、Agent 边界、角色说明 | 具体任务执行日志 |
| `90-Agent-System/` | AI 协作系统层 | 规则、工作流、提示词、自动化、决策、迁移报告、系统状态 | 业务领域正文、个人日记 |
| `output-feishu/` | 飞书发布中间层 | 清洗后可发布到飞书的 Markdown projection | 主知识源、未清洗私密内容 |
| `output-public/` | 公开/半公开输出层 | 面向外部输出的说明、历史 public projection | 主库内容编辑源 |
| `scripts/` | 本地维护脚本层 | 可重复运行的维护、迁移、校验脚本 | 一次性临时命令、业务正文 |
| `Nexus/` | 实验/数据辅助层 | Nexus 相关数据或实验产物 | 正式知识入口 |

## Runtime / App State

这些目录是工具运行状态或本地应用状态，不应该作为知识库内容维护：

| 目录 | 说明 | 规则 |
|---|---|---|
| `.git/` | Git 内部状态 | 不手动编辑 |
| `.obsidian/` | Obsidian 本地配置和插件状态 | 不作为知识内容同步原则来源 |
| `.stfolder/` | Syncthing 状态 | 不纳入知识结构 |
| `.claude/`, `.claudian/` | Claude / Claudian 本地状态 | 不作为知识资产 |
| `.conversations/`, `.workspaces/` | 工具会话/工作区状态 | 不作为长期知识 |

## `10-Knowledge/` 领域目录

| 目录 | 职责 |
|---|---|
| `AI/` | AI 总览、人物、公司、模型、论文、系统、新闻和 AI 导航总控 |
| `AI-Foundations/` | AI 历史、基础概念、经典论文、范式 |
| `AI-Applications/` | AI 行业应用、Agent 产品、workflow、落地案例 |
| `AI-Architecture/` | AI 系统设计、架构评审、案例库、面试/评审材料 |
| `AI-Engineering/` | AI 工程、LLMOps、AgentOps、训练、评估、部署、框架 |
| `AI-Open-Source/` | AI 开源项目、组织、分类、模式、watchlist |
| `Advertising/` | 广告投放、归因、预算、SKAN、fraud、投放复盘 |
| `International-Payments/` | 国际支付、成功率、3DS、拒付、路由、清结算、对账 |
| `Security/` | 安全标准、工具、控制清单、应用/API 安全、安全运营、案例复盘 |
| `Big-Data/` | 大数据平台、产品、主题、playbook、案例 |
| `Cloud-Native/` | 云原生、平台工程、工作流、案例 |
| `Engineering-Management/` | 技术管理、角色路径、管理问题感、管理案例 |
| `English-Learning/` | 英语学习材料、路径、模板、onboarding |
| `Macro-Insight/` | 宏观观察、信息源、雷达、案例 |
| `Skills-Gaming/` | 游戏技能项目、市场、系统、playbook、hackathon 经验 |
| `Personal-Knowledge-System/` | 个人知识系统、Obsidian/GitHub/飞书/Codex/Hermes 协作 |
| `Shared-Templates/` | 跨领域模板和旧库共享模板 |

## `90-Agent-System/` 子目录

| 目录 | 职责 |
|---|---|
| `automations/` | Codex/Hermes 自动化矩阵、导出和说明 |
| `decisions/` | 结构性决策记录 |
| `integrations/` | Hermes、Feishu、Codex 等外部工具集成说明 |
| `legacy-tony2026/` | 旧库迁出后的历史说明、archive、tags 等非正文遗留资产 |
| `migration/` | 迁移报告、迁移脚本输出、迁移审计 |
| `plans/` | 系统建设计划、清理计划、刷新计划 |
| `prompts/` | Hermes/Codex 可复用提示词 |
| `reviews/` | 审计、评估、完整性检查报告 |
| `rules/` | Agent 或工具规则 |
| `scripts/` | 脚本说明和 runbook，不放可执行脚本本体 |
| `skills/` | 能力/skill 说明或候选 |
| `workflows/` | 稳定协作流程，例如飞书发布、review gate、knowledge gardener |

## 写入规则

| 场景 | 应写入 |
|---|---|
| 刚产生的 AI 调研、草稿、任务请求 | working vault，而不是主库 |
| 经 Tony 接受、可长期复用的知识 | `10-Knowledge/` 对应领域 |
| 只是帮助今天找到入口 | `00-Home/` 或 `20-Maps/` |
| 跨领域导航变化 | `20-Maps/`，并同步相关入口 |
| 可复用流程稳定下来 | `30-Playbooks/` 或 `90-Agent-System/workflows/` |
| 项目推进状态 | `40-Projects/<project>/` |
| Agent 协作机制变化 | `90-Agent-System/` |
| 飞书可读版本 | `output-feishu/` |

## 清理规则

1. 不再新建深层 `_Imported` 源目录。
2. 不把 working vault 的原始输出直接搬入正式知识层。
3. 如果某页只是入口，保持短、清晰、可点击。
4. 如果某页是领域正文，要能回答一个明确问题。
5. 如果某目录职责变了，同步更新本页、[[90-Agent-System/仓库地图]] 和相关入口页。

