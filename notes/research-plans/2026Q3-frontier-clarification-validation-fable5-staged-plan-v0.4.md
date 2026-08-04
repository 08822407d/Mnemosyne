# Frontier Clarification Validation — Staged Fable5 Research Plan v0.4

> Non-execution-source plan. It supersedes v0.3 for Stage-A execution surface, selection and quota sequencing only. It does not execute Fable5, accept a report, modify the validation package, select a V0 surface or authorize validation.

```yaml
plan_id: FABLE5-FRONTIER-CLARIFICATION-VALIDATION-STAGED-PLAN-001
version: 0.4.0
created_by_task: MNEMOSYNE-188
status: A1_Project_knowledge_Research_candidate_ready_after_merge_A2_deferred
source_package: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
source_package_merge_commit: 67eb96d5317a2bb589236a4a8b2e75be2508d830
manual_candidate_merge_commit: 5e556c2a6dacb41d68bf6209dbf8156b92b79e72
foundational_research: complete_adjudicated
quota_execution_authority: user_only
```

## 1. Work completed before v0.4

- Foundational Pro and Fable reports were completed and adjudicated.
- The complete validation package was merged through PR #233.
- The manual surface candidate and initial Stage-A task design were merged through PR #234.
- Claude Project/GitHub delivery packets were merged through PR #236.
- Same-response operator-flow mirroring was merged through PR #238.
- A1 run 001 failed closed after Research could not access 18 required repository files.
- PR #239 preserved that failure and introduced an ordinary-chat v0.2 fallback.
- PR #241 made readiness, selection and execution intent explicit.
- No valid A1 report, A2 report, V0 result or V1 result exists.

## 2. Why v0.4 changes the surface

v0.2 avoided Advanced Research rather than repairing its input surface. Current official Claude documentation supports a more direct candidate:

```yaml
Project_GitHub_selection: selected_files_or_folders_become_Project_knowledge
Project_RAG: works_with_Research
Research: searches_internal_context_and_web
```

Therefore v0.4 uses exact one-run Project Files and a Research-direct visibility probe. It does not rely on a prior ordinary-chat GitHub receipt.

## 3. Stage-A task dispositions

### A1

```yaml
task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
state_after_MNEMOSYNE_188_merge: READY_NOT_SELECTED
execution_contract: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.3.md
operator: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/OPERATOR.md
Project_file_count: 22
R0_probe: required
R1_substantive_report: only_after_R0_PASS
Advanced_Research: used_directly_against_Project_knowledge
chat_level_GitHub_during_Research: disabled
```

The user may select A1 after the MNEMOSYNE-188 PR merges. Readiness alone does not spend quota.

### A2

```yaml
task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
state_after_MNEMOSYNE_188_merge: DEFERRED_PENDING_VALID_A1_ADJUDICATION
execution_contract: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.3.md
operator: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/OPERATOR.md
Project_file_count: 15
R0_probe: required_after_later_selection
R1_substantive_report: only_after_R0_PASS
```

A2 remains prepared but unselected because A1 may require amendments that change A2's audit object.

## 4. R0/R1 evidence semantics

```yaml
R0:
  purpose: prove_Research_direct_access_to_exact_Project_knowledge
  substantive_findings: prohibited
  external_web_collection: prohibited
  PASS_does_not_prove: audit_quality

R1:
  purpose: produce_complete_canonical_research_report
  allowed_only_after: R0_PASS
  report_authority: non_execution_source_evidence_only
```

A failed R0 stops the task and becomes surface evidence. It cannot support package or manual-surface findings.

## 5. Independence and contamination

- A1 and A2 use separate new Projects.
- Neither Project contains prior reports, prior chats, the other task or unrelated files.
- Project Files are exact manifest sets; the whole repository is not loaded.
- GitHub and other connectors are disabled for Research after Project Files are added.
- R0 is cancelled if it begins broad external collection before binding the internal files.

## 6. Stage B

The four Stage-B topics remain non-runnable:

```yaml
Stage_B:
  reviewer_independence: deferred
  V1_inference_and_thresholds: deferred
  no_write_context_isolation_evidence_equivalence: deferred
  portability_and_propagation: deferred
  generation_gate: valid_Stage_A_report_adjudication
```

## 7. Quota sequence

```yaml
recommended_sequence:
  1: merge_MNEMOSYNE_188_or_request_changes
  2: optionally_select_A1
  3: run_A1_R0
  4: only_if_R0_PASS_run_A1_R1
  5: return_and_adjudicate_A1
  6: decide_whether_A2_remains_current_and_worth_quota
  7: if_selected_run_A2_R0_then_R1

automatic_execution: false
automatic_quota_spend: false
automatic_A2_after_A1: false
```

## 8. Capability assessment

```yaml
capability:
  product_surface_repair_and_report_adjudication: FRONTIER_RECOMMENDED
  Project_file_selection_and_R0_receipt_check: HUMAN_plus_MECHANICAL
  A1_A2_independent_research: Fable_5_Max_requested
  final_package_or_surface_decision: FRONTIER_RECOMMENDED_plus_HUMAN
additional_Pro_Deep_Research: NOT_NEEDED
additional_same_topic_Fable_task_generation: NOT_NEEDED
```

## 9. Boundaries

This plan does not change the canonical research questions, validation package, manual surface candidate, Mnemosyne execution source, Meta-Agent route or non-FABLE health-review route.