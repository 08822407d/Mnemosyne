# Fable5 Ready Queue

> Human-facing queue for runnable, not-yet-completed Fable5 research tasks. This directory is navigation and transfer support, not execution source and not research evidence.

```yaml
queue_id: MNEMOSYNE-FABLE5-READY-QUEUE-001
created_by_task: MNEMOSYNE-184
status: active_after_MNEMOSYNE_184_merge
repository: 08822407d/Mnemosyne
research_execution_authority: user_only
repository_write_by_Fable5: prohibited
```

## Current ready tasks

```text
FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/
FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/
```

Each task directory contains:

```text
task.md
OPERATOR.md
input-manifest.yaml
```

Use `OPERATOR.md` first. It states the recommended Claude environment, exact GitHub `+` operation, a connector preflight, the required file/folder selection and manual fallback.

## Queue rules

```yaml
ready_queue_rules:
  contains_only:
    - runnable_candidate_tasks
    - not_yet_completed_tasks
    - exact_operator_entrypoints
  prohibited:
    - completed_task_redirects
    - prior_research_reports
    - hidden_material_from_other_tasks
    - retired_or_superseded_tasks
    - unrelated_Mnemosyne_files
```

A task is not executed merely because it appears here. The user separately decides whether to run it and selects the visible model/effort and quota.

## Completion and retirement

After a report is returned and accepted:

1. preserve the original task under `raw/research-reports/cycles/<cycle>/tasks/`;
2. preserve the report or report receipt in the same cycle;
3. update the cycle manifest and current status;
4. remove the completed task directory from this queue;
5. leave any historical redirect outside this queue.

If a task is retired without execution, remove it from this queue and preserve the reason in a non-runnable plan or retirement record.

## Access model

Do not add the whole Mnemosyne repository to Claude Project Files. Preferred route:

1. fresh standalone Claude chat or new one-run Project;
2. empty Project Files and no prior task chats;
3. choose visible `Fable 5` with `Max` effort;
4. keep Research off;
5. use chat `+` -> `Add from GitHub` and select/link `08822407d/Mnemosyne` on the required branch;
6. run the exact-path preflight from `OPERATOR.md`;
7. enable Research only after the preflight passes.

If the current UI exposes only explicit file/folder selection, select the groups in `input-manifest.yaml`. If connector reads fail, use the manifest-listed manual fallback rather than adding the whole repository.

## Canonical operating guidance

```text
notes/research-operations/claude-project-github-and-fable5-delivery-v0.1.md
```
