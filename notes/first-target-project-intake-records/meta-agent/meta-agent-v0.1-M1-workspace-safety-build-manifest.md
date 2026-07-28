# Meta-Agent v0.1 M1 — Workspace, Safety and Build-Start Manifest

> Target-specific, non-execution-source M1 manifest. It defines the exact bootstrap workspace, safe-input boundary, future M2 target-write scope, upgrade profile, verification and model-capability split. It does not create any target file in MNEMOSYNE-170.

```yaml
manifest_id: META-AGENT-V0.1-M1-BUILD-START-MANIFEST-001
created_by_task: MNEMOSYNE-170
target_project_id: meta-agent
M0_ref: notes/first-target-project-intake-records/meta-agent/meta-agent-v0.1-M0-requirements-and-authority-baseline.md
status: proposed_for_acceptance_by_merging_the_canonical_MNEMOSYNE_170_PR
effective_on_merge: true
M1_complete_on_merge: true
execution_source: current/human-approved-spec.md
execution_source_modified: false
target_write_in_MNEMOSYNE_170: false
future_M2_target_write: requires_fresh_task_local_authorization
```

## 1. Selected bootstrap workspace and repository role

```yaml
workspace_decision:
  repository: 08822407d/Mnemosyne
  repository_visibility_treatment: public_risk
  workspace_root: target-projects/meta-agent/
  workspace_role:
    - bootstrap_Meta_Agent_v0_1_target_workspace
    - initial_file_based_target_runtime_store
  sole_runtime_truth_source_file: target-projects/meta-agent/current/approved-spec.md
  entire_directory_is_truth_source: false
  Mnemosyne_root_execution_source_is_target_truth: false
  dedicated_external_repository_now: not_required
  future_external_repository_migration: allowed_only_by_approved_migration_manifest
```

This arrangement minimizes start-up friction while keeping the authority boundary explicit. The target truth source is one file, not the repository, directory, current context, handoff, methodology file or Mnemosyne execution source.

## 2. Public-repository safe-input and storage policy

```yaml
safe_input_policy:
  repository_capture_safety_preflight_required_before_any_new_original_or_target_material: true
  default_storage_route_for_user_originals: outside_git
  allowed_in_bootstrap_public_workspace:
    - public_information
    - synthetic_material
    - explicitly_redacted_excerpt_with_manifest
    - safe_external_pointer
    - high_level_user_confirmed_requirement_or_decision_that_passes_preflight
    - reviewed_non_sensitive_research_or_method_summary
  prohibited:
    - secrets
    - credentials
    - tokens_or_account_material
    - private_source_code
    - customer_or_confidential_material
    - unredacted_personal_or_sensitive_learning_records
    - raw_voice_or_chat_transcripts_without_separate_approval
    - reconstructed_lost_conversation_presented_as_fact
    - unverified_current_platform_or_model_claim_presented_as_stable_truth
  repository_original_route:
    allowed_only_after_complete_preflight: true
    default_for_Meta_Agent_private_originals: false
  redacted_excerpt_route:
    redaction_manifest_required: true
  safe_pointer_route:
    pointer_must_not_contain_secret_or_sensitive_payload: true
  outside_git_route:
    preferred_for_private_or_large_originals: true
```

M2 must use only already reviewed repository evidence and user-approved high-level target requirements. It must not request raw private materials.

## 3. Exact M2 substantive target-file scope

The first v0.1 construction task may create exactly these seven target files and no other substantive target path:

```yaml
M2_target_files:
  - path: target-projects/meta-agent/current/approved-spec.md
    role: sole_Meta_Agent_runtime_truth_source
    authority: target_execution_source
  - path: target-projects/meta-agent/current/active-context.md
    role: current_stage_completed_pending_unknowns_and_safe_next_action
    authority: non_execution_operational_state
  - path: target-projects/meta-agent/authority/source-and-owner-map.md
    role: owner_source_priority_safe_input_and_write_authority_map
    authority: user_approved_support_record_referenced_by_execution_source
  - path: target-projects/meta-agent/methodology/core-methodology.md
    role: initial_general_agent_design_methodology_with_stable_method_IDs
    authority: approved_method_library_only_as_referenced_by_execution_source
  - path: target-projects/meta-agent/cases/case-and-feedback-ledger.md
    role: empty_or_minimal_case_feedback_and_promotion_gate
    authority: evidence_and_candidate_only
  - path: target-projects/meta-agent/history/decision-version-and-migration-log.md
    role: decisions_versions_object_lineage_migrations_and_rollback
    authority: reviewed_history_and_migration_record
  - path: target-projects/meta-agent/handoff/handoff-current.md
    role: fresh_session_handoff
    authority: non_execution_navigation
```

The target file set is deliberately small. TODOs and open questions are kept inside `current/active-context.md` for v0.1 rather than creating separate files. A startup-instructions file, dedicated evaluation directory, research map, capability registry, RAG/index, database or automation files are deferred until evidence shows they are needed.

## 4. Required content by file

### `current/approved-spec.md`

Must contain:

- Meta-Agent identity, purpose and non-goals;
- owner and sole runtime truth rule;
- accepted MA-REQ IDs from M0;
- target file roles and conflict precedence;
- methodology/case/feedback promotion rules;
- safe-input and write-authorization boundary;
- compact version set;
- next-tier execution and frontier escalation rules;
- update, supersession and acceptance rules.

### `current/active-context.md`

Must contain:

- current stage and version;
- completed and pending work;
- pending requirements, unknowns and unsupported assumptions;
- current operational blockers;
- one safe next action;
- explicit statement that it is not execution source.

### `authority/source-and-owner-map.md`

Must contain:

- user owner rule;
- source priority and conflict resolution;
- exact runtime truth source ref;
- allowed/prohibited material classes;
- task-local repository action authorization rule;
- evidence, support, candidate and inference roles.

### `methodology/core-methodology.md`

Must contain only a compact initial method set with stable IDs and source refs, including at minimum:

```yaml
initial_method_objects:
  - MA-METHOD-0001: requirement_and_problem_framing
  - MA-METHOD-0002: single_Agent_vs_multi_Agent_decision
  - MA-METHOD-0003: authority_source_and_memory_role_separation
  - MA-METHOD-0004: capability_aware_work_decomposition_and_escalation
  - MA-METHOD-0005: evaluation_feedback_and_methodology_promotion_gate
  - MA-METHOD-0006: handoff_and_fresh_session_continuity
```

These methods must remain general and must not silently encode one project's case details as universal methodology.

### `cases/case-and-feedback-ledger.md`

Must begin with no fabricated real cases. It should define:

- `MA-CASE-*`, `MA-FEEDBACK-*` and lesson-candidate fields;
- target/project scope;
- source refs;
- review status;
- promotion gate;
- explicit prohibition on automatic global methodology updates.

### `history/decision-version-and-migration-log.md`

Must record:

- initial user/route decisions;
- initial version set;
- stable ID rules;
- bootstrap state and previous-state reference;
- migration mapping schema;
- rollback plan and its limitations;
- future change-class gate.

### `handoff/handoff-current.md`

Must allow a fresh session to recover:

- target identity and sole runtime truth source;
- current stage;
- accepted and pending scope;
- boundaries and prohibited actions;
- current open blockers;
- one safe next action;
- required reading order.

## 5. Standard target-specific upgrade profile

The first Meta-Agent build uses the advisory contract's `standard` profile because it is long-lived and methodology-bearing.

