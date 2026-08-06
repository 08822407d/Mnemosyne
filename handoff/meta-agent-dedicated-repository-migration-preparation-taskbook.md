# Meta-Agent Dedicated Repository Migration Preparation Taskbook

> Canonical next-stage taskbook for the dedicated Meta-Agent construction conversation. This task prepares a complete migration source manifest, candidate mapping, Meta-Agent-owned behavior-guidance adoption matrix and Owner decision package. It does not initialize or write the destination repository and does not perform cutover.

```yaml
task_id: META-AGENT-DEDICATED-REPOSITORY-MIGRATION-PREPARATION-001
prepared_by: MNEMOSYNE-191
status: READY_AFTER_MNEMOSYNE_191_MERGE_NOT_EXECUTED
owner_route: dedicated_Meta_Agent_construction_conversation
recommended_model_class: frontier_or_Pro
source_repository: 08822407d/Mnemosyne
minimum_source_baseline: 9e60fef75c524fc2e8acf227e84eaa820f08bc59
destination_repository: 08822407d/Meta-Agent
destination_write_authorized: false
destination_initialization_authorized: false
shadow_copy_authorized: false
cutover_authorized: false
prototype_or_pilot_authorized: false
private_material_authorized: false
```

## 1. Purpose

Complete all high-quality preparation that must precede the first destination commit:

1. formally bind and close the successful receive-only pre-migration test;
2. repair live Meta-Agent navigation after PR #255 without rewriting historical timepoint evidence;
3. produce an exhaustive recursive source path/tree/blob manifest from a pinned latest Mnemosyne commit;
4. classify every target-local artifact by authority, memory role and migration disposition;
5. freeze candidate source-to-destination path mappings without silently making Owner decisions;
6. produce a Meta-Agent-owned behavior-guidance adoption matrix;
7. assess how the Mnemosyne initial memory-system candidate maps onto the current Meta-Agent package;
8. produce a contextualized Owner decision package for destination initialization and later migration;
9. create one Mnemosyne branch and at most one canonical PR;
10. stop before any write to `08822407d/Meta-Agent`.

## 2. First response and execution intent

The executing conversation must begin with:

```yaml
execution_intent:
  response_role: ANALYSIS_AND_PREPARATION
  task_id: META-AGENT-DEDICATED-REPOSITORY-MIGRATION-PREPARATION-001
  execution_disposition: RUN_NOW_REQUIRED
  current_conversation_mainline: META_AGENT_PRODUCT_BUILD
  source_repository_write: authorized_within_exact_task_scope
  destination_repository_write: prohibited
  migration_cutover: prohibited
  private_material: prohibited
```

Then proceed. Do not ask the user to repeat decisions already fixed by this taskbook.

## 3. Required preflight

Before substantive work or branch creation, verify at execution time:

```yaml
preflight:
  source_repository: 08822407d/Mnemosyne
  latest_master_sha:
  latest_master_contains_PR_255_merge: true
  minimum_baseline_is_ancestor_or_identical: true
  accessible_open_PRs: []
  exact_task_ID_or_branch_matches: []

  destination_repository: 08822407d/Meta-Agent
  accessible: true
  visibility: public
  commits: 0
  branches: []
  open_PRs: []

  target_truth:
    repository: 08822407d/Mnemosyne
    path: target-projects/meta-agent/current/approved-spec.md
    effective_for_operational_use: false

  authorization:
    source_Mnemosyne_write: true
    destination_write: false
    destination_initialization: false
    shadow_copy: false
    cutover: false
```

Stop and return `BLOCKED_STATE_CHANGED` if:

- the destination contains an unknown commit, branch or PR;
- another open PR overlaps Meta-Agent target-local state or migration paths;
- latest `master` does not contain PR #255;
- the destination is no longer public without an updated material-policy decision;
- target truth or operational status has changed;
- complete repository enumeration is unavailable.

## 4. Required reading order

Read the following separately and preserve their roles:

### 4.1 Meta-Agent truth and governance

1. `target-projects/meta-agent/current/approved-spec.md`
2. `target-projects/meta-agent/authority/source-and-owner-map.md`
3. `target-projects/meta-agent/methodology/core-methodology.md`
4. `target-projects/meta-agent/cases/case-and-feedback-ledger.md`
5. `target-projects/meta-agent/history/decision-version-and-migration-log.md`

