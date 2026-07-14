# MNEMOSYNE-118 Result Record

```yaml
task_id: MNEMOSYNE-118
task_name: Add a single-active PR lineage guard and continue fresh-replay readiness work
task_type: user_approved_behavior_guidance_hardening_and_repository_write_lineage_control
action_actor: ChatGPT_GitHub_app
started_from:
  base_branch: master
  base_commit: 158453bd7c6c4ee16704783d0a7b14e3500786ed
  prerequisite_PR:
    number: 165
    merged: true
    merge_commit: 158453bd7c6c4ee16704783d0a7b14e3500786ed
branch: mnemosyne-118-single-active-pr-lineage-guard
canonical_pr_number: 166
user_decision_recorded: true
user_authorization_context:
  - design and add a reasonable effective Mnemosyne guidance rule to prevent the PR-163/PR-164 duplicate-parallel-PR failure mode
  - load Mnemosyne guidance in the current conversation
  - automatically continue the next planned work within valid task boundaries
execution_source_modified: false
behavior_guidance_modified: true
single_active_pr_guard_created: true
fresh_replay_package_modified: false
fresh_replay_executed: false
target_workspace_created: false
target_materials_ingested: false
target_repository_written: false
operational_build_started: false
additional_regression_formalized: false
FABLE5_GREENFIELD_track_resumed_or_taken_over: false
auto_merge_authorized: false
```

## Summary

MNEMOSYNE-118 addresses the operational failure that produced PR #163 and PR #164 as two parallel implementations of the same task. Existing Mnemosyne guidance already required fresh default-branch state and careful conflict handling, but it did not require a duplicate-PR search before branch creation, a second search before PR creation, continuation of an existing PR head branch, or a single disclosed merge target.

The task creates a user-approved single-active PR lineage guard, loads it through the Mnemosyne guidance-refresh workflow whenever branch/PR work is relevant, and adds startup/README wayfinding.

The current five-regression fresh-session replay remains a separate read-only test. MNEMOSYNE-118 verifies that its canonical v2 package and startup prompt are present on merged `master`, but does not execute the replay because this maintenance conversation is not a fresh isolated session.

## Official GitHub basis checked

GitHub official documentation confirms the mechanisms used by this guard:

- the pull-request listing API supports filtering by PR `state`, `head`, and `base`, with pagination controls;
- a PR's base branch is the destination and its head branch contains the proposed changes;
- after a PR is opened, additional changes can be added by committing to its head branch rather than creating another PR;
- commit/ref comparison exposes changed-file details for mechanical branch-range review.

These platform capabilities support a repository policy of checking for an existing related PR, continuing its head branch when appropriate, and comparing the final canonical branch to the base.

## Duplicate-lineage preflight before branch creation

```yaml
github_write_lineage_preflight:
  task_id: MNEMOSYNE-118
  intended_scope_summary: prevent_unapproved_parallel_PRs_and_enforce_one_user_merge_target
  default_branch: master
  pinned_default_branch_sha: 158453bd7c6c4ee16704783d0a7b14e3500786ed
  intended_branch: mnemosyne-118-single-active-pr-lineage-guard
  repository_visibility: public
  open_pr_enumeration:
    method: GitHub_search_prs_state_open
    requested_limit: 50
    observed_open_pr_count: 0
    pagination_limitation: none_observed_for_zero_result
  matches:
    by_exact_task_id: []
    by_intended_head_branch: []
    by_equivalent_scope: []
    existing_MNEMOSYNE_118_artifacts: []
  decision: create_new_lineage
```

## Duplicate-lineage recheck before PR creation

```yaml
github_write_lineage_recheck:
  task_id: MNEMOSYNE-118
  canonical_branch: mnemosyne-118-single-active-pr-lineage-guard
  open_pr_enumeration:
    method: GitHub_search_prs_state_open
    requested_limit: 100
    observed_open_pr_count: 0
  exact_task_or_head_search:
    matches: []
  parallel_variant_authorized: false
  decision: create_one_canonical_PR
```

## Post-creation uniqueness check

