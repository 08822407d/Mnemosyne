# Mnemosyne Frontier Clarification Validation — Scoped Handoff Package

> Non-execution-source transfer artifact. This package transfers the PR #231 post-adjudication Mnemosyne maintenance task to a fresh conversation. It does not override `current/human-approved-spec.md`, select or execute validation, modify Meta-Agent, or take over the separately owned non-FABLE health-review route.

```yaml
package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-HANDOFF-001
created_by_task: MNEMOSYNE-180
repository: 08822407d/Mnemosyne
prepared_from_master: 96eb9757b6554d397267501dd29e4682c155d830
source_checkpoint:
  PR: 231
  merge_commit: 96eb9757b6554d397267501dd29e4682c155d830
  merged_at: 2026-07-29T10:03:45Z
package_status: non_execution_source_transfer_artifact
intended_receiver_action: receive_Mnemosyne_handoff
transferred_task: PREPARE_READ_ONLY_VALIDATION_PACKAGE
validation_execution_authorized: false
execution_source: current/human-approved-spec.md
execution_source_modified: false
```

## 1. Why this is the stable handoff point

The current source conversation has become very large. The route has nevertheless reached a clean checkpoint:

- the Pro Deep Research report is complete and accepted with corrections as primary non-execution-source evidence;
- the independent Fable report is complete and accepted with corrections as adversarial non-execution-source evidence;
- source sampling, evidence calibration and cross-report adjudication are complete;
- PR #231 merged the resulting guards, review records, research-cycle receipts and validation design;
- no additional same-topic Pro or Fable research is recommended;
- no validation cell, fixture package or partial run is in progress;
- no open PR existed when this handoff task began.

The next stage is therefore separable from the old conversation history: prepare a complete public/synthetic, read-only validation package, but do not execute it.

## 2. Receiver guidance load

```yaml
receiver_guidance_load:
  project_guidance: not_applicable
  mnemosyne_guidance: required
  ordered_operations:
    - receive_authorized_handoff_package
    - execute_Load_Mnemosyne_guidance_as_separate_operation
    - confirm_received_task_preserved
    - continue_received_task_under_refreshed_constraints
```

Handoff receive and guidance refresh are separate operations. The guidance refresh must not import `handoff/handoff-current.md`, `current/active-context.md`, `current/todo.md`, `current/open-questions.md`, the Meta-Agent product route, or the non-FABLE health-review route as this conversation's action plan.

## 3. Current execution source and authority boundary

```yaml
Mnemosyne_execution_source:
  path: current/human-approved-spec.md
  role: sole_execution_source

non_execution_sources:
  - this_handoff_package
  - current_status_files
  - handoff_files
  - research_reports_and_receipts
  - research_reviews_and_adjudication
  - validation_designs_and_future_taskbooks
  - model_inference
```

A research report, current view, handoff package, newer file or stronger model does not automatically change authority.

## 4. Completed work that must not be repeated

### 4.1 Research and adjudication

```yaml
completed_research_cycle:
  id: RC-2026Q3-frontier-planning-clarification-handoff
  Pro:
    task_id: PRO-DR-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001
    disposition: ACCEPT_WITH_CORRECTIONS_AS_PRIMARY_NON_EXECUTION_SOURCE_EVIDENCE
  Fable:
    task_id: FABLE5-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001
    disposition: ACCEPT_WITH_CORRECTIONS_AS_INDEPENDENT_ADVERSARIAL_NON_EXECUTION_SOURCE_EVIDENCE
    rerun_required: false
  additional_Pro_Deep_Research: not_needed
  additional_Fable_research: not_needed
```

Do not execute the completion redirects under `notes/research-prompts/`. The original completed task texts are archived under the research cycle.

### 4.2 Accepted risk-adaptive interpretation

No universal clarification architecture is approved.

```yaml
risk_adaptive_routes:
  DIRECT_FRONTIER:
    use_for:
      - high_impact_low_clarity
      - owner_authority_privacy_architecture_or_trust_boundary
      - material_problem_reconstruction
      - unresolved_conflicting_evidence_or_requirements

  STRUCTURED_OWNER_PACKAGE:
    use_for:
      - bounded_auditable_owner_decisions
      - direct_owner_completion_is_practical
      - live_interviewer_is_unnecessary_unavailable_or_unvalidated

  NEXT_TIER_INTERVIEWER:
    status: validation_gated_candidate
    eligible_only_when:
      - impact_is_low_or_moderate
      - question_meaning_and_scope_are_frozen
      - package_is_self_contained
      - user_can_reject_options_and_correct_interpretations
      - visible_reconstructable_ledger_exists
      - semantic_stop_and_frontier_reentry_rules_exist

  GATED_MIXED_ESCALATION:
    status: preferred_validation_candidate_for_mixed_impact_routes
    universal_default: false

  RESEARCH_FIRST:
    use_only_when:
      - external_evidence_gap_changes_owner_decision
      - upstream_scope_is_frozen
      - expected_information_value_justifies_cost_and_delay
```

