# Artifact Delivery Repair Status

> Non-execution-source live wayfinding record. `current/human-approved-spec.md` remains the only execution source.

```yaml
record_type: live_repair_status
created_by_task: MNEMOSYNE-127
latest_updated_by_task: MNEMOSYNE-137
route: post_PR_173_artifact_delivery_reconciliation
status: behavior_validation_reviewed_PASS_issue_closure_authorized
user_decision_recorded: true
user_decision_provenance:
  - approval_of_MNEMOSYNE_124
  - instruction_to_redo_all_current_conversation_work_after_PR_173
  - approval_of_MNEMOSYNE_137_validation_storage_status_sync_and_issue_closure_on_PR_merge
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

Their useful intent was re-evaluated from the current execution source, Issues #170/#171, DR6 evidence, and the user's correction. Their proposal files are not active guidance.

## 2. Concurrent repository work preserved

PR #177 / MNEMOSYNE-126 was created in another conversation and merged after PR #176. It is unrelated FABLE5-GREENFIELD evidence-storage work and remains preserved.

MNEMOSYNE-127 started from the post-PR-177 `master`; it did not reset or revert the repository to PR #173. MNEMOSYNE-137 starts from the then-current `master` and does not import or alter unrelated conversation work.

## 3. Reconciliation outcome

The active implementation is the user-approved behavior guard:

- `current/artifact-delivery-and-direct-generation-guard.md`

It is loaded through:

- `commands/load-mnemosyne-guidance.md`
- `handoff/startup-instructions.md`

Wayfinding is available in:

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

## 5. Fresh behavior validation

```yaml
validation:
  validation_id: MNEMOSYNE-ARTIFACT-DELIVERY-VALIDATION-001
  instrument: notes/artifact-delivery-behavior-validation-v0.1.md
  evidence_root: notes/artifact-delivery-validation-results/MNEMOSYNE-ARTIFACT-DELIVERY-VALIDATION-001/
  tested_guard_blob_sha: 95f9f404e5de0d06b52a9be314b2fb2e76636ac2
  executor_result: PASS
  Stage_B_reviewed_result: PASS
  cases:
    ARTIFACT_DELIVERY_001: PASS
    ARTIFACT_DELIVERY_002: PASS
    ARTIFACT_DELIVERY_003: PASS
    ARTIFACT_DELIVERY_004: PASS
    ARTIFACT_DELIVERY_005: NOT_RUN
  long_artifact_file_first_verified: true
  same_response_generation_verified: true
  short_inline_behavior_verified: true
  Deep_Research_exception_verified: true
  invented_path_or_false_delivery_detected: false
  future_generation_only_response_detected: false
```

Case 005 was conditional and was not run because no natural file-tool failure occurred. No failure-handling conclusion is claimed.

## 6. Issue disposition

```yaml
issues:
  issue_170:
    closure_conditions_satisfied: true
    authorized_disposition: close_on_MNEMOSYNE_137_PR_merge
  issue_171:
    closure_conditions_satisfied: true
    authorized_disposition: close_on_MNEMOSYNE_137_PR_merge
```

Issue #170 conditions are satisfied because Cases 001, 003, and 004 passed with no invented path or false delivery. Issue #171 conditions are satisfied because Case 002 passed with no future-generation-only response.

The closeout PR is authorized to use GitHub closing keywords. Neither issue is directly closed before the PR merges.

## 7. Boundaries and limitations

- No direct Git rollback was performed.
- Unrelated conversation work is preserved.
- `current/human-approved-spec.md` is unchanged.
- Meta-Agent authority, §19 no-write policy, `HO-GUIDANCE-001`, target-project state, and FABLE5 substantive conclusions are unchanged.
- This validation is behavioral evidence, not a formal no-write proof.
- Operator-visible Project/model/reasoning facts do not prove hidden backend identity.
- One successful fresh run is bounded evidence, not a permanent platform guarantee.
