# Research Prompt Registry — Not the Ready Queue

This directory is a legacy registry and historical reference surface. It may contain:

- currently prepared task texts;
- completed-task redirects;
- retired or superseded prompt references;
- older task formats retained for link stability.

Do **not** browse this directory to decide which Fable5 task should be run next.

The human-facing queue of currently runnable Fable5 tasks is:

```text
handoff/fable5-ready/
```

Each ready task directory contains:

```text
task.md
OPERATOR.md
input-manifest.yaml
```

Lifecycle:

```yaml
ready_task:
  discoverable_at: handoff/fable5-ready/<TASK_ID>/

completed_and_accepted:
  original_task_archived_at: raw/research-reports/cycles/<cycle>/tasks/
  report_or_receipt_archived_at: raw/research-reports/cycles/<cycle>/reports/
  ready_directory_removed: true
  optional_completed_redirect_in_this_registry: allowed

retired_without_execution:
  ready_directory_removed: true
  reason_recorded_elsewhere: required
```

A file in this registry is not runnable merely because its filename begins with `FABLE5-`, `PRO-DR-` or another provider/task prefix. Check the ready queue and current status.

See:

```text
notes/research-operations/claude-project-github-and-fable5-delivery-v0.1.md
```