### 4.3 Research-trigger rule

A ready-to-run research task may be generated only when all are true:

- the unknown is external and researchable;
- plausible answers change downstream action;
- upstream scope is sufficiently frozen;
- ordinary verification and current sources are insufficient;
- expected decision value justifies quota, cost and delay.

The task must state the decision it can change, upstream dependencies, stop condition, evidence requirements and return destination. The human retains provider/surface selection, quota trigger and execution authorization.

### 4.4 Deep Research delivery correction

One Deep Research run has one canonical substantive report. Product report view and Markdown/Word/PDF downloads are representations of that same report. Do not require an arbitrary second custom file unless the surface explicitly supports and confirms its creation.

## 5. Transferred local task

```yaml
transferred_task:
  id: PREPARE_READ_ONLY_VALIDATION_PACKAGE
  phase: design_only
  objective: convert_the_existing_validation_design_into_a_complete_frozen_execution_and_review_package
  execute_validation: false
  use_real_user_data: false
  target_project_write: false
  repository_write_by_future_validation_executor: false
  additional_literature_research: false
```

The receiver should prepare, in one bounded repository task where practical:

- package README and scope manifest;
- a representative public/synthetic scenario set;
- hidden author keys stored separately from worker-visible inputs;
- frozen Q0–Q4 condition contracts;
- question/answer-ledger and escalation test cases;
- blocking-invariant rubric and comparative measures;
- reviewer and adjudication instructions;
- V0 sentinel/context-isolation taskbook;
- V1 small-smoke execution taskbook;
- run manifest and result-return format;
- stop, rollback, invalid-run and escalation rules;
- capability decomposition and user-decision package for later execution.

The package should reuse and refine the existing validation design rather than silently inventing a new research question.

## 6. Validation design baseline

Current candidate conditions:

```yaml
Q0_bare_question:
  description: unexplained_question_or_option_codes

Q1_structured_nonconversational_package:
  description: context_rich_owner_decision_package_without_interviewer

Q2_packet_plus_next_tier_interviewer:
  description: frozen_frontier_packet_plus_next_tier_live_clarification

Q3_gated_mixed_escalation:
  description: Q2_plus_predefined_frontier_reentry_and_semantic_escalation

Q4_direct_frontier_clarification:
  description: frontier_planner_conducts_interaction
  role: high_fidelity_comparator_not_automatic_gold_truth
```

Current critical invariants include:

- no invented owner, authority, privacy or architecture decision;
- no tentative answer recorded as confirmed approval;
- no missed planted high-impact escalation;
- no hidden-key or cross-condition contamination;
- verbatim answer or safe reference remains separate from Agent interpretation;
- user can reject options and correct interpretation;
- prompt, packet and output identity are reconstructable.

Aggregate scores cannot override an unresolved critical-invariant failure.

## 7. What is unresolved and must remain unresolved at receive time

```yaml
unknowns_and_unselected_items:
  - final_synthetic_scenario_set
  - hidden_author_keys
  - final_Q0_to_Q4_prompt_contracts
  - reviewer_arrangement_and_independence_limitations
  - exact_smoke_size_and_progression_threshold
  - execution_surface_with_provable_context_isolation
  - visible_frontier_and_next_tier_model_or_mode_conditions_at_test_time
  - quota_or_cost_authorization
  - acceptable_burden_and_error_boundaries
  - post_validation_adoption_decision
```

Do not turn these into implicit defaults. Package preparation may propose recommendations and explain consequences, but actual execution remains separately gated.

## 8. Context-isolation and execution-surface boundary

Each future condition × scenario cell must use an isolated context appropriate to the condition. A worker must not see hidden labels, expected answers, other-condition outputs or reviewer scores. Reviewer context must be separate from worker context. Exact prompt/packet/output identity must be preserved.

If a future surface cannot establish the required isolation, it must return:

```yaml
status: CONTEXT_ISOLATION_FAILURE
cells_started: 0
```

The ordinary maintenance conversation is not automatically an eligible validation-execution surface.

## 9. Capability decomposition

```yaml
capability_decomposition:
  frontier_reasoning:
    - author_and_review_synthetic_scenarios
    - define_hidden_keys_and_material_ambiguities
    - freeze_condition_semantics_and_blocking_invariants
    - adjudicate_high_impact_failures_and_cross_condition_results

  next_tier_candidate:
    - populate_frozen_files
    - execute_frozen_Q2_or_Q3_interviews_after_surface_validation
    - maintain_ledgers_and_return_structured_results

  mechanical:
    - IDs_and_required_fields
    - matrix_completeness
    - sentinel_isolation_tests
    - exact_input_output_hashing
    - forbidden_material_scan

  human_decisions_before_execution:
    - visible_model_or_mode_conditions
    - execution_surface_and_quota
    - acceptable_burden_and_failure_boundaries
    - progression_from_V0_to_V1_or_beyond
```

