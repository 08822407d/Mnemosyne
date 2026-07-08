# Mnemosyne Command Registry

This directory is a lightweight registry for short user-facing commands.

This file is not an execution source. Command files are not execution sources. Commands are invocation shortcuts only; they do not override `current/human-approved-spec.md`.

Commands help users apply Mnemosyne behavior guidance, prepare explicit handoff packages, receive explicit handoff packages, and list available command shortcuts.

## Available commands

| Command | Invocation examples | Purpose | Command file |
| --- | --- | --- | --- |
| Load Mnemosyne guidance | “Load Mnemosyne guidance.” / “加载 Mnemosyne 指导约束。” / “加载最新指导。” | Refresh Mnemosyne behavior constraints in the current conversation while preserving the current local task. This does not start handoff and does not import maintenance live route. | `commands/load-mnemosyne-guidance.md` |
| Prepare Mnemosyne handoff | “Prepare Mnemosyne handoff.” / “准备 Mnemosyne 工作交接包。” | In the current conversation, create an explicit non-execution-source handoff package for a later receiving conversation. | `commands/prepare-mnemosyne-handoff.md` |
| Receive Mnemosyne handoff | “Receive Mnemosyne handoff.” / “接收 Mnemosyne 工作交接包。” | In a new conversation, process an explicitly provided handoff package or authorized package path. No package means no handoff. | `commands/receive-mnemosyne-handoff.md` |
| List Mnemosyne commands | “List Mnemosyne commands.” / “列出 Mnemosyne commands。” | List available Mnemosyne command shortcuts, purposes, invocation phrases, and required files. | `commands/list-mnemosyne-commands.md` |

## Invocation examples

- “Load Mnemosyne guidance.”
- “加载 Mnemosyne 指导约束。”
- “加载最新指导。”
- “Prepare Mnemosyne handoff.”
- “准备 Mnemosyne 工作交接包。”
- “Receive Mnemosyne handoff.”
- “接收 Mnemosyne 工作交接包。”
- “List Mnemosyne commands.”
- “列出 Mnemosyne commands。”

## Command separation

`Load Mnemosyne guidance` is behavior-constraint refresh only. It must not be interpreted as handoff preparation, handoff receive, repository maintenance takeover, or automatic route detection.

Handoff is an explicit artifact-mediated workflow:

1. The current conversation prepares a handoff package only when the user explicitly requests it.
2. The new conversation receives a handoff package only when the user explicitly provides the package or an authorized package path and asks to continue from it.

A receiving conversation cannot detect a hidden paired action across conversation contexts. It can verify only the current user instruction, the provided package or authorized path, and accessible evidence paths.

## Future command convention

- Use one command per file under `commands/`.
- Each command file should include purpose, invocation examples, required files, behavior, and boundaries.
- Future command files must remain user-facing shortcuts and must not become execution sources.
