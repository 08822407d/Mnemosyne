# WORK-ULTRA-FABLE-MNE-DR-006 — Pro Owner Brief（MNE-DR-006 交接加固）

```yaml
artifact_id: WORK-ULTRA-FABLE-MNE-DR-006-HANDOFF-PROTOCOL-REPOSITORY-AUDIT-001-pro-owner-brief
task_id: WORK-ULTRA-FABLE-MNE-DR-006-HANDOFF-PROTOCOL-REPOSITORY-AUDIT-001
verdict: REPOSITORY_AUDIT_COMPLETE_READY_FOR_PRO_OWNER_REVIEW
execution_source: current/human-approved-spec.md（本简报与全部产物均非执行源）
repository_writes_performed_by_this_run: none
audited_master: e726dea818dca9418181775d0e7dcd62eb6c464a（start == end，单一 master 分支，0 个 open PR）
```

## 操作内容（需要你手动执行）

本次审计运行本身不需要任何补救操作。需要你手动执行的只有评审与决策：

1. **（必需）评审本任务 8 份产物**，重点按顺序：`pro-owner-brief`（本文件）→ `repository-audit` → `failure-taxonomy` → `guidance-architecture-comparison` → `command-guard-patch-spec` → `validation-design`。
2. **（必需）对下方 D1–D5 逐项给出决定**（可全部拒绝；每项均有 reject-premise 路径）。
3. **（提醒，非本任务范围）F2 Handoff 003 的 post-merge receive rehearsal 仍是当前 route gate**（`receive_rehearsal_run: false`）。该 rehearsal 按已批准的 route 合同独立进行，不依赖、也不被本审计的任何提案阻塞。
4. **（可选）** 若接受任何 patch 提案，另行发起带仓库写授权的实施任务；本次运行未获写授权、也未执行任何写入。

## 结论摘要（证据分级见各产物）

- 输入完整性门、执行时仓库门、17/17 静态身份校验全部通过；未读取任何 cold source（`raw/` 全程未读正文）；未使用任何对话导出。
- **两起已归档 F2 协议失败均为「发布方/出版侧合同缺陷」**：FC‑01 聊天可见 startup 文本相对 canonical artifact 漂移（wrong path/ID/receive key，仓库 canonical 正确）；FC‑02 冻结了错误的 source-archive blob（7c2af723… vs 实际 6e90c8f1…），接收方**正确 fail-closed 阻断**。FC‑03（Handoff 002 schema/oracle 机械不相容）由 Pro 裁决在 rehearsal 前拦截。归档内**没有任何接收方行为失败**——接收侧纪律是有效的，出问题的是发布闭合。
- **Handoff 003 修复经本审计机械复核为结构闭合**：schema‑001 的 40 个 expected 字段中 39 个由 Package 003 提供，唯一缺口恰为设计内的 `package.blob` 自引用（由 Startup 003 提供 `bb60b9c1…`，与树内实际 blob 相等）；全部 25+ 交叉引用 blob 相符。**尚未行为验证**（rehearsal 未跑）。
- **通用层（prepare/receive/load 命令 + guards）目前是 advisory prose，不是可强制协议**：无身份钉定、无 typed oracle、无 publication receipt、无 startup 传输保真规则；上述机械性质全部只存在于 F2 route-specific 修复中。明天用通用命令新建一个交接，FC‑01/02/03 条件将原样复现。
- **跨 route 根因结论保持 BLOCKED**：你报告的另一起 incomplete handoff 仅有 TODO 中的二手记录（OWNER_REPORTED_BUT_NOT_ARCHIVALLY_VERIFIED），缺 exact source/receiver exports；本审计未做任何 god-view 断言。

## 需要你决定的事项

**D1 — Guidance 加载架构**（详见 comparison 产物；本审计不替你选）
推荐（可拒绝）：**先 C（source-selected exact guidance manifest），后 B2（单 startup 双相位、验收 token 仍由你把关），远期 E（仅高影响触发人工门）；A 保留为通用回退；D（task-local bundle）不作默认**。Reject-premise 路径：若你把「单独发送指导消息」视为有意的人工注意检查点，则保留 A、仅在其下叠加 C，放弃 B/E——C 在任何前提下都有益。HO‑GUIDANCE‑001 的 target-project 问题本审计未触碰、仍开放。

**D2 — Patch 采纳范围**（详见 patch-spec）
两档：**最小高价值子集 P‑04（publication receipt）+ P‑05（startup 传输保真 guard）+ P‑06（manifest mode）**——零 schema 迁移，直接覆盖 FC‑01/02/08/09；或**全量 P‑01…P‑11**（含通用 receive schema 与 oracle 模板）。建议：先最小子集，待 Handoff 003 rehearsal 与 MNE‑HVAL‑001 回传真实行为后再决定全量。P‑00（执行源 §15 一句话）可选、可后置。

**D3 — 验证包授权**（详见 validation-design）
MNE‑HVAL‑001 已设计未执行：合成 fixture、隐藏 key 承诺方案、22 个场景、false PASS/false BLOCK 硬阈值（seeded 身份/oracle 缺陷 false PASS 必须为 0）。需要你分别授权：fixture 写入、执行、quota 上限（建议 ≤20 个接收对话、≤6 个 Pro turn）。

**D4 — God-view 导出研究**
是否按 TODO‑001 启动 bounded archival study（导出既往 handoff 双方对话）。没有它，FC‑01 的漂移产生机理与 FC‑10（另一起 incomplete handoff）永远停留在 UNKNOWN；有它，需先过隐私/公库安全预检。本审计对此无立场，仅指出：**不导出，则跨 route 根因永久 BLOCKED**。

**D5 — `handoff/handoff-current.md` 处置**
该卡当前指向已被取代的 route（MNEMOSYNE‑140 时代），是站立的 stale-pointer 隐患。二选一：每次交接强制刷新（增加负担），或降级为固定横幅「授权包路径只来自 Owner 启动消息」（推荐，见 P‑09）。

## 下一步

- 建议顺序：完成 F2 Handoff 003 rehearsal（既有 gate，先行）→ D1–D5 决定 → 若采纳，最小子集实施任务（含仓库写授权）→ MNE‑HVAL‑001 fixture 发布与执行 → 复盘后决定全量 patch 与 B2/E。
- 模型要求：D1–D5 属 Owner 决策，无需 Pro；后续实施任务为 bounded 写入，NEXT_TIER_SUFFICIENT_CANDIDATE，需在各自任务内重估；MNE‑HVAL‑001 的裁决环节按设计可由 next-tier 执行、异常 ≤1 个 Pro turn。
- 下一步仓库写入：**待单独授权**（本任务 0 写入；任何实施/fixture 写入均需你新的任务级授权，目标仓库均为 08822407d/Mnemosyne，写入类型为新增文件与命令/guard 版本化修订）。
