# Multi-Model Adjudication and Runtime-Provenance Research Status

> Non-execution-source live wayfinding. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
status_id: MULTI-MODEL-ADJUDICATION-PROVENANCE-STATUS-006
last_status_task: MNEMOSYNE-150
cycle: raw/research-reports/cycles/2026Q3-multi-model-adjudication-provenance
latest_reliable_progress_checkpoint:
  record: current/pr198-pro-switch-model-quality-restart-checkpoint.md
  canonical_PR: 199
  trusted_through_PR: 198
  trusted_merge_commit: e895e586fcda6783af567e3513b2c5f03ebd2d1c
  record_status: merged
  record_merge_commit: 96244617606f2a7afe3c1f0451438720df9f3307
  activation_status: activated_and_recovery_completed
  activation_record_task: MNEMOSYNE-150
  purpose: restart_boundary_for_next_Pro_selection_trial
  backend_identity_proof_required_for_activation: false
activation_event:
  trigger_source: explicit_user_instruction
  trigger_conditions_met:
    post_switch_model_quality_problem_declared: true
    restart_or_reassessment_from_PR198_requested: true
  affected_post_checkpoint_work:
    - labeled_Pro_PR198_review_response
  affected_repository_writes:
    - none_identified
  recovery_disposition:
    - discard_untrusted_reasoning_output
    - preserve_Git_history
    - preserve_PR198_and_PR199_records
    - preserve_PR200_v0_2_implementation
    - continue_from_PR198_trust_boundary_for_future_assessment
  backend_identity_proof_obtained: false
previous_checkpoint:
  record: current/multi-model-adjudication-provenance-reliable-progress-checkpoint.md
  effective_after_merge_commit: 94de7427da56659f472cbc11eb1bf310d5b6116a
  status: retained_as_historical_earlier_restart_boundary
canonical_DR07_pair:
  primary_research_candidate: independent_labeled_Pro
  control: independent_labeled_Thinking_RESEARCH_INCOMPLETE_REPOSITORY_ACCESS
  project_internal_pair_used: false
heterogeneous_follow_up:
  study_id: FABLE5-GOV-001
  storage_PR: 197
  storage_status: merged
  role: heterogeneous_corroboration_and_recovery_design_enhancement
recommendation_adoption:
  task: MNEMOSYNE-147
  canonical_PR: 198
  v0_2_review_and_repair:
    implementation_task: MNEMOSYNE-149
    canonical_PR: 200
    status: merged
    review_context:
      provider_relation: same_provider
      heterogeneous_provider_review: false
      mechanical_and_multi_agent_cross_checks: true
    implementation_status: merged
    original_record_preserved: true
    historical_v0_1_records_rewritten: false
    checkpoint_activation_effect: none
  active_guard: current/run-context-and-pr-provenance-guard.md
  active_guard_record_version: v0_2
  guidance_loader_updated: true
  maturity: v0_2_bounded_review_completed_and_user_authorized
checkpoint_activation_context:
  task: MNEMOSYNE-150
  activation_basis: explicit_user_instruction_after_post_switch_model_quality_incident
  product_surface: standard_ChatGPT_conversation
  prior_checkpoint_activation_status: dormant
  current_activation_status: recorded_after_user_trigger
  backend_model_identity: UNKNOWN_OR_NOT_ATTESTABLE
  heterogeneous_review_performed: false
  execution_source_modified: false
GF_STEP_5_substantive_adjudication: not_started
next_gate:
  - preserve_PR200_v0_2_guard_as_current_behavior_instrument
  - create_separately_bounded_future_tasks_for_GF_STEP_5_or_other_Mnemosyne_work
  - use_fresh_review_context_for_future_substantive_adjudication
  - preserve_Git_history_and_mechanical_evidence_during_any_future_recovery
  - require_fresh_task_local_authorization_for_each_future_repository_write_or_execution_source_change
```

## Current interpretation

PR #198 remains the user-designated trusted substantive baseline for the Pro-selection trial. The checkpoint was activated because the user explicitly declared a post-switch model-quality problem and requested return to this boundary. Activation does not prove backend model identity and does not accuse any provider or routing system.

The affected untrusted reasoning output was discarded as a decision input. No repository write from that affected response was identified. PR #200 remains the accepted bounded v0.2 guard implementation and was not invalidated by the checkpoint activation.

Future work should preserve this history and use fresh bounded tasks for new substantive adjudication. DR07, FABLE5-GOV-001, and Fable GF-STEP-1 through GF-STEP-5 remain stored advisory inputs and are not automatically rerun.