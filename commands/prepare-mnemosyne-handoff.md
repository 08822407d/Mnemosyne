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
- `notes/handoff-package-strategy-v0.1.md`, when package tier or structure is being selected
- `notes/handoff-package-strategy-receiver-guidance-load-addendum-2026-07.md`
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
- an explicit `receiver_guidance_load` instruction.

For a Mnemosyne-governed handoff, `receiver_guidance_load` must require the receiving conversation to execute `Load Mnemosyne guidance` / `加载 Mnemosyne 指导约束` before substantive continuation.

For a specific target-project business-conversation handoff:

```yaml
receiver_guidance_load:
  project_guidance: required
  mnemosyne_guidance: yes | no | unknown_requires_user_decision
```

The project-local guidance requirement is mandatory. Whether Mnemosyne guidance should also be loaded is the unresolved scope question recorded in `notes/handoff-guidance-scope-open-question.md`; do not silently convert one task-local choice into a global rule.

## Required behavior

1. Do not treat the package as execution source.
2. Support critical claims with authorized files or mark them as unknown, unsupported, or stale.
3. Keep the package minimally sufficient and high-signal.
4. Use long-transfer file/chunking guidance when the package is long.
5. Make the receiving guidance-load instruction visible in both the package and any paired startup prompt.
6. Keep behavior-guidance refresh separate from explicit handoff receive; neither command replaces the other.
7. Apply the receiver-guidance-load addendum when validating package completeness.
8. Do not modify repository files unless the user separately authorizes repository writes.

## Boundaries

- This command is not an execution source.
- This command does not modify `current/human-approved-spec.md`.
- This command does not approve new design content.
- This command does not decide the open target-project business-conversation Mnemosyne-guidance scope.
- This command does not authorize target workspace creation, target material ingestion, target repository write, operational build, regression formalization, automation, MCP, RAG, or auto-writeback.