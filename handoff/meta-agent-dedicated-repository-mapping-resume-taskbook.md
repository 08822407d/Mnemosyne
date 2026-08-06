# Meta-Agent Dedicated-Repository Mapping Resume — Frontier Taskbook

> Semantic continuation after the mechanical inventory task. This task must not repeat repository-wide enumeration when a valid merged E0 inventory exists. It performs the authority, migration, behavior-guidance, memory-alignment and Owner-decision work that requires frontier judgment. It writes only Mnemosyne and stops before destination initialization.

```yaml
task_id: META-AGENT-DEDICATED-REPOSITORY-MAPPING-RESUME-001
prepared_by: MNEMOSYNE-192
status: WAITING_FOR_MECHANICAL_INVENTORY_PR_MERGE
owner_route: dedicated_Meta_Agent_construction_conversation
recommended_model_class: GPT_Pro_or_frontier
source_repository: 08822407d/Mnemosyne
destination_repository: 08822407d/Meta-Agent
destination_write_authorized: false
destination_initialization_authorized: false
shadow_copy_authorized: false
cutover_authorized: false
private_material_authorized: false
```

## 1. Purpose

Consume the merged mechanical inventory and finish the substantive preparation that the prior task could not start:

1. bind the blocked result and mechanical-inventory evidence;
2. close PR #255 post-merge state and repair current Meta-Agent navigation;
3. adjudicate every source artifact's authority, memory role, status and migration disposition;
4. produce complete candidate destination mapping options;
5. compare snapshot-first and filtered-history strategies;
6. produce a Meta-Agent-owned behavior-guidance adoption matrix;
7. align the initial Mnemosyne memory-system candidate with the actual source inventory;
8. produce a contextualized Owner initialization decision package;
9. create one Mnemosyne branch and at most one canonical PR;
10. stop before any write to `08822407d/Meta-Agent`.

## 2. Cost-control and non-repetition rule

The task must not rerun exhaustive recursive Git enumeration unless the merged E0 identity fails verification.

```yaml
reuse_rule:
  required_E0_task: META-AGENT-DEDICATED-REPOSITORY-MECHANICAL-INVENTORY-001
  required_E0_status: PASS_TO_FRONTIER_MAPPING_RESUME
  verify_only:
    - E0_source_commit_is_ancestor_or_identical_to_execution_time_latest_master
    - E0_root_subtree_SHA_matches_that_source_commit
    - E0_manifest_hashes_match_repository_files
    - E0_recursive_tree_complete_true
    - E0_duplicate_paths_zero
    - E0_missing_objects_zero
  prohibited_when_valid:
    - rerun_git_ls_tree_for_full_semantic_work
    - repeat_tool_capability_exploration
    - repeat_receive_only_test
```

If E0 identity is valid but latest master contains later changes under `target-projects/meta-agent/`, return `BLOCKED_SOURCE_TREE_CHANGED_AFTER_E0` and request a bounded mechanical delta refresh. Do not silently apply an old manifest to changed source content.

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
  cutover: prohibited
```

## 4. Execution-time preflight

Verify:

```yaml
source:
  repository: 08822407d/Mnemosyne
  execution_time_latest_master:
  open_PRs: []
  exact_task_or_branch_matches: []

E0:
  mechanical_inventory_PR_merged: true
  result_record_status: PASS_TO_FRONTIER_MAPPING_RESUME
  source_commit:
  root_subtree_SHA:
  manifest_hashes_match: true
  source_tree_unchanged_since_E0: true

destination:
  repository: 08822407d/Meta-Agent
  visibility: public
  commits: 0
  branches: []
  open_PRs: []

target_truth:
  path: target-projects/meta-agent/current/approved-spec.md
  effective_for_operational_use: false
