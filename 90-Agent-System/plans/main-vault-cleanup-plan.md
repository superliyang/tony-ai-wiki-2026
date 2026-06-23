---
title: "主知识库清理计划"
created: 2026-06-16
updated: 2026-06-16
status: active
tags:
  - agent-system
  - cleanup
  - vault-boundary
---

# 主知识库清理计划

这份计划用于把主知识库从“混合工作区”整理成“正式知识库”。原则是先治理入口，再小批量迁移，不做一次性大搬家。

## 当前判断

主库保留这些职责：

- `00-Home/`: 人类每日入口、当前主线和下一步。
- `10-Knowledge/`: 已审或明确提升后的正式知识资产。
- `20-Maps/`: 跨领域地图、导航和旧库入口。
- `30-Playbooks/`: 可复用方法、流程和模板。
- `40-Projects/`: 项目记录、迁移计划和构建工作。
- `60-Agents/`: 工具角色、能力边界和人机协作说明。
- `90-Agent-System/`: Agent 协作规则、工作流、决策和系统治理。

主库不再承担这些职责：

- Hermes 自动写入区。
- Hermes active memory。
- 未审 AI 产物的默认堆放处。
- 工具 runtime、会话缓存、临时输出目录。

## 边界

- Hermes 工作库: `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/`
- 主知识库: `/Users/tony/Vault/tony-wiki-space/tony-ai-wiki-2026/`
- 旧库归档: `/Users/tony/Vault/tony-wiki-space/tony-legacy-archive/`
- 旧原始导入: old source copy, now deletion candidate after extraction

## 清理批次

### Batch 1: 冻结旧 AI Inbox

目标：停止把 `00-Inbox-AI/` 当作 active staging。

- 将 [[00-Inbox-AI/README]] 标记为 frozen historical staging。
- 保留现有文件，不批量移动。
- 新 Hermes 内容统一进入 working vault。
- 新人工资料进入 working vault 的 `00-Human-Inbox/`。

### Batch 2: 盘点旧 AI Inbox

目标：把 452 个历史文件分成四类。

| 类别 | 处理 |
|---|---|
| 可提升 | 整理成正式知识、地图、playbook 或项目记录 |
| 可归档 | 保留为历史证据，但从入口隐藏 |
| 可丢弃 | 记录原因后删除或移到归档 |
| 待判断 | 放入 review queue，等待 Tony 决策 |

### Batch 3: 输出目录分流

目标：明确 `output-feishu/`、`output-public/`、`Nexus/` 的定位。

- `output-feishu/`: 保留为飞书发布 projection，不作为主知识。
- `output-public/`: 仅保留公开/半公开输出说明。
- `Nexus/`: 判断是否属于项目资产；若是 runtime 或中间数据，应迁出主库。

### Batch 4: 工具状态目录处理

目标：把工具 runtime 和会话缓存从主库语义里剥离。

候选目录：

- `.conversations/`
- `.workspaces/`
- `.claude/`
- `.claudian/`

处理前需要确认它们是否仍被工具依赖。不要在未确认前删除。

### Batch 5: 领域知识补齐

目标：让 `10-Knowledge/` 的领域层更均衡。

优先补齐：

- `AI/`
- `AI-Engineering/`
- `AI-Open-Source/`
- `International-Payments/`
- `Security/`

方式：每次只选择一个领域，补齐专题总览、主题索引、地图索引、学习路径和恢复笔记。

## Promotion Rule

从 working vault 或旧 inbox 提升内容时，必须满足：

1. 有明确来源或上下文。
2. 有适合的正式位置。
3. 不直接复制大量未消化材料。
4. 保留回链到源文件。
5. 更新最近的地图或专题总览。

## 当前下一步

1. 完成入口治理：总地图、仓库地图、当前主线、旧 AI Inbox README。
2. 建立 `00-Human-Inbox/` 到 working vault。
3. 对 `00-Inbox-AI/` 做一次只读盘点，先输出分类报告，不搬文件。
4. 从最有价值的历史 Hermes 文件开始做小批量 promotion。
