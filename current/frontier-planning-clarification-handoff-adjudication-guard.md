# Frontier Planning and Clarification Handoff — Adjudication Guard

> User-reviewed follow-up behavior guard derived from the completed Pro and Fable research cycle. This file is not a standalone execution source; `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
guard_id: MNEMOSYNE-FRONTIER-CLARIFICATION-ADJUDICATION-001
created_by_task: MNEMOSYNE-179
status: active_after_MNEMOSYNE_179_merge
source_cycle: RC-2026Q3-frontier-planning-clarification-handoff
source_adjudication: notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/03-cross-report-consensus-conflict-and-adjudication.md
execution_source_modified: false
scope_precedence: supersedes_only_clarification_architecture_and_research_trigger_interpretations_in_the_v0_2_guard
```

## 1. Preserved user requirements

Substantial Mnemosyne and target-project-design replies continue to:

- place all current user operations in the opening operation section or explicitly state no operation;
- place meaningful follow-on work in a visible closing `## 下一步` section;
- state whether frontier/Pro-class reasoning is required, recommended or unnecessary;
- separately assess Pro Deep Research and independent frontier-review value;
- give material questions enough context for the user to understand their origin, meaning, consequence and options;
- treat literal user wording as primary evidence but not automatically a complete final specification;
- preserve correction, rejection, deferral and supersession rights;
- avoid psychological, intelligence or stable cognitive-style profiling.

## 2. Risk-adaptive clarification routing

No single clarification architecture is the universal default.

```yaml
route_selection:
  DIRECT_FRONTIER:
    use_when:
      - high_impact_and_low_clarity
      - owner_authority_privacy_architecture_or_trust_boundary
      - material_problem_reconstruction
      - unresolved_conflicting_evidence_or_requirements

  STRUCTURED_OWNER_PACKAGE:
    use_when:
      - decisions_are_bounded
      - direct_owner_completion_is_practical
      - live_interviewer_is_unnecessary_unavailable_or_unvalidated
      - auditability_is_more_important_than_live_adaptation

  NEXT_TIER_INTERVIEWER:
    status: candidate_not_validated_default
    use_only_when:
      - impact_is_low_or_moderate
      - question_meaning_and_scope_are_frozen
      - package_is_self_contained
      - user_can_reject_options_and_correct_interpretations
      - visible_reconstructable_ledger_exists
      - semantic_stop_and_frontier_reentry_rules_exist

  GATED_MIXED_ESCALATION:
    status: preferred_validation_candidate_for_mixed_impact_work
    not_yet: approved_universal_default

  RESEARCH_FIRST:
    use_when:
      - external_evidence_gap_changes_the_owner_decision
      - upstream_scope_is_frozen
      - expected_information_value_justifies_cost_and_delay
```

## 3. Minimum material-question contract

A material question must include, as applicable:

- stable question ID;
- plain-language question;
- concise origin and current known state;
- decisions already fixed and not being reopened;
- the Agent interpretation marked as candidate rather than truth;
- why the answer changes downstream work;
- option meanings, tradeoffs and reversibility;
- an `other / none / reject the premise` path;
- free-form answer support;
- consequence of deferral;
- dependencies;
- semantic escalation conditions.

Do not add every field mechanically when a shorter question remains fully understandable.

## 4. Recommendation and framing rule

Recommendations may be included when they:

- are separated from verified facts and owner values;
- state assumptions and uncertainty;
- remain rejectable;
- do not preselect or default a high-impact owner decision;
- include omitted-option and reject-premise paths;
- require explicit owner confirmation where impact is high.

A blanket prohibition on all recommendations is not adopted.

## 5. Escalation rule

Escalation uses semantic decision categories and evidence, not keyword matching alone.

```yaml
mandatory_frontier_or_human_reentry:
  - new_owner_or_execution_source_claim
  - privacy_or_sensitive_material_boundary_change
  - architecture_or_product_goal_change
  - trust_or_permission_boundary_change
  - irreversible_or_high_cost_commitment
  - material_restatement_of_user_intent
  - conflict_with_fixed_decision
  - interviewer_or_packet_identity_loss
```

Deterministic indicators may supplement these categories but cannot replace contextual review.

## 6. Answer-ledger rule

The ledger must be visible or retrievable, reconstructable and correction-aware. It separates a verbatim answer or safe reference from the Agent interpretation.

Persistent external storage is conditional on:

- product-surface support;
- interaction duration;
- sensitivity and privacy;
- target owner rule;
- task-local authorization.

It is not a universal requirement for every short clarification.

## 7. Research trigger

```yaml
research_task_generation_gate:
  all_required:
    - question_is_external_and_researchable
    - plausible_answers_change_downstream_action
    - upstream_scope_is_sufficiently_frozen
    - ordinary_verification_or_current_sources_are_insufficient
    - expected_decision_value_justifies_cost_and_delay
  task_must_state:
    - decision_it_can_change
    - upstream_dependencies
    - stop_condition
    - evidence_and_source_requirements
    - return_destination
  human_retains:
    - provider_or_surface_selection
    - quota_or_cost_trigger
    - execution_authorization
```

Do not use research to avoid an owner preference or authority decision.

## 8. Capability split

```yaml
frontier_planner:
  - ambiguous_problem_reconstruction
  - option_and_dependency_design
  - research_value_judgment
  - high_impact_adjudication

next_tier_candidate:
  - bounded_interactive_clarification_from_a_frozen_packet
  - answer_capture_and_ledger_updates
  - scoped_context_explanation

mechanical:
  - required_field_and_ID_checks
  - ledger_completeness
  - deterministic_conflict_flags
  - artifact_identity
```

A next-tier label is never proof of adequacy. Failed semantic, authority, safety or identity checks require escalation or redesign.

## 9. Validation boundary

```yaml
validation_design: notes/validation-designs/frontier-planning-clarification-handoff-read-only-validation-v0.1.md
status: not_executed
additional_same_topic_Deep_Research: not_recommended
additional_Fable_research: not_recommended
```

No target-project propagation, automatic routing, or execution-source change follows from this guard without separate authority.
