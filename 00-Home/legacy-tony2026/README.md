# 学习知识库

> 一个按学习领域组织的 Obsidian vault。AI 学习只是其中一个专题区，而不是整个 vault 的唯一结构。

## 当前入口

- [[当前工作台|当前工作台]]
- [[AGENTS]]


## 设计原则

顶层先按“大类”划分，避免所有内容直接平铺在根目录。这样以后新增别的学习方向时，不需要推倒重来。

当前建议的层级是：

```text
.
├── README.md
├── AGENTS.md
├── 01-Areas/
│   ├── AI-Foundations/
│   ├── AI-Learning/
│   ├── AI-Engineering/
│   ├── AI-Applications/
│   ├── AI-Open-Source/
│   ├── Big-Data/
│   ├── Security/
│   ├── Cloud-Native/
│   ├── International-Payments/
│   ├── Skills-Gaming/
│   └── English-Learning/
├── 08-Shared-Templates/
└── 99-Archive/
```

其中：

- `01-Areas/` 放具体学习领域
- `AGENTS.md` 放仓库级协作与维护规则，供本地和云端 Codex 共用
- `08-Shared-Templates/` 以后可放跨领域通用模板
- `99-Archive/` 放长期归档内容

## 当前专题

当前已经建立的专题是：

- [[01-Areas/Cloud-Native/专题总览|Cloud-Native]]
- [[01-Areas/AI-Foundations/专题总览|AI-Foundations]]
- [[01-Areas/AI-Learning/专题总览|AI-Learning]]
- [[01-Areas/AI-Engineering/专题总览|AI-Engineering]]
- [[01-Areas/AI-Applications/专题总览|AI-Applications]]
- [[01-Areas/AI-Open-Source/专题总览|AI-Open-Source]]
- [[01-Areas/Big-Data/专题总览|Big-Data]]
- [[01-Areas/Security/专题总览|Security]]
- [[01-Areas/International-Payments/专题总览|International-Payments]]
- [[01-Areas/Skills-Gaming/专题总览|Skills-Gaming]]
- [[01-Areas/English-Learning/专题总览|English-Learning]]

后续你可以继续新增：

- `Product-Learning`
- `Management-Learning`
- `Finance-Learning`
- `Language-Learning`

每个专题内部再决定自己的实体、目录和模板。

## 为什么这样更稳

- AI 知识库只是一个专题，不会绑死整个 vault
- 以后新增其他学习方向时，结构仍然一致
- 每个专题都可以有自己的对象模型，不互相污染
- 顶层更干净，首页只负责导航，不负责承载全部知识细节
- 仓库级规则放在 `AGENTS.md`，这样本地和云端协作者会按同一套方法维护知识库

## 下一步

当前这个 vault 已经不只是 AI 学习库，而是一个多专题知识系统。

现在最成熟的几条主线包括：

1. `AI-Foundations`：历史、范式、基础概念
2. `AI-Learning`：公司、人物、模型、论文、主题、新闻
3. `AI-Engineering`：训练、框架、工具链、部署
4. `AI-Applications`：产品、工作流、行业落地
5. `AI-Open-Source`：开源项目、组织、模式、watchlist 和研究工作流
6. `Big-Data`：数据系统主干、数仓 / lakehouse、实时数据、数据平台与治理
7. `Security`：计算机安全全景、网络 / 客户端 / 应用 / 云 / 数据 / 合规与安全运营
8. `International-Payments`：支付业务、成功率、风控、拒付、资金与治理
9. `Skills-Gaming`：赛道、玩法、系统、公平性、AI-native 交付
10. `English-Learning`：主干原则、技巧例子、训练模板、材料包与人群路径

如果你想系统看 AI，建议的学习顺序是：

1. 先看 `AI-Foundations`
2. 再进入 `AI-Learning`
3. 然后过渡到 `AI-Engineering`
4. 最后看 `AI-Applications`

如果你想切到其他专题，现在也可以从：

1. `Cloud-Native`
2. `Big-Data`
3. `Security`
4. `International-Payments`
5. `Skills-Gaming`
6. `English-Learning`
7. 然后顺着各自的 `专题总览 -> 问题/决策入口 -> 索引/地图 -> 学习进度/恢复笔记`

## 云端协作

如果你在云端使用 Codex 来维护这个仓库：

1. 先读 [[AGENTS]]
2. 再进入相关专题的 `专题总览`
3. 如果任务涉及结构调整，优先补导航层、地图层和恢复层
4. 默认不要改 `.obsidian/*` 和 `.p_obsidian/*`
