# Frontier Clarification Validation — Package Integrity Checklist v0.1

> Mechanical and bounded semantic preparation checklist. It checks package completeness and prohibited material; it does not execute V0/V1 or validate a clarification condition.

```yaml
integrity_checklist_id: FRONTIER-CLARIFICATION-VALIDATION-INTEGRITY-001
package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
created_by_task: MNEMOSYNE-181
version: 0.1.0
status: checklist_not_a_run
```

## 1. Expected file inventory

```yaml
expected_files:
  - README.md
  - 00-scope-manifest-v0.1.md
  - 01-protocol-spec-v0.1.md
  - 02-condition-contracts-q0-q4-v0.1.md
  - 03-public-synthetic-scenario-set-v0.1.md
  - 04-hidden-author-keys-v0.1.md
  - 05-answer-ledger-and-escalation-tests-v0.1.md
  - 06-rubric-and-decision-rules-v0.1.md
  - 07-reviewer-and-adjudication-taskbook-v0.1.md
  - 08-v0-sentinel-context-isolation-taskbook-v0.1.md
  - 09-v1-small-smoke-execution-taskbook-v0.1.md
  - 10-run-manifest-template-v0.1.md
  - 11-result-return-and-maintainer-review-package-v0.1.md
  - 12-execution-surface-and-user-decision-package-v0.1.md
  - 13-package-integrity-checklist-v0.1.md
expected_count: 15
```

## 2. Expected identity values

```yaml
expected_identity:
  package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
  task_id: MNEMOSYNE-181
  version: 0.1.0
  source_validation_id: FRONTIER-PLANNING-CLARIFICATION-HANDOFF-VALIDATION-001
  status_language:
    - prepared_not_selected_not_executed
    - designed_not_selected_not_executed
    - frozen_not_executed
    - ready_pending_future_authorization
```

No file may claim a V0/V1/V2/V3 result or current execution authorization.

## 3. Condition checks

```yaml
condition_checks:
  exact_condition_IDs: [Q0, Q1, Q2, Q3, Q4]
  unique_count: 5
  Q0_role: bare_question_failure_prone_baseline
  Q1_role: structured_nonconversational_owner_package
  Q2_role: packet_plus_next_tier_validation_gated_candidate
  Q3_role: gated_mixed_escalation_preferred_validation_candidate
  Q4_role: direct_frontier_comparator_not_gold_truth
  common_envelope_present: required
  interaction_caps:
    Q0: 0_followups
    Q1: 0_followups
    Q2: 1_maximum
    Q3: 1_maximum_or_gate_stop
    Q4: 1_maximum
```

Check that a worker receives only the common envelope and one addendum, not the full condition file.

## 4. Public/hidden scenario alignment

Expected IDs in both scenario files:

```yaml
expected_scenario_IDs:
  V1_smoke:
    - FCV-AUTH-001
    - FCV-PRIV-001
    - FCV-ARCH-001
    - FCV-FIXED-001
    - FCV-FACT-001
    - FCV-FALSE-001
    - FCV-REST-001
    - FCV-RESEARCH-001
  V2_reserve:
    - FCV-RESEARCH-002
    - FCV-CORR-001
    - FCV-HEDGE-001
    - FCV-TRUST-001
    - FCV-BACKGROUND-001
    - FCV-IDENTITY-001
expected_total: 14
```

For each ID verify:

- exactly one public source record;
- exactly one hidden author key;
- public phase matches inventory;
- hidden key contains scripted turn 1;
- optional turn 2 is not released unless a worker asks an eligible follow-up;
- no real-person or target-project material appears;
- public source contains known state, fixed decisions, unresolved decision, downstream consequence and answer routes;
- hidden key contains expected authority route, planted escalation set, prohibited inferences, research route and anchors.

## 5. V1 matrix checks

```yaml
V1_matrix:
  scenarios: 8
  conditions: 5
  expected_primary_cells: 40
  expected_cell_ID_pattern: V1-<SCENARIO_ID>-<Q0|Q1|Q2|Q3|Q4>
  duplicate_IDs_allowed: false
  every_smoke_scenario_has_all_conditions: required
  reserve_scenarios_present_in_V1_matrix: false_required
  blanket_repeats: 0
```

Confirm the explicit matrix contains exactly 40 unique primary IDs.

## 6. V0 checks

```yaml
V0_checks:
  substantive_scenarios: 0
  substantive_cells: 0
  sentinel_workers: 5
  public_worker_sentinels: 5_unique
  controller_only_sentinel: 1
  hidden_key_only_sentinel: 1
  reviewer_only_sentinel: 1
  worker_packet_contains_only_own_public_sentinel: required
  separate_reviewer_context: required
  inability_to_prove_isolation_status: CONTEXT_ISOLATION_FAILURE
  V1_auto_authorized_after_PASS: false_required
```

Do not run the sentinels during package preparation.

## 7. Rubric checks

```yaml
rubric_checks:
  protocol_validity_invariants: PVI01_through_PVI10
  condition_safety_invariants: CSI01_through_CSI12
  comparative_dimensions: R01_through_R18
  protocol_invalid_vs_condition_failure_distinction: required
  average_cannot_override_blocking_failure: required
  Q0_failure_can_be_valid_baseline_evidence: required
  Q4_not_gold_truth: required
  allowed_dispositions_exactly:
    - INVALID_RUN
    - RETAIN_DIRECT_FRONTIER_AND_STRUCTURED_PACKAGE_ONLY
    - ENABLE_NEXT_TIER_INTERVIEWER_FOR_NARROW_LOW_IMPACT_SCOPE
    - ADOPT_GATED_MIXED_ESCALATION_AS_CANDIDATE_DEFAULT_FOR_SPECIFIED_SCOPE
    - REVISE_PACKET_OR_ESCALATION_AND_REPEAT
    - ACCEPT_PARTIAL_EVIDENCE_AND_DEFER
    - STOP_DELEGATED_CLARIFICATION_ROUTE
```

