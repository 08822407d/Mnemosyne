# Fable F2 Cross-Repository Safe Concurrency Research — Current Status

```yaml
status_id: MNE-FABLE5-CROSS-REPOSITORY-CONCURRENCY-STATUS-001
created_by_task: MNEMOSYNE-214
source_master: 4198d18352a071cbdcc7dc97734e65886da0621b
canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
display_name: MNE-DR-005 跨仓库并发
roadmap_priority: F2
status: READY_NOT_SELECTED_PENDING_MNEMOSYNE_214_MERGE
external_execution_or_quota_authorized: false
Project_creation_authorized: false
automatic_retry: false
repository_write_by_Fable: prohibited
validation_execution_by_Fable: prohibited
```

## Why the timing gate is now met

The roadmap permits F2 after a small public/synthetic cross-repository behavior test or in parallel with its result review. Target Lifecycle V1 has produced a complete controller bundle on:

```text
08822407d/mnemosyne-target-lifecycle-validation-002
tlr-v1-controller@e892749fc9e242b24908f89b6a78f1c0f0bed75e
```

The exact result-bundle blob is:

```text
8a5f3644707ae518182ed352174e58d1ca419067
```

All selected scenarios have provisional executor dispositions, while one execution-profile write-allowlist discrepancy remains pending fresh Pro adjudication. F2 must treat the V1 bundle as provisional behavior evidence and must not pre-empt the dedicated V1 review.

## Prepared package

```text
handoff/fable5-ready/FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001/
```

It contains a Chinese operator flow, one-run task and 30-file input manifest.

## Activation gate

F2 may be selected only after:

1. the MNEMOSYNE-214 preparation PR is merged;
2. the V1 controller inputs remain accessible and no invalidation notice exists;
3. the Owner explicitly chooses one Fable 5 Research run;
4. visible model/mode and any usage-credit warning are recorded at launch.

A later V1 Pro adjudication may be returned alongside the F2 report, but is not required before launch because the roadmap explicitly permits parallel review.