The validation-package design is `FRONTIER_RECOMMENDED`; frozen population and mechanical checks need not consume frontier quota.

## 10. Route ownership and non-interference

```yaml
route_ownership:
  this_handoff:
    route: Mnemosyne_self_development_frontier_clarification_validation
    receiver: fresh_Mnemosyne_maintenance_conversation

  Meta_Agent_product_build:
    owner: existing_dedicated_Meta_Agent_conversation
    current_stage: owner_review_and_disposition
    default_substantive_write_root: target-projects/meta-agent/
    takeover_by_receiver: prohibited

  non_FABLE_comprehensive_health_review:
    owner: its_existing_separate_conversation
    current_global_handoff_file_may_reference_it: true
    takeover_by_receiver: prohibited
```

Do not modify `target-projects/meta-agent/`, perform Meta-Agent owner acceptance, or use `handoff/handoff-current.md` as this route's task source.

## 11. Mandatory evidence read order

Read the minimum first layer:

1. `handoff/mnemosyne-frontier-clarification-validation-handoff-package.md`;
2. `commands/receive-mnemosyne-handoff.md`;
3. `current/human-approved-spec.md`;
4. `current/frontier-planning-clarification-handoff-research-status.md`;
5. `current/frontier-planning-clarification-handoff-adjudication-guard.md`;
6. `current/deep-research-report-delivery-correction-guard.md`;
7. `notes/validation-designs/frontier-planning-clarification-handoff-read-only-validation-v0.1.md`;
8. `notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/03-cross-report-consensus-conflict-and-adjudication.md`;
9. `notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/04-interim-architecture-and-validation-decision.md`.

Read on demand:

- the source-audit and input-reliability reviews;
- the research-cycle manifest and report receipts;
- `current/model-capability-aware-work-planning-open-question.md`;
- `current/user-operation-next-step-capability-and-intent-guard.md`.

Do not bulk-load old conversation exports, all historical task results, all TODOs or all research reports unless a specific conflict or audit need requires them.

## 12. First receive operation

The receiver's first response is receive-only. It must verify the latest `master`, confirm this handoff PR is merged, read the minimum first layer, report missing/conflicting sources and stop.

```yaml
mnemosyne_handoff_receive:
  package_present: true
  package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-HANDOFF-001
  package_status: non_execution_source_transfer_artifact
  receiver_guidance_load:
    project_guidance: not_applicable
    mnemosyne_guidance: required
    refresh_completed: pending
  execution_source: current/human-approved-spec.md
  verified_master_sha:
  evidence_paths_checked: []
  evidence_paths_missing_or_unchecked: []
  current_task_from_package: PREPARE_READ_ONLY_VALIDATION_PACKAGE
  validation_selected: false
  validation_executed: false
  Meta_Agent_route_imported: false
  non_FABLE_health_review_route_imported: false
  repository_write_performed: false
  forbidden_actions: []
  safe_next_action: wait_for_separate_guidance_refresh_and_continuation_instruction
  limitations_or_unknowns: []
  status: RECEIVED_AWAITING_GUIDANCE_REFRESH | INPUT_OR_STATE_CONFLICT
```

## 13. Hard prohibitions

The receiver must not:

- treat this package as execution source;
- start V0, V1, V2 or V3 validation during receive;
- generate results for unexecuted cells;
- use real user conversations, private material or sensitive target data as fixtures;
- modify `current/human-approved-spec.md`;
- modify Meta-Agent target truth or any other target-project truth;
- take over the non-FABLE health-review route;
- execute more same-topic Pro Deep Research or Fable research by default;
- infer exact backend identity from picker labels, latency, style or self-report;
- assume that a next-tier model is adequate merely because a task is labelled bounded;
- create a second active PR for the same task.

## 14. Safe next action after receive and guidance refresh

```yaml
safe_next_action:
  action: PREPARE_READ_ONLY_VALIDATION_PACKAGE
  actor: fresh_Pro_or_equivalent_frontier_Mnemosyne_conversation
  prerequisites:
    - successful_handoff_receive
    - separate_Load_Mnemosyne_guidance_operation
    - received_task_preserved_after_refresh
    - latest_master_and_open_PR_preflight
  repository_write: yes_via_one_new_task_branch_and_at_most_one_PR
  validation_execution: false
  additional_Deep_Research: not_needed
  parallel_frontier_research: not_needed
  stop_conditions:
    - source_or_authority_conflict
    - concurrent_overlapping_PR
    - package_scope_requires_real_user_data
    - execution_isolation_is_accidentally_assumed_in_design
    - proposal_would_modify_Meta_Agent_or_another_target_truth
```

## 15. Source-conversation retirement condition

After the canonical MNEMOSYNE-180 handoff PR merges, the source conversation has no remaining substantive task in this route. No post-merge status-only PR is required. The new conversation becomes the route owner after it successfully receives this package and separately refreshes Mnemosyne guidance.
