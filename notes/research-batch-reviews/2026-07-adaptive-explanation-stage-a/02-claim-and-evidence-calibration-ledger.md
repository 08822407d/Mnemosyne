# Adaptive Explanation Stage A — Claim and Evidence Calibration Ledger

> Non-execution-source calibration record. It preserves the distinction between direct evidence, adjacent evidence and maintainer synthesis. It does not turn the report into an approved teaching policy or experiment.

```yaml
ledger_id: ADAPTIVE-EXPLANATION-STAGE-A-CLAIM-EVIDENCE-LEDGER-001
created_by_task: MNEMOSYNE-175
research_id: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001
source_report: raw/research-reports/cycles/2026Q3-adaptive-explanation-stage-a/PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001-report.md
maintainer_review: notes/research-batch-reviews/2026-07-adaptive-explanation-stage-a/01-maintainer-reliability-review.md
status: accepted_with_corrections_non_execution_source
```

## Calibration scale

```yaml
support_class:
  - direct_empirical
  - adjacent_empirical
  - systematic_review_or_meta_analysis
  - validated_measurement_or_standard
  - conceptual_framework
  - official_guidance
  - engineering_inference
maturity:
  - replicated_peer_reviewed
  - peer_reviewed_bounded
  - preprint_or_unreplicated
  - qualitative_or_small_sample
  - conceptual_only
confidence:
  - low
  - moderate
  - moderate_to_high
  - high
```

## Claim ledger

### AE-CLAIM-001 — Generic “explain simply” is not an operational policy

```yaml
claim: A broad instruction to explain simply to a learner with weak foundations does not specify which prerequisite, failure hypothesis, representation, probe, step size or outcome should guide the next action.
support_class:
  - systematic_review_or_meta_analysis
  - conceptual_framework
  - engineering_inference
maturity: peer_reviewed_bounded
population_and_domain: broad_education_and_mathematics_formative_assessment
direct_or_analogical: partly_direct_problem_framing_plus_engineering_synthesis
contradictory_or_null_evidence: no_direct_head_to_head_test_of_the_exact_prompt_found
confidence: moderate_to_high
maintainer_disposition: accept_as_problem_definition_not_as_proven_intervention_effect
```

### AE-CLAIM-002 — Local evidence should outrank a global learner label

```yaml
claim: Teaching decisions should rely on evidence scoped to the current concept and task rather than a persistent global weak_or_strong learner label.
support_class:
  - official_guidance
  - validated_measurement_or_standard
  - conceptual_framework
  - engineering_inference
maturity: peer_reviewed_bounded
population_and_domain: formative_assessment_diagnostic_measurement_open_learner_models
direct_or_analogical: direct_for_local_evidence_principle_indirect_for_the_full_policy
contradictory_or_null_evidence: global_prior_knowledge_can_predict_performance_but_is_too_coarse_for_local_action
confidence: moderate_to_high
maintainer_disposition: accept_with_scope_recency_assistance_and_uncertainty_requirements
```

### AE-CLAIM-003 — Broad self-description is only a weak prior

```yaml
claim: A statement such as my_foundations_are_weak should encourage caution but should not be treated as proof that a specific prerequisite is absent.
support_class:
  - validated_measurement_or_standard
  - engineering_inference
maturity: peer_reviewed_bounded
population_and_domain: mathematics_concept_inventories_and_predictive_validity
direct_or_analogical: analogical_inference
contradictory_or_null_evidence: direct_self_report_vs_local_measure_comparison_not_established_by_the_cited_inventory_sources
confidence: moderate
maintainer_disposition: accept_as_conservative_default_not_as_directly_proven_claim
```

### AE-CLAIM-004 — Keep five objects separate

```yaml
claim: Learner-state evidence, local explanation context, explanation action, outcome evidence and presentation preference should remain distinct.
support_class:
  - conceptual_framework
  - engineering_inference
  - adjacent_empirical
maturity: conceptual_only_for_the_integrated_object_model
population_and_domain: tutoring_learner_models_and_human_AI_interaction
direct_or_analogical: integrated_engineering_synthesis
contradictory_or_null_evidence: no_direct_test_of_this_exact_five_object_decomposition
confidence: moderate_to_high
maintainer_disposition: accept_as_candidate_design_and_experiment_analysis_boundary
```

### AE-CLAIM-005 — Multiple local failure hypotheses are preferable to one diagnosis

```yaml
claim: A tutor should maintain a small contestable set of local failure hypotheses and permit unknown rather than choosing one diagnosis from sparse dialogue.
support_class:
  - conceptual_framework
  - adjacent_empirical
  - engineering_inference
maturity: peer_reviewed_bounded_components_integrated_policy_unreplicated
population_and_domain: formative_assessment_open_learner_models_diagnostic_teaching
 direct_or_analogical: component_evidence_plus_synthesis
contradictory_or_null_evidence: exact_dialogue_only_diagnostic_accuracy_unknown
confidence: moderate
maintainer_disposition: accept_for_controlled_testing_not_operational_assumption
```

