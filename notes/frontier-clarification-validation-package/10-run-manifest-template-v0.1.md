# Frontier Clarification Validation — Run Manifest Template v0.1

> Template for a future separately authorized V0 or V1 run. Do not fill fields with invented values. This template is not a run and contains no result.

```yaml
manifest_template_id: FRONTIER-CLARIFICATION-VALIDATION-RUN-MANIFEST-001
package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
created_by_task: MNEMOSYNE-181
version: 0.1.0
status: template_not_a_run
```

## 1. Run identity

```yaml
run:
  run_id:
  task_id:
  phase: V0_MECHANICAL_AND_SENTINEL | V1_SMALL_SMOKE
  status: planned | running | complete | partial_stop | failed_preflight | context_isolation_failure | identity_failure | incomplete
  started_at:
  ended_at:
  operator:
  authorization_ref:
  package_commit_sha:
  package_version: 0.1.0
  scenario_set_version: 0.1.0
  condition_contract_version: 0.1.0
  rubric_version: 0.1.0
  V0_prerequisite_run_id:
```

## 2. Scope receipt

```yaml
scope_receipt:
  authorized_phase:
  authorized_primary_cells:
  authorized_targeted_repeats:
  V2_authorized: false
  V3_authorized: false
  repository_write_authorized: false
  target_write_authorized: false
  real_user_data_authorized: false
  additional_research_authorized: false
  Meta_Agent_work_authorized: false
  non_FABLE_health_review_authorized: false
```

Any value inconsistent with the user authorization blocks execution.

## 3. Run-context provenance

```yaml
run_context:
  record_version: v0.2
  action_actor:
  actor_kind: human | model | agent | mechanical_process | mixed
  action_source:
  switch_history:
    status: confirmed_none | recorded | unknown
    evidence: []
  product_surface:
    value:
    evidence: []
  operator_selection:
    verbatim:
    evidence: []
  backend:
    status: unknown_or_not_attestable
    reason: consumer_UI_selection_latency_style_and_self_report_do_not_attest_exact_backend
  user_authorization:
    status: authorized | not_authorized | unknown
    actor:
    decision_ref:
    authorized_actions: []
    excluded_actions: []
    evidence: []
    expires_with_run: true
    not_future_precedent: true
  limitations: []
  omissions: []
```

Add provider normalization or exact-request served identifier only when authoritative semantics and evidence exist. Keep evidence classes separate.

## 4. Condition execution map

For V1, record each condition independently:

```yaml
condition_execution_map:
  Q0:
    product_surface_visible_text:
    operator_visible_model_or_mode_text:
    visible_reasoning_or_intelligence_text:
    tool_access:
      web: false
      repository: false
      broad_files: false
      connected_apps: false
      write: false
    backend_status: unknown_or_not_attestable
  Q1:
    product_surface_visible_text:
    operator_visible_model_or_mode_text:
    visible_reasoning_or_intelligence_text:
    tool_access:
      web: false
      repository: false
      broad_files: false
      connected_apps: false
      write: false
    backend_status: unknown_or_not_attestable
  Q2:
    product_surface_visible_text:
    operator_visible_model_or_mode_text:
    visible_reasoning_or_intelligence_text:
    tool_access:
      web: false
      repository: false
      broad_files: false
      connected_apps: false
      write: false
    backend_status: unknown_or_not_attestable
  Q3:
    product_surface_visible_text:
    operator_visible_model_or_mode_text:
    visible_reasoning_or_intelligence_text:
    tool_access:
      web: false
      repository: false
      broad_files: false
      connected_apps: false
      write: false
    backend_status: unknown_or_not_attestable
  Q4:
    product_surface_visible_text:
    operator_visible_model_or_mode_text:
    visible_reasoning_or_intelligence_text:
    tool_access:
      web: false
      repository: false
      broad_files: false
      connected_apps: false
      write: false
    backend_status: unknown_or_not_attestable
```

For V0, use the same map for the five sentinel workers. Preserve visible text verbatim. Record any fallback/limit notice and stop or create a new run ID before pooling changed conditions.

## 5. Package receipt

