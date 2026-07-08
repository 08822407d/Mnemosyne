# MNEMOSYNE-092 Result Record

```yaml
task_id: MNEMOSYNE-092
task_name: Implement guidance-loading dialogue-locality protocol
task_type: command_startup_protocol_repair
action_actor: ChatGPT_GitHub_app
started_from: user_approved_follow_up_after_MNEMOSYNE_092_analysis
branch: mnemosyne-092-dialogue-locality-protocol
base_branch: master
base_commit: d46f1ee62cf6e1f590f6ffbbe716ba66f0f31997
files_modified:
  - commands/load-mnemosyne-guidance.md
  - handoff/startup-instructions.md
files_created:
  - notes/codex-task-results/MNEMOSYNE-092-result.md
execution_source_modified: false
current_state_files_modified: false
maintenance_live_state_files_modified: false
handoff_current_modified: false
handoff_startup_instructions_modified: true
official_083_artifacts_modified: false
target_workspace_created: false
target_materials_ingested: false
target_repository_written: false
regression_formalized: false
operational_build_started: false
paused_post_handoff_route_resumed_or_closed: false
```

## Summary

MNEMOSYNE-092 implements a command/startup-level repair for guidance-loading dialogue locality.

The repair makes `commands/load-mnemosyne-guidance.md` mode-aware, distinguishing:

- `behavior_guidance_only`;
- `maintenance_handoff`;
- `target_project_support`.

It also updates `handoff/startup-instructions.md` so the full maintenance startup set imports the Mnemosyne maintenance live route only when the applied load mode is `maintenance_handoff`.

The repair does not modify `current/human-approved-spec.md`. It relies on the existing execution-source and handoff-correctness principles rather than adding a new execution-source rule in this task.

## File changes

### `commands/load-mnemosyne-guidance.md`

- Adds explicit command aliases for behavior-only, maintenance handoff, and target-project support modes.
- Adds load-mode resolution rules.
- Splits required reads by mode.
- Prevents `current/active-context.md`, `handoff/handoff-current.md`, `current/todo.md`, and `current/open-questions.md` from being treated as local action-plan sources in guidance-only / target-project contexts.
- Requires a first-response `guidance_load_binding` report.
- Preserves the prior objective-neutral engineering, operation/conclusion separation, long-transfer, Deep Research, staged prompt-generation, visibility, and missing-file behaviors.

### `handoff/startup-instructions.md`

- Clarifies startup scope.
- Renames the old ordinary startup read set to the maintenance startup set.
- Adds a guidance-only / target-project startup set.
- Adds a dialogue-locality guard requiring the assistant to distinguish local conversation task, Mnemosyne maintenance route, and target-project route before stating a next step.
- Requires reporting applied load mode and local-task binding.

## Verification evidence

### Source file preflight

```yaml
source_files_fetched_from_master:
  commands/load-mnemosyne-guidance.md:
    sha: 4958a47b52874b6a8c10e3824c1feae1051f3d58
  handoff/startup-instructions.md:
    sha: 61ddda3882735ff6ef638043f809e0882e2c2ea0
  notes/codex-task-results/MNEMOSYNE-092-result.md:
    pre_existing: false
    fetch_status: 404_not_found
```

### Branch and pre-result-record compare

`compare_commits(master, mnemosyne-092-dialogue-locality-protocol)` before this result record was created:

```yaml
status: ahead
ahead_by: 2
behind_by: 0
total_commits: 2
base_commit: d46f1ee62cf6e1f590f6ffbbe716ba66f0f31997
files:
  - filename: commands/load-mnemosyne-guidance.md
    status: modified
    additions: 137
    deletions: 24
    changes: 161
  - filename: handoff/startup-instructions.md
    status: modified
    additions: 46
    deletions: 3
    changes: 49
```

### Protected path check

Pre-result-record compare showed only these paths changed:

```text
commands/load-mnemosyne-guidance.md
handoff/startup-instructions.md
```

Therefore the following protected paths were not modified by the command/startup repair commits:

```text
current/human-approved-spec.md
current/active-context.md
current/todo.md
current/open-questions.md
handoff/handoff-current.md
handoff/meta-agent-next-conversation-startup-prompt.md
handoff/meta-agent-post-079-phase-closure-handoff-package.md
target-projects/**
manual-import-inbox/**
```

This result record adds only:

```text
notes/codex-task-results/MNEMOSYNE-092-result.md
```

## Final expected PR changed files

```text
commands/load-mnemosyne-guidance.md
handoff/startup-instructions.md
notes/codex-task-results/MNEMOSYNE-092-result.md
```

## Known limitations

- This task did not run a live replay of the new guidance load protocol.
- This task did not update `current/human-approved-spec.md`.
- This task did not resume or close the paused post-handoff route recorded by MNEMOSYNE-085.
- This task did not create or modify target workspace/material/write/build/regression artifacts.
- Future replay should test whether guidance-only / target-project prompts correctly avoid importing Mnemosyne maintenance live route as local task state.

## Boundary

This result record is not an execution source. It records a low-scope command/startup repair and does not approve target workspace creation, target material ingestion, target repository write, operational memory-system build, regression formalization, or Mnemosyne execution-source update.
