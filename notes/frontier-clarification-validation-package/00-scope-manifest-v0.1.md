# Frontier Clarification Validation — Scope Manifest v0.1

> Frozen package-scope manifest. This is not a run manifest and contains no validation result.

```yaml
scope_manifest_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-SCOPE-001
package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
created_by_task: MNEMOSYNE-181
version: 0.1.0
status: frozen_package_scope_not_executed
execution_source: current/human-approved-spec.md
execution_source_modified: false
```

## 1. Authority and source map

```yaml
authority_map:
  execution_source:
    path: current/human-approved-spec.md
    role: sole_Mnemosyne_execution_source

  user_authorization:
    source: current_conversation_instruction_after_PR_232_merge
    authorized:
      - receive_handoff_against_merged_master
      - load_Mnemosyne_guidance_as_separate_operation
      - preserve_PREPARE_READ_ONLY_VALIDATION_PACKAGE_task
      - prepare_complete_validation_package
      - create_one_branch_and_one_PR
    excluded:
      - execute_V0
      - execute_V1
      - execute_V2
      - execute_V3
      - use_real_user_data
      - modify_execution_source
      - modify_Meta_Agent
      - import_non_FABLE_health_review
      - merge_PR

  transfer_artifact:
    path: handoff/mnemosyne-frontier-clarification-validation-handoff-package.md
    role: non_execution_source_task_transfer

  source_validation_design:
    path: notes/validation-designs/frontier-planning-clarification-handoff-read-only-validation-v0.1.md
    role: candidate_design_to_operationalize_without_execution

  source_adjudication:
    - notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/03-cross-report-consensus-conflict-and-adjudication.md
    - notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/04-interim-architecture-and-validation-decision.md
    - current/frontier-planning-clarification-handoff-adjudication-guard.md
```

No package file may override the execution source or turn an unselected validation condition into an approved default.

## 2. Source checkpoint

```yaml
source_checkpoint:
  PR_231_merge_commit: 96eb9757b6554d397267501dd29e4682c155d830
  PR_232_merge_commit: 22c1b63b2238aece5d8f9cd3810dcc1a832a9b83
  package_branch_base: 22c1b63b2238aece5d8f9cd3810dcc1a832a9b83
  prior_research:
    Pro: complete_accepted_with_corrections
    Fable: complete_accepted_with_corrections_no_rerun
    additional_same_topic_research: not_needed
  prior_validation:
    design_exists: true
    complete_package_prepared_before_MNEMOSYNE_181: false
    selected_for_execution: false
    cells_started: 0
    executed: false
```

## 3. Validation questions preserved

The package operationalizes, without changing, these questions:

1. Does context-rich presentation improve understanding of why a question is being asked compared with a bare question or option code?
2. Does a bounded next-tier interviewer preserve the frontier planner's intended meaning, fixed decisions and authority boundary?
3. Does live interviewing reduce owner burden or create another interpretation surface?
4. Can the workflow preserve literal answers separately from interpretations, corrections, deferrals and supersession?
5. Can it reliably detect and escalate owner, execution-source, privacy, architecture, trust-boundary and material product-goal conflicts?
6. Does gated mixed escalation reduce frontier turns after rework without hiding critical failures?
7. Does the research trigger distinguish decision-relevant external evidence gaps from owner preferences, premature research and non-decision-changing questions?

## 4. Included package scope

```yaml
included:
  package_index_and_scope:
    - README.md
    - 00-scope-manifest-v0.1.md
  protocol:
    - 01-protocol-spec-v0.1.md
  conditions:
    - 02-condition-contracts-q0-q4-v0.1.md
  scenarios:
    - 03-public-synthetic-scenario-set-v0.1.md
    - 04-hidden-author-keys-v0.1.md
  interaction_controls:
    - 05-answer-ledger-and-escalation-tests-v0.1.md
  review:
    - 06-rubric-and-decision-rules-v0.1.md
    - 07-reviewer-and-adjudication-taskbook-v0.1.md
  future_execution_taskbooks:
    - 08-v0-sentinel-context-isolation-taskbook-v0.1.md
    - 09-v1-small-smoke-execution-taskbook-v0.1.md
  manifests_and_return:
    - 10-run-manifest-template-v0.1.md
    - 11-result-return-and-maintainer-review-package-v0.1.md
  human_gate:
    - 12-execution-surface-and-user-decision-package-v0.1.md
  mechanical_review:
    - 13-package-integrity-checklist-v0.1.md
```

## 5. Explicitly excluded scope

