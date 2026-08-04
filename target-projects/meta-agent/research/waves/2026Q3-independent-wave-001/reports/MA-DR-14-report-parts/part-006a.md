| Hybrid architecture | 高 | 高 | classification router、multiple stores、deletion orchestration | dual truth、classification drift、orphan copies |
| Full retrieval quarantine | 中至高 | 高 | ingestion review、scanners、provenance、adversarial tests | review bottleneck、false confidence in scanners |

Vault-style dynamic credentials illustrate both benefits and maintenance burden. Leases and TTLs allow automatic expiry and revocation, but revocation can depend on downstream backends; force-removal may leave the secret system out of sync, and large lease populations can cause resource exhaustion or denial of service.citeturn16search0turn16search2turn16search16 因此 “short-lived credential” 仍需要 capacity planning、backend health、revocation monitoring 和 fallback—not merely a TTL field。

**Unresolved questions and Owner decisions**

| Owner decision | 为什么不能由本研究决定 |
|---|---|
| 哪些实际项目和数据主体会进入 private scope？ | 决定适用法律、合同、地域、consent 和 customer obligations |
| 是否允许任何真实 customer 或 regulated data？ | 当前 baseline 明确未授权；风险和责任显著高于一般 private notes |
| 首个候选是 local、cloud 还是 hybrid？ | 取决于协作、设备、availability 和行政负担偏好 |
| recovery key 由谁保管、是否允许第二 custodian？ | confidentiality 与 recoverability 存在不可消除的权衡 |
| 每类材料保留多久？ | 必须由 purpose、合同、法律和 Owner 风险偏好决定 |
| 是否允许 provider-side plaintext processing？ | 决定是否需要 client-side encryption，以及搜索和 connector 能力 |
| 是否公开任何 private-material pointer？ | 某些项目中仅“材料存在”就可能敏感 |
| 是否允许 semantic/vector index？ | embedding leakage、deletion、rebuild 和 cross-project isolation 仍需验证 |
| 是否允许 MCP 或外部 connector 读取 private corpus？ | 当前 target 明确未授权；协议能力不等于安全批准 |
| Agent 是否可产生长期 derived summaries？ | 影响 retention、cross-project contamination 和 methodology boundary |
| audit 保存多久、谁能查？ | 长期 audit 可帮助 incident，却会形成敏感行为数据集 |
| 删除目标是 logical removal、crypto erase 还是 media sanitization？ | 不同材料、介质和合同要求不同 |
| 是否允许 legal/contract hold？ | hold 会覆盖普通 deletion，需明确 authority 和解除流程 |
| 什么 residual risk 和 maintenance burden 可接受？ | 属于 Owner 的产品、隐私和 operational judgment |
| 什么证据足以从 synthetic prototype 进入 bounded pilot？ | 当前没有 pilot authorization 或 acceptance thresholds |

## 可移植来源表与最终处置

**Portable source table**

| 来源、版本与日期 | Direct URL / identifier | 支持的主要主张 | 限制 |
|---|---|---|---|
| NIST, **FIPS 199 — Standards for Security Categorization**, 2004 | `https://doi.org/10.6028/NIST.FIPS.199` | 按 confidentiality、integrity、availability 影响分类。citeturn10search1 | 美国联邦标准；本报告仅借用风险框架 |
| NIST, **SP 800-53 Rev. 5**, Release 5.2.0 noted 2025 | `https://doi.org/10.6028/NIST.SP.800-53r5` | access、audit、identity、incident、media、PII 和 privacy control families。citeturn10search2turn10search3 | 控制目录，不等于自动合规或有效实现 |
| NIST, **SP 800-63-4 Digital Identity Guidelines**, final 2025 | `https://doi.org/10.6028/NIST.SP.800-63-4` | identity proofing、authentication、federation 分离。citeturn9search0turn9search1 | 面向数字身份服务；具体 assurance level 需风险评估 |
| NIST, **SP 800-162 Guide to ABAC**, updated final 2019 | `https://doi.org/10.6028/NIST.SP.800-162` | subject/object/operation/environment 属性授权。citeturn9search18 | ABAC policy 复杂度和属性质量需自行管理 |
| NIST, **SP 800-207 Zero Trust Architecture**, final 2020 | `https://doi.org/10.6028/NIST.SP.800-207` | 不因网络位置产生 implicit trust；保护 resources。citeturn19search2turn19search9 | 抽象架构，不指定单一实现 |
| NIST, **SP 800-207A**, final 2023 | `https://doi.org/10.6028/NIST.SP.800-207A` | 应同时使用 user、service、application identity 实施细粒度 policy。citeturn19search0 | cloud-native emphasis；并非所有本地原型都需 service mesh |
| NIST, **SP 800-57 Part 1 Rev. 5**, final 2020 | `https://doi.org/10.6028/NIST.SP.800-57pt1r5` | key lifecycle、protection、backup、recovery、compromise。citeturn17search1 | Rev. 6 截至研究日期仍是 draft |
| NIST, **SP 800-88 Rev. 2 Guidelines for Media Sanitization**, final 2025 | `https://doi.org/10.6028/NIST.SP.800-88r2` | sanitization 是可验证 program，不是单一 delete command。citeturn14search0turn14search4 | 对 cloud replicas 和第三方 copies 仍需 provider evidence |
| NIST, **SP 800-111 Guide to Storage Encryption**, final 2007 | `https://doi.org/10.6028/NIST.SP.800-111` | full-disk、volume、file/folder encryption 的不同适用边界。citeturn9search2 | 较旧；不覆盖现代 Agent/connector threat |
| NIST, **Privacy Framework 1.0**, 2020 | `https://doi.org/10.6028/NIST.CSWP.01162020` | privacy risk 与 data processing lifecycle 的治理框架。citeturn2search12 | voluntary framework；PF 1.1 截至研究时仍非最终版 |
| IETF, **RFC 9700 OAuth 2.0 Security Best Current Practice**, 2025 | `https://www.rfc-editor.org/rfc/rfc9700.html`, DOI `10.17487/RFC9700` | redirect matching、token privilege、flow 和 replay security。citeturn1search3turn1search4 | 实际 connector 仍可能不支持全部 best practices |
| IETF, **RFC 9449 OAuth 2.0 DPoP**, 2023 | `https://www.rfc-editor.org/rfc/rfc9449.html`, DOI `10.17487/RFC9449` | sender-constrained tokens、降低 token-only replay。citeturn11search0turn11search13 | 不防止同一 compromised execution context 使用 key |
