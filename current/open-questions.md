# Open Questions

## MNEMOSYNE-068 Meta-Agent first-target intake follow-up

- Meta-Agent target selection:
  - status: selected_for_draft_manifest_preparation_by_user_confirmation
  - target_project_id_candidate: meta-agent
  - note: this does not approve real dry-run, workspace creation, material ingestion, or target repository write.
- Meta-Agent intake draft:
  - status: ingested_by_MNEMOSYNE-068
  - path: `notes/first-target-project-intake-records/meta-agent/meta-agent-target-project-selection-complete-draft.yaml`
- MNEMOSYNE-068 Meta-Agent draft run manifest package:
  - status: draft_for_user_review
  - path: `notes/first-target-project-intake-records/meta-agent/meta-agent-first-target-draft-run-manifest-package.md`
  - note: draft manifest package is not user-approved for real dry-run.
- Target-project intake filling guide:
  - status: created_by_MNEMOSYNE-068
  - note: non-execution-source guidance for completing target intake consistently; not an execution-source requirement by itself.

- Final manifest candidate preparation approval:
  - status: approved_by_user_in_MNEMOSYNE-076_for_preparation_only
  - path: `notes/first-target-project-intake-records/meta-agent/meta-agent-final-manifest-candidate-approval-for-preparation-record.md`
  - note: actual dry-run execution remains unapproved.
- Controlled dry-run preparation package:
  - status: created_by_MNEMOSYNE-076
  - preparation_plan: `notes/first-target-project-intake-records/meta-agent/meta-agent-controlled-dry-run-preparation-plan-v0.1.md`
  - evidence_plan: `notes/first-target-project-intake-records/meta-agent/meta-agent-controlled-dry-run-evidence-and-no-write-proof-plan-v0.1.md`
  - operator_prompt_package: `notes/first-target-project-intake-records/meta-agent/meta-agent-controlled-dry-run-operator-prompt-package-v0.1.md`
- Actual controlled dry-run execution:
  - status: not_approved
  - next_decision_options:
    - approve_actual_controlled_dry_run_execution
    - request_preparation_revision
    - defer_dry_run
    - continue_external_requirements_analysis
- Post-076 current-route sync:
  - status: repaired_by_MNEMOSYNE-077
  - note: live route now points to preparation package / actual-execution decision, not final-manifest-candidate approval.
- Still unresolved before real dry-run:
  - target_runtime_truth_source
  - final run manifest approval
  - final safe input policy approval
  - operator confirmation
  - workspace creation approval if needed
  - no-target-write proof
- Post-068 temporal sync:
  - status: repaired_by_MNEMOSYNE-069
  - note: older checkpoints should not be rewritten to imply Meta-Agent had been selected before MNEMOSYNE-068; Meta-Agent selection is a current post-068 state only.
- Meta-Agent dry-run nature:
  - status: clarified_by_MNEMOSYNE-069
  - note: planned dry-run is a controlled no-target-write real-target evaluation/design-package-generation run; it is not direct operational memory-system installation or target repository write for a Meta-Agent memory system.
- Meta-Agent requirements-analysis alignment:
  - status: external_alignment_ingested_for_manifest_revision_by_MNEMOSYNE-071
  - alignment_verdict: READY_FOR_MNEMOSYNE_MANIFEST_REVISION
  - note: external alignment package has been received and ingested for the narrow purpose of manifest revision; requirements analysis remains incomplete and is not sufficient for real dry-run approval, workspace creation, target material ingestion, target repository write, or memory-system build.
- Meta-Agent draft package contamination guard:
  - status: created_by_MNEMOSYNE-070
  - path: `notes/first-target-project-intake-records/meta-agent/meta-agent-analysis-alignment-guard.md`
  - note: draft package is a provisional pre-analysis scaffold, not completed requirements analysis, approved design spec, final build plan, operational memory-system installation, or approved real dry-run manifest.
- External alignment package:
  - status: ingested_by_MNEMOSYNE-071
  - path: `notes/first-target-project-intake-records/meta-agent/meta-agent-requirements-analysis-handoff-intake-alignment-package.md`
  - verdict: READY_FOR_MNEMOSYNE_MANIFEST_REVISION
- Revised draft manifest package v0.2:
  - status: created_by_MNEMOSYNE-071
  - path: `notes/first-target-project-intake-records/meta-agent/meta-agent-first-target-draft-run-manifest-package-v0.2.md`
  - note: current revised draft for user review only; not approved for real dry-run.