```yaml
excluded:
  execution:
    - any_V0_sentinel_run
    - any_V1_smoke_cell
    - any_V2_core_cell
    - any_V3_target_portability_cell
    - any_generated_validation_result
  data:
    - current_user_conversation_content_as_fixture
    - voice_transcripts
    - private_files
    - customer_or_confidential_material
    - target_project_material
    - credentials_or_secrets
  authority:
    - execution_source_change
    - target_project_truth_change
    - automatic_route_adoption
    - automatic_quota_spend
    - automatic_model_or_surface_selection
    - automatic_research_execution
  routes:
    - target-projects/meta-agent
    - Meta_Agent_owner_acceptance
    - non_FABLE_comprehensive_health_review
    - handoff/handoff-current.md_as_action_plan
  platform_claims:
    - exact_backend_attestation_from_UI_label
    - backend_inference_from_latency_style_or_self_report
  automation:
    - GitHub_Actions
    - MCP
    - RAG
    - auto_writeback
    - multi_Agent_automatic_execution
```

## 6. Material and repository-visibility boundary

The repository is public at package preparation time. Every authored scenario and answer script is synthetic and contains no user-derived transcript, personal data, credential, secret, customer data or target-project content.

```yaml
material_receipt:
  public_repository_safe: yes
  public_or_synthetic_only: yes
  current_user_data_used: no
  private_chat_excerpt_used: no
  voice_transcript_used: no
  target_project_material_used: no
  credentials_or_secrets_present: no
  real_participant: no
```

The hidden-author-key file is hidden only from future worker contexts. It is not a secret-storage mechanism and is not confidential merely because it is separated from public worker packets. Future workers must have no repository search or broad file access by default.

## 7. Frozen condition set

```yaml
conditions:
  Q0:
    label: bare_question
    role: failure_prone_baseline
  Q1:
    label: structured_nonconversational_owner_package
    role: direct_auditable_package
  Q2:
    label: frozen_packet_plus_next_tier_interviewer
    role: validation_gated_candidate
  Q3:
    label: gated_mixed_escalation
    role: preferred_validation_candidate_not_validated_default
  Q4:
    label: direct_frontier_clarification
    role: high_fidelity_comparator_not_gold_truth
```

## 8. Frozen scenario set

```yaml
scenario_set:
  total: 14
  V1_smoke: 8
  V2_reserve: 6
  V3_target_patterns: 0
  scenario_source: authored_synthetic
  hidden_keys_separate_from_worker_visible_inputs: required
```

The reserve scenarios are frozen to make future coverage visible. They are not an authorization to prepare or execute V2 automatically.

## 9. Package-level required invariants

```yaml
package_invariants:
  - all_files_identify_themselves_as_non_execution_source
  - no_file_claims_validation_execution
  - public_and_hidden_scenario_material_are_separate_files
  - Q0_to_Q4_contracts_are_versioned_and_frozen
  - V0_and_V1_have_separate_authorization_gates
  - no_V2_or_V3_execution_taskbook_is_present
  - worker_inputs_exclude_hidden_keys_other_conditions_and_other_outputs
  - reviewer_and_worker_contexts_are_separate
  - literal_answer_and_interpretation_are_separate
  - correction_deferral_rejection_and_supersession_are_represented
  - semantic_escalation_is_not_keyword_only
  - exact_input_output_identity_is_required
  - protocol_validity_failure_is_separate_from_condition_safety_failure
  - no_result_changes_execution_source_or_target_truth_automatically
```

## 10. Human decisions intentionally unresolved

```yaml
unresolved_owner_decisions:
  before_V0:
    - choose_or_defer_execution_surface
    - approve_surface_specific_isolation_evidence
    - select_visible_model_or_mode_condition_for_each_role
    - decide_quota_or_cost_boundary
    - decide_reviewer_arrangement_and_known_independence_limits
    - authorize_V0_only
  before_V1:
    - accept_valid_V0_receipt
    - approve_exact_V1_execution_condition_map
    - approve_40_cell_smoke_burden
    - approve_stop_and_targeted_repeat_limits
    - authorize_V1_only
  after_V1:
    - adjudicate_results
    - decide_revise_defer_stop_or_later_V2_design
    - decide_any_Mnemosyne_behavior_adoption
```

No unresolved item is assigned a silent default by this package.

## 11. Version and change rule

- Package version `0.1.0` is immutable for a future pinned run.
- Any semantic change to a scenario, hidden key, condition, rubric or execution rule requires a new package version and a new run manifest.
- Results from different versions must not be silently pooled.
- Editorial repairs that alter executable text or scoring anchors are semantic changes.

## 12. Preparation completion definition

Package preparation is complete only when:

- all manifest-listed files exist at one branch/commit;
- all IDs and references resolve;
- public and hidden scenario files contain matching unique scenario IDs;
- the V1 matrix resolves to exactly 40 unique primary cell IDs;
- V0/V1 statuses remain unexecuted;
- no forbidden path is modified;
- the package integrity checklist has been applied as a preparation review;
- one canonical PR exposes the entire package for human review.
