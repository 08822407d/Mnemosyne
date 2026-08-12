# PR Merge and Post-Merge Branch Retention Guard

> User-approved Mnemosyne behavior guard for making branch-retention requirements visible when a response asks the user to review or merge a pull request, explicitly releasing previously retained branches when their dependency ends, and auditing retained-branch obligations for stale or zombie states. This file is not a standalone execution source; `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
guard_id: MNEMOSYNE-PR-MERGE-BRANCH-DISPOSITION-001
guard_version: v0.3
created_by_task: MNEMOSYNE-196
last_amended_by_task: MNEMOSYNE-203
status: active_after_MNEMOSYNE_203_merge
execution_source: current/human-approved-spec.md
execution_source_modified: false
amendment_source:
  - notes/proposed-active-guidance-amendments-from-or01-v0.1.md
  - notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-OR-01-RESULT-001.md
applies_to:
  - Mnemosyne_conversations_that_ask_the_user_to_review_or_merge_a_repository_PR
  - Mnemosyne_repository_tasks
  - Mnemosyne_target_delivery_tasks_when_this_guard_is_explicitly_loaded
  - periodic_manual_or_automated_Mnemosyne_branch_retention_obligation_audits
user_default:
  when_no_prominent_retention_instruction_is_given: branch_may_be_deleted_after_merge
user_facing_asymmetry:
  ordinary_delete_allowed: silent_default_no_notice_required
  retention_required: prominent_notice_required
  prior_retention_released: explicit_release_notice_required
```

## 1. Problem addressed

A PR head branch may need to remain after merge because another task, comparison, replay, external Agent, release process, post-merge verification, or rollback rehearsal still depends on the live branch ref. If that requirement is buried in analysis or omitted, the user may reasonably delete the branch immediately after merging.

The opposite problem is also real: routinely telling the user that every ordinary merged branch may be deleted adds noise, while branches previously marked “retain” may remain indefinitely after their real dependency ended or the responsible conversation stopped checking them.

The Owner therefore establishes three linked rules:

1. **Silence means ordinary deletion is allowed after merge.**
2. **A prior explicit retention instruction must later receive an explicit release notice when retention is no longer needed.**
3. **Explicit retention obligations may be periodically audited so stale, satisfied, unclear, missing-dependency, or missing-branch states do not remain invisible.**

Branch retention is never implicit, branch release after a prior retention instruction is never implicit, and an audit never creates automatic deletion authority.

## 2. User-facing rule before merge

### 2.1 No verified retention dependency

When no verified post-merge workflow needs the live head branch:

- do not add a branch-deletion instruction to the user-facing merge steps;
- do not add a routine `DELETE_ALLOWED` block merely for completeness;
- rely on the Owner default that an omitted retention notice means the branch may be deleted after merge.

The actor may still record the internal conclusion `retention_required: false` in task evidence.

### 2.2 Retention required

When retention is required, the opening `操作内容（需要你手动执行）` section must state conspicuously:

```text
⚠ 合并后请保留分支 `<branch>`，暂时不要删除。
保留原因：<verified dependency>。
保留至：<exact gate/event>。
```

The notice must name:

```yaml
branch_retention_notice:
  obligation_id:
  branch:
  originating_PR:
  reason:
  retain_until:
  responsible_route_or_task:
  release_notice_required: true
```

Requirements:

1. Put the notice next to the PR review/merge instruction and before long analysis.
2. Name the exact branch.
3. Explain the concrete dependency.
4. Give an exact release gate, or identify the specific pending decision that blocks deletion.
5. Do not rely on a PR body, repository file, closing `下一步`, parenthetical note, or buried paragraph.
6. If several branches require retention, issue a separate obligation for each.

### 2.3 Unknown retention state

If branch state or downstream dependency cannot be established, return:

```yaml
branch_retention_state: UNKNOWN_BLOCKS_MERGE_INSTRUCTION
```

Do not ask the user to merge until the uncertainty is resolved.