- Requirements analysis:
  - status: incomplete
  - note: requirements analysis remains incomplete; sufficient for manifest revision but not real dry-run approval, workspace creation, target material ingestion, target repository write, or memory system build.
- Next user decision:
  - status: awaiting_user_decision
  - options:
    - approve_v0_2_as_revised_draft_for_review_only
    - request_revision
    - reject_current_draft
    - continue_external_requirements_analysis
- Post-071 current-route sync:
  - status: repaired_by_MNEMOSYNE-072
  - note: high-signal current route now points to v0.2 and no longer asks for an external alignment package as if it were missing.
- v0.2 review-only approval:
  - status: approved_by_user_in_MNEMOSYNE-073
  - path: `notes/first-target-project-intake-records/meta-agent/meta-agent-v0.2-review-only-approval-record.md`
  - note: approved as review/preparation baseline only; not approved for real dry-run.
- Post-v0.2 next approval gates:
  - status: created_by_MNEMOSYNE-073
  - path: `notes/first-target-project-intake-records/meta-agent/meta-agent-post-v0.2-next-approval-gates.md`
  - unresolved:
    - target_runtime_truth_source
    - final_safe_input_policy
    - operator_no_target_write_confirmation
    - workspace_decision
    - final_run_manifest_next_action
- Post-v0.2 gate decision record:
  - status: created_by_MNEMOSYNE-074
  - path: `notes/first-target-project-intake-records/meta-agent/meta-agent-post-v0.2-next-gate-decision-record.md`
- Final run manifest candidate:
  - status: created_by_MNEMOSYNE-074
  - path: `notes/first-target-project-intake-records/meta-agent/meta-agent-final-run-manifest-candidate-v0.1.md`
  - note: candidate for user review only; not approved for real dry-run.
- Final manifest candidate next decision:
  - status: superseded_by_MNEMOSYNE-076_preparation_approval
  - note: final manifest candidate was approved for preparation only; live next decision is actual controlled dry-run execution / preparation revision / defer / continue analysis.



> Current execution source remains `current/human-approved-spec.md`. This file is not execution source.

## Current corrections

- Recovered light prompts are no longer a future hypothetical; MNEMOSYNE-038 recovered and indexed them.
- R4/R5 route-selection wording is superseded; use the MNEMOSYNE-044 coverage map for D-01–D-07 promotion/reflection status.
- DR1 research priority is answered for the current cycle; DR1 research and ingestion are complete.
- OP-09 and OP-10 remain partially answered by DR1, not closed.
- OP-08 remains open/partially addressed as a broader privacy/redaction/access-control question.
- Repository public/private selection is not an open defect question because visibility is user-controlled. Verify visibility before imports and apply the safety gate.
- D-promotion questions point to `notes/MNEMOSYNE-031-D01-D07-execution-source-coverage-map.md`.
- MNEMOSYNE-048 ordinary Mnemosyne conversation verification returned PASS and created onboarding/review instruments.
- The pre-050 fresh ordinary replay was user-supplied and verified PASS for the pre-050 package.
- MNEMOSYNE-050 changes the onboarding/replay/check semantics, so the prior replay does not close the post-050 gate.
- MNEMOSYNE-053 answered the replay protocol update by adding post-053 scoring/review semantics.
- Post-MNEMOSYNE-053 fresh ordinary Thinking replay returned maintainer-reviewed PASS with `quality_band: strong` and normalized score 95.9; the replay-quality portion of the first-target dry-run gate is satisfied.
- MNEMOSYNE-055 synchronized the post-053 replay reviewed PASS and repaired stale live post-050 gate wording.
- Scorecard weights/thresholds remain recalibration candidates after more evidence.


## MNEMOSYNE-066 PRO-04 / DR5 first-real-dry-run evaluation follow-up

- PRO-04 v2 intake form:
  - status: ingested_by_MNEMOSYNE-066
  - verdict: READY_FOR_MAINTAINER_REVIEW
  - note: forms support first target selection and approval intake; they do not select target, create workspace, ingest materials, or start dry-run.
- DR5 first-real-dry-run evaluation framework:
  - status: evidence_ingested_by_MNEMOSYNE-066
  - report_id: RPT-2026Q2-FTDRE-0001
  - note: real dry-run success requires evidence-backed, authority-bounded, no-target-write validation; artifact polish alone is insufficient.
