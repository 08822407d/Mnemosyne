# MNEMOSYNE-041 Result Record

## task_id

MNEMOSYNE-041

## task_name

Add manual import inbox workflow for non-image file transfer to Codex Cloud.

## files_created

- `manual-import-inbox/README.md`
- `notes/manual-import-inbox-workflow.md`
- `notes/codex-task-results/MNEMOSYNE-041-result.md`

## files_modified

- `current/human-approved-spec.md`
- `handoff/startup-instructions.md`
- `handoff/handoff-current.md`
- `current/active-context.md`
- `current/todo.md`

## files_not_modified

- `README.md` was not modified; the required startup/handoff/spec/context/todo updates were sufficient.
- No research-report files were modified.
- No `AGENTS.md`, `CLAUDE.md`, `.github/workflows/**`, or automation scripts were created or modified.

## summary

Added a root-level `manual-import-inbox/` folder with a user-facing README and documented the operational workflow for manually staging non-image files when Codex Cloud task conversations cannot directly receive them as attachments. Updated the execution source, startup/handoff notes, active context, and TODO list so future Mnemosyne-affiliated ChatGPT/Codex tasks know to inventory and verify inbox files before moving or ingesting them.

## execution-source update summary

`current/human-approved-spec.md` now includes section `## 14. Manual import inbox / Codex Cloud non-image attachment boundary`, which records that `manual-import-inbox/` is temporary staging only, not execution source/raw evidence/canonical research storage/delivery storage, and that tasks must verify file presence, names, types, and destinations before processing.

## manual-import-inbox path

`manual-import-inbox/`

## verification commands and outputs

### `git status --short`

```text
 M current/active-context.md
 M current/human-approved-spec.md
 M current/todo.md
 M handoff/handoff-current.md
 M handoff/startup-instructions.md
?? manual-import-inbox/
?? notes/manual-import-inbox-workflow.md
```

### `git diff HEAD --stat`

```text
 current/active-context.md       |  8 ++++++++
 current/human-approved-spec.md  | 13 +++++++++++++
 current/todo.md                 |  5 +++++
 handoff/handoff-current.md      |  7 +++++++
 handoff/startup-instructions.md |  3 +++
 5 files changed, 36 insertions(+)
```

### `git diff HEAD --name-only`

```text
current/active-context.md
current/human-approved-spec.md
current/todo.md
handoff/handoff-current.md
handoff/startup-instructions.md
```

Note: this command lists tracked-file diffs only before staging; new untracked files were visible in `git status --short`.

### `git diff HEAD -- current/human-approved-spec.md handoff/startup-instructions.md handoff/handoff-current.md current/active-context.md current/todo.md manual-import-inbox/README.md notes/manual-import-inbox-workflow.md notes/codex-task-results/MNEMOSYNE-041-result.md`

```diff
diff --git a/current/active-context.md b/current/active-context.md
index 390c12b..e28344c 100644
--- a/current/active-context.md
+++ b/current/active-context.md
@@ -1,6 +1,14 @@
 # Active Context
 
 
+
+## MNEMOSYNE-041 status
+
+- MNEMOSYNE-041 adds a manual import inbox workflow for current Codex Cloud non-image attachment limitations.
+- `manual-import-inbox/` is temporary staging only: not execution source, raw evidence, canonical research/report storage, or delivery storage.
+- Future inbox-handling tasks must preflight-inventory files, verify names/types/destinations, and stop on missing or ambiguous files rather than guessing.
+- Current execution source remains `current/human-approved-spec.md`.
+
 ## MNEMOSYNE-040 DR1 memory-testing evidence ingestion
 
 - MNEMOSYNE-040 normalized and ingested DR1 memory-system testing/debugging/evaluation evidence as `RC-2026Q2-memory-testing`.
diff --git a/current/human-approved-spec.md b/current/human-approved-spec.md
index cebbe82..db101f3 100644
--- a/current/human-approved-spec.md
+++ b/current/human-approved-spec.md
@@ -149,3 +149,16 @@
 - 如果已生成文件，该文件应被视为优先 transfer artifact；聊天消息只是摘要或指针。
 - 本原则不要求对短回答或短的一步式指令生成文件。
 - 本原则本身不授权任何仓库编辑；它只指导长转发内容应如何打包和交付。
+
+## 14. Manual import inbox / Codex Cloud non-image attachment boundary
+
+- Current Codex Cloud task conversations cannot be assumed to receive non-image file attachments directly.
+- When non-image files need to enter the repository, the user may manually place them in the repository.
+- The preferred staging location for manually uploaded batches is `manual-import-inbox/`.
+- Files in `manual-import-inbox/` are temporary transfer artifacts only.
+- Files in `manual-import-inbox/` are not execution source, not raw evidence, not canonical research originals, and not target-project delivery artifacts until verified and moved/copied to canonical paths.
+- ChatGPT/Codex tasks must verify file presence, names, types, and intended destination before processing.
+- ChatGPT/Codex tasks must not assume they can detect manual file additions in real time; the user must notify the task/conversation after upload.
+- If files are missing or ambiguous, the task must stop or ask for correction rather than guessing.
+- This rule is based on current tool/platform behavior and may be revised if Codex Cloud attachment capability changes.
+
```

The targeted diff also showed the corresponding concise additions to `current/todo.md`, `handoff/handoff-current.md`, and `handoff/startup-instructions.md`.

### `git diff HEAD --name-only | grep -E '^(AGENTS\.md$|CLAUDE\.md$|\.github/workflows/)' || true`

```text
```

### `test -f manual-import-inbox/README.md && echo MANUAL_IMPORT_INBOX_READY`

```text
MANUAL_IMPORT_INBOX_READY
```

## protected file check

No protected files were listed by the protected-file check. No automation files were created or modified.

## known gaps

- This task documents the current operational boundary only. If Codex Cloud attachment behavior changes, the rule should be revised through the normal Mnemosyne update process.
- No actual user-uploaded research/report files were added or ingested in this task.

## whether task claims completion

Yes. MNEMOSYNE-041 is complete.

## additional final verification

### `git diff --check`

```text
```

Exit status: 0.

### Final `git diff HEAD --stat`

```text
 current/active-context.md       |  8 ++++++++
 current/human-approved-spec.md  | 12 ++++++++++++
 current/todo.md                 |  5 +++++
 handoff/handoff-current.md      |  7 +++++++
 handoff/startup-instructions.md |  3 +++
 5 files changed, 35 insertions(+)
```
