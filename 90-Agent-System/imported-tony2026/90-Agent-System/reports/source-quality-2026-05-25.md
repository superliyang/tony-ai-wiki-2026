---
title: Source Quality Report - 2026-05-25
type: source-quality-report
status: generated
key: 2026-05-25
---

# Source Quality Report - 2026-05-25

## 来源质量排名

| source | items | high_value | avg_importance | warnings | top_topic |
| --- | ---: | ---: | ---: | ---: | --- |
| Anthropic News | 1 | 1 | 5.00 | 0 | AI-Engineering |
| DeepSeek News | 1 | 1 | 5.00 | 0 | AI-Engineering |
| Apache Flink Blog | 1 | 1 | 5.00 | 0 | Big-Data |
| GitHub Trending AI | 10 | 1 | 1.70 | 0 | Others |

## 建议

- 优先保留和调优 `Anthropic News`：本轮 high_value=1，avg=5.00。
- 本轮来源没有明显噪音，继续观察多轮趋势。

## Warnings

- openai-blog: RSS fetch failed: HTTPSConnectionPool(host='openai.com', port=443): Read timed out.

## 输入

- classified_items: 90-Agent-System/logs/semantic-analysis-2026-05-25.json