- First real dry-run scorecard:
  - status: support_instrument_created_by_MNEMOSYNE-066
  - note: critical blockers override score; PASS does not mean production-ready, target repository write approval, or global rule update approval.
- Post-066 current-state sync:
  - status: repaired_by_MNEMOSYNE-067
  - note: MNEMOSYNE-066 created the required support instruments, but maintainer verification found active-context/handoff high-signal current-route wording still lagged; MNEMOSYNE-067 repairs that sync.
- Next user-facing route:
  - status: ready_after_MNEMOSYNE-067_maintainer_review
  - note: ask user for first target selection using intake forms; do not request raw material upload yet.
- DR3:
  - status: deferred
  - note: project workspace/delivery-package industry-practice research remains optional after actual target intake/dry-run evidence clarifies need.
- OP-08:
  - status: still_not_closed
  - note: DR4/DR5 and support instruments strengthen v0.1 governance, but broader privacy/redaction/access-control remains open.

## Current open questions

- Post-MNEMOSYNE-053 fresh replay reviewed PASS has been synchronized by MNEMOSYNE-055; remaining first dry-run blockers are user target selection, authority/safe input/no-target-write approval, and approved run manifest.
- Which first target project will be selected after post-053 replay reviewed PASS? Meta-Agent selected for draft manifest preparation only; no real dry-run approved.
- What authority/safe input/no-target-write approvals, source map, and approved run manifest will the user provide? No real target-project dry-run has occurred; no target materials have been uploaded/ingested; no target repository has been written.
- Should any D-01/D-03/D-04/D-05 candidate wording be promoted later? (separate approval only)
- OP-08 remains partially addressed; OP-09/OP-10 remain partially answered by DR1.
- OP-08: What broader privacy/redaction/access-control rule should govern original-source materials if sensitive content appears?
  - status: partially_addressed_by_MNEMOSYNE_043
- OP-09: Can current models reliably perform memory-system testing / debugging / root-cause diagnosis?
  - status: partially_answered_by_DR1
- OP-10: Are there mature industry practices or successful examples for memory-system testing/debugging in AI-Agent teams?
  - status: partially_answered_by_DR1
- OP-11: When should handoff-local exceptions be promoted into global execution-source changes, and what approval form is required?


## MNEMOSYNE-056 target-project workspace boundary questions

- Should `target-projects/` become the standard root for all target-project workspaces inside the Mnemosyne repository?
  - status: answered_by_MNEMOSYNE-057
  - note: default root is `target-projects/<target_project_id>/`, unless user approves an exception.
- Should target-specific Mnemosyne-generated intermediate work live under each target project's own workspace instead of global notes?
  - status: answered_by_MNEMOSYNE-057
  - note: high-level rule approved; detailed layout remains a non-execution-source proposal/reference.
- Where should target-project user originals, raw requirements, restatements, redactions, and user decisions live?
  - status: partially_answered_by_MNEMOSYNE-057
  - note: default policy approved in principle; actual storage of originals requires per-target safety/visibility/user approval.
- How should Mnemosyne-global lessons cite target-specific examples without promoting target-specific design into global policy?
  - status: answered_by_MNEMOSYNE-057_at_high_level
  - note: use stable path plus labels; global promotion still needs candidate review and user approval.
- Should future first-target dry-run folder conventions move from `notes/target-project-dry-runs/<dry_run_id>/` to `target-projects/<target_project_id>/04-dry-runs/<dry_run_id>/` after user approval?
  - status: answered_by_MNEMOSYNE-057_for_future_runs
  - note: future approved target dry-run outputs should be target-scoped after workspace approval; no real workspace created yet.

## MNEMOSYNE-058 / 059 PRO-01 and DR4 follow-up

- PRO-01 audit status:
  - status: processed_by_MNEMOSYNE-058
  - note: stale first-dry-run support instrument paths/replay references repaired; manifest authority/status fields strengthened.
- DR4 user-input governance report:
  - status: evidence_ingested_by_MNEMOSYNE-058
  - report_id: RPT-2026Q2-UIG-0001
  - note: originals/raw requirements default outside Git; user-approved decisions, redacted excerpts, synthetic substitutes, and safe external pointers/manifests are the preferred in-repo layer.
