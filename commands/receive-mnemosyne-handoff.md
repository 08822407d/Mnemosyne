# Receive Mnemosyne Handoff

This file is not an execution source. It defines a user-facing shortcut for receiving an explicit Mnemosyne handoff package in a new conversation; it does not override `current/human-approved-spec.md`.

## Command names

- Receive Mnemosyne handoff
- 接收 Mnemosyne 工作交接包
- 根据 Mnemosyne 交接包继续

## Purpose

Use this command only when the user explicitly provides a handoff package or an authorized handoff-package path and asks the new conversation to continue from it.

No provided package means no handoff. The receiving conversation must not infer a handoff from “Load Mnemosyne guidance” or from a general request to continue.

## Required inputs

A valid receive attempt requires:

- explicit user request to receive or continue from a handoff package;
- handoff package content or an authorized repository path to the package;
- enough package metadata to identify the package as a handoff package.

If any required input is missing, stop and state that the input is not a handoff receive.

## Required files

Read or ask the user to provide:

- `README.md`
- `current/human-approved-spec.md`
- this command file, if available
- the provided handoff package or authorized package path
- task-relevant evidence files cited by the package, as needed and accessible

## Required behavior

1. Treat the package as a non-execution-source transfer artifact.
2. Treat `current/human-approved-spec.md` as the current execution source.
3. Verify package claims against cited evidence paths when they are needed for action.
4. Mark missing, stale, conflicting, unsupported, or unknown information explicitly.
5. Do not use `current/active-context.md`, `handoff/handoff-current.md`, `current/todo.md`, or `current/open-questions.md` as the receiving conversation's action plan unless the package and user request explicitly make them relevant; they still remain non-execution-source.
6. State one safe next action within the package boundaries.
7. Do not modify repository files unless the user separately authorizes repository writes.

## Required first response after receiving

Report:

```yaml
mnemosyne_handoff_receive:
  package_present: true_or_false
  package_id:
  package_status: non_execution_source_transfer_artifact
  execution_source: current/human-approved-spec.md
  evidence_paths_checked:
  evidence_paths_missing_or_unchecked:
  current_task_from_package:
  forbidden_actions:
  safe_next_action:
  limitations_or_unknowns:
```

## Boundaries

- This command is not an execution source.
- This command does not modify `current/human-approved-spec.md`.
- This command does not approve new design content.
- This command does not authorize target workspace creation, target material ingestion, target repository write, operational build, regression formalization, automation, MCP, RAG, or auto-writeback.
- This command does not allow “Load Mnemosyne guidance” to be treated as handoff receive.
