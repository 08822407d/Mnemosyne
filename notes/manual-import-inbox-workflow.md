# Manual Import Inbox Workflow

## Status

non-execution-source operational workflow note

## Why this exists

Current Codex Cloud task conversations cannot be assumed to receive non-image file attachments directly.

## Standard workflow

1. ChatGPT proposes canonical filenames and, if known, final canonical paths.
2. If the user does not want to create deep directories manually, ChatGPT instructs the user to place files in `manual-import-inbox/`.
3. The user manually uploads/commits the files and notifies the relevant conversation/task.
4. ChatGPT or Codex verifies current repository state.
5. Codex inventories `manual-import-inbox/`.
6. Codex moves/copies files to canonical paths using `git mv` where appropriate.
7. Codex performs the type-specific ingestion/analysis/index update.
8. Codex records verification in a result record.
9. Processed inbox files should not remain in the inbox unless a specific reason is documented.

## Preflight checklist

- list files under `manual-import-inbox/`;
- compare to expected manifest/task instructions;
- check file extensions and apparent content type;
- check whether final destination already exists;
- if destination exists, compare rather than overwrite;
- stop on ambiguity.

## Naming guidance

Use stable ASCII filenames where possible.
Avoid duplicated extensions like `.md.md`.
Use task-specific prefixes when multiple files are uploaded.

## Boundaries

The inbox is not execution source, not raw evidence by itself, and not canonical storage.
