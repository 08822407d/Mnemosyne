# First-Target Minimum Upgrade Contract Status

> Non-execution-source live candidate status. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
status_id: FIRST-TARGET-MINIMUM-UPGRADE-CONTRACT-STATUS-003
created_by_task: MNEMOSYNE-166
last_status_task: MNEMOSYNE-170
candidate_id: FIRST-TARGET-MINIMUM-UPGRADE-CONTRACT-001
candidate_path: notes/first-target-minimum-upgrade-contract-v0.1.md
advisory_pilot_checklist: notes/first-target-minimum-upgrade-contract-advisory-pilot-checklist-v0.1.md
source_research_cycle: RC-2026Q3-target-memory-governance-and-learning
status: advisory_pilot_instantiated_for_Meta_Agent_pending_M0_M1_PR_merge
disposition: ACCEPT_AS_ADVISORY_PILOT_ONLY
execution_source: current/human-approved-spec.md
execution_source_modified: false
formal_target_project_selected: true
selected_target_project: meta-agent
target_specific_profile: standard
template_pack_modified: false
target_files_created: false
implementation_authorized_in_MNEMOSYNE_170: false
```

## User route selection and disposition

The user first accepted the candidate as an advisory pilot rather than a mandatory global rule. After PR #220 merged, the user explicitly selected:

```text
META_AGENT_PRODUCT_BUILD_LAUNCH_PREPARATION
```

and required M0 and M1 to complete before v0.1 target-file construction.

```yaml
selected_route:
  id: META_AGENT_PRODUCT_BUILD_LAUNCH_PREPARATION
  target_project: meta-agent
  decision_ref: current_conversation_user_instruction_after_PR_220_merge

disposition:
  value: ACCEPT_AS_ADVISORY_PILOT_ONLY
  target_specific_instantiation: META-AGENT-V0.1-UPGRADE-CONTRACT-001
  profile: standard
  global_template_mandate: false
  target_tailoring_required: true
  global_promotion_requires:
    - completed_target_specific_pilot
    - evidence_and_burden_review
    - explicit_user_disposition
    - fresh_bounded_repository_task
```

## Target-specific instantiation

```yaml
Meta_Agent_pilot:
  M0_ref: notes/first-target-project-intake-records/meta-agent/meta-agent-v0.1-M0-requirements-and-authority-baseline.md
  M1_ref: notes/first-target-project-intake-records/meta-agent/meta-agent-v0.1-M1-workspace-safety-build-manifest.md
  target_runtime_truth_source: target-projects/meta-agent/current/approved-spec.md
  workspace_root: target-projects/meta-agent/
  profile: standard
  initial_versions:
    design_version: 0.1.0
    schema_version: 0.1.0
    policy_version: 0.1.0
    delivery_version: 0.1.0
  target_write_now: false
  M2_after_merge_requires_fresh_authorization: true
```

The standard profile is selected because Meta-Agent is expected to be long-lived and methodology-bearing. It remains file-based and deliberately excludes unnecessary service architecture.

## Candidate scope retained

The target-specific pilot covers:

- stable identity for authority-bearing objects;
- source references and object lineage;
- design, schema, policy and delivery versions;
- preserved raw evidence and approved authority;
- migration manifests and old-to-new mappings for breaking or authority changes;
- preserve/transform/recompute/retire decisions;
- validation and acceptance criteria;
- previous-state and rollback references;
- rebuildable derived views where practical;
- target-specific escalation by change class;
- bounded next-tier execution and frontier escalation;
- burden and value review before any global promotion.

It does **not** make the following universal or required for Meta-Agent v0.1:

- full event-sourced runtime;
- dual-write;
- shadow cutover;
- bitemporal storage;
- automated migration service;
- a six-layer memory architecture;
- RAG, MCP, vector storage or auto-writeback.

## Checklist activation

The advisory checklist becomes applicable to the Meta-Agent M2 construction after the canonical MNEMOSYNE-170 PR merges and a fresh M2 task is authorized.

```yaml
activation_gate:
  target_project_selected: true
  target_owner_identified: true
  target_runtime_truth_source_identified: true
  repository_and_storage_safety_boundary: defined_in_M1
  target_lifespan_and_change_expectation: long_lived_versioned
  approved_run_manifest: defined_in_M1_effective_on_merge
  M2_task_local_write_authorization: still_required
```

The checklist remains non-blocking for the target design by default. M1 makes selected identity, authority, version, rollback and proportionality checks part of M2 acceptance for this target only.

## Existing-template relationship

The target-project template pack already contains adjacent hooks for migration requirement, design version, model migration, drift review, versioning and rollback. MNEMOSYNE-170 does not modify that template pack.

The pilot is instantiated through the Meta-Agent-specific M0/M1 artifacts rather than promoted into a mandatory global template. Later evidence may justify a small global patch, simplification or rejection.

## Pilot result options after M2

```yaml
pilot_result_options:
  PASS_FOR_TARGET_SPECIFIC_USE:
    meaning: useful_and_proportionate_for_Meta_Agent_v0_1
  PASS_WITH_SIMPLIFICATION:
    meaning: useful_after_reducing_fields_or_gates
  REVISE_CONTRACT:
    meaning: candidate_structure_requires_revision
  DEFER_UNTIL_REAL_MIGRATION_EVIDENCE:
    meaning: first_build_evidence_is_insufficient
  REJECT_AS_TOO_BURDENSOME:
    meaning: process_cost_exceeds_demonstrated_value
```

No pilot result automatically changes Mnemosyne or target-project execution sources or global templates.

## Boundaries

- No target workspace, material or target file is created by MNEMOSYNE-170.
- No target runtime truth source exists until M2 creates and the user accepts it.
- No execution-source or global template change is authorized.
- No automatic migration, writeback, model routing, cross-Agent sharing or learner profiling is authorized.
- The non-FABLE health review and all other conversation-owned routes remain separate.
- Public Git history limitations apply to any later target write.

## Safe next action

```yaml
safe_next_action:
  current:
    - review_and_merge_the_single_MNEMOSYNE_170_PR
  after_merge:
    - verify_M0_M1_and_standard_profile_on_latest_master
    - create_one_bounded_M2_target_file_construction_task
  operational_use: requires_M2_acceptance_and_user_disposition
```
