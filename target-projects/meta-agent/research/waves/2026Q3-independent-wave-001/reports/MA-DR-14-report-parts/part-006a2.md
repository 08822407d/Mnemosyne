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
