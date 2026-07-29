# Model-Capability-Aware Work Planning — Open Question

> Non-execution-source live open-question record. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
open_question_id: MODEL-CAPABILITY-PLANNING-001
record_type: live_non_execution_source_open_question
created_by_task: MNEMOSYNE-163
last_status_task: MNEMOSYNE-178
status: interim_capability_research_and_clarification_guard_adopted_controlled_validation_still_open
user_decision_recorded: true
source_raw: raw/chatgpt-discussion-058.md
active_behavior_guard: current/user-operation-next-step-capability-and-intent-guard.md
clarification_template: notes/templates/frontier-planned-clarification-package-v0.1.md
research_status: current/frontier-planning-clarification-handoff-research-status.md
execution_source: current/human-approved-spec.md
formal_controlled_validation_mainline_selected: false
implementation_of_automatic_model_or_research_routing_authorized: false
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
- re-estimate after upstream research or failures change the downstream task;
- separately assess whether Pro Deep Research or an independent frontier review is worth the cost;
- automatically prepare research tasks when research is recommended and sufficiently specified, without automatically spending quota;
- let a frontier planner prepare context-rich clarification packages so a next-tier model can conduct bounded interactive clarification without degrading the user's intent.

This is a workflow and resource constraint, not a permanent provider routing table.

## 2. Interim operational rule now adopted

The active guard requires every meaningful closing `## 下一步` section to state:

```yaml
capability_class:
  - FRONTIER_REQUIRED
  - FRONTIER_RECOMMENDED
  - FRONTIER_OPTIONAL
  - NEXT_TIER_SUFFICIENT_CANDIDATE
  - MECHANICAL_ONLY
  - UNKNOWN_REASSESS_BEFORE_EXECUTION

deep_research_status:
  - NOT_NEEDED
  - OPTIONAL_VALUE
  - RECOMMENDED
  - REQUIRED_BEFORE_HIGH_IMPACT_DECISION
  - DEFER_UNTIL_UPSTREAM_DEPENDENCY
  - UNAVAILABLE_OR_QUOTA_BLOCKED

parallel_frontier_research_status:
  - NOT_NEEDED
  - OPTIONAL_INDEPENDENT_CHALLENGE
  - RECOMMENDED_HETEROGENEOUS_REVIEW
  - REQUIRED_FOR_HIGH_IMPACT_ACCEPTANCE
  - DEFER_UNTIL_PRIMARY_RESULT
  - UNAVAILABLE
```

The user-facing text must explicitly say:

- whether Pro/frontier capability is required, recommended, unnecessary, or unknown;
- whether Pro Deep Research is needed, optional, recommended, required, or premature;
- whether independent Fable-class/other-provider research has a distinct role;
- which bounded components can use a next-tier model;
- what evidence, failure, or scope change will trigger re-estimation.

The estimate must separate:

```yaml
decomposition:
  frontier_reasoning:
  next_tier_execution:
  mechanical_verification:
  human_decision:
  Deep_Research:
  independent_frontier_review:
```

When research is recommended or required and the topic is frozen, the planner should create a ready-to-run task and report contract in the same response. This does not authorize model switching, quota spend, or research execution and does not permit fabricating a report before the run exists.

## 3. Frontier-planned clarification handoff

The user wants frontier quota preserved during interactive human clarification without reducing the quality of context and explanation.

The interim pattern is:

```text
frontier planner reconstructs problem and decision structure
  -> routes unknowns to user decision, fact check, research, design judgment, or missing artifact
  -> prepares context-rich questions and option meanings
  -> next-tier interviewer conducts bounded interaction and maintains answer ledger
  -> frontier reviewer re-enters for high-impact conflict or final adjudication
```

A next-tier interviewer is only a candidate when the packet is frozen and self-contained. Each material question must include background, purpose, current interpretation, option meanings, consequences, recommendation, deferral/default behavior, dependencies, and escalation triggers.

The interviewer must preserve verbatim answers separately from interpretations, allow correction, explain why questions matter, maintain a cumulative ledger, and stop on new authority, privacy, architecture, trust-boundary, or product-goal conflicts.

This pattern remains unvalidated.

## 4. Distinction from run provenance

```yaml
model_provenance:
  question: what_actor_surface_visible_selection_review_and_attestable_backend_facts_applied_to_a_run
  current_guard: current/run-context-and-pr-provenance-guard.md

model_capability_planning:
  question: what_reasoning_capability_the_task_requires_and_how_work_should_be_split_escalated_and_verified
  current_status: interim_reporting_rule_active_controlled_validation_open

research_trigger_planning:
  question: when_external_evidence_value_justifies_Deep_Research_or_parallel_frontier_review
  current_status: interim_rule_and_tasks_prepared_validation_open

clarification_handoff:
  question: whether_a_frontier_planned_packet_allows_a_next_tier_model_to_interact_with_the_user_without_intent_loss
  current_status: candidate_template_prepared_controlled_validation_absent

lower_tier_executability:
  question: whether_a_non_frontier_executor_can_follow_the_artifact_and_meet_the_acceptance_contract
  current_status: design_time_examples_exist_controlled_validation_absent
```

