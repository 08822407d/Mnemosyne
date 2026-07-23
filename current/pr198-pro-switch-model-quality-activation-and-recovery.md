# PR #198 Pro-Switch Model-Quality Activation and Recovery Record

> Non-execution-source incident, activation, and recovery record. It records the user-activated operational checkpoint and the completed recovery path. It does not attest a hidden backend model, accuse a provider, or replace `current/human-approved-spec.md`.

```yaml
record_id: MNEMOSYNE-PR198-MODEL-QUALITY-ACTIVATION-RECOVERY-001
created_by_task: MNEMOSYNE-150
record_type: checkpoint_activation_incident_assessment_and_completed_recovery
checkpoint_ref: current/pr198-pro-switch-model-quality-restart-checkpoint.md
checkpoint_id: MNEMOSYNE-PR198-RELIABLE-PROGRESS-RESTART-001
trusted_baseline:
  pull_request: 198
  merge_commit: e895e586fcda6783af567e3513b2c5f03ebd2d1c
activation_status: activated
recovery_status: completed
recovery_completion:
  pull_request: 200
  merge_commit: 898b20e16f9b4694bb45110a0be036761b511740
recorded_at: 2026-07-23
execution_source_modified: false
backend_identity_attested: false
provider_failure_claimed: false
model_substitution_claimed: false
```

## 1. Activation evidence

The checkpoint required both an explicit post-switch quality problem report and an explicit request to restart from the PR #198 boundary.

The user supplied both conditions in the Mnemosyne maintenance conversation:

```yaml
activation_evidence:
  - class: direct_user_instruction
    ref: current_Mnemosyne_maintenance_conversation_2026_07_23
    observed_or_accessed_at: 2026-07-23
    claim_scope: checkpoint_activation_and_restart_from_PR_198_boundary
    detail:
      - user_reported_that_the_labeled_Pro_run_remained_materially_unreliable
      - user_reported_switching_back_to_5_6_Sol_xhigh
      - user_explicitly_requested_context_rollback_to_the_PR_199_recorded_checkpoint
```

Backend identity did not need to be proven for operational activation, and this record does not infer it.

## 2. Contamination window

```yaml
contamination_window:
  start_event:
    ref: current_Mnemosyne_maintenance_conversation_2026_07_23
    description: user_switched_the_existing_conversation_to_the_labeled_Pro_option_and_requested_review_and_improvement_of_PR_198
    exact_timestamp_available: false
  end_event:
    ref: current_Mnemosyne_maintenance_conversation_2026_07_23
    description: user_switched_back_to_5_6_Sol_xhigh_and_explicitly_activated_the_PR_198_restart_boundary
    exact_timestamp_available: false
  repository_default_branch_during_window:
    known_checkpoint_record_commit: 96244617606f2a7afe3c1f0451438720df9f3307
  limitation: conversation_event_timestamps_and_immutable_message_hashes_are_not_available_in_the_repository
```

## 3. Affected-artifact inventory

```yaml
affected_artifacts:
  - artifact_id: FAILED_LABELED_PRO_PR198_REVIEW_RESPONSE
    medium: ChatGPT_conversation_response
    repository_path: null
    immutable_hash: unavailable
    role: substantive_review_and_candidate_follow_up_route
    disposition: rejected_not_trusted_not_used_as_design_authority
    repository_write_result: none
    downstream_task_or_PR_created_from_affected_response: false

unaffected_or_retained:
  - PR_198_and_merge_commit_e895e586fcda6783af567e3513b2c5f03ebd2d1c
  - PR_199_and_merge_commit_96244617606f2a7afe3c1f0451438720df9f3307
  - exact_FABLE5_GOV_001_archives_and_hashes
  - DR07_archives_and_comparison_records
  - Fable_GF_STEP_1_through_GF_STEP_5_advisory_outputs
  - explicit_user_decisions_through_PR_198
```

No branch, pull request, commit, repository comment, or external-service mutation was created by the affected labeled-Pro review response.

## 4. Incident evidence and claim limits

