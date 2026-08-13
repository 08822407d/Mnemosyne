# Branch-Backed Interview Amendment — Target-Lifecycle Owner Review

> Owner-approved amendment to `MNE-TARGET-LIFECYCLE-OWNER-REVIEW-001`. It changes only how intermediate Owner answers are preserved. It does not change TLR-01 through TLR-05, adopt candidate v0.2, run validation, or authorize target work.

```yaml
amendment_id: MNE-TARGET-LIFECYCLE-OWNER-REVIEW-BRANCH-LEDGER-AMENDMENT-001
package_id: MNE-TARGET-LIFECYCLE-OWNER-REVIEW-001
task_id: MNEMOSYNE-207
status: owner_approved_pending_merge
supersedes_for_interview_persistence_only:
  - README.repository_write_during_interview_false
  - 04-next-tier-interviewer-contract.prohibited_all_repository_writes
  - 05-answer-ledger-and-result-template.repository_write_during_interview_false
  - 07-same-conversation-startup-message.no_branch_commit_or_PR
execution_source: current/human-approved-spec.md
active_guard_ref: current/owner-review-branch-ledger-guard.md
```

## 1. Owner direction

For future material multi-step human reviews, the selected next-tier interviewer may create one task-local branch before the interview is complete and preserve intermediate answers there. One review task/package may use only one branch. A later Pro/frontier segment should continue that same branch rather than reconstructing the interview from chat memory or opening a replacement branch.

## 2. This package's branch contract

```yaml
owner_review_branch_ledger:
  package_id: MNE-TARGET-LIFECYCLE-OWNER-REVIEW-001
  review_task_id: MNE-TARGET-LIFECYCLE-OWNER-REVIEW-001
  repository: 08822407d/Mnemosyne
  base_branch: master
  working_branch: mnemosyne-tlr-owner-review-001-ledger
  working_root: notes/owner-review-working/MNE-TARGET-LIFECYCLE-OWNER-REVIEW-001/
  branch_creation_authorized_after_receive_passes: true
  intermediate_recording_authorized: true
  at_most_one_branch: true
  at_most_one_later_draft_PR: true
  direct_master_write: prohibited
```

If the branch already exists, verify its package identity and continue it. Do not create another branch.

## 3. Allowed files

The next-tier interviewer may create or update only review-evidence files under the working root, such as:

- `README.md` — package identity, base, branch, current question, and write boundary;
- `source-receipt.md` — package/source identities and missing inputs;
- `answer-ledger.md` — Owner answers, interviewer interpretations, confirmations, corrections, deferrals, and current question;
- `final-result-candidate.md` — only after TLR-01 through TLR-05 have been covered.

The ledger must distinguish Owner wording from interviewer interpretation and must not convert an unconfirmed answer into a confirmed decision.

## 4. Still prohibited

The interview branch must not modify:

- Mnemosyne execution source or active guards;
- candidate v0.1 or create candidate v0.2;
- validation plans or fixtures;
- Meta-Agent or either business target;
- product configuration, Projects, Skills, connectors, backups, or external research;
- private source, credentials, customer material, or the complete conversation export in this public repository.

No PR is required during the interview. Owner confirmation does not authorize implementation or merge.

## 5. Pro/frontier continuation

After the interview is complete or when frontier re-entry is needed, Pro/frontier should:

1. read execution-time latest `master` and the exact working-branch head;
2. verify package/task identity and whether master advanced materially;
3. read the correction-aware ledger and source receipt;
4. continue commits on the same branch;
5. correct interpretations, consolidate the final result, and remove redundant non-sensitive working files from the branch tip when useful;
6. create at most one Draft PR only after the task has a coherent reviewable result.

A later commit may remove a file from the current branch tree, but ordinary deletion does not erase earlier Git history. Sensitive material must never be placed in the branch ledger.

## 6. Receive-before-write gate

The first response must still be the package receive report. Branch creation and ledger writing begin only after receive passes. A blocked receive performs no write.
