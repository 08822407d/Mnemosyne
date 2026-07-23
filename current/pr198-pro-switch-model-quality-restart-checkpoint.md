# PR #198 Reliable-Progress and Pro-Switch Model-Quality Restart Checkpoint

> Non-execution-source operational checkpoint. It records the user-designated trustworthy work boundary and its completed first activation/recovery cycle. It is not backend-model attestation and does not replace `current/human-approved-spec.md`.

```yaml
checkpoint_id: MNEMOSYNE-PR198-RELIABLE-PROGRESS-RESTART-001
created_by_task: MNEMOSYNE-148
record_type: user_confirmed_model_quality_restart_checkpoint
trusted_through_pull_request: 198
trusted_merge_commit: e895e586fcda6783af567e3513b2c5f03ebd2d1c
trusted_default_branch_state: master@e895e586fcda6783af567e3513b2c5f03ebd2d1c
supersedes_for_future_restart_selection:
  - MULTI-MODEL-ADJUDICATION-PROVENANCE-RELIABLE-PROGRESS-001
previous_checkpoints_retained_as_history: true
checkpoint_effective_when: PR_199_is_human_merged
canonical_PR_number: 199
checkpoint_current_status: activated_and_recovery_completed
latest_activation:
  activation_record: current/pr198-pro-switch-model-quality-activation-and-recovery.md
  activation_record_id: MNEMOSYNE-PR198-MODEL-QUALITY-ACTIVATION-RECOVERY-001
  recorded_by_task: MNEMOSYNE-150
  affected_repository_writes: none
  recovery_completed_by_PR: 200
  recovery_merge_commit: 898b20e16f9b4694bb45110a0be036761b511740
user_designated_trusted_scope:
  - all_repository_history_and_merged_content_through_PR_198
  - FABLE5_GOV_001_stage_storage_through_PR_197
  - focused_run_context_and_PR_provenance_guard_adopted_by_PR_198
  - user_decisions_and_exact_artifact_identities_recorded_through_PR_198
  - no_GF_STEP_5_substantive_adjudication_has_started
not_claimed:
  - actual_backend_model_identity_of_any_consumer_chat_run
  - that_Pro_was_or_is_operating_correctly
  - automatic_acceptance_of_any_research_or_Fable_finding
```

## Purpose

The checkpoint was created before a trial in which the user switched the current standard ChatGPT conversation from the reported `Extra High` option to `Pro` and attempted substantive Mnemosyne review work.

Merged PR #198 was the last user-confirmed trustworthy work point for that trial. It replaced PR #196 as the latest default restart selection without deleting or rewriting the earlier checkpoint record.

The trial later met both activation conditions. The incident and completed recovery are recorded in `current/pr198-pro-switch-model-quality-activation-and-recovery.md`.

## Activation trigger

This checkpoint activates only when the user explicitly communicates both:

1. work performed after switching to `Pro` appears to have the wrong intelligence/model-quality level, is materially unreliable, or otherwise should not be trusted; and
2. the affected work should be restarted, reassessed, or rolled back logically to PR #198 / this checkpoint.

Generic disagreement, one disappointing answer, unusual latency, prose style, verbosity, or a model self-report does not activate the checkpoint by itself.

The user's explicit activation is sufficient operational authority. Backend identity does not need to be proven before the recovery procedure is used.

## Default recovery semantics

After activation:

1. preserve all Git and PR history;
2. retain `master@e895e586fcda6783af567e3513b2c5f03ebd2d1c` and all work through PR #198 as the trusted baseline;
3. reassess or redo substantive reasoning performed after the checkpoint, including architecture judgment, research interpretation, prioritization, maintainer adjudication, repair-route selection, task/prompt design that depended on affected judgment, and execution-source proposals;
4. preserve exact-byte storage, hashes, immutable external originals, and other mechanical evidence after inspection;
5. preserve explicit user decisions, but ask for reconfirmation when a decision materially depended on an affected summary or recommendation;
6. inspect later repository changes individually rather than assuming every post-checkpoint commit is invalid;
7. when a later merged change is defective, correct it through a new reviewed superseding or revert PR rather than rewriting history or force-moving `master`;
8. do not rerun DR07, FABLE5-GOV-001, or Fable GF-STEP-1 through GF-STEP-5 by default unless the user explicitly expands the recovery scope;
9. require fresh task-local authorization for every repository write, repair, execution-source change, target-project action, or research expansion.