```yaml
github_write_lineage_post_creation_check:
  canonical_pr_number: 166
  canonical_head_branch: mnemosyne-118-single-active-pr-lineage-guard
  all_accessible_open_prs:
    - 166
  exact_task_id_matches:
    - 166
  other_related_open_prs: []
  parallel_variant_authorized: false
  exactly_one_canonical_open_PR: true
```

```yaml
merge_instruction:
  task_id: MNEMOSYNE-118
  merge_target_pr: 166
  merge_target_head_branch: mnemosyne-118-single-active-pr-lineage-guard
  related_open_prs: []
  closed_or_superseded_related_prs: []
  exactly_one_merge_target: true
  duplicate_preflight_completed: true
```

## Files created

- `current/github-single-active-pr-lineage-guard.md`
- `notes/codex-task-results/MNEMOSYNE-118-result.md`

## Files modified

- `README.md`
- `commands/load-mnemosyne-guidance.md`
- `handoff/startup-instructions.md`

## Guard behavior

The guard establishes:

- one task ID → one canonical write branch → at most one open canonical PR by default;
- complete accessible open-PR/task/head checks before branch creation and again before PR creation;
- continuation of an existing related PR head branch instead of silently creating another PR;
- a new follow-up task ID for repairs after a task's PR has merged, unless the user explicitly approves task-number reuse;
- explicit handling of closed/unmerged attempts;
- parallel variants only after prior explicit user approval and with a canonicalization plan;
- immediate write stop and reconciliation when an accidental duplicate appears;
- exactly one user-facing merge target, with all related open/closed/superseded PRs disclosed;
- mandatory result-record fields for preflight, lineage, related PRs, and merge instruction.

## Guidance refresh in this conversation

The current conversation read the required README, execution source, and guidance command, reported the required `mnemosyne_guidance_refresh` schema, preserved the current task, and did not start a new handoff or import an unrelated maintenance route.

## Fresh-replay readiness continuation

Verified on `master@158453bd7c6c4ee16704783d0a7b14e3500786ed`:

- canonical startup prompt exists: `handoff/meta-agent-regression-fresh-session-replay-startup-prompt.md`;
- canonical replay package exists: `handoff/meta-agent-regression-fresh-session-replay-package-v2.md`;
- the replay scope remains `REG-META-DRYRUN-001`, `002`, `004`, `005`, and `007`;
- primary surface remains Chat;
- preferred model remains GPT-5.6 Sol Pro with the highest available Chat reasoning;
- fallback remains GPT-5.6 Sol with the highest available Chat reasoning;
- repository and target-project writes remain prohibited;
- the tested fresh conversation may not close the final gate.

## Verification

```yaml
branch_compare_before_result_record:
  base: master@158453bd7c6c4ee16704783d0a7b14e3500786ed
  head: mnemosyne-118-single-active-pr-lineage-guard
  ahead_by: 4
  behind_by: 0
  changed_files:
    - README.md
    - commands/load-mnemosyne-guidance.md
    - current/github-single-active-pr-lineage-guard.md
    - handoff/startup-instructions.md

branch_compare_after_initial_result_record:
  ahead_by: 5
  behind_by: 0
  changed_files:
    - README.md
    - commands/load-mnemosyne-guidance.md
    - current/github-single-active-pr-lineage-guard.md
    - handoff/startup-instructions.md
    - notes/codex-task-results/MNEMOSYNE-118-result.md
```

This annotation updates only the result record on the existing canonical PR head branch. A final compare follows before the user-facing merge instruction.

## Known limitations

- The new guard is a user-approved behavior-guidance and operational-control file loaded by the Mnemosyne guidance command; `current/human-approved-spec.md` remains the sole execution source and was not modified by this task.
- The guard is not automatically enforced by GitHub Actions or repository rulesets.
- PR enumeration confidence depends on the accessible GitHub interface and pagination coverage; incomplete coverage blocks a uniqueness claim unless the user grants a new task-local exception.
- The independent five-regression fresh replay still requires a genuinely new Chat conversation.

## Boundary

MNEMOSYNE-118 does not authorize parallel PRs, merges, auto-merge, branch deletion, task-number reuse, target-project actions, Meta-Agent construction, automatic replay execution, global regression promotion, FABLE5-GREENFIELD continuation, or any repository write outside this task's canonical branch and documented files.
