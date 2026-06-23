---
title: MLOps 与 LLMOps
type: topic
status: learning
tags:
  - ai/topic
  - ai/mlops
  - ai/llmops
created: 2026-03-26
updated: 2026-04-14
---

# MLOps 与 LLMOps

## 它在讲什么

`MLOps` 关注的是：模型如何被实验、评测、注册、部署、监控，并能持续迭代。

`LLMOps` 则是在这条链路上增加了大模型时代的新资产：

- prompt
- eval dataset
- trace / session
- human feedback
- tool call / agent step
- online regression

所以更准确地说：

- `MLOps` 是模型生命周期工程
- `LLMOps` 是大模型应用生命周期工程
- `AgentOps` 是 `LLMOps` 往 action / memory / approval / multi-step execution 再推进一层

## 为什么现在必须单独学它

如果没有这层，你会很容易出现几种典型问题：

- 实验很多，但复现不了
- prompt 一改就退化，却不知道是哪版退化的
- 模型上线后用户体验变差，但线下 benchmark 看不出来
- 有 trace，没有可比较的 eval；有 eval，没有清晰 release gate
- 能跑 agent demo，但无法建立长期可运营的 feedback loop

## 一条最实用的主线

1. `Experiment Tracking`
2. `Evaluation and Benchmarks`
3. `Prompt Registry / Datasets / Evals`
4. `Model Registry and Deployment`
5. `Online Evals / Human Feedback / Annotation`
6. `LLMOps / AgentOps / Observability`

这条线的本质是：把模型、prompt、数据、trace 和 release 变成可治理资产。

## 这层里最值得记住的系统

- [[../09-Systems/MLflow|MLflow]]：open-source 的 tracking / registry / prompt registry 主线
- [[../09-Systems/Weights & Biases Platform|Weights & Biases Platform]]：实验跟踪、registry 与 Weave eval / trace 平台
- [[../09-Systems/Arize Phoenix|Arize Phoenix]]：LLM / agent tracing、eval 和 observability
- [[../09-Systems/Promptfoo|Promptfoo]]：pre-release eval、CI 和 red teaming
- [[../09-Systems/Langfuse|Langfuse]]：LLM / agent prompt、trace、score、dataset、release 对比
- [[../09-Systems/Ragas|Ragas]]：RAG 与 agent / tool-use 的 metric、dataset 与 testset generation 工具层
- [[../09-Systems/Inspect AI|Inspect AI]]：task / scorer / sandbox 分离的 agent eval framework
- [[../09-Systems/Giskard|Giskard]]：quality、RAG 与安全脆弱性测试更强的 test-suite 工具链

## 一条容易混淆但很重要的边界

- `Experiment tracking` 解决“这次为什么有效”
- `Evaluation` 解决“它到底是否更好”
- `Registry` 解决“哪个版本可以进下一阶段”
- `Observability` 解决“上线后它到底发生了什么”
- `Online eval / feedback` 解决“用户真实使用是否支持继续迭代”

很多团队的问题，不是没有某个工具，而是把这几层混成了一层。

## 推荐继续往下读

1. [[../../AI-Engineering/07-Topics/Experiment Tracking|Experiment Tracking]]
2. [[../../AI-Engineering/07-Topics/Evaluation and Benchmarks|Evaluation and Benchmarks]]
3. [[../../AI-Engineering/07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]]
4. [[../../AI-Engineering/07-Topics/Model Registry and Deployment|Model Registry and Deployment]]
5. [[../../AI-Engineering/07-Topics/Online Evals、Human Feedback 与 Annotation|Online Evals、Human Feedback 与 Annotation]]
6. [[../../AI-Engineering/07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]]
7. [[../07-Maps/MLOps 与 LLMOps 生态图|MLOps 与 LLMOps 生态图]]

## 关联

- [[Agent 平台]]
- [[AI 基础设施与 GPU Cloud]]
- [[Inference Serving]]
- [[../09-Systems/Langfuse|Langfuse]]
- [[../09-Systems/Ragas|Ragas]]
- [[../09-Systems/Inspect AI|Inspect AI]]
- [[../09-Systems/Giskard|Giskard]]
- [[../../AI-Engineering/07-Topics/Agent 效果评估：方法论、开源工具与判断框架|Agent 效果评估：方法论、开源工具与判断框架]]
- [[../../AI-Engineering/08-Maps/MLOps 与 LLMOps 工程图|MLOps 与 LLMOps 工程图]]
- [[../../Cloud-Native/02-Projects/OpenTelemetry|OpenTelemetry]]
- [[../../Cloud-Native/02-Projects/KServe|KServe]]

## 资料

- [MLflow Docs](https://mlflow.org/docs/latest/)
- [Weights & Biases Docs](https://docs.wandb.ai/)
- [Arize Phoenix Docs](https://arize.com/docs/phoenix)
- [Promptfoo Docs](https://www.promptfoo.dev/docs/intro/)
- [Langfuse Docs](https://langfuse.com/docs)
