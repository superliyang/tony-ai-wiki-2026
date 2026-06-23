---
title: Prometheus
type: project
status: learning
tags:
  - cloud-native/project
  - cloud-native/prometheus
created: 2026-03-24
updated: 2026-03-24
---

# Prometheus

## 定位

`Prometheus` 是云原生生态里最重要的 monitoring 与 alerting 项目之一，尤其适合 metrics 驱动的系统可观测性。

## 它解决什么问题

- 采集和存储 time-series metrics
- 基于规则进行 alerting
- 用统一查询语言观察系统状态

## 为什么它重要

在云原生环境里，workload 数量多、变化快、实例生命周期短，传统静态监控方式很快不够用。Prometheus 的数据模型和生态，使它成为 metrics 这一层的事实标准之一。

## 学习重点

- metrics 与 logs / traces 的边界
- time-series 和 labels 为什么适合云原生场景
- alerting 为什么是 observability 闭环的一部分，而不是单独存在

## 来源

- [Prometheus](https://prometheus.io/)
- [Getting started with Prometheus](https://prometheus.io/docs/tutorials/getting_started/)
- [Prometheus FAQ](https://prometheus.io/docs/introduction/faq/)

## 相关

- [[../03-Topics/可观测性|可观测性]]
- [[OpenTelemetry]]