## 3. Internal pre-merge verification

Before issuing a merge instruction, inspect and record:

```yaml
branch_retention_preflight:
  PR_state:
  PR_head_branch:
  PR_head_SHA:
  unique_or_unmerged_work_outside_PR:
  downstream_live_branch_dependencies: []
  immutable_commit_or_artifact_substitute_available:
  retention_required: true | false | unknown
  retention_gate:
  decision: SILENT_DEFAULT_DELETE_AFTER_MERGE | RETAIN_REQUIRED | RETAIN_UNTIL_GATE | UNKNOWN_BLOCKS_MERGE_INSTRUCTION
```

Decision rules:

1. No verified dependency → `SILENT_DEFAULT_DELETE_AFTER_MERGE`; no user-facing branch notice.
2. Dependency with known gate → `RETAIN_UNTIL_GATE`; issue prominent retention notice.
3. Dependency without known release gate → `RETAIN_REQUIRED`; name the blocking decision and responsible route.
4. Unknown state → block the merge instruction.
5. Prefer immutable commit refs, merged history, saved artifacts, or tags when they eliminate the need for a live working branch.
6. Vague caution or possible future usefulness is not a valid retention reason.

## 4. Retention-obligation tracking

Every explicit retention notice creates an active obligation that must remain retrievable until released.

```yaml
branch_retention_obligation:
  obligation_id:
  branch:
  originating_task:
  originating_PR:
  notice_ref:
  reason:
  retain_until:
  responsible_route_or_task:
  status: ACTIVE | RELEASED | SUPERSEDED
  release_notice_ref:
```

The obligation should be recorded in the task result or another durable route-status/handoff artifact when the branch will outlive the current turn. If ownership moves to another conversation, the handoff must carry the active obligation.

Do not create a permanent central registry merely for ordinary branches. Track only branches that received an explicit retention instruction.

## 4A. Periodic retention-obligation audit

A periodic manual or automated maintenance task may inspect explicit active retention obligations to detect stale or zombie states. It must use a bounded audit record such as:

```yaml
branch_retention_obligation_audit:
  audit_id:
  repository:
  observed_at:
  active_obligations_checked: []
  obligation_results:
    - obligation_id:
      branch:
      branch_exists:
      stated_reason:
      retain_until:
      responsible_route_or_task:
      gate_status: not_reached | reached | unclear | dependency_missing
      unique_unpreserved_work_status:
      disposition: keep | release_notice_required | clarify | incident
  repository_writes_or_deletions_authorized: false
```

Rules:

1. Audit only obligations that were explicitly created; do not turn every merged branch into a permanent retention-registry item.
2. The audit may identify stale obligations, satisfied gates, unclear gates, missing dependencies, missing responsible routes, or branches that no longer exist.
3. The audit does not authorize branch deletion, obligation closure, repository writes, or silent extension of a retention period.
4. A reached release gate requires verification that no unique unpreserved work remains and then the explicit user-facing release notice required by §5.
5. An unclear gate or missing dependency is routed to the responsible route or Owner for clarification; it must not be silently kept forever merely because the audit cannot decide.
6. A branch that is missing while its obligation remains active is an incident candidate. Do not mark the obligation cleanly released merely because the branch cannot be found.
7. If the stated reason remains valid and the gate is not reached, record `keep` without creating a new user-facing retention notice unless the existing instruction must be corrected or transferred.
8. Audit cadence is repository- and Owner-specific. It should be informed by actual obligation volume, branch lifetime, repository automation, and observed stale-state risk rather than a universal schedule.
9. Automated maintenance may enumerate and assess evidence, but any deletion or other external side effect remains separately authorized and verified.

## 5. Mandatory release notice

When a previously retained branch reaches its release gate, the responsible Mnemosyne response must explicitly tell the user that the earlier retention requirement has ended.

Required wording or a direct equivalent:

```text
此前要求暂时保留的分支 `<branch>` 现在可以删除了。
```

