---
title: AI 五大专题审察与组织
type: map
status: learning
tags:
  - ai/maps
created: 2026-03-27
updated: 2026-04-03
---

# AI 五大专题审察与组织

## 这次审察的结论

- AI 相关 area 现在已经从四个扩到五个：`AI-Foundations -> AI-Learning -> AI-Open-Source -> AI-Engineering -> AI-Applications`
- `AI-Open-Source` 不适合硬塞进现有任一专题，因为它横跨本地 runtime、serving、agent runtime、memory、eval 与 AI platform
- 现在五大专题已经有了统一控制塔：一个审察说明页、一个 `Canvas` 白板导航、一个 `Base` 数据库导航
- 原先四大专题的分工依旧成立，只是多了一层“开源项目、组织、模式、watchlist”控制塔

## 五大专题怎么分工

### 1. AI-Foundations

- 负责历史、范式、数学直觉与经典问题
- 它回答的是：`为什么现代 AI 会变成今天这样`
- 入口：[[../../AI-Foundations/专题总览|AI-Foundations]]、[[../../AI-Foundations/01-History/历史索引|历史索引]]、[[../../AI-Foundations/02-Foundations/基础索引|基础索引]]、[[../../AI-Foundations/03-Paradigms/范式索引|范式索引]]、[[../../AI-Foundations/04-Papers/经典论文索引|经典论文索引]]、[[../../AI-Foundations/06-Maps/地图索引|地图索引]]

### 2. AI-Learning

- 负责公司、人物、模型、系统、论文、现代主题与前沿动态
- 它回答的是：`现在 AI 世界里有哪些关键对象与主线`
- 入口：[[../专题总览|AI-Learning]]、[[../06-Topics/AI 主题索引|AI 主题索引]]、[[../09-Systems/系统索引|系统索引]]、[[地图索引]]

### 3. AI-Open-Source

- 负责开源项目、开源组织、工程模式、watchlist 与研究 workflow
- 它回答的是：`哪些开源项目值得持续研究，它们代表什么工程模式`
- 入口：[[../../AI-Open-Source/专题总览|AI-Open-Source]]、[[../../AI-Open-Source/01-Categories/分类索引|分类索引]]、[[../../AI-Open-Source/03-Projects/项目索引|项目索引]]、[[../../AI-Open-Source/04-Patterns/模式索引|模式索引]]、[[../../AI-Open-Source/06-Maps/地图索引|地图索引]]

### 4. AI-Engineering

- 负责训练、推理、部署、MLOps / LLMOps、AI Security、Agent 平台与工程治理
- 它回答的是：`系统是怎么被真正构建、治理与放大的`
- 入口：[[../../AI-Engineering/专题总览|AI-Engineering]]、[[../../AI-Engineering/07-Topics/主题索引|主题索引]]、[[../../AI-Engineering/08-Maps/地图索引|地图索引]]

### 5. AI-Applications

- 负责行业、产品、工作流、案例、组织 rollout 与 vendor choice
- 它回答的是：`AI 怎么进入业务与组织`
- 入口：[[../../AI-Applications/专题总览|AI-Applications]]、[[../../AI-Applications/05-Topics/主题索引|主题索引]]、[[../../AI-Applications/06-Maps/地图索引|地图索引]]

## 建议怎么用新的导航层

1. 如果你只想先有一个全局 AI 入口，先开 [[../../AI 总控制塔|AI 总控制塔]]
2. 如果你还不确定一个主题该放在哪个 area，先看这页
3. 如果你想快速浏览结构关系，打开 [[AI 五大专题导航.canvas|AI 五大专题导航（Canvas）]]
4. 如果你想像数据库一样筛选总览、索引、地图和状态页，打开 [[AI 五大专题导航.base|AI 五大专题导航（Base）]]
5. 如果你在研究具体开源项目，先跳去 `AI-Open-Source`
6. 如果你已经明确自己要学哪条线，再回到对应 area 的 `专题总览` 继续深入

## 推荐的五条跨专题学习路线

### 大模型主线

`AI-Foundations -> AI-Learning -> AI-Engineering -> AI-Applications`

### Agent 主线

`AI-Learning -> AI-Open-Source -> AI-Engineering -> AI-Applications`

- 先看对象与系统样本
- 再看代表开源 runtime、memory、eval 与 harness 项目
- 再读 runtime、security、approval、eval、memory 与 coordination
- 最后看 workflow、vendor choice 与 assistant-to-runtime migration

### 开源栈主线

`AI-Learning -> AI-Open-Source -> AI-Engineering`

- 先建立领域对象感
- 再用项目、组织、模式和 watchlist 建立判断力
- 最后把这些判断翻译成训练、推理、平台与治理工程

### AI Security 主线

`AI-Learning -> AI-Open-Source -> AI-Engineering -> AI-Applications`

- 先理解 threat map 和系统对象层
- 再看 guardrails、eval、runtime、plugin、memory 相关开源工具
- 再进入 threat modeling、tool safety、supply chain 与 red teaming
- 最后看高信任行业里的组织落地

### 企业 AI 落地主线

`AI-Learning -> AI-Open-Source -> AI-Engineering -> AI-Applications`

- 先理解 systems、frontier dynamics、infra 与 MLOps / LLMOps 生态
- 再通过开源项目理解替代路线和工程模式
- 再读平台选型、部署模型、observability 与 security
- 最后在行业、workflow、case study 与 rollout 模板层做判断

## 当前仍值得继续补的地方

- `AI-Foundations` 仍然可以继续补人物线与更完整的双语 glossary
- `AI-Learning` 的人物层仍然比公司、模型和系统层更薄一些
- `AI-Open-Source` 现在完成了第一批控制塔骨架，后续应继续补第二批项目与 adopt case
- `AI-Engineering` 的 AI Security 与 Enterprise LLMOps 还可以继续加更多案例层
- `AI-Applications` 的产品层现在可用，但仍然是 selective，而不是 exhaustive

## 关联资产

- [[../../AI 总控制塔|AI 总控制塔]]
- [[AI 五大专题导航.canvas|AI 五大专题导航（Canvas）]]
- [[AI 五大专题导航.base|AI 五大专题导航（Base）]]
- [[AI Ecosystem Map]]
- [[../../AI-Foundations/专题总览|AI-Foundations]]
- [[../专题总览|AI-Learning]]
- [[../../AI-Open-Source/专题总览|AI-Open-Source]]
- [[../../AI-Engineering/专题总览|AI-Engineering]]
- [[../../AI-Applications/专题总览|AI-Applications]]
