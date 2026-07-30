# Frontier Clarification Validation — V1 Small-Smoke Execution Taskbook v0.1

> Future read-only execution taskbook for 40 public/synthetic cells. This file does not authorize or execute V1 and does not authorize V2/V3.

```yaml
V1_taskbook_id: FRONTIER-CLARIFICATION-VALIDATION-V1-SMOKE-001
package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
created_by_task: MNEMOSYNE-181
version: 0.1.0
status: ready_pending_valid_V0_and_explicit_V1_authorization
scenarios: 8
conditions: 5
primary_cells: 40
blanket_repeats: 0
real_user_data: prohibited
repository_write_during_run: prohibited
```

## 1. Purpose

V1 tests whether Q0–Q4 can be executed, isolated, observed and reviewed across a small balanced set of synthetic authority, privacy, architecture, fixed-decision, external-fact, false-choice, restatement and research-trigger cases.

V1 is designed to discover blocking failures, condition collapse, interpretation burden and rework. It does not establish production effectiveness or universal model adequacy.

## 2. Required package inputs

At execution time pin one commit containing all package files:

```text
notes/frontier-clarification-validation-package/README.md
notes/frontier-clarification-validation-package/00-scope-manifest-v0.1.md
notes/frontier-clarification-validation-package/01-protocol-spec-v0.1.md
notes/frontier-clarification-validation-package/02-condition-contracts-q0-q4-v0.1.md
notes/frontier-clarification-validation-package/03-public-synthetic-scenario-set-v0.1.md
notes/frontier-clarification-validation-package/04-hidden-author-keys-v0.1.md
notes/frontier-clarification-validation-package/05-answer-ledger-and-escalation-tests-v0.1.md
notes/frontier-clarification-validation-package/06-rubric-and-decision-rules-v0.1.md
notes/frontier-clarification-validation-package/07-reviewer-and-adjudication-taskbook-v0.1.md
notes/frontier-clarification-validation-package/08-v0-sentinel-context-isolation-taskbook-v0.1.md
notes/frontier-clarification-validation-package/09-v1-small-smoke-execution-taskbook-v0.1.md
notes/frontier-clarification-validation-package/10-run-manifest-template-v0.1.md
notes/frontier-clarification-validation-package/11-result-return-and-maintainer-review-package-v0.1.md
notes/frontier-clarification-validation-package/12-execution-surface-and-user-decision-package-v0.1.md
notes/frontier-clarification-validation-package/13-package-integrity-checklist-v0.1.md
```

Do not execute from a moving branch or a partial package.

## 3. Mandatory preflight

```yaml
V1_preflight:
  explicit_V1_authorization:
  authorization_scope_exactly_V1_smoke: yes | no
  package_commit_sha:
  package_version: 0.1.0
  valid_V0_run_id:
  valid_V0_status: PASS_required
  V0_surface_and_access_boundary_unchanged: yes | no
  public_hidden_separation_verified: yes | no
  package_integrity_check_passed: yes | no
  final_condition_execution_map_complete: yes | no
  worker_context_fresh_per_cell: yes | no
  reviewer_context_separate: yes | no
  owner_script_release_mechanism:
  worker_repository_web_connected_app_access: none_required
  artifact_storage_location:
  no_write_proof_method:
  public_or_synthetic_material_only: yes_required
  real_user_or_target_material_present: no_required
  quota_or_cost_limit:
  stop_and_targeted_repeat_limit:
```

Any failed required field returns `PREFLIGHT_FAILURE` with `primary_cells_started: 0`. Do not improvise a weaker run.

## 4. Human-selected execution condition map

The future user must fill this before V1:

```yaml
condition_execution_map:
  Q0:
    product_surface:
    operator_visible_model_or_mode:
    reasoning_setting_if_visible:
    intended_role: baseline_worker
  Q1:
    product_surface:
    operator_visible_model_or_mode:
    reasoning_setting_if_visible:
    intended_role: structured_package_worker
  Q2:
    product_surface:
    operator_visible_model_or_mode:
    reasoning_setting_if_visible:
    intended_role: next_tier_interviewer_candidate
  Q3:
    product_surface:
    operator_visible_model_or_mode:
    reasoning_setting_if_visible:
    intended_role: next_tier_gated_interviewer_candidate
  Q4:
    product_surface:
    operator_visible_model_or_mode:
    reasoning_setting_if_visible:
    intended_role: direct_frontier_comparator
```

Record visible text verbatim. Consumer-chat backend remains `unknown_or_not_attestable`. If the visible condition changes mid-run, stop or create a new run ID; do not silently pool cells.

Architecture and model condition may be confounded if Q4 uses a stronger visible condition. The final review must state that limitation rather than calling V1 a controlled provider/model comparison.

## 5. Roles and information boundary

```yaml
V1_roles:
  controller:
    responsibilities:
      - pin_package_and_run_identity
      - render_exact_worker_packets
      - create_fresh_contexts
      - release_owner_scripts_turn_by_turn
      - capture_exact_outputs
      - maintain_manifest
    may_generate_worker_content_after_hidden_key_access: false

  owner_script_releaser:
    responsibilities:
      - release_only_current_scripted_turn
      - never_improvise_new_policy_or_answer

  worker:
    receives:
      - common_envelope
      - one_condition_addendum
      - one_rendered_public_scenario_packet
      - current_owner_script_turn_when_eligible
    must_not_receive:
      - hidden_key_file
      - another_condition_contract
      - another_cell_output
      - reviewer_material
      - unreleased_owner_script

  reviewer:
    starts_after_relevant_outputs_are_frozen: true
    separate_context_from_worker: required
```

## 6. V1 scenario set

```yaml
V1_scenarios:
  - FCV-AUTH-001
  - FCV-PRIV-001
  - FCV-ARCH-001
  - FCV-FIXED-001
  - FCV-FACT-001
  - FCV-FALSE-001
  - FCV-REST-001
  - FCV-RESEARCH-001
```

The six reserve scenarios are not run in V1.

## 7. Conditions

```yaml
V1_conditions:
  - Q0
  - Q1
  - Q2
  - Q3
  - Q4
```

## 8. Primary cell matrix and rotation

```yaml
cell_order:
  - [V1-FCV-AUTH-001-Q0, V1-FCV-AUTH-001-Q1, V1-FCV-AUTH-001-Q2, V1-FCV-AUTH-001-Q3, V1-FCV-AUTH-001-Q4]
  - [V1-FCV-PRIV-001-Q1, V1-FCV-PRIV-001-Q2, V1-FCV-PRIV-001-Q3, V1-FCV-PRIV-001-Q4, V1-FCV-PRIV-001-Q0]
  - [V1-FCV-ARCH-001-Q2, V1-FCV-ARCH-001-Q3, V1-FCV-ARCH-001-Q4, V1-FCV-ARCH-001-Q0, V1-FCV-ARCH-001-Q1]
  - [V1-FCV-FIXED-001-Q3, V1-FCV-FIXED-001-Q4, V1-FCV-FIXED-001-Q0, V1-FCV-FIXED-001-Q1, V1-FCV-FIXED-001-Q2]
  - [V1-FCV-FACT-001-Q4, V1-FCV-FACT-001-Q0, V1-FCV-FACT-001-Q1, V1-FCV-FACT-001-Q2, V1-FCV-FACT-001-Q3]
  - [V1-FCV-FALSE-001-Q0, V1-FCV-FALSE-001-Q1, V1-FCV-FALSE-001-Q2, V1-FCV-FALSE-001-Q3, V1-FCV-FALSE-001-Q4]
  - [V1-FCV-REST-001-Q1, V1-FCV-REST-001-Q2, V1-FCV-REST-001-Q3, V1-FCV-REST-001-Q4, V1-FCV-REST-001-Q0]
  - [V1-FCV-RESEARCH-001-Q2, V1-FCV-RESEARCH-001-Q3, V1-FCV-RESEARCH-001-Q4, V1-FCV-RESEARCH-001-Q0, V1-FCV-RESEARCH-001-Q1]
```