### AE-CLAIM-006 — Ordinary dialogue has limited diagnostic identifiability

```yaml
claim: Dialogue may generate plausible hypotheses about prerequisite absence, retrieval failure, relation gaps, notation barriers, misconceptions, task misunderstanding and tutor defects, but many distinctions require isolating tasks, transfer probes, artifacts or human confirmation.
support_class:
  - adjacent_empirical
  - validated_measurement_or_standard
  - engineering_inference
maturity: peer_reviewed_bounded
population_and_domain: educational_measurement_tutoring_dialogue_and_mathematics_diagnostics
direct_or_analogical: mixed
contradictory_or_null_evidence: category_specific_dialogue_validity_is_incomplete
confidence: moderate
maintainer_disposition: accept_with_unknown_and_stronger_evidence_rules
```

### AE-CLAIM-007 — No universal prerequisite graph or mastery threshold

```yaml
claim: Prerequisite structure and required mastery depend on target concept, representation and explanation route; multiple routes and alternative strategies must be representable.
support_class:
  - validated_measurement_or_standard
  - conceptual_framework
  - engineering_inference
maturity: peer_reviewed_bounded
population_and_domain: knowledge_space_Q_matrix_learning_progression_and_concept_inventory_research
direct_or_analogical: direct_for_model_limits_engineering_synthesis_for_route_policy
contradictory_or_null_evidence: structured_domains_can_support_stable_local_maps_but_not_universal_open_domain_graphs
confidence: moderate_to_high
maintainer_disposition: accept
```

### AE-CLAIM-008 — Proposed hybrid local prerequisite record

```yaml
claim: A small auditable hybrid record can represent alternative routes, route-specific required level, local evidence state, assistance provenance, recency and recheck triggers.
support_class:
  - engineering_inference
maturity: conceptual_only
population_and_domain: proposed_Stage_B_analysis_structure
direct_or_analogical: analogical_from_measurement_models
contradictory_or_null_evidence: not_yet_implemented_or_validated
confidence: moderate
maintainer_disposition: candidate_only_for_Stage_B_design
```

### AE-CLAIM-009 — Diagnostic probes should be selected by information value and burden

```yaml
claim: A tutor should ask a diagnostic question when competing hypotheses would materially change the explanation and the expected information gain justifies interruption cost.
support_class:
  - systematic_review_or_meta_analysis
  - adjacent_empirical
  - engineering_inference
maturity: peer_reviewed_bounded_components
population_and_domain: formative_assessment_self_explanation_retrieval_transfer_and_teach_back
direct_or_analogical: integrated_engineering_rule
contradictory_or_null_evidence: no_validated_universal_information_burden_threshold
confidence: moderate
maintainer_disposition: accept_for_controlled_testing
```

### AE-CLAIM-010 — Representation and guidance must be contextual

```yaml
claim: Examples, visual or symbolic representations and guidance levels should be selected based on task and evidence, not a fixed visual_verbal_intuitive_formal learner style.
support_class:
  - systematic_review_or_meta_analysis
  - adjacent_empirical
maturity: replicated_peer_reviewed_for_rejecting_fixed_universal_support
population_and_domain: STEM_representation_and_expertise_reversal
direct_or_analogical: direct_for_context_dependence_not_for_one_selection_algorithm
heterogeneity: substantial_in_multiple_representation_evidence
confidence: high_for_rejecting_fixed_style_moderate_for_action_rules
maintainer_disposition: accept_with_contextual_action_boundary
```

### AE-CLAIM-011 — Explanation-failure recovery must include tutor error

```yaml
claim: After an explanation fails, the tutor should locate the earliest break, audit its own explanation, maintain competing hypotheses, change a meaningful dimension, use a minimal check and preserve unknown when needed.
support_class:
  - adjacent_empirical
  - systematic_review_or_meta_analysis
  - engineering_inference
maturity: peer_reviewed_bounded_components_integrated_loop_unreplicated
population_and_domain: feedback_conceptual_change_refutation_self_explanation_error_learning
direct_or_analogical: integrated_engineering_synthesis
contradictory_or_null_evidence: refutation_or_repair_can_be_burdensome_or_harmful_when_the_diagnosis_is_wrong
confidence: moderate
maintainer_disposition: accept_as_C3_candidate_not_production_policy
```

### AE-CLAIM-012 — Accessible explanation must preserve the path to rigor