A frontier model producing an artifact does not prove that the artifact requires a frontier model to execute. A mechanically described task does not prove that a lower-tier model will preserve semantic, authority, safety, research, and intent boundaries.

## 5. Evidence now available

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
    execution_preflight: CONTEXT_ISOLATION_FAILURE_recorded_via_PR_229
    cells_started: 0
    evidence_role:
      - demonstrates_surface_capability_can_block_a_bounded_task_independently_of_reasoning_quality
      - demonstrates_that_task_label_and_model_strength_do_not_replace_context_isolation

  user_operation_capability_intent_guard:
    initial_adoption: merged_PR_229
    v0_2_research_and_clarification_amendment: pending_MNEMOSYNE_178
    evidence_role: explicit_user_workflow_requirement_not_controlled_validation
```

The B0 failure is especially important: a frozen task may be suitable for a next-tier model yet remain impossible on the current product surface because the surface lacks isolated worker contexts.

## 6. Remaining open questions

The repository still lacks a controlled answer for:

- how to classify reasoning demand independently of provider names;
- what evidence permits a next-tier model to be treated as adequate for an instruction set;
- whether selected Mnemosyne and target-project artifacts are understandable to a next-tier executor;
- how much review and rework erase delegation savings;
- how capability requirements change across design, implementation, review, handoff, clarification, and maintenance;
- how product-surface capabilities such as context isolation, file binding, tool access, and observability interact with model reasoning strength;
- how to alert the user before a frontier stage without forcing unnecessary model-choice interruptions;
- how to prevent the construction model's capability from becoming an implicit target-product runtime dependency;
- what same-input benchmark is representative enough to justify an operational routing candidate;
- whether context-rich clarification packets actually reduce user memory burden and intent loss;
- how often next-tier interviewers invent context, misread tentative answers, or fail to escalate;
- which fields in the clarification package are necessary and which create bureaucracy;
- what decision-value threshold justifies Pro Deep Research;
- how to avoid both over-research and under-research;
- when parallel frontier research adds independent value rather than duplicate cost;
- whether automatic research-task delivery reduces frontier turns without creating premature or badly framed prompts.

## 7. Candidate task-demand and research dimensions

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

  research_need:
    - stable_authoritative_fact_check
    - distributed_multi_source_evidence
    - contested_or_heterogeneous_evidence
    - novel_or_immature_domain
    - high_impact_irreversible_decision
    - owner_decision_not_researchable
    - upstream_dependency_not_ready

  clarification_handoff:
    - context_completeness
    - question_dependencies
    - option_meaning_and_tradeoffs
    - user_memory_support
    - answer_ledger
    - contradiction_detection
    - escalation_contract

  escalation:
    - uncertainty_or_conflict_trigger
    - authority_or_safety_trigger
    - context_scale_trigger
    - novel_architecture_trigger
    - failed_validation_trigger
    - surface_capability_failure
    - research_evidence_gap
    - next_tier_interviewer_drift
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

These are analysis aids, not a mandatory schema, score, threshold, or provider mapping.

## 8. Interim estimation rules

### Frontier-required or recommended candidates

- ambiguous problem reconstruction from symptoms or incomplete user wording;
- greenfield or immature-domain architecture;
- owner, truth-source, privacy, trust-boundary, or irreversible migration changes;
- high-impact conflict adjudication;
- methodology promotion from local evidence;
- severe-failure and disputed-result adjudication;
- designing a multi-question clarification package when option meanings and dependencies materially shape the product;
- deciding whether an evidence gap warrants expensive Deep Research when the decision value is unclear.

### Next-tier candidates

- frozen self-contained inputs;
- exact paths, IDs, output schema, and stop conditions;
- bounded application of already approved rules;
- exact Tutor cells or file population with independent review;
- low-risk additive maintenance;
- conducting interactive clarification from a frozen context-rich package with explicit escalation rules.

### Mechanical candidates

- file/path existence;
- hashes and byte identity;
- schema and ID uniqueness;
- deterministic transformations;
- exact comparisons and forbidden-material scans;
- clarification question-ID, required-field, and answer-completeness checks.

A mixed task should be decomposed rather than assigned wholesale to the strongest model.

## 9. Prepared research tasks

```yaml
prepared_tasks:
  Pro_Deep_Research:
    research_id: PRO-DR-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001
    path: notes/research-prompts/PRO-DR-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001.md
    status: prepared_not_executed
    role: multidisciplinary_evidence_review_and_validation_design

  Fable_independent_challenge:
    task_id: FABLE5-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001
    path: notes/research-prompts/FABLE5-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001.md
    status: prepared_not_executed
    role: independent_problem_reconstruction_adversarial_review_and_alternative_architecture
