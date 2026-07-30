# Frontier Clarification Validation — Staged Fable5 Research Plan v0.1

> Non-execution-source research planning record. It distinguishes completed foundational research from new post-package audits. It does not start Fable5, spend quota, accept a report, modify the validation package or authorize V0/V1.

```yaml
plan_id: FABLE5-FRONTIER-CLARIFICATION-VALIDATION-STAGED-PLAN-001
created_by_task: MNEMOSYNE-182
version: 0.1.0
status: stage_A_tasks_prepared_not_executed_stage_B_topics_deferred
source_package: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
source_package_merge_commit: 67eb96d5317a2bb589236a4a8b2e75be2508d830
foundational_Pro_research: complete_adjudicated
foundational_Fable_research: complete_adjudicated_no_rerun
additional_foundational_same_topic_research: not_needed
post_package_independent_review: recommended
quota_execution_authority: user_only
```

## 1. Why any new Fable5 work is justified

The original research question—whether and how frontier-planned clarification, structured owner packages, next-tier interviewing and gated escalation should be designed—has already been independently researched and adjudicated. Repeating that broad question would add little value.

New artifacts now exist that did not exist during the original research:

- a complete 14-file validation package;
- frozen Q0–Q4 condition contracts;
- 14 synthetic scenarios and hidden author keys;
- a V0 sentinel taskbook and a 40-cell V1 taskbook;
- protocol-validity and condition-safety result semantics;
- an execution-surface decision package;
- a new manual-surface preparation candidate.

These create two decision-relevant objects for independent challenge:

1. whether the package would actually produce interpretable evidence rather than a well-documented but confounded result;
2. whether a manual multi-conversation surface can satisfy the package's isolation, identity, provenance and no-write requirements.

Fable5 is useful here as an independent adversarial reviewer, not as an authority and not as a substitute for controlled validation.

## 2. Stage A — recommended now

Stage A contains two independent tasks that may be run in separate fresh Fable5 research conversations. They have distinct decision value and may run in parallel because neither report is supplied to the other.

### A1 — Validation-package adversarial audit

```yaml
task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
ready_to_run_task: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
decision_it_can_change:
  - proceed_to_surface_selection_without_package_revision
  - revise_condition_contracts_scenarios_keys_rubric_or_result_semantics
  - stop_if_construct_validity_or_contamination_is_not_repairable
primary_role: independent_static_construct_validity_and_failure_mode_audit
```

The report should not redesign the whole clarification architecture unless a package defect traces to the adjudicated architecture.

### A2 — Manual-surface isolation and provenance threat model

```yaml
task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
ready_to_run_task: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
decision_it_can_change:
  - prepare_and_verify_manual_V0_preflight
  - revise_manual_candidate
  - prefer_API_or_runtime_preparation
  - defer_or_stop_surface_route
primary_role: independent_execution_surface_trust_observability_and_no_write_audit
```

This task reviews a candidate surface. It does not select or execute that surface.

## 3. Stage A independence and return order

```yaml
Stage_A_protocol:
  execute_in:
    A1: fresh_Fable_5_high_or_xhigh_research_conversation
    A2: separate_fresh_Fable_5_high_or_xhigh_research_conversation
  cross_report_visibility_before_completion: prohibited
  prior_Pro_report_supplied: false
  prior_foundational_Fable_report_supplied: false
  repository_write: prohibited
  validation_execution: prohibited
  return_to: current_Mnemosyne_frontier_clarification_validation_route
  adjudicate_before_Stage_B_task_freeze: required
```

The maintainer should compare both reports with repository sources, calibrate evidence strength and determine whether package or surface-candidate amendments are needed before any surface selection.

## 4. Stage B — four conditional topics, not ready-to-run yet

The user has enough Fable5 quota for additional runs, but these tasks should not be frozen now because Stage A findings or a later owner surface decision may materially change their inputs.

### B1 — Reviewer independence and next-tier judge reliability

```yaml
topic_id: FABLE5-FCV-REVIEWER-INDEPENDENCE-001
trigger:
  - Stage_A_finds_material_rubric_or_judge_ambiguity
  - or_owner_selects_a_surface_and_reviewer_arrangement
question: >-
  What minimum reviewer separation, mechanical support and adjudication pattern
  is sufficient for the V0/V1 evidence class, and which judgments cannot be
  delegated to a next-tier reviewer?
decision_it_can_change:
  - one_reviewer_plus_mechanical
  - two_separate_reviewers
  - heterogeneous_review
  - defer_due_to_independence_limit
ready_to_run_now: false
```

