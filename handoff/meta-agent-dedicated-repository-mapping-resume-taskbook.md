# Meta-Agent Dedicated-Repository Mapping Resume — Frontier Taskbook v0.2

> Semantic continuation after the merged E0 mechanical inventory. This version uses a two-plane source contract: a frozen 226-blob payload snapshot plus later migration-control evidence. It must not repeat repository-wide enumeration when the E0 evidence is valid. It writes only Mnemosyne and stops before destination initialization.

```yaml
task_id: META-AGENT-DEDICATED-REPOSITORY-MAPPING-RESUME-001
taskbook_version: 0.2.0
prepared_by: MNEMOSYNE-192
revised_by: MNEMOSYNE-194
status: READY_AFTER_MNEMOSYNE_194_MERGE_NOT_EXECUTED
owner_route: dedicated_Meta_Agent_construction_conversation
recommended_model_class: GPT_Pro_or_frontier
source_repository: 08822407d/Mnemosyne
destination_repository: 08822407d/Meta-Agent
source_contract: handoff/meta-agent-dedicated-repository-mapping-resume-source-contract-v0.2.yaml
destination_write_authorized: false
destination_initialization_authorized: false
shadow_copy_authorized: false
cutover_authorized: false
private_material_authorized: false
```

## 1. Purpose

Consume the merged E0 evidence and finish the substantive migration preparation that requires frontier judgment:

1. verify and bind the E0 mechanical inventory and its later remote PR transfer;
2. close PR #255 post-merge state and repair current Meta-Agent navigation;
3. adjudicate every blob in the frozen 226-blob payload snapshot by authority, memory role, material class, status and migration disposition;
4. keep PR #258 inventory artifacts in a separate control-evidence plane rather than recursively adding them to the payload;
5. produce complete candidate destination mapping options;
6. compare snapshot-first and filtered-history strategies;
7. produce Meta-Agent-owned behavior-guidance candidates and an adoption matrix;
8. align the initial Mnemosyne memory-system candidate with the actual source inventory;
9. produce a contextualized Owner initialization decision package;
10. produce an exact E1 overlay manifest for the task's own bounded changes;
11. create one Mnemosyne branch and at most one canonical PR;
12. stop before any write to `08822407d/Meta-Agent`.

## 2. Supersession and non-repetition rule

This v0.2 taskbook supersedes the v0.1 rule that treated any post-E0 target-root change as an automatic block. PR #258 necessarily added the inventory generator and manifests inside the root they describe. Re-inventorying those generated artifacts would create self-reference and snapshot churn.

Required source contract:

```text
handoff/meta-agent-dedicated-repository-mapping-resume-source-contract-v0.2.yaml
```

```yaml
reuse_rule:
  required_E0_task: META-AGENT-DEDICATED-REPOSITORY-MECHANICAL-INVENTORY-001
  required_E0_status: PASS_TO_FRONTIER_MAPPING_RESUME
  base_payload_commit: 8ef1c43b18b8686a30ffef544ca8b32fce1ca6cb
  base_payload_root_subtree: 4c1cd341777d46b3d6794abc62682e9c915ec46a
  base_payload_blob_count: 226
  E0_remote_PR: 258
  E0_remote_merge_commit: a443940a2ff2425ebb8fc67e084fce5b7b49de58

  verify_only:
    - source_contract_matches_E0_closure
    - E0_manifest_hashes_match_repository_files
    - E0_recursive_tree_complete_true
    - E0_duplicate_paths_zero
    - E0_missing_objects_zero
    - execution_time_diff_from_base_contains_only_expected_control_paths_before_E1

  prohibited_when_valid:
    - rerun_full_recursive_git_ls_tree
    - include_PR258_inventory_outputs_in_the_226_blob_payload
    - repeat_tool_capability_exploration
    - repeat_receive_only_test
    - treat_current_whole_target_root_as_if_it_were_the_E0_payload_tree
```

The payload plane and control-evidence plane are distinct:

```yaml
payload_plane:
  commit: 8ef1c43b18b8686a30ffef544ca8b32fce1ca6cb
  root: target-projects/meta-agent/
  blobs_to_semantically_map: 226

control_evidence_plane:
  minimum_commit: a443940a2ff2425ebb8fc67e084fce5b7b49de58
  exact_PR258_inventory_paths: source_contract_allowlist
  default_destination_disposition: retain_in_Mnemosyne_with_immutable_pointer
```

