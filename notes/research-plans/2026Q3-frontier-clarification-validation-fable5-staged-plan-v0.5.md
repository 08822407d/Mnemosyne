# 2026Q3 Frontier-Clarification Validation — Fable5 Staged Plan v0.5

> Non-execution-source staged plan. It incorporates the completed A1 Project-knowledge probe, the Search-mode/cost adjudication, and the v0.4 single-invocation workflow. It does not select or execute research, spend quota, amend the validation package, or authorize validation.

```yaml
plan_id: MNEMOSYNE-FCV-FABLE5-STAGED-PLAN-001
version: 0.5.0
created_by_task: MNEMOSYNE-195
status: prepared_paused_not_selected
supersedes:
  - notes/research-plans/2026Q3-frontier-clarification-validation-fable5-staged-plan-v0.4.md
workflow: notes/research-operations/claude-fable5-project-knowledge-research-v0.4.md
```

## 1. Current state

```yaml
A1:
  task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
  display_name: MNE-DR-001 验证包审计
  run_001: failed_closed_connector_transition
  Project_knowledge_probe:
    path_access: PASS
    semantic_exhaustiveness: NOT_ATTESTABLE_UNDER_SEARCH_MODE
    cost_gate: FAIL
    operator_reported_cost_USD_approx: 7
  valid_substantive_report: absent
  state: PAUSED_QUOTA_READY_NOT_SELECTED
  active_contract: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.4.md

A2:
  task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
  display_name: MNE-DR-002 表面威胁
  attempts: 0
  state: DEFERRED_PENDING_VALID_A1_ADJUDICATION
  active_contract: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.4.md
```

## 2. Stage order

```text
Stage 0 — no-quota Project setup receipt
  -> Stage 1 — one A1 Research invocation
       G0 semantic coverage
       G1 substantive audit only after G0 PASS
  -> Stage 2 — frontier adjudication of A1
  -> Stage 3 — decide whether A2 remains current and worth quota
  -> Stage 4 — optional one A2 Research invocation
       G0 semantic coverage
       G1 substantive threat model only after G0 PASS
  -> Stage 5 — execution-surface decision
  -> later V0/V1 only under separate authorization
```

## 3. Cost and non-repetition rules

```yaml
- do_not_repeat_the_completed_full_A1_Project_knowledge_probe
- do_not_run_a_separate_paid_visibility_probe
- use_one_Research_invocation_per_selected_task
- no_external_web_before_semantic_coverage_PASS
- no_source_count_target
- no_automatic_retry
- no_automatic_A2
```

## 4. Selection gates

A1 may run only after a future response explicitly states a `RUN_*` disposition and the user accepts quota use.

A2 may run only after:

- a valid A1 report exists;
- frontier adjudication is complete;
- package/manual-surface inputs remain current;
- A2 remains decision-relevant;
- the user separately accepts quota use.

## 5. Paused work that remains prohibited

```yaml
- validation_execution
- real_or_private_data
- Meta_Agent_route_import
- non_FABLE_health_review_takeover
- V0_or_V1_authorization
- package_amendment_without_A1_adjudication
- exact_backend_claim
```

## 6. Resume condition

```yaml
resume_when:
  - Fable_quota_is_available
  - user_explicitly_selects_A1
  - current_product_surface_has_not_materially_changed_or_is_reverified

until_then:
  A1: PAUSED_READY_NOT_SELECTED
  A2: DEFERRED
  repository_preparation: complete
```
