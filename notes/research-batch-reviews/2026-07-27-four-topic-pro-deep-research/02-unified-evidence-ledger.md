# Four-Topic Pro Deep Research — Unified Evidence Ledger

> Non-execution-source evidence index. It records what the accepted reports can and cannot support. It does not adopt a design, close a TODO, modify `current/human-approved-spec.md`, or authorize implementation.

```yaml
ledger_id: MNEMOSYNE-PRO-DR-FOUR-TOPIC-EVIDENCE-LEDGER-001
task_id: MNEMOSYNE-165
created_at: 2026-07-27
maintainer_review: notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/01-maintainer-reliability-review.md
execution_source: current/human-approved-spec.md
execution_source_modified: false
```

## 1. Accepted report inventory

| ID | Topic | Maintainer disposition | Portable-source state | Current authority |
|---|---|---|---|---|
| `PRO-DR-HO-GUIDANCE-001` | Target-project conversations and additional Mnemosyne guidance | `PASS_WITH_REPAIRS` | identifiers present; literal direct URLs incomplete | non-execution-source evidence only |
| `PRO-DR-LEARNER-COGNITIVE-COACHING-001` | Learner state, mastery evidence, problem-solving strategy and cognitive coaching | `ACCEPT_WITH_CORRECTIONS` | identifiers present; literal direct URLs incomplete | non-execution-source evidence only |
| `PRO-DR-CROSS-AGENT-SHARED-MEMORY-001` | Governed reuse of learner/user/environment/domain memory | `ACCEPT_WITH_CORRECTIONS` | portable direct links substantially present | non-execution-source evidence only |
| `PRO-DR-TARGET-MEMORY-MIGRATION-001` | Versioned, reversible evolution of target-Agent memory systems | `ACCEPT_WITH_CORRECTIONS` | portable direct links substantially present | non-execution-source evidence only |

Exact artifact identities and archive reconstruction instructions are recorded by the MNEMOSYNE-165 archive manifest on the canonical branch. Raw report bytes remain preserved separately from this derived ledger.

## 2. Claim ledger

### E-01 — Project-local authority must remain primary

```yaml
claim: Target-project execution truth and owner rules must remain distinct from Mnemosyne maintenance guidance, raw evidence, research reports and derived views.
support:
  HO_GUIDANCE: direct_design_and_platform_evidence_plus_maintainer_inference
  SHARED_MEMORY: authority_and_projection_evidence
  MIGRATION: control_plane_vs_runtime_truth_boundary
  LEARNER: evidence_inference_decision_separation
confidence: high_as_a_governance_candidate
status: accepted_candidate_not_execution_source
```

### E-02 — Full Mnemosyne guidance is not a universal business-conversation default

```yaml
claim: A target-project conversation should not automatically import complete Mnemosyne maintenance guidance merely because Mnemosyne designed the project memory system.
support:
  HO_GUIDANCE: strongest_direct_topic_support
  SHARED_MEMORY: least_disclosure_and_purpose_limitation
  MIGRATION: avoid_second_runtime_truth_source
limitations:
  - no_public_direct_A_B_C_experiment
  - surface_specific_behavior_varies
status: experiment_and_user_decision_required
```

### E-03 — Learner mastery requires evidence beyond conversational fluency

```yaml
claim: Dialogue fluency, terminology and self-report alone are insufficient evidence of robust mastery.
support:
  LEARNER: educational_measurement_knowledge_tracing_transfer_and_retention_evidence
candidate_evidence_hierarchy:
  - explanation_and_error_diagnosis
  - independent_familiar_tasks
  - artifacts_with_provenance
  - unfamiliar_transfer
  - delayed_retest
  - repeated_cross_context_performance
limitations:
  - hierarchy_is_engineering_default_not_universal_psychometric_law
status: accepted_candidate_principle
```

### E-04 — Learner state should be scoped, multidimensional and uncertain

```yaml
claim: A useful learner state should be domain-, task- and time-scoped, multidimensional, provenance-linked and able to represent insufficient or contradictory evidence.
support:
  LEARNER: direct_topic_synthesis
  SHARED_MEMORY: temporal_validity_and_scope
  MIGRATION: versioned_derived_state
status: accepted_candidate_principle
prohibited_inference:
  - stable_global_learning_style
  - personality_or_clinical_label
  - intelligence_or_moral_character
```

### E-05 — Observation, hypothesis, confirmation and decision are separate objects

```yaml
claim: Observed behavior, model hypotheses, user/teacher confirmation and intervention decisions must remain separate and auditable.
support:
  LEARNER: direct_topic_support
  SHARED_MEMORY: provenance_and_owner_control
  MIGRATION: preserve_authority_and_rebuild_projections
status: accepted_candidate_principle
```

### E-06 — Personalized coaching requires transparency and reversibility

```yaml
claim: Adaptive coaching should expose its purpose, supporting evidence, uncertainty, alternatives, burden, consent, success criteria and stop/rollback controls.
support:
  LEARNER: direct_topic_synthesis_and_governance_sources
  SHARED_MEMORY: purpose_limitation_and_least_disclosure
confidence: moderate_to_high
status: candidate_for_low_stakes_pilot_only
not_authorized:
  - covert_persuasion
  - psychological_diagnosis
  - high_stakes_automated_adjudication
```

### E-07 — Cross-Agent reuse should use governed projections, not unrestricted global profiles

