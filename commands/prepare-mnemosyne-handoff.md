# Prepare Mnemosyne Handoff

This file is not an execution source. It defines a user-facing shortcut for preparing a Mnemosyne handoff package in the current conversation; it does not override `current/human-approved-spec.md`.

## Command names

- Prepare Mnemosyne handoff
- 准备 Mnemosyne 工作交接包
- 生成 Mnemosyne 交接包

## Purpose

Use this command only when the user explicitly asks the current conversation to prepare a handoff package for a later new conversation.

A handoff package is a transfer artifact, not execution source. It is used when the current conversation has become too large or unstable to continue reliably.

## Required files and inputs

Read or ask the user to provide:

- `README.md`
- `current/human-approved-spec.md`
- this command file, if available
- task-local materials needed for the handoff package
- task-relevant evidence files needed to support package claims

Read current-state or handoff files only when they are relevant to the explicit package being prepared. They remain non-execution-source.

## Required package content

A package should include:

- package id;
- package status: non-execution-source transfer artifact;
- intended receiver action: receive Mnemosyne handoff;
- current execution source;
- non-execution-source boundary;
- local task summary;
- current phase or gate;
- completed work;
- unresolved work;
- forbidden actions;
- safe next action;
- evidence paths;
- freshness or scope limits;
- missing or unknown information;
- instruction for the user to provide the package or authorized package path in the new conversation;
- explicit receiver-guidance instruction.

Every package and its paired startup prompt must expose a `receiver_guidance_load` block rather than leaving guidance loading implicit.

For a Mnemosyne-owned handoff:

```yaml
receiver_guidance_load:
  project_guidance: not_applicable
  mnemosyne_guidance: required
  ordered_operations:
    - receive_authorized_handoff_package
    - execute_Load_Mnemosyne_guidance_as_separate_operation
    - continue_received_task_under_refreshed_constraints
```

For a target-project business-conversation handoff:

```yaml
receiver_guidance_load:
  project_guidance: required
  mnemosyne_guidance: yes | no | unknown_requires_user_decision
```

The target project's confirmed execution source, owner rule, or constraint guidance must be loaded. Whether Mnemosyne guidance is also loaded remains the unresolved question recorded in `current/handoff-guidance-open-question.md`. A task-local `yes` or `no` is not a global precedent.

Reading `current/human-approved-spec.md` during handoff receive does not remove the requirement to state the Mnemosyne guidance-refresh operation explicitly when it is required.

## Required behavior

1. Do not treat the package as execution source.
2. Support critical claims with authorized files or mark them as unknown, unsupported, or stale.
3. Keep the package minimally sufficient and high-signal.
4. Use long-transfer file/chunking guidance when the package is long.
5. Make `receiver_guidance_load` visible in both the package and its paired startup prompt.
6. Keep handoff receive and guidance refresh distinct: the package transfers task state; the guidance command refreshes behavior constraints while preserving that task.
7. Do not modify repository files unless the user separately authorizes repository writes.

## Boundaries

- This command is not an execution source.
- This command does not modify `current/human-approved-spec.md`.
- This command does not approve new design content.
- This command does not decide the open target-project-business Mnemosyne-guidance question.
- This command does not authorize target workspace creation, target material ingestion, target repository write, operational build, regression formalization, automation, MCP, RAG, or auto-writeback.
