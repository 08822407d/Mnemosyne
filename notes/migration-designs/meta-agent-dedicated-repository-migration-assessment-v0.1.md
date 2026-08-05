# Meta-Agent Dedicated Repository Migration Assessment v0.1

> Mnemosyne-maintenance assessment only. It evaluates how a future Meta-Agent move could preserve authority, behavior, history, and repository operations. It does not select a destination repository, change Meta-Agent target truth, perform a copy/cutover, or take over the Meta-Agent product route.

```yaml
assessment_id: MNEMOSYNE-META-AGENT-DEDICATED-REPOSITORY-MIGRATION-ASSESSMENT-001
created_by_task: MNEMOSYNE-189
status: PREPARE_AND_VALIDATE_BEFORE_CUTOVER
repository: 08822407d/Mnemosyne
source_master: ca0926a9d67f10e60d8e97373370daa792c6eacb
Meta_Agent_route_owner: dedicated_Meta_Agent_conversation
execution_source_modified: false
Meta_Agent_target_truth_modified: false
migration_selected: false
new_repository_created: false
```

## 1. Question and decision boundary

This assessment addresses:

1. what must move if Meta-Agent receives a dedicated repository;
2. how to notify a fresh or existing Meta-Agent conversation after cutover;
3. how to preserve the process/safety behavior Meta-Agent currently borrows from Mnemosyne;
4. how to prevent two competing truth sources or writers;
5. how to test whether Mnemosyne-based conversations can deliver target-owned content and open PRs directly in target repositories.

It does not decide:

- the destination repository name or visibility;
- whether migration should occur immediately;
- operational activation, pilot scope, private-material capability, or methodology promotion;
- whether a generic ChatGPT GitHub app, Codex, or this conversation's write-capable GitHub action surface is the permanent writer.

## 2. Current verified state

Meta-Agent currently uses:

```yaml
physical_location: 08822407d/Mnemosyne/target-projects/meta-agent/
sole_designated_target_truth: target-projects/meta-agent/current/approved-spec.md
target_truth_effective_for_operational_use: false
route: META_AGENT_PRODUCT_BUILD
handoff_status: READY_FOR_RECEIVE_ONLY_HANDOFF
```

The target truth remains inactive. The current handoff directs a new Meta-Agent conversation to recover from the target-local spec, authority map, active context, methodology, history, research records, and dedicated handoff package.

A temporary compatibility guard already states that Mnemosyne guidance is only a process/repository-safety layer until Meta-Agent moves to a dedicated repository and adopts its own owner-approved behavior guidance. Migration review is therefore an expected future gate, not an invented new concern.

## 3. Evidence-based migration posture

The accepted MA-DR-13 review says dedicated-repository migration should be triggered by measurable access/visibility mismatch, independent release/CI, disaster-recovery, churn/conflict, operational ownership, or product-handoff needs. Repository tidiness alone is insufficient.

Current evidence now supports a **preparation and validation gate**, but not an immediate cutover:

```yaml
signals_present:
  - dedicated_repository_is_an_existing_pending_requirement_MA_PEND_0002
  - target_workspace_has_grown_beyond_the_original_seven_file_bootstrap
  - Meta_Agent_has_its_own_research_wave_handoff_and_route_lifecycle
  - temporary_Mnemosyne_guidance_compatibility_guard_has_an_explicit_migration_review_trigger
  - repeated_Meta_Agent_PRs_share_Mnemosyne_issue_and_PR_numbering_and_review_surface
  - user_now_requests_dedicated_repository_migration_evaluation

signals_not_yet_established:
  - destination_repository_identity_and_visibility
  - independent_release_or_runtime_selected
  - measured_clone_search_or_repository_health_failure
  - dedicated_CI_secrets_or_backup_requirements
  - approved_cross_repository_writer_surface
  - owner_cutover_decision
```

Recommended current disposition:

```yaml
disposition: PREPARE_MIGRATION_PACKAGE_AND_RUN_SYNTHETIC_DRY_RUNS
immediate_copy_or_cutover: false
```

## 4. Migration class and authority impact

