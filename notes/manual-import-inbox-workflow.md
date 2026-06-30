# Manual Import Inbox Workflow

## Status

non-execution-source operational workflow note

## Why this exists

Current Codex Cloud task conversations cannot be assumed to receive non-image file attachments directly.

## Standing helper/template files

`manual-import-inbox/README.md` and `manual-import-inbox/BATCH-MANIFEST-template.md` are standing helper/template files. They are not user-staged import payloads. Processed inbox cleanup applies to user-staged import files and filled manifests, not to these standing helper files. Files copied or filled from the template must still follow safety preflight and should not remain in the inbox after processing unless documented.

## Standard workflow

1. ChatGPT verifies or records current repository visibility before suggesting upload.
2. ChatGPT confirms material sensitivity and whether the material is safe for the current visibility.
3. ChatGPT proposes canonical filenames and, if known, final canonical paths.
4. If the user does not want to create deep directories manually, ChatGPT instructs the user to place only safe files in `manual-import-inbox/`.
5. The user manually uploads/commits the files and notifies the relevant conversation/task.
6. ChatGPT or Codex verifies current repository state.
7. Codex inventories `manual-import-inbox/`.
8. Codex moves/copies safe files to canonical paths using `git mv` where appropriate.
9. Codex performs the type-specific ingestion/analysis/index update.
10. Codex records verification in a result record.
11. Processed inbox files should not remain in the inbox unless a specific reason is documented.

## Safety preflight checklist

Record or verify before inventory/move/copy:

- `repository_visibility`
- `sensitivity`
- `public_repo_safe`
- `contains_secrets_or_credentials`
- `contains_personal_or_confidential_data`
- `git_history_exposure_acknowledged`

If visibility is public or unverified, only public, synthetic, or explicitly redacted material may be staged. Do not commit secrets or credentials under any visibility. Removing or moving a staged file later does not itself remove the file from Git history. Stop on unsafe material and use another user-approved transfer/storage path.

## Processing checklist

- list files under `manual-import-inbox/`;
- compare to expected manifest/task instructions;
- check file extensions and apparent content type;
- check whether final destination already exists;
- if destination exists, compare rather than overwrite;
- stop on ambiguity or unsafe material.

## Naming guidance

Use stable ASCII filenames where possible.
Avoid duplicated extensions like `.md.md`.
Use task-specific prefixes when multiple files are uploaded.

## Boundaries

The inbox is not execution source, not raw evidence by itself, and not canonical storage. Repository visibility and platform behavior are time-sensitive facts and must be reverified when relevant.

## MNEMOSYNE-063 artifact classification gate

Use `notes/manual-import-artifact-classification-v0.1.md` before moving files from `manual-import-inbox/` to canonical paths.

Required classification rules:

- Classify payloads before moving them; verify the classification after moving.
- A full research report original requires full body and required sections.
- Summary/link stubs must not become report originals.
- Prompt originals must not be stored as report originals.
- Pro review results must not be stored as Deep Research reports.
- Synthetic smoke-test results must not be stored as real target dry-run results.
- If classification is uncertain, hold for user instead of guessing.
