# First-Target Minimum Upgrade Contract Status

> Non-execution-source live candidate/pilot status. `current/human-approved-spec.md` remains Mnemosyne's only execution source; target operational acceptance remains separate.

```yaml
status_id: FIRST-TARGET-MINIMUM-UPGRADE-CONTRACT-STATUS-004
created_by_task: MNEMOSYNE-166
last_status_task: MNEMOSYNE-171
candidate_id: FIRST-TARGET-MINIMUM-UPGRADE-CONTRACT-001
candidate_path: notes/first-target-minimum-upgrade-contract-v0.1.md
advisory_pilot_checklist: notes/first-target-minimum-upgrade-contract-advisory-pilot-checklist-v0.1.md
source_research_cycle: RC-2026Q3-target-memory-governance-and-learning
status: Meta_Agent_M2_design_time_pilot_pass_pending_owner_acceptance_and_real_use_evidence
disposition: ACCEPT_AS_ADVISORY_PILOT_ONLY
execution_source: current/human-approved-spec.md
execution_source_modified: false
selected_target_project: meta-agent
target_specific_profile: standard
canonical_M2_PR: 222
target_files_created_on_canonical_branch: 7
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
  target_runtime_truth_source: target-projects/meta-agent/current/approved-spec.md
  workspace_root: target-projects/meta-agent/
  profile: standard
  initial_versions:
    design_version: 0.1.0
    schema_version: 0.1.0
    policy_version: 0.1.0
    delivery_version: 0.1.0
  operational_acceptance: pending
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

This is an interim design-time result. It is not proof that a later real migration is effortless or that the contract should be globally promoted.

## 3. What the pilot adds from the first target write

- stable IDs for requirements, pending requirements, decisions, methods and migrations;
- one designated target truth-source path;
- explicit artifact roles and source refs;
- design/schema/policy/delivery versions from v0.1;
- a bootstrap transition and future old-to-new mapping schema;
- preserve/transform/recompute/retire defaults;
- a previous-state reference and rollback plan;
- an empty case/feedback ledger with a promotion gate;
- bounded next-tier execution and frontier escalation;
- no operational activation without owner disposition.

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
```

A later review may simplify, revise, defer or reject parts of the contract based on real evidence.

## 6. Pilot result options after owner review and use

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

## 7. Boundaries

- The M2 PR creates the target package only if human-merged.
- File creation or PR merge does not activate operational use.
- No private material, real case or target feedback is included.
- No global template or Mnemosyne execution-source change is authorized.
- The non-FABLE health review remains separately owned.
- Public Git history limitations remain explicit.

## 8. Safe next action

```yaml
safe_next_action:
  - review_and_merge_PR_222
  - record_explicit_owner_operational_disposition
  - after_first_bounded_use_measure_burden_value_and_upgradeability
```
