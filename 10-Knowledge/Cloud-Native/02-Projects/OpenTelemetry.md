---
title: OpenTelemetry
type: project
status: learning
tags:
  - cloud-native/project
  - cloud-native/opentelemetry
created: 2026-03-24
updated: 2026-03-24
---

# OpenTelemetry

## 定位

`OpenTelemetry` 是云原生 observability 里非常关键的标准化层。它更像一套 vendor-neutral framework 和 specification，而不是单一后端产品。

## 它解决什么问题

- 统一 traces、metrics、logs 的采集与传输思路
- 降低 instrumentation 与 observability backend 的耦合
- 为跨系统、跨团队、跨 vendor 的 telemetry 提供共同语言

## 为什么它重要

如果说 Prometheus 更像 metrics 侧的重要项目，那么 OpenTelemetry 更像“可观测性采集与语义标准层”。它让团队不必把应用埋点完全绑死在单一平台上。

## 学习重点

- traces / metrics / logs 三类 signal 的关系
- SDK、Collector、Exporter 分别在做什么
- 为什么 observability 在云原生里越来越像一条数据管线，而不是单点监控工具

## 来源

- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
- [OpenTelemetry Overview](https://opentelemetry.io/docs/specs/otel/overview/)
- [OpenTelemetry](https://opentelemetry.io/)

## 相关

- [[../03-Topics/可观测性|可观测性]]
- [[Prometheus]]
