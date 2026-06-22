# Manual Import Inbox

This folder is a temporary staging area for files that the user manually adds to the repository when Codex Cloud cannot directly receive non-image file attachments.

Files placed here are not execution source and are not canonical research/report/raw/delivery files.

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
