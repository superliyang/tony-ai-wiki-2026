---
title: 模型行为治理：Model Spec、Preparedness、Transparency 与 AI Act
type: topic
status: learning
tags:
  - ai/topic
  - ai/governance
  - ai/safety
  - ai/policy
created: 2026-04-13
updated: 2026-04-13
---

# 模型行为治理：Model Spec、Preparedness、Transparency 与 AI Act

## 这个主题是什么

这一页讨论的是：当一个 frontier 模型不只是实验对象，而是要被部署进产品、平台、企业和监管环境时，`模型行为` 本身如何被约束、解释、披露和放行。

它关心的不是单个 guardrail 规则，而是更上层的几种资产：

- `Model Spec / Constitution`
- `Preparedness / Safeguards reporting`
- `Transparency / trust reporting`
- `external obligations`，例如 `AI Act`

## 为什么这个主题在 2025-2026 变重要

因为 frontier AI 的治理界面正在公开化、版本化和制度化。

最近这波变化最值得记住的是：

- 模型行为准则开始被显式公开
- 上线门槛开始以 preparedness / safeguards 的形式写出来
- transparency 不再是一张 system card，而是持续资产
- GPAI 的外部义务开始有明确日期和边界

## 你先要抓住什么

- `app guardrails` 和 `model behavior governance` 不是一回事
- `usage policy` 和 `Model Spec / Constitution` 不是一回事
- `system card` 和 `Preparedness / Safeguards reporting` 也不是一回事

## 四层最实用的分法

### 1. `behavior layer`

模型应该怎么默认表现、如何处理 operator / user / system / other agent 的关系。

代表资产：

- [OpenAI Model Spec](https://model-spec.openai.com/)
- [Claude’s Constitution — January 2026](https://www-cdn.anthropic.com/9214f02e82c4489fb6cf45441d448a1ecd1a3aca/claudes-constitution.pdf)

### 2. `preparedness layer`

模型能力强到什么程度时，需要什么级别的 safeguards 才能部署。

代表资产：

- [OpenAI Preparedness Framework update](https://openai.com/index/updating-our-preparedness-framework/)

### 3. `transparency layer`

哪些行为、评测、风险和缓解措施会被长期公开表达。

代表资产：

- [Anthropic Transparency](https://www.anthropic.com/transparency)

### 4. `external obligation layer`

外部监管如何给 GPAI providers 带来明确义务。

代表资产：

- [EU AI Act GPAI guidelines](https://digital-strategy.ec.europa.eu/en/library/guidelines-scope-obligations-providers-general-purpose-ai-models-under-ai-act)

## 为什么这条线不能被并进 AI Safety 或 AI Security 就算了

因为它既不是纯 `safety`，也不是纯 `security`。

它更像：

- `behavior governance`
- `deployment governance`
- `reporting governance`
- `regulatory governance`

也就是说，它不是替代 `AI Safety` 或 `AI Security`，而是站在它们之上，把风险语言收进组织和制度语言。

## 这条线最容易混淆的几个边界

### `Model Spec / Constitution` vs `Usage Policy`

- 前者更像行为设计和行为原则
- 后者更像平台使用边界与禁止事项

### `Preparedness` vs `System Card`

- `System Card` 更像对模型或系统的说明和评测摘要
- `Preparedness` 更像能力阈值、风险等级和 deploy/no-deploy 的门槛语言

### `Transparency` vs `Marketing`

- 真正的 transparency 资产会持续暴露风险语言和治理结构
- 不是只发布优点与案例

### `AI Act` vs 内部自律

- 内部框架可以决定组织如何表达和自约束
- 监管义务则会直接影响外部合规、采购、部署和法律边界

## 为什么它会影响企业判断

如果你在做企业 AI、平台 AI 或 agent 产品，未来会越来越常被问到：

- 模型行为边界怎么定义
- 遇到高风险能力时如何 gating
- 有哪些公开治理资产可以让客户审视
- 对 GPAI 的外部义务如何影响部署与采购

这类问题如果没有专门的知识框架，就很容易退化成：

- “我们有很多 guardrails”
- “我们很重视安全”

但这已经不够了。

## 学这页最该记住什么

- 模型治理的公开界面已经开始成型
- frontier deployment 的语言正在从 benchmark 转向 `behavior + safeguards + transparency + obligations`
- 这条线现在已经值得进入 AI 知识主干，而不是继续放在边角

## 推荐继续往下读

- [[AI Safety 与 AI Security]]
- [[AI Safety]]
- [[AI Security]]
- [[安全治理线：AI Safety、AI Security、Prompt Injection、Approval、Audit 与 Release Gate]]
- [[产品落地线：Model、Workflow、Case Study、Rollout、ROI 与 Governance]]
- [[../11-Recent-Supplements/2025-2026 AI 治理补线：Model Spec、Preparedness、Transparency 与 AI Act|2025-2026 AI 治理补线：Model Spec、Preparedness、Transparency 与 AI Act]]

## 相关

- [[Prompt Injection 与 Jailbreaks]]
- [[Agent]]
- [[Deep Research 与 Research Agents]]
