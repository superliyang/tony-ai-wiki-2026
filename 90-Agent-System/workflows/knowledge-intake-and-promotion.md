---
title: "Knowledge Intake And Promotion"
created: 2026-06-16
updated: 2026-06-16
status: active
tags:
  - workflow
  - knowledge-promotion
  - hermes
  - codex
---

# Knowledge Intake And Promotion

这条 workflow 定义从 working vault staging 到主知识库正式目录的完整链路。

核心原则：

```text
Hermes 负责发现、调研、整理候选和执行重活。
Codex 负责判断内容类型、保护正文、对齐知识体系、提升到主库。
Tony 负责最终方向、品味和高价值判断。
```

## Source Surfaces

| 来源 | 默认位置 | 说明 |
|---|---|---|
| Hermes 调研 | `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/10-Generated/` | 自动调研、repo analysis、digest、草稿 |
| Hermes 待审 | `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/20-Review-Queue/pending/` | 建议 promote、defer、discard、publish 的候选 |
| Tony 手动材料 | `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/00-Human-Inbox/` | 手动摘录、链接、想法、待加工资料 |
| 历史 AI staging | `00-Inbox-AI/` | 旧系统遗留，只读盘点和小批次提升 |
| 旧库迁出内容 | `10-Knowledge/*` formal domains | 旧知识已进入正式领域目录 |

## Domain Routing

先判断候选内容属于已知领域还是未知领域。

### 已知领域扩展

如果内容能落入现有正式领域，优先进入该领域体系：

| 内容类型 | 优先目标 |
|---|---|
| 开源项目 | `10-Knowledge/AI-Open-Source/03-Projects/` |
| 开源组织 | `10-Knowledge/AI-Open-Source/02-Organizations/` |
| 开源工程模式 | `10-Knowledge/AI-Open-Source/04-Patterns/` |
| AI 工程主题 | `10-Knowledge/AI-Engineering/` |
| 可执行方法 | `30-Playbooks/` |
| 项目状态 / 构建记录 | `40-Projects/` |
| Agent 规则 / 工作流 | `90-Agent-System/` |

不要因为材料来自 Hermes 就放入 AI 协作区。判断依据是内容本体，不是来源。

### 未知领域扩展

如果内容不属于现有领域，先不要直接创建完整新领域。先创建一个 domain proposal：

```text
/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/20-Review-Queue/pending/YYYY-MM-DD-domain-proposal.md
```

proposal 至少包含：

- proposed_domain：建议领域名；
- why_now：为什么现在值得开；
- relation_to_existing_domains：和现有领域是否重叠；
- seed_sources：来源材料；
- first_5_notes：最小起步笔记；
- risk：是否会造成目录膨胀或重复。

只有 Tony / Codex 接受后，才在主库建立新领域入口。

## Promotion Steps

### 1. 从 staging / 收件箱读取候选内容

Codex 读取 working vault 的 `10-Generated/`、`20-Review-Queue/pending/`、`00-Human-Inbox/`，必要时读取历史 `00-Inbox-AI/` 和正式领域目录。

### 2. 判断内容类型

每个候选必须先归类：

| type | 说明 |
|---|---|
| `project` | 开源项目、产品、工具 |
| `organization` | 组织、社区、公司 |
| `category` | 稳定项目类别 |
| `pattern` | 可复用工程模式 |
| `case-study` | 组合案例或 adoption 案例 |
| `topic` | 抽象主题 / 概念 |
| `playbook` | 可执行方法 |
| `map` | 导航、对比、关系图 |
| `domain-proposal` | 未知领域提案 |
| `publish-package` | 可输出到飞书的发布包 |

### 3. 正文保护

主库正文不要整包复制 AI 报告。

Codex 应做：

- 保留来源链接；
- 提炼稳定事实和判断；
- 标记不确定点；
- 删除运行日志、过程噪音和 prompt 痕迹；
- 把长报告拆成项目卡、模式卡、地图或 playbook。

### 4. 补 frontmatter

正式笔记必须至少包含：

```yaml
---
title:
created:
updated:
status: active|learning|seed
type: project|organization|category|pattern|case-study|topic|playbook|map
domain:
source:
---
```

AI-Open-Source 项目卡额外字段：

```yaml
category:
organization:
repo:
local_fit:
mac_fit:
production_fit:
learning_fit:
watchlist:
```

### 5. 加知识地图链接

每个提升笔记至少链接一个上层入口：

- 领域专题总览；
- 分类索引；
- 项目索引；
- 模式索引；
- 地图索引；
- 相关 playbook 或 case study。

### 6. 加系列导航

如果候选属于一个系列，必须补系列导航：

- 开源项目系列：项目页 ↔ 分类 ↔ 组织 ↔ 模式 ↔ Watchlist；
- 学习系列：主题页 ↔ 学习路径 ↔ 恢复笔记；
- 发布系列：source note ↔ `output-feishu/` ↔ Feishu record；
- 项目系列：项目 README ↔ 决策 ↔ 下一步 ↔ 阶段复盘。

### 7. 移动到正式目录

移动或创建正式笔记时，只移动 bounded slice。

未被提升的原始材料继续留在 working vault 或历史 inbox。

### 8. 更新 MOC / Dataview 所需字段

更新最近的 MOC：

- `专题总览.md`
- `项目索引.md`
- `分类索引.md`
- `模式索引.md`
- `Watchlist 索引.md`
- 相关地图或 Base 文件

Dataview 字段要稳定，不要每个笔记发明新字段。

### 9. 记录日志

每次 promotion 写一条日志：

```text
/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/40-Logs/promotions/YYYY-MM-DD-topic.md
```

日志包含：

- source；
- promoted_files；
- updated_maps；
- skipped_material；
- open_questions；
- next_action。

## Feishu Delegation

费力但低判断风险的发布执行交给 Hermes：

1. Codex 或 Tony 先确认某份内容可以发布。
2. Codex 生成或确认 `output-feishu/` 下的 publish-ready Markdown。
3. Hermes 调用 Feishu CLI 发布。
4. Hermes 把发布记录写入 working vault `40-Logs/feishu-publishing/`。
5. Codex 只在需要时把 Feishu URL 回链到主库源笔记。

Hermes 不应从 raw staging 直接发布到飞书。