The release notice must be prominent and must identify the prior obligation:

```yaml
branch_retention_release:
  obligation_id:
  branch:
  previous_notice_ref:
  release_gate_satisfied:
  unique_unpreserved_work: false
  prior_retention_requirement_ended: true
  now_may_be_deleted: true
  notice_delivered_to_user: true
```

Rules:

1. Issue the notice in the opening operation section, or another equally prominent operation notice, even when deletion is optional.
2. Name the exact branch and the satisfied gate.
3. Verify there is no unique unpreserved work before release.
4. Update the durable obligation to `RELEASED` and record the release-notice reference.
5. Do not leave an indefinite retention instruction active after its dependency closes.
6. If repository policy retains the branch independently of task need, distinguish policy retention from the ended user-facing requirement.

This explicit release rule applies only to branches that were previously subject to an explicit retention instruction. Ordinary merged branches with no retention notice require no later release message.

## 6. Relationship to merge instructions

The compact merge instruction always identifies the merge target, but branch-retention fields are included only when retention is required:

```yaml
merge_instruction:
  task_id:
  merge_target_pr:
  merge_target_head_branch:
  related_open_prs: []
  exactly_one_merge_target: true
  duplicate_preflight_completed: true

  # Include only when retention is required:
  branch_retention:
    obligation_id:
    branch:
    reason:
    retain_until:
```

Do not add a `DELETE_ALLOWED` field to the user-facing merge instruction for an ordinary branch.

## 7. Result-record and PR-finalization requirements

Important repository-writing task records should include:

- the branch-retention preflight;
- whether an explicit retention obligation was created;
- any retention reason, gate, responsible route, and notice reference;
- whether an immutable commit or artifact can replace the live branch;
- any periodic audit record when an audit was actually performed;
- any stale/zombie, unclear-gate, missing-dependency, or missing-branch finding;
- any later release-to-delete record.

PR finalization rules:

- if retention is required, record and surface it prominently;
- if retention is not required, record the internal `SILENT_DEFAULT_DELETE_AFTER_MERGE` conclusion without adding a user-facing deletion instruction;
- if a prior retention obligation is released, create the explicit user-facing release notice and close the obligation;
- if an audit identifies an unclear or incident state, do not present it as a clean release or routine deletion candidate.

## 8. Valid reasons to retain a branch

Valid reasons include:

- an external Agent or tool must read the exact live branch ref;
- an approved post-merge comparison or provenance check cannot use immutable commits instead;
- a staged rollout, release, backport, or rollback rehearsal names the branch;
- unresolved parallel-lineage reconciliation depends on the branch;
- a user-approved experiment names the branch as a required input;
- repository limitations make the branch the only carrier of unique evidence not preserved elsewhere.

Invalid reasons include habit, generic caution, uncertainty about whether it might be useful, or the assistant's failure to verify the dependency.

## 9. Relationship to other guards

This guard complements:

- `current/github-single-active-pr-lineage-guard.md` for canonical branch/PR selection;
- `current/cross-conversation-execution-intent-and-operator-flow-guard.md` for visible current actions;
- `current/run-context-and-pr-provenance-guard.md` for repository-action evidence;
- `current/user-operation-next-step-capability-and-intent-guard.md` for opening operation placement.

When rules conflict, the stricter fail-closed action applies. None of these guards authorizes merge, retention, deletion, or audit-triggered side effects.

## 10. Boundaries

This guard does not:

- authorize a PR merge, branch deletion, branch retention, tag creation, audit-triggered repository write, or any other repository side effect;
- require a deletion notice for every ordinary merged branch;
- require a permanent registry for ordinary branches that never received a retention notice;
- preserve unique unmerged work automatically;
- replace branch-protection rules or repository policy;
- make a branch an execution source, target truth, or authoritative artifact;
- apply automatically to a separate target project unless that project's Owner adopts it or a task explicitly loads it as a process constraint.