### B2 — V1 inference limits and progression thresholds

```yaml
topic_id: FABLE5-FCV-V1-INFERENCE-AND-THRESHOLDS-001
trigger:
  - package_audit_passes_or_is_revised
  - V0_surface_is_selected_and_verified
  - before_any_V1_authorization
question: >-
  What conclusions can and cannot be supported by an eight-scenario, five-
  condition, forty-cell smoke design without blanket repeats, and what hard
  failures, uncertainty bounds or progression rules should govern V1?
decision_it_can_change:
  - retain_40_cell_smoke
  - revise_scenario_balance_or_repeat_policy
  - narrow_allowed_dispositions
  - stop_before_V1
ready_to_run_now: false
```

### B3 — No-write and context-isolation evidence equivalence

```yaml
topic_id: FABLE5-FCV-EVIDENCE-EQUIVALENCE-001
trigger:
  - selected_surface_cannot_supply_default_mechanical_proof
  - a_run_scoped_exception_is_being_considered
question: >-
  Under what narrow conditions, if any, can alternative evidence support a
  bounded no-write or context-isolation claim, and what claims must remain
  BLOCKED when full observability is unavailable?
decision_it_can_change:
  - accept_specific_run_scoped_exception
  - reject_exception_and_change_surface
  - narrow_claim_scope
  - defer
ready_to_run_now: false
```

### B4 — Portability and target-project propagation

```yaml
topic_id: FABLE5-FCV-PORTABILITY-AND-PROPAGATION-001
trigger:
  - valid_V1_evidence_exists
  - a_specific_target_owner_requests_portability_review
question: >-
  Which validated clarification mechanisms are portable beyond Mnemosyne, what
  target-specific authority/privacy changes are required, and what evidence is
  insufficient for propagation?
decision_it_can_change:
  - no_propagation
  - narrow_target_specific_pilot
  - revise_before_V3
  - prepare_V3_candidate
ready_to_run_now: false
```

B4 is deliberately late. Running it before V1 would encourage theoretical propagation from unvalidated evidence.

## 5. Why six simultaneous tasks are not recommended

The six topics are not six independent opportunities. Stage A can reveal that:

- the package requires revision, changing B1 and B2;
- manual isolation is blocked, changing B1 and B3;
- no surface is acceptable, eliminating immediate value from B2;
- a selected API/runtime surface supplies better logs, reducing B3's value;
- V1 is never authorized, making B4 premature.

Therefore:

```yaml
quota_recommendation:
  execute_now_if_user_chooses: 2
  preserve_as_conditional_reserve: 4
  automatically_spend_all_available_runs: false
  next_task_generation_gate: Stage_A_reports_received_and_adjudicated
```

## 6. Evidence and report handling

For each Fable5 report:

- treat existing designs as hypotheses, not instructions to endorse;
- preserve independent framing by excluding prior Pro/Fable reports;
- use repository files as the exact object under audit;
- distinguish direct evidence, adjacent evidence, analogy and original engineering reasoning;
- record inaccessible or uncertain sources;
- state that exact served backend identity is unknown unless run-specific metadata attests it;
- return the complete report body and a clearly named complete-response copy if the Fable surface supports file creation;
- do not write GitHub or connected services.

A fluent report is not accepted automatically. The maintainer must perform input-integrity, evidence-role, source and cross-report adjudication.

## 7. Deep Research and Pro assessment

```yaml
additional_Pro_Deep_Research:
  status: NOT_NEEDED
  reason: broad_external_evidence_and_foundational_architecture_have_already_been_adjudicated

additional_Pro_frontier_static_review:
  status: OPTIONAL_AFTER_Fable_if_disposition_changing_conflict_remains

Fable5_Stage_A:
  status: RECOMMENDED
  role: independent_post_package_adversarial_review
```

## 8. Safe next action

```yaml
safe_next_action:
  - review_and_merge_the_task_files_without_running_them
  - user_may_execute_A1_and_A2_in_separate_fresh_Fable5_conversations
  - return_complete_reports_for_adjudication
  - freeze_any_Stage_B_task_only_after_Stage_A_disposition
```

No research run, report or conclusion has been generated by this plan.