## 3. Required first response

```yaml
execution_intent:
  response_role: ANALYSIS_AND_PREPARATION
  task_id: META-AGENT-DEDICATED-REPOSITORY-MAPPING-RESUME-001
  execution_disposition: RUN_NOW_REQUIRED
  current_conversation_mainline: META_AGENT_PRODUCT_BUILD
  source_repository_write: authorized_within_exact_task_scope
  destination_repository_write: prohibited
  target_truth_change: prohibited
  accepted_methodology_change: prohibited
  behavior_guidance_activation: prohibited
  memory_system_adoption: prohibited
  cutover: prohibited
```

Do not ask the user to repeat decisions already recorded. Do not silently decide the remaining Owner choices.

## 4. Execution-time preflight

### 4.1 Source repository and lineage

Verify:

```yaml
source:
  repository: 08822407d/Mnemosyne
  execution_time_latest_master:
  latest_master_contains:
    PR_255_merge_9e60fef: true
    PR_256_merge_5bb586c: true
    PR_257_merge_8ef1c43: true
    PR_258_merge_a443940: true
    MNEMOSYNE_194_merge: true
  accessible_open_PRs: []
  exact_task_or_branch_matches: []
  rejected_PR_259:
    closed_unmerged: true
    branch_absent: true
    content_used: false
```

### 4.2 E0 identity

Verify the source contract and merged files:

```yaml
E0:
  result_record_status: PASS_TO_FRONTIER_MAPPING_RESUME
  source_commit: 8ef1c43b18b8686a30ffef544ca8b32fce1ca6cb
  root_subtree_SHA: 4c1cd341777d46b3d6794abc62682e9c915ec46a
  tree_count: 45
  blob_count: 226
  manifest_hashes_match: true
  recursive_tree_complete: true
  duplicate_paths: 0
  missing_objects: 0
```

### 4.3 Expected-control-only drift gate

Compare `8ef1c43b...` to execution-time latest `master`.

Pass only when every pre-E1 target-root change is under:

```text
target-projects/meta-agent/migration/source-inventory/
```

and exactly matches the PR #258 control paths recorded in the source contract. Changes outside the target root are allowed only when they are Mnemosyne taskbooks, adjudications, status, README or result records that do not alter Meta-Agent target-local content.

```yaml
pre_E1_drift_result:
  PASS_EXPECTED_CONTROL_ONLY_DRIFT:
    action: continue_against_frozen_payload_snapshot
  BLOCKED_SOURCE_TREE_CHANGED_AFTER_E0:
    action: request_bounded_mechanical_delta_refresh_for_noncontrol_target_paths_only
  BLOCKED_E0_IDENTITY_MISMATCH:
    action: stop
```

Do not block merely because PR #258 inventory artifacts exist under the bootstrap root.

### 4.4 Destination and target authority

```yaml
destination:
  repository: 08822407d/Meta-Agent
  visibility: public
  commits: 0
  branches: []
  open_PRs: []

target_truth:
  repository: 08822407d/Mnemosyne
  path: target-projects/meta-agent/current/approved-spec.md
  effective_for_operational_use: false
```

Stop on destination mutation, target-truth change, operational activation, unknown visibility/material policy, or an overlapping open PR.

## 5. Required reading order

### 5.1 Source contract and E0 evidence

1. `handoff/meta-agent-dedicated-repository-mapping-resume-source-contract-v0.2.yaml`
2. `notes/adjudications/meta-agent-E0-mechanical-inventory-post-merge-and-snapshot-boundary-adjudication-2026-08-06.md`
3. `target-projects/meta-agent/migration/source-inventory/source-tree-closure-v0.1.yaml`
4. `target-projects/meta-agent/migration/source-inventory/source-tree-entries-v0.1.jsonl`
5. `target-projects/meta-agent/migration/source-inventory/source-blob-inventory-v0.1.jsonl`
6. `target-projects/meta-agent/migration/source-inventory/source-artifact-preclassification-v0.1.jsonl`
7. `target-projects/meta-agent/migration/source-inventory/source-inventory-verification-v0.1.md`
8. `notes/codex-task-results/META-AGENT-DEDICATED-REPOSITORY-MECHANICAL-INVENTORY-001-result.md`
9. PR #258 metadata and changed-path inventory