### 4.2 Live state, compatibility and preservation

6. `target-projects/meta-agent/current/active-context.md`
7. `target-projects/meta-agent/handoff/handoff-current.md`
8. `target-projects/meta-agent/current/meta-agent-mnemosyne-guidance-compatibility-guard.md`
9. `target-projects/meta-agent/migration/pre-migration-preservation-checkpoint-2026-08-06.md`
10. `target-projects/meta-agent/migration/destination-access-verification-2026-08-06.md`
11. `target-projects/meta-agent/handoff/receipts/handoff-receive-report-2026-08-05.md`
12. PR #255 metadata and changed-path inventory

### 4.3 Mnemosyne migration and memory design

13. `notes/migration-designs/meta-agent-dedicated-repository-migration-assessment-v0.1.md`
14. `notes/validation-designs/target-project-dedicated-repository-migration-and-pr-validation-v0.1.md`
15. `notes/migration-designs/meta-agent-pre-migration-readiness-assessment-2026-08-06.md`
16. `notes/target-project-delivery-models/mnemosyne-to-dedicated-target-repository-operating-model-v0.1.md`
17. `notes/adjudications/meta-agent-pre-migration-receive-result-adjudication-2026-08-06.md`
18. `notes/memory-system-designs/meta-agent-initial-memory-system-design-v0.1.md`
19. `notes/validation-designs/meta-agent-initial-memory-system-adoption-and-validation-v0.1.md`

### 4.4 Research adjudication inputs, not raw-report default load

20. `target-projects/meta-agent/research/waves/2026Q3-independent-wave-001/reviews/MA-DR-08-15-cross-report-convergence-v0.1.md`
21. `target-projects/meta-agent/research/waves/2026Q3-independent-wave-001/reviews/MA-DR-11-formal-intake-review.md`
22. `target-projects/meta-agent/research/waves/2026Q3-independent-wave-001/reviews/MA-DR-13-formal-intake-review.md`

Read raw reports only when a specific disputed mapping or design claim cannot be resolved from the accepted review/candidate records. Record each raw-report access.

## 5. Repository lineage and exact write scope

Create one branch from execution-time latest `master`:

```text
meta-agent-dedicated-repository-migration-preparation-001
```

At most one canonical PR may be created. Before branch creation and immediately before PR creation, enumerate:

- all accessible open PRs;
- exact task-ID matches;
- intended branch matches;
- overlapping target-local migration/state paths.

Allowed write roots in Mnemosyne:

```text
target-projects/meta-agent/current/active-context.md
target-projects/meta-agent/handoff/handoff-current.md
target-projects/meta-agent/migration/
target-projects/meta-agent/decision-support/
target-projects/meta-agent/current/                     [new behavior guidance candidate only if kept clearly non-authoritative]
target-projects/meta-agent/commands/                    [candidate loader only if non-authoritative and not activated]
notes/codex-task-results/
```

Do not modify:

```text
target-projects/meta-agent/current/approved-spec.md
target-projects/meta-agent/authority/source-and-owner-map.md
target-projects/meta-agent/methodology/core-methodology.md
target-projects/meta-agent/cases/case-and-feedback-ledger.md
target-projects/meta-agent/history/decision-version-and-migration-log.md
current/human-approved-spec.md
08822407d/Meta-Agent (all paths)
```

A later Owner decision may authorize changes to protected target files; this task may not.

## 6. Workstream A — receive result binding and post-PR #255 closure

Create a target-local non-truth adjudication/receipt that preserves the full receive result or a content-identity-bound exact transfer and records the frontier adjudication.

Update `active-context.md` and `handoff-current.md` so current navigation reflects:

```yaml
PR_255:
  merged: true
  merge_commit: 9e60fef75c524fc2e8acf227e84eaa820f08bc59
preservation_branch_pending: false
preservation_PR_pending: false
migration_direction_selected: true
destination_initialized: false
recursive_manifest_status: pending_or_completed_by_this_task
safe_next_action: owner_review_of_mapping_and_initialization_decision_package
```

Rules:

- do not rewrite the preservation checkpoint's historical front matter;
- create a post-merge supersession/closeout record that points to the checkpoint and PR #255;
- do not create another self-referential “pending future PR” current-state loop;
- current navigation should require runtime verification of the actual latest repository state.