- DR4 corrected Deep Research prompt:
  - status: prompt_original_ingested_by_MNEMOSYNE-059
  - prompt_id: PROMPT-2026Q2-UIG-0001
  - prompt_path: `raw/research-reports/cycles/2026Q2-user-input-governance/research-prompts/originals/DR4_user_originals_requirements_redaction_governance_prompt.md`
  - note: prompt requires full report body in final Deep Research answer and forbids summary+download-only report delivery.
- Deep Research output delivery:
  - status: behavior_rule_repaired_by_MNEMOSYNE-058
  - note: future Deep Research prompts must require full report body in the final answer/report body; downloadable files may be backup only and must not be the sole canonical report.
- Does OP-08 close?
  - status: not_closed
  - note: DR4 informs v0.1 target-input governance, but broader privacy/redaction/access-control remains open until separately approved.
- 059 result-record discrepancy:
  - status: repaired_by_MNEMOSYNE-060
  - note: `notes/codex-task-results/MNEMOSYNE-059-result.md` claimed MNEMOSYNE-058/059 were present in all current-state files, but maintainer verification found the intended open-questions follow-up section absent; this section is the repair.

## MNEMOSYNE-061 staged PRO/DR prompt-batch guidance

- Should future Pro/Deep Research prompt packs be generated all at once?
  - status: answered_by_MNEMOSYNE-061
  - note: default is dependency-aware staged generation; downstream prompts are generated only after upstream batch results are reviewed and repaired when dependency risk exists.

## MNEMOSYNE-062 / 063 / 064 B1 PRO-02 / PRO-03 follow-up

- MNEMOSYNE-062:
  - status: blocked_missing_payloads
  - note: no PRO-02/PRO-03 ingestion or hardening occurred because payload files were absent from `manual-import-inbox`.
- PRO-02 synthetic smoke-test:
  - status: ingested_by_MNEMOSYNE-063
  - verdict: PASS_WITH_WARNINGS
  - note: synthetic controls were sufficient and no boundary violation occurred; synthetic result does not close real target dry-run gate.
- PRO-03 adversarial failure test:
  - status: ingested_by_MNEMOSYNE-063
  - verdict: REPAIR_RECOMMENDED
  - note: repository is not currently unsafe, but small deterministic controls were applied before real target dry-run/material intake.
- MNEMOSYNE-063 current-state sync discrepancy:
  - status: repaired_by_MNEMOSYNE-064_and_MNEMOSYNE-065
  - note: `notes/codex-task-results/MNEMOSYNE-063-result.md` claimed current-state files were updated, but maintainer verification found compact state still stopped at MNEMOSYNE-061; MNEMOSYNE-064 updated active-context/TODO/handoff but left this B1 follow-up in historical open-questions; MNEMOSYNE-065 places this section in the current open-questions portion.
- B1 downstream prompt status:
  - status: ready_for_maintainer_to_generate_next_batch_after_MNEMOSYNE-065_review
  - note: do not generate or run PRO-04 / DR3 / DR5 until maintainer verifies MNEMOSYNE-065; after acceptance, next recommended batch is PRO-04 only unless maintainer decides otherwise.
- OP-08:
  - status: still_not_closed
  - note: user-input governance, redaction/pointer controls, and manual-import classification are strengthened, but broader privacy/redaction/access-control remains open.

## Historical open-question list below

The material below is retained for history and may include superseded route wording. Use the current corrections above for live status.

# Open Questions

> MNEMOSYNE-031 final checkpoint records are non-execution-source review/restatement records. Current execution source remains `current/human-approved-spec.md`.

## answered

1. startup-instructions 应放在 `current/` 还是 `handoff/`？
   - 结论：当前放在 `handoff/startup-instructions.md`。

2. startup-instructions 是否应强制读取 `current-capability-boundaries`？
   - 结论：涉及能力边界、新机制设计、平台适配、目标项目设计时必须读取。

3. v0.1 是否已经足以支持新对话接手？
   - 结论：根据 `notes/startup-rehearsal-report.md`，当前结论为 pass，当前文件集足以支持新 ChatGPT / 新 Codex 任务仅依赖仓库文件接手。

4. startup-instructions 在新 ChatGPT / 新 Codex 接手演练中的可执行性是否足够？
   - 结论：根据 `notes/startup-rehearsal-report.md` 与 `notes/v0.1-independent-verification-report.md`，当前为可执行且足以支撑 v0.1 接手（PASS_WITH_WARNINGS）。