The rotation is an operational order, not randomization. Fresh context per cell remains mandatory.

## 9. Public packet rendering algorithm

For each cell:

1. read one public scenario record;
2. read the common envelope;
3. extract only the assigned condition addendum;
4. serialize scenario fields in the exact order defined by the condition contract;
5. exclude authoring metadata not named by the contract;
6. exclude the hidden key and all future owner turns;
7. record exact packet bytes/chars and hash/ref;
8. create a fresh worker context with no tools or repository access;
9. deliver only the rendered packet.

If rendering is ambiguous or a required field is absent, mark `PACKET_CONSTRUCTION_FAILURE` and stop before the worker starts.

## 10. Cell execution algorithm

```yaml
cell_algorithm:
  step_1: create_fresh_worker_context
  step_2: provide_exact_rendered_packet
  step_3: capture_worker_turn_1_verbatim
  step_4: release_scripted_owner_answer_turn_1_only
  step_5: capture_worker_turn_2_verbatim
  step_6:
    Q0_Q1: do_not_release_turn_2_script_and_require_final_record
    Q2_Q3_Q4: if_one_eligible_followup_is_asked_release_turn_2_script_else_do_not_release
  step_7: capture_worker_final_verbatim
  step_8: close_worker_context
  step_9: write_local_cell_record_and_hash
  step_10: do_not_score_inside_worker_context
```

The owner-script releaser returns the authored turn exactly. It does not adapt the answer to make the worker look better or worse.

## 11. Exact cell record

```yaml
cell_record:
  run_id:
  cell_id:
  attempt: 1
  scenario_id:
  condition_id:
  package_commit_sha:
  common_envelope_ref:
  condition_contract_ref:
  public_scenario_ref:
  hidden_key_ref_controller_reviewer_only:
  rendered_packet_ref:
  rendered_packet_hash:
  worker_surface:
  operator_visible_model_or_mode:
  exact_backend:
    status: unknown_or_not_attestable
  worker_context_receipt:
  started_at:
  completed_at:
  worker_turn_1_verbatim: |
  owner_turn_1_released_verbatim: |
  worker_turn_2_verbatim: |
  owner_turn_2_released_verbatim: |
  worker_final_verbatim: |
  interaction_record:
  answer_ledger:
  tool_calls: []
  warnings: []
  truncation: false
  execution_error:
  status: complete | invalid_protocol | malformed | not_run | stopped
```

Blank fields must use explicit `not_applicable`, `not_released` or `missing`; never invent text.

## 12. Output-format mechanical checks

Before review verify:

- unique `cell_id` and attempt lineage;
- exact scenario/condition IDs;
- package commit and version;
- exact rendered packet identity;
- only eligible owner turns released;
- required worker turns preserved;
- final interaction record and ledger present;
- no hidden key text in worker input;
- no other condition or cell output in context;
- no repository/web/app tool call;
- incomplete or stopped cells explicitly marked;
- output not silently edited.

Mechanical format success is not substantive safety success.

## 13. Interaction caps

```yaml
interaction_caps:
  Q0:
    followups: 0
  Q1:
    followups: 0
  Q2:
    followups: 1_maximum
  Q3:
    followups: 1_maximum_unless_gate_stops_first
  Q4:
    followups: 1_maximum
```

A worker that wants more turns records unresolved items and `interaction_cap_reached: true`.

## 14. Review workflow

After cell artifacts are frozen:

1. run mechanical identity and forbidden-material checks;
2. perform reviewer Pass A for protocol validity, condition safety and content;
3. perform reviewer Pass B for condition adherence/contamination;
4. compare Q0–Q4 within each scenario;
5. aggregate by condition without one composite score;
6. adjudicate material disagreements;
7. create the complete return bundle;
8. leave human disposition pending.

Use `07-reviewer-and-adjudication-taskbook-v0.1.md` and `11-result-return-and-maintainer-review-package-v0.1.md`.

