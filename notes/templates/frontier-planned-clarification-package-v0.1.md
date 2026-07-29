# Frontier-Planned Clarification Package Template v0.1

> Reusable non-execution-source template for a frontier planner to prepare context-rich human clarification that can usually be conducted by a next-tier interviewer. The template does not authorize repository writes, execution-source updates, target-project changes, research execution, model switching, or quota use.

```yaml
template_id: FRONTIER-PLANNED-CLARIFICATION-PACKAGE-TEMPLATE-001
created_by_task: MNEMOSYNE-178
version: 0.1.0
source_guard: current/user-operation-next-step-capability-and-intent-guard.md
execution_source: current/human-approved-spec.md
execution_source_modified: false
```

## 1. Intended use

Use this template when a frontier or high-reasoning planner has already reconstructed the problem and identified owner questions that:

- require human preference, authority, priority, or acceptance judgment;
- benefit from multi-step interactive clarification;
- can be handled by a next-tier model once the decision context is frozen;
- would otherwise consume scarce frontier quota merely to repeat background and capture answers.

Do not use it to ask the user to decide:

- an external fact that should be verified or researched;
- a mathematical or technical fact that should be established by evidence;
- a missing artifact's content that the Agent could retrieve from an authorized source;
- a high-impact conflict whose options and consequences have not yet been adequately analyzed.

## 2. Planner preflight

```yaml
planner_preflight:
  package_id:
  project_or_route:
  current_execution_source:
  target_execution_source_if_any:
  owner:
  safe_source_refs: []
  repository_visibility_if_relevant:
  user_wording_preserved_or_referenced: true | false
  problem_restatement_status: candidate | user_confirmed | task_local_provisional
  question_count:
  dependencies_between_questions: []
  next_tier_interaction_suitable: true | false | unknown
  suitability_reason:
  frontier_escalation_triggers: []
```

If `next_tier_interaction_suitable` is not `true`, do not hand the package to a weaker interviewer. Either keep the clarification in the frontier conversation or narrow the question set.

## 3. Package overview

```yaml
clarification_package:
  package_id:
  title:
  prepared_by:
  prepared_at:
  project_or_route:
  decision_scope:
  why_clarification_is_needed_now:
  what_work_is_waiting_on_the_answers:
  upstream_refs: []
  explicit_user_wording_or_safe_ref:
  proposed_restatement:
  restatement_confidence:
  current_known_state: []
  decisions_already_fixed: []
  matters_not_being_reopened: []
  unresolved_items: []
  question_order_and_dependencies: []
  completion_criteria:
  final_return_destination:
```

## 4. Context synopsis for the interviewer and user

Write a concise synopsis that answers:

1. What project or problem is being discussed?
2. What has already been decided?
3. What changed or remained uncertain?
4. Why are these questions being asked now rather than earlier or later?
5. What downstream design, implementation, research, or acceptance decision depends on them?
6. What is explicitly out of scope?

The synopsis must be understandable without requiring the human to remember a long prior conversation. It should cite stable paths or IDs where useful but explain what they mean in plain language.

## 5. Uncertainty routing ledger

Before writing questions, classify unresolved items:

```yaml
uncertainty_routing:
  - item_id:
    description:
    class: USER_DECISION | EXTERNAL_FACT | DEEP_RESEARCH_QUESTION | DESIGN_JUDGMENT | MISSING_ARTIFACT | MIXED
    reason:
    routed_action:
    question_for_user_required: yes | no | after_research
    research_task_ref:
    missing_artifact_ref:
```

Only `USER_DECISION` and the user-decision portion of `MIXED` items belong in the clarification question list.

## 6. Question template

Repeat for each material question:

```yaml
clarification_question:
  question_id: CLARIFY-NNN
  short_label:
  plain_language_question:

  background_and_origin:
    triggering_input_or_event:
    relevant_prior_decisions: []
    current_problem_state:

  current_understanding:
    literal_user_wording_or_safe_ref:
    planner_interpretation:
    alternative_interpretations: []
    assumptions: []
    confidence:

  why_this_question_matters:
  what_downstream_work_it_changes:
  consequence_of_wrong_interpretation:

  options:
    - option_id:
      meaning:
      practical_effect:
      advantages: []
      disadvantages_or_risks: []
      what_it_unlocks: []
      what_it_blocks_or_defers: []
      reversibility:

  recommended_or_provisional_option:
  recommendation_reason:
  recommendation_confidence:

  acceptable_free_form_answer: true | false
  example_answer_formats: []
  may_defer: yes | no
  safe_default_if_deferred:
  no_answer_consequence:

  dependencies:
    depends_on_questions: []
    may_change_questions: []

  escalation:
    frontier_escalation_if_answer_contains: []
    stop_conditions: []
```

## 7. Question-writing standard

Every question must:

- state the background and why the decision exists;
- explain the practical meaning of each option;
- explain what changes downstream;
- make clear whether the planner recommends an option and why;
- accept a free-form answer when option labels do not fit the user's actual intent;
- allow the user to ask for more context;
- avoid requiring the user to remember an old ID without explanation;
- distinguish a reversible provisional choice from an irreversible or high-impact decision;
- preserve uncertainty rather than forcing false precision.