### 5.2 Truth, authority and method at the frozen payload commit

Read these from `8ef1c43b18b8686a30ffef544ca8b32fce1ca6cb`, not from an unqualified moving branch:

10. `target-projects/meta-agent/current/approved-spec.md`
11. `target-projects/meta-agent/authority/source-and-owner-map.md`
12. `target-projects/meta-agent/methodology/core-methodology.md`
13. `target-projects/meta-agent/cases/case-and-feedback-ledger.md`
14. `target-projects/meta-agent/history/decision-version-and-migration-log.md`
15. `target-projects/meta-agent/current/active-context.md`
16. `target-projects/meta-agent/handoff/handoff-current.md`
17. `target-projects/meta-agent/current/meta-agent-mnemosyne-guidance-compatibility-guard.md`
18. `target-projects/meta-agent/migration/pre-migration-preservation-checkpoint-2026-08-06.md`

### 5.3 Current repository state and prior blocker

19. execution-time current `target-projects/meta-agent/current/active-context.md`
20. execution-time current `target-projects/meta-agent/handoff/handoff-current.md`
21. `notes/codex-task-results/META-AGENT-DEDICATED-REPOSITORY-MIGRATION-PREPARATION-001-blocked-result.md`
22. `notes/adjudications/meta-agent-migration-preparation-enumeration-blocker-adjudication-2026-08-06.md`

Record frozen-versus-current differences. Do not use current stale navigation as target truth.

### 5.4 Mnemosyne migration and memory design

23. `notes/migration-designs/meta-agent-dedicated-repository-migration-assessment-v0.1.md`
24. `notes/validation-designs/target-project-dedicated-repository-migration-and-pr-validation-v0.1.md`
25. `notes/migration-designs/meta-agent-pre-migration-readiness-assessment-2026-08-06.md`
26. `notes/target-project-delivery-models/mnemosyne-to-dedicated-target-repository-operating-model-v0.1.md`
27. `notes/memory-system-designs/meta-agent-initial-memory-system-design-v0.1.md`
28. `notes/validation-designs/meta-agent-initial-memory-system-adoption-and-validation-v0.1.md`

### 5.5 Accepted research reviews only by default

29. `target-projects/meta-agent/research/waves/2026Q3-independent-wave-001/reviews/MA-DR-08-15-cross-report-convergence-v0.1.md`
30. `target-projects/meta-agent/research/waves/2026Q3-independent-wave-001/reviews/MA-DR-11-formal-intake-review.md`
31. `target-projects/meta-agent/research/waves/2026Q3-independent-wave-001/reviews/MA-DR-13-formal-intake-review.md`

Read raw reports only for a specific unresolved classification or mapping claim. Record each raw-report access.

## 6. Cost control for the 226-blob review

The Pro conversation must not read every large raw report or transport chunk in full by default.

```yaml
semantic_review_strategy:
  all_226_records:
    source: E0_blob_inventory_plus_preclassification
    final_record_required: true

  deterministic_low_risk_paths:
    method: path_role_front_matter_and_existing_manifest_review

  material_review_required_50:
    method: explicit_frontier_review
    read_full_source_only_when_needed: true

  raw_transport_chunks:
    default: classify_from_transport_manifest_path_and_accepted_review
    full_chunk_content_read: prohibited_unless_integrity_or_material_dispute_requires_it

  research_reports:
    default: use_formal_intake_and_cross_report_reviews
    raw_report_access: on_demand_and_logged
```

Every base blob still receives a final semantic record; cost control changes the evidence-loading method, not completeness.

## 7. Branch and write scope

Create one branch from execution-time latest `master`:

```text
meta-agent-dedicated-repository-mapping-resume-001
```

Before branch creation and immediately before PR creation, enumerate all accessible open PRs, exact task-ID matches, intended branch matches, and overlapping Meta-Agent migration/state paths.

Allowed Mnemosyne paths:

```text
target-projects/meta-agent/current/active-context.md
target-projects/meta-agent/handoff/handoff-current.md
target-projects/meta-agent/migration/
target-projects/meta-agent/decision-support/
target-projects/meta-agent/current/                     [candidate behavior guidance only]
target-projects/meta-agent/commands/                    [candidate loader only]
notes/codex-task-results/
```