5. 用户是否接受 MNEMOSYNE-023 的 `PASS_WITH_WARNINGS` 结论，并允许进入 v0.2 第一方向选择？
   - 结论：用户接受 `PASS_WITH_WARNINGS`，其不阻断进入 v0.2。

6. v0.2 第一方向应选择哪个？
   - 结论：v0.2 第一方向选择 `self-improvement workflow`。

7. self-improvement workflow 的最小对象和模板是什么？
   - 结论：当前由 `notes/self-improvement-workflow.md` 和 `notes/self-improvement-template-pack.md` 提供基础流程与模板包。
   - 状态：已由 template pack 初步覆盖；是否拆分或小修见 open 区域。

8. 用户反馈和 Codex 任务结果如何进入 raw？
   - 结论：当前由 `notes/self-improvement-workflow.md` 定义基本流程，并由 `notes/self-improvement-template-pack.md` 提供 Raw Input 与 Codex Task Result Record 模板。
   - 状态：partially_answered；实际效果仍待用户 review。

9. Codex Task Result Record 是否需要固定模板？
   - 结论：当前由 `notes/self-improvement-template-pack.md` 中的 Codex Task Result Record Template 覆盖。
   - 状态：answered；是否小修见 open 区域。

10. 是否需要把重要 Codex 完成回复精简保存？
    - 结论：重要任务、异常任务、验证任务应保存精简结果记录；普通任务可不保存完整回复。
    - 状态：模板已由 `notes/self-improvement-template-pack.md` 初步覆盖；是否小修见 open 区域。

11. 是否需要为 similarity/conflict report 设计最小格式？
    - 结论：当前由 `notes/self-improvement-template-pack.md` 中的 Similarity / Conflict Check Template 覆盖。
    - 状态：answered；是否小修见 open 区域。

12. 是否需要为 user decision 设计固定记录格式？
    - 结论：当前由 `notes/self-improvement-template-pack.md` 中的 User Decision Record Template 覆盖。
    - 状态：answered；是否小修见 open 区域。

13. 是否先设计 AGENTS.md / CLAUDE.md，还是先设计目标项目模板？
    - 结论：当前先进入目标项目 intake / memory system design spec 模板设计；AGENTS.md / CLAUDE.md 留作后续。

14. 目标项目 intake 和 memory system design spec 应先做哪个，还是一起做？
    - 结论：MNEMOSYNE-027 选择一起创建基础模板包。

15. 是否先深化 delivery manifest，还是先选择第一个目标项目场景试用模板？
    - 结论：MNEMOSYNE-028 先深化 delivery manifest，已创建 `notes/delivery-manifest-template-pack.md`。

16. 是否先直接选择第一个目标项目场景，还是先建立 review / selection 准备文件？
    - 结论：MNEMOSYNE-029 先建立三类模板包 review 清单与首个场景选择矩阵。

17. 是否先做研究报告 summary / PDF 图表复核？
   - 结论：用户选择先做一次 D；MNEMOSYNE-030 建立 report summaries，MNEMOSYNE-030A 补齐 PDF figure review index 和状态同步。


18. 是否需要把 7 份研究报告的研究动机入库？
   - 结论：需要。MNEMOSYNE-030C 创建 `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`，用于解释 7 份报告为什么存在、服务什么设计问题、如何约束 Mnemosyne，以及为什么研究报告和 motivation 都不是执行源。
   - 状态：answered；motivation 已在 MNEMOSYNE-031 R1 由用户选择 B 接受，并保留 review notes。

19. 研究课题 prompt 原文应该放在哪里？
    - 结论：pro 深度研究 prompt 原文约定放在 `raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/AI_agent_external_persistent_memory_deep_research_prompt_pro.md`。
    - 状态：answered；pro prompt 文件已放入约定路径。

20. 6 个轻度研究 prompt 原文缺失时应如何处理？
    - 结论：不得编造原文；只记录 report title / summary 可确认的 topic title，并在 `research-prompt-index.md` 和 `report-topic-and-prompt-map.md` 中标记 `missing_original_prompt`。
    - 状态：answered。

21. 是否需要同步 research motivation / prompt mapping 到 current 索引与接手文件？
    - 结论：需要。MNEMOSYNE-030F 负责补齐 current 索引、active-context、handoff、todo、open-questions 的状态。
    - 状态：answered；MNEMOSYNE-030G-MANUAL 用于手工修正 030F 后仍残留的状态不同步。