```yaml
claim: Cross-Agent reuse should default to purpose-bound least-disclosure projections over authoritative scoped records rather than universal replication of a full user profile.
support:
  SHARED_MEMORY: strongest_direct_topic_support
  HO_GUIDANCE: context_and_authority_minimization
  LEARNER: sensitivity_and_scope_of_learner_evidence
limitations:
  - direct_evidence_is_recent_and_bounded
  - architecture_layers_remain_candidate
status: accepted_architecture_candidate
```

### E-08 — Promotion from local to shared scope must be deliberate

```yaml
claim: Project- or Agent-local facts should not become shared canonical memory without provenance, owner authority, consent, scope, freshness and conflict review.
support:
  SHARED_MEMORY: direct_topic_support
  MIGRATION: authority_preserving_change
  LEARNER: contestability_and_context_limits
status: accepted_candidate_rule_for_future_design_review
```

### E-09 — Missing or stale shared memory must fail safely

```yaml
claim: When shared memory is unavailable, stale, unauthorized or contradicted, Agents should narrow scope, revalidate, use non-personalized behavior or escalate rather than fabricate continuity.
support:
  SHARED_MEMORY: direct_topic_support
  MIGRATION: stale_state_and_cutover_validation
  HO_GUIDANCE: task_local_unknown_requires_decision_pattern
status: accepted_candidate_principle
```

### E-10 — Early target memory systems need an upgrade contract

```yaml
claim: The first target-project memory system should include stable identities, source references, versions, migration mappings, validation, rollback and preserved raw/approved authority boundaries.
support:
  MIGRATION: strongest_direct_topic_support
  SHARED_MEMORY: temporal_and_authority_change
  LEARNER: rebuildable_derived_state
status: accepted_candidate_for_target_project_intake_and_design
```

### E-11 — Derived artifacts should be rebuildable where practical

```yaml
claim: Summaries, embeddings, indexes and model-generated projections should be reproducible from preserved authoritative evidence and versioned transformation context where practical.
support:
  MIGRATION: direct_topic_support
  LEARNER: evidence_ledger_vs_projection
  SHARED_MEMORY: provenance_and_poisoning_recovery
status: accepted_candidate_principle
limitations:
  - full_event_sourcing_is_not_universally_required
```

### E-12 — Event sourcing and dual-write are conditional mechanisms

```yaml
claim: Append-only history is broadly useful, but full event-sourced runtime, dual-write, shadow and bitemporal mechanisms should depend on lifecycle, audit, migration risk and system size.
support:
  MIGRATION: direct_topic_synthesis_plus_official_engineering_analogy
status: maintainer_correction_to_overgeneralization
```

### E-13 — Research findings require target-specific validation

```yaml
claim: The reports support candidates, threat models and experiments; they do not prove universal best practices or authorize deployment.
support:
  all_four_reports: explicit_limitations
  maintainer_review: cross_report_calibration
status: binding_evidence_role_boundary_for_this_batch
```

## 3. Evidence maturity classification

```yaml
maturity_classes:
  official_product_or_engineering_documentation:
    use: current_product_facts_and_engineering_patterns
    limitation: may_be_surface_specific_or_analogical
  peer_reviewed_research:
    use: stronger_direct_or_adjacent_evidence
    limitation: population_domain_and_task_transfer_still_require_review
  empirical_preprint:
    use: emerging_failure_modes_and_candidate_mechanisms
    limitation: replication_and_production_validity_uncertain
  conceptual_framework:
    use: design_hypotheses_and_taxonomies
    limitation: not_causal_validation
  bounded_simulation_or_benchmark:
    use: comparative_and_stress_test_evidence
    limitation: not_real_sensitive_multi_user_or_long_term_deployment
  maintainer_inference:
    use: connects_evidence_to_Mnemosyne_decision_context
    limitation: requires_user_adjudication_before_adoption
```

## 4. Conflicts and non-conflicts

```yaml
resolved_by_scope:
  - event_sourcing_is_useful_but_not_universal
  - trimmed_guidance_is_candidate_default_not_global_policy
  - shared_memory_layers_are_candidate_not_fixed_schema
  - learner_evidence_hierarchy_is_default_not_universal_measurement_law
unresolved:
  - exact_HO_GUIDANCE_global_or_task_local_policy
  - which_learner_state_fields_are_safe_for_cross_Agent_reuse
  - minimum_target_project_upgrade_contract
  - whether_and_how_to_operationalize_adaptive_explanation
  - GPT_Live_product_specific_configuration_and_validation
  - acceptable_automation_and_human_review_boundary
not_a_conflict:
  - preserving_raw_evidence_and_using_rebuildable_derived_views
  - target_project_runtime_truth_remaining_separate_from_Mnemosyne_archive
  - user_decision_remaining_authoritative
```

## 5. Invalid conclusions prohibited by this ledger

- “The four reports prove the proposed architectures are optimal.”
- “A learner's stable thinking style can be inferred from ordinary dialogue.”
- “The user has approved a global cognitive profile or cross-Agent sharing.”
- “Every target project must use event sourcing, dual-write or six memory layers.”
- “Every target-project conversation must load trimmed or complete Mnemosyne guidance.”
- “The reports authorize updates to `current/human-approved-spec.md`.”
- “The reports authorize target workspace creation, material ingestion, runtime installation or automatic migration.”
- “The visible Pro selection or report quality proves the exact served backend.”

## 6. Ledger status

```yaml
ledger_status:
  evidence_received: complete_4_of_4
  reliability_reviewed: true
  correction_boundaries_recorded: true
  ready_for_user_decision_preparation: true
  ready_for_automatic_policy_adoption: false
  ready_for_implementation: false
```
