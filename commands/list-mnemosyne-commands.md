# List Mnemosyne Commands

This file is not an execution source. It defines how a session should list available Mnemosyne command shortcuts; it does not override `current/human-approved-spec.md`.

## Command names

- List Mnemosyne commands
- 列出 Mnemosyne commands

## Invocation examples

- “List Mnemosyne commands.”
- “列出 Mnemosyne commands。”

## Purpose

List the available Mnemosyne user-facing command shortcuts for a ChatGPT conversation, Codex task, or future agent session.

## Required files

- `commands/README.md`
- Command files under `commands/`

## Behavior

- Read `commands/README.md` and command files under `commands/`.
- Return a concise list of available commands, invocation phrases, purpose, and required files.
- Do not modify repository files.
- If command files are unavailable, state that the command registry cannot be fully listed.

## Boundaries

- The command registry is not an execution source.
- Command listings do not override `current/human-approved-spec.md`.
- Listing commands does not authorize repository modifications.
