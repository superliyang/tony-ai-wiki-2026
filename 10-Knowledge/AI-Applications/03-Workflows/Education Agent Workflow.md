---
title: Education Agent Workflow
type: workflow
status: learning
tags:
  - ai/workflow
  - ai/education
inputs:
  - teaching objective
  - curriculum or lesson context
  - student or classroom constraints
steps:
  - clarify educational goal and boundary
  - retrieve teaching materials and policy context
  - draft learning support artifact or feedback
  - route through teacher review
  - deliver bounded output and record adjustments
tools:
  - curriculum repository
  - classroom materials
  - school policy documents
  - feedback and content generation tools
outputs:
  - lesson draft
  - feedback draft
  - classroom support artifact
evaluation:
  - teacher time saved
  - feedback quality
  - student safety and policy compliance
risks:
  - bypassing teacher judgment
  - weak age or pedagogy alignment
  - academic integrity issues
related_products:
  - ChatGPT Agent 产品卡
created: 2026-03-23
updated: 2026-03-23
---

# Education Agent Workflow

## 简介

教育 workflow 的关键不是让 agent 直接“替老师教”，而是让它进入老师已经存在的教学准备、反馈和支持流程里，放大教师能力而不是绕过教师。

## 步骤

1. 明确教学目标、年级边界和输出用途
2. 检索课程资料、已有教案、学校政策与评价标准
3. 生成 lesson plan、反馈草稿、练习材料或 support artifact
4. 由教师审核、调整语气与难度，并确认是否适合当前学生群体
5. 发布到课堂或学生支持流程，并记录后续反馈

## 工具链

- curriculum repository
- school or district policy docs
- lesson planning tools
- controlled content generation and review interfaces

## 评估

- 是否节省教师准备与反馈时间
- 生成内容是否符合教学目标与年龄适配
- 是否提升反馈一致性与课堂支持质量
- 是否在不损害学术诚信的前提下提升学习支持

## 风险

- 让学生绕过思考过程，直接获得答案
- 生成内容与 pedagogy 或校方政策不一致
- 对敏感年龄段缺少 guardrails
- 把 teacher-in-the-loop 错当成可选项

## 最适合的产品

- [[../02-Products/ChatGPT Agent 产品卡|ChatGPT Agent 产品卡]]

## 代表案例

- [[../04-Case-Studies/MagicSchool Education Copilot|MagicSchool Education Copilot]]
- [[../04-Case-Studies/California State University ChatGPT Edu Rollout|California State University ChatGPT Edu Rollout]]

## 相关

- [[../01-Industries/Education Agents|Education Agents]]
- [[../05-Topics/Agent Adoption and Change Management|Agent Adoption and Change Management]]
- [[../../AI-Engineering/07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]
