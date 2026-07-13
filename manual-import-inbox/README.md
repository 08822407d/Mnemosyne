# Manual Import Inbox

This folder is a temporary staging area for files that the user manually adds to the repository when Codex Cloud cannot directly receive non-image file attachments.

Files placed here are not execution source and are not canonical research/report/raw/delivery files.

## Standing helper files

`manual-import-inbox/README.md` and `manual-import-inbox/BATCH-MANIFEST-template.md` are standing helper/template files. They are not user-staged import payloads.

Processed inbox cleanup applies to user-staged import files and filled manifests, not to these standing helper files. Files copied or filled from the template must still follow the safety preflight above and should not remain in the inbox after processing unless a task documents the reason.

## Retained processed Fable review transfer artifacts

The following files were processed by MNEMOSYNE-091 and are intentionally retained byte-for-byte as transfer/provenance artifacts. They are **not canonical**, **not execution source**, and are superseded for ordinary review use by the canonical copies listed below.

| Retained transfer file | Processing status | Canonical destination | Retention reason |
|---|---|---|---|
| `FABLE5-independent-review-output1-project-understanding-and-scope-proposal.md` | processed_retained_for_provenance | `notes/cross-model-review-results/FABLE5-REVIEW-001/01-project-understanding-and-scope-proposal.md` | preserve the manually transferred source while making canonical status unambiguous |
| `FABLE5-REVIEW-001-formal-result.md` | processed_retained_for_provenance | `notes/cross-model-review-results/FABLE5-REVIEW-001/02-formal-review-result.md` | preserve the manually transferred source while making canonical status unambiguous |
| `FABLE5-REVIEW-002-regression-warning-traceability-review-result.md` | processed_retained_for_provenance | `notes/cross-model-review-results/FABLE5-REVIEW-002/01-regression-warning-traceability-review-result.md` | preserve the manually transferred source while making canonical status unambiguous |

This documented exception resolves their inbox status. New processed payloads must not be retained merely by analogy; each future retention requires its own explicit reason.

## Safety preflight

Before any upload, inventory, move, or copy, record or verify:

- `repository_visibility`
- `sensitivity`
- `public_repo_safe`
- `contains_secrets_or_credentials`
- `contains_personal_or_confidential_data`
- `git_history_exposure_acknowledged`

If repository visibility is public or unverified, only public, synthetic, or explicitly redacted material may be staged here. Do not commit secrets or credentials under any visibility. Removing or moving a file later does not itself remove the file from Git history. Stop on unsafe material, not only ambiguity; use another user-approved transfer/storage path instead.

A later ChatGPT/Codex task must:

1. inventory the files in this folder;
2. verify expected names, types, intended destinations, and safety preflight fields;
3. stop if any file is unsafe for the current repository visibility;
4. move or copy safe files to canonical repository paths;
5. update appropriate indexes/summaries/status files;
6. remove processed inbox copies unless intentionally retained with a documented reason.

Do not treat this folder as permanent storage.
