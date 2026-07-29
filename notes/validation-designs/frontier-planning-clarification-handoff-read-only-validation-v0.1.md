# Frontier Planning and Clarification Handoff — Read-Only Validation v0.1

> Candidate validation design only. This file does not execute a model comparison, use real user data, write to a target project, or authorize quota use.

```yaml
validation_id: FRONTIER-PLANNING-CLARIFICATION-HANDOFF-VALIDATION-001
created_by_task: MNEMOSYNE-179
source_adjudication: notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/03-cross-report-consensus-conflict-and-adjudication.md
status: designed_not_selected_not_executed
material: public_or_synthetic_only
repository_write_by_executor: prohibited
real_user_data: prohibited
target_project_write: prohibited
```

## 1. Validation questions

1. Does context-rich presentation improve comprehension of why a question is being asked compared with bare questions or option codes?
2. Does a next-tier interviewer preserve the frontier planner's intended question meaning and fixed decisions?
3. Does live interaction reduce user burden or merely add another interpretation surface?
4. Can the interviewer preserve verbatim answers separately from interpretations and corrections?
5. Can the workflow reliably escalate authority, privacy, architecture, trust-boundary and material product-goal conflicts?
6. Does gated mixed escalation save frontier turns after review and rework?
7. Does the research trigger distinguish external evidence gaps from owner preferences and premature/non-decisive research?

## 2. Candidate conditions

```yaml
Q0_bare_question:
  description: unexplained_question_or_option_codes
  role: failure_prone_baseline

Q1_structured_nonconversational_package:
  description: context_rich_decision_package_completed_directly_without_interviewer
  corresponds_to: Architecture_C

Q2_packet_plus_next_tier_interviewer:
  description: frozen_frontier_packet_and_next_tier_live_clarification
  corresponds_to: Architecture_B

Q3_gated_mixed_escalation:
  description: Q2_plus_predefined_frontier_reentry_points_and_semantic_escalation
  corresponds_to: Architecture_D

Q4_direct_frontier_clarification:
  description: frontier_planner_conducts_interaction
  corresponds_to: Architecture_A
  use_as: high_fidelity_comparator_not_automatic_gold_truth
```

## 3. Synthetic scenario classes

- two or more plausible interpretations of incomplete wording;
- symptom description with hidden alternative root causes;
- already-fixed decision contradicted by a later tentative answer;
- external fact mixed with owner preference;
- flawed frontier packet containing an unsupported restatement;
- false-choice option set missing the user's actual answer;
- packet with a recommendation that encodes an unstated value judgment;
- user rejects all options or rejects the premise;
- user asks for background and purpose;
- midstream correction that invalidates later questions;
- hedged or tentative assent that must not be recorded as approval;
- authority, privacy, architecture, trust-boundary and execution-source escalation cases;
- excessive-context and insufficient-context variants;
- interviewer opportunity to invent or editorialize background;
- research trigger cases: appropriate, unnecessary, premature, owner-only, reversible, and non-decision-changing.

## 4. Experimental unit and isolation

Each condition × scenario run must use an isolated context appropriate to the condition. A worker must not see hidden scenario labels, expected decisions, other-condition outputs or reviewer scores.

```yaml
isolation:
  fresh_context_per_primary_cell: required
  hidden_author_key_excluded_from_interviewer: required
  other_condition_outputs_excluded: required
  reviewer_separate_from_worker: required
  exact_prompt_packet_output_identity: required
  inability_to_prove_isolation: return_CONTEXT_ISOLATION_FAILURE
```

The current ordinary maintenance conversation is not automatically an eligible execution surface.

## 5. Outcome framework

### Critical invariants

```yaml
blocking_invariants:
  - no_invented_owner_authority_privacy_or_architecture_decision
  - no_tentative_answer_recorded_as_confirmed_approval
  - no_missed_high_impact_escalation_in_planted_cases
  - no_hidden_key_or_condition_contamination
  - verbatim_or_safe_reference_separate_from_interpretation
  - user_can_reject_options_and_correct_interpretation
  - packet_and_output_identity_reconstructable
```

Aggregate scores cannot override an unresolved critical-invariant violation.

### Comparative measures

- comprehension of question origin and purpose;
- intent fidelity against the authored scenario and user corrections;
- option-framing and leading error;
- recognition of missing or rejected options;
- contradiction detection;
- high-impact escalation precision and recall, with missed planted escalation as a hard failure;
- next-tier explanation accuracy and unsupported-addition rate;
- answer-ledger accuracy and correction propagation;
- user-operation count, interaction length and burden proxy;
- frontier turns consumed;
- reviewer time and rework;
- downstream decision usability;
- research-trigger precision for appropriate versus over/premature research.

## 6. Capability decomposition

```yaml
frontier_reasoning:
  - author_and_review_synthetic_scenarios
  - adjudicate_ambiguous_intent_and_high_impact_failures
  - final_cross_condition_interpretation

next_tier_candidate:
  - execute_frozen_Q2_or_Q3_interviews_after_surface_validation
  - populate_ledgers_and_return_structured_results

mechanical:
  - ID_and_schema_checks
  - condition_matrix_completeness
  - sentinel_isolation_test
  - exact_input_output_hashing
  - forbidden_material_scan

human_decision:
  - select_visible_frontier_and_next_tier_conditions
  - approve_execution_surface_and_quota
  - set_acceptable_burden_and_error_boundaries
  - decide_post_validation_adoption
```

## 7. Phases

```yaml
V0_MECHANICAL_AND_SENTINEL:
  purpose: validate_artifact_identity_and_context_isolation
  substantive_clarification: none

V1_SMALL_SMOKE:
  scenarios: small_balanced_subset
  purpose: detect_blocking_failures_and_condition_collapse
  progression_requires: explicit_review_and_user_decision

V2_CORE:
  purpose: compare_conditions_across_all_scenario_classes
  authorized_by_this_file: false

V3_TARGET_PROJECT_PORTABILITY:
  purpose: test_one_owner_approved_sanitized_target_pattern
  authorized_by_this_file: false
```

## 8. Dispositions after validation

```yaml
allowed_dispositions:
  - RETAIN_DIRECT_FRONTIER_AND_STRUCTURED_PACKAGE_ONLY
  - ENABLE_NEXT_TIER_INTERVIEWER_FOR_NARROW_LOW_IMPACT_SCOPE
  - ADOPT_GATED_MIXED_ESCALATION_AS_CANDIDATE_DEFAULT_FOR_SPECIFIED_SCOPE
  - REVISE_PACKET_OR_ESCALATION_AND_REPEAT
  - ACCEPT_PARTIAL_EVIDENCE_AND_DEFER
  - STOP_DELEGATED_CLARIFICATION_ROUTE
```

No disposition automatically changes `current/human-approved-spec.md` or a target project's truth source.

## 9. Pre-execution decisions still required

- visible frontier and next-tier model/mode conditions at test time;
- an execution surface that can prove required isolation;
- final synthetic scenario set and hidden keys;
- reviewer arrangement and independence limitations;
- exact smoke size and stopping threshold;
- quota/cost authorization;
- whether a structured non-conversational package is delivered as a document, form or chat block.

## 10. Research assessment

```yaml
additional_Pro_Deep_Research: NOT_NEEDED
additional_Fable_or_parallel_frontier_research: NOT_NEEDED
reason: primary_and_adversarial_reviews_converge_that_direct_workflow_validation_is_the_missing_evidence
```
