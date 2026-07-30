# Fable5 Ready Research Queue

> Human-facing queue for runnable Fable5 research tasks. Select tasks from this directory, not from `notes/research-prompts/`. This directory contains no completed redirects, prior reports, hidden reviewer keys or execution authority.

```yaml
queue_id: MNEMOSYNE-FABLE5-READY-QUEUE-001
created_by_task: MNEMOSYNE-183
status: two_stage_A_tasks_ready_not_executed
repository: 08822407d/Mnemosyne
recommended_access: fresh_chat_plus_Add_from_GitHub
Project_Files_whole_repo: prohibited_by_workflow
research_execution_authority: user_only
```

## Ready tasks

| Order | Task | Purpose | Directory |
|---|---|---|---|
| A1 | `FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001` | Independent static audit of the merged validation package | `handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/` |
| A2 | `FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001` | Independent threat model of the manual V0 surface candidate | `handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/` |

A1 and A2 may be run independently in separate fresh Fable5 research chats. Do not expose either report to the other run before both are complete.

## What to open

For each task, read only its directory first:

```text
task.md              entrypoint and canonical-task pointer
OPERATOR.md          exact Claude UI steps and copyable startup message
input-manifest.yaml  exact repository/file selection and fallback inventory
```

Do not manually browse the legacy `notes/research-prompts/` directory to decide what is runnable. It contains both active historical paths and completed redirects.

## Preferred user flow

1. Open a fresh standalone Claude chat or a new one-run Project.
2. Keep Project Files empty for the preferred route.
3. In the chat input, select `+` -> `Add from GitHub`.
4. Select `08822407d/Mnemosyne` and the branch/commit required by the task.
5. Use the copyable startup instruction in that task's `OPERATOR.md`.
6. Let the task perform its own exact-path read gate.
7. If any required path cannot be read, stop and use the explicit selection/upload fallback in `input-manifest.yaml`.

A visible repository hyperlink is not a file-read receipt. Do not proceed merely because the link appears.

## Independence rule

The existing `Mnemosyne 复合评审` Project contains visible Memory and prior chats. It is not the preferred clean environment for these two independent audits. Use a fresh standalone chat or a new one-run Project without prior Mnemosyne/Fable reports, hidden keys or project instructions.

## Lifecycle

```yaml
ready:
  location: handoff/fable5-ready/<TASK_ID>/
  contains: task_entrypoint_operator_guide_input_manifest

completed_and_accepted:
  archive_original_task: raw/research-reports/cycles/<cycle>/tasks/
  archive_report_or_receipt: raw/research-reports/cycles/<cycle>/reports/
  remove_ready_directory: required
  completed_redirect_inside_ready_queue: prohibited

retired_without_execution:
  remove_ready_directory: required
  record_retirement_reason: required
```

## Governing delivery note

See:

```text
notes/research-operations/claude-project-github-and-fable5-delivery-v0.1.md
```

This queue does not execute research, spend quota, authorize GitHub writes, select an execution surface, run V0/V1 or change an execution source.
