@GitHub # Startup Prompt — Receive F1 Validation-Disposition Handoff

Receive Mnemosyne handoff.

Use this authorized handoff package:

`handoff/mnemosyne-f1-validation-disposition-handoff-package.md`

Package ID:

`MNE-F1-VALIDATION-DISPOSITION-HANDOFF-001`

## Required first operation

1. Read `commands/receive-mnemosyne-handoff.md` from execution-time latest `08822407d/Mnemosyne@master`.
2. Read the authorized handoff package.
3. Read only the package's minimum receive evidence needed to verify the receive report.
4. Verify that current `master` contains the handoff package and that the package's load-bearing path/blob identities still match. Do not require current `master` to equal the pre-publication baseline `5ca091e1c52bb1e7483b2d54e9259d3ec85b7b93`; publication of the package necessarily moves `master`.
5. Output the required `mnemosyne_handoff_receive` YAML report.
6. Stop after the receive report.

Do **not** load Mnemosyne guidance in the same operation. I will send:

`加载 Mnemosyne 指导约束`

as a separate next message.

## Transferred local task

You are the new coordinator for the bounded F1 reusable-capability ownership/lifecycle validation-disposition route.

After the separate guidance refresh, confirm that the received F1 task was preserved. Then explain in natural Chinese and ask me to choose or modify one of:

- `A_ACCEPT_DESIGN_AND_AUTHORIZE_EXACT_EXECUTION_PROFILE_PREPARATION_ONLY`
- `B_ACCEPT_DESIGN_BUT_DEFER_SYNTHETIC_EXECUTION_PREPARATION`
- `C_REVISE_DESIGN`
- `D_REJECT_BOUNDED_VALIDATION_AND_STOP_AT_PROVISIONAL_BASELINE`

The repository recommendation is A, but it is advisory and must not be silently defaulted.

Do not prepare an exact execution profile, create a branch, create a PR, or run validation before I make an explicit decision and separately authorize any repository write.

## Task-local GitHub authorization

This startup prompt authorizes only:

- read-only handoff receive verification;
- reading the package and its minimum cited evidence;
- reporting the receive result.

It does **not** authorize:

- repository writes, branch or PR creation, comments, reviews, merge or auto-merge;
- selection of A/B/C/D;
- exact execution-profile preparation;
- validation-repository creation or modification;
- F1 validation execution;
- capability lifecycle schema implementation;
- construction of the business-function code-library Agent;
- Meta-Agent or real-target work;
- F2/V2 continuation, G2A, A0 or `v2a-sentinel-001-controller` creation;
- execution-source modification;
- Work, Deep Research, Fable or external quota.

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
    - confirm_received_F1_task_preserved
    - continue_received_task_under_refreshed_constraints
```

## Prohibited route imports

Do not import as the action plan:

- `current/active-context.md`;
- `handoff/handoff-current.md`;
- `current/todo.md`;
- `current/open-questions.md`;
- F2/V2 current status, package 003 or A0/G2A materials;
- Meta-Agent construction;
- real target-project routes;
- Target-Lifecycle validation cleanup;
- Fable, Work or platform research;
- unrelated paused or maintenance routes.

The handoff package is a non-execution-source transfer artifact. `current/human-approved-spec.md` remains the sole execution source.
