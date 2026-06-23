---
title: 安全工程与 DevSecOps
type: topic
status: active
domain: Security
created: 2026-04-29
updated: 2026-04-29
---

# 安全工程与 DevSecOps

## 定位

安全工程与 DevSecOps 的目标是把安全控制嵌入软件生命周期，而不是上线前靠安全团队“拦一下”。

它回答：

- 安全需求什么时候进入设计
- 代码什么时候被扫描
- 依赖什么时候被检查
- 镜像什么时候被签名
- 风险什么时候阻断发布
- 例外如何审批和过期

## 生命周期控制点

1. 需求阶段：安全需求、隐私需求、合规边界
2. 设计阶段：威胁建模、架构评审、数据流审查
3. 开发阶段：secure coding、secret scanning、SAST、SCA
4. 测试阶段：DAST、API security testing、fuzzing、abuse case testing
5. 构建阶段：SBOM、artifact signing、provenance、CI/CD hardening
6. 发布阶段：release gate、risk acceptance、change approval
7. 运行阶段：runtime monitoring、vulnerability management、incident feedback

## 好的 DevSecOps 不是

- 把一堆扫描工具塞进 CI
- 让开发者每天看几百个低价值告警
- 安全团队成为唯一审批者

## 好的 DevSecOps 是

- 默认安全模板
- 清晰风险分级
- 可解释阻断门槛
- 自动化证据生成
- 安全能力平台化
- 事故和漏洞反哺开发规范

## 关联

- [[./应用安全与 API 安全|应用安全与 API 安全]]
- [[./供应链安全|供应链安全]]
- [[./威胁建模|威胁建模]]
- [[./漏洞管理与攻击面管理|漏洞管理与攻击面管理]]
