# Fable5 Research Delivery Status

> Non-execution-source live status for the Mnemosyne frontier-clarification Stage-A tasks. `current/human-approved-spec.md` remains the only Mnemosyne execution source.

```yaml
status_id: MNEMOSYNE-FABLE5-RESEARCH-DELIVERY-STATUS-006
created_by_task: MNEMOSYNE-184
last_updated_by_task: MNEMOSYNE-195
repository: 08822407d/Mnemosyne
workflow: notes/research-operations/claude-fable5-project-knowledge-research-v0.4.md
ready_queue: handoff/fable5-ready/
staged_plan: notes/research-plans/2026Q3-frontier-clarification-validation-fable5-staged-plan-v0.5.md
A1_probe_adjudication: notes/adjudications/fable5-A1-R0-project-knowledge-search-mode-adjudication-2026-08-07.md
status: A1_PAUSED_SINGLE_INVOCATION_V0_4_PREPARED_A2_DEFERRED
execution_source_modified: false
validation_executed: false
Meta_Agent_route_imported: false
non_FABLE_health_review_imported: false
```

## 1. Run history

```yaml
A1_run_001:
  surface: ordinary_chat_GitHub_then_Research
  result: INPUT_OR_REPOSITORY_INTEGRITY_FAILURE
  Research_non_task_inputs_accessible: 0_of_18
  substantive_report_received: false
  operator_reported_cost_USD_approx: 8

A1_Project_knowledge_probe:
  surface: new_one_run_Project_Files_plus_Research
  Research_can_search_Project_knowledge: PASS
  required_manifest_paths_locatable: 22_of_22
  canonical_specification_final_heading: observed
  package_identity: PASS
  Project_Search_mode: true
  byte_complete_or_exhaustive_read: NOT_ATTESTABLE
  external_web_sources: 0
  repository_write_reported: false
  substantive_audit_started: false
  operator_reported_cost_USD_approx: 7
  low_cost_probe_gate: FAIL
  identical_rerun: prohibited
```

The additional same-task `OPERATOR.md` in the probe Project was an operator file-selection mistake, not a Fable or Search-mode defect. Future O0 setup requires zero extra files.

## 2. Product-surface conclusion

```yaml
ordinary_chat_connector_inheritance_to_Research:
  supported: false_for_run_001

Project_Files_to_Project_knowledge_in_Research:
  path_access_supported: true
  Search_mode_expected_when_content_large: true
  byte_complete_read_attestable: false
```

The original access problem is materially solved by Project knowledge. The v0.3 `complete_read` Boolean and separate paid R0 are retired.

## 3. Current execution intent

```yaml
A1:
  task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
  display_name: MNE-DR-001 验证包审计
  state: PAUSED_QUOTA_READY_NOT_SELECTED
  current_execution_requested: false
  current_execution_required: false
  active_execution_contract: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.4.md
  Project_file_count: 22
  separate_paid_visibility_probe: prohibited
  Research_invocations_after_selection: 1

A2:
  task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
  display_name: MNE-DR-002 表面威胁
  state: DEFERRED_PENDING_VALID_A1_ADJUDICATION
  current_execution_requested: false
  current_execution_required: false
  active_execution_contract: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.4.md
  Project_file_count: 15

external_execution_or_quota_authorized_by_readiness_alone: false
```

## 4. v0.4 execution architecture

```yaml
O0_operator_setup:
  Research_quota: none
  verifies:
    - new_Project_zero_prior_chats
    - exact_file_set_no_extras
    - sync
    - visible_model_and_effort
    - Search_mode_indicator
    - connectors_and_write_tools_disabled

single_Research_invocation:
  G0:
    role: Project_Search_mode_semantic_coverage
    external_web_before_PASS: prohibited
    byte_complete_claim: prohibited
  G1:
    role: complete_substantive_report
    allowed_only_after_G0_PASS_same_invocation: true
```

G0 reports path resolution, identity markers, terminal markers, required IDs/heading maps, gaps, and retrieval limitations. It does not claim every byte was loaded simultaneously.

## 5. Cost and stop controls

```yaml
cost_controls:
  separate_paid_probe: prohibited
  one_Research_invocation_per_selected_task: true
  source_count_target: none
  external_web_before_G0_PASS: prohibited
  identical_failed_configuration_retry: prohibited
  automatic_A2: prohibited
```

The operator cancels if broad external-web harvesting begins before G0 completes. Internal Project Search activity is expected.

## 6. Route state

```yaml
frontier_clarification_validation:
  package_merged: true
  A1_access_surface_empirically_supported: true
  A1_substantive_report_received: false
  A2_substantive_report_received: false
  execution_surface_selected: false
  V0_authorized: false
  V0_executed: false
  V1_authorized: false
  V1_executed: false

route_separation:
  Meta_Agent_product_build: dedicated_repository_separate_route
  non_FABLE_health_review: separate_conversation_not_imported
```

## 7. Safe next gate

```yaml
safe_next_action:
  current:
    - human_review_and_merge_MNEMOSYNE_195_PR_or_request_changes
  later_after_quota_and_explicit_user_selection:
    - run_A1_once_under_v0_4
    - return_complete_G0_ledger_and_G1_report
    - perform_frontier_repository_bound_adjudication
  A2:
    - remain_deferred_until_valid_A1_adjudication
  automatic_research_execution: false
  automatic_surface_selection: false
  automatic_V0_or_V1: false
```
