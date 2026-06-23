---
title: "2026-06 AI Open Source Watchlist 刷新"
created: 2026-06-18
updated: 2026-06-18
status: learning
type: map
domain: ai-open-source
as_of: 2026-06-18
tags:
  - knowledge
  - ai-open-source
  - watchlist
  - content-refresh
---

# 2026-06 AI Open Source Watchlist 刷新

这页记录第一批内容刷新中，AI Open Source Watchlist 的更新判断。

## Watchlist 判断

| Project | 当前信号 | 建议动作 |
|---|---|---|
| Unsloth | 继续高频更新，Studio 化，支持更多模型和训练场景 | 进入正式项目卡，连接 training / local lab / fine-tuning pattern |
| vLLM | 高频 release，Q2 roadmap 聚焦生产 serving、硬件、RL rollout、omni workload | 保持 Watchlist，连接 deployment / serving pattern |
| LangGraph | 仍是 stateful agent runtime 重要样本，release 和 issue 活跃 | 保持 Watchlist，连接 agent runtime pattern |
| Langfuse | agent observability / eval / MCP evaluator 正在增强 | 保持 Watchlist，连接 eval / observability pattern |
| Qwen Code / Qwen3-Coder | open-source coding agent + code model 路线值得跟 | 新增候选项目卡，连接 China AI / coding agent pattern |

## 项目进入 Watchlist 的理由

| Reason | 项目 |
|---|---|
| 改变本地训练和 fine-tuning 工作流 | Unsloth |
| 改变生产 serving 和 inference stack | vLLM |
| 改变 agent runtime 设计 | LangGraph |
| 改变 eval / observability / release gate | Langfuse |
| 改变 open coding agent 与模型协同路线 | Qwen Code / Qwen3-Coder |

## Source Links

- Unsloth releases: https://github.com/unslothai/unsloth/releases
- Unsloth repository: https://github.com/unslothai/unsloth
- Unsloth Studio announcement: https://github.com/unslothai/unsloth/discussions/4370
- vLLM releases: https://github.com/vllm-project/vllm/releases
- vLLM Q2 roadmap: https://github.com/vllm-project/vllm/issues/39749
- LangGraph releases: https://github.com/langchain-ai/langgraph/releases
- Langfuse changelog: https://langfuse.com/changelog
- Qwen Code GitHub: https://github.com/QwenLM/qwen-code
- Qwen3-Coder GitHub: https://github.com/QwenLM/Qwen3-Coder

## Next Actions

| Priority | Action | Target |
|---|---|---|
| P1 | 建立 Unsloth 项目卡 | [[10-Knowledge/AI-Open-Source/03-Projects/项目索引]] |
| P1 | 建立 Qwen Code 项目卡 | [[10-Knowledge/AI-Open-Source/03-Projects/项目索引]] |
| P1 | 更新 serving category | [[10-Knowledge/AI-Open-Source/01-Categories/分类索引]] |
| P2 | 抽取 Agent Eval / Observability pattern | [[10-Knowledge/AI-Open-Source/04-Patterns/模式索引]] |
