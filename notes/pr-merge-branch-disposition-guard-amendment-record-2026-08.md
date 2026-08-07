# PR Branch-Retention Guard — Retention-Only Notice Amendment

```yaml
record_id: MNEMOSYNE-PR-BRANCH-RETENTION-NOTICE-AMENDMENT-001
created_by_task: MNEMOSYNE-197
status: adopted_on_human_merge_of_MNEMOSYNE_197_PR
source_guard: current/pr-merge-branch-disposition-guard.md
execution_source_modified: false
owner_instruction: current_conversation_2026_08_after_PR_263_merge
```

## 1. Owner decision

The Owner amended the branch-disposition behavior adopted by MNEMOSYNE-196:

```yaml
before:
  every_PR_merge_instruction_showed_DELETE_ALLOWED_or_RETENTION

after:
  no_retention_dependency:
    user_facing_notice: omitted
    Owner_default: branch_may_be_deleted_after_merge

  retention_dependency:
    user_facing_notice: prominent_and_required

  prior_retention_dependency_ends:
    user_facing_release_notice: explicit_and_required
```

The intent is to avoid repetitive ordinary deletion notices while preventing branches previously marked for temporary retention from becoming stale indefinitely.

## 2. Required semantics

### Ordinary PR branch

When no verified workflow needs the live head branch after merge:

- the response asks the user to review/merge the PR without discussing branch deletion;
- silence means the branch may be deleted after merge;
- internal task records may still state `SILENT_DEFAULT_DELETE_AFTER_MERGE`.

### Retained branch

When a verified dependency requires the live branch:

- the opening operation section must say `合并后请保留分支`;
- it must name the branch, reason, responsible route/task, and release gate;
- a durable retention obligation must be recorded if the branch outlives the turn.

### Release of a retained branch

When the dependency closes:

- the responsible response must say `此前要求暂时保留的分支 <branch> 现在可以删除了` or an equally direct equivalent;
- it must verify no unique unpreserved work remains;
- it must mark the retention obligation released.

## 3. Integration

The amendment updates:

```text
current/pr-merge-branch-disposition-guard.md
current/github-single-active-pr-lineage-guard.md
current/cross-conversation-execution-intent-and-operator-flow-guard.md
commands/load-mnemosyne-guidance.md
current/post-interruption-live-wayfinding-status.md
```

## 4. Boundaries

This amendment does not:

- authorize merge, branch retention, branch deletion, repository write, or tag creation;
- allow deletion of unmerged branches or unique unpreserved work;
- remove the fail-closed rule when retention state is unknown;
- apply automatically to Meta-Agent or another target project without target-local adoption;
- change `current/human-approved-spec.md`.
