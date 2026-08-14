# Owner-Review Branch-Backed Ledger Guard

> User-approved Mnemosyne behavior guard for material multi-step human review. This file is not an execution source; `current/human-approved-spec.md` remains the only execution source.

```yaml
guard_id: MNEMOSYNE-OWNER-REVIEW-BRANCH-LEDGER-001
created_by_task: MNEMOSYNE-207
last_amended_by_task: MNEMOSYNE-210
status: active_after_MNEMOSYNE_210_merge
applies_to:
  - material_multi_step_owner_review
  - correction_aware_human_decision_interview
  - next_tier_interview_followed_by_frontier_consolidation
execution_source: current/human-approved-spec.md
owner_direction_ref:
  - current_conversation_after_exact_export_supply
  - current_conversation_after_PR_277_workflow_failure_review
specific_PR_readiness_guard: current/agent-product-ready-pr-and-frontier-efficiency-guard.md
```

## 1. Purpose

A long owner-review interview must not depend only on one chat context until the final question. The Owner has granted standing permission for a material multi-step Mnemosyne Owner review to create one task-local branch and preserve intermediate answers there so that a later Pro/frontier segment can continue from durable evidence.

This standing permission is confined to the Mnemosyne repository and review-evidence writes described here. It does not grant target-project or cross-repository write authority.

## 2. One task, one branch

For one review package/task:

- allocate one stable review task/package ID;
- create at most one review branch from execution-time latest default branch;
- do not create replacement or parallel branches for later questions;
- continue the same branch through next-tier interviewing and Pro/frontier consolidation;
- apply `current/github-single-active-pr-lineage-guard.md` before branch creation and before any later PR.

A branch is the task workspace, not a new execution source or target truth.

## 3. Allowed intermediate records

The branch write allowlist should be confined to one package-specific working root, for example:

```text
notes/owner-review-working/<PACKAGE_ID>/
```

Recommended files:

- `README.md` — package, base commit, branch, scope, write authority, current question;
- `source-receipt.md` — exact source/package identities and missing inputs;
- `answer-ledger.md` — Owner answer, interviewer interpretation, confirmation state, corrections, and next question;
- `final-result-candidate.md` — created only after all questions are covered.

The interviewer may update the same ledger after every material answer. It must distinguish:

- Owner verbatim text or a safe exact reference;
- interviewer interpretation;
- `unconfirmed`, `confirmed`, `corrected`, `deferred`, or `rejected` state;
- correction history rather than silent replacement.

## 4. Prohibited interview writes

Branch-backed recording does not authorize the next-tier interviewer to modify:

- `current/human-approved-spec.md` or active guards;
- the reviewed candidate architecture;
- target truth, target code, or target repositories;
- Meta-Agent;
- validation implementation;
- product configuration, Projects, Skills, connectors, or backups;
- private source, credentials, or complete private conversation exports in a public repository.

The branch contains review evidence only until the Owner confirms the final result and a later task receives implementation authority.

## 5. Model-switch continuation

A later Pro/frontier model may continue the same branch when it:

1. reads execution-time latest `master` and the exact branch head;
2. verifies the branch/package/task identity;
3. checks whether `master` advanced and whether the package became stale;
4. reads the branch ledger and correction history;
5. continues commits on the same branch rather than creating another branch.

The Pro/frontier segment may revise interpretations, consolidate records, and delete unnecessary working files from the branch tip when within the task scope.

Before ending the frontier segment, it must also apply the frontier-turn completion check in `current/agent-product-ready-pr-and-frontier-efficiency-guard.md`: complete all authorized frontier-level synthesis and review, then route only genuinely bounded or mechanical follow-up away from the scarce frontier condition.

## 6. Deletion and withdrawal semantics

A later commit can delete a file so that it disappears from the branch's current tree and final PR diff. This is suitable for obsolete, redundant, or superseded non-sensitive working files.

Ordinary deletion does **not** erase the file from earlier Git commits. Therefore:

- do not commit secrets, credentials, or material that must be impossible to recover from history;
- use safe references/excerpts for private source;
- if sensitive data is accidentally committed, stop and use an explicit history-cleaning/security procedure rather than treating a later deletion as erasure.

## 7. PR and merge behavior

- A PR is not required merely to keep an interview branch durable.
- At most one canonical PR may later be opened for the review task.
- When the interview, Pro/frontier consolidation, required Agent review and mechanical checks are complete and no blocking decision remains, the canonical PR must be created as a **Ready PR** (`draft: false`) by default.
- A Draft PR is allowed only when substantive work is still incomplete, a material Owner decision or required review remains pending, further substantive commits are intentionally expected, or the Owner explicitly requests Draft status.
- The mere fact that future validation, target adoption or another separately gated stage has not run does not make a completed review/formalization PR incomplete; those boundaries must be stated in the PR rather than represented by Draft status.
- The Pro/frontier consolidation may keep useful intermediate evidence, merge it into the final result, or delete redundant working files before PR creation.
- The responsible Agent must complete substantive semantic review and give a clear merge recommendation before asking the Owner to merge. It must not shift comprehensive diff review to the Owner by saying only “please review the PR”.
- Owner confirmation, Ready transition, approval or merge is an authority/acceptance gate. None of those actions by itself proves that the Owner performed a complete file-by-file or line-by-line content review.
- Owner confirmation of interview answers does not automatically authorize candidate implementation, validation, target adoption or merge.

The more specific Ready-PR, Owner-review-evidence and post-merge rules are in `current/agent-product-ready-pr-and-frontier-efficiency-guard.md`.

## 8. Concurrency and stale-state handling

- Writes to the same ledger path must be sequential.
- A second writer must verify current branch head before updating.
- If another task modifies overlapping review files or the source package changes materially, stop and reconcile.
- If the branch cannot be read or written, fall back to a visible chat ledger and disclose the persistence failure.

## 9. Required visible receipt

When branch-backed recording starts, report:

```yaml
owner_review_branch_ledger:
  package_id:
  task_id:
  repository:
  base_branch:
  base_sha:
  working_branch:
  working_root:
  current_head:
  current_question:
  writes_limited_to_review_evidence: true
  execution_source_modified: false
  target_modified_or_activated: false
```

At model switch or completion, update the receipt with the latest head and unconfirmed items.

## 10. Boundaries

This guard:

- authorizes only task-local intermediate review recording under the standing Owner permission stated above;
- does not authorize direct writes to `master`;
- does not authorize a second branch for the same review task;
- does not make provisional answers final;
- does not authorize private-material publication;
- does not attest model identity;
- does not turn Ready status or merge into evidence of comprehensive human content review;
- does not replace final Owner confirmation, required Agent review, mechanical checks or post-merge verification.
