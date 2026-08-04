# Fable5 Research Delivery Status

> Non-execution-source live status for the Mnemosyne frontier-clarification Stage-A Fable5 tasks. `current/human-approved-spec.md` remains the only Mnemosyne execution source.

```yaml
status_id: MNEMOSYNE-FABLE5-RESEARCH-DELIVERY-STATUS-005
created_by_task: MNEMOSYNE-184
last_updated_by_task: MNEMOSYNE-188
repository: 08822407d/Mnemosyne
verified_master_before_MNEMOSYNE_188: 5cc758caa6baf86de0cf67cda2d852724f5edbbb
workflow: notes/research-operations/claude-fable5-project-knowledge-research-v0.3.md
ready_queue: handoff/fable5-ready/
staged_plan: notes/research-plans/2026Q3-frontier-clarification-validation-fable5-staged-plan-v0.4.md
failed_run_cycle: raw/research-reports/cycles/2026Q3-frontier-clarification-validation-stage-a/manifest.md
operator_flow_guard: current/artifact-delivery-and-direct-generation-guard.md
execution_intent_guard: current/cross-conversation-execution-intent-and-operator-flow-guard.md
status: A1_Project_knowledge_Research_candidate_ready_after_merge_A2_deferred
execution_source_modified: false
validation_executed: false
Meta_Agent_target_modified: false
non_FABLE_health_review_modified: false
```

## 1. Work since A1 run 001

```yaml
A1_run_001:
  ordinary_chat_preflight: PASS
  canonical_task_complete_read: best_supported_true
  later_Research_non_task_inputs_accessible: 0_of_18
  result: INPUT_OR_REPOSITORY_INTEGRITY_FAILURE
  substantive_report_received: false
  operator_reported_cost_USD_approx: 8

MNEMOSYNE_186:
  preserved_failed_run: true
  v0_2_surface: ordinary_Fable_chat_Research_off
  role: conservative_fallback
  executed: false

MNEMOSYNE_187:
  execution_intent_guard_added: true
  A1_state: READY_NOT_SELECTED
  A2_state: DEFERRED_PENDING_A1_ADJUDICATION
  research_run_selected: false

MNEMOSYNE_188:
  current_change:
    - verify_current_official_Project_GitHub_Project_RAG_and_Research_facts
    - prepare_direct_Project_knowledge_Research_surface
    - add_R0_visibility_probe_before_R1_report
    - keep_A2_deferred_until_A1_adjudication
```

Meta-Agent PRs #242/#243 and Issue #244 occurred after the Pro-quota pause but belong to separate routes; they do not change this route's research questions, package or validation state.

## 2. Current product-fact basis

As reviewed on 2026-08-03 from official Claude documentation:

- selected GitHub files/folders added under Project Files become Project knowledge and can be synced;
- Project RAG is documented to work with Research;
- Research uses web and internal context and may consume quota faster;
- enabled connector tools may be invoked automatically, so unneeded/write-capable connectors should be disabled;
- Project files are subject to per-file and total-content limits, but the current exact task sets are small and the whole repository is not selected.

This supports a direct Project-knowledge candidate. It does not prove the user's current rollout will pass R0.

## 3. Current execution intent

```yaml
A1:
  task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
  state_after_MNEMOSYNE_188_merge: READY_NOT_SELECTED
  current_execution_requested: false
  current_execution_required: false
  future_selection: allowed_by_explicit_RUN_disposition
  active_execution_contract: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.3.md
  Project_file_count: 22
  R0_probe_required: true
  R1_allowed_only_after_R0_PASS: true

A2:
  task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
  state_after_MNEMOSYNE_188_merge: DEFERRED_PENDING_VALID_A1_ADJUDICATION
  current_execution_requested: false
  current_execution_required: false
  active_execution_contract: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.3.md
  Project_file_count: 15

external_execution_or_quota_authorized_by_readiness_alone: false
```

## 4. v0.3 execution surface

```yaml
surface:
  environment: separate_new_one_run_Project_per_task
  Project_prior_chats: 0
  Project_Files: exact_manifest_set_only
  whole_repository: prohibited
  Project_sync: required
  visible_model: Fable_5
  visible_effort: Max
  Research:
    R0: direct_Project_knowledge_visibility_probe
    R1: substantive_report_only_after_R0_PASS
  chat_level_GitHub_during_Research: disabled
  other_connectors_during_Research: disabled
  repository_write: prohibited
```

This differs materially from run 001: primary inputs are Project knowledge inside Research, not a prior ordinary-chat connector state.

## 5. R0/R1 result roles

```yaml
R0:
  may_support:
    - Research_direct_Project_knowledge_access
    - exact_input_binding
    - cost_and_surface_observation
  may_not_support:
    - package_finding
    - manual_surface_finding
    - V0_or_V1_decision

R1:
  report_role: non_execution_source_research_evidence
  automatic_authority: false
  maintainer_adjudication_required: true
```

R0 must use zero external web sources. If broad external collection starts before the Project-file gate completes, the operator cancels the probe.

## 6. Route state

```yaml
frontier_clarification_validation:
  package_merged: true
  A1_substantive_report_received: false
  A2_substantive_report_received: false
  execution_surface_selected: false
  V0_authorized: false
  V0_executed: false
  V1_authorized: false
  V1_executed: false

route_separation:
  Meta_Agent_product_build: separate_owner_conversation_not_imported
  non_FABLE_health_review: separate_conversation_not_imported
```

## 7. Safe next gate

```yaml
safe_next_action:
  current:
    - review_and_merge_MNEMOSYNE_188_PR_or_request_changes
  after_merge_user_choice:
    - SELECT_A1_R0_AND_CONDITIONAL_R1
    - DEFER_A1
  after_valid_A1_report:
    - frontier_repository_bound_adjudication
    - decide_whether_A2_remains_current_and_worth_quota
  automatic_research_execution: false
  automatic_A2_execution: false
  automatic_surface_selection: false
  automatic_V0_or_V1: false
```
