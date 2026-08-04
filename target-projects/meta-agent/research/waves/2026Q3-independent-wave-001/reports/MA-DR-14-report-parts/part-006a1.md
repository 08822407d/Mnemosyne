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
