# Handoff Package Strategy — Receiver Guidance-Load Addendum (2026-07)

```yaml
record_type: non_execution_source_operational_strategy_addendum
created_by_task: MNEMOSYNE-116
base_strategy: notes/handoff-package-strategy-v0.1.md
execution_source_rule: current/human-approved-spec.md#20-交接接收端约束加载原则
status: active_addendum
```

## Purpose

This addendum operationalizes the execution-source requirement that a receiving conversation be told explicitly which behavior or project constraints to load before substantive continuation.

It supplements `notes/handoff-package-strategy-v0.1.md`; it does not replace or override the execution source.

## Additional common field

Every newly prepared handoff package should include:

```yaml
receiver_guidance_load:
  project_guidance:
  mnemosyne_guidance:
  command_or_path:
  timing: before_substantive_continuation
  scope_note:
```

## Mnemosyne-governed handoff

```yaml
receiver_guidance_load:
  project_guidance: not_applicable_or_separately_specified
  mnemosyne_guidance: required
  command_or_path: Load Mnemosyne guidance | 加载 Mnemosyne 指导约束
  timing: before_substantive_continuation
  scope_note: behavior_refresh_does_not_replace_explicit_handoff_receive
```

The instruction must appear in both the handoff package and any paired startup prompt.

## Specific target-project business-conversation handoff

```yaml
receiver_guidance_load:
  project_guidance: required
  mnemosyne_guidance: yes | no | unknown_requires_user_decision
  command_or_path:
  timing: before_substantive_continuation
  scope_note: task_local_choice_not_global_precedent
```

The project's own confirmed constraints, execution source, or owner rule must be loaded. Whether Mnemosyne guidance should also be loaded remains unresolved and must not be silently assumed.

Open-question record:

- `notes/handoff-guidance-scope-open-question.md`

## Generation and validity checks

A package is incomplete when:

- it is Mnemosyne-governed but omits the explicit Mnemosyne guidance-refresh instruction;
- it is a target-project business handoff but omits project-local guidance;
- it leaves the Mnemosyne-guidance scope implicit rather than recording `yes`, `no`, or `unknown_requires_user_decision`;
- its package and startup prompt disagree about guidance loading.

A change to the relevant project authority, execution source, or guidance-loading decision makes the package stale and requires revalidation.

## Boundary

This addendum does not decide the open project-business scope, authorize automatic handoff, or authorize repository, target, material, workspace, build, or automation actions.