# MNEMOSYNE-237 / 238 Execution-Surface Pro Adjudication 001

```yaml
adjudication_id: MNE-MNEMOSYNE-237-238-EXECUTION-SURFACE-PRO-ADJUDICATION-001
MNEMOSYNE_237: CLOSED_BLOCKED_NO_RETRY
MNEMOSYNE_238: CLOSED_BLOCKED_NO_RETRY
substantive_Fable_and_Pro_findings_invalidated: false
selected_successor_task: MNEMOSYNE-239
selected_branch: mnemosyne-239-f2-g2a-and-handoff-audit-closeout
old_empty_branch_retained: mnemosyne-235-f2-g2a-and-handoff-audit-closeout
G2A_issued: false
A1_execution_authorized: false
```

## Findings

1. 237 failed across incompatible execution surfaces: DNS failure; missing `gh`; cloud inputs/remote/auth absent; and one Owner mid-run branch-policy override. None reached content publication.
2. 238 proved the current connector's Git Data writes are live, but model-mediated copying of large Base64 arguments introduced an exact-byte defect at call 12. The fail-closed SHA gate worked.
3. Repeating connector blob calls would preserve the same transcription surface. Sequential Contents-API commits remain rejected because they can leave a reachable partial branch.
4. The most reliable available surface is an authenticated local Git worktree. Remove the non-essential `gh` dependency: Phase A performs one verified commit and one non-force push; the originating Pro conversation then performs exact connector readback and creates the Ready PR.
5. A task-matching new branch resolves the Owner's maintainability concern without deleting or moving the historical empty branch.

## Disposition

`MNEMOSYNE-239` is the only authorized successor. It must run once, without mid-run instruction changes. It may not retry 235–238, reuse or clean their objects, write the validation repository, issue G2A/A1, merge, amend or force-push.
