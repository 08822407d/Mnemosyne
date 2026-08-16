# V2 Run Manifest and Result Template

> Templates only. Empty fields are not authorization. A future run package must freeze exact values and receive separate Owner approval.

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-RUN-RESULT-TEMPLATE-001
status: template_not_run_authorization
```

## 1. Owner run-selection record

```yaml
Owner_run_selection:
  decision_id:
  selected_stage: V2_A | V2_B | V2_C
  selected_cells: []
  sentinel_only: true | false
  selected_repositories: []
  visibility_and_material_class:
  controller_surface:
  worker_surfaces: []
  visible_model_or_agent_labels: []
  external_quota_authorized:
  connector_or_app_changes_authorized:
  retry_authorized: false
  retention_and_cleanup:
  result_storage:
  authorization_text_verbatim:
```

## 2. Controller receive

```yaml
controller_receive:
  validation_id:
  package_id:
  package_version:
  selected_stage:
  selected_cells: []
  run_id:
  repository_receipts:
    - repository:
      role:
      default_branch:
      expected_base_sha:
      observed_base_sha:
      visibility:
      material_class:
  protected_repository_before_refs: []
  selected_product_surfaces: []
  permission_receipts: []
  unresolved_inputs: []
  receive_result: PASS | BLOCKED
```

## 3. Task/branch/PR map

```yaml
branch_and_task_map:
  run_id:
  controller_branch:
  tasks:
    - task_id:
      cell_id:
      repository:
      base_sha:
      canonical_branch:
      canonical_PR:
      writer:
      exact_write_set: []
      read_and_version_set: []
      generated_or_derived_effects: []
      shared_or_global_objects: []
      semantic_contracts: []
      predecessor_identity:
      authorization_ref:
      expected_disposition:
```

## 4. Per-cell result

```yaml
cell_result:
  validation_id:
  run_id:
  stage:
  cell_id:
  task_ids: []
  selected: true | false
  input_identities: []
  actual_branches_and_PRs: []
  actual_changed_paths: []
  observed_read_version_identities: []
  generated_or_derived_effects_observed: []
  semantic_checks:
    - check_id:
      artifact_identity:
      evidence_strength:
      result:
  merge_or_interleaving_orders: []
  expected_behavior:
  observed_behavior:
  mechanical_checks: {}
  evidence_strength:
    declared:
    artifact_present:
    statically_inspected:
    mechanically_verified:
    runtime_executed:
    runtime_passed:
    independently_reproduced:
    platform_signed_or_independently_attested:
    known_limitations: []
  incidents: []
  unresolved_gaps: []
  provisional_executor_disposition:
    value: CELL_PASS | EXPECTED_NEGATIVE_OBSERVED | CELL_FAIL | BLOCKED | DISPUTED
    reason:
  repository_write_performed: true | false
  prohibited_repository_write_performed: true | false
  validation_worker_architecture_change_performed: false
  automatic_retry_performed: false
```

## 5. Ordered-step record for V2-B

```yaml
ordered_step_result:
  run_id:
  cell_id:
  step_id:
  task_id:
  repository:
  observed_base_identity:
  predecessor_result_identity:
  predecessor_identity_revalidated:
  exact_write_set: []
  publication_identity:
  result: SUCCESS | FAILED | BLOCKED | NOT_RUN
  partial_state_after_step:
  recovery_selected:
  recovery_authorization_ref:
  recovery_result_identity:
  human_gate_ref:
  limitations: []
```

## 6. Incident record

```yaml
incident:
  incident_id:
  run_id:
  stage:
  cell_id:
  detected_at:
  category:
    - executor_deviation
    - fixture_or_profile_defect
    - tool_or_product_limitation
    - candidate_or_amendment_defect
    - insufficient_evidence
    - authorization_or_material_blocker
    - unresolved
  exact_state_identities: []
  automatic_actions_stopped:
  evidence_preserved:
  human_or_Pro_gate:
  repair_attempted: false
  historical_evidence_rewritten: false
```

## 7. Mechanical summary

```yaml
mechanical_summary:
  run_id:
  common_checks_M0_M17: {}
  V2_A_checks: {}
  V2_B_checks: {}
  V2_C_checks: {}
  protected_repository_no_write_results: []
  all_selected_checks_accounted_for:
  disputed_checks: []
  mechanical_disposition:
```

## 8. Stage result bundle

```yaml
stage_result_bundle:
  validation_id:
  package_id:
  run_id:
  selected_stage:
  selected_cells: []
  source_repository_identities: []
  controller_identity:
  worker_identities: []
  product_surface_receipts: []
  permission_receipts: []
  cell_result_refs: []
  mechanical_summary_ref:
  incident_ledger_ref:
  partial_states: []
  limitations: []
  provisional_executor_disposition:
    value:
    reason:
  fresh_Pro_adjudication:
    status: pending
    value: null
  Owner_architecture_decision:
    status: pending
    value: null
  validation_execution_only: true
  production_readiness_proven: false
  real_target_adoption_authorized: false
```

## 9. Post-run no-write and cleanup template

```yaml
post_run_closeout:
  protected_repository_after_refs: []
  before_after_comparisons: []
  claim_scope:
    named_repositories: []
    named_refs: []
    time_window:
    accessible_action_surfaces: []
  synthetic_branches_and_PRs: []
  retained_until:
  cleanup_authorized:
  cleanup_completed:
  exact_result_storage:
  unresolved_retention_obligations: []
```

## 10. Reporting constraints

- Raw controller and worker states remain historical evidence.
- Fresh Pro and Owner fields remain pending until their actual decisions occur.
- A correct rejection/stop in a negative cell may be a cell PASS, but the report must say what was rejected and why.
- A stage PASS is limited to the selected fixture, cells, identities and evidence strength.
- No result self-authorizes another stage, architecture modification or real-target adoption.
