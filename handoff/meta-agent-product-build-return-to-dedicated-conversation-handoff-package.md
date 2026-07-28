# Meta-Agent Product Build — Return to Dedicated Conversation Handoff Package

> Official repository-backed handoff for returning the Meta-Agent product-build route to the user's existing dedicated Meta-Agent conversation. This file is non-execution-source navigation and transfer evidence. It does not activate Meta-Agent v0.1, approve operational use, modify either execution source, authorize new target writes, or select a pilot case.

```yaml
handoff_id: META-AGENT-PRODUCT-BUILD-RETURN-HANDOFF-001
created_by_task: MNEMOSYNE-172
repository: 08822407d/Mnemosyne
prepared_from_master: b8d75150ea2058f0dc0ca88f5666bd95b4e8592e
source_M2_PR: 222
transfer_direction:
  from: current_Mnemosyne_maintenance_conversation
  to: existing_dedicated_Meta_Agent_build_conversation
transfer_effective: on_human_merge_of_canonical_MNEMOSYNE_172_PR
current_conversation_after_transfer: Mnemosyne_self_development_and_maintenance_only
Meta_Agent_operational_use_authorized: false
owner_acceptance_pending: true
```

## 1. Why this transfer is now appropriate

The dedicated Meta-Agent conversation was previously paused because Mnemosyne had not yet established a sufficiently explicit way to:

- preserve an early target design without treating it as final;
- keep original evidence, approved requirements, current state and derived artifacts separate;
- give authority-bearing objects stable identities;
- version the design from its first real target write;
- map later renames, splits, merges, replacements and retirements;
- validate semantic and authority preservation during upgrades;
- retain a previous-state reference and rollback path;
- allow future Mnemosyne, model and tool improvements to update the target through reviewed migration rather than silent overwrite.

That prerequisite is now materially satisfied at the **design and bootstrap-file level**.

```yaml
upgradeability_preparation:
  M0_requirements_and_authority: complete_merged_PR_221
  M1_workspace_safety_manifest_and_upgrade_profile: complete_merged_PR_221
  M2_seven_file_target_package: complete_merged_PR_222
  target_specific_upgrade_contract:
    id: META-AGENT-V0.1-UPGRADE-CONTRACT-001
    profile: standard
    design_time_result: PASS_FOR_TARGET_SPECIFIC_DESIGN_USE_PENDING_OWNER_ACCEPTANCE
  actual_real_migration_proven_easy: false
  operational_use_accepted: false
```

The target can therefore return to its dedicated conversation without requiring the Mnemosyne-maintenance conversation to remain the product-build owner.

## 2. Verified repository baseline

```yaml
verified_baseline:
  PR_221:
    purpose: accept_M0_and_M1
    merge_commit: 8ff567c6cd5020bd05e13034866825fdb6473f4a
  PR_222:
    purpose: construct_Meta_Agent_v0_1_seven_file_package
    merge_commit: b8d75150ea2058f0dc0ca88f5666bd95b4e8592e
    merged_at: 2026-07-28T07:49:02Z
  master_relation_to_PR_222_merge_commit_at_handoff_preparation: identical
  accessible_open_PRs_before_MNEMOSYNE_172_branch: []
```

The seven target files are present on `master`:

```text
target-projects/meta-agent/current/approved-spec.md
target-projects/meta-agent/current/active-context.md
target-projects/meta-agent/authority/source-and-owner-map.md
target-projects/meta-agent/methodology/core-methodology.md
target-projects/meta-agent/cases/case-and-feedback-ledger.md
target-projects/meta-agent/history/decision-version-and-migration-log.md
target-projects/meta-agent/handoff/handoff-current.md
```

No extra substantive target file was created by M2.

## 3. Current target authority state

```yaml
target_authority:
  owner: user
  designated_sole_runtime_truth_source:
    path: target-projects/meta-agent/current/approved-spec.md
    exists: true
    effective_for_operational_use: false
    owner_acceptance: pending
  Mnemosyne:
    role: design_archive_control_plane_and_bootstrap_host
    target_runtime_truth_source: false
  other_six_target_files:
    target_runtime_truth_source: false
```

The target spec is **proposed and designated**, not activated. The PR #222 merge created the files but did not silently turn them into an operational Agent.

## 4. What M0 accomplished

M0 established a bounded Meta-Agent v0.1 requirements and authority baseline:

- target identity: general-purpose Agent-design and methodology system;
- software engineering: heavy early incubation domain, not the entire identity;
- user: owner and final decision authority;
- stable confirmed requirement IDs `MA-REQ-0001` through `MA-REQ-0016`;
- pending requirement IDs `MA-PEND-0001` through `MA-PEND-0008`;
- explicit separation of confirmed, pending, unknown, unsupported and deferred/non-goal material;
- one designated future target truth-source path;
- conflict precedence and explicit update/supersession rules;
- prohibition on treating Mnemosyne, research, current context, handoff or newer model inference as a second target truth source.

M0 deliberately did not settle every long-term product surface, repository, private-storage, automation, learner, GPT Live, shared-memory or model-routing question.

## 5. What M1 accomplished

M1 established the build-start boundary:

```yaml
workspace:
  root: target-projects/meta-agent/
  repository: 08822407d/Mnemosyne
  visibility_treatment: public_risk
safe_input_default:
  - public
  - synthetic
  - explicitly_redacted_excerpt_with_manifest
  - safe_external_pointer
  - outside_git_for_private_or_large_originals
upgrade_profile: standard
initial_versions:
  design: 0.1.0
  schema: 0.1.0
  policy: 0.1.0
  delivery: 0.1.0
```

M1 also froze:

- the exact seven-file M2 allowlist;
- file roles and truth-source boundaries;
- stable-ID prefixes;
- migration/rollback expectations;
- stop conditions;
- prohibited material classes;
- next-tier versus frontier work split;
- the requirement to check or explicitly defer applicable high-severity findings from the separately owned non-FABLE health review before operational acceptance or broad target write.

## 6. What M2 accomplished

M2 created the first real Meta-Agent target package and passed the recorded design/build checks:

```yaml
M2_contents:
  confirmed_requirements: MA-REQ-0001_through_MA-REQ-0016
  pending_requirements: MA-PEND-0001_through_MA-PEND-0008
  methods: MA-METHOD-0001_through_MA-METHOD-0006
  decisions: MA-DEC-0001_through_MA-DEC-0006
  bootstrap_migration: MA-MIG-0001
  real_cases: 0
  real_feedback_records: 0
  real_evaluation_records: 0
  versions: 0.1.0
```

The package includes:

- one designated but inactive target truth source;
- an authority/source/owner map;
- a compact six-method library;
- an empty case and feedback ledger with a promotion gate;
- decision, version, migration and rollback history;
- current-state navigation;
- fresh-session handoff;
- explicit capability-aware work decomposition;
- no private target material, no reconstructed lost conversation and no fabricated real case.

## 7. Upgradeability mechanisms now present

The dedicated conversation may rely on the following as the current upgradeability baseline:

### Stable identity

```text
MA-REQ
MA-PEND
MA-DEC
MA-METHOD
MA-CASE
MA-FEEDBACK
MA-EVAL
MA-MIG
```

IDs must not be silently reused. Rename, split, merge, replacement and retirement require mapping.

### Version dimensions

```yaml
design_version: 0.1.0
schema_version: 0.1.0
policy_version: 0.1.0
delivery_version: 0.1.0
```

A later change must identify the dimensions it changes rather than incrementing an ambiguous single version.

### Authority preservation

The system separates:

- raw/source evidence;
- approved target requirements and decisions;
- target execution source;
- current operational state;
- handoff/navigation;
- research evidence;
- model-generated or derived projections.

A stronger future model may recompute candidates and derived views, but it cannot silently rewrite confirmed requirements or owner decisions.

### Migration mapping

Future breaking, authority, privacy or platform changes must record old-to-new relations such as:

```text
unchanged
renamed
moved
reformatted
superseded
split_into
merged_from
replaced_by
retired
recomputed_from
unmappable_requires_human_review
```

### Preserve / transform / recompute / retire

Raw evidence and confirmed authority are normally preserved. Current state may be transformed with freshness checks. Summaries, indexes and embeddings should be recomputed where practical. Ephemeral scratch may be retired unless promoted through review.

### Rollback

- before merge: close or replace the single canonical PR;
- after merge but before operational activation: revert or supersede with a reviewed revision;
- after activation: use an owner-approved `MA-MIG-*` record, validation and rollback plan.

Public Git history cannot be promised erased.

### Replaceable implementation layers

v0.1 deliberately has no RAG, MCP, vector store, automated index, automated writeback, event-sourced runtime, dual-write or shadow cutover. Those can be added later only when target-specific evidence justifies them.

## 8. What remains unproven or incomplete

The transfer must not overstate current maturity.

