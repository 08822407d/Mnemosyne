# Model-Capability-Aware Work Planning — Open Question

> Non-execution-source live open-question record. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
open_question_id: MODEL-CAPABILITY-PLANNING-001
record_type: live_non_execution_source_open_question
created_by_task: MNEMOSYNE-163
last_status_task: MNEMOSYNE-177
status: interim_user_facing_estimation_guard_adopted_controlled_validation_still_open
user_decision_recorded: true
source_raw: raw/chatgpt-discussion-058.md
active_behavior_guard: current/user-operation-next-step-capability-and-intent-guard.md
execution_source: current/human-approved-spec.md
formal_controlled_validation_mainline_selected: false
implementation_of_automatic_routing_authorized: false
controlled_validation_completed: false
```

## 1. User constraint retained

Mnemosyne and future target-Agent artifacts must not state or imply that the user will always execute work with the most capable available model or highest reasoning tier.

The intended operating pattern is:

- concentrate genuinely deep, large-scale, open-ended, ambiguous, or high-impact reasoning into visible stages;
- notify the user before those stages so the user can choose Pro or another provider's frontier model;
- use a next-tier model for bounded, lower-difficulty, routine, or mechanical work when adequate;
- preserve scarce frontier-model quota rather than spend it on every small Agent request;
- design and validate instructions so a next-tier executor can meet the required contract where suitable;
- keep durable capability requirements independent of volatile provider/model names;
- re-estimate after upstream research or failures change the downstream task.

This is a workflow and resource constraint, not a permanent provider routing table.

## 2. Interim operational rule now adopted

MNEMOSYNE-177 adopts a user-facing behavior guard requiring every meaningful closing `## 下一步` section to state whether the next stage:

```yaml
capability_class:
  - FRONTIER_REQUIRED
  - FRONTIER_RECOMMENDED
  - FRONTIER_OPTIONAL
  - NEXT_TIER_SUFFICIENT_CANDIDATE
  - MECHANICAL_ONLY
  - UNKNOWN_REASSESS_BEFORE_EXECUTION
```

The user-facing text must explicitly say whether Pro/frontier capability is required, recommended, unnecessary, or currently unknown.

The estimate must separate:

```yaml
decomposition:
  frontier_reasoning:
  next_tier_execution:
  mechanical_verification:
  human_decision:
```

This is an interim planning and communication rule. It does not prove a lower-tier model is adequate, does not select a provider, and does not close the controlled-validation question.

## 3. Distinction from run provenance

```yaml
model_provenance:
  question: what_actor_surface_visible_selection_review_and_attestable_backend_facts_applied_to_a_run
  current_guard: current/run-context-and-pr-provenance-guard.md

model_capability_planning:
  question: what_reasoning_capability_the_task_requires_and_how_work_should_be_split_escalated_and_verified
  current_status: interim_reporting_rule_active_controlled_validation_open

lower_tier_executability:
  question: whether_a_non_frontier_executor_can_follow_the_artifact_and_meet_the_acceptance_contract
  current_status: design_time_examples_exist_controlled_validation_absent
```

A frontier model producing an artifact does not prove that the artifact requires a frontier model to execute. A mechanically described task does not prove that a lower-tier model will preserve semantic, authority, and safety boundaries.

## 4. Evidence now available

```yaml
available_evidence:
  four_topic_Pro_research_batch:
    state: complete_reviewed_and_ingested_as_non_execution_source_evidence
    cycle: RC-2026Q3-target-memory-governance-and-learning

  Meta_Agent_first_target_build:
    M0_M1: merged_PR_221
    M2: merged_PR_222
    bootstrap_review: merged_PR_224_PASS_WITH_LIMITATIONS
    capability_split_used:
      - frontier_reasoning_and_human_decision
      - bounded_next_tier_execution
      - mechanical_verification
      - owner_acceptance
    evidence_role: design_and_build_example_not_controlled_model_comparison

  Adaptive_Explanation_Stage_A:
    state: completed_reviewed_and_ingested_via_PR_227
    disposition: ACCEPT_WITH_CORRECTIONS_AND_PREPARE_STAGE_B_DECISION_PACKAGE
    relation:
      - supports_decomposition_between_open_research_protocol_execution_and_adjudication
      - does_not_validate_any_model_tier

  Adaptive_Explanation_Stage_B0:
    protocol_design: merged_PR_228
    smoke_execution_authorized: true
    execution_preflight: CONTEXT_ISOLATION_FAILURE
    cells_started: 0
    evidence_role:
      - demonstrates_surface_capability_can_block_a_bounded_task_independently_of_reasoning_quality
      - demonstrates_that_task_label_and_model_strength_do_not_replace_context_isolation
```

The B0 failure is especially important: a frozen task may be suitable for a next-tier model yet still be impossible on the current product surface because the surface lacks isolated worker contexts.

## 5. Remaining open questions

The repository still lacks a controlled answer for:

- how to classify reasoning demand independently of provider names;
- what evidence permits a next-tier model to be treated as adequate for an instruction set;
- whether selected Mnemosyne and target-project artifacts are understandable to a next-tier executor;
- how much review and rework erase delegation savings;
- how capability requirements change across design, implementation, review, handoff, and maintenance;
- how product-surface capabilities such as context isolation, file binding, tool access, and observability interact with model reasoning strength;
- how to alert the user before a frontier stage without forcing unnecessary model-choice interruptions;
- how to prevent the construction model's capability from becoming an implicit target-product runtime dependency;
- what same-input benchmark is representative enough to justify an operational routing candidate.

## 6. Candidate task-demand dimensions

