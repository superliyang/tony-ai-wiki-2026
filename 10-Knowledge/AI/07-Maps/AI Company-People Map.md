---
title: AI Company-People Map
type: topic
status: draft
tags:
  - ai/map
created: 2026-03-01
updated: 2026-03-01
---

# AI Company-People Map

> 这一张图只看公司与关键人物的关系。

```mermaid
graph LR
    subgraph us["美国"]
        openai["[[OpenAI]]"]
        anthropic["[[Anthropic]]"]
        gdm["[[Google DeepMind]]"]
        meta["[[Meta AI]]"]
    end

    subgraph cn["中国"]
        deepseek["[[DeepSeek]]"]
        moonshot["[[Moonshot AI]]"]
        zhipu["[[Zhipu AI]]"]
    end

    subgraph people["关键人物"]
        sam["[[Sam Altman]]"]
        dario["[[Dario Amodei]]"]
        liang["[[梁文锋]]"]
        demis["[[Demis Hassabis]]"]
        yann["[[Yann LeCun]]"]
        yang["[[杨植麟]]"]
        zhang["[[张鹏]]"]
    end

    openai -->|关键人物| sam
    anthropic -->|关键人物| dario
    deepseek -->|关键人物| liang
    gdm -->|关键人物| demis
    meta -->|关键人物| yann
    moonshot -->|关键人物| yang
    zhipu -->|关键人物| zhang
```

## 怎么看这张图

- 这张图适合先建立“公司是谁在代表”的感知
- 后面如果你补更多公司，优先先把关键人物挂上来
- 如果一个人物跨多个组织活动，也可以继续扩展这里

## 返回

- [[AI Ecosystem Map]]
- [[AI Company-Models Map]]
- [[AI Topic-Papers Map]]
