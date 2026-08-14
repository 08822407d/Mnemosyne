# Run Manifest and Result Template

```yaml
package_id: MNE-TARGET-LIFECYCLE-VALIDATION-PACKAGE-002
file_role: run_identity_and_return_schema
status: prepared_not_executed
```

## 1. Run manifest

Create this object before any V0 write:

```yaml
validation_run_manifest:
  run_id:
  package_id: MNE-TARGET-LIFECYCLE-VALIDATION-PACKAGE-002
  package_version: 0.2.0
  candidate_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-002
  validation_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-VALIDATION-002

  authorization:
    disposition:
    phase_scope:
    decision_ref:
    allowed_actions: []
    prohibited_actions: []
    expires_with_run: true
    not_future_precedent: true

  date_or_window:
    started_at:
    completed_at:

  execution:
    actor:
    actor_kind:
    product_surface:
    visible_selection_verbatim:
    reasoning_setting_verbatim:
    backend:
      status: unknown_or_not_attestable
      reason:
    switch_history:
      status: confirmed_none | recorded | unknown
      evidence: []

  repository:
    full_name_or_store:
    visibility:
    default_branch:
    pinned_base_sha:
    fixture_commit:
    allowed_write_roots: []
    prohibited_repositories: []
    retention_plan:

  material_safety:
    class: public_synthetic_only
    real_target_material_present: false
    private_material_present: false
    credentials_present: false
    review_ref:

  phases:
    V0:
      authorized:
      executed:
      result:
    V1:
      authorized:
      executed:
      selected_scenarios: []
      result:

  artifacts:
    - ref:
      relation:
      immutable_identity:
        type:
        value:

  limitations: []
  omissions: []
```

## 2. V0 result

```yaml
V0_result:
  run_id:
  package_identity_pass:
  authorization_pass:
  repository_identity_pass:
  material_safety_pass:
  real_repository_no_write_baseline_recorded:
  open_lineage_enumeration_complete:
  blockers: []
  incidents: []
  disposition:
    value: V0_PASS_ELIGIBLE_FOR_SEPARATE_V1_DECISION | V0_BLOCKED_MISSING_AUTHORITY | V0_BLOCKED_MATERIAL_OR_VISIBILITY | V0_BLOCKED_IDENTITY_OR_NO_WRITE_PROOF | V0_PROTOCOL_DEFECT
    reason:
```

## 3. Task write contract instance

```yaml
task_write_contract:
  task_id:
  scenario_id:
  primary_target:
  authority_owner:
  primary_writer:
  authorization_ref:
  base_ref:
  exact_write_set: []
  read_or_dependency_set: []
  shared_or_repository_global_objects_touched: []
  conflicting_active_write_sets: []
  concurrency_class: target_local_disjoint | shared_object | repository_global | unknown
  decision: proceed | serialize | reconcile | blocked
  expected_changed_paths: []
  actual_changed_paths: []
  final_diff_verification_ref:
  violations: []
```

## 4. Scenario-attempt ledger

```yaml
scenario_attempt:
  scenario_id:
  attempt_id:
  retry_of: null
  exact_input_ref:
  input_identity:
  task_contract_refs: []
  context_or_run_ref:
  started_at:
  completed_at:

  actions:
    performed: []
    blocked: []

  output_refs:
    - ref:
      immutable_identity:

  repository_lineage:
    branches: []
    commits: []
    PRs: []

  mechanical_checks:
    M0_package_identity:
    M1_repository_material_identity:
    M2_canonical_task_lineage:
    M3_declared_actual_write_set:
    M4_concurrency_intersection:
    M5_authority_preservation:
    M6_parent_content_boundary:
    M7_change_documentation:
    M8_source_API_preservation:
    M9_backup_restore:
    M10_real_repository_no_write:
    M11_output_retry_identity:

  semantic_rubric:
    R1_authority_fidelity:
    R2_scope_concurrency_fidelity:
    R3_source_change_fidelity:
    R4_documentation_migration_adequacy:
    R5_deferral_fidelity:
    R6_provenance_recoverability:

  critical_failures: []
  corrections: []
  missing_facts: []
  executor_limitations: []

  disposition:
    value: SCENARIO_PASS | SCENARIO_PASS_WITH_NONCRITICAL_OBSERVATION | SCENARIO_FAIL_CANDIDATE_OR_SEMANTIC | SCENARIO_FAIL_EXECUTOR | SCENARIO_BLOCKED_MISSING_AUTHORITY_OR_FACT | SCENARIO_INVALID_PROTOCOL_OR_IDENTITY
    reason:
```

## 5. Real-repository no-write proof

```yaml
real_repository_no_write_proof:
  run_id:
  repositories:
    - repository:
      before_ref:
      after_ref:
      changed: true | false | unknown
      proof_method:
      observed_at:
      limitation:
  complete_for_claimed_scope: true | false
  exception:
    approved: false
    decision_ref: null
    reason: null
    alternative_evidence: []
    confidence: null
    independently_verified_by_Owner: false
    not_future_precedent: true
```

If `complete_for_claimed_scope` is false and no valid exception exists, the run cannot claim a high-confidence no-write result.

## 6. Backup/restore result

```yaml
backup_restore_result:
  scenario_id: S11
  source_repository:
  source_commit_or_version:
  source_tree_or_integrity:
  snapshots:
    - location:
      content_scope:
      source_identity:
      integrity_identity:
      independent_editing_allowed: false
  simulated_failures: []
  restore_source:
  restored_repository_or_location:
  restored_integrity_identity:
  required_records_recovered: []
  mismatches: []
  disposition:
```

## 7. Incident ledger

```yaml
incident:
  incident_id:
  phase:
  scenario_id:
  class: authority | propagation | parent_copy | concurrency | invention | material | provenance | backup | protocol | executor
  description:
  first_detected_at:
  affected_artifacts: []
  contamination_scope:
  immediate_action:
  preserved_attempt_refs: []
  retry_allowed:
  adjudication_required:
```

## 8. Complete result bundle

```yaml
validation_result_bundle:
  result_id:
  run_manifest_ref:
  V0_result_ref:
  V1_executed:
  scenario_attempt_refs: []
  task_contract_refs: []
  mechanical_evidence_refs: []
  no_write_proof_ref:
  backup_restore_ref:
  incident_refs: []

  scenario_summary:
    passed: []
    passed_with_observation: []
    candidate_or_semantic_failures: []
    executor_failures: []
    blocked: []
    invalid: []

  critical_blockers: []
  candidate_defects: []
  validation_protocol_defects: []
  executor_defects: []
  disputed_items: []
  noncritical_observations: []

  proposed_amendments:
    - proposal:
      evidence_refs: []
      adoption_status: not_adopted_pending_Pro_and_Owner_review

  reviewer_events: []
  Pro_frontier_disposition:
    status: pending
    value: null
  Owner_architecture_decision:
    status: pending
    value: null

  target_adoption_authorized: false
  execution_source_modified: false
  real_target_modified: false
```

## 9. Human-readable final report

The visible final response must include:

1. exact run/package/repository identity;
2. V0 result and whether V1 was authorized;
3. every scenario disposition with critical evidence;
4. all critical failures, incidents and preserved retries;
5. no-write proof status;
6. backup/restore result;
7. candidate defects versus executor/protocol defects;
8. limitations and unresolved disputes;
9. proposed amendments clearly marked non-adopted;
10. the next required Pro/frontier and Owner decisions.

A downloadable file or repository artifact may be supplied as a supporting copy, but must not replace the complete decision-relevant final response.
