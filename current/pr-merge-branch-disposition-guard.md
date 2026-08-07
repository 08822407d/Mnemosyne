# PR Merge and Post-Merge Branch Disposition Guard

> User-approved Mnemosyne behavior guard for making branch-retention requirements visible whenever a response asks the user to review or merge a pull request. This file is not a standalone execution source; `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
guard_id: MNEMOSYNE-PR-MERGE-BRANCH-DISPOSITION-001
created_by_task: MNEMOSYNE-196
status: active_after_MNEMOSYNE_196_merge
execution_source: current/human-approved-spec.md
execution_source_modified: false
applies_to:
  - Mnemosyne_conversations_that_ask_the_user_to_review_or_merge_a_repository_PR
  - Mnemosyne_repository_tasks
  - Mnemosyne_target_delivery_tasks_when_this_guard_is_explicitly_loaded
user_default:
  when_no_prominent_retention_instruction_is_given: branch_may_be_deleted_after_merge
```

## 1. Problem addressed

A PR may need its head branch retained after merge because another task, comparison, replay, external Agent, release process, post-merge verification, or rollback rehearsal still depends on the live branch ref. When that requirement is buried in analysis or omitted from the opening operation section, the user may reasonably delete the branch immediately after merging.

The Owner has established this default interpretation:

> If a Mnemosyne response asks the user to review or merge a PR and does not prominently state that the PR branch must be retained, the user may assume the branch can be deleted after merge.

Therefore branch retention is never an implicit requirement.

## 2. Mandatory branch-disposition declaration

Every user-facing response that asks the user to review or merge a PR must place a branch-disposition declaration in the opening operation section, next to the merge instruction.

Use this schema or a plain-language equivalent with the same semantics:

```yaml
post_merge_branch:
  branch:
  disposition:
    DELETE_ALLOWED |
    RETAIN_REQUIRED |
    RETAIN_UNTIL_GATE |
    UNKNOWN_BLOCKS_MERGE_INSTRUCTION
  reason:
  retain_until:
  deletion_allowed_after:
  user_action:
```

The compact merge instruction should include the same conclusion:

```yaml
merge_instruction:
  task_id:
  merge_target_pr:
  merge_target_head_branch:
  post_merge_branch_disposition:
  branch_retention_reason:
  branch_retention_until:
  deletion_allowed_after:
```

## 3. Prominence rule

When branch retention is required, the response must state it before long analysis in conspicuous language, for example:

```text
⚠ 合并后请保留分支 `<branch>`，暂时不要删除。
保留至：<exact gate/event>。
```

Requirements:

1. The instruction must appear in the opening `操作内容（需要你手动执行）` section.
2. It must name the exact branch.
3. It must explain why the branch is still required.
4. It must give an exact release gate or say that deletion remains blocked pending a named decision.
5. It must not be conveyed only in a PR body, repository file, closing `下一步`, parenthetical note, or long analysis paragraph.
6. If several PRs or branches are involved, state the disposition for each one separately.

## 4. Default deletion rule

Use `DELETE_ALLOWED` when the PR has merged and no verified post-merge workflow needs the live head ref.

Recommended wording:

```text
合并后可删除分支 `<branch>`；无需保留该分支。
```

A merged PR's commits remain in repository history even after normal branch deletion. However, this fact does not authorize deleting an unmerged branch or a branch with unique, unreviewed work.

If the response omits a prominent retention instruction, the Owner's default is `DELETE_ALLOWED` after merge.

## 5. Valid reasons to retain a branch

`RETAIN_REQUIRED` or `RETAIN_UNTIL_GATE` requires a concrete, verified dependency, such as:

- an external Agent or tool must read the exact branch ref before the change reaches `master`;
- a post-merge comparison or provenance check explicitly depends on the branch ref and cannot use immutable commits instead;
- a staged rollout, release, backport, or rollback rehearsal has an approved branch-based contract;
- unresolved parallel-lineage reconciliation requires the branch to remain available;
- a user-approved experiment names the branch as a required input;
- repository limitations make the branch the only available carrier of unique evidence not yet preserved elsewhere.

Vague caution, habit, or the possibility that the branch might be useful later is insufficient. Prefer immutable commit refs, merged history, saved artifacts, or tags when they remove the need to retain a working branch.

## 6. Pre-merge verification

Before issuing a merge instruction, inspect and record:

```yaml
branch_disposition_preflight:
  PR_state:
  PR_head_branch:
  PR_head_SHA:
  unique_or_unmerged_work_outside_PR:
  downstream_branch_ref_dependencies: []
  immutable_commit_or_artifact_substitute_available:
  retention_required:
  retention_gate:
  disposition:
```

Decision rules:

1. If no branch dependency exists, use `DELETE_ALLOWED`.
2. If a dependency exists and its release gate is known, use `RETAIN_UNTIL_GATE`.
3. If the branch must remain but the release gate is not yet known, use `RETAIN_REQUIRED` and name the blocking decision.
4. If branch state or downstream dependency cannot be established, use `UNKNOWN_BLOCKS_MERGE_INSTRUCTION`; do not ask the user to merge until clarified.
5. Do not claim that a branch must be retained merely because the assistant cannot remember whether it is needed; verify or block.

## 7. Post-merge follow-through

When a retained branch reaches its release gate, the responsible Mnemosyne response must prominently update the disposition:

```yaml
post_merge_branch_release:
  branch:
  previous_disposition:
  release_gate_satisfied:
  unique_unpreserved_work: false
  new_disposition: DELETE_ALLOWED
```

Do not leave an indefinite `retain` instruction active after its dependency is closed. If the branch remains by repository policy rather than task need, distinguish policy retention from a user-required action.

## 8. Result-record and PR-finalization requirements

Important repository-writing task records should include:

- the branch-disposition preflight;
- the user-facing branch disposition;
- any retention reason and release gate;
- whether an immutable commit or artifact can replace the branch;
- any later release-to-delete record.

PR finalization must not say only `merge this PR`; it must also say whether the head branch may be deleted after merge.

## 9. Relationship to other guards

This guard complements:

- `current/github-single-active-pr-lineage-guard.md` for canonical branch/PR selection;
- `current/cross-conversation-execution-intent-and-operator-flow-guard.md` for visible current actions;
- `current/run-context-and-pr-provenance-guard.md` for repository-action evidence;
- `current/user-operation-next-step-capability-and-intent-guard.md` for opening operation placement.

When rules conflict, the stricter fail-closed action applies. None of these guards authorizes merge or branch deletion.

## 10. Boundaries

This guard does not:

- authorize a PR merge, branch deletion, branch retention, tag creation, or repository write by itself;
- require branches to be retained after ordinary merged PRs;
- preserve unique unmerged work automatically;
- replace branch-protection rules or repository policy;
- make a branch an execution source, target truth, or authoritative artifact;
- apply automatically to a separate target project unless that project's Owner adopts it or a task explicitly loads it as a process constraint.
