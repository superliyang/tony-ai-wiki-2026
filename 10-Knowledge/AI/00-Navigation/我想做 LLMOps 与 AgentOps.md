---
title: 我想做 LLMOps 与 AgentOps
type: guide
status: active
updated: 2026-04-03
---

# 我想做 LLMOps 与 AgentOps

## 先判断你在缺哪一层

- 你缺的是 `tracking`、`eval`、`release`、`registry`，还是 `observability`
- 你面对的是普通 LLM app，还是有 tool use、memory、approval 的 agent system
- 你是先要把实验跑通，还是要把线上治理起来
- 你需要的是平台选型，还是一条工程主线

## 最短阅读路径

1. [[AI 总控制塔|AI 总控制塔]]
2. [[AI-Learning/06-Topics/MLOps 与 LLMOps|MLOps 与 LLMOps]]
3. [[AI-Learning/07-Maps/MLOps 与 LLMOps 生态图|MLOps 与 LLMOps 生态图]]
4. [[AI-Engineering/07-Topics/Experiment Tracking|Experiment Tracking]]
5. [[AI-Engineering/07-Topics/Evaluation and Benchmarks|Evaluation and Benchmarks]]
6. [[AI-Engineering/07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]]
7. [[AI-Engineering/07-Topics/Model Registry and Deployment|Model Registry and Deployment]]
8. [[AI-Engineering/07-Topics/Online Evals、Human Feedback 与 Annotation|Online Evals、Human Feedback 与 Annotation]]
9. [[AI-Engineering/07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]]
10. [[AI-Engineering/07-Topics/LLMOps 平台对比：MLflow、W&B、Langfuse、Phoenix、Promptfoo|LLMOps 平台对比：MLflow、W&B、Langfuse、Phoenix、Promptfoo]]
11. [[AI-Engineering/08-Maps/MLOps 与 LLMOps 工程图|MLOps 与 LLMOps 工程图]]
12. [[AI-Engineering/07-Topics/Enterprise MLOps 与 LLMOps Vendor Tradeoffs|Enterprise MLOps 与 LLMOps Vendor Tradeoffs]]
13. [[AI-Engineering/08-Maps/Enterprise LLMOps Vendor Choice Map|Enterprise LLMOps Vendor Choice Map]]

## 关键平台样本

- [[AI-Learning/09-Systems/MLflow|MLflow]]
- [[AI-Learning/09-Systems/Weights & Biases Platform|Weights & Biases Platform]]
- [[AI-Learning/09-Systems/Langfuse|Langfuse]]
- [[AI-Learning/09-Systems/Arize Phoenix|Arize Phoenix]]
- [[AI-Learning/09-Systems/Promptfoo|Promptfoo]]

## 读完这条线后，你应该能自己回答

- 你到底是缺 `observability`，还是缺 `eval + release gate`
- `AgentOps` 相比 `LLMOps` 多出来的关键层到底是什么
- 哪类平台更适合你的当前阶段：tracking、pre-release eval、trace debugging，还是 enterprise governance
- 哪些东西必须成套看：dataset、trace、feedback、release，而不是只买一个“看板”

## 关联

- [[AI 决策导航|AI 决策导航]]
- [[什么时候该上 Langfuse、Phoenix、Promptfoo，什么时候 MLflow 与 W&B 更合适]]
- [[AI 问题导航|AI 问题导航]]
- [[AI-Open-Source/03-Projects/Langfuse|Langfuse]]
- [[AI-Open-Source/03-Projects/Promptfoo|Promptfoo]]
