---
title: Source Quality Report - 2026-05-30
type: source-quality-report
status: generated
key: 2026-05-30
---

# Source Quality Report - 2026-05-30

## 来源质量排名

| source | items | high_value | avg_importance | warnings | top_topic |
| --- | ---: | ---: | ---: | ---: | --- |
| Anthropic News | 1 | 1 | 5.00 | 0 | AI-Engineering |
| DeepSeek News | 1 | 1 | 5.00 | 0 | AI-Engineering |
| Apache Flink Blog | 1 | 1 | 5.00 | 0 | Big-Data |
| GitHub Trending AI | 10 | 1 | 2.00 | 0 | Others |
| OpenCode Releases | 1 | 0 | 1.00 | 0 | Others |

## 建议

- 优先保留和调优 `Anthropic News`：本轮 high_value=1，avg=5.00。
- 观察 `OpenCode Releases`：warnings=0，high_value=0。

## Warnings

- arxiv-ai-agents: RSS fetch failed: HTTPSConnectionPool(host='export.arxiv.org', port=443): Read timed out. (read timeout=20)

## 输入

- classified_items: 90-Agent-System/logs/semantic-analysis-2026-05-30.json
