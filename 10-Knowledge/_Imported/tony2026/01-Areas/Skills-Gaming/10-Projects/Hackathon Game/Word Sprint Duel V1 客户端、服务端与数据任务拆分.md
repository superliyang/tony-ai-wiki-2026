---
title: Word Sprint Duel V1 客户端、服务端与数据任务拆分
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# Word Sprint Duel V1 客户端、服务端与数据任务拆分

## Client

### 必做

- start screen
- tutorial / onboarding
- word duel 主界面
- result screen
- rematch / next entry

### 客户端状态

- `idle`
- `tutorial`
- `playing`
- `submitting`
- `result`
- `error`

### 客户端最小模块

- UI shell
- duel state machine
- score calculator
- local event emitter
- API client

## Backend

### 必做接口

- `GET /tournament/current`
- `POST /match/submit-score`
- `POST /events`
- `GET /result/{match_id}`
- `GET /eligibility`

### 服务端最小职责

- 给客户端一个可解释的 tournament shell
- 接收并校验 score payload
- 返回结果与解释字段
- 记录事件与错误分支

## Data / Event Layer

### 关键事件

- `session_start`
- `tutorial_complete`
- `match_start`
- `match_end`
- `score_submitted`
- `result_received`
- `rematch_clicked`
- `unsupported_region_seen`
- `submit_error`

### 最小分析问题

- 首局完成率是多少
- result screen 之前流失有多少
- 有没有人愿意 rematch
- 是否存在异常 score 或提交流程失败

## AI 协作切分建议

### 交给 AI 编程助手的 chunk

1. `client UI shell + state machine`
2. `mock API contracts`
3. `event schema + logging`
4. `result explanation rendering`
5. `tutorial / copy / QA checklist`

### 必须人工把关的 chunk

- score 规则
- fairness 解释
- scope cuts
- result feel

## 关联

- [[Word Sprint Duel V1 技术选型与主机方案]]
- [[Word Sprint Duel V1 实现蓝图]]
- [[Word Sprint Duel V1 AI 协作任务包]]