```yaml
upgrade_contract:
  contract_id: META-AGENT-V0.1-UPGRADE-CONTRACT-001
  source_candidate: FIRST-TARGET-MINIMUM-UPGRADE-CONTRACT-001
  profile: standard
  status_after_M2_acceptance: confirmed_for_target

  stable_identity:
    object_id_rule: prefix_plus_zero_padded_sequence
    prefixes:
      requirement: MA-REQ
      pending_requirement: MA-PEND
      decision: MA-DEC
      method: MA-METHOD
      case: MA-CASE
      feedback: MA-FEEDBACK
      evaluation: MA-EVAL
      migration: MA-MIG
    ID_reuse_prohibited: true
    rename_split_merge_retire_mapping_required: true

  version_set:
    design_version: 0.1.0
    schema_version: 0.1.0
    policy_version: 0.1.0
    delivery_version: 0.1.0
    derived_transformation_context: none_or_explicitly_recorded

  authority_and_source:
    target_execution_source_ref: target-projects/meta-agent/current/approved-spec.md
    raw_evidence_role: external_or_reviewed_evidence_not_target_truth
    approved_requirement_and_decision_role: preserved_and_explicitly_superseded_only
    current_state_role: operational_non_execution
    derived_artifact_role: rebuildable_non_authoritative
    conflict_precedence_ref: M0_baseline_and_target_approved_spec

  migration:
    manifest_required_for_Class_2_to_Class_4_changes: true
    old_to_new_mapping_required: true
    preserve_transform_recompute_retire_decisions_required: true
    compatibility_statement_required: true

  rollback:
    bootstrap_previous_state_ref: master_before_M2_with_no_target_projects_meta_agent_workspace
    initial_rollback_method: revert_or_close_unmerged_M2_lineage_before_operational_use
    Git_history_erasure_promised: false
    public_history_persistence_limitation: explicit

  derived_views:
    initial_derived_indexes_or_embeddings: none
    future_views_rebuildable_where_practical: true

  explicitly_not_required:
    - full_event_sourced_runtime
    - dual_write
    - shadow_cutover
    - bitemporal_database
    - automated_migration_service
    - vector_store_or_RAG
```

## 6. Capability-aware work split

The M2 construction task should be designed so that scarce frontier reasoning is concentrated and bounded work can be delegated safely.

```yaml
model_capability_split:
  frontier_reasoning:
    tasks:
      - change_core_product_purpose_or_non_goals
      - resolve_conflicting_or_ambiguous_requirements
      - change_owner_runtime_truth_authority_privacy_or_trust_boundary
      - create_novel_methodology_without_prior_decision_basis
      - approve_target_specific_feedback_as_general_methodology
      - adjudicate_failed_validation_or_high_impact_exception
    action: stop_and_escalate_to_user_selected_frontier_model_and_human_decision

  next_tier_execution:
    tasks:
      - create_the_seven_files_from_frozen_M0_M1_inputs
      - populate_exact_required_sections_and_IDs
      - update_bounded_current_state_and_handoff
      - apply_approved_low_risk_additive_changes
    requirements:
      - self_contained_inputs
      - exact_path_allowlist
      - explicit_forbidden_actions
      - acceptance_checks
      - stop_on_ambiguity

  mechanical_verification:
    tasks:
      - changed_path_allowlist
      - required_heading_and_front_matter_check
      - stable_ID_uniqueness_and_prefix_check
      - version_field_check
      - source_ref_and_link_check
      - forbidden_material_and_placeholder_scan
      - diff_and_final_LF_check

  human_decision:
    tasks:
      - accept_or_revise_v0_1
      - approve_any_truth_or_authority_change
      - approve_sensitive_material_use
      - approve_operational_use
```

No named provider/model is permanently bound to a tier. The exact user-visible selection is recorded at execution time, and hidden backend identity remains `unknown_or_not_attestable` without provider metadata.

## 7. Allowed M2 inputs

```yaml
allowed_inputs:
  - current/human-approved-spec.md_for_Mnemosyne_process_and_safety_only
  - this_M1_manifest
  - the_M0_requirements_and_authority_baseline
  - notes/first-target-minimum-upgrade-contract-v0.1.md
  - notes/first-target-minimum-upgrade-contract-advisory-pilot-checklist-v0.1.md
  - notes/target-project-memory-system-template-pack.md
  - reviewed_Meta_Agent_alignment_and_v0_2_records
  - accepted_controlled_no_target_write_dry_run_and_maintainer_review
  - user_instruction_selecting_META_AGENT_PRODUCT_BUILD_LAUNCH_PREPARATION
  - current_verified_repository_state

prohibited_inputs:
  - raw_private_Meta_Agent_material
  - unapproved_external_conversation_content
  - invented_reconstruction_of_lost_originals
  - target_repository_content_not_explicitly_authorized
  - stale_or_unverified_platform_facts_as_current_truth
  - failed_or_wrong_topic_research_outputs_as_substantive_evidence
```

