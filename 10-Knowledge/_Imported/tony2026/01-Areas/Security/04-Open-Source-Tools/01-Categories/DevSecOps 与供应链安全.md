---
title: DevSecOps 与供应链安全
type: category
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# DevSecOps 与供应链安全

## 解决什么问题

- 代码、依赖、secret、镜像、SBOM、签名和开源项目健康度进入 CI/CD。
- 把安全检查从上线后扫描前移到 PR、构建和发布门禁。

## 代表项目

- [Trivy](https://github.com/aquasecurity/trivy)：漏洞、配置、secret、SBOM 多合一扫描。
- [Semgrep](https://github.com/semgrep/semgrep)：轻量静态分析。
- [Gitleaks](https://github.com/gitleaks/gitleaks)：secret 扫描。
- [TruffleHog](https://github.com/trufflesecurity/trufflehog)：泄露凭据发现与验证。
- [OSV-Scanner](https://github.com/google/osv-scanner)：基于 OSV 的漏洞扫描。
- [Syft](https://github.com/anchore/syft)：SBOM 生成。
- [Grype](https://github.com/anchore/grype)：漏洞扫描。
- [cosign](https://github.com/sigstore/cosign)：容器和二进制签名。
- [OpenSSF Scorecard](https://github.com/ossf/scorecard)：开源项目安全健康度评分。
- [Snyk CLI](https://github.com/snyk/cli)：CLI 安全扫描。

## 典型组合

`Semgrep + Gitleaks + OSV/Trivy + Syft + cosign + Scorecard -> release gate -> GRC 证据`

## 学习价值

- 理解 DevSecOps 的核心不是“扫更多”，而是把安全发现变成开发者可修、可例外、可验证、可审计的流水线。

