---
title: Source Quality Report - 2026-W22
type: source-quality-report
status: generated
key: 2026-W22
---

# Source Quality Report - 2026-W22

## 来源质量排名

| source | items | high_value | avg_importance | warnings | top_topic |
| --- | ---: | ---: | ---: | ---: | --- |
| CISA Known Exploited Vulnerabilities | 10 | 10 | 4.20 | 0 | Security |
| AWS Security Blog | 6 | 6 | 4.50 | 0 | Security |
| LangGraph Releases | 3 | 3 | 4.00 | 1 | AI-Open-Source |
| OpenCode Releases | 5 | 3 | 3.20 | 0 | AI-Engineering |
| Anthropic News | 1 | 1 | 5.00 | 0 | AI-Engineering |
| DeepSeek News | 1 | 1 | 5.00 | 0 | AI-Engineering |
| Apache Flink Blog | 1 | 1 | 5.00 | 0 | Big-Data |
| Cloudflare Blog | 2 | 1 | 3.50 | 0 | Security |
| LiteLLM Releases | 5 | 1 | 3.20 | 0 | AI-Open-Source |
| OpenAI Blog | 8 | 1 | 2.62 | 0 | Others |
| GitHub Trending AI | 10 | 1 | 1.70 | 0 | Others |
| CISA Alerts | 1 | 0 | 3.00 | 0 | Security |

## 建议

- 优先保留和调优 `CISA Known Exploited Vulnerabilities`：本轮 high_value=10，avg=4.20。
- 观察 `LangGraph Releases`：warnings=1，high_value=3。
- 观察 `CISA Alerts`：warnings=0，high_value=0。

## Warnings

- arxiv-ai-agents: RSS fetch failed: HTTPSConnectionPool(host='export.arxiv.org', port=443): Read timed out. (read timeout=20)
- github-langgraph-releases: GitHub releases fetch failed, using cached items from previous logs: HTTPSConnectionPool(host='api.github.com', port=443): Max retries exceeded with url: /repos/langchain-ai/langgraph/releases (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)')))

## 输入

- classified_items: 90-Agent-System/logs/semantic-analysis-2026-W22.json