```yaml
incident_assessment:
  classification: execution_quality_and_task_contract_failure
  evidence_tier: direct_user_report_plus_observable_output_contract_failure
  observed_failures:
    - required_complete_FABLE5_GOV_001_report_was_not_successfully_located_and_read
    - substantive_Mnemosyne_findings_were_issued_after_required_input_integrity_failed
    - repository_navigation_stopped_after_a_guessed_direct_file_path_returned_not_found
    - requested_repository_improvement_was_not_performed
    - the_run_did_not_return_a_formal_BLOCKED_or_INCOMPLETE_status
  does_not_establish:
    - hidden_backend_model_identity
    - model_substitution
    - provider_failure
    - routing_configuration
    - causal_relation_to_Allow_Ultra_or_any_other_account_setting
```

The incident record is sufficient to reject the output for Mnemosyne use. It is not sufficient to identify the hidden backend cause.

## 5. Recovery actions

```yaml
recovery_actions:
  - order: 1
    action: preserve_Git_and_PR_history
    result: completed
  - order: 2
    action: retain_PR_198_as_trusted_substantive_baseline
    result: completed
  - order: 3
    action: discard_the_failed_labeled_Pro_review_judgments_and_MNEMOSYNE_149_suggestion_from_that_response
    result: completed
  - order: 4
    action: independently_re_review_PR_198_against_complete_FABLE5_GOV_001_evidence_in_fresh_Work_Ultra_task_project
    result: completed
    review_task: WORK-ULTRA-PR198-REVIEW-001
  - order: 5
    action: record_user_disposition_and_implement_bounded_C01_through_C08_repairs
    result: completed
    implementation_task: MNEMOSYNE-149
  - order: 6
    action: merge_the_reviewed_v0_2_repair
    result: completed
    pull_request: 200
    merge_commit: 898b20e16f9b4694bb45110a0be036761b511740
```

## 6. Downstream dependencies and re-entry result

```yaml
downstream_dependency_review:
  failed_labeled_Pro_response_used_by_PR_200: false
  PR_200_inputs:
    - complete_FABLE5_GOV_001_task_and_report
    - commit_pinned_PR_198_implementation_files
    - fresh_Work_Ultra_review_findings
    - explicit_user_disposition_C01_through_C08
    - mechanical_repository_validation
  unresolved_dependency_on_failed_response: false

re_entry_validation:
  trusted_baseline_preserved: true
  affected_repository_writes_found: false
  fresh_independent_review_completed: true
  user_adjudication_recorded: true
  bounded_repair_merged: true
  current_guard_version: v0.2
  execution_source_unchanged: true
  recovery_complete: true
```

## 7. Actors and review relations

```yaml
recovery_actors:
  checkpoint_activator:
    actor: user
    role: operational_quality_judgment_and_restart_authority
  recovery_maintainer:
    actor: current_Mnemosyne_maintenance_conversation
    role: apply_checkpoint_semantics_and_reject_affected_judgment
  independent_reviewer:
    actor: ChatGPT_Work_review_lead_and_multi_agent_cross_checks
    task: WORK-ULTRA-PR198-REVIEW-001
    provider_relation_to_original_implementation: same
    heterogeneous_provider_review: false
  implementation_actor:
    actor: Codex_in_ChatGPT_Work
    task: MNEMOSYNE-149
  final_human_gate:
    actor: user
    role: approve_C01_through_C08_and_merge_PR_200
```

## 8. Current disposition

```yaml
current_disposition:
  checkpoint_activation: historical_completed_event
  checkpoint_recovery: completed
  trusted_substantive_baseline_for_this_incident: PR_198
  current_repository_head_after_recovery: master@898b20e16f9b4694bb45110a0be036761b511740
  failed_labeled_Pro_review: rejected
  future_Pro_authenticity_testing: not_required
  GF_STEP_5_substantive_adjudication: not_started
  next_work_requires_separate_user_authorization: true
```

The checkpoint remains available as a historical record of this incident. This completed activation does not automatically activate it for a future event; any future recovery decision requires a separately recorded user instruction and incident scope.

## 9. Boundary

This record does not rewrite history, revert `master`, prove a backend model identity, accuse OpenAI or another provider, modify the execution source, adjudicate Fable GF-STEP-5, authorize target-project work, authorize a future repository write, or merge its own pull request.