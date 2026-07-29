# Frontier Planning and Clarification Handoff — Interim Architecture and Validation Decision

```yaml
decision_id: FRONTIER-PLANNING-CLARIFICATION-HANDOFF-INTERIM-001
created_by_task: MNEMOSYNE-179
decision_class: user_approved_behavior_guard_interpretation_and_non_execution_source_candidate_architecture
research_phase: complete
additional_research: not_recommended
validation_phase: designed_not_selected_not_executed
execution_source_modified: false
target_project_propagation_authorized: false
```

## 1. Immediate durable behavior retained

The following are explicit user workflow requirements and do not require empirical validation before being used in Mnemosyne conversations:

- current user operations are presented first;
- meaningful follow-on work is presented in a visible closing `## 下一步` section;
- every meaningful next stage states whether frontier/Pro-class capability is required, recommended or unnecessary;
- Deep Research and parallel frontier-review value are assessed separately;
- material questions include background, meaning, consequences and option interpretation;
- literal user wording remains evidence but is not assumed to be a complete final specification;
- the user can correct, reject, defer or supersede interpretations;
- owner decisions are not replaced by research, and researchable facts are not pushed back to the owner without verification.

## 2. Research-trigger policy

```yaml
research_gate:
  generate_ready_to_run_task_only_if:
    - uncertainty_is_external_and_researchable
    - plausible_answers_change_downstream_action
    - upstream_scope_is_sufficiently_frozen
    - current_sources_or_bounded_verification_are_insufficient
    - expected_decision_value_justifies_cost_and_delay
  required_task_fields:
    - exact_question
    - decision_it_can_change
    - upstream_dependencies
    - evidence_and_source_requirements
    - stop_condition
    - return_destination
  human_controls:
    - provider_or_surface_selection
    - quota_or_cost_trigger
    - actual_research_execution
  prohibited:
    - research_to_avoid_owner_preference
    - automatic_quota_spend
    - fabricated_report_before_run
    - repeated_parallel_research_without_distinct_value
```

## 3. Clarification architecture routing

No single architecture is approved as a universal default.

```yaml
routing:
  direct_frontier_interaction:
    use_for:
      - high_impact_low_clarity
      - owner_authority_privacy_architecture_trust_boundary
      - material_problem_restatement
      - unresolved_cross_evidence_conflict

  structured_nonconversational_package:
    use_for:
      - bounded_decision_set
      - direct_owner_review_is_practical
      - interviewer_is_unavailable_unvalidated_or_unnecessary
      - auditability_outweighs_live_adaptation

  next_tier_interactive_clarification:
    status: candidate_validation_gated
    use_only_when:
      - low_or_moderate_impact
      - problem_and_question_meaning_are_frozen
      - package_is_self_contained
      - user_can_reject_options_and_correct_interpretations
      - visible_reconstructable_ledger_exists
      - semantic_escalation_rules_and_frontier_reentry_exist

  gated_mixed_escalation:
    status: preferred_validation_candidate_for_mixed_routes
    not_yet: validated_default

  research_first:
    use_only_when:
      - external_fact_gap_is_decision_relevant
      - research_scope_is_frozen
      - reversible_provisional_action_is_inadequate
```

## 4. Question design minimum

Every material owner question should include the minimum context needed to answer without reconstructing a long conversation:

```yaml
minimum_question_contract:
  - question_ID
  - plain_language_question
  - concise_origin_and_current_state
  - decisions_already_fixed_if_relevant
  - planner_interpretation_marked_as_candidate
  - why_the_answer_changes_downstream_work
  - option_meanings_and_tradeoffs_when_options_are_used
  - other_none_or_reject_premise_path
  - free_form_answer_allowed
  - deferral_effect
  - dependencies
  - semantic_escalation_conditions
```

Recommendations are allowed when clearly separated from facts and values, explain their assumptions, remain rejectable, and do not act as a default for high-impact owner decisions.

## 5. Ledger and interviewer requirements

```yaml
answer_ledger:
  must_be:
    - visible_or_available_to_user
    - reconstructable
    - separate_verbatim_or_safe_reference_from_interpretation
    - correction_aware
    - dependency_aware
  persistent_external_store:
    requirement: conditional_on_surface_duration_sensitivity_and_authority

next_tier_interviewer:
  may:
    - explain_frozen_context
    - ask_scoped_followups
    - record_answers_corrections_deferrals_and_unknowns
    - update_visible_ledger
  must_not:
    - redesign_the_problem
    - invent_context_or_owner_decisions
    - silently_select_or_default_an_option
    - convert_tentative_language_to_approval
    - resolve_high_impact_conflicts
    - update_execution_source_or_target_truth
```

## 6. Delivery correction

```yaml
Deep_Research_delivery:
  canonical_substantive_output: one_complete_report
  inline_report: canonical_product_representation
  Markdown_Word_PDF_download: export_of_same_report
  arbitrary_second_named_complete_response_file:
    required: false
    allowed_only_if_surface_explicitly_supports_and_confirms_creation: true
  operator_export_and_rename:
    allowed: true
    must_be_labeled_as_export_of_same_report: true
```

## 7. Validation requirement

The remaining uncertainty is no longer primarily literature coverage. It is whether the candidate routing and delegation actually reduce user burden and frontier turns without harming intent fidelity, answer interpretation, escalation and downstream decisions.

```yaml
next_evidence_gate:
  design: notes/validation-designs/frontier-planning-clarification-handoff-read-only-validation-v0.1.md
  state: designed_not_selected_not_executed
  real_user_data: prohibited_without_separate_decision
  repository_write_by_executor: prohibited
  target_project_write: prohibited
  model_or_surface_selection: future_user_decision
```

## 8. Stop and rollback

- Any missed authority/privacy/architecture/trust-boundary escalation blocks broader delegation.
- Any invented background or conversion of tentative language to approval blocks the affected interviewer condition.
- If next-tier interaction does not improve burden or frontier-turn use over the structured package without fidelity loss, retain structured packages and direct frontier interaction.
- If the packet repeatedly misframes the problem, return to direct frontier clarification and revise the planner contract.
- No experimental result automatically propagates to Meta-Agent or another target project.
