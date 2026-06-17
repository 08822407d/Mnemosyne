# Load Mnemosyne Guidance

This file is not an execution source. It defines a user-facing shortcut for loading Mnemosyne repository guidance; it does not override `current/human-approved-spec.md`.

## Command names

- Load Mnemosyne guidance
- 加载 Mnemosyne 指导约束

## Invocation examples

- “Load Mnemosyne guidance.”
- “加载 Mnemosyne 指导约束。”

## Purpose

Use this one-line command at the beginning of a new ChatGPT conversation, Codex task, or future agent session when Mnemosyne repository guidance is not automatically loaded.

## Required files

At minimum, read or ask the user to provide:

- `current/human-approved-spec.md`
- `current/active-context.md`
- `handoff/handoff-current.md`
- `handoff/startup-instructions.md`
- `current/todo.md`
- `current/open-questions.md`
- `notes/codex-task-authoring-and-diff-verification-guidelines.md`

If the task involves tool capability, platform capability, model behavior, automation feasibility, or target-project memory-system design, also read the research evidence current views already referenced by `handoff/startup-instructions.md`.

## Required behavior

1. Do not rely on old conversation context or model memory.
2. Treat `current/human-approved-spec.md` as the only execution source.
3. Read or ask the user to provide the required files listed above.
4. When applicable, also read the research evidence current views referenced by `handoff/startup-instructions.md`.
5. Apply the objective neutral engineering stance from `current/human-approved-spec.md`.
6. Apply the operation/conclusion separation principle from `current/human-approved-spec.md`.
7. If the response asks the user to do something, put the operation steps/content in a clearly marked section before explanation.
8. If the response reports findings or conclusions, put the conclusion/problem/result in a clearly marked section before supporting explanation.
9. Apply the long-transfer file/chunking guidance from `current/human-approved-spec.md`. When producing long content for the user to manually forward, prefer generating a downloadable file and show only a concise summary in the chat. If the content must be split, label chunks with package/task title, stable ID, chunk number, total chunk count if known, and wait-for-all-chunks instruction.
10. The first response after loading should include:
   - current execution source;
   - current phase;
   - non-execution-source boundaries;
   - current forbidden actions;
   - current next-route options;
   - whether any conflict or missing file was found.
11. If required files are unavailable, ask for the missing files or clearly state the limitation. Do not invent repository state.

## Boundaries

- This command is a shortcut for loading existing repository guidance.
- This command is not an execution source.
- This command does not approve new design content.
- This command does not authorize edits, automation, MCP, RAG, auto-writeback, or changes outside the user-approved task scope.