Protected:

```text
target-projects/meta-agent/current/approved-spec.md
target-projects/meta-agent/authority/source-and-owner-map.md
target-projects/meta-agent/methodology/core-methodology.md
target-projects/meta-agent/cases/case-and-feedback-ledger.md
target-projects/meta-agent/history/decision-version-and-migration-log.md
current/human-approved-spec.md
08822407d/Meta-Agent (all paths)
```

At most one canonical PR. No destination write.

## 8. Workstream A — post-PR #255 and E0 remote closeout

Create:

```text
target-projects/meta-agent/migration/receipts/PR-255-post-merge-closeout-and-supersession.yaml
target-projects/meta-agent/migration/receipts/E0-mechanical-inventory-remote-closeout.yaml
target-projects/meta-agent/migration/receipts/migration-preparation-blocked-result-binding.yaml
```

The E0 remote closeout must distinguish:

```yaml
Codex_execution_time:
  local_completion: true
  remote_push: failed
  PR_created_by_execution_environment: false

later_GitHub_transfer:
  PR: 258
  head: fb5ebde7beb0e42bc3b4af33ee205a18d23034ee
  merge_commit: a443940a2ff2425ebb8fc67e084fce5b7b49de58
  content_identity_bound_by_E0_closure: true
```

Update live `active-context.md` and `handoff-current.md` to reflect actual repository facts:

```yaml
PR_255:
  merged: true
  merge_commit: 9e60fef75c524fc2e8acf227e84eaa820f08bc59
preservation_branch_pending: false
preservation_PR_pending: false
E0_inventory_status: merged_PASS
E0_payload_snapshot: 8ef1c43b18b8686a30ffef544ca8b32fce1ca6cb
E0_control_evidence_merge: a443940a2ff2425ebb8fc67e084fce5b7b49de58
destination_initialized: false
safe_next_action: Owner_review_of_mapping_behavior_and_initialization_decision_package
```

Do not rewrite the historical preservation checkpoint. Point to its closeout/supersession. Avoid another self-referential future-PR loop.

## 9. Workstream B — base-snapshot semantic manifest

Consume every one of the 226 E0 base blob records and create:

```text
target-projects/meta-agent/migration/semantic-mapping/base-snapshot-semantic-manifest-v0.2.jsonl
target-projects/meta-agent/migration/semantic-mapping/base-snapshot-summary-v0.2.yaml
```

One final record per E0 blob:

```yaml
semantic_source_artifact:
  source_repository: 08822407d/Mnemosyne
  source_commit: 8ef1c43b18b8686a30ffef544ca8b32fce1ca6cb
  source_path:
  relative_path:
  git_blob_sha:
  content_sha256:
  bytes:
  artifact_id:
  artifact_role:
  authority_class:
  memory_role:
    - canonical_truth
    - authority
    - current_state
    - handoff
    - behavior_guidance
    - methodology
    - case_feedback
    - research_evidence
    - candidate
    - history_migration
    - migration_control
    - derived_navigation
    - raw_transport
    - historical_failure_or_superseded
  material_class:
    - public
    - synthetic
    - redacted
    - safe_pointer
    - blocked_unknown_or_restricted
  current_status_at_snapshot:
  supersession_state:
  migration_zone:
  final_disposition:
    - preserve_exactly
    - preserve_with_path_rewrite
    - transform
    - recompute
    - retain_in_Mnemosyne_with_pointer
    - migrate_minimal_status_only
    - exclude_from_destination
    - blocked_pending_owner_decision
  destination_path_candidates: []
  target_authority_effect:
  source_refs_preserved:
  required_validation: []
  rationale:
  evidence_refs: []
  reviewer_confidence:
```

No base blob may be omitted. Every E0 record with `material_review_required:true` must show explicit review. Any blocked material or authority ambiguity blocks destination initialization.

## 10. Workstream C — control-evidence exclusions and E1 overlay

Create:

```text
target-projects/meta-agent/migration/semantic-mapping/control-evidence-exclusion-ledger-v0.1.yaml
target-projects/meta-agent/migration/semantic-mapping/E1-overlay-manifest-v0.1.jsonl
target-projects/meta-agent/migration/semantic-mapping/composite-migration-candidate-v0.1.yaml
```

### 10.1 Control-evidence exclusion ledger