## 7. Workstream B — exhaustive recursive source manifest

Enumerate the complete Git tree under:

```text
target-projects/meta-agent/
```

at one pinned execution-time `master` commit.

### 7.1 Completeness requirement

Use a repository tree/blob mechanism capable of proving recursive completeness. Do not use:

- code search;
- semantic search;
- a hand-maintained folder list;
- sampled files;
- conversation memory;
- a generated summary without tree identity.

If complete recursive enumeration with blob identity is unavailable, stop with:

```text
BLOCKED_INCOMPLETE_REPOSITORY_ENUMERATION
```

### 7.2 Manifest fields

Every blob must receive one record:

```yaml
source_artifact:
  source_repository: 08822407d/Mnemosyne
  source_commit:
  source_path:
  git_blob_sha:
  bytes: observed_or_unknown
  artifact_id: present_or_none
  artifact_role:
  authority_class:
    - target_truth
    - owner_or_authority_support
    - current_state
    - handoff
    - approved_method
    - case_or_feedback_evidence
    - research_evidence
    - candidate
    - decision_or_migration_history
    - migration_control
    - derived_navigation
    - raw_transport
    - historical_failure_or_superseded
    - unknown_requires_review
  material_class:
    - public
    - synthetic
    - redacted
    - safe_pointer
    - unknown_requires_stop
  current_status:
  migration_zone:
  disposition:
    - preserve_exactly
    - transform
    - recompute
    - retire
    - historical_pointer_only
    - exclude_Mnemosyne_control_plane
    - blocked_pending_owner_decision
  destination_path_candidate:
  destination_authority_effect:
  source_refs_preserved:
  transform_or_validation_required:
  rationale:
```

### 7.3 Tree closure receipt

The manifest must include:

```yaml
tree_closure:
  root_path: target-projects/meta-agent/
  source_commit:
  recursive_tree_complete: true
  blob_count:
  tree_count:
  duplicate_paths: 0
  unmapped_paths:
  unknown_material_paths:
  manifest_sha256_or_git_blob_identity:
  verifier_relation:
```

Any unknown material class or unmapped path blocks later destination write.

## 8. Workstream C — migration zones

Classify every source artifact into exactly one primary zone:

```yaml
zones:
  Z1_TARGET_CORE:
    meaning: truth_authority_method_state_history_handoff_and_target_owned_behavior
    default: migrate_or_transform

  Z2_TARGET_EVIDENCE:
    meaning: research_cases_feedback_evaluations_and_exact_evidence_identity
    default: migrate_or_preserve_with_source_binding

  Z3_TARGET_CANDIDATES:
    meaning: unaccepted_designs_prototypes_and_pending_specs
    default: preserve_as_candidate_not_truth

  Z4_TARGET_MIGRATION_CONTROL:
    meaning: target_specific_mapping_receipts_rollback_and_destination_state
    default: migrate_or_regenerate

  Z5_MNEMOSYNE_BOOTSTRAP_AND_CONTROL:
    meaning: Mnemosyne_design_records_guards_status_and_task_results_outside_target_root
    default: remain_in_Mnemosyne_with_immutable_pointer

  Z6_HISTORICAL_FAILURE_OR_SUPERSEDED:
    meaning: failed_transports_stale_navigation_or_retired_artifacts
    default: minimal_status_or_pointer_preventing_resurrection
```

Do not copy Mnemosyne root maintenance state into the destination.

## 9. Workstream D — candidate destination mapping

Prepare at least these two complete mapping options:

### Option 1 — project-root flattening, recommended candidate

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

For each option report:

```yaml
mapping_option:
  path_rewrite_rules:
  files_preserved_byte_exact:
  files_transformed:
  cross_repo_links_to_update:
  behavior_guidance_effect:
  history_and_rollback_effect:
  fresh_session_load_cost:
  human_review_burden:
  advantages: []
  risks: []
  recommended: true_or_false
```

Recommendation may be provided, but the task must not silently select the Owner's destination root.

## 10. Workstream E — history strategy

Prepare a bounded comparison:

```yaml
snapshot_first:
  exact_source_commit_and_manifest: required
  Mnemosyne_history_pointer: required
  destination_per_file_history: begins_at_migration
  complexity: lower

filtered_subdirectory_history:
  exact_filter_tool_and_version: required
  branches_tags_and_refs_scope: explicit
  rewritten_path_validation: required
  complexity: higher

full_repository_mirror:
  recommendation: reject_for_project_separation
```

Default recommendation should remain snapshot-first unless measured value justifies filtered history. The Owner makes the final choice.

## 11. Workstream F — Meta-Agent-owned behavior guidance adoption matrix

Create a candidate matrix with one row per adopted, transformed or excluded behavior semantic.

Required source inputs:

```text
target-projects/meta-agent/current/meta-agent-mnemosyne-guidance-compatibility-guard.md
current/artifact-delivery-and-direct-generation-guard.md
current/cross-conversation-execution-intent-and-operator-flow-guard.md
current/external-research-display-name-guard.md
current/deep-research-report-delivery-correction-guard.md
current/user-operation-next-step-capability-and-intent-guard.md
current/github-single-active-pr-lineage-guard.md
current/run-context-and-pr-provenance-guard.md
commands/load-mnemosyne-guidance.md
```

Required matrix schema:

```yaml
behavior_semantic:
  source_ref:
  semantic_summary:
  relation:
    - adopt
    - adapt_for_Meta_Agent
    - exclude_Mnemosyne_specific
    - defer_pending_evidence_or_owner
  destination_guidance_section:
  target_authority_effect:
  blocking_validation_cases: []
  rationale:
```

Minimum semantics to address:

1. sole target truth and role separation;
2. objective evidence-bound engineering judgment;
3. operation section and visible next step;
4. model-capability and research-value classification;
5. file-first delivery and one canonical Deep Research report;
6. explicit external-task execution intent and dedicated operator flow;
7. `MA-DR-*` compact display-name allocation;
8. public/private/material-safety boundary;
9. platform permission versus task authorization;
10. one-task/one-branch/at-most-one-PR;
11. run context and PR provenance;
12. no automatic handoff or route import;
13. no automatic methodology promotion;
14. no exact-backend inference from visible selection or style.

Explicitly exclude:

- Mnemosyne maintenance current state, TODO, open questions and handoff;
- MNE-DR A1/A2 state;
- other target projects;
- Mnemosyne frontier-clarification architecture unless separately adopted for a Meta-Agent use case;
- automatic future propagation of Mnemosyne guard changes.

Candidate destination paths:

```text
current/meta-agent-behavior-guidance.md
commands/load-meta-agent-guidance.md
```

They remain candidate/non-active in this task.

## 12. Workstream G — initial memory-system alignment

Use the candidate design at:

```text
notes/memory-system-designs/meta-agent-initial-memory-system-design-v0.1.md
```

Do not automatically adopt it. Produce an alignment ledger:

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
    - adopt_during_migration
    - defer_until_post_migration
    - reject
    - revise
  rationale:
```

At minimum evaluate:

- existing truth/state/authority/method/case/history/handoff/research layers;
- Meta-Agent-owned behavior guidance;
- artifact-role registry;
- memory-object envelope for new records;
- hot/warm/cold load profiles;
- deterministic derived index;
- freshness/supersession rules;
- case-feedback-evaluation lifecycle;
- no hidden global user profile;
- future RAG trigger and source binding;
- validation and review-burden measurement.

The task should recommend which memory additions belong in the migration shadow PR and which should wait for a separate post-migration memory-system PR.

Default conservative recommendation:

```yaml
migration_shadow_PR:
  include:
    - existing_target_package
    - Meta_Agent_owned_behavior_guidance_candidate
    - migration_manifest_mapping_and_rollback
  defer:
    - nonessential_new_memory_schema_or_indexes
    - RAG_or_automation
