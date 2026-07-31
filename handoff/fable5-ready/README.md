# Fable5 Ready Queue

> Human-facing queue for runnable, not-yet-completed Fable5 tasks. This directory is navigation and transfer support, not execution source or research evidence.

```yaml
queue_id: MNEMOSYNE-FABLE5-READY-QUEUE-001
created_by_task: MNEMOSYNE-184
last_updated_by_task: MNEMOSYNE-186
status: revised_repository_bound_static_audit_queue_active_after_MNEMOSYNE_186_merge
repository: 08822407d/Mnemosyne
research_execution_authority: user_only
repository_write_by_Fable5: prohibited
```

## Current task state

```yaml
A1:
  directory: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/
  attempts: 1
  substantive_reports_received: 0
  prior_result: INPUT_OR_REPOSITORY_INTEGRITY_FAILURE
  current_state: revised_rerun_ready_after_MNEMOSYNE_186_merge

A2:
  directory: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/
  attempts: 0
  substantive_reports_received: 0
  current_state: preventively_repaired_ready_after_MNEMOSYNE_186_merge
```

Each directory contains:

```text
task.md
OPERATOR.md
input-manifest.yaml
```

The active execution contract is separately named by `task.md` and the manifest. The long canonical audit/threat-model specification remains under `notes/research-prompts/`.

## Run-001 correction

A1 run 001 showed that an ordinary-chat GitHub preflight did not qualify the later Advanced Research executor. The canonical task itself was read completely; the package/source inputs were not available to the paid Research executor.

For the current A1/A2 tasks:

```yaml
visible_model: Fable_5
visible_effort: Max
Advanced_Research: off_for_entire_run
ordinary_web_search:
  during_repository_gate: off
  after_gate_PASS: targeted_only
repository_gate_and_substantive_work_same_chat: required
sample_only_preflight: prohibited
```

## Queue rules

```yaml
ready_queue_rules:
  contains_only:
    - runnable_candidate_tasks
    - not_yet_substantively_completed_tasks
    - exact_operator_entrypoints
  prohibited:
    - completed_task_redirects
    - prior_substantive_research_reports
    - hidden_material_from_other_tasks
    - retired_or_superseded_tasks
    - unrelated_Mnemosyne_files
```

A failed input-binding attempt does not remove a task from the queue when a bounded repair preserves the research question. It is archived as failed-run evidence, and the ready task identifies the revised execution contract.

## Access model

Do not add the whole Mnemosyne repository to Claude Project Files.

Required route:

1. fresh standalone Claude chat or new one-run Project;
2. empty Project Files and no prior task chats;
3. visible `Fable 5` with `Max` effort;
4. Advanced Research off for the entire run;
5. chat `+ -> Add from GitHub`, repository `08822407d/Mnemosyne`, branch `master`;
6. read every support and mandatory path listed by the task's v0.2 manifest;
7. return the full same-context input-binding receipt;
8. continue in the same ordinary chat only after `PASS`;
9. use ordinary web search only for targeted support after the gate.

The full operating procedure must also be given directly in the maintainer/design response; users must not be forced to browse this directory merely to discover the steps.

## Completion and retirement

After a substantive report is returned and accepted:

1. preserve the original active execution contract and canonical specification under the research cycle;
2. preserve the report or report receipt in the same cycle;
3. update the cycle manifest and current status;
4. remove the completed task directory from this queue;
5. leave any historical redirect outside this queue.

A failed input-binding run is stored under a `failed-runs/` path and does not count as an accepted substantive report.

## Current operating guidance

```text
notes/research-operations/claude-fable5-repository-bound-static-audit-v0.2.md
```

Historical delivery guidance remains at:

```text
notes/research-operations/claude-project-github-and-fable5-delivery-v0.1.md
```
