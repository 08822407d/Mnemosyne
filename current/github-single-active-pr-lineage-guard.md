# GitHub Single-Active PR Lineage Guard

> User-approved Mnemosyne behavior guard for repository-writing tasks. This file is not a standalone execution source; `current/human-approved-spec.md` remains the only execution source. It operationalizes the GitHub write-authority and result-record requirements in §18.

```yaml
guard_id: MNEMOSYNE-GITHUB-SINGLE-ACTIVE-PR-LINEAGE-001
created_by_task: MNEMOSYNE-118
status: active_user_approved_behavior_guard
applies_to:
  - ordinary_ChatGPT_GitHub_app_repository_writes
  - Codex_repository_writes
  - future_Agent_repository_writes
execution_source: current/human-approved-spec.md
default_rule: one_task_id_one_canonical_write_branch_at_most_one_open_canonical_PR
parallel_PR_default: prohibited
```

## 1. Problem addressed

MNEMOSYNE-116 accidentally produced PR #163 and PR #164 as two parallel implementations of the same task from the same base. Only one PR was disclosed in the final merge instruction. The first PR was merged, the second then conflicted, and a reconciliation task was required.

The failure was not merely a merge-conflict problem. It was a write-lineage control failure:

- no final check established whether the same task already had an open PR;
- a second branch and PR were created instead of continuing the existing PR head branch;
- the user-facing response did not enumerate all related PRs;
- more than one plausible merge target existed at the same time.

## 2. Canonical write lineage

For each user-approved repository-writing task, define exactly one canonical lineage by default:

```yaml
canonical_write_lineage:
  task_id:
  base_branch:
  pinned_base_sha:
  canonical_branch:
  canonical_pr_number: null_or_integer
  scope_summary:
```

Default invariants:

1. One `task_id` has one canonical write branch.
2. One `task_id` has at most one open canonical PR.
3. New corrections for an already merged task use a new task ID unless the user explicitly approves an amendment/reuse.
4. A branch or PR created for one task must not silently become the canonical lineage of another task.

## 3. Mandatory preflight before branch creation

Before creating any repository-writing branch, the actor must perform and record a duplicate-lineage preflight:

```yaml
github_write_lineage_preflight:
  task_id:
  intended_scope_summary:
  default_branch:
  pinned_default_branch_sha:
  intended_branch:
  open_pr_enumeration:
    method:
    pagination_complete: true_or_false
    all_accessible_open_prs_checked: true_or_false
  matches:
    by_exact_task_id: []
    by_intended_head_branch: []
    by_equivalent_scope: []
    existing_result_records_or_task_artifacts: []
  decision: create_new_lineage | continue_existing_lineage | stop_and_reconcile | blocked_incomplete_enumeration | explicitly_approved_parallel_variant
```

Required checks:

- enumerate all accessible open PRs, completing pagination when the interface exposes pagination;
- search exact `task_id` in PR title/body and result-record paths;
- search the intended branch name;
- inspect semantically equivalent recent PR scope when task naming may differ;
- verify the latest default-branch SHA before the first write.

If complete accessible enumeration is unavailable, the actor must not claim that no duplicate exists. Default action is `blocked_incomplete_enumeration`; a new PR may proceed only under a new, explicit, task-local user exception that records the limitation and is not a future precedent.

## 4. Decision rules

### 4.1 No related open PR exists

Create the canonical branch once, from the pinned latest default branch. Record the branch name and base SHA in the result record.

### 4.2 A related open PR exists

Do not create a second branch or PR. Continue the existing PR by committing to its head branch, or stop and ask for a scope decision if the existing PR cannot safely carry the new change.

### 4.3 A related PR is already merged

Do not reuse the old task ID or silently reopen the merged lineage. Use a new follow-up task ID and a new branch from current default branch for any repair, amendment, or reconciliation, unless the user explicitly authorizes task-number reuse.

### 4.4 A related PR is closed but unmerged

Explicitly choose and record one of:

- reopen and continue the same PR;
- keep it closed and create a new follow-up task/branch;
- reconcile its useful changes into a new branch from current default branch.

Do not silently create a parallel replacement while leaving the relationship undisclosed.

## 5. Second preflight before PR creation

Immediately before creating a PR, repeat the open-PR enumeration and exact-head/task-ID checks. The PR may be created only if:

- no related open PR exists; or
- this branch is the already-designated canonical lineage; or
- an explicitly approved parallel variant is recorded.

The actor must record the recheck result and the exact head/base pair.

## 6. Parallel variants

A second active branch or PR for the same task is allowed only when the user explicitly approves parallel variants before creation.

The record must include:

```yaml
parallel_variant_authorization:
  approved: true
  approved_by:
  reason:
  variant_ids:
  scope_separation:
  canonicalization_plan:
  user_will_not_be_given_multiple_merge_targets: true
```

Every variant needs a distinct branch and variant ID. Before any merge instruction is shown to the user, the variants must be reconciled to exactly one canonical merge target, or all merge instructions must remain blocked.

## 7. Accidental duplicate handling

When an unapproved duplicate branch or PR is discovered:

1. stop further repository writes on all affected lineages;
2. enumerate every related branch and PR;
3. do not tell the user to merge any of them yet;
4. determine whether one lineage is already merged;
5. if none is merged, select one canonical PR and close/supersede the others, or create one clean reconciliation branch from latest default branch;
6. if one is merged, retain the merged state, close remaining duplicate PRs, and port only missing valid deltas through a new follow-up task from latest default branch;
7. verify final default-branch content mechanically.

Do not resolve the situation by asking the user to choose blindly between overlapping PRs or by recommending unconditional conflict resolution.

## 8. User-facing merge instruction gate

Before telling the user to merge a PR, the response must include a compact merge-target declaration:

```yaml
merge_instruction:
  task_id:
  merge_target_pr:
  merge_target_head_branch:
  related_open_prs: []
  closed_or_superseded_related_prs: []
  exactly_one_merge_target: true
  duplicate_preflight_completed: true
```

If more than one related open PR remains, or `exactly_one_merge_target` is false, the assistant must not issue a merge instruction.

## 9. Result-record requirements

Every important repository-writing task result must record:

- `task_id` and user authorization;
- pinned base branch and SHA;
- canonical branch;
- pre-branch duplicate-lineage preflight;
- pre-PR duplicate-lineage recheck;
- canonical PR number;
- all related PR numbers and states;
- whether parallel variants were approved;
- the single user-facing merge target;
- final comparison against default branch;
- any enumeration limitations or exceptions.

## 10. Mechanical basis

GitHub exposes open/closed PR state and filters for head/base branches, allowing a preflight to identify an existing PR for a candidate head branch. Once a PR is open, further changes can be added to that PR by committing to its head branch; a new PR is not required. Commit/ref comparison can then verify the intended branch range and changed files.

## 11. Boundaries

- This guard does not authorize repository writes, parallel PRs, merges, auto-merge, branch deletion, or task-number reuse.
- This guard does not introduce GitHub Actions or automatic enforcement.
- It does not make PR metadata or result records execution source.
- It does not replace user approval, platform permission, latest-default-branch checks, diff verification, or post-merge validation.