```yaml
candidate_dimensions:
  task_reasoning_demand:
    - mechanical_or_exact_transformation
    - bounded_rule_application
    - localized_judgment
    - multi_source_synthesis
    - architecture_or_policy_adjudication
    - open_ended_research_or_novel_design

  surface_requirements:
    - context_isolation
    - tool_or_file_access
    - exact_input_output_identity
    - long_context_capacity
    - parallel_worker_support
    - reviewer_separation
    - observability_and_audit

  escalation:
    - uncertainty_or_conflict_trigger
    - authority_or_safety_trigger
    - context_scale_trigger
    - novel_architecture_trigger
    - failed_validation_trigger
    - surface_capability_failure
    - excessive_rework_or_review_trigger

  executor_support:
    - self_contained_inputs
    - explicit_authority_and_forbidden_actions
    - exact_or_bounded_scope
    - acceptance_criteria
    - deterministic_checks
    - stop_on_ambiguity
    - return_to_frontier_reviewer
```

These are analysis aids, not a mandatory schema, score, or provider mapping.

## 7. Interim estimation rules

### Frontier-required or recommended candidates

- ambiguous problem reconstruction from symptoms or incomplete user wording;
- greenfield or immature-domain architecture;
- owner, truth-source, privacy, trust-boundary, or irreversible migration changes;
- high-impact conflict adjudication;
- methodology promotion from local evidence;
- severe-failure and disputed-result adjudication.

### Next-tier candidates

- frozen self-contained inputs;
- exact paths, IDs, output schema, and stop conditions;
- bounded application of already approved rules;
- exact Tutor cells or file population with independent review;
- low-risk additive maintenance.

### Mechanical candidates

- file/path existence;
- hashes and byte identity;
- schema and ID uniqueness;
- deterministic transformations;
- exact comparisons and forbidden-material scans.

A mixed task should be decomposed rather than assigned wholesale to the strongest model.

## 8. Candidate future controlled study

A future bounded route should combine:

### Layer A — Artifact analysis

- select representative Mnemosyne and target-project tasks;
- identify implicit expert assumptions, long-context dependence, surface dependencies, and unstated judgment;
- determine where schemas, checklists, stop conditions, and mechanical evidence lower capability demand.

### Layer B — Read-only same-input replay

```yaml
comparison_conditions:
  frontier_condition: selected_by_user_at_test_time
  next_tier_condition: selected_by_user_at_test_time
  exact_served_backend: unknown_or_not_attestable_unless_provider_metadata_exists
```

Compare correctness, evidence recovery, authority adherence, hallucination, escalation, output usability, mechanical checks, reviewer time, and rework burden.

### Layer C — Decomposition pilot

Compare:

1. monolithic frontier execution;
2. frontier planning/adjudication plus next-tier bounded execution and mechanical verification.

Measure whether the second pattern actually reduces frontier usage after review and rework.

### Layer D — Surface capability matrix

Test whether a model-capable task still fails because the product surface lacks required isolation, file binding, tool access, or auditability. B0 provides the first concrete surface-blocking example.

### Layer E — Target-product portability

Verify that ordinary operation of Meta-Agent or a small business Agent does not silently require the construction model. Genuine frontier functions should be explicit escalation points.

## 9. Representative task candidates

```yaml
candidate_task_classes:
  mechanical:
    - exact_path_and_ID_validation
    - status_field_synchronization_from_pinned_facts
  bounded_execution:
    - populate_a_frozen_small_target_file_set
    - execute_an_isolated_frozen_synthetic_Tutor_cell
  localized_judgment:
    - review_a_handoff_for_missing_roles_or_conflicts
    - classify_one_feedback_item_without_promoting_it
  frontier_required_candidate:
    - reconstruct_an_ambiguous_user_problem
    - adjudicate_owner_truth_privacy_or_methodology_change
  surface_capability_candidate:
    - verify_worker_context_isolation_before_multi_condition_experiment
```

## 10. Decisions required before controlled validation

A later decision package should ask the user to select:

- currently visible frontier and next-tier conditions;
- acceptable errors, reviewer burden, and rework;
- representative task classes;
- a product surface with adequate isolation and evidence;
- whether tests remain synthetic/read-only;
- whether the initial policy candidate is `next_tier_unless_escalated`, `frontier_for_design_next_tier_for_execution`, or another explicit pattern.

Exact product labels must be captured at test time, not hard-coded into durable guidance.

## 11. Current route relation

```yaml
route_relation:
  Adaptive_Explanation_Stage_B0:
    state: blocked_CONTEXT_ISOLATION_FAILURE_zero_cells
    current_requirement: select_or_defer_an_isolated_execution_surface
  MODEL_CAPABILITY_PLANNING_001:
    queued: true
    interim_reporting_guard_active: true
    controlled_validation_ready_for_future_selection: true
    selected_as_current_mainline: false
```

## 12. Safe next action

```yaml
safe_next_action:
  current:
    - preserve_the_interim_user_facing_capability_estimation_guard
    - do_not_claim_controlled_lower_tier_validation
  when_user_selects_the_controlled_route:
    - prepare_one_bounded_read_only_model_capability_replay_package
    - include_surface_capability_as_a_separate_dimension
    - ask_user_to_select_visible_frontier_and_next_tier_conditions
    - prohibit_repository_and_target_writes_unless_separately_authorized
```

## 13. Boundaries

- This record is not execution source or approved automatic routing policy.
- It does not require frontier models for all work.
- It does not declare a current provider hierarchy or attest a backend.
- It does not authorize automatic model selection, switching, or quota consumption.
- It does not prove a next-tier model is adequate.
- It does not modify Meta-Agent target truth or product-route ownership.