```yaml
not_yet_proven_or_complete:
  Meta_Agent_operationally_effective: false
  owner_acceptance: pending
  production_ready: false
  real_project_cases: 0
  real_feedback_records: 0
  real_evaluation_records: 0
  real_migration_cost_or_success: untested
  next_tier_executor_rework_rate: unmeasured
  fresh_session_operational_replay_of_v0_1: not_run
  private_material_store: not_configured
  dedicated_external_repository: not_selected
  final_product_surface: pending
  learner_GPT_Live_shared_memory_modules: not_implemented
  advanced_automation_RAG_MCP: not_implemented
  health_review_high_severity_findings: not_found_as_canonical_result_at_handoff_preparation
```

The upgrade contract makes later changes more bounded and traceable; it does not make them automatic, costless or guaranteed correct.

## 9. Route ownership after transfer

```yaml
route_ownership_after_handoff_merge:
  Meta_Agent_product_build:
    owner_conversation: existing_dedicated_Meta_Agent_conversation
    current_stage: owner_review_and_disposition
    operational_activation: pending
  current_conversation:
    owner_role: Mnemosyne_maintainer
    Meta_Agent_product_work: excluded_unless_user_explicitly_reassigns
    automatic_Meta_Agent_continuation: false
  non_FABLE_health_review:
    owner: its_existing_separate_conversation
    takeover_by_either_route: prohibited
```

The dedicated conversation may use the latest repository state. It must not infer authority from its old conversation memory or restart completed M0/M1/M2 work.

## 10. Mandatory read order for the dedicated conversation

Read separately and preserve each role:

1. `handoff/meta-agent-product-build-return-to-dedicated-conversation-handoff-package.md` — this transfer package.
2. `handoff/meta-agent-product-build-return-to-dedicated-conversation-startup-prompt.md` — receive protocol.
3. `target-projects/meta-agent/handoff/handoff-current.md` — target-local handoff/navigation.
4. `target-projects/meta-agent/current/approved-spec.md` — designated target truth; confirm it remains inactive.
5. `target-projects/meta-agent/authority/source-and-owner-map.md` — owner, source, material and write authority.
6. `target-projects/meta-agent/current/active-context.md` — current state, blockers and safe next action.
7. `target-projects/meta-agent/methodology/core-methodology.md` — proposed method library.
8. `target-projects/meta-agent/history/decision-version-and-migration-log.md` — decisions, versions, migration and rollback.
9. `target-projects/meta-agent/cases/case-and-feedback-ledger.md` — empty evidence/candidate ledger.
10. `current/meta-agent-product-build-status.md` — Mnemosyne-side route status.
11. `current/first-target-minimum-upgrade-contract-status.md` — advisory-pilot status.
12. `notes/first-target-project-intake-records/meta-agent/meta-agent-v0.1-M0-requirements-and-authority-baseline.md`.
13. `notes/first-target-project-intake-records/meta-agent/meta-agent-v0.1-M1-workspace-safety-build-manifest.md`.
14. `notes/codex-task-results/MNEMOSYNE-171-result.md` and `MNEMOSYNE-171-pr-finalization.md` — M2 evidence and canonical lineage.

Do not load all historical Meta-Agent records unless a conflict, source question or audit need requires them.

## 11. How to use the existing dedicated conversation's old context

The existing dedicated conversation may contain valuable earlier design reasoning, but that context predates M0/M1/M2 and may be stale.

```yaml
old_conversation_context_policy:
  role: historical_or_candidate_evidence
  authority: not_target_truth
  automatic_merge_into_v0_1: prohibited
  required_handling:
    - compare_against_latest_repository_baseline
    - identify_conflicts_or_missing_source
    - label_uncommitted_ideas_as_candidate_or_unknown
    - ask_user_before_promoting_any_material
    - never_reconstruct_missing_originals_as_fact
```

The dedicated conversation should not discard its prior work, but it must re-anchor itself to the repository-backed target package.

## 12. Receive sequence

The handoff is intentionally staged.

### Operation 1 — Receive and stop

The user supplies the startup prompt in the existing dedicated conversation. The receiver:

- verifies latest `master` and the handoff merge;
- reads the mandatory first-layer files;
- reports loaded/missing/conflicting sources;
- confirms the target spec remains inactive;
- confirms no write or owner disposition was performed;
- stops.

### Operation 2 — Separate Mnemosyne guidance refresh

For this bootstrap owner-review task only, the user may separately instruct:

```text
加载 Mnemosyne 约束指导，但只作为 Meta-Agent bootstrap 审阅和仓库操作的流程／安全约束刷新；不要导入 Mnemosyne maintenance route，不要把 Mnemosyne 指导当作 Meta-Agent target truth。
```

This task-local choice does not resolve `HO-GUIDANCE-001` for future ordinary Meta-Agent operation.

### Operation 3 — Substantive owner review

Only after the receive report and any separate guidance refresh should the user instruct the dedicated conversation to review the v0.1 package and prepare a disposition.

## 13. Immediate substantive next task in the dedicated conversation

The next product-build task is **owner review and disposition**, not more construction.

```yaml
allowed_owner_dispositions:
  ACCEPT_V0_1_FOR_BOUNDED_OPERATIONAL_PILOT:
    meaning: approve_a_narrow_public_or_synthetic_pilot_after_activation_patch_and_required_checks
  ACCEPT_WITH_LIMITATIONS:
    meaning: approve_only_after_explicit_limitations_and_required_target_revision
  REQUEST_REVISION:
    meaning: keep_v0_1_inactive_and_prepare_a_reviewed_revision
  REJECT_AND_ROLL_BACK:
    meaning: do_not_activate_and_apply_the_recorded_revert_or_supersession_route
```

The dedicated conversation must not infer the user's disposition from PR #222 merge.

## 14. Preconditions before bounded operational activation

Before recommending `ACCEPT_V0_1_FOR_BOUNDED_OPERATIONAL_PILOT`, the dedicated conversation should:

1. verify all seven files on latest `master`;
2. perform substantive owner-oriented review, not only mechanical checks;
3. check again for a canonical non-FABLE health-review result and applicable P0/P1-equivalent findings;
4. incorporate applicable high-severity findings or record explicit deferral and residual risk;
5. verify the first pilot uses only public, synthetic, explicitly redacted or safe-pointer material;
6. define one bounded pilot case and exact write scope;
7. define evaluation, stop and rollback criteria;
8. require a fresh task-local repository action context for any activation or pilot write;
9. keep `target-projects/meta-agent/current/approved-spec.md` inactive until the activation change is human-merged and owner-accepted.

## 15. Recommended first bounded pilot after activation

This is a recommendation, not an approved pilot manifest:

- one public or synthetic Agent-design request;
- no private user material;
- no automatic tool execution or target-repository write;
- compare a single-Agent, workflow and multi-Agent option when relevant;
- exercise all six initial method objects;
- record one scoped case, feedback record and evaluation only under an approved manifest;
- test fresh-session recovery;
- observe next-tier executor usability and frontier-escalation behavior;
- record upgrade-contract burden and value;
- do not promote case lessons into core methodology automatically.

## 16. Future upgrade flow

When Mnemosyne, models, tools or requirements improve, the target should use:

```text
new_evidence_or_Mnemosyne_improvement
  -> target_specific_change_candidate
  -> authority_and_scope_review
  -> version_and_change_class_decision
  -> MA-MIG mapping when required
  -> validation_and_rollback_plan
  -> owner decision
  -> bounded target update
  -> post_change evaluation
```

Mnemosyne improvements do not automatically overwrite Meta-Agent. The dedicated conversation should request a reviewed migration package when a relevant Mnemosyne change is available.

## 17. Concurrency and task-number guard

- Verify latest `master` and enumerate all accessible open PRs before any write.
- Do not assume the next global Mnemosyne task number; allocate a fresh task ID after checking repository state because the Mnemosyne-maintenance conversation may continue in parallel.
- Use one canonical branch and at most one merge target for a bounded Meta-Agent task.
- Avoid modifying mixed global Mnemosyne wayfinding files unless a separate integration task explicitly authorizes it.
- Prefer target-local files and `current/meta-agent-product-build-status.md` for Meta-Agent route state.
- Do not modify `current/human-approved-spec.md` as part of Meta-Agent target work.

## 18. Hard prohibitions

The dedicated conversation must not:

- claim v0.1 is already operational;
- treat PR #222 merge as owner acceptance;
- repeat M0, M1 or M2 as though they were unfinished;
- make the old dedicated-conversation context authoritative;
- ingest private or raw target material;
- activate or modify the target spec without explicit task-local authorization;
- make Mnemosyne a second target truth source;
- create RAG, MCP, auto-writeback, shared memory, learner profile or GPT Live modules without separate approved routes;
- take over the non-FABLE health-review route;
- promote a case or feedback item into general methodology automatically;
- infer the exact served backend from UI labels, speed, style or model self-report.

## 19. Transfer completion condition

```yaml
transfer_complete_when:
  - canonical_MNEMOSYNE_172_PR_is_human_merged
  - dedicated_conversation_receives_the_package
  - receiver_reports_latest_baseline_and_inactive_truth_status
  - current_conversation_ceases_Meta_Agent_product_build_actions
```

No owner disposition or operational activation is required for the transfer itself to be complete.
