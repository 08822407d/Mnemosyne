# Frontier Planning and Clarification Handoff — Cross-Report Consensus, Conflict, and Adjudication

```yaml
adjudication_id: FRONTIER-PLANNING-CLARIFICATION-HANDOFF-CROSS-REPORT-001
created_by_task: MNEMOSYNE-179
reports:
  - PRO-DR-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001
  - FABLE5-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001
adjudication_status: complete_with_validation_remaining
execution_source_modified: false
```

## 1. Shared problem reconstruction

Both reports ultimately describe the same control problem:

> Convert incomplete human wording into correct, auditable downstream decisions while preserving human authority, supporting limited memory/attention, and avoiding unnecessary frontier-model and research expenditure.

Both reject treating the user's literal wording as either irrelevant or infallibly complete. Both also reject silent replacement of the user's goal by a model-generated restatement.

## 2. Strong consensus

```yaml
consensus:
  - material_questions_need_visible_background_meaning_and_downstream_consequences
  - literal_user_evidence_must_remain_separate_from_Agent_interpretation
  - free_form_correction_and_reject_the_premise_paths_are_needed
  - owner_preferences_external_facts_design_judgments_and_missing_artifacts_need_different_routes
  - high_impact_authority_privacy_architecture_and_trust_boundary_conflicts_need_frontier_or_human_reentry
  - research_importance_is_not_the_same_as_research_value
  - research_tasks_should_name_the_decision_they_can_change_and_a_stop_condition
  - the_human_retains_quota_and_research_execution_authority
  - independent_frontier_review_should_have_a_distinct_role_and_preserve_framing_independence
  - packet_and_interviewer_components_need_controlled_validation
  - no_direct_public_study_validates_the_integrated_workflow
  - target_project_propagation_requires_owner_specific_authority
```

## 3. Material conflicts

### Conflict A — Default interaction architecture

- **Pro:** supports a frontier-planned packet plus bounded next-tier interviewer as a candidate architecture, with safeguards and staged validation.
- **Fable:** treats pure packet → next-tier delegation as the riskiest architecture and recommends a structured non-conversational package immediately, followed by gated mixed escalation after validation.

**Adjudication:** neither report establishes a universal default. Use risk-adaptive routing:

```yaml
A_direct_frontier:
  use_when:
    - high_impact
    - low_clarity
    - unresolved_authority_privacy_architecture_or_trust_boundary

C_structured_decision_package:
  use_when:
    - bounded_owner_decisions
    - user_can_review_directly
    - live_interviewer_adds_little_value_or_cannot_be_validated

B_next_tier_interviewer:
  use_when_candidate_only:
    - low_or_moderate_impact
    - high_clarity
    - frozen_self_contained_packet
    - visible_answer_ledger
    - semantic_stop_and_escalation_rules
    - easy_frontier_reentry

D_gated_mixed_escalation:
  role: preferred_validation_candidate_for_mixed_impact_routes
  status: not_validated_default

E_research_first:
  use_when:
    - external_fact_gap_changes_owner_decision
    - upstream_question_is_frozen
    - expected_information_value_justifies_cost
```

### Conflict B — Recommendations in high-impact questions

- **Pro:** allows recommendations with evidence, uncertainty and option meanings.
- **Fable:** argues recommendations should be prohibited on high-impact questions due to anchoring.

**Adjudication:** do not blanket-prohibit recommendations. Instead:

- separate facts, engineering judgment and owner values;
- present recommendation as provisional and rejectable;
- provide `other / none / reject premise`;
- do not preselect or default a high-impact option;
- explain which values and assumptions drive the recommendation;
- require explicit owner confirmation.

### Conflict C — Escalation implementation

Fable favors a hard-coded stop list; Pro emphasizes contextual escalation.

**Adjudication:** use semantic categories plus explicit examples and deterministic indicators where available. Keyword-only matching is insufficient; unconstrained model discretion is also insufficient.

### Conflict D — Ledger architecture

Fable says the ledger must be externally stored; Pro emphasizes cumulative visibility and provenance.

**Adjudication:** require the ledger to be visible, reconstructable, and identity-preserving. Persistent external storage is required only when the surface, duration, sensitivity and project authority justify it.

### Conflict E — Deep Research delivery

Both reports preserve human control. The repository task contract incorrectly required the canonical Deep Research report and a separately generated `complete-response` file as though they were two outputs.

**Adjudication:** there is one canonical substantive report. Markdown/Word/PDF exports are representations of the same report. An additional arbitrary named file is optional only when the surface explicitly supports and confirms it.

## 4. Fable runtime concern

The low visible quota consumption and 10m15s duration do not by themselves invalidate the report. The content passes task binding and architecture challenge. Its limitations are already captured by source maturity and claim calibration.

```yaml
Fable_runtime_adjudication:
  low_quota_observation: retained
  rerun_due_to_duration_alone: false
  use_as_primary_source_authority: false
  use_as_independent_adversarial_evidence: true
  require_Pro_cross_adjudication_before_policy_change: satisfied_by_MNEMOSYNE_179
```

## 5. Combined disposition

```yaml
combined_disposition:
  preserve_existing_user_requirements:
    - operation_section_first
    - next_step_section_last
    - explicit_model_capability_estimate
    - explicit_Deep_Research_and_parallel_review_assessment
    - context_for_material_user_questions
    - human_wording_not_assumed_complete
    - user_correction_and_supersession
  amend_candidate_architecture:
    - replace_single_packet_interviewer_default_with_risk_adaptive_routing
    - mark_next_tier_interviewer_as_validation_gated_candidate
    - preserve_structured_nonconversational_fallback
    - preserve_direct_frontier_for_high_impact_low_clarity
  amend_research_trigger:
    - require_decision_change_and_stop_condition
    - preserve_human_execution_and_quota_trigger
  amend_delivery_contract:
    - one_canonical_Deep_Research_report
    - standard_export_is_same_report_not_second_output
  additional_research: not_needed
  next_evidence_gate: synthetic_read_only_controlled_validation
```
