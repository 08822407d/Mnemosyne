# Mnemosyne Command Registry

This directory is a lightweight registry for short user-facing commands.

This file is not an execution source. Command files are not execution sources. Commands are invocation shortcuts only; they do not override `current/human-approved-spec.md`.

Commands help users load Mnemosyne guidance in new ChatGPT conversations, Codex tasks, or future agent sessions when repository guidance is not automatically loaded.

## Available commands

| Command | Invocation examples | Purpose | Command file |
| --- | --- | --- | --- |
| Load Mnemosyne guidance | “Load Mnemosyne guidance.” / “加载 Mnemosyne 指导约束。” | Route a new session to the repository execution source, startup guidance, active context, handoff, todo, open questions, and relevant evidence views. | `commands/load-mnemosyne-guidance.md` |
| List Mnemosyne commands | “List Mnemosyne commands.” / “列出 Mnemosyne commands。” | List available Mnemosyne command shortcuts, purposes, invocation phrases, and required files. | `commands/list-mnemosyne-commands.md` |

## Invocation examples

- “Load Mnemosyne guidance.”
- “加载 Mnemosyne 指导约束。”
- “List Mnemosyne commands.”
- “列出 Mnemosyne commands。”

## Future command convention

- Use one command per file under `commands/`.
- Each command file should include purpose, invocation examples, required files, behavior, and boundaries.
- Future command files must remain user-facing shortcuts and must not become execution sources.
