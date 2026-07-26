@GitHub # Startup Prompt — Receive PRO-SLICE-01 Phase A Decision Handoff

Receive Mnemosyne handoff.

Use this authorized handoff package:

`handoff/pro-slice-01-phase-a-decision-handoff-package.md`

Package ID:

`MNEMOSYNE-PRO-SLICE-01-PHASE-A-DECISION-HANDOFF-001`

## Required first operation

1. Read `commands/receive-mnemosyne-handoff.md`.
2. Read the authorized package.
3. Read only the minimum evidence paths needed to verify the receive report.
4. Verify that PR #206 is merged and that current `master` is at or descends from the package's trusted baseline.
5. Output the required `mnemosyne_handoff_receive` YAML report.
6. Stop after the receive report.

Do **not** load Mnemosyne guidance in the same operation. I will send
`加载 MNEMOSYNE 约束指导` as a separate next message.

## Transferred local task

You are the new coordinator for the bounded `PRO-SLICE-01` Phase A decision route.

After the separate guidance refresh, your immediate task is to present the exact Phase A scope and ask me to choose one of:

- `ACCEPT_AS_SPECIFIED`
- `ACCEPT_WITH_MODIFICATIONS`
- `DEFER`
- `REJECT`

Do not generate an implementation task before I choose. If I accept or modify Phase A, prepare a new read-only implementation taskbook under a fresh task ID; do not execute it or write to GitHub without a separate task-local authorization.

## Task-local GitHub authorization

This startup prompt authorizes only:

- read-only receive verification;
- reading the package and its minimum cited evidence;
- reporting the receive result.

It does **not** authorize repository writes, branch or PR creation, comments, reviews, merge, auto-merge, Phase A implementation, Phase B work, execution-source modification, target-project actions, or external research.

## Required receiver-guidance sequence

```yaml
receiver_guidance_load:
  project_guidance: not_applicable
  mnemosyne_guidance: required
  ordered_operations:
    - receive_authorized_handoff_package
    - emit_mnemosyne_handoff_receive_report
    - stop_after_receive_report
    - wait_for_separate_user_instruction
    - execute_Load_Mnemosyne_guidance_as_separate_operation
    - confirm_received_task_preserved
    - continue_received_task_under_refreshed_constraints
```

## Prohibited route imports

Do not import as the action plan:

- `current/active-context.md`
- `handoff/handoff-current.md`
- `current/todo.md`
- `current/open-questions.md`
- unrelated target-project routes
- concurrent-workstream governance
- FABLE5-GOV deferred-governance work
- platform/model-routing research
- prior paused maintenance routes

The handoff package is a non-execution-source transfer artifact. `current/human-approved-spec.md` remains the sole execution source.