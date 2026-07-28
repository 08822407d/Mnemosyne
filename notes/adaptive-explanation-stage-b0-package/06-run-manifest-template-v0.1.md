# Adaptive Explanation Stage B0 — Run Manifest Template v0.1

> Template for a future authorized smoke execution. Do not fill with invented values. The manifest records visible operator conditions and artifact identity; it does not attest the exact backend.

```yaml
manifest_template_id: ADAPTIVE-EXPLANATION-STAGE-B0-RUN-MANIFEST-TEMPLATE-001
created_by_task: MNEMOSYNE-176
version: 0.1.0
status: template_not_a_run
```

## 1. Run identity

```yaml
run:
  run_id:
  task_id: ADAPTIVE-EXPLANATION-STAGE-B0-SMOKE-EXECUTION-001
  phase: smoke
  status: planned | running | complete | partial_stop | failed_preflight
  started_at:
  ended_at:
  operator:
  authorization_ref:
  package_commit_sha:
  package_version: 0.1.0
  fixture_set_version: 0.1.0
  condition_contract_version: 0.1.0
  rubric_version: 0.1.0
```

## 2. Product and visible model condition

```yaml
execution_condition:
  product_surface_visible_text:
  operator_visible_model_or_mode_text:
  visible_reasoning_or_intelligence_text:
  account_or_workspace_type_if_relevant:
  usage_or_quota_counter_before:
  usage_or_quota_counter_after:
  fallback_or_limit_notice_verbatim:
  tool_access:
    web: false
    files: package_inputs_only
    connected_apps: false
    repository_write: false
  exact_served_backend:
    status: unknown_or_not_attestable
    provider_metadata_ref:
```

Rules:

- preserve visible text verbatim where available;
- do not normalize a UI label into a provider model identity;
- do not use speed, style or self-report as backend evidence;
- if the visible condition changes during the run, stop or create a new run ID rather than pooling cells silently.

## 3. Isolation receipt

```yaml
isolation:
  implementation:
  tutor_context_fresh_per_cell: yes | no
  tutor_hidden_key_access: no_required
  tutor_other_condition_access: no_required
  reviewer_separate_context: yes | no
  controller_seen_hidden_keys:
  controller_generated_tutor_content_after_hidden_key_access: no_required
  isolation_test_description:
  result: pass | fail | unclear
```

A result other than `pass` blocks execution.

## 4. Package receipt

```yaml
package_receipt:
  README:
    path: notes/adaptive-explanation-stage-b0-package/README.md
    blob_or_content_hash:
  protocol:
    path: notes/adaptive-explanation-stage-b0-package/01-protocol-spec-v0.1.md
    blob_or_content_hash:
  conditions:
    path: notes/adaptive-explanation-stage-b0-package/02-condition-contracts-v0.1.md
    blob_or_content_hash:
  fixtures:
    path: notes/adaptive-explanation-stage-b0-package/03-synthetic-fixture-set-v0.1.md
    blob_or_content_hash:
  rubric:
    path: notes/adaptive-explanation-stage-b0-package/04-rubric-and-decision-rules-v0.1.md
    blob_or_content_hash:
  taskbook:
    path: notes/adaptive-explanation-stage-b0-package/05-execution-taskbook-v0.1.md
    blob_or_content_hash:
  return_package:
    path: notes/adaptive-explanation-stage-b0-package/07-return-and-review-package-v0.1.md
    blob_or_content_hash:
```

## 5. Fixture review receipt

```yaml
fixture_review:
  reviewer_count:
  reviewers:
    - reviewer_id:
      role:
      domain_coverage:
  mathematics_reference_correctness: pass | fail | partial
  public_hidden_separation: pass | fail
  turn_2_coherence_across_conditions: pass | fail | partial
  case_anchor_observability: pass | fail | partial
  revisions_before_run: []
  final_fixture_version:
```

## 6. Cell inventory

Use one row per primary or repeated cell.

```yaml
cells:
  - cell_id:
    fixture_id:
    condition_id:
    run_order:
    attempt: 1
    status: complete | invalid | not_run | repeated
    started_at:
    completed_at:
    output_ref:
    output_bytes_or_chars:
    truncation: false
    tool_calls: []
    warnings: []
    invalidation_reason:
    repeat_of:
```

Expected primary cell count: `32`.

## 7. Reviewer inventory

```yaml
reviews:
  - review_id:
    cell_id:
    reviewer_id:
    pass_type: content_blinded | condition_adherence | adjudication
    review_ref:
    critical_invariant_failures: []
    material_disagreement: yes | no
```

## 8. Failure and incident log

```yaml
incidents:
  - incident_id:
    type:
      - preflight_failure
      - context_isolation_failure
      - hidden_key_leakage
      - condition_contamination
      - mathematics_error
      - answer_leakage
      - output_identity_failure
      - product_interruption
      - quota_or_fallback_notice
      - truncation
      - other
    affected_cells: []
    observed_evidence:
    immediate_action:
    resolved: yes | no
    resolution_ref:
```

## 9. Material and privacy receipt

```yaml
material_receipt:
  public_mathematics_content_only: yes | no
  synthetic_learner_traces_only: yes | no
  current_user_data_used: no_required
  private_chat_or_voice_transcripts_used: no_required
  customer_or_confidential_material_used: no_required
  credentials_or_secrets_present: no_required
  real_participants: no_required
  persistent_learner_state_created: no_required
```

Any failed `no_required` field stops the run and blocks repository storage.

## 10. Artifact inventory

```yaml
artifacts:
  root:
  manifest_file:
  cell_output_count:
  reviewer_output_count:
  summary_files: []
  archive_if_any:
    filename:
    bytes:
    sha256:
    exact_reconstruction_verified: yes | no | not_applicable
  repository_ingestion:
    authorized: false
    performed: false
```

Do not claim an exact archive unless reconstruction and hash identity are verified.

## 11. Completion and stop receipt

```yaml
completion:
  status: COMPLETE | PARTIAL_STOP | PREFLIGHT_FAILURE | CONTEXT_ISOLATION_FAILURE
  cells_expected: 32
  cells_completed:
  cells_invalid:
  cells_not_run:
  targeted_repeats:
  critical_invariant_failures_observed:
  stop_condition_triggered:
  stop_reason:
  smoke_disposition_proposed:
    - PROCEED_TO_B0_CORE_DESIGN_AND_EXECUTION_DECISION
    - REVISE_AND_REPEAT_SMOKE
    - ACCEPT_PARTIAL_PROTOCOL_EVIDENCE_AND_DEFER
    - STOP_B0_ROUTE
  proposed_by:
  final_maintainer_disposition: pending
```

## 12. Limitations

```yaml
limitations:
  - synthetic_fixtures_do_not_measure_real_learning
  - hidden_author_keys_are_construction_intent_not_real_mental_state
  - small_smoke_counts_do_not_support_inferential_effect_claims
  - exact_backend_unknown_unless_attested
  - reviewer_judgment_and_fixture_validity_may_limit_results
```
