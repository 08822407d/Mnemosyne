# Four-Topic Pro Deep Research — Decision Preparation

> Non-execution-source decision-preparation record. It presents bounded follow-up choices after research ingestion. It does not choose for the user, modify `current/human-approved-spec.md`, close TODOs, or authorize target-project implementation.

```yaml
decision_package_id: MNEMOSYNE-PRO-DR-FOUR-TOPIC-DECISION-PREP-001
task_id: MNEMOSYNE-165
created_at: 2026-07-27
maintainer_review: notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/01-maintainer-reliability-review.md
evidence_ledger: notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/02-unified-evidence-ledger.md
execution_source: current/human-approved-spec.md
```

## 1. What is ready now

```yaml
ready:
  - preserve_four_topic_reports_as_non_execution_source_evidence
  - preserve_maintainer_corrections_and_limitations
  - use_the_reports_to_prepare_experiments_and_candidate_designs
  - compare_the_reports_with_target_project_requirements_when_a_target_is_selected
not_ready:
  - execution_source_update
  - universal_model_or_memory_schema
  - cross_Agent_automatic_sharing
  - actual_user_cognitive_profile
  - GPT_Live_configuration
  - target_workspace_or_runtime_installation
  - automatic_migration
```

## 2. Recommended interpretation

The strongest combined interpretation is not “adopt four architectures.” It is:

1. preserve authority and evidence boundaries;
2. design target-specific projections and migrations rather than global replication;
3. make uncertainty, freshness, contestability and rollback first-class;
4. validate guidance, learner modeling and sharing with controlled experiments;
5. treat early target systems as versioned and upgradeable;
6. require a new user decision before any candidate becomes a behavior rule or implementation task.

## 3. Candidate next routes

### Route A — Four-topic evidence acceptance only

```yaml
route_id: FOUR_TOPIC_EVIDENCE_ACCEPTANCE_ONLY
scope:
  - accept_the_batch_as_non_execution_source_evidence_with_corrections
  - no_candidate_design_or_experiment_yet
benefit: lowest_risk_and_no_automatic_scope_expansion
cost: research_value_remains_unoperationalized
```

### Route B — HO-GUIDANCE controlled experiment

```yaml
route_id: HO_GUIDANCE_CONTROLLED_EXPERIMENT
objective: compare_project_only_vs_trimmed_common_constraints_vs_full_guidance_with_route_firewall
required_before_execution:
  - define_test_surfaces
  - freeze_target_project_guidance
  - freeze_acceptance_rubric
  - synthetic_or_public_inputs_only
  - no_target_write
outputs:
  - task_contamination_results
  - authority_conflict_results
  - handoff_correctness
  - context_cost
  - user_burden
not_authorized_by_this_record: true
```

This route is the most direct way to resolve `HO-GUIDANCE-001`, but it should not be treated as a prerequisite for every other target-project design activity.

### Route C — Learner-state and adaptive-explanation research synthesis

```yaml
route_id: LEARNER_STATE_AND_ADAPTIVE_EXPLANATION_SYNTHESIS
objective:
  - reanalyse_RAW_0059_with_the_accepted_learner_report
  - define_research_questions_for_local_prerequisite_diagnosis_and_explanation_entry_point
  - preserve_the_separate_GPT_Live_product_specific_question
required_process:
  - fresh_high_reasoning_Pro_or_equivalent_reanalysis
  - similarity_check_against_existing_learner_and_metacognitive_TODOs
  - current_GPT_Live_official_fact_verification_before_product_specific_prompt_generation
  - staged_prompt_generation
not_authorized:
  - actual_user_profile
  - cognitive_diagnosis
  - Deep_Research_prompt_generation_without_reanalysis
```

This route follows the gate established by MNEMOSYNE-164 and is the natural next step for the two newly captured learning TODOs.

### Route D — Cross-Agent shared-memory candidate architecture

```yaml
route_id: CROSS_AGENT_SHARED_MEMORY_CANDIDATE
objective: derive_a_minimal_file_based_manual_promotion_and_projection_design
minimum_boundaries:
  - no_global_full_user_profile
  - project_local_truth_by_default
  - explicit_owner_and_purpose
  - least_disclosure_projection
  - freshness_and_revocation
  - no_automatic_writeback
  - safe_degradation
suitable_initial_role: design_candidate_and_threat_model
not_authorized_by_this_record: true
```

### Route E — First-target minimum upgrade contract