```

The Pro task is recommended but not required to adopt the baseline user-requested behavior. The Fable task is optional now and recommended before making the workflow a mandatory cross-project default or high-impact execution-source rule.

## 10. Candidate future controlled study

A future bounded route should combine:

### Layer A — Artifact analysis

- select representative Mnemosyne and target-project tasks;
- identify implicit expert assumptions, long-context dependence, surface dependencies, unstated judgment, research gaps, and clarification dependencies;
- determine where schemas, checklists, stop conditions, context packets, and mechanical evidence lower capability demand.

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

### Layer E — Clarification handoff pilot

Compare:

```yaml
clarification_conditions:
  - bare_questions_or_option_codes
  - context_rich_questions_with_frontier_interviewer
  - frontier_packet_plus_next_tier_interviewer
  - frontier_packet_plus_next_tier_interviewer_with_answer_ledger_and_escalation
```

Measure context comprehension, answer fidelity, correction, option bias, contradiction detection, escalation, user burden, frontier turns saved, and downstream decision correctness.

### Layer F — Research-trigger replay

Use synthetic planning cases to compare:

- no research when needed;
- unnecessary Deep Research;
- premature task generation;
- appropriately staged research;
- duplicated parallel research;
- independent challenge with distinct decision value.

### Layer G — Target-product portability

Verify that ordinary operation of Meta-Agent or a small business Agent does not silently require the construction model. Genuine frontier functions should be explicit escalation points.

## 11. Representative task candidates

```yaml
candidate_task_classes:
  mechanical:
    - exact_path_and_ID_validation
    - status_field_synchronization_from_pinned_facts
    - clarification_package_required_field_validation

  bounded_execution:
    - populate_a_frozen_small_target_file_set
    - execute_an_isolated_frozen_synthetic_Tutor_cell
    - conduct_interactive_clarification_from_a_frozen_packet

  localized_judgment:
    - review_a_handoff_for_missing_roles_or_conflicts
    - classify_one_feedback_item_without_promoting_it
    - explain_option_context_without_changing_the_option_set

  frontier_required_candidate:
    - reconstruct_an_ambiguous_user_problem
    - adjudicate_owner_truth_privacy_or_methodology_change
    - design_the_clarification_question_set_and_option_architecture
    - decide_whether_research_is_required_before_a_high_impact_choice

  surface_capability_candidate:
    - verify_worker_context_isolation_before_multi_condition_experiment
```

## 12. Decisions required before controlled validation

A later decision package should ask the user to select:

- currently visible frontier and next-tier conditions;
- acceptable errors, reviewer burden, and rework;
- representative task classes;
- a product surface with adequate isolation and evidence;
- whether tests remain synthetic/read-only;
- clarification packet examples and answer-ledger format;
- Deep Research trigger cases and acceptable over/under-research errors;
- whether the initial policy candidate is `next_tier_unless_escalated`, `frontier_for_design_next_tier_for_execution`, or another explicit pattern.

Exact product labels must be captured at test time, not hard-coded into durable guidance.

## 13. Current route relation

```yaml
route_relation:
  Adaptive_Explanation_Stage_B0:
    state: blocked_CONTEXT_ISOLATION_FAILURE_zero_cells
    current_requirement: select_or_defer_an_isolated_execution_surface

  FRONTIER_PLANNING_CLARIFICATION_HANDOFF_RESEARCH:
    state: baseline_and_tasks_prepared_pending_MNEMOSYNE_178_merge
    Pro_research: recommended_not_required_for_baseline_adoption
    Fable_challenge: optional_now_recommended_before_mandatory_cross_project_propagation

  MODEL_CAPABILITY_PLANNING_001:
    queued: true
    interim_reporting_guard_active: true
    controlled_validation_ready_for_future_selection: true
    selected_as_current_mainline: false
```

## 14. Safe next action

```yaml
safe_next_action:
  current:
    - review_and_merge_the_single_MNEMOSYNE_178_PR
  after_merge:
    - use_the_v0_2_guard_in_Mnemosyne_conversations
    - execute_the_prepared_Pro_Deep_Research_task_when_quota_and_priority_allow
    - optionally_execute_the_independent_Fable_challenge
  research_execution_automatic: false
  target_project_propagation_automatic: false
```

## 15. Boundaries

- This record is not execution source or approved automatic routing policy.
- It does not require frontier models for all work.
- It does not declare a current provider hierarchy or attest a backend.
- It does not authorize automatic model selection, switching, quota consumption, or research execution.
- It does not prove a next-tier model is adequate.
- It does not make the prepared research tasks completed reports.
- It does not modify Meta-Agent target truth or product-route ownership.
