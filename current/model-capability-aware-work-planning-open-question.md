# Model-Capability-Aware Work Planning — Open Question

> Non-execution-source live open-question record. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
open_question_id: MODEL-CAPABILITY-PLANNING-001
record_type: live_non_execution_source_open_question
created_by_task: MNEMOSYNE-163
last_status_task: MNEMOSYNE-173
status: prerequisite_evidence_available_ready_for_future_bounded_route_selection
user_decision_recorded: true
source_raw: raw/chatgpt-discussion-058.md
execution_source: current/human-approved-spec.md
formal_mainline_selected: false
implementation_authorized: false
controlled_validation_completed: false
```

## 1. User constraint retained

Mnemosyne and future target-Agent artifacts must not state or imply that the user will always execute work with the most capable available model or highest reasoning tier.

The intended operating pattern is:

- concentrate genuinely deep, large-scale, high-impact reasoning into visible stages;
- notify the user before those stages so the user can choose Pro or another provider's frontier model;
- use a next-tier model for bounded, lower-difficulty, routine or mechanical work when adequate;
- preserve scarce frontier-model quota rather than spend it on every small Agent request;
- design and validate instructions so that a next-tier executor can meet the required contract where the task is suitable;
- keep task capability requirements independent of volatile provider/model names.

This is a workflow and resource constraint, not a permanent provider routing table.

## 2. Distinction from run provenance

```yaml
model_provenance:
  question: what_actor_surface_visible_selection_review_and_attestable_backend_facts_applied_to_a_run
  current_guard: current/run-context-and-pr-provenance-guard.md

model_capability_planning:
  question: what_reasoning_capability_the_task_requires_and_how_work_should_be_split_escalated_and_verified
  current_status: open_ready_for_bounded_study

lower_tier_executability:
  question: whether_a_non_frontier_executor_can_follow_the_artifact_and_meet_the_acceptance_contract
  current_status: design_time_examples_exist_controlled_validation_absent
```

A frontier model producing an artifact does not prove that the artifact requires a frontier model to execute. A mechanically described task does not prove that a lower-tier model will preserve semantic, authority and safety boundaries.

## 3. Evidence prerequisite now satisfied

MNEMOSYNE-163 originally deferred a dedicated study until the four isolated Pro Deep Research reports returned. That prerequisite is now satisfied.

```yaml
available_evidence:
  four_topic_Pro_research_batch:
    state: complete_reviewed_and_ingested_as_non_execution_source_evidence
    cycle: RC-2026Q3-target-memory-governance-and-learning
    topics:
      - HO_GUIDANCE
      - learner_state_and_cognitive_coaching
      - cross_Agent_shared_memory
      - target_memory_migration

  Meta_Agent_first_target_build:
    M0_M1: merged_PR_221
    M2: merged_PR_222
    bootstrap_review: merged_PR_224_PASS_WITH_LIMITATIONS
    capability_split_used:
      - frontier_reasoning_and_human_decision
      - bounded_next_tier_execution
      - mechanical_verification
      - owner_acceptance
    evidence_role: first_design_and_build_example_not_controlled_model_comparison

  Adaptive_Explanation_Stage_A:
    state: current_mainline_prompt_ready_not_executed
    relation: future_research_report_may_supply_additional_task_decomposition_and_evaluation_evidence
```

The Meta-Agent build demonstrates that a task can be structured around frozen inputs, exact paths, stable IDs, acceptance checks, stop conditions and escalation boundaries. It does **not** establish that a specific next-tier model can execute the same task reliably, because no controlled same-input model comparison was performed.

## 4. Remaining questions

The repository still lacks an approved answer for:

- how to classify reasoning/capability demand independently of provider model names;
- how to split an Agent-building route into frontier-reasoning, bounded execution, mechanical verification and human-decision components;
- what evidence permits a next-tier model to be treated as adequate for an instruction set;
- how taskbooks should expose escalation triggers, uncertainty, verification and fallback behavior;
- whether selected Mnemosyne guidance and target-project artifacts are understandable to a next-tier executor;
- when verification and rework cost erase the benefit of delegation;
- how to alert the user before a frontier stage without forcing a model-choice interruption for every task;
- how to prevent the construction model's capability from becoming an implicit target-product runtime dependency;
- how capability requirements should change across design, implementation, review, handoff and maintenance.

## 5. Candidate dimensions — not approved schema

```yaml
candidate_dimensions:
  task_reasoning_demand:
    - mechanical_or_exact_transformation
    - bounded_rule_application
    - localized_judgment
    - multi_source_synthesis
    - architecture_or_policy_adjudication
    - open_ended_research_or_novel_design

  decomposition:
    - frontier_reasoning_components
    - next_tier_execution_components
    - mechanical_verification_components
    - human_decision_components

  escalation:
    - uncertainty_or_conflict_trigger
    - authority_or_safety_trigger
    - context_scale_trigger
    - novel_architecture_trigger
    - failed_validation_trigger
    - excessive_rework_or_review_trigger

  executor_support:
    - self_contained_inputs
    - explicit_authority_and_forbidden_actions
    - exact_or_bounded_scope
    - acceptance_criteria
    - deterministic_checks
    - stop_on_ambiguity
    - return_to_frontier_reviewer

  fallback:
    - block_and_request_stronger_review
    - narrow_scope
    - produce_candidate_only
    - perform_mechanical_substeps_only
    - defer_until_user_selects_a_frontier_condition
