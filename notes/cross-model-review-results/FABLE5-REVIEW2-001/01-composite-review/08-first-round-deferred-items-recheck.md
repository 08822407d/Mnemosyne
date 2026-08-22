# 阶段1 专题08 — 第一轮遗留延迟项两个月后复检

```yaml
track_id: FABLE5-REVIEW2-001
record_type: composite_review_theme_report
theme: first_round_deferred_items_recheck
generated_by_model: claude-fable-5
surface: vscode
date: 2026-08-22
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
evidence_class: mixed_per_claim_labels
authority_level: non_execution_source_advisory_evidence
independence_note: >
  本轨道作者与第一轮 GF5 系列作者同为 Fable 族（§19 同族限制声明）。
  本专题不是对第一轮结论的独立复核，而是"当时的延迟决定在两个月后的
  事实环境下是否仍成立"的时效复检；复检依据全部为可核查的仓库事实。
```

复检对象：PRO-FABLE-GF5-MAINTAINER-ADJUDICATION-001（decision-matrix.yaml）中路由为 DEFER / WATCH / P3 / 无动作的条目，以及两项当时低判的增强建议。逐条给出：当时裁定 → 两个月事实 → 复检结论。

## GF5-TRIAGE-001 — FR-01/03 平台表面 delta 研究（当时：ACCEPT + DEFER_RESEARCH）

- 两个月事实 [VERIFIED_REPOSITORY_FACT]：专项研究未执行；但研究对象发生了实质变化——(a) ChatGPT 写入面已由 §18（07 月）收录并在实践中大量使用；(b) Claude 写入面于 08 月成为现实并有专门事实文件（claude-github-work-surface-facts.md，08-15）；(c) 发布事故链（235–239）提供了付费研究买不到的表面失败实证。
- 复检结论：**原题过时，建议改判**。不是"补做原研究"，而是二选一：(i) 销账——判定原研究目的已被现实事件+新事实文件覆盖；(ii) 重定范围——针对"未来一个月 Claude 为主力"的新格局做一次窄范围表面核验（如需要，属于 Fable 独立研究额度的合理用途）。交 Owner。
- claim: MODEL_INFERENCE（改判建议）

## GF5-TRIAGE-006 — 基质无关写入谱系失败类（当时：降 P3 可移植性候选）

- 两个月事实 [VERIFIED_REPOSITORY_FACT]：CUR-04 系 guard 持续演进（118→196/197→210），仍是 GitHub 专用表述；同时写入基质真的多样化了（ChatGPT app / 本地 git / Codex），且 235–239 事故正是"同一逻辑发布在不同执行面上反复失败"——基质差异成为实际故障源。
- 复检结论：**P3 维持成立但理由变化**——不是因为不重要，而是因为 F2/MNE-DR-005 路线实质上正在做这件事的更完整版本（跨仓库有序写入）。建议：不单独立项，把"基质无关谱系失败类"并入 F2 的 amendment candidate 审视范围，随 D-01 一起决。
- claim: MODEL_INFERENCE

## GF5-TRIAGE-008 — spec 内过时机制迁出（当时：RESEARCH_VOLATILE_FACTS_KEEP_STABLE_PRINCIPLES）

- 两个月事实 [VERIFIED_REPOSITORY_FACT]：spec 零修改；本轮专题02 确认 §5/§10/§14 三处快照过期（R2-CONF-002/003/004）；平台事实类内容实际已在 spec 外自然生长（claude-github-work-surface-facts、platform-guides/、DR6 派生视图）——"易变事实外置"的方向被实践自发采用，只差 spec 侧收尾。
- 复检结论：**升级为 P1 修复项**。两个月验证了当时的判断方向（stable principles 留、volatile facts 出），现在有了具体的三处证据与现成的外置目的地。与 R2-CONF-001（§7 死条款）可合并为一次"执行源时效性修订"任务交 Owner。
- claim: VERIFIED_REPOSITORY_FACT（事实）+ DESIGN_RECOMMENDATION（升级）

## GF5-TRIAGE-009 — Owner 连续性（当时：P3 WATCH）