```yaml
package_receipt:
  root: notes/frontier-clarification-validation-package/
  files:
    - path: README.md
      blob_or_content_hash:
    - path: 00-scope-manifest-v0.1.md
      blob_or_content_hash:
    - path: 01-protocol-spec-v0.1.md
      blob_or_content_hash:
    - path: 02-condition-contracts-q0-q4-v0.1.md
      blob_or_content_hash:
    - path: 03-public-synthetic-scenario-set-v0.1.md
      blob_or_content_hash:
    - path: 04-hidden-author-keys-v0.1.md
      blob_or_content_hash:
    - path: 05-answer-ledger-and-escalation-tests-v0.1.md
      blob_or_content_hash:
    - path: 06-rubric-and-decision-rules-v0.1.md
      blob_or_content_hash:
    - path: 07-reviewer-and-adjudication-taskbook-v0.1.md
      blob_or_content_hash:
    - path: 08-v0-sentinel-context-isolation-taskbook-v0.1.md
      blob_or_content_hash:
    - path: 09-v1-small-smoke-execution-taskbook-v0.1.md
      blob_or_content_hash:
    - path: 10-run-manifest-template-v0.1.md
      blob_or_content_hash:
    - path: 11-result-return-and-maintainer-review-package-v0.1.md
      blob_or_content_hash:
    - path: 12-execution-surface-and-user-decision-package-v0.1.md
      blob_or_content_hash:
    - path: 13-package-integrity-checklist-v0.1.md
      blob_or_content_hash:
  all_required_files_present: yes | no
  versions_match: yes | no
  integrity_check_ref:
```

## 6. Isolation receipt

```yaml
isolation:
  implementation:
  context_graph_ref:
  fresh_worker_context_per_cell: yes | no
  worker_hidden_key_access: no_required
  worker_other_condition_access: no_required
  worker_other_output_access: no_required
  worker_future_owner_turn_access: no_required
  worker_repository_or_broad_file_access: no_required
  reviewer_separate_context: yes | no
  controller_seen_hidden_keys:
  controller_generated_worker_content_after_hidden_key_access: no_required
  isolation_test_description:
  V0_run_id:
  result: pass | fail | unclear
```

A V1 result other than `pass` blocks cell execution.

## 7. Public/hidden scenario receipt

```yaml
scenario_receipt:
  public_scenario_file:
  hidden_key_file:
  public_IDs: []
  hidden_IDs: []
  ID_sets_equal: yes | no
  V1_IDs_exactly_eight: yes | no
  reserve_IDs_exactly_six: yes | no
  worker_packets_contain_hidden_material: no_required
  scripted_owner_turn_release_mechanism:
```

## 8. V0 sentinel inventory

Use for V0 only:

```yaml
V0_sentinel_inventory:
  sentinel_workers_expected: 5
  sentinel_workers:
    - condition_id:
      packet_id:
      packet_hash:
      worker_context_receipt:
      output_ref:
      observed_public_sentinel:
      observed_forbidden_sentinels: []
      status: complete | invalid | not_run
  reviewer_context_receipt:
  forbidden_sentinel_events: []
  substantive_cells_started: 0
```

## 9. V1 cell inventory

Use one row per primary or repeated cell:

```yaml
cells:
  - cell_id:
    scenario_id:
    condition_id:
    run_order:
    attempt: 1
    repeat_of:
    status: complete | invalid_protocol | malformed | stopped | not_run | repeated
    worker_context_receipt:
    rendered_packet_ref:
    rendered_packet_hash:
    owner_turns_released:
    output_ref:
    output_bytes_or_chars:
    started_at:
    completed_at:
    truncation: false
    tool_calls: []
    warnings: []
    invalidation_reason:
```

Expected primary count for V1: `40`.

## 10. Review inventory

```yaml
reviews:
  - review_id:
    cell_id_or_scope:
    reviewer_id:
    actor_kind: model | human | mechanical_process
    pass_type: protocol_validity | content_safety | condition_adherence | scenario_comparison | condition_summary | adjudication
    context_relation_to_worker:
    model_relation_to_worker:
    provider_relation_to_worker:
    criteria_fixed_before_exposure:
    review_ref:
    protocol_validity_failures: []
    condition_safety_failures: []
    material_disagreement: yes | no
    limitations: []
```

