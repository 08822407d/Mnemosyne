# Artifact Delivery Repair Status

> Non-execution-source live wayfinding record. `current/human-approved-spec.md` remains the only execution source.

```yaml
record_type: live_repair_status
created_by_task: MNEMOSYNE-127
route: post_PR_173_artifact_delivery_reconciliation
status: reviewed_guard_prepared_behavior_validation_pending
user_decision_recorded: true
user_decision_provenance:
  - approval_of_MNEMOSYNE_124
  - instruction_to_redo_all_current_conversation_work_after_PR_173
execution_source: current/human-approved-spec.md
```

## 1. Reliable boundary

PR #173 / MNEMOSYNE-123 is accepted as the reliable pre-incident boundary and is not redone.

The following later merged PRs are retained in Git history but are not the active implementation:

```yaml
suspect_period_history:
  PR_174:
    task_id: MNEMOSYNE-124
    role: initial_candidate_plan
    current_status: historical_superseded
  PR_175:
    task_id: MNEMOSYNE-125
    role: operationalization_proposal
    current_status: historical_superseded
  PR_176:
    task_id: MNEMOSYNE-125_reused_after_merge
    role: amendment_proposal
    current_status: historical_superseded
```

Their useful intent was re-evaluated from the current execution source, Issues #170/#171, DR6 evidence, and the user's current correction. Their proposal files are not active guidance.

## 2. Concurrent repository work preserved

PR #177 / MNEMOSYNE-126 was created in another conversation and merged after PR #176. It is unrelated FABLE5-GREENFIELD evidence-storage work and is preserved unchanged.

MNEMOSYNE-127 starts from the post-PR-177 `master`; it does not reset or revert the repository to PR #173.

## 3. Reconciliation outcome

The active implementation is the user-approved behavior guard:

- `current/artifact-delivery-and-direct-generation-guard.md`

It is loaded through:

- `commands/load-mnemosyne-guidance.md`
- `handoff/startup-instructions.md`

Wayfinding is added to:

- `README.md`

The guard:

- defines functional file-first triggers;
- requires same-response generation for explicitly requested low-risk downloadable artifacts when safe and tool-supported;
- separates safe local artifact creation from independently authorized external actions;
- requires successful creation and a real link before claiming delivery;
- preserves short inline responses and the Deep Research full-report-body exception;
- does not authorize repository writes or close issues automatically.

## 4. Superseded files

```yaml
removed_from_current_wayfinding:
  - current/proposed-section-13-artifact-delivery-operationalization.md
  - current/proposed-mnemosyne-125-execution-source-amendment.md
historical_audit_record_retained:
  - notes/MNEMOSYNE-124-artifact-delivery-repair-plan.md
```

The retained notes file has an explicit superseded/historical banner.

## 5. Validation and issue status

```yaml
validation:
  path: notes/artifact-delivery-behavior-validation-v0.1.md
  status: pending_after_guard_merge
issues:
  issue_170:
    state: open
    reason: fresh_behavior_validation_not_yet_complete
  issue_171:
    state: open
    reason: fresh_behavior_validation_not_yet_complete
```

Static review or repository merge alone is not sufficient to close either issue.

## 6. Boundaries

- No direct Git rollback was performed.
- PR #177 content was not removed or overwritten.
- `current/human-approved-spec.md` is unchanged.
- Meta-Agent authority, §19 no-write policy, `HO-GUIDANCE-001`, target-project state, and FABLE5 substantive conclusions are unchanged.
- No issue is closed by this record.