```

These dimensions are analysis aids only. They do not define a mandatory field set, score, threshold or provider mapping.

## 6. Candidate future study

A future bounded route should combine four layers.

### Layer A — Repository and artifact analysis

- select representative Mnemosyne and target-project tasks;
- identify implicit expert assumptions, long-context dependence and unstated judgment;
- determine where exact anchors, schemas, checklists, stop conditions and mechanical evidence reduce capability demand;
- separate failures caused by reasoning, context, instruction, tool access, observability, authority or product orchestration.

### Layer B — Controlled read-only replay

Use pinned inputs and one acceptance rubric under user-selected visible conditions:

```yaml
comparison_conditions:
  frontier_condition: selected_by_user_at_test_time
  next_tier_condition: selected_by_user_at_test_time
  exact_served_backend: unknown_or_not_attestable_unless_provider_metadata_exists
```

Compare:

- task correctness;
- evidence recovery;
- authority and prohibited-action adherence;
- hallucination or invented facts;
- escalation behavior;
- output usability;
- mechanical-check results;
- reviewer time and rework burden.

Neither tested run may declare itself final.

### Layer C — Decomposition pilot

Compare:

1. a monolithic frontier execution;
2. frontier planning/adjudication plus next-tier bounded execution and mechanical verification.

Measure whether the second pattern actually saves frontier quota after verification and rework.

### Layer D — Target-product portability

Verify that ordinary use of a future Meta-Agent or small business Agent does not silently require the model that designed it. Functions that genuinely need higher capability should be explicit escalation points rather than making the entire product frontier-only.

## 7. Representative task candidates

These are candidates for later user review, not an approved test set:

```yaml
candidate_task_classes:
  mechanical:
    - exact_path_and_ID_validation
    - status_field_synchronization_from_pinned_facts
  bounded_execution:
    - populate_a_frozen_small_target_file_set
    - apply_an_approved_additive_template_change
  localized_judgment:
    - review_a_handoff_for_missing_roles_or_conflicts
    - classify_one_feedback_item_without_promoting_it
  frontier_required_candidate:
    - reconstruct_an_ambiguous_user_problem
    - adjudicate_owner_truth_privacy_or_methodology_change
```

Meta-Agent M2 is a useful bounded-execution candidate only if replay inputs are sanitized and repository writes are prohibited during the test.

## 8. Decisions required before controlled validation

A later decision package should ask the user to select:

- the currently visible frontier condition;
- the currently visible next-tier condition used in real small-task practice;
- acceptable errors, reviewer burden and rework;
- representative task classes;
- whether tests remain synthetic/read-only or include a separate approved low-risk write case;
- whether the initial policy candidate is:
  - `next_tier_unless_escalated`;
  - `frontier_for_design_next_tier_for_execution`;
  - another explicit policy.

Exact product labels must be captured at test time, not hard-coded into durable guidance.

## 9. Current route relation

```yaml
route_relation:
  selected_current_mainline: PRO_DR_ADAPTIVE_EXPLANATION_STAGE_A_001
  MODEL_CAPABILITY_PLANNING_001:
    queued: true
    ready_for_future_selection: true
    selected_now: false
  reason_for_not_starting_now:
    - preserve_single_substantive_mainline
    - current_Stage_A_prompt_is_already_prepared_and_user_accepted
    - no_user_selected_frontier_and_next_tier_test_conditions_yet
```

## 10. Safe next action

```yaml
safe_next_action:
  current:
    - preserve_this_open_question_as_ready_but_unselected
    - execute_and_review_the_current_Adaptive_Explanation_Stage_A_research
  when_user_selects_this_route:
    - prepare_one_bounded_read_only_model_capability_replay_package
    - present_candidate_task_set_and_acceptance_rubric
    - ask_user_to_select_visible_frontier_and_next_tier_conditions
    - prohibit_repository_and_target_writes_unless_separately_authorized
```

## 11. Boundaries

- This record is not execution source or approved routing policy.
- It does not require frontier models for all Mnemosyne, Meta-Agent or target-Agent work.
- It does not declare a current model hierarchy or attest a backend.
- It does not authorize automatic model selection, switching, quota consumption or provider routing.
- It does not approve a capability schema, threshold, score or mandatory field.
- It does not claim a next-tier model is adequate before controlled evidence exists.
- It does not modify Meta-Agent target truth or product-route ownership.
- It does not start the controlled replay or create a new Deep Research task.
