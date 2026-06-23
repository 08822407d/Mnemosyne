# Current Evidence Map / 当前证据映射（派生视图）

> 说明：本文件是 current 派生视图，不是原始研究报告。  
> 当前来源轮次：`RC-2026Q2-initial`；补充当前证据轮次：`RC-2026Q2-memory-testing`。  
> 详细映射见：`raw/research-reports/cycles/2026Q2-initial/evidence-map.md`。

## 当前采用的研究证据视图

- active_cycles: RC-2026Q2-initial; RC-2026Q2-memory-testing (supplemental)
- report_count: 8
- use: 约束 Mnemosyne 的能力边界判断、机制设计与平台适配假设。

## 当前重点结论（摘要）

- 保持“模型负责计算，文件负责记忆”。
- 外部文件/Git 仓库作为长期真相源。
- 普通对话窗口默认半自动，不假设自动写回。
- 本地开发 Agent / 云端工作流能力需分层声明，不可混同。
- 研究报告属于高权重证据层，不是执行源。

## 需要人工复核

- RPT-2026Q2-0002 ~ RPT-2026Q2-0007（PDF）中的图表、图片与版式相关证据。
- 若未来设计决策依赖上述图表结论，必须先完成人工复核。

## 演化说明

- future_refresh: 本文件会随新 cycle 的 evidence map 更新 current 视图。
- history_policy: 旧 cycle 不覆盖、不删除，保留可追溯历史。


## Memory-system testing/debugging DR1 evidence

- report_id: RPT-2026Q2-MT-0001
- summary: `raw/research-reports/cycles/2026Q2-memory-testing/report-summaries/DR1_memory_testing_debugging_evidence_review_summary.md`
- conclusion: No unified mature industry-standard testing framework exists specifically for AI Agent external persistent memory systems. Mature reusable sub-practices exist and should be combined.
- candidate failure taxonomy: stale handoff; wrong source priority; memory drift; memory overwrite; missing critical context; over-retention; under-retention; hallucinated memory; retrieval failure; stale tool capability assumption; implicit automation assumption; privacy leakage; inconsistent handoff vs active context; user decision not recorded or not propagated; first target-project dry-run output looks complete but cannot actually land.
- current-stage implication: evaluate state correctness, source priority, temporal correctness, decision propagation, handoff executability, and delivery landability, not only final answer correctness.
- boundary: research evidence only; not execution source and not automatic writeback authority.

## DR2 / handoff-strategy evidence — RC-2026Q2-handoff-strategy

```yaml
- evidence_id: EVID-2026Q2-HO-0001
  source_report: RPT-2026Q2-HO-0001
  claim_or_implication: Correct handoff should mean fresh-session recovery of execution source, current phase/gate, live state, authorities, prohibitions, completed/incomplete work, safe next action, and explicit unknown handling without relying on old implicit context.
  confidence_or_status: report_conclusion; candidate_for_template_review
  mnemosyne_use: Define handoff correctness criteria for future replay/handoff template updates.
  not_execution_source: true

- evidence_id: EVID-2026Q2-HO-0002
  source_report: RPT-2026Q2-HO-0001
  claim_or_implication: Handoff packages should be tiered into minimum, standard, and extended forms, with extended packages reserved for high-risk migration, post-failure recovery, stale branch diagnosis, or historical contamination analysis.
  confidence_or_status: report_recommendation; requires_user_review_before_adoption
  mnemosyne_use: Candidate input for future handoff package template design.
  not_execution_source: true

- evidence_id: EVID-2026Q2-HO-0003
  source_report: RPT-2026Q2-HO-0001
  claim_or_implication: Quantitative/semi-quantitative scoring should include blocking gates plus dimensions such as execution-source recovery, gate recovery, state accuracy, authority recovery, next-action correctness, evidence quality, stale-context detection, unsupported-assumption labeling, safety/privacy preservation, token efficiency, and cross-model robustness.
  confidence_or_status: report_recommendation; scoring_instrument_not_yet_adopted
  mnemosyne_use: Candidate input for future replay scorecard update.
  not_execution_source: true

- evidence_id: EVID-2026Q2-HO-0004
  source_report: RPT-2026Q2-HO-0001
  claim_or_implication: Stale-context and old-conversation contamination are major risks; old replay results, old exports, old result records, and research reports must not be promoted into current truth.
  confidence_or_status: report_conclusion_consistent_with_existing_boundaries
  mnemosyne_use: Reinforce stale-state resistance in current handoff and verification work.
  not_execution_source: true

- evidence_id: EVID-2026Q2-HO-0005
  source_report: RPT-2026Q2-HO-0001
  claim_or_implication: Handoff tests should record model/tool provenance, including visible model/tool label, interface/session type, repository ref/commit, memory/history settings, accessible files, automation level, and known limitations.
  confidence_or_status: report_recommendation; exact_field_set_requires_review
  mnemosyne_use: Candidate input for future provenance schema updates.
  not_execution_source: true

- evidence_id: EVID-2026Q2-HO-0006
  source_report: RPT-2026Q2-HO-0001
  claim_or_implication: Replay/verification testing should be repeatable and evidence-backed, with PASS / PASS_WITH_WARNINGS / FAIL / BLOCKED semantics and repository evidence paths for key claims.
  confidence_or_status: report_recommendation; aligns_with_existing_replay_direction
  mnemosyne_use: Inform future replay protocol refinement without changing current gate automatically.
  not_execution_source: true

- evidence_id: EVID-2026Q2-HO-0007
  source_report: RPT-2026Q2-HO-0001
  claim_or_implication: Before first real target-project dry-run, Mnemosyne should run and score a post-050 fresh replay; any blocking failure should prevent proceeding.
  confidence_or_status: report_recommendation; current_gate_not_closed_by_report
  mnemosyne_use: Inform readiness review before dry-run start.
  not_execution_source: true
```