```yaml
route_id: FIRST_TARGET_MINIMUM_UPGRADE_CONTRACT
objective: add_candidate_versioning_migration_and_rollback_requirements_to_the_first_real_target_project_design_process
candidate_minimum:
  - stable_object_IDs
  - source_refs
  - schema_design_delivery_and_policy_versions
  - preserved_raw_and_approved_authority
  - migration_manifest
  - old_to_new_mapping
  - validation_and_acceptance_criteria
  - rollback_ref
  - rebuildable_derived_views_where_practical
conditional_not_universal:
  - event_sourced_runtime
  - dual_write
  - shadow_cutover
  - bitemporal_store
not_authorized_by_this_record: true
```

This route is most directly connected to the user's earlier goal: begin using Mnemosyne before it is perfect while avoiding lock-in and enabling later upgrades.

### Route F — Integrated target-project design pilot

```yaml
route_id: INTEGRATED_TARGET_PROJECT_DESIGN_PILOT
objective: apply_only_the_current_approved_Mnemosyne_design_plus_selected_candidate_safeguards_to_a_real_target_project
preconditions:
  - explicit_target_selection
  - complete_requirements_and_authority_map
  - privacy_and_storage_decisions
  - target_runtime_truth_source
  - approved_run_manifest
  - user_selection_of_which_research_candidates_may_be_tested
  - rollback_and_acceptance_plan
status: not_ready_without_new_user_decisions
```

## 4. Recommended sequencing

The research does not justify making all candidate routes one large implementation mainline. The recommended order is:

```yaml
recommended_sequence:
  step_1:
    action: accept_and_store_the_four_topic_evidence_with_corrections
  step_2:
    action: choose_one_near_term_decision_or_experiment_route
  step_3:
    action: generate_a_fresh_bounded_task_and_acceptance_rubric
  step_4:
    action: run_read_only_or_synthetic_validation_before_any_behavior_rule_or_target_write
  step_5:
    action: obtain_explicit_user_disposition_for_any_candidate_adoption
```

For near-term product value, the strongest candidates are:

1. `FIRST_TARGET_MINIMUM_UPGRADE_CONTRACT`, because it reduces the risk of starting a target project before Mnemosyne is mature;
2. `LEARNER_STATE_AND_ADAPTIVE_EXPLANATION_SYNTHESIS`, because MNEMOSYNE-164 already created a deliberate Pro-reanalysis gate;
3. `HO_GUIDANCE_CONTROLLED_EXPERIMENT`, because it can resolve an existing open question;
4. `CROSS_AGENT_SHARED_MEMORY_CANDIDATE`, after real target-project evidence clarifies which information genuinely needs reuse.

This ordering is a maintainer recommendation only. It does not override another conversation-owned mainline.

## 5. Decision options after this package merges

```yaml
user_disposition_options:
  ACCEPT_EVIDENCE_ONLY:
    meaning: accept_storage_and_reviews_without_starting_a_new_route
  SELECT_FIRST_TARGET_UPGRADE_CONTRACT:
    meaning: prepare_a_candidate_minimum_upgrade_contract_for_user_review
  SELECT_LEARNER_AND_ADAPTIVE_EXPLANATION_SYNTHESIS:
    meaning: run_the_fresh_Pro_reanalysis_required_by_MNEMOSYNE_164
  SELECT_HO_GUIDANCE_EXPERIMENT:
    meaning: prepare_a_read_only_or_synthetic_controlled_experiment
  SELECT_CROSS_AGENT_MEMORY_CANDIDATE:
    meaning: prepare_a_minimal_file_based_shared_memory_candidate
  DEFER_ALL_FOLLOW_UP:
    meaning: preserve_evidence_and_take_no_further_action
  CUSTOM:
    meaning: user_defines_another_bounded_route
```

No option is selected by merging the research-storage PR. Merge means only that the reports, reviews and decision preparation are preserved in the repository.

## 6. Non-interference boundary

- This package does not resume or take over the separate non-FABLE comprehensive health-review route.
- It does not resume Meta-Agent product construction.
- It does not change the model-capability-aware work-planning open question.
- It does not start GPT Live research or configure a learning Agent.
- It does not modify existing target-project or handoff routes.
- It does not close `HO-GUIDANCE-001` or any learning-related TODO.

## 7. Safe next action

```yaml
safe_next_action:
  before_merge: human_review_and_merge_the_single_MNEMOSYNE_165_PR
  after_merge:
    - verify_master_contains_the_exact_archive_reviews_ledger_and_status
    - present_the_user_disposition_options
  automatic_route_after_merge: none
```