Record every PR #258 inventory/control path and its disposition. Default:

```yaml
final_disposition: retain_in_Mnemosyne_with_immutable_pointer
part_of_base_payload: false
part_of_destination_copy_by_default: false
```

A minimal destination migration receipt may point back to E0 evidence; do not copy the generator and full inventory manifests merely because they sit under the bootstrap root.

### 10.2 E1 overlay manifest

For every file added, modified or deleted by this E1 task, record:

```yaml
E1_overlay_artifact:
  path:
  operation: add | modify | delete
  base_blob_or_absence:
  branch_head_blob_or_absence:
  artifact_role:
  authority_effect:
  material_class:
  migration_disposition:
  included_in_composite_candidate:
  validation_required:
  rationale:
```

The overlay is a bounded delta, not a second full inventory.

### 10.3 Composite candidate

```yaml
composite_migration_candidate:
  base_payload:
    commit: 8ef1c43b18b8686a30ffef544ca8b32fce1ca6cb
    blob_count: 226
    semantic_manifest:
  E1_overlay:
    manifest:
    added_count:
    modified_count:
    deleted_count:
  excluded_control_evidence:
    ledger:
  unresolved_blockers: []
  post_merge_overlay_verification_required: true
```

## 11. Workstream D — destination mapping options

Produce two complete options covering all 226 base records plus every included E1 overlay artifact.

### Option 1 — project-root flattening

```text
current/
authority/
methodology/
cases/
history/
handoff/
research/
decision-support/
candidates/
migration/
memory/
commands/
```

### Option 2 — preserve bootstrap prefix

```text
target-projects/meta-agent/...
```

For each option include:

```yaml
mapping_option:
  path_rewrite_rules:
  base_records_covered:
  overlay_records_covered:
  excluded_control_records:
  files_preserved_byte_exact:
  files_transformed:
  cross_repository_links_to_update:
  fresh_session_load_cost:
  human_review_burden:
  history_and_rollback_effect:
  behavior_guidance_effect:
  advantages: []
  risks: []
  recommendation:
  recommendation_is_rejectable: true
```

No path may disappear. Do not silently select the Owner's destination root.

## 12. Workstream E — history strategy

Compare:

```yaml
snapshot_first:
  payload_source_commit: 8ef1c43b18b8686a30ffef544ca8b32fce1ca6cb
  base_manifest: exact
  E1_overlay: exact
  immutable_Mnemosyne_pointer: required
  destination_history_begins_at_migration: true
  default_recommendation: true_unless_measured_need_changes_it

filtered_subdirectory_history:
  exact_tool_version_and_ref_scope: required
  rewritten_path_validation: required
  treatment_of_post_snapshot_control_artifacts: explicit
  direct_per_file_history: preserved_with_rewrite
  complexity_and_risk: higher

full_repository_mirror:
  disposition: reject_for_project_separation
```

The Owner chooses.

## 13. Workstream F — Meta-Agent-owned behavior guidance

Create candidate, non-active files:

```text
target-projects/meta-agent/current/meta-agent-behavior-guidance-candidate.md
target-projects/meta-agent/commands/load-meta-agent-guidance-candidate.md
target-projects/meta-agent/migration/behavior-guidance-adoption-matrix-v0.1.yaml
```

The matrix classifies each relevant Mnemosyne semantic as:

```yaml
- adopt
- adapt_for_Meta_Agent
- exclude_Mnemosyne_specific
- defer_pending_evidence_or_owner
```

Required topics:

1. sole target truth and artifact-role separation;
2. objective evidence-bound engineering judgment;
3. opening operation section and visible next step;
4. model-capability and research-value assessment;
5. file-first delivery and one canonical Deep Research report;
6. explicit external-task intent and dedicated operator flow;
7. `MA-DR-*` compact display names;
8. public/private/material-safety boundary;
9. platform permission versus task authorization;
10. one task/branch/PR lineage;
11. run context and PR provenance;
12. no automatic handoff or route import;
13. no automatic methodology promotion;
14. no exact-backend inference from visible selection or style.

Explicitly exclude Mnemosyne maintenance live state, MNE-DR A1/A2, other targets, and automatic future propagation of Mnemosyne guard changes.

These candidates must not be activated by this task.

## 14. Workstream G — initial memory-system alignment

For every component in:

```text
notes/memory-system-designs/meta-agent-initial-memory-system-design-v0.1.md
```

produce:

```yaml
memory_alignment:
  design_component:
  base_snapshot_artifacts: []
  E1_overlay_candidate_paths: []
  destination_candidate_paths: []
  already_satisfied:
  gap:
  adoption_effect:
  requires_target_truth_change:
  requires_new_stable_ID:
  validation_refs: []
  recommendation:
    - migrate_existing
    - adopt_behavior_during_shadow
    - defer_to_post_migration_memory_PR
    - reject_or_defer
```

Preserve the separation:

```yaml
shadow_migration_PR:
  - existing_target_package
  - behavior_guidance_candidate
  - mapping_validation_and_rollback

post_migration_memory_foundation_PR:
  - artifact_role_registry
  - prospective_memory_envelope
  - load_profiles
  - freshness_retention_supersession
  - deterministic_active_memory_index
  - validation_scaffolding
```

Do not silently adopt the memory design.

## 15. Workstream H — Owner initialization decision package

Create:

```text
target-projects/meta-agent/decision-support/dedicated-repository-initialization-owner-decision-package.md
```

Ask only decisions still required, with context, consequences, recommendation, alternatives, deferral effect and free-form/reject-premise option:

1. confirm long-term public visibility or defer/reconsider;
2. choose destination root mapping;
3. choose snapshot-first/composite-overlay or filtered history;
4. choose initialization actor/surface;
5. choose exact first-commit paths and wording;
6. decide whether behavior guidance candidate enters the later shadow PR;
7. choose rollback window and trigger;
8. confirm destination initialization remains non-authoritative before cutover;
9. confirm treatment of accepted research evidence versus raw transport chunks;
10. confirm whether a minimal destination pointer to Mnemosyne E0 evidence is desired.

Recommended initial commit candidate remains minimal:

```text
README.md
MIGRATION-STATUS.md
```

with explicit `initialized_empty_non_authoritative` semantics. Recommendation is rejectable and not authorization.

## 16. Workstream I — result, PR and overlay verification plan

Create one result record with full provenance and one PR. The PR must state:

- payload source commit/subtree/counts;
- E0 control-evidence commit and manifest identities;
- semantic manifest count exactly 226;
- material-review completion and unresolved blockers;
- control-evidence exclusions;
- E1 overlay counts and paths;
- both mapping options;
- behavior guidance remains candidate;
- memory design remains candidate;
- destination writes are zero;
- Owner decisions remain pending;
- next phase is mechanical overlay verification and Owner initialization decision, not automatic write.

Prepare a post-merge mechanical verification instruction that can be run without Pro to confirm:

```yaml
- E1_PR_merge_commit
- overlay_paths_exact
- overlay_blob_identities_match
- no_unlisted_target_root_changes
- base_E0_manifest_unchanged
- destination_repository_unchanged
```

## 17. Result semantics

```yaml
- READY_FOR_POST_MERGE_OVERLAY_VERIFICATION_AND_OWNER_DECISION
- READY_WITH_BLOCKING_OWNER_DECISIONS
- REVISE_SEMANTIC_MAPPING
- BLOCKED_SOURCE_TREE_CHANGED_AFTER_E0
- BLOCKED_E0_IDENTITY_MISMATCH
- BLOCKED_AUTHORITY_OR_MATERIAL_CONFLICT
- BLOCKED_DESTINATION_STATE_CHANGED
```

Aggregate quality cannot override one truth, authority, material, payload-closure or destination-state blocker.

## 18. Stop conditions

Stop if:

- E0 evidence is absent or invalid;
- pre-E1 target-root drift includes anything outside the exact PR #258 control prefix;
- any of the 226 base blobs lacks a final semantic record;
- any E1 changed path lacks an overlay record;
- material or authority remains unknown;
- destination has changed;
- a competing PR exists;
- the task would modify target truth, accepted methodology, authority map, case ledger or migration history;
- destination write or initialization is requested;
- behavior guidance or memory design would be activated automatically;
- PR #259 content or deleted branch is imported.

## 19. Safe next action

Human review and merge of the one Mnemosyne E1 PR precede:

1. a mechanical post-merge E1-overlay verification;
2. Owner review of the initialization decision package;
3. any separately authorized minimal destination initialization.

No automatic target write follows.
