Vault-style dynamic credentials illustrate both benefits and maintenance burden. Leases and TTLs allow automatic expiry and revocation, but revocation can depend on downstream backends; force-removal may leave the secret system out of sync, and large lease populations can cause resource exhaustion or denial of service.citeturn16search0turn16search2turn16search16 因此 “short-lived credential” 仍需要 capacity planning、backend health、revocation monitoring 和 fallback—not merely a TTL field。

**Unresolved questions and Owner decisions**

| Owner decision | 为什么不能由本研究决定 |
|---|---|
| 哪些实际项目和数据主体会进入 private scope？ | 决定适用法律、合同、地域、consent 和 customer obligations |
