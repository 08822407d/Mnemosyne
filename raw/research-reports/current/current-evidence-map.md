# Current Evidence Map / 当前证据映射（派生视图）

> 说明：本文件是 current 派生视图，不是原始研究报告。  
> 当前来源轮次：`RC-2026Q2-initial`；补充当前证据轮次：`RC-2026Q2-memory-testing`、`RC-2026Q2-handoff-strategy`、`RC-2026Q2-user-input-governance`、`RC-2026Q2-first-target-dry-run-evaluation`、`RC-2026Q3-platform-context-apps-delta`。  
> 详细映射见各 cycle 的 evidence / summary / review 文件。

## 当前采用的研究证据视图

- active_cycles: RC-2026Q2-initial; RC-2026Q2-memory-testing; RC-2026Q2-handoff-strategy; RC-2026Q2-user-input-governance; RC-2026Q2-first-target-dry-run-evaluation; RC-2026Q3-platform-context-apps-delta
- report_count: 12
- use: 约束 Mnemosyne 的能力边界判断、机制设计与平台适配假设。

## 当前重点结论（摘要）

- 保持“模型负责计算，文件负责记忆”。
- 外部文件/Git 仓库作为长期真相源。
- 普通对话窗口默认半自动，不假设自动写回。
- 本地开发 Agent / 云端工作流能力需分层声明，不可混同。
- 研究报告属于高权重证据层，不是执行源。
- Project memory、platform memory、connected apps、sync、repository authorization、surface capability 和 task authority 必须分层记录。
- Search/sync connector 适合相关性检索，不默认构成完整枚举或 mechanical proof。

## 需要人工复核

- RPT-2026Q2-0002 ~ RPT-2026Q2-0007（PDF）中的图表、图片与版式相关证据。
- 若未来设计决策依赖上述图表结论，必须先完成人工复核。
- DR6 原始报告中的 Deep Research citation markers 具有可移植性限制；关键 operational claims 应使用 portable source manifest 或重新查验官方来源。

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

## DR4 / user-input governance evidence — RC-2026Q2-user-input-governance

```yaml
- evidence_id: EVID-2026Q2-UIG-0001
  source_report: RPT-2026Q2-UIG-0001
  claim_or_implication: visibility_unverified = public_equivalent / public-risk for storage decisions.
  confidence_or_status: report_conclusion; candidate_for_target_input_governance
  not_execution_source: true
- evidence_id: EVID-2026Q2-UIG-0002
  source_report: RPT-2026Q2-UIG-0001
  claim_or_implication: Originals/raw requirements/sensitive materials default outside Git; user-approved decisions, reviewed redacted excerpts, synthetic substitutes, and safe external pointers/manifests are eligible in Git if approved and safe.
  confidence_or_status: report_conclusion; aligns_with_existing_visibility_boundary
  not_execution_source: true
- evidence_id: EVID-2026Q2-UIG-0003
  source_report: RPT-2026Q2-UIG-0001
  claim_or_implication: AI/human restatements are explanatory layer, not original requirements or approved baseline.
  confidence_or_status: report_conclusion
  not_execution_source: true
- evidence_id: EVID-2026Q2-UIG-0004
  source_report: RPT-2026Q2-UIG-0001
  claim_or_implication: Redaction manifest and external pointer schemas are recommended before real target material intake.
  confidence_or_status: report_recommendation; adopted_as_non_execution_guidance_by_MNEMOSYNE-058
  not_execution_source: true
- evidence_id: EVID-2026Q2-UIG-0005
  source_report: RPT-2026Q2-UIG-0001
  claim_or_implication: Git history exposure means delete/move/revert does not erase historical exposure; private repo does not automatically authorize storing originals.
  confidence_or_status: report_conclusion
  not_execution_source: true
```

## DR5 first real target-project dry-run evaluation evidence — RC-2026Q2-first-target-dry-run-evaluation

```yaml
- evidence_id: EVID-2026Q2-FTDRE-0001
  source_report: RPT-2026Q2-FTDRE-0001
  claim_or_implication: First real dry-run success must be evidence-backed and authority-bounded, not artifact-polish-based.
  not_execution_source: true
- evidence_id: EVID-2026Q2-FTDRE-0002
  source_report: RPT-2026Q2-FTDRE-0001
  claim_or_implication: Synthetic smoke test, tabletop dry-run, real target dry-run, target delivery, and target repository write are distinct evaluation objects.
  not_execution_source: true
- evidence_id: EVID-2026Q2-FTDRE-0003
  source_report: RPT-2026Q2-FTDRE-0001
  claim_or_implication: Critical blockers must be checked before scoring; synthetic evidence cannot be reported as real dry-run evidence.
  not_execution_source: true
- evidence_id: EVID-2026Q2-FTDRE-0004
  source_report: RPT-2026Q2-FTDRE-0001
  claim_or_implication: Deterministic checks cover boundaries/evidence; LLM-as-judge is limited to quality judgments; user confirmation is required for usefulness and risk acceptance.
  not_execution_source: true
- evidence_id: EVID-2026Q2-FTDRE-0005
  source_report: RPT-2026Q2-FTDRE-0001
  claim_or_implication: PASS does not mean production-ready, target repository write approved, or global rule update approved.
  not_execution_source: true
- evidence_id: EVID-2026Q2-FTDRE-0006
  source_report: RPT-2026Q2-FTDRE-0001
  claim_or_implication: Dry-run findings should flow to postmortem/regression/candidate layers, not directly to execution source.
  not_execution_source: true
```

