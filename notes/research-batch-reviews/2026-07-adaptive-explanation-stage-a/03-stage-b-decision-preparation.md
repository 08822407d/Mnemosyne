# Adaptive Explanation — Stage B Decision Preparation

> Non-execution-source decision preparation derived from the accepted-with-corrections Stage A report. This file does not approve, generate or execute an experiment; recruit participants; assess the current user; configure GPT Live; or authorize persistent/cross-Agent learner memory.

```yaml
decision_package_id: ADAPTIVE-EXPLANATION-STAGE-B-DECISION-PREPARATION-001
created_by_task: MNEMOSYNE-175
source_research: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001
source_review: notes/research-batch-reviews/2026-07-adaptive-explanation-stage-a/01-maintainer-reliability-review.md
source_calibration: notes/research-batch-reviews/2026-07-adaptive-explanation-stage-a/02-claim-and-evidence-calibration-ledger.md
status: candidate_ready_for_user_disposition
Stage_B_selected: false
Stage_B_generated: false
Stage_B_executed: false
```

## 1. Decision now supported by Stage A

Stage A supports preparing a bounded text-dialogue test of the candidate framework. It does not support deploying the framework or treating the local diagnostic taxonomy as validated.

```yaml
Stage_A_supports:
  - test_generic_simple_vs_fixed_representation_vs_adaptive_vs_adaptive_recovery_conditions
  - use_independent_performance_transfer_retention_burden_and_overreliance_outcomes
  - keep_local_hypotheses_contestable_and_allow_unknown
  - audit_Agent_explanation_error
  - begin_with_public_or_synthetic_protocol_testing

Stage_A_does_not_support:
  - production_adaptive_tutor
  - stable_global_learner_level
  - persistent_learner_profile
  - cross_Agent_sharing
  - real_participant_study_without_separate_governance
  - one_universal_prerequisite_graph_or_explanation_sequence
```

## 2. Recommended staged interpretation of Stage B

The report uses “Stage B” for a controlled text-dialogue experiment. The maintainer recommends splitting the decision into two gates so that protocol defects can be found before collecting real user data.

### Stage B0 — Synthetic/public pre-pilot

```yaml
Stage_B0:
  purpose:
    - test_condition_adherence
    - test_local_hypothesis_and_unknown_handling
    - test_Agent_self_audit_and_recovery
    - test_item_and_rubric_clarity
    - estimate_interaction_length_and_burden_proxies
    - expose_answer_leakage_and_condition_contamination
  materials:
    - public_mathematics_content
    - expert_reviewed_synthetic_learner_trajectories
    - adversarial_and_ambiguous_dialogue_traces
    - no_private_user_history
  may_establish:
    - protocol_feasibility
    - condition_separation
    - safety_and_stop_rule_behavior
    - measurement_and_scoring_feasibility
    - candidate_revision_needs
  cannot_establish:
    - real_learning_effect
    - delayed_retention_in_real_learners
    - actual_user_burden_or_dropout
    - fairness_across_real_groups
    - persistent_learner_model_validity
```

### Stage B1 — Real-participant pilot

```yaml
Stage_B1:
  prerequisite:
    - Stage_B0_reviewed_or_explicitly_waived_by_user
    - exact_protocol_and_items
    - participant_population_and_recruitment_decision
    - consent_privacy_retention_and_deletion_policy
    - model_product_surface_and_usage_budget
    - independent_scoring_plan
    - statistical_precision_or_power_plan
    - adverse_event_stop_and_rollback_plan
  status: not_selected
  real_user_data_authorized: false
```

## 3. Candidate experimental conditions

The four-condition structure is retained as a candidate:

```yaml
C0_generic_simple_instruction:
  intent: reproduce_the_common_generic_instruction
  distinguishing_feature: no_explicit_local_diagnosis_or_recovery_contract

C1_fixed_representation_policy:
  intent: test_whether_a_consistent_intuitive_or_worked_example_first_policy_is_enough
  distinguishing_feature: structured_but_not_locally_adaptive

C2_adaptive_local_diagnosis:
  intent: test_bounded_competing_hypotheses_low_burden_probes_and_contextual_action_selection
  distinguishing_feature: local_evidence_and_unknown_rule

C3_adaptive_plus_recovery:
  intent: test_C2_plus_Agent_explanation_audit_meaningful_repair_self_correction_and_stop_rules
  distinguishing_feature: explicit_failure_recovery
```

The exact system prompts, prohibited assistance, turn budget, evidence records and condition-adherence rubric remain to be written after user selection.

## 4. Candidate mathematics scope

A small B0 can use three microdomains, each chosen for visible prerequisite structure and separable explanation failures:

```yaml
candidate_microdomains:
  calculus:
    preferred_candidate: derivative_as_local_linear_approximation_or_limit_derivative_relation
    candidate_failure_cases:
      - notation_barrier
      - limit_concept_gap
      - relation_between_secant_and_tangent
      - abstraction_jump

  linear_algebra:
    preferred_candidate: span_and_linear_independence_or_solution_structure_of_linear_systems
    candidate_failure_cases:
      - procedural_vs_relational_knowledge
      - geometric_symbolic_mapping
      - alternative_valid_solution_route
      - misleading_analogy

  probability_statistics:
    preferred_candidate: conditional_probability_and_Bayes_or_sampling_distribution_interpretation
    candidate_failure_cases:
      - base_rate_or_conditioning_misconception
      - notation_barrier
      - sample_vs_population_confusion
      - verbal_symbolic_mapping
```