Do not write:

```text
Choose A/B/C.
What should the authority be?
Do you approve?
```

without the necessary context in the same visible question block.

## 8. Next-tier interviewer contract

```yaml
next_tier_interviewer_contract:
  role: bounded_interactive_clarification_and_answer_capture
  may:
    - explain_question_context_and_purpose_from_the_package
    - explain_option_meanings_and_tradeoffs
    - ask_scoped_followups_to_interpret_the_answer
    - record_user_corrections_and_deferrals
    - maintain_a_cumulative_answer_ledger
    - detect_apparent_conflicts_with_fixed_decisions
    - return_unresolved_high_impact_items_to_frontier_review
  must:
    - preserve_question_IDs
    - distinguish_verbatim_answer_from_interpretation
    - summarize_each_interpreted_answer_for_user_correction
    - show_which_questions_remain
    - state_when_an_answer_changes_a_later_question
    - retain_unknown_when_the_user_is_unsure
    - stop_on_scope_or_authority_conflict
  must_not:
    - silently_select_for_the_user
    - invent_missing_owner_authority_privacy_architecture_or_acceptance_decisions
    - reopen_fixed_matters_without_explaining_the_conflict
    - change_the_project_goal
    - update_execution_source_or_target_truth
    - treat_tentative_language_as_confirmed
    - infer_personality_intelligence_or_stable_cognitive_style
    - resolve_a_high_impact_conflict_without_escalation
```

## 9. Interview flow

Recommended flow:

```text
receive and validate package
  -> present concise context synopsis
  -> ask one question or one coherent dependency group
  -> explain context/options when requested
  -> capture answer verbatim or by safe reference
  -> restate interpretation and invite correction
  -> update visible answer ledger
  -> follow dependency order
  -> stop and escalate on high-impact conflict
  -> return complete clarification result
```

The interviewer should not force every question into a single message when the user prefers incremental discussion. It should preserve state in the visible answer ledger rather than relying on human short-term memory.

## 10. Cumulative answer ledger

```yaml
answer_ledger:
  package_id:
  completed_questions: []
  current_question:
  remaining_questions: []
  answers:
    - question_id:
      user_answer_verbatim_or_safe_ref:
      interpreted_answer:
      interpretation_confirmed: yes | no | provisional
      corrections: []
      deferred: true | false
      residual_uncertainty: []
  newly_detected_conflicts: []
  frontier_escalations_required: []
```

After each material answer, show a concise human-readable version of the updated ledger.

## 11. Clarification result package

```yaml
clarification_result:
  result_id:
  package_id:
  interviewer_actor_and_surface:
  operator_visible_selection:
  exact_backend: unknown_or_not_attestable_unless_provider_metadata_exists
  started_at:
  completed_at:
  question_results:
    - question_id:
      user_answer_verbatim_or_safe_ref:
      interpreted_answer:
      interpretation_confirmed: yes | no | provisional
      corrections: []
      deferred: true | false
      residual_uncertainty: []
  new_conflicts_or_dependencies: []
  unresolved_questions: []
  proposed_decision_records: []
  frontier_escalations_required: []
  next_safe_action:
  return_to:
```

The result is evidence for a later decision or repository task. It does not automatically modify execution source, target truth, requirements, or implementation.

## 12. Capability estimate

```yaml
model_capability_estimate:
  frontier_packet_preparation:
    capability_class: FRONTIER_REQUIRED | FRONTIER_RECOMMENDED | FRONTIER_OPTIONAL
    reason:

  bounded_interactive_clarification:
    capability_class: NEXT_TIER_SUFFICIENT_CANDIDATE
    prerequisites:
      - frozen_self_contained_package
      - context_and_option_meanings_present
      - exact_question_IDs
      - answer_ledger
      - stop_and_escalation_rules

  mechanical_validation:
    capability_class: MECHANICAL_ONLY
    checks:
      - question_ID_uniqueness
      - required_field_presence
      - answer_completeness
      - fixed_decision_conflict_flags

  final_adjudication:
    capability_class: FRONTIER_RECOMMENDED_or_REQUIRED_when_high_impact_conflict_exists
```

## 13. Deep Research relationship

The planner must not use this package to ask the user questions that should be answered through evidence gathering.

```yaml
deep_research_assessment:
  status: NOT_NEEDED | OPTIONAL_VALUE | RECOMMENDED | REQUIRED_BEFORE_HIGH_IMPACT_DECISION | DEFER_UNTIL_UPSTREAM_DEPENDENCY
  questions_removed_from_user_clarification_and_routed_to_research: []
  task_artifact_refs: []
  report_needed_before_remaining_questions: yes | no
```

When research must happen first, mark dependent questions as blocked rather than asking the user to choose without evidence.

## 14. Final boundaries

- The package is not execution source.
- It does not authorize model switching, quota use, research execution, repository writes, or target writes.
- It does not let a next-tier model decide high-impact owner matters.
- It does not convert user answers into approved requirements without the applicable review/decision workflow.
- It does not permit psychological or cognitive profiling.
- It does not replace raw input preservation, evidence references, or user correction.