## DR6 platform / context / apps delta evidence — RC-2026Q3-platform-context-apps-delta

```yaml
- evidence_id: EVID-2026Q3-PCAD-0001
  source_report: RPT-2026Q3-PLATFORM-DELTA-0001
  claim_or_implication: Project-only memory is selected only when creating a new Project; existing default-memory Projects cannot be converted in place.
  confidence_or_status: official_fact_independently_rechecked
  mnemosyne_use: cleanroom setup candidate
  not_execution_source: true

- evidence_id: EVID-2026Q3-PCAD-0002
  source_report: RPT-2026Q3-PLATFORM-DELTA-0001
  claim_or_implication: Project-only blocks outside-Project chat references but allows references to other chats inside the same Project; non-Enterprise default-memory Projects may reference outside-Project conversations.
  confidence_or_status: official_fact_independently_rechecked
  mnemosyne_use: fresh-session and isolation provenance
  not_execution_source: true

- evidence_id: EVID-2026Q3-PCAD-0003
  source_report: RPT-2026Q3-PLATFORM-DELTA-0001
  claim_or_implication: Plugin visibility/installation, app enablement, app authentication, sync, source permission, action control, approval policy, per-chat invocation and task authority are distinct.
  confidence_or_status: official_fact_independently_rechecked
  mnemosyne_use: terminology and permission-mapping candidate
  not_execution_source: true

- evidence_id: EVID-2026Q3-PCAD-0004
  source_report: RPT-2026Q3-PLATFORM-DELTA-0001
  claim_or_implication: GitHub repository authorization is separate from sync selection; plan/surface availability and search indexing can differ.
  confidence_or_status: official_fact_independently_rechecked
  mnemosyne_use: GitHub test preflight and provenance
  not_execution_source: true

- evidence_id: EVID-2026Q3-PCAD-0005
  source_report: RPT-2026Q3-PLATFORM-DELTA-0001
  claim_or_implication: Deep Research uses connected-app read actions only during research.
  confidence_or_status: official_fact_independently_rechecked
  mnemosyne_use: preferred surface for read-only research cycles
  not_execution_source: true

- evidence_id: EVID-2026Q3-PCAD-0006
  source_report: RPT-2026Q3-PLATFORM-DELTA-0001
  claim_or_implication: Synced app data may be saved or reused through ChatGPT Memory; disconnecting the app does not erase prior conversations that used the data.
  confidence_or_status: official_fact_independently_rechecked
  mnemosyne_use: connected-app contamination and retention risk
  not_execution_source: true

- evidence_id: EVID-2026Q3-PCAD-0007
  source_report: RPT-2026Q3-PLATFORM-DELTA-0001
  claim_or_implication: Visible model/reasoning labels are operator-observed provenance but not complete runtime attestation.
  confidence_or_status: candidate_guidance_supported_by_current_product_behavior
  mnemosyne_use: provenance schema
  not_execution_source: true

- evidence_id: EVID-2026Q3-PCAD-0008
  source_report: RPT-2026Q3-PLATFORM-DELTA-0001
  claim_or_implication: Search, sync and connector results are relevance-oriented and should not be assumed to be complete branch/ref/PR enumerations.
  confidence_or_status: official_and_live_evidence_consistent
  mnemosyne_use: no-write evidence taxonomy
  not_execution_source: true

- evidence_id: EVID-2026Q3-PCAD-0009
  source_report: RPT-2026Q3-PLATFORM-DELTA-0001
  claim_or_implication: Long cross-conversation artifacts should be delivered file-first; requested low-risk artifacts should be generated immediately when no further authorization is required.
  confidence_or_status: candidate_workflow_guidance
  mnemosyne_use: Issues #170/#171 repair
  not_execution_source: true

- evidence_id: EVID-2026Q3-PCAD-0010
  source_report: RPT-2026Q3-PLATFORM-DELTA-0001
  claim_or_implication: Target-project business guidance loading should be reviewed separately from Issues #170/#171 and may use project-local guidance plus a trimmed Mnemosyne operator appendix.
  confidence_or_status: candidate_guidance; HO-GUIDANCE-001 remains open
  mnemosyne_use: future handoff-guidance adjudication
  not_execution_source: true
```

## DR6 corrections and limitations

- Issue #171 is the immediate low-risk artifact-generation issue, not `HO-GUIDANCE-001`.
- The original report says connected apps were not used in its execution environment.
- Its repository read manifest lists only README and Issues #170/#171; exact repository path mappings were maintainer-reviewed separately.
- Original Deep Research `turn...` citation markers may not be portable in GitHub; see the cycle `source-manifest.md`.
- No DR6 recommendation is automatically approved as an execution-source rule.