- 两个月事实：无方案、无新记录 [VERIFIED_REPOSITORY_FACT]；但 Owner 决策带宽的**吞吐维度**显性化（订阅轮换 + 2 个 HIGH 决策债排队，专题06 R2-SPOF-001）。
- 复检结论：**连续性维持 WATCH；吞吐问题分拆出来现在处理**（打包批示、决策分流——本轨道门3 即实践）。建议 Owner 用一句话销掉连续性账（"无方案、接受风险"或指定最低限度安排），避免它无限期挂在每轮评审里。
- claim: MODEL_INFERENCE

## GF5-TRIAGE-010 — 语言政策 / 自动化时机 / overfitting 处置（当时：捆绑拆分，P3）

- 语言政策：**升级证据充分**。两个月内 Owner 两次明确表达英文/长 YAML 负担（199 §1 引用的 issue 评论；08-22 对本轨道的通俗中文指令）；guard 层 3336 行全英文（R2-CONF-007）。复检结论：升 P2，建议门3 给出"分层语言规则"具体案文供 Owner 批。[VERIFIED_REPOSITORY_FACT（证据）]
- 自动化时机（AUTO fence）：维持现状成立——v0.1 边界仍被遵守，且没有出现"需要自动化才能解决"的新failure（发布事故的解是换通道不是自动化）。不动。[VERIFIED_REPOSITORY_FACT]
- overfitting 处置（keep_with_refresh_gate ×3、abstract_later ×1）：三个 keep 项的 refresh gate 均未触发核验（§10/§14 的 Codex 前提、§13 DR 例外、§17 产品名）——其中 §10/§14 已在本轮被确认过期（R2-CONF-003/004），即 refresh gate 应当触发而没有触发。复检结论：refresh gate 是又一个"声明了但没有执行钩子"的机制（与 R2-FRESH-006 同病），修复并入执行源时效性修订任务。[VERIFIED_REPOSITORY_FACT]

## GF5-ENH-CUR-003 — no-re-ask 约定（当时：medium，未采纳）

- 两个月事实：未建；跨会话重复询问的实际痛感出现在 Owner 侧（08-22 指令明确要求减少需要 Owner 处理的重复内容 [MODEL_INFERENCE 关联]）；但 handoff 面的主要问题被证明是 staleness 而非 re-ask（专题03）。
- 复检结论：维持不采纳；其目标被"署名方案 + onboarding + per-route status"组合部分覆盖。不再复查，销账。
- claim: MODEL_INFERENCE

## GF5-ENH-CUR-004 — 轻量 staleness-flag 约定（当时：low，未采纳）

- 两个月事实：专题03 三条 REPAIR 级 staleness 发现（启动三件套、review-status 半旧、总路标缺位），全部可被"live 文件强制 last_updated_by_task + 失效声明"预防或至少暴露。
- 复检结论：**当时判 low 是错判（以两个月后证据回看），升级为 P2 采纳候选**。最低成本版本已在专题03 R2-FRESH-006 具体化。
- claim: VERIFIED_REPOSITORY_FACT（证据）+ DESIGN_RECOMMENDATION（升级）

## 附：第一轮"未落实/仍开放"清单（定向报告 c.5）状态迁移

| 项 | 定向时点状态 | 本轮处置 |
|---|---|---|
| 机械 no-write 门 BLOCKED | 挂账 | → D-03，建议显式作废或收尾 |
| W4 open_uncertain | 挂账 | → D-05，随 D-03 历史化 |
| Case 005 NOT_RUN | 挂账 | → D-09，保持或声明永久策略 |
| HO-GUIDANCE-001 | unresolved | → D-04，A/B 立项前决 |
| FR-01/03 研究 | UNKNOWN | → 本专题改判建议（销账或重定范围） |
| F2 停在 G2A 门 | 等 Owner | → D-01（HIGH） |

## 小结

七个延迟项复检结果：2 项升级（008 → P1、ENH-CUR-004 → P2）、1 项改判（001 销账或重定范围）、1 项并入活路线（006 → F2）、1 项拆分（009 吞吐现做/连续性 watch）、1 项部分升级（010 语言 → P2）、1 项销账（ENH-CUR-003）。总体规律 [MODEL_INFERENCE]：当时判低的条目里，凡涉及**时效与状态维护机制**的都被两个月的现实抬高了；凡涉及**结构完备性**的都被实践自然覆盖或吸收。这与 Owner 的实用化转向方向一致——机制债比设计债更值得先还。