22. 研究报告 review 是否应假定用户已通读和理解全部报告？
    - 结论：不应假定。研究报告主要供 Mnemosyne 元 Agent 作为高权重证据层使用；用户接受证据入口，不等于亲自验证全部报告结论。
    - 状态：answered。

23. MNEMOSYNE-031 是否需要加入用户设计构想重述？
    - 结论：需要。由于用户记忆不强且原始构想经过多轮讨论形成，应先由 AI 整理待重述清单，再由用户口语化重述，最后整理为 raw user intent evidence。
    - 状态：answered；用户重述不是原始需求、最终设计或执行源。

24. MNEMOSYNE-032 dry-run independent verification verdict 是什么？
    - 结论：PASS。
    - 依据：read-only independent verification checked `master`, execution-source boundary, protected-file conditions, missing prompt boundary, PDF review boundary, dry-run artifacts, Codex self-assessment consistency, and invalid-test conditions.
    - 状态：answered；dry-run artifacts remain validation evidence only, not execution source and not final design.

25. 是否需要在 first target 前建立 Idea Capture Buffer？
   - 结论：需要。用户希望任意新开对话也能继续 Mnemosyne 建设，且当前上下文巨大；Idea Capture Buffer 用于防止新想法丢失或直接污染 execution source。

## Answered in MNEMOSYNE-031 checkpoint

- R1 Research Motivation Review: answered; user decision B.
- R2 Research Prompts and Topic Mapping Review: answered; user decision B.
- R3 Report Summaries Review: answered; user decision B.
- R4A User Design Intent Restatement Prompt List: completed.
- R4B User Oral Restatement: answered; completed as 9 main records + 1 addendum.
- R4C User Design Intent Synthesis: answered; synthesis candidate draft generated, not execution source.
- R5 Final Combined Writeback Package: answered; generated, with final D-01 to D-07 decisions governed by the research review record.

## open


1. 用户是否接受 `notes/template-pack-review-and-first-scenario-selection.md`？
   - 说明：该文件已创建，用于 review 三类模板包并准备首个场景选择，但尚未经过用户 review。

2. 用户是否接受当前 `notes/delivery-manifest-template-pack.md`，是否需要小修？
   - 说明：`notes/delivery-manifest-template-pack.md` 已创建，但尚未经过用户 review。

3. 用户是否接受当前 `notes/target-project-memory-system-template-pack.md`，是否需要小修？
   - 说明：`notes/target-project-memory-system-template-pack.md` 已创建，但尚未经过用户 review。

4. 用户是否接受当前 `notes/self-improvement-template-pack.md`，是否需要小修？
   - 说明：template pack 已创建，但尚未经过用户最终 review。

5. self-improvement template pack 是否需要拆成多个独立模板文件？
   - 说明：当前先采用单文件模板包；是否拆分仍待用户 review 后决定。

7. 哪些 PDF 图表 / 图片需要优先人工复核？
   - 说明：RPT-2026Q2-0002 ~ RPT-2026Q2-0007 均为 pending_manual_review。

8. 人工复核结果是否会影响目标项目模板或 capability boundaries？
   - 说明：若复核发现关键差异，可能需要登记后续修正任务。

11. 第一个目标项目模板优先服务哪类场景？
   - 说明：候选场景包括长期研究、学习系统、源码学习、软件开发项目、AI Agent 项目、个人长期对话 / 知识管理、多 Agent 团队或混合未知场景，尚未由用户确认。

14. 是否需要更正式的隐私分级字段？
   - 说明：目标项目 intake 已包含 `privacy_level` 和 `sensitive_content_types`，但是否扩展为正式隐私分级体系仍待决定。

15. `raw/concept-origin-extract-001.md` 是否需要拆分成多个 raw record？
   - 说明：当前可按需回查；是否拆分仍待决定。

20. 完成 R4 / R5 后优先走哪条路线？
    - 说明：first dry-run 已通过 MNEMOSYNE-032 independent verification，final verdict 为 `PASS`；当前剩余路线为 PDF review、Idea Capture Buffer / candidate cleanup、template small fixes 或 memory-system testing/debugging feasibility research。
21. 如果未来找回轻度研究 prompt，是否补入 originals 并更新索引？
22. 是否需要把 prompt 原文与 report summary 的差异做 delta / review note？
23. 用户重述后哪些内容可进入 candidate requirements？
24. 哪些用户构想需要研究报告校验？
25. 哪些用户构想可能落后、过于理想化或与现有设计冲突？


