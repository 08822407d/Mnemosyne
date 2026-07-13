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

For a Mnemosyne-owned handoff, the package must explicitly instruct the new conversation to perform these as separate ordered operations:

1. receive the authorized handoff package through `commands/receive-mnemosyne-handoff.md`;
2. execute `Load Mnemosyne guidance` / `加载 Mnemosyne 指导约束` through `commands/load-mnemosyne-guidance.md`;
3. continue the received local task under the refreshed constraints.

Reading `current/human-approved-spec.md` during handoff receive does not remove the requirement to state the guidance-refresh operation explicitly in the package.

For a target-project business-conversation handoff, the package must explicitly require loading the target project's own confirmed constraint guidance or owner rule when one exists. Whether such a business conversation should additionally load Mnemosyne guidance is an unresolved policy question recorded in `current/handoff-guidance-open-question.md`; do not silently present either answer as settled.

## Required behavior

1. Do not treat the package as execution source.
2. Support critical claims with authorized files or mark them as unknown, unsupported, or stale.
3. Keep the package minimally sufficient and high-signal.
4. Use long-transfer file/chunking guidance when the package is long.
5. Do not modify repository files unless the user separately authorizes repository writes.
6. Keep handoff receive and guidance refresh distinct: the package transfers task state; the later guidance command refreshes behavior constraints while preserving that task.
7. For target-project handoffs, prefer the project's confirmed constraints and explicitly record the unresolved Mnemosyne-guidance question rather than importing Mnemosyne maintenance state by default.

## Boundaries

- This command is not an execution source.
- This command does not modify `current/human-approved-spec.md`.
- This command does not approve new design content.
- This command does not authorize target workspace creation, target material ingestion, target repository write, operational build, regression formalization, automation, MCP, RAG, or auto-writeback.