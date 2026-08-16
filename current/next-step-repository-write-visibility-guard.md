# Next-Step Repository-Write Visibility Guard

> User-approved Mnemosyne behavior guard created by `MNEMOSYNE-225`. This file is not a standalone execution source; `current/human-approved-spec.md` remains the only Mnemosyne execution source. It is a narrow, more-specific clarification of the existing user-operation and next-step presentation rules.

```yaml
guard_id: MNEMOSYNE-NEXT-STEP-REPOSITORY-WRITE-VISIBILITY-001
guard_version: v0.1
created_by_task: MNEMOSYNE-225
status: active_after_MNEMOSYNE_225_merge
execution_source: current/human-approved-spec.md
execution_source_modified: false
applies_to:
  - Mnemosyne_maintenance_and_self_development_conversations
  - Mnemosyne_repository_review_validation_and_handoff_tasks
  - Mnemosyne_target_project_memory_system_design_and_delivery_tasks
```

## 1. Purpose

A user coordinating several conversations must be able to see immediately whether the proposed next stage will change a repository. Model selection alone is not enough for scheduling: a bounded next-tier task that writes a branch can conflict with another conversation even when its reasoning demand is low.

This guard therefore makes repository-write visibility mandatory in every substantial closing `## 下一步` section.

## 2. Required visible line

When a reply contains a meaningful closing `## 下一步` section, it must include one concise line using one of these forms:

```text
下一步仓库写入：是——<仓库、分支/PR或写入类型；已授权状态>。
下一步仓库写入：否——只读核验、对话内分析或其他不改变仓库状态的工作。
下一步仓库写入：待单独授权——<可能写入的仓库/动作和前置门槛>。
下一步仓库写入：待确认——<尚未确认的目标仓库、并行状态或工具能力>。
```

The line must be adjacent to the model-capability recommendation: normally in the same compact closing block, or no more than three short lines away from `模型要求：...`.

If the exact repository is known and the next stage writes it, name it. If the exact branch, PR, target repository or action is not yet known, say so rather than implying a safe write surface.

## 3. Classification rules

Count the following as repository writes:

- creating, moving or deleting a branch or tag;
- creating, updating, moving or deleting a repository file;
- committing or pushing changes;
- opening, retargeting, closing, merging or otherwise changing a pull request;
- adding comments, labels, reviews or other durable GitHub repository state;
- writing a validation, Meta-Agent or real-target repository even when the material is synthetic.

Classify these as no repository write:

- read-only repository inspection;
- exact identity, diff, branch, PR or merge verification without mutation;
- reasoning or design performed only in the current conversation;
- preparing text that is not uploaded or committed in the same next stage.

Use `待单独授权` when a prepared package is complete but repository mutation remains a separate Owner gate. Use `待确认` when safety depends on a future latest-master, open-PR, visible-branch, target identity or tool-capability check.

## 4. Current operation versus later next step

The opening operation section and the closing next-step section describe different time points.

- If the current user operation is “merge PR #N”, that operation is itself a repository write and must be explicit in the opening operation section.
- The closing line describes what happens after that current operation. It may therefore say `下一步仓库写入：否` when the post-merge step is only read-only verification.
- If the current Agent has already written a branch during the present response, report that in the result body. The closing line still classifies the next stage rather than hiding or reclassifying the write already performed.

## 5. Parallel-conversation planning

When another Mnemosyne-owned conversation may write the same repository, the closing line must also state whether the next write is:

- blocked until the other lineage closes;
- allowed only after exact write-set and semantic independence verification;
- deferred to a separate target repository or branch;
- read-only and therefore non-conflicting.

Do not treat different branch names as sufficient independence. Consider path/write set, read/version dependencies, shared or generated objects, authority scope, merge order and external effects.

## 6. Relationship to existing guidance

This guard narrows and strengthens:

- `current/user-operation-next-step-capability-and-intent-guard.md`, especially the existing `repository_or_external_write` field;
- `current/github-single-active-pr-lineage-guard.md` for parallel repository work;
- `current/run-context-and-pr-provenance-guard.md` for durable write records;
- `current/human-approved-spec.md` §12 for operation/analysis separation.

It does not authorize repository writes, model switching, validation execution, external quota use, target construction, branch deletion, PR merge or any other action.