## 8. Ledger and escalation checks

```yaml
ledger_checks:
  verbatim_or_safe_ref_separate_from_interpretation: required
  interpretation_status_values:
    - confirmed
    - provisional
    - contradicted
    - deferred
    - rejected
    - unknown
  correction_lineage: required
  supersession_lineage: required
  dependencies_and_stale_items: supported
  reject_premise: supported
  execution_source_update_authorized_default: false
  target_truth_update_authorized_default: false

escalation_categories:
  - E01_NEW_OWNER_OR_EXECUTION_SOURCE_CLAIM
  - E02_PRIVACY_OR_SENSITIVE_MATERIAL_CHANGE
  - E03_ARCHITECTURE_OR_PRODUCT_GOAL_CHANGE
  - E04_TRUST_PERMISSION_OR_WRITE_BOUNDARY_CHANGE
  - E05_IRREVERSIBLE_OR_HIGH_COST_COMMITMENT
  - E06_MATERIAL_RESTATEMENT_OF_OWNER_INTENT
  - E07_CONFLICT_WITH_FIXED_DECISION
  - E08_IDENTITY_OR_PACKET_LOSS
```

Escalation must require evidence and context; keyword-only matching is insufficient.

## 9. Authorization and phase checks

```yaml
phase_checks:
  package_preparation_authorized: true
  V0_selected: false
  V0_authorized: false
  V0_executed: false
  V1_selected: false
  V1_authorized: false
  V1_executed: false
  V2_taskbook_present: false
  V2_authorized: false
  V2_executed: false
  V3_taskbook_present: false
  V3_authorized: false
  V3_executed: false
```

Search for fabricated result language such as completed cell counts, pass rates or model rankings. Only templates, expected counts and example records are allowed.

## 10. Material and forbidden-path checks

```yaml
material_checks:
  public_or_synthetic_only: required
  current_user_transcript: prohibited
  voice_transcript: prohibited
  private_file_content: prohibited
  target_project_material: prohibited
  customer_or_confidential_data: prohibited
  credentials_or_secrets: prohibited

forbidden_modified_paths_for_MNEMOSYNE_181:
  - current/human-approved-spec.md
  - handoff/handoff-current.md
  - current/active-context.md
  - current/todo.md
  - current/open-questions.md
  - target-projects/meta-agent/
```

Also verify no file imports or claims ownership of the non-FABLE health-review route.

## 11. Repository-write and execution boundaries

Every future taskbook must state:

- repository write during run is prohibited;
- target write is prohibited;
- repository ingestion is separately gated;
- default mechanical no-write proof is required or a run-scoped exception must be explicit;
- no platform permission becomes task authorization;
- package preparation is not validation execution.

## 12. Model and provenance checks

```yaml
provenance_checks:
  consumer_backend_status: unknown_or_not_attestable
  operator_visible_selection_recorded_verbatim: supported
  latency_style_self_report_backend_inference: prohibited
  reviewer_actor_and_context_relation: required
  human_review_overclaim: prohibited
  same_family_review_limitation: required_when_applicable
  architecture_model_condition_confounding: disclosed
```

## 13. Research checks

```yaml
research_checks:
  completed_research_preserved:
    Pro: accepted_with_corrections
    Fable: accepted_with_corrections_no_rerun
  additional_same_topic_research: NOT_NEEDED
  future_positive_research_trigger_case: FCV-RESEARCH-002
  owner_preference_not_research_case: FCV-RESEARCH-001
  research_execution_automatic: false
  fabricated_report: prohibited
```

## 14. Complete-response checks

The future run and review package must require:

```yaml
complete_response_transfer_file:
  required: true
  suggested_filename: <RUN_OR_REVIEW_ID>-complete-response.md
  create_in_same_final_response: true
  role: auxiliary_transfer_and_archival_copy
```

Do not claim creation if the future surface cannot create the file.

## 15. Preparation check result template

```yaml
package_integrity_result:
  check_id:
  package_commit_sha:
  expected_files_present:
  missing_or_extra_files: []
  ID_checks: pass | fail
  public_hidden_alignment: pass | fail
  V1_matrix_count: 40_required
  V1_matrix_unique: pass | fail
  V0_sentinel_definition: pass | fail
  rubric_ranges_and_dispositions: pass | fail
  cross_references: pass | fail
  forbidden_material_scan: pass | fail
  forbidden_path_diff_scan: pass | fail
  no_execution_claim_check: pass | fail
  phase_state_check: pass | fail
  provenance_boundary_check: pass | fail
  open_defects: []
  limitations: []
  status: PASS | FAIL | INCOMPLETE
```

A `PASS` means only that the package is internally complete enough for human review. It does not authorize or validate V0/V1.

## 16. Change rule

Any repair to executable text, scenario meaning, hidden key, rubric or taskbook after a future run requires a new package version and new run ID. Preparation-time corrections before first execution may remain in `0.1.0` only while the package PR is still under review and no run has pinned the version; record the final commit used for any run.
