# Model-Capability-Aware Work Planning — Open Question

> Non-execution-source live record. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
open_question_id: MODEL-CAPABILITY-PLANNING-001
created_by_task: MNEMOSYNE-163
last_status_task: MNEMOSYNE-179
status: primary_and_adversarial_research_complete_interim_rules_adjudicated_controlled_validation_open
active_general_guard: current/user-operation-next-step-capability-and-intent-guard.md
clarification_adjudication_guard: current/frontier-planning-clarification-handoff-adjudication-guard.md
research_status: current/frontier-planning-clarification-handoff-research-status.md
validation_design: notes/validation-designs/frontier-planning-clarification-handoff-read-only-validation-v0.1.md
execution_source: current/human-approved-spec.md
controlled_validation_completed: false
automatic_model_or_research_routing_authorized: false
```

## 1. Preserved user constraint

Mnemosyne and target-Agent designs must not assume that the user always runs the strongest available model. Work should be decomposed into:

```yaml
decomposition:
  frontier_reasoning:
    - ambiguous_problem_reconstruction
    - novel_or_high_impact_architecture
    - authority_privacy_trust_and_irreversibility
    - conflicting_evidence_and_final_adjudication
  next_tier_candidate:
    - frozen_bounded_execution
    - contextualized_low_or_moderate_impact_clarification
    - exact_template_population
  mechanical:
    - paths_IDs_hashes_schema_and_exact_comparisons
  human_decision:
    - owner_goal_priority_authority_quota_and_acceptance
```

Every meaningful `## 下一步` must state whether Pro/frontier capability is required, recommended or unnecessary, and must separately assess Deep Research and independent frontier-review value.

## 2. Research phase completed

```yaml
research_cycle: RC-2026Q3-frontier-planning-clarification-handoff
Pro_report:
  state: complete_reviewed
  role: multidisciplinary_evidence_and_validation_design
Fable_report:
  state: complete_reviewed
  role: independent_adversarial_and_alternative_architecture
additional_same_topic_research: not_recommended
```

The two reports converge that there is no direct public validation of the integrated frontier-planner → next-tier-interviewer workflow. The remaining gap is controlled same-input validation, not another broad literature review.

## 3. Interim capability estimates

```yaml
frontier_problem_reconstruction:
  capability_class: FRONTIER_RECOMMENDED_or_REQUIRED

structured_owner_package_generation:
  capability_class: FRONTIER_RECOMMENDED_for_design_then_NEXT_TIER_SUFFICIENT_CANDIDATE_for_frozen_population

next_tier_interactive_clarification:
  capability_class: NEXT_TIER_SUFFICIENT_CANDIDATE
  only_if:
    - low_or_moderate_impact
    - frozen_self_contained_packet
    - visible_answer_ledger
    - semantic_escalation_and_frontier_reentry
  validation_status: unproven

final_high_impact_adjudication:
  capability_class: FRONTIER_RECOMMENDED_or_REQUIRED

mechanical_validation:
  capability_class: MECHANICAL_ONLY
```

These are capability estimates, not a provider/model routing table or proof of adequacy.

## 4. Research-trigger rule

Deep Research is considered only when an external evidence gap can change a downstream decision and ordinary verification is insufficient.

```yaml
Deep_Research_gate:
  required:
    - external_researchable_unknown
    - decision_changes_across_plausible_answers
    - upstream_scope_frozen
    - expected_value_exceeds_cost_and_delay
  human_retains:
    - execution_trigger
    - quota_or_cost_authorization
    - provider_or_surface_choice
  task_generation:
    - may_be_automatic_when_gate_passes
    - must_name_decision_and_stop_condition
```

Independent frontier research is used selectively for framing-independent reconstruction, adversarial challenge, source replication, or high-impact heterogeneous review. Agreement alone is not the value measure.

## 5. Product-surface dimension

Reasoning strength does not substitute for:

- context isolation;
- file and tool access;
- exact input/output identity;
- reviewer separation;
- auditability;
- stable transfer and persistence.

A bounded task may remain impossible on a surface that lacks required controls, as demonstrated by the Stage B0 `CONTEXT_ISOLATION_FAILURE`.

## 6. Clarification routing

```yaml
DIRECT_FRONTIER:
  high_impact_or_low_clarity: true

STRUCTURED_OWNER_PACKAGE:
  bounded_direct_owner_decisions: true

NEXT_TIER_INTERVIEWER:
  candidate_for_low_or_moderate_impact_frozen_questions: true
  default_for_all_clarification: false

GATED_MIXED_ESCALATION:
  preferred_validation_candidate_for_mixed_impact: true
  validated_default: false

RESEARCH_FIRST:
  decision_relevant_external_fact_gap_only: true
```

## 7. Remaining open questions

- Can a next-tier interviewer preserve intent and fixed decisions across realistic multi-step clarification?
- Does interaction outperform a structured non-conversational package after review and rework cost?
- What packet fields are necessary rather than bureaucratic?
- What product-surface evidence is enough to rely on ledgers, context isolation and reviewer separation?
- What error and burden levels justify a durable target-Agent routing rule?
- How much frontier quota is actually saved after validation and adjudication?

## 8. Safe next action

```yaml
safe_next_action:
  current: review_and_merge_MNEMOSYNE_179
  after_merge: decide_whether_to_prepare_but_not_execute_the_read_only_validation_package
  Pro_required_for_merge_or_mechanical_verification: false
  Pro_recommended_for_validation_design_finalization_and_post_run_adjudication: true
  additional_Deep_Research: NOT_NEEDED
  additional_parallel_frontier_research: NOT_NEEDED
```

## 9. Boundaries

- This record is not execution source.
- It does not establish automatic routing, model superiority or backend identity.
- It does not prove next-tier adequacy.
- It does not authorize validation execution, quota use or target-project propagation.