```

Stop on any changed state, overlapping PR, invalid manifest identity, destination mutation, or target-truth/activation change.

## 5. Required reading order

### 5.1 Truth, authority and method

1. `target-projects/meta-agent/current/approved-spec.md`
2. `target-projects/meta-agent/authority/source-and-owner-map.md`
3. `target-projects/meta-agent/methodology/core-methodology.md`
4. `target-projects/meta-agent/cases/case-and-feedback-ledger.md`
5. `target-projects/meta-agent/history/decision-version-and-migration-log.md`

### 5.2 Current and historical state

6. `target-projects/meta-agent/current/active-context.md`
7. `target-projects/meta-agent/handoff/handoff-current.md`
8. `target-projects/meta-agent/current/meta-agent-mnemosyne-guidance-compatibility-guard.md`
9. `target-projects/meta-agent/migration/pre-migration-preservation-checkpoint-2026-08-06.md`
10. `notes/codex-task-results/META-AGENT-DEDICATED-REPOSITORY-MIGRATION-PREPARATION-001-blocked-result.md`
11. `notes/adjudications/meta-agent-migration-preparation-enumeration-blocker-adjudication-2026-08-06.md`

### 5.3 E0 mechanical evidence

12. `target-projects/meta-agent/migration/source-inventory/README.md`
13. `target-projects/meta-agent/migration/source-inventory/source-tree-closure-v0.1.yaml`
14. `target-projects/meta-agent/migration/source-inventory/source-tree-entries-v0.1.jsonl`
15. `target-projects/meta-agent/migration/source-inventory/source-blob-inventory-v0.1.jsonl`
16. `target-projects/meta-agent/migration/source-inventory/source-artifact-preclassification-v0.1.jsonl`
17. `target-projects/meta-agent/migration/source-inventory/source-inventory-verification-v0.1.md`
18. E0 task result and PR metadata

### 5.4 Mnemosyne migration and memory design

19. `notes/migration-designs/meta-agent-dedicated-repository-migration-assessment-v0.1.md`
20. `notes/validation-designs/target-project-dedicated-repository-migration-and-pr-validation-v0.1.md`
21. `notes/migration-designs/meta-agent-pre-migration-readiness-assessment-2026-08-06.md`
22. `notes/target-project-delivery-models/mnemosyne-to-dedicated-target-repository-operating-model-v0.1.md`
23. `notes/memory-system-designs/meta-agent-initial-memory-system-design-v0.1.md`
24. `notes/validation-designs/meta-agent-initial-memory-system-adoption-and-validation-v0.1.md`

### 5.5 Accepted research reviews only by default

25. `target-projects/meta-agent/research/waves/2026Q3-independent-wave-001/reviews/MA-DR-08-15-cross-report-convergence-v0.1.md`
26. `target-projects/meta-agent/research/waves/2026Q3-independent-wave-001/reviews/MA-DR-11-formal-intake-review.md`
27. `target-projects/meta-agent/research/waves/2026Q3-independent-wave-001/reviews/MA-DR-13-formal-intake-review.md`

Read raw reports only for a specific unresolved claim and record each access.

## 6. Branch and write scope

Create one branch:

```text
meta-agent-dedicated-repository-mapping-resume-001
```

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

At most one PR. No destination write.

## 7. Workstream A — closeout and live navigation repair

Create:

```text
target-projects/meta-agent/migration/receipts/PR-255-post-merge-closeout-and-supersession.yaml
target-projects/meta-agent/migration/receipts/migration-preparation-blocked-result-binding.yaml
```

Update live `active-context.md` and `handoff-current.md` to reflect actual repository facts:

```yaml
PR_255:
  merged: true
  merge_commit: 9e60fef75c524fc2e8acf227e84eaa820f08bc59
preservation_branch_pending: false
preservation_PR_pending: false
E0_inventory_status: merged_PASS
destination_initialized: false
safe_next_action: Owner_review_of_mapping_behavior_and_initialization_decision_package
```

Do not rewrite the historical preservation checkpoint. Point to its supersession/closeout.

Avoid another future-PR recursion: current state should say that the task's own PR requires human review without making a not-yet-created PR a precondition for interpreting already merged historical state.

## 8. Workstream B — final semantic source manifest

Consume every E0 blob record. Produce one final record per blob:

```yaml
semantic_source_artifact:
  source_path:
  git_blob_sha:
  content_sha256:
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
  current_status:
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
  reviewer_confidence:
```

No blob may be omitted. Any unresolved item must remain explicit and block destination write if material or authority is uncertain.

## 9. Workstream C — destination mapping options

Produce two complete options covering every source artifact:

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

For each option include exact rewrite rules, preserved/changed counts, cross-repository link updates, fresh-session load cost, review burden, history/rollback effects, behavior-guidance effects, advantages, risks and recommendation.

Do not select the Owner's destination root silently.

## 10. Workstream D — history strategy

Compare:

```yaml
snapshot_first:
  source_commit_and_manifest: exact
  immutable_Mnemosyne_pointer: required
  destination_history_begins_at_migration: true
  default_recommendation: true_unless_measured_need_changes_it