```yaml
claim: Progressive formalization, explicit analogy limits and local bridges are preferable to false simplifications that later require unlearning.
support_class:
  - conceptual_framework
  - adjacent_empirical
  - engineering_inference
maturity: peer_reviewed_bounded_components
population_and_domain: mathematics_STEM_cognitive_load_and_conceptual_change
direct_or_analogical: mixed
confidence: moderate_to_high
maintainer_disposition: accept_as_design_constraint
```

### AE-CLAIM-013 — Assisted performance is not learning

```yaml
claim: Conversational fluency, satisfaction, correct repetition and tutor-assisted accuracy are insufficient; independent performance, transfer and delayed retention are required.
support_class:
  - direct_empirical
  - systematic_review_or_meta_analysis
  - conceptual_framework
maturity: replicated_peer_reviewed
population_and_domain: learning_science_AI_tutoring_and_transfer
direct_or_analogical: direct_for_measurement_principle
contradictory_or_null_evidence: none_that_justifies_using_satisfaction_alone
confidence: high
maintainer_disposition: accept_as_Stage_B_measurement_requirement
```

### AE-CLAIM-014 — AI tutoring effects are design-dependent

```yaml
claim: Structured and guarded AI tutoring can improve learning in bounded contexts, while unrestricted assistance can improve practice performance without improving and sometimes harming independent learning.
support_class:
  - direct_empirical
maturity: peer_reviewed_bounded
population_and_domain: bounded_mathematics_physics_and_school_settings
direct_or_analogical: close_but_not_identical_to_university_foundational_math_Stage_B
contradictory_or_null_evidence: results_differ_by_guardrails_task_and_outcome
confidence: moderate_to_high
maintainer_disposition: accept_with_domain_and_implementation_limits
```

### AE-CLAIM-015 — C0 to C3 are defensible comparison conditions

```yaml
claim: Generic simple, fixed representation, adaptive local diagnosis and adaptive plus recovery conditions can test whether added adaptation and recovery improve outcomes beyond simpler policies.
support_class:
  - engineering_inference
  - adjacent_empirical
maturity: conceptual_only_as_one_experiment_set
population_and_domain: proposed_foundational_university_mathematics_text_pilot
direct_or_analogical: engineering_synthesis
contradictory_or_null_evidence: exact_condition_prompts_and_adherence_not_yet_tested
confidence: moderate
maintainer_disposition: accept_for_Stage_B_decision_preparation_only
```

### AE-CLAIM-016 — Two-week stratified between-subject MVP

```yaml
claim: A two-week stratified between-subject pilot across three microtopics is a feasible minimum real-participant design.
support_class:
  - engineering_inference
maturity: conceptual_only
population_and_domain: proposed_pilot
direct_or_analogical: not_empirically_established_as_optimal
contradictory_or_null_evidence: feasibility_cost_attrition_and_precision_unknown
confidence: low_to_moderate
maintainer_disposition: preserve_as_candidate_not_approved_protocol
```

### AE-CLAIM-017 — Synthetic/public pre-pilot is justified

```yaml
claim: Scripted learner trajectories, adversarial traces and expert review can test policy adherence, failure handling, misdiagnosis and measurement mechanics before real participant data.
support_class:
  - engineering_inference
  - official_guidance
maturity: conceptual_only_for_this_route
population_and_domain: protocol_and_safety_preflight
direct_or_analogical: engineering_synthesis
contradictory_or_null_evidence: cannot_establish_learning_effectiveness_or_real_user_burden
confidence: moderate_to_high
maintainer_disposition: recommended_first_Stage_B_decision_candidate
```

### AE-CLAIM-018 — Persistence remains deferred

```yaml
claim: Stage A evidence may inform fields of a future scoped evidence object but does not justify persistent or cross-Agent learner memory.
support_class:
  - conceptual_framework
  - official_guidance
  - engineering_inference
maturity: peer_reviewed_bounded_plus_governance_inference
population_and_domain: open_learner_models_privacy_and_Mnemosyne_authority_rules
direct_or_analogical: direct_for_contestability_indirect_for_persistence_policy
confidence: moderate_to_high
maintainer_disposition: accept_and_keep_persistence_out_of_Stage_B
```

## Ledger conclusion

```yaml
ledger_conclusion:
  findings_suitable_for_Stage_B_decision_basis:
    - AE_CLAIM_001
    - AE_CLAIM_002
    - AE_CLAIM_005
    - AE_CLAIM_006
    - AE_CLAIM_007
    - AE_CLAIM_009
    - AE_CLAIM_010
    - AE_CLAIM_011
    - AE_CLAIM_013
    - AE_CLAIM_014
    - AE_CLAIM_015
    - AE_CLAIM_017
  candidate_only_not_validated:
    - AE_CLAIM_004
    - AE_CLAIM_008
    - AE_CLAIM_016
  retained_boundaries:
    - AE_CLAIM_018
  execution_source_effect: none
  teaching_policy_approved: false
  Stage_B_experiment_approved: false
```
