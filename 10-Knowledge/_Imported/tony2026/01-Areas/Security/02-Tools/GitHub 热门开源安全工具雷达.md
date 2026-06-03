---
title: GitHub 热门开源安全工具雷达
type: tool-radar
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# GitHub 热门开源安全工具雷达

> 这页用于把 GitHub 上常见、热门、可学习的安全工具接入知识库。
> 注意：star 数会变化，热度不等于生产适配度；红队、漏洞验证、扫描类工具只能在授权范围内使用。

> 更完整的“开源项目知识库格式”维护入口见：[[../04-Open-Source-Tools/专题总览|Security Open Source Tools 专题总览]]。

## 使用原则

- 先按问题选工具：资产发现、代码安全、云安全、检测响应、数据安全、身份密钥、AI 安全。
- 先在实验室练，再进生产：扫描、PoC、红队框架、反作弊和自动化响应都要有授权、范围和停止条件。
- 先小闭环，再平台化：工具输出必须能进入 owner、工单、SLA、例外、验证和证据。
- 不迷信 star：维护活跃度、许可证、社区质量、误报率、集成能力和组织流程同样重要。

## 快速雷达

| 工具族 | 代表项目 | 适合解决的问题 |
|---|---|---|
| 资产发现与攻击面 | [Amass](https://github.com/owasp-amass/amass)、[subfinder](https://github.com/projectdiscovery/subfinder)、[httpx](https://github.com/projectdiscovery/httpx)、[naabu](https://github.com/projectdiscovery/naabu)、[katana](https://github.com/projectdiscovery/katana)、[Nmap](https://github.com/nmap/nmap)、[masscan](https://github.com/robertdavidgraham/masscan)、[RustScan](https://github.com/bee-san/RustScan) | 子域名、端口、Web 入口、服务识别、暴露面盘点 |
| Web/API 安全测试 | [OWASP ZAP](https://github.com/zaproxy/zaproxy)、[nuclei](https://github.com/projectdiscovery/nuclei)、[sqlmap](https://github.com/sqlmapproject/sqlmap)、[mitmproxy](https://github.com/mitmproxy/mitmproxy)、[dirsearch](https://github.com/maurosoria/dirsearch) | Web/API 漏洞、代理分析、目录发现、模板化漏洞验证 |
| AppSec / DevSecOps | [Trivy](https://github.com/aquasecurity/trivy)、[Semgrep](https://github.com/semgrep/semgrep)、[Gitleaks](https://github.com/gitleaks/gitleaks)、[TruffleHog](https://github.com/trufflesecurity/trufflehog)、[OSV-Scanner](https://github.com/google/osv-scanner)、[Syft](https://github.com/anchore/syft)、[Grype](https://github.com/anchore/grype)、[cosign](https://github.com/sigstore/cosign)、[Scorecard](https://github.com/ossf/scorecard) | 代码、依赖、secret、SBOM、镜像、签名、供应链 |
| 云原生与 IaC | [Prowler](https://github.com/prowler-cloud/prowler)、[Checkov](https://github.com/bridgecrewio/checkov)、[kube-bench](https://github.com/aquasecurity/kube-bench)、[Kubescape](https://github.com/kubescape/kubescape)、[Falco](https://github.com/falcosecurity/falco)、[Terrascan](https://github.com/tenable/terrascan)、[ThreatMapper](https://github.com/deepfence/ThreatMapper) | 云配置、Kubernetes 基线、IaC 扫描、运行时检测、CNAPP 学习 |
| 身份、密钥与策略 | [Vault](https://github.com/hashicorp/vault)、[OpenBao](https://github.com/openbao/openbao)、[Infisical](https://github.com/Infisical/infisical)、[Authelia](https://github.com/authelia/authelia)、[OPA](https://github.com/open-policy-agent/opa)、[cert-manager](https://github.com/cert-manager/cert-manager)、[step-ca](https://github.com/smallstep/certificates) | secrets、证书、SSO/MFA、策略即代码、机器身份 |
| 蓝队、检测与 SOC | [Wazuh](https://github.com/wazuh/wazuh)、[osquery](https://github.com/osquery/osquery)、[Sigma](https://github.com/SigmaHQ/sigma)、[YARA](https://github.com/VirusTotal/yara)、[Suricata](https://github.com/OISF/suricata)、[Zeek](https://github.com/zeek/zeek)、[MISP](https://github.com/MISP/MISP)、[Velociraptor](https://github.com/velocidex/velociraptor)、[TheHive](https://github.com/TheHive-Project/TheHive) | 终端查询、检测规则、恶意样本规则、网络检测、威胁情报、事件响应 |
| DFIR 与逆向 | [Volatility3](https://github.com/volatilityfoundation/volatility3)、[Timesketch](https://github.com/google/timesketch)、[x64dbg](https://github.com/x64dbg/x64dbg)、[radare2](https://github.com/radareorg/radare2)、[Frida](https://github.com/frida/frida)、[MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | 内存取证、时间线分析、逆向、动态插桩、移动安全分析 |
| 授权攻防与 AD | [Metasploit](https://github.com/rapid7/metasploit-framework)、[Impacket](https://github.com/fortra/impacket)、[BloodHound](https://github.com/SpecterOps/BloodHound)、[Sliver](https://github.com/BishopFox/sliver) | 授权渗透测试、协议分析、AD 攻击路径、对抗模拟 |
| AI 安全 | [promptfoo](https://github.com/promptfoo/promptfoo)、[garak](https://github.com/garak-llm/garak)、[Counterfit](https://github.com/microsoft/Counterfit)、[LLM Guard](https://github.com/ProtectAI/llm-guard)、[Rebuff](https://github.com/protectai/rebuff) | prompt/agent/RAG 测试、LLM 红队、输入输出防护、AI 应用安全评测 |

## 高星工具观察

> 基于 2026-05-05 的 GitHub 搜索/API 抽样，数字会变化，只做热度参考。

| 项目 | 大致定位 | 观察到的信号 |
|---|---|---|
| [x64dbg](https://github.com/x64dbg/x64dbg) | Windows 逆向调试 | 高 star、逆向/恶意样本分析常用 |
| [mitmproxy](https://github.com/mitmproxy/mitmproxy) | 交互式 HTTP/TLS 代理 | Web/API/移动端调试和安全测试常用 |
| [Metasploit](https://github.com/rapid7/metasploit-framework) | 渗透测试框架 | 授权测试和漏洞验证经典框架 |
| [sqlmap](https://github.com/sqlmapproject/sqlmap) | SQL 注入自动化 | Web 漏洞学习和验证常见工具 |
| [Trivy](https://github.com/aquasecurity/trivy) | 漏洞/配置/secret/SBOM 扫描 | DevSecOps 与云原生场景非常常见 |
| [nuclei](https://github.com/projectdiscovery/nuclei) | 模板化漏洞扫描 | 攻击面验证和漏洞检测生态活跃 |
| [Gitleaks](https://github.com/gitleaks/gitleaks) / [TruffleHog](https://github.com/trufflesecurity/trufflehog) | Secret 扫描 | CI/CD 和代码仓 secret 治理常用 |
| [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | 移动安全分析 | Android/iOS 静态和动态分析常用 |
| [Semgrep](https://github.com/semgrep/semgrep) | 轻量 SAST | 规则可读、适合 AppSec 工程化 |
| [Wazuh](https://github.com/wazuh/wazuh) | 开源 SIEM/XDR | 蓝队、安全运营和实验室常用 |

## 按学习路线使用

### L1：个人实验室

- Web/API：OWASP ZAP、mitmproxy、nuclei、sqlmap、dirsearch。
- 资产发现：Amass、subfinder、httpx、naabu、Nmap、RustScan。
- AppSec：Trivy、Semgrep、Gitleaks、TruffleHog、OSV-Scanner。
- 蓝队：Wazuh、osquery、Sigma、YARA、Suricata、Zeek。

### L2：团队 CI/CD

- PR 阶段：Semgrep、Gitleaks、TruffleHog、OSV-Scanner、Checkov。
- 构建阶段：Trivy、Syft、Grype、cosign、Scorecard。
- 云原生阶段：Prowler、kube-bench、Kubescape、Falco。
- 输出进入：工单、SLA、例外、复测、审计证据。

### L3：企业安全平台

- 检测：Wazuh、osquery、Sigma、YARA、Suricata、Zeek、Falco。
- 响应：Velociraptor、TheHive、MISP、Timesketch。
- 身份与策略：Vault/OpenBao、Infisical、OPA、cert-manager。
- 治理：把工具结果接入 [[./GRC、合规与证据平台|GRC、合规与证据平台]] 或内部证据平台。

## 工具落地检查

每引入一个工具，都要回答：

- 它对应哪个风险？
- 覆盖哪些资产？
- 输出给谁处理？
- 误报如何治理？
- 修复如何验证？
- 例外如何到期？
- 指标和证据在哪里？

## 关联

- [[./工具平台分类索引|工具平台分类索引]]
- [[./安全工具平台总览|安全工具平台总览]]
- [[../04-Open-Source-Tools/专题总览|Security Open Source Tools 专题总览]]
- [[../06-Maps/安全工具平台能力地图|安全工具平台能力地图]]
- [[../08-Playbooks/安全工具平台选型与落地 Playbook|安全工具平台选型与落地 Playbook]]