## 11. Incident log

```yaml
incidents:
  - incident_id:
    type:
      - preflight_failure
      - context_isolation_failure
      - hidden_key_contamination
      - cross_condition_contamination
      - reviewer_material_leakage
      - real_or_private_material
      - packet_mismatch
      - output_identity_failure
      - condition_safety_failure
      - product_interruption
      - fallback_or_quota_notice
      - truncation
      - no_write_proof_failure
      - other
    affected_cells: []
    observed_evidence:
    immediate_action:
    resolved: yes | no
    resolution_ref:
    protocol_validity_effect:
    condition_viability_effect:
```

## 12. Material and privacy receipt

```yaml
material_receipt:
  public_or_synthetic_only: yes | no
  current_user_data_used: no_required
  private_chat_or_voice_transcript_used: no_required
  target_project_material_used: no_required
  customer_or_confidential_material_used: no_required
  credentials_or_secrets_present: no_required
  real_participants_used: no_required
  persistent_user_state_created: no_required
```

Any failed `no_required` field stops the run and blocks repository storage.

## 13. No-write receipt

```yaml
no_write_receipt:
  repository_ref_before:
  repository_ref_after:
  mechanical_diff_or_ref_comparison:
  repository_write_calls_observed: 0_required
  target_write_calls_observed: 0_required
  worker_write_capability: disabled | unavailable | unknown
  alternative_evidence_if_default_unavailable:
  run_scoped_exception:
    approved: false
    decision_ref:
    exact_scope:
    alternative_evidence:
    not_future_precedent: true
  confidence:
```

A missing default proof requires `INCOMPLETE` or a separately approved run-scoped exception.

## 14. Artifact inventory

```yaml
artifacts:
  root:
  manifest_file:
  package_receipt_file:
  packet_count:
  cell_output_count:
  reviewer_output_count:
  summary_files: []
  complete_response_file:
    filename:
    created: yes | no
    role: auxiliary_transfer_and_archival_copy
  archive_if_any:
    filename:
    bytes:
    sha256:
    exact_reconstruction_verified: yes | no | not_applicable
  repository_ingestion:
    authorized: false
    performed: false
```

Do not claim a file, archive or hash unless verified.

## 15. Aggregate result fields

```yaml
aggregate:
  protocol_validity:
  protocol_invalid_cells:
  condition_safety_failures_by_condition: {}
  condition_adherence_by_condition: {}
  planted_escalations_by_condition: {}
  missed_escalations_by_condition: {}
  false_escalations_by_condition: {}
  ledger_and_correction_summary:
  research_trigger_summary:
  context_comprehension_summary:
  intent_fidelity_summary:
  unsupported_addition_summary:
  owner_operation_burden_proxies:
  frontier_turn_and_rework_proxies:
  reviewer_disagreements:
  findings_supported: []
  findings_not_supported: []
```

## 16. Completion and stop receipt

```yaml
completion:
  status: COMPLETE | PARTIAL_STOP | PREFLIGHT_FAILURE | CONTEXT_ISOLATION_FAILURE | IDENTITY_FAILURE | INVALID_RUN | INCOMPLETE
  cells_expected:
  cells_started:
  cells_completed:
  cells_invalid:
  cells_not_run:
  targeted_repeats:
  stop_condition_triggered:
  stop_reason:
  proposed_disposition:
  proposed_by:
  human_disposition: pending
  V2_authorized: false
  execution_source_modified: false
  target_project_modified: false
  Meta_Agent_modified: false
  non_FABLE_health_review_modified: false
```

## 17. Limitations

```yaml
limitations:
  - synthetic_scenarios_do_not_measure_real_user_outcomes
  - small_counts_do_not_support_population_effect_claims
  - hidden_keys_are_authored_intent_not_real_inner_state
  - architecture_and_visible_model_condition_may_be_confounded
  - exact_backend_unknown_unless_exact_request_metadata_is_attested
  - reviewer_judgment_and_package_validity_limit_results
  - V0_pass_does_not_prove_all_future_surface_behavior
```