## Post-checkpoint artifact defaults

```yaml
recovery_defaults:
  exact_byte_storage_and_hashes: preserve_and_recheck
  raw_external_research_originals: preserve_and_spot_check
  summaries_and_interpretations: recheck_against_originals_and_supersede_if_needed
  architecture_judgments: redo_when_in_affected_chain
  accept_reject_prioritize_decisions: redo_analysis_and_return_to_user
  explicit_user_decisions: preserve_unless_dependency_requires_reconfirmation
  execution_source_proposals: redo_and_reauthorize
  already_merged_changes: inspect_then_supersede_or_revert_through_new_PR_if_needed
  target_project_work: stop_and_return_to_target_owner_or_user_decision
```

## Checkpoint-creation run context

```yaml
run_context:
  action_actor: ChatGPT_GitHub_app
  provider_product_surface: standard_ChatGPT_conversation
  surface_evidence: operator_reported
  operator_visible_or_reported_selection: Extra High
  selection_evidence: operator_reported
  provider_documented_model_mapping: GPT-5.6 Sol
  backend_model_identity: UNKNOWN_OR_NOT_ATTESTABLE
  model_self_report_used_as_identity_evidence: false
  model_or_surface_switches_during_task: []
  review_independence_class: user_designated_trust_boundary_recorded_by_current_conversation
  heterogeneous_review_performed: false
  heterogeneous_review_exception: explicit_user_task_local_decision_to_create_immediate_checkpoint_before_Pro_trial
  later_stronger_model_review: permitted_but_not_required_for_checkpoint_activation
```

## Completed activation and recovery

```yaml
activation_history:
  - activation_id: MNEMOSYNE-PR198-MODEL-QUALITY-ACTIVATION-RECOVERY-001
    status: activated_and_recovery_completed
    activation_evidence: explicit_user_quality_problem_report_and_restart_instruction
    affected_artifacts:
      - failed_labeled_Pro_PR198_review_response
    affected_repository_writes: none
    recovery_review_task: WORK-ULTRA-PR198-REVIEW-001
    recovery_implementation_task: MNEMOSYNE-149
    recovery_PR: 200
    recovery_merge_commit: 898b20e16f9b4694bb45110a0be036761b511740
    detailed_record: current/pr198-pro-switch-model-quality-activation-and-recovery.md
```

The activation is a completed historical event. It does not remain continuously active and does not automatically govern a future incident. A future event needs a separately recorded user instruction, incident scope, and recovery decision.

## Next permitted work

After completed recovery, the next substantive Mnemosyne task requires separate user selection and authorization. GF-STEP-5 substantive adjudication remains not started.

## Boundary

This record does not prove a backend model identity, accuse a provider, automatically activate for a future event, rewrite repository history, modify the execution source, adjudicate Fable GF-STEP-5, authorize repairs or target-project work, merge a pull request, or enable auto-merge.

Under `current/run-context-and-pr-provenance-guard.md`, a run record may point to this file through `recovery_refs.checkpoint_ref`. That reference is informational only: it does not constitute an incident assessment or activation record, prove provider failure or model substitution, authorize recovery or repository writes, or satisfy either checkpoint activation condition. The completed incident and activation record is `current/pr198-pro-switch-model-quality-activation-and-recovery.md`; future `incident_assessment_ref` or `activation_record_ref` values must identify separately authorized records that actually exist.