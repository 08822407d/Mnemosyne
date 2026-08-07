# PR Merge Branch-Disposition Guard — Adoption Record

```yaml
record_id: MNEMOSYNE-PR-MERGE-BRANCH-DISPOSITION-ADOPTION-001
created_by_task: MNEMOSYNE-196
status: adopted_on_human_merge_of_MNEMOSYNE_196_PR
execution_source_modified: false
guard: current/pr-merge-branch-disposition-guard.md
source_instruction: current_conversation_user_instruction_after_Meta_Agent_migration
```

## 1. Owner decision

The Owner established this default for Mnemosyne-owned conversations:

> When a response asks the user to review or merge a repository PR, any requirement to keep the PR's head branch must be stated prominently. If no prominent branch-retention instruction is given, the user will assume the branch may be deleted after merge.

## 2. Adopted operational rule

```yaml
PR_merge_response:
  branch_disposition_required_in_opening_operation_section: true
  allowed_values:
    - DELETE_ALLOWED
    - RETAIN_REQUIRED
    - RETAIN_UNTIL_GATE
    - UNKNOWN_BLOCKS_MERGE_INSTRUCTION

Owner_default_when_omitted:
  branch_may_be_deleted_after_merge: true
```

When retention is required, the response must state:

- exact branch;
- reason;
- exact retention gate or blocking decision;
- deletion condition;
- an explicit `合并后请保留分支` instruction before long analysis.

When no verified dependency exists, the response should say that the branch may be deleted after merge.

## 3. Motivation and correction

The rule was requested after the Meta-Agent repository migration exposed a branch-retention requirement that was not sufficiently visible in the operator-facing response. The problem was not merely whether a branch could technically be deleted. It was that a task-local dependency could be lost because the user-facing merge instruction did not make retention operationally prominent.

This adoption corrects future Mnemosyne behavior. It does not retroactively alter prior PRs or prove that every historical branch-retention instruction was defective.

## 4. Integrated files

```text
current/pr-merge-branch-disposition-guard.md
current/github-single-active-pr-lineage-guard.md
current/cross-conversation-execution-intent-and-operator-flow-guard.md
commands/load-mnemosyne-guidance.md
README.md
```

## 5. Boundaries

- This record does not authorize merge or branch deletion.
- It does not require retaining ordinary merged branches without a concrete dependency.
- It does not automatically apply to Meta-Agent or another dedicated target repository after migration unless that project's Owner adopts it or a task explicitly loads it.
- It does not make a working branch an authoritative artifact or execution source.