```

Deviate only with explicit rationale and Owner decision package.

## 13. Workstream H — Owner decision package

Create a decision package that provides sufficient context and preserves free-form/reject-premise options.

Required decisions:

```yaml
owner_decisions:
  destination_visibility:
    observed_current: public
    decision: confirm_public | change_before_initialization | defer

  destination_root_layout:
    options:
      - flatten_to_project_root
      - preserve_target_projects_meta_agent_prefix
      - owner_defined

  history_strategy:
    options:
      - snapshot_first
      - filtered_subdirectory_history
      - defer

  initialization_actor_and_surface:
    options:
      - dedicated_Meta_Agent_conversation_write_capable_GitHub_surface
      - Codex
      - manual_human_commit
      - other

  initialization_exact_paths:
    recommended_minimum:
      - README.md
      - MIGRATION-STATUS.md

  behavior_guidance_adoption_scope:
    options:
      - adopt_recommended_minimum
      - review_each_semantic
      - defer

  initial_memory_system_scope:
    options:
      - migration_minimum_only
      - include_selected_memory_foundation
      - defer_all_new_memory_components_post_migration

  rollback_window:
  destination_initialization_authorized_now: yes_or_no
```

Each question must explain meaning, downstream effect, risk, deferral consequence, recommendation and a free-form response path.

## 14. Required deliverables

```text
target-projects/meta-agent/migration/post-PR255-preservation-closeout-2026-08-06.md
target-projects/meta-agent/migration/source-tree-manifest-<source-short-sha>.yaml
target-projects/meta-agent/migration/source-tree-manifest-verification-<source-short-sha>.md
target-projects/meta-agent/migration/source-to-destination-mapping-candidate-v0.1.md
target-projects/meta-agent/migration/behavior-guidance-adoption-matrix-v0.1.md
target-projects/meta-agent/migration/initial-memory-system-alignment-v0.1.md
target-projects/meta-agent/decision-support/dedicated-repository-initialization-owner-decision-package-v0.1.md
target-projects/meta-agent/current/active-context.md
target-projects/meta-agent/handoff/handoff-current.md
notes/codex-task-results/META-AGENT-DEDICATED-REPOSITORY-MIGRATION-PREPARATION-001-result.md
notes/codex-task-results/META-AGENT-DEDICATED-REPOSITORY-MIGRATION-PREPARATION-001-pr-finalization.md
```

If one YAML manifest exceeds the connected write surface's safe payload limit, use deterministic parts plus a manifest that records exact reconstruction order, bytes and hashes. Do not silently omit paths.

## 15. Validation before PR creation

```yaml
validation:
  source_commit_pinned: true
  complete_recursive_tree_proven: true
  every_blob_has_identity: true
  all_paths_classified: true
  unmapped_paths: 0_or_explicit_blocker
  unknown_material_paths: 0
  target_truth_unchanged: true
  approved_methodology_unchanged: true
  historical_checkpoint_not_rewritten: true
  live_navigation_current: true
  destination_writes: 0
  destination_repository_still_empty: true
  owner_decisions_not_defaulted: true
  one_branch_at_most_one_PR: true
```

An aggregate score cannot override a missing path, unknown material, authority conflict or destination write.

## 16. Final status semantics

```yaml
final_status:
  READY_FOR_OWNER_INITIALIZATION_DECISION:
    meaning: all_source_mapping_behavior_and_memory_preparation_complete_no_destination_write

  READY_WITH_EXPLICIT_BLOCKERS:
    meaning: complete_manifest_exists_but_named_owner_or_tool_decisions_remain

  BLOCKED_INCOMPLETE_REPOSITORY_ENUMERATION:
    meaning: complete_recursive_tree_or_blob_identity_not_provable

  BLOCKED_AUTHORITY_OR_MATERIAL_CONFLICT:
    meaning: unresolved_truth_privacy_owner_or_material_issue

  INVALID:
    meaning: wrong_context_destination_write_duplicate_PR_or_scope_contamination
```

## 17. Final response requirements

The final response must begin with the single PR review instruction if a PR was created, then report:

- execution-time source and destination state;
- final source tree counts and identity method;
- stale-state closure;
- mapping and behavior-guidance disposition;
- memory-system alignment recommendation;
- unresolved Owner decisions;
- explicit confirmation of zero destination writes;
- capability and research assessment;
- exactly one safe next action.

Do not include an instruction to initialize the destination unless the Owner has separately authorized it after reviewing the decision package.

## 18. Boundaries

This task does not authorize:

- a destination first commit;
- destination branch or PR creation;
- target-truth path change;
- migration cutover;
- operational activation;
- private material;
- prototype or pilot execution;
- RAG, MCP, auto-indexing or auto-writeback;
- automatic adoption of the initial memory-system candidate;
- automatic propagation of future Mnemosyne rules.
