---
title: Source Quality Report - 2026-05-28
type: source-quality-report
status: generated
key: 2026-05-28
---

# Source Quality Report - 2026-05-28

## 来源质量排名

| source | items | high_value | avg_importance | warnings | top_topic |
| --- | ---: | ---: | ---: | ---: | --- |
| arXiv AI Agents | 3 | 3 | 4.33 | 0 | AI-Engineering |
| GitHub Trending AI | 10 | 2 | 2.00 | 0 | Others |
| Anthropic News | 1 | 1 | 5.00 | 0 | AI-Engineering |
| DeepSeek News | 1 | 1 | 5.00 | 0 | AI-Engineering |
| Apache Flink Blog | 1 | 1 | 5.00 | 0 | Big-Data |
| Cloudflare Blog | 2 | 0 | 2.00 | 0 | AI-Engineering |

## 建议

- 优先保留和调优 `arXiv AI Agents`：本轮 high_value=3，avg=4.33。
- 观察 `Cloudflare Blog`：warnings=0，high_value=0。

## Warnings

- github-langgraph-releases: GitHub releases fetch failed: HTTPSConnectionPool(host='api.github.com', port=443): Max retries exceeded with url: /repos/langchain-ai/langgraph/releases (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)')))
- github-opencode-releases: GitHub releases fetch failed: HTTPSConnectionPool(host='api.github.com', port=443): Max retries exceeded with url: /repos/sst/opencode/releases (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)')))

## 输入

- classified_items: 90-Agent-System/logs/semantic-analysis-2026-05-28.json
