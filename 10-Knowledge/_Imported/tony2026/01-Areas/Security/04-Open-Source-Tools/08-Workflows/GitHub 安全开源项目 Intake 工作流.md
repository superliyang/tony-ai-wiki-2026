---
title: GitHub 安全开源项目 Intake 工作流
type: workflow
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# GitHub 安全开源项目 Intake 工作流

## 目标

把 GitHub 安全工具从“看到一个 repo 就收藏”变成可持续研究流程。

## Step 1：初筛

只收满足至少两个条件的项目：

- 能代表一个安全工作流。
- 有明确学习价值。
- 有活跃维护或稳定生态。
- 能进入实验室、CI/CD 或平台落地。
- 和已有项目有明显差异。

## Step 2：分类

放入一个主分类：

- 攻击面发现与资产测绘
- Web、API 与应用安全测试
- DevSecOps 与供应链安全
- 云原生、Kubernetes 与 IaC 安全
- 身份、密钥、证书与策略
- SecOps、检测工程与威胁情报
- DFIR、逆向与恶意样本分析
- 授权攻防、AD 与对抗模拟
- 加固、隐私与网络防护
- AI 安全与 LLM 红队

## Step 3：评分

| 维度 | 问题 |
|---|---|
| learning_fit | 是否能帮助理解一个安全能力？ |
| local_fit | 是否适合本地实验？ |
| mac_fit | 是否适合当前 Mac 环境？ |
| production_fit | 是否适合进入团队/企业流程？ |
| risk | 是否有误用、误伤或合规风险？ |

## Step 4：沉淀

- 普通项目：先放 [[../03-Projects/项目索引|项目索引]]。
- 核心样本：建立项目卡。
- 抽象复用：更新 [[../04-Patterns/模式索引|模式索引]]。
- 值得持续看：加入 [[../09-Watchlist/重点 Watchlist|重点 Watchlist]]。

## Step 5：实验

每个核心项目都应该有下一步实验：

- 最小安装。
- 最小输入。
- 最小输出。
- 如何接入工单/CI/SIEM/GRC。
- 如何避免误用和误伤。