## 15. Failure handling

```yaml
failure_handling:
  preflight_or_package_identity_failure:
    - start_zero_cells
    - return_PREFLIGHT_FAILURE

  context_isolation_failure:
    - stop_new_cells
    - preserve_completed_artifacts
    - return_CONTEXT_ISOLATION_FAILURE_or_PARTIAL_STOP

  hidden_key_or_cross_condition_leakage:
    - stop_new_cells
    - invalidate_affected_evidence
    - preserve_incident

  packet_scenario_or_condition_mismatch:
    - mark_cell_invalid_protocol
    - inspect_controller
    - allow_one_targeted_repeat_only_if_authorized

  output_missing_malformed_or_truncated:
    - preserve_failed_attempt
    - allow_one_targeted_repeat_only_if_within_limit

  severe_condition_safety_failure:
    - preserve_as_substantive_result
    - trigger_immediate_review
    - apply_user_approved_early_stop_rule_if_any

  visible_model_or_mode_change:
    - record_notice_verbatim
    - stop_or_create_new_run_ID
    - do_not_pool_silently

  quota_or_cost_boundary_reached:
    - stop_before_new_cell
    - mark_remaining_not_run
```

## 16. Targeted repeat rule

A repeat is permitted only for:

- malformed/truncated output;
- packet or capture mismatch;
- product interruption;
- output identity failure that is repaired before repeat.

```yaml
targeted_repeat:
  repeat_cell_id:
  repeat_of:
  exact_reason:
  original_attempt_preserved: true
  changed_input_or_surface: false_required_or_new_run
  attempt_number: 2
  selection_of_better_output: prohibited
```

No blanket repetition or best-of selection.

## 17. Local artifact layout

Unless later repository ingestion is separately authorized:

```text
frontier-clarification-v1-run-<run-id>/
├── manifest.yaml
├── package-receipt.md
├── packets/
│   └── <cell-id>-input.md
├── cells/
│   └── <cell-id>-attempt-<n>.md
├── reviews/
│   ├── reviewer-a/
│   ├── reviewer-b/
│   └── adjudication/
├── summaries/
│   ├── protocol-validity.md
│   ├── condition-safety.md
│   ├── scenario-comparisons.md
│   ├── condition-comparisons.md
│   └── proposed-disposition.md
├── incidents-and-stop-log.md
└── <RUN_ID>-complete-response.md
```

Do not place private data in local artifacts. Repository ingestion is separately gated.

## 18. No-write and material receipt

```yaml
execution_receipt:
  repository_ref_before:
  repository_ref_after:
  mechanical_no_write_evidence:
  repository_write_calls: 0
  target_write_calls: 0
  current_user_data_used: false
  private_or_target_material_used: false
  real_participants_used: false
  credentials_or_secrets_present: false
```

If default mechanical no-write evidence is unavailable, the run is incomplete unless the user approves a run-scoped exception. No exception is granted here.

## 19. Completion receipt

```yaml
V1_completion:
  status: COMPLETE | PARTIAL_STOP | PREFLIGHT_FAILURE | CONTEXT_ISOLATION_FAILURE | IDENTITY_FAILURE | INCOMPLETE
  run_id:
  package_commit_sha:
  V0_run_id:
  primary_cells_expected: 40
  primary_cells_started:
  primary_cells_completed:
  protocol_invalid_cells:
  not_run_cells:
  targeted_repeats:
  critical_stop_triggered: yes | no
  stop_reason:
  review_completed: yes | no | partial
  proposed_disposition:
  human_disposition: pending
  repository_writes_performed: false
  real_or_private_data_used: false
  V2_authorized: false
```

## 20. Boundaries

V1 execution, even when later authorized, does not:

- prove real-user burden or satisfaction;
- validate a model/provider generally;
- attest exact backend identity;
- authorize V2 or V3;
- update `current/human-approved-spec.md`;
- propagate to Meta-Agent or another target project;
- authorize repository ingestion or auto-writeback;
- permit additional same-topic research automatically.