The scope may be narrowed to one or two domains if expert item validation or review burden is too high.

## 5. Candidate synthetic trajectory types

Stage B0 should not simulate a single stereotyped learner. It should include contrasting traces that produce observational ambiguity.

```yaml
synthetic_trajectory_types:
  - true_prerequisite_gap
  - temporary_retrieval_failure_resolved_by_minimal_cue
  - component_knowledge_without_relation
  - notation_only_barrier
  - coherent_misconception
  - task_wording_misunderstanding
  - tutor_misunderstands_the_question
  - tutor_gives_a_factually_incorrect_or_misleading_explanation
  - high_load_or_long_turn_failure
  - alternative_valid_strategy_misclassified_as_error
  - insufficient_evidence_with_multiple_equally_plausible_hypotheses
  - adversarial_fluent_but_not_transferable_response
```

Each trace requires an authoring rationale, expected acceptable tutor actions, prohibited overclaims and an `unknown` option.

## 6. Candidate outcome and process measures

### B0 protocol measures

```yaml
B0_measures:
  task_and_condition_adherence:
  unsupported_learner_label_rate:
  correct_use_of_unknown:
  diagnostic_false_positive_and_false_negative_by_trace:
  Agent_error_detection_and_correction:
  answer_leakage_or_over_assistance:
  explanation_action_changed_when_evidence_changed:
  recovery_changed_a_meaningful_dimension:
  source_or_mathematical_correctness:
  turn_count_and_token_or_time_proxy:
  independent_reviewer_disagreement:
```

### Future B1 learning measures

```yaml
B1_candidate_measures:
  immediate_independent_comprehension:
  near_transfer:
  unfamiliar_transfer:
  delayed_retention:
  independent_performance_without_tutor:
  confidence_accuracy_calibration:
  error_reduction:
  burden_and_cognitive_load:
  help_seeking_and_overreliance:
  dropout_or_refusal:
  subgroup_and_accessibility_differences:
```

Satisfaction and conversational fluency remain secondary.

## 7. Candidate B0 workflow

```text
freeze public/synthetic content and prerequisite maps
  -> author and independently review ambiguous learner traces
  -> freeze C0-C3 prompts and tool permissions
  -> run each condition against the same pinned trace set
  -> perform blind rubric review where practical
  -> classify protocol, safety, diagnostic and recovery failures
  -> revise or stop before any real-participant proposal
```

Stage B0 should be read-only with respect to GitHub and target projects. Any artifact storage after execution requires a separate task-local action context.

## 8. Stop and rollback candidates

```yaml
Stage_B0_stop_conditions:
  - conditions_cannot_be_distinguished_in_practice
  - C2_or_C3_regularly_invents_stable_learner_traits
  - tutor_fails_to_detect_known_explanation_errors
  - diagnostic_probes_leak_answers_or_destroy_measurement
  - unknown_state_is_not_respected
  - mathematics_or_rubrics_cannot_be_validated
  - review_burden_exceeds_the_value_of_the_added_policy
  - sensitive_or_private_material_becomes_required

rollback:
  - keep_Stage_A_as_research_evidence_only
  - do_not_generate_or_run_real_participant_Stage_B1
  - simplify_or_reject_the_candidate_policy
```

## 9. User disposition options

Select exactly one in a later explicit decision:

```yaml
user_disposition_options:
  SELECT_STAGE_B0_SYNTHETIC_PREPILOT_DESIGN:
    meaning: authorize_one_fresh_task_to_design_but_not_execute_a_public_synthetic_B0_protocol
    recommended: true

  PREPARE_NARROWER_STAGE_B0_DECISION_PACKAGE:
    meaning: first_narrow_domains_conditions_or_outcomes_before_protocol_design

  ACCEPT_STAGE_A_EVIDENCE_AND_DEFER_STAGE_B:
    meaning: preserve_the_report_and_review_without_experiment_design

  REQUEST_STAGE_A_SOURCE_OR_CLAIM_REPAIR_FIRST:
    meaning: repair_named_nonblocking_source_or_calibration_items_before_any_B0_design

  REJECT_STAGE_B_ROUTE:
    meaning: do_not_use_Stage_A_to_prepare_an_experiment
```

## 10. Maintainer recommendation

```yaml
recommendation:
  value: SELECT_STAGE_B0_SYNTHETIC_PREPILOT_DESIGN
  rationale:
    - Stage_A_supports_testing_but_not_deployment
    - synthetic_public_traces_reduce_privacy_and_participant_risk
    - protocol_and_diagnostic_failures_can_be_found_before_real_data
    - B0_can_test_C0_to_C3_separation_and_Agent_self_correction
  confidence: moderate
  not_authorized_by_this_file:
    - protocol_generation
    - experiment_execution
    - real_participant_recruitment
    - current_user_assessment
    - persistent_learner_memory
```

## 11. Boundaries

- This is decision preparation only.
- Stage B0 and B1 remain unselected and unexecuted.
- No experiment prompt, participant material or repository write manifest is approved.
- No persistent learner-state schema is adopted.
- GPT Live and cross-Agent sharing remain later, separate routes.
- Any next task requires explicit user selection and fresh task-local authorization.
