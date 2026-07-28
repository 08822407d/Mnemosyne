# First-Target Minimum Upgrade Contract Status

> Non-execution-source live candidate/pilot status. `current/human-approved-spec.md` remains Mnemosyne's only execution source; target operational acceptance remains separate.

```yaml
status_id: FIRST-TARGET-MINIMUM-UPGRADE-CONTRACT-STATUS-005
created_by_task: MNEMOSYNE-166
last_status_task: MNEMOSYNE-172
candidate_id: FIRST-TARGET-MINIMUM-UPGRADE-CONTRACT-001
candidate_path: notes/first-target-minimum-upgrade-contract-v0.1.md
advisory_pilot_checklist: notes/first-target-minimum-upgrade-contract-advisory-pilot-checklist-v0.1.md
source_research_cycle: RC-2026Q3-target-memory-governance-and-learning
status: Meta_Agent_M2_merged_design_time_pilot_pass_transferred_for_owner_review
disposition: ACCEPT_AS_ADVISORY_PILOT_ONLY
execution_source: current/human-approved-spec.md
execution_source_modified: false
selected_target_project: meta-agent
target_specific_profile: standard
canonical_M2_PR: 222
canonical_M2_merge_commit: b8d75150ea2058f0dc0ca88f5666bd95b4e8592e
target_files_created_on_master: 7
operational_use_authorized: false
global_template_promotion: false
```

## 1. Target-specific instantiation

```yaml
Meta_Agent_pilot:
  contract_id: META-AGENT-V0.1-UPGRADE-CONTRACT-001
  M0_ref: notes/first-target-project-intake-records/meta-agent/meta-agent-v0.1-M0-requirements-and-authority-baseline.md
  M1_ref: notes/first-target-project-intake-records/meta-agent/meta-agent-v0.1-M1-workspace-safety-build-manifest.md
  M2_result_ref: notes/codex-task-results/MNEMOSYNE-171-result.md
  M2_PR: 222
  M2_state: merged
  target_runtime_truth_source: target-projects/meta-agent/current/approved-spec.md
  target_truth_effective: false_pending_owner_acceptance
  workspace_root: target-projects/meta-agent/
  profile: standard
  initial_versions:
    design_version: 0.1.0
    schema_version: 0.1.0
    policy_version: 0.1.0
    delivery_version: 0.1.0
  operational_acceptance: pending
  route_owner_after_MNEMOSYNE_172_merge: existing_dedicated_Meta_Agent_conversation
```

The candidate remains target-tailored. Nothing in this pilot makes it mandatory for all Mnemosyne products.

## 2. Design-time checklist result

```yaml
advisory_pilot_interim_result:
  result: PASS_FOR_TARGET_SPECIFIC_DESIGN_USE_PENDING_OWNER_ACCEPTANCE
  stable_identity: pass
  source_and_authority: pass
  compact_version_set: pass
  realistic_change_mapping: pass_bootstrap_and_future_schema
  preserve_transform_recompute_retire: pass
  semantic_validation_requirements: pass
  previous_state_and_rollback: pass
  rebuildable_derived_views: pass_no_initial_derived_views
  Mnemosyne_target_truth_separation: pass
  next_tier_executor_and_frontier_escalation: pass
  proportionality: pass_compact_seven_file_profile
  target_design_blocked_by_checklist: false
  operational_use_authorized: false
```

This is a design-time result, not proof that a real migration is effortless or that the contract should be globally promoted.

## 3. Upgradeability available from the first target write

- stable IDs for requirements, pending requirements, decisions, methods and migrations;
- one designated but inactive target truth-source path;
- explicit artifact roles and source refs;
- design/schema/policy/delivery versions from v0.1;
- bootstrap transition and future old-to-new mapping schema;
- preserve/transform/recompute/retire defaults;
- previous-state reference and rollback plan;
- empty case/feedback ledger with a promotion gate;
- bounded next-tier execution and frontier escalation;
- no operational activation without owner disposition.

These mechanisms are sufficient for the dedicated Meta-Agent conversation to continue without waiting for all Mnemosyne research and TODOs.

## 4. Complexity deliberately excluded

The Meta-Agent v0.1 pilot does not require:

- full event-sourced runtime;
- dual-write or shadow cutover;
- bitemporal storage;
- automated migration service;
- six-layer mandatory architecture;
- RAG, MCP, vector store, auto-indexing or auto-writeback;
- automatic cross-Agent sharing.

These remain optional future mechanisms triggered by actual target-specific need.

## 5. Evidence and burden boundary

```yaml
current_evidence:
  design_time_value:
    - authority_and_truth_source_defined_before_history_accumulates
    - stable_IDs_and_versions_present_from_v0_1
    - migration_and_rollback_not_retrofitted_after_lock_in
    - seven_file_profile_avoids_service_architecture
  not_yet_measured:
    - real_operational_review_burden
    - first_real_case_update_cost
    - real_migration_cost
    - next_tier_executor_rework_rate
    - long_term_drift_and_retrieval_behavior
    - actual_upgrade_from_a_later_Mnemosyne_release
```

A later review may simplify, revise, defer or reject parts of the contract based on real evidence.

## 6. Transfer and review ownership

```yaml
transfer:
  handoff_package: handoff/meta-agent-product-build-return-to-dedicated-conversation-handoff-package.md
  startup_prompt: handoff/meta-agent-product-build-return-to-dedicated-conversation-startup-prompt.md
  effective_on: human_merge_of_canonical_MNEMOSYNE_172_PR
  dedicated_conversation_next_role:
    - receive_and_reanchor
    - prepare_owner_review_and_disposition_after_separate_instruction
    - measure_pilot_burden_and_value_after_any_bounded_use
  current_Mnemosyne_conversation_after_transfer:
    - no_further_Meta_Agent_product_actions_unless_explicitly_reassigned
```

## 7. Future pilot result options

```yaml
future_pilot_result_options:
  PASS_FOR_TARGET_SPECIFIC_USE:
    meaning: useful_and_proportionate_for_Meta_Agent
  PASS_WITH_SIMPLIFICATION:
    meaning: useful_after_reducing_fields_or_gates
  REVISE_CONTRACT:
    meaning: target_specific_structure_requires_revision
  DEFER_UNTIL_REAL_MIGRATION_EVIDENCE:
    meaning: build_only_evidence_is_insufficient
  REJECT_AS_TOO_BURDENSOME:
    meaning: process_cost_exceeds_demonstrated_value
```

No result automatically changes either execution source or the global target-project template pack.

## 8. Boundaries

- PR #222 is merged, but file creation does not activate operational use.
- No private material, real case or target feedback is included.
- No global template or Mnemosyne execution-source change is authorized.
- The non-FABLE health review remains separately owned.
- Public Git history limitations remain explicit.
- The transfer handoff is not owner acceptance.

## 9. Safe next action

```yaml
safe_next_action:
  - review_and_merge_the_single_MNEMOSYNE_172_handoff_PR
  - existing_dedicated_Meta_Agent_conversation_receives_and_verifies_the_package
  - dedicated_conversation_prepares_owner_disposition_only_after_separate_user_instruction
  - after_first_bounded_use_measure_burden_value_and_upgradeability
```