filtered_subdirectory_history:
  exact_tool_version_and_ref_scope: required
  rewritten_path_validation: required
  direct_per_file_history: preserved_with_rewrite
  complexity_and_risk: higher

full_repository_mirror:
  disposition: reject_for_project_separation
```

The Owner chooses.

## 11. Workstream E — Meta-Agent-owned behavior guidance

Create candidate, non-active files:

```text
target-projects/meta-agent/current/meta-agent-behavior-guidance-candidate.md
target-projects/meta-agent/commands/load-meta-agent-guidance-candidate.md
target-projects/meta-agent/migration/behavior-guidance-adoption-matrix-v0.1.yaml
```

The matrix must classify each relevant Mnemosyne semantic as `adopt`, `adapt_for_Meta_Agent`, `exclude_Mnemosyne_specific`, or `defer`.

Required topics:

- sole target truth and artifact-role separation;
- evidence-bound engineering judgment;
- opening operation and visible next step;
- model-capability and research-value assessment;
- file-first delivery and one canonical Deep Research report;
- explicit external-task intent and dedicated operator flow;
- `MA-DR-*` compact display names;
- material/public/private boundary;
- platform permission versus task authorization;
- one task/branch/PR lineage;
- run context and PR provenance;
- no automatic handoff or route import;
- no automatic methodology promotion;
- no hidden backend inference.

Explicitly exclude Mnemosyne maintenance live state, MNE-DR A1/A2, other targets, and automatic future guard propagation.

These candidates must not be activated by this task.

## 12. Workstream F — initial memory-system alignment

For every component in the Mnemosyne candidate memory design, produce:

```yaml
memory_alignment:
  design_component:
  current_source_artifacts: []
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

Preserve the recommended separation:

```yaml
shadow_migration_PR:
  - current_existing_target_package
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

## 13. Workstream G — Owner initialization decision package

Create:

```text
target-projects/meta-agent/decision-support/dedicated-repository-initialization-owner-decision-package.md
```

Ask only decisions still required, with context, consequences, recommendation, alternatives, deferral effect and free-form option:

1. confirm long-term public visibility or defer/reconsider;
2. choose destination root mapping;
3. choose snapshot-first or filtered history;
4. choose initialization actor/surface;
5. choose exact first-commit paths and wording;
6. decide whether behavior guidance candidate enters shadow PR;
7. choose rollback window and trigger;
8. confirm destination initialization remains non-authoritative before cutover.

Recommended initial commit candidate remains minimal:

```text
README.md
MIGRATION-STATUS.md
```

with explicit `initialized_empty_non_authoritative` semantics. Recommendation is rejectable and not an authorization.

## 14. Workstream H — result and PR

Create one result record with full provenance and one PR. The PR must state:

- source E0 commit/subtree/manifest identities;
- semantic manifest counts and unresolved blockers;
- both mapping options;
- behavior guidance remains candidate;
- memory design remains candidate;
- destination writes are zero;
- Owner decisions remain pending;
- next phase is initialization decision, not automatic write.

## 15. Result semantics

```yaml
- READY_FOR_OWNER_INITIALIZATION_DECISION
- READY_WITH_BLOCKING_OWNER_DECISIONS
- REVISE_MECHANICAL_OR_SEMANTIC_MAPPING
- BLOCKED_SOURCE_TREE_CHANGED_AFTER_E0
- BLOCKED_AUTHORITY_OR_MATERIAL_CONFLICT
```

## 16. Stop conditions

Stop if:

- E0 evidence is absent, invalid, or stale against changed target root;
- any source blob lacks a final semantic record;
- material or authority is unknown;
- destination has changed;
- a competing PR exists;
- the task would modify target truth, approved methodology, authority map, case ledger or migration history;
- destination write or initialization is requested;
- behavior guidance or memory design would be activated automatically.

## 17. Safe next action

Human review and merge of the one Mnemosyne PR precede any destination initialization. The Owner then answers the initialization package. No automatic target write follows.
