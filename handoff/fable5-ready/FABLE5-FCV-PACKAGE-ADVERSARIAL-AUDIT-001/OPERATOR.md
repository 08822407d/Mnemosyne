# Operator Guide — FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001

## Purpose

Run one independent Fable5 static audit of the merged frontier-clarification validation package. Do not execute V0/V1, modify GitHub or expose prior Pro/Fable reports.

## Recommended Claude environment

```yaml
preferred_surface: fresh_standalone_chat_or_new_one_run_Project
existing_Mnemosyne_复合评审_Project: not_recommended_for_this_independent_run
Project_Files: leave_empty_for_preferred_route
Project_Instructions: none_task_specific
prior_task_chats_or_reports: absent
visible_model: Fable_5
visible_effort: Max
GitHub_access: chat_level_plus_Add_from_GitHub
Research_initially: off
```

The existing Project shown in the user's screenshots contains Project Memory and prior chats. It remains useful for continuity work, but creates avoidable framing dependence for this audit.

## Preferred connector-linked steps

1. Open a fresh standalone chat, or create a new one-run Project with no prior chats, Instructions or Files.
2. Select visible model `Fable 5` and effort `Max`. Record the exact visible text.
3. Keep Research off.
4. In the chat input, click `+` -> `Add from GitHub`.
5. Select or link repository `08822407d/Mnemosyne`, branch `master`.
6. Confirm that a repository link or selection receipt appears. Do not treat that receipt as proof of a file read.
7. Send the connector preflight below.
8. Continue only if the same chat returns complete-read receipts for all four paths and the visible IDs match.
9. Enable Research and web search.
10. Send the startup instruction below.
11. The task must verify every mandatory path from `input-manifest.yaml` before analysis.
12. If the task returns an integrity failure, do not ask it to guess or continue. Use the explicit-selection or upload fallback in a new clean run.

## Copyable connector preflight

```text
Use the GitHub integration read-only. Research must remain off. Do not analyze the research topic and do not read prior reports.

Read exactly these four files:

1. handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/task.md
2. handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml
3. notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
4. notes/frontier-clarification-validation-package/README.md

Return only:

repository_read_preflight:
  task_id:
  repository:
  selected_branch_or_ref:
  repository_link_visible:
  exact_path_receipts:
    - path:
      complete_read: true | false
      visible_artifact_id_or_heading:
      source_identity_observed:
      limitation:
  Project_Files_used: false
  chat_level_GitHub_used: true
  Research_enabled_during_preflight: false
  write_action_performed: false
  result: PASS | INPUT_OR_REPOSITORY_INTEGRITY_FAILURE

Expected visible identities include task ID FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001 and package ID MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001. A visible GitHub hyperlink without complete file reads is a failure. Do not write GitHub.
```

## Copyable Research startup instruction

```text
Research is now authorized for this one read-only report. Use the GitHub integration read-only.

Re-read:

handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/task.md
handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml

Then read and execute exactly the canonical task they identify:

notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md

Before substantive analysis, verify every mandatory repository path and bind the audit object to package ID MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001 version 0.1.0. The package files and external adjudication inputs originate from package commit 67eb96d5317a2bb589236a4a8b2e75be2508d830. If the current Claude UI exposes only branch-level access, verify exact paths, IDs, versions and cross-file consistency, then state any remaining historical-commit attestation limitation explicitly. Do not invent commit access.

Do not use Project Memory as evidence, prior Pro/Fable reports, A2 materials, other ready-task directories or any GitHub write action. If any mandatory file is missing, unreadable, truncated or mismatched, return only the canonical task's INPUT_OR_REPOSITORY_INTEGRITY_FAILURE object.

The final response must contain the complete report body. Record the exact visible model and effort text and any UI fallback or quota warning, but do not infer the exact served backend.
```

## Explicit file/folder selection fallback

If the GitHub UI exposes a file browser, select only:

```text
handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/task.md
handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml
notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
notes/frontier-clarification-validation-package/                       [entire folder]
notes/validation-designs/frontier-planning-clarification-handoff-read-only-validation-v0.1.md
notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/03-cross-report-consensus-conflict-and-adjudication.md
notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/04-interim-architecture-and-validation-decision.md
```

Do not add the whole repository to Project Files. If this selection must persist, use a new one-run Project rather than the existing continuity Project.

## Manual upload fallback

The minimum upload set is 19 files: the canonical task, all 15 package files and the three external design/adjudication files. This reaches close to the current per-chat upload-count boundary, so prefer GitHub folder selection or connector reads.

If manual upload is necessary:

1. download every file from the recorded source ref;
2. preserve path and filename in a transfer receipt;
3. upload exactly the 19 files, not this operator guide or unrelated files;
4. start a new clean chat or one-run Project;
5. replace connector receipts in the startup instruction with the transfer receipt;
6. stop if any file is omitted, transformed or truncated.

## Independence controls

Do not expose:

- the foundational Pro report;
- the foundational Fable report;
- A2's task or report;
- current maintainer conclusions not named by the canonical task;
- unrelated repository files;
- prior chats or Project Memory from the existing continuity Project.

## Return

Return the complete Fable5 report to the current Mnemosyne frontier-clarification validation conversation. Do not add the report to reusable Project Files and do not reuse this chat/Project for A2 before both independent reports are complete.