The existing Meta-Agent migration log classifies a storage/runtime-platform move as Class 4 and requires:

- data and authority mapping;
- export and recovery;
- staged validation;
- no dual truth;
- rollback.

A repository move also changes the physical path of the designated truth source. Even if its semantic content is unchanged, activation of the new path is an Owner-controlled target-truth location decision.

```yaml
cutover_authority:
  owner_decision_required: true
  target_truth_path_change_record_required: true
  MA_MIG_record_required: true
  old_to_new_mapping_required: true
  validation_required: true
  rollback_required: true
  simultaneous_active_truth_sources: prohibited
```

## 5. Candidate destination layout

No repository name is selected. A candidate root layout is:

```text
<NEW_META_AGENT_REPOSITORY>/
├── README.md
├── current/
│   ├── approved-spec.md
│   ├── active-context.md
│   ├── meta-agent-behavior-guidance.md
│   └── ...
├── authority/
│   └── source-and-owner-map.md
├── methodology/
│   └── core-methodology.md
├── cases/
│   └── case-and-feedback-ledger.md
├── history/
│   └── decision-version-and-migration-log.md
├── handoff/
│   ├── handoff-current.md
│   └── dedicated migration handoff/startup artifacts
├── research/
├── decision-support/
├── notes/
└── commands/
    └── load-meta-agent-guidance.md
```

Candidate path mapping:

| Old Mnemosyne path | Candidate destination path | Default treatment |
|---|---|---|
| `target-projects/meta-agent/current/approved-spec.md` | `current/approved-spec.md` | preserve content; path change requires Owner cutover |
| `target-projects/meta-agent/current/active-context.md` | `current/active-context.md` | regenerate current state after copy validation |
| `target-projects/meta-agent/authority/` | `authority/` | preserve |
| `target-projects/meta-agent/methodology/` | `methodology/` | preserve |
| `target-projects/meta-agent/cases/` | `cases/` | preserve |
| `target-projects/meta-agent/history/` | `history/` | preserve and append new `MA-MIG-*` |
| `target-projects/meta-agent/handoff/` | `handoff/` | preserve history; regenerate active handoff |
| `target-projects/meta-agent/research/` | `research/` | preserve exact report identities and reviews |
| `target-projects/meta-agent/decision-support/` | `decision-support/` | preserve as non-truth support |
| temporary compatibility guard | destination behavior guidance + old historical bridge | transform, validate, then retire compatibility mode |

The destination root may retain the `target-projects/meta-agent/` prefix instead, but that would preserve bootstrap nesting rather than simplify project-local paths. The final path mapping is an Owner decision and must be frozen before copy.

## 6. What should be copied, referenced, recomputed, or retired

```yaml
preserve_exactly:
  - approved_spec_and_stable_ID_objects
  - authority_source_map
  - methodology
  - cases_and_feedback_ledger
  - decision_version_migration_history
  - accepted_research_originals_identities_and_reviews
  - owner_decisions_and_source_refs

transform_or_regenerate:
  - active_context
  - handoff_current
  - repository_specific_paths_and_links
  - repository_action_context_templates
  - startup_prompt
  - behavior_guidance_loader
  - derived_indexes_or_navigation

retain_in_Mnemosyne_as_history_or_pointer:
  - original_bootstrap_and_Mnemosyne_design_records
  - migration_manifest_and_validation_result
  - old_target_path_tombstone_with_last_authoritative_commit
  - immutable_destination_repository_and_cutover_ref

retire_after_cutover:
  - old_path_as_active_writer
  - temporary_live_dependency_on_Mnemosyne_guidance
  - any_dual_write_or_live_mirror
```

Private material remains outside Git unless separately approved. Migration does not make previous public Git history disappear.

## 7. History transfer options

### Option A — exact snapshot plus source manifest

Copy the selected target tree at one pinned Mnemosyne commit, preserving:

- every path;
- byte/hash identity;
- source commit;
- role and authority;
- old-to-new mapping.

Keep Mnemosyne as the historical design archive. This is the simplest and lowest-risk bootstrap cutover because authority depends on explicit migration records, not on reproducing every historical commit in the destination.

### Option B — filtered subdirectory history