## MNEMOSYNE-031 final open questions

- OP-01: What exact approval form is required before candidate material becomes execution source?
- OP-02: How abstract should the first storage backend design be?
- OP-03: What default directory names and lifecycle rules should task-private workspaces use?
- OP-04: What minimum index format should be used first?
- OP-05: Should each target project have a memory-system issue log and troubleshooting record?
- OP-06: How often should capability research be performed, and how should capability versions be named?
- OP-07: Which first reusable template should be built after Mnemosyne itself: software development, source-code explanation, or language learning?
- OP-08: What privacy/redaction/access-control rule should govern original-source materials if sensitive content appears?
  - status: partially_addressed_by_MNEMOSYNE_043
  - MNEMOSYNE-043 adds a manual-import safety default for public/unverified repository visibility, but does not close the broader privacy/redaction/access-control policy question.
- OP-09: Can current models reliably perform memory-system testing / debugging / root-cause diagnosis?
  - status: partially_answered_by_DR1
  - DR1 meaning: Models can assist with evaluation, review, classification, and diagnosis, but should not be the sole judge. Reliable diagnosis needs traces, file evidence, human review, regression checks, PR/diff evidence, and postmortem-style review.
- OP-10: Are there mature industry practices or successful examples for memory-system testing/debugging in AI-Agent teams?
  - status: partially_answered_by_DR1
  - DR1 meaning: No single mature end-to-end standard exists specifically for external persistent memory systems, but mature reusable sub-practices exist and can be combined.
- OP-11: When should handoff-local exceptions be promoted into global execution-source changes, and what approval form is required?
## MNEMOSYNE-033 Idea Capture Buffer open questions

- Idea Capture Buffer 的条目多久 triage 一次？
- Pro Deep Research 优先研究哪些 memory-system testing/debugging 问题？
- 哪些 PDF 图表 / 表格 / 图片应优先复核？
- 是否要先做 template review，还是 first real target dry-run？
- 哪些 idea 可以升级到 candidate requirements？
- 哪些 idea 需要用户 decision？

## MNEMOSYNE-033A exported conversation derived insight open questions

- 当前不同 ChatGPT 入口的模型能力差异如何影响 Mnemosyne 工作分工？
  - 说明：Custom GPT、普通 ChatGPT、Pro 强度、Deep Research 和 Codex Cloud 的能力与 UI 可能变化，应按当前事实动态核实，不应写成长期固定假设。
- Codex Cloud 当前使用哪个模型、是否可选模型，以及这个事实如何保持最新？
  - 说明：该问题影响 repo-editing / review / verification 分工；需要以当前产品状态和用户实际界面为准。
- 任务提示文件化交付是否应成为全局硬规则，还是仅针对长任务 / 高风险任务？
  - 说明：历史失败包括复制截断、嵌套 code fence、云端未同步和 stale branch；适用范围仍需用户确认。
- 哪些历史动机已被 raw / restatement 充分保存，哪些还需要单独 motivation record？
  - 说明：避免重复保存，也避免用户核心动机只留在对话上下文中。
- 完整对话导出是否应完整入库，还是只入 near-original extract / selected raw excerpts？
  - 说明：默认不完整入库；需权衡隐私、体积、重复污染、检索价值和旧任务文本误导风险。
- AI 回复在 raw/context evidence 中保存到什么粒度？
  - 说明：用户希望保留会影响后续构想演化的 AI 关键回应，但需控制隐私、冗余和过时分析污染。
- Idea Capture Buffer 多久 triage 一次、由谁触发、什么算“重要对话后”？
  - 说明：当前规则只说明可在重要对话或 Codex 任务后追加，仍需确定 cadence 和触发条件。
- 任务结果记录保存范围应如何定义？
  - 说明：是否只保存有警告、限制、失败、未完成、人工复核需求的精简记录，而不是保存所有 Codex 完成回复，仍需策略确认。

## MNEMOSYNE-036 construction-stage open questions

- How should HADB relate to raw records, candidate requirements, and `current/human-approved-spec.md`?
- When should a settled HADB require a clarification addendum during artifact generation?
- How should agent-operational artifacts be tested or verified for reproducible use by later agents?
- What minimum evidence is needed before indexing/retrieval acceleration becomes a real Mnemosyne mechanism?
- What cadence should research-to-improvement review use, and how should it map research findings to open questions and failure modes?
- Which real target projects should be used to test whether Mnemosyne's prototype memory-system designs actually work?