## 8. M2 acceptance criteria

```yaml
M2_acceptance_criteria:
  exact_target_file_set: seven_of_seven_and_no_extra_substantive_target_paths
  sole_target_truth_source_explicit: true
  accepted_M0_requirement_IDs_preserved: true
  stable_IDs_unique: true
  version_set_present: true
  source_and_authority_roles_separated: true
  no_private_or_prohibited_material: true
  no_automatic_methodology_promotion: true
  handoff_recoverable_by_fresh_session: true
  active_context_has_one_safe_next_action: true
  upgrade_profile_instantiated: true
  migration_and_rollback_record_present: true
  next_tier_executor_boundaries_and_escalation_present: true
  operational_use_claimed_before_owner_acceptance: false
```

## 9. Stop conditions

M2 must stop before target write or before PR creation if:

```yaml
stop_conditions:
  - required_core_requirement_is_ambiguous_or_conflicting
  - target_truth_source_or_owner_rule_would_change
  - a_needed_path_is_outside_the_allowlist
  - sensitive_or_unapproved_material_is_required
  - private_storage_or_external_repository_is_needed_but_not_approved
  - a_current_health_review_P0_or_P1_finding_is_found_and_applies
  - exact_acceptance_or_rollback_evidence_cannot_be_produced
  - the_executor_would_need_to_invent_methodology_or_target_facts
  - concurrent_open_PR_or_equivalent_write_lineage_appears
```

## 10. Non-FABLE health-review boundary

Repository search on the MNEMOSYNE-170 base found the health-review handoff/startup records but no canonical completed result report.

```yaml
health_review_gate:
  route_owner: separate_conversation
  canonical_result_found_on_master: false
  takeover_by_MNEMOSYNE_170: prohibited
  M0_M1_blocked: false
  bounded_M2_bootstrap_file_creation_blocked: false_unless_new_applicable_P0_or_P1_appears
  operational_use_or_broad_target_write:
    required_before_acceptance:
      - check_for_canonical_P0_P1_or_equivalent_findings
      - incorporate_applicable_findings_or_record_explicit_deferral_and_residual_risk
```

## 11. Rollback and revision plan

```yaml
rollback_or_revision_plan:
  before_M2_merge:
    action: close_or_replace_the_single_M2_PR
    target_workspace_on_master: absent
  after_M2_merge_but_before_operational_acceptance:
    action: revert_the_M2_merge_or_supersede_with_a_reviewed_v0_1_1_revision
    public_Git_history_remains: true
  after_operational_acceptance:
    action: use_MA_MIG_manifest_and_owner_approved_change_class_gate
  non_reversible_limitations:
    - committed_public_history_cannot_be_promised_erased
    - external_copies_or_caches_may_persist
```

## 12. M1 acceptance criteria

M1 is complete when the canonical MNEMOSYNE-170 PR is human-merged and:

```yaml
M1_acceptance:
  workspace_and_repository_role_decided: true
  public_safe_input_and_storage_policy_approved: true
  exact_seven_file_M2_scope_defined: true
  target_runtime_truth_source_ref_defined: true
  standard_upgrade_profile_instantiated_for_future_M2: true
  capability_split_and_escalation_defined: true
  validation_stop_and_rollback_rules_defined: true
  health_review_boundary_recorded_without_takeover: true
  target_files_created_in_MNEMOSYNE_170: false
```

## 13. Boundary

- This manifest does not create the workspace or target files.
- It does not authorize operational use.
- It does not authorize private materials, automation, RAG, MCP or shared memory.
- It does not modify the Meta-Agent test-route evidence.
- It does not change Mnemosyne's execution source.
- After merge, M2 still requires fresh task-local repository-write authorization.