Create a filtered history containing only `target-projects/meta-agent/`, optionally rewriting that prefix to repository root. This preserves more Git lineage but requires a trusted history-filtering tool, full ref/tag decisions, and stronger verification.

### Option C — mirror the entire Mnemosyne repository

Not recommended for this purpose. A Git mirror preserves the whole repository, but it does not separate Meta-Agent from unrelated Mnemosyne history or authority.

GitHub documents mirror cloning/pushing as a way to duplicate an entire repository. A subdirectory split requires additional filtering not provided by the simple mirror procedure. Source: https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository

Recommended initial choice:

```yaml
recommended_history_strategy: OPTION_A_EXACT_SNAPSHOT_WITH_IMMUTABLE_MNEMOSYNE_HISTORY_POINTER
optional_upgrade: OPTION_B_ONLY_IF_PER_FILE_COMMIT_HISTORY_HAS_MEASURED_VALUE
```

## 8. Behavior preservation after migration

Behavior should remain semantically equivalent, but Meta-Agent should no longer depend on Mnemosyne's live maintenance guidance.

### 8.1 Preserve as Meta-Agent-owned guidance

The destination repository should adopt an Owner-reviewed `current/meta-agent-behavior-guidance.md` and `commands/load-meta-agent-guidance.md` covering the subset currently used through the compatibility guard:

1. Meta-Agent target truth and authority separation;
2. objective, evidence-bound engineering style;
3. opening user-operation section and closing next-step section;
4. capability-tier and research-need assessment;
5. file-first artifact delivery and Deep Research single-report semantics;
6. explicit cross-conversation execution intent and dedicated operator flow;
7. compact external research display names (`MA-DR-*`);
8. repository visibility, material safety, and private-original boundaries;
9. one-task/one-branch/at-most-one-PR lineage;
10. run context and PR provenance;
11. no route import, no automatic handoff, and no permission-as-authority;
12. target-local clarification or validation rules only when separately adopted by the Meta-Agent Owner.

### 8.2 Do not automatically import

Do not copy as active Meta-Agent behavior merely because it exists in Mnemosyne:

- Mnemosyne maintenance `current/active-context.md`, `todo`, `open-questions`, or handoff;
- Mnemosyne-specific Fable A1/A2 state;
- the frontier-clarification architecture as Meta-Agent truth;
- other target projects;
- future Mnemosyne guard changes without an explicit Meta-Agent adoption decision.

### 8.3 Versioned compatibility snapshot

The migration package should record:

```yaml
behavior_compatibility_snapshot:
  source_repository: 08822407d/Mnemosyne
  source_commit:
  source_guard_paths: []
  adopted_semantics: []
  excluded_Mnemosyne_specific_semantics: []
  destination_guidance_path:
  validation_ref:
  owner_decision_ref:
```

After cutover, Mnemosyne guidance changes become candidate upstream deltas. They do not silently update Meta-Agent.

## 9. How to notify Meta-Agent after migration

Use a **receive-only migration handoff** in the destination repository plus a historical redirect in Mnemosyne.

The first message to the Meta-Agent conversation should provide only the destination repository and startup-prompt path, then require a structured receive report and stop.

The handoff must state:

```yaml
migration_notification_required_fields:
  migration_ID:
  old_repository_and_last_authoritative_ref:
  new_repository_and_candidate_or_active_ref:
  old_truth_path:
  new_truth_path:
  authority_cutover_status:
  copy_validation_status:
  behavior_guidance_path:
  behavior_snapshot_source_refs: []
  active_context_path:
  handoff_path:
  startup_prompt_path:
  old_path_disposition:
  no_dual_writer_status:
  rollback_window_and_trigger:
  operational_activation_status:
  private_material_status:
  safe_next_action:
```

The receive report must verify, rather than assume:

- the destination repository is accessible;
- the expected commit and paths exist;
- exact truth-source role and activation state;
- old path is historical/non-active after cutover;
- behavior guidance loads without importing Mnemosyne maintenance;
- no related open PR or stale migration branch exists;
- no pilot, prototype, private material, or activation was implicitly authorized.