## MNEMOSYNE-040 DR1 memory-testing evidence open questions

- Which DR1 failure modes should become the first minimal memory issue log / drift review checklist?
- What minimal checklist should be used before or during the first target-project dry-run to test execution-source reading, handoff executability, active-context propagation, layer separation, uncertainty handling, artifact usability, and honest tool-capability boundaries?
- When, if ever, should optional deeper multi-model independent review research be reopened for template/review-package design?

## MNEMOSYNE-044 execution-source coverage map

- MNEMOSYNE-044 created `notes/MNEMOSYNE-031-D01-D07-execution-source-coverage-map.md` as a non-execution-source review/proposal artifact.
- Final D-01 to D-07 decisions remain authoritative checkpoint records in the MNEMOSYNE-031 review record.
- Only D-01 to D-07 content already reflected in `current/human-approved-spec.md` is currently executable.
- Unreflected or partially reflected promotion candidates require separate user approval before any spec change.
- Open review item: decide whether to promote the D-01, D-03, D-04, and D-05 candidate wording from the coverage map; do not treat that wording as approved until separately confirmed.

## MNEMOSYNE-051 / DR2 handoff-strategy implications

- What parts of DR2's handoff scoring rubric should be adopted before the first real target-project dry-run?
  - status: partially_adopted_by_MNEMOSYNE-053
  - note: DR2 scoring rubric has been provisionally adopted as `notes/handoff-replay-scorecard-v0.1.md`; which scorecard weights/thresholds should later be recalibrated remains open.
- Should the replay protocol be updated to incorporate DR2 scoring, and if so through a separate user-approved task?
  - status: answered_for_v0.1_by_MNEMOSYNE-053
  - note: Replay protocol was updated by MNEMOSYNE-053; future changes still require reviewed user-approved tasks.
- What minimum model/tool provenance fields are required for future handoff tests?
  - status: provisionally_defined_by_MNEMOSYNE-053
  - note: Minimum provenance fields were provisionally defined in `notes/handoff-replay-scorecard-v0.1.md` and `notes/first-target-project-fresh-replay-protocol.md`.
- Which DR2 recommendations should become candidate requirements, and which should remain research-gated?
  - status: partially_answered_open_for_v0.2
  - note: Cross-model thresholds, dual-review calibration, selected historical excerpts formal protocol, and automated handoff generation remain v0.2 / future / research-gated.
- Does DR2 change the required post-050 replay gate before first real target-project dry-run?
  - status: answered_by_user_approved_MNEMOSYNE-053
  - current_boundary: DR2 changed the current required gate only through user-approved MNEMOSYNE-053; the gate is now post-MNEMOSYNE-053 replay, not because research alone changed it.
- OP-09 and OP-10 are partially_informed_by_DR2 because DR2 discusses handoff replay scoring, model/tool provenance, and the limits of model-judge evaluation, but it does not close those questions.


## MNEMOSYNE-058 / 059 PRO-01 and DR4 follow-up

- PRO-01 audit status:
  - status: processed_by_MNEMOSYNE-058
  - note: stale first-dry-run support instrument paths/replay references repaired; manifest authority fields strengthened.
- DR4 user-input governance report:
  - status: evidence_ingested_by_MNEMOSYNE-058
  - report_id: RPT-2026Q2-UIG-0001
  - note: originals/raw requirements default outside Git; user-approved decisions, redacted excerpts, synthetic substitutes, and safe external pointers/manifests are the preferred in-repo layer.
- DR4 corrected Deep Research prompt:
  - status: prompt_original_ingested_by_MNEMOSYNE-059
  - prompt_id: PROMPT-2026Q2-UIG-0001
  - note: prompt requires full report body in final Deep Research answer and forbids summary+download-only report delivery.
- Deep Research output delivery:
  - status: behavior_rule_repaired_by_MNEMOSYNE-058
  - note: future Deep Research prompts must require full report body in the final answer/report body; downloadable files may be backup only and must not be the sole canonical report.
- Does OP-08 close?
  - status: not_closed
  - note: DR4 informs v0.1 target-input governance, but broader privacy/redaction/access-control remains open until separately approved.