## 10. Cutover protocol

```text
freeze source scope and latest commit
  -> inventory/classify every target artifact
  -> freeze old-to-new path mapping
  -> create destination as shadow/non-authoritative
  -> copy and hash-verify
  -> install destination behavior guidance and startup/handoff
  -> run read-only fresh-session recovery tests
  -> run target-repository PR capability test with synthetic material
  -> run rollback and no-dual-writer rehearsal
  -> Owner cutover decision
  -> activate exactly one destination truth/write route
  -> tombstone old path in Mnemosyne
  -> regenerate current context/handoff/derived views
  -> verify no dual writer and retain rollback window
```

Copy is not cutover. During shadow validation, the original Mnemosyne path remains authoritative and the destination must be labelled non-authoritative.

## 11. Can Mnemosyne-based conversations write target repositories and create PRs?

The answer is **surface-dependent and must be validated**.

Current official OpenAI documentation says the standard ChatGPT GitHub app is read-only; Codex can edit repositories and propose/open pull requests. This conversation's installed `@GitHub` action surface has independently demonstrated branch/file/PR writes to Mnemosyne, but that does not prove generic ChatGPT GitHub sync or every future target repository has the same permission. Sources:

- https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt
- https://openai.com/index/introducing-codex/

A target-repository write requires all of:

```yaml
cross_repository_write_gate:
  exact_product_surface_identified: true
  destination_repository_exists: true
  destination_access_and_permission_verified: true
  task_local_authorization: true
  source_Mnemosyne_ref_pinned: true
  destination_base_ref_pinned: true
  exact_destination_path_allowlist: true
  source_repository_write_prohibited_unless_separately_authorized: true
  one_destination_branch: true
  at_most_one_destination_PR: true
  before_after_refs_and_changed_paths_observable: true
```

If the standard read-only GitHub app is the only available surface, use Codex or another explicitly write-capable surface for destination PR creation.

## 12. Generic target-project delivery model

For future specific-demand Agents, Mnemosyne should support two modes:

### Bootstrap-host mode

Use `target-projects/<id>/` temporarily when the target repository does not yet exist or the design is not ready for cutover.

### Direct target-repository mode

Once a target repository exists and passes capability tests:

- target-owned runtime truth and live state are written directly to the target repository;
- Mnemosyne retains design records, migration/delivery manifests, safe evidence, and immutable pointers;
- target changes use the target repository's branch/PR lineage;
- Mnemosyne does not keep a live duplicate truth tree.

The target repository may use its own behavior guidance or an explicitly versioned/adopted Mnemosyne-derived package. Sharing a GitHub account or connector does not merge project authority.

## 13. Decision gates

```yaml
Gate_0_owner_scope:
  decide:
    - destination_repository_name_owner_visibility
    - path_mapping
    - history_strategy
    - behavior_guidance_adoption_scope

Gate_1_shadow_copy:
  requires:
    - exact_inventory
    - source_ref_and_hashes
    - destination_non_authoritative_label

Gate_2_read_only_recovery:
  requires:
    - fresh_session_recovers_truth_authority_state_and_handoff
    - behavior_equivalence_tests_pass

Gate_3_repository_write_capability:
  requires:
    - synthetic_target_PR_test_passes
    - no_source_repo_write
    - exact_diff_and_PR_observability

Gate_4_cutover:
  owner_only: true
  requires:
    - no_unresolved_blocker
    - rollback_test
    - tombstone_plan
    - no_dual_writer
```

## 14. Recommendation

```yaml
recommendation:
  now:
    - adopt_display_name_guard
    - preserve_this_assessment_and_validation_design
    - do_not_create_or_cut_over_repository_in_MNEMOSYNE_189
  next_when_selected:
    - create_a_dedicated_migration_preparation_task_in_the_Meta_Agent_route
    - choose_destination_and_run_synthetic_cross_repo_validation
  migration_decision:
    status: NOT_YET_SELECTED
    likely_value: increasing_but_requires_owner_and_empirical_gates
```

No additional broad research is required before preparing a bounded migration package. A final cutover decision should use frontier reasoning plus mechanical evidence from the dry runs.
