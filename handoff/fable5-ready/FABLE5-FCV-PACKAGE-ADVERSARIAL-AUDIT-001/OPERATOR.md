# Operator Guide — FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001

## Purpose

Run one independent Fable5 static audit of the merged frontier-clarification validation package. Do not execute V0/V1, modify GitHub, or provide prior Pro/Fable reports.

## Recommended Claude environment

```yaml
preferred_surface: fresh_standalone_chat_or_new_one_run_Project
existing_Mnemosyne_复合评审_Project: not_recommended_for_independent_run
Project_Files: leave_empty_for_preferred_route
Project_Instructions: none_task_specific
prior_task_chats_or_reports: not_available_to_run
GitHub_access: chat_level_plus_Add_from_GitHub
```

The existing project shown in the user's 2026-07-30 screenshots has persistent Memory and prior chats. Use a fresh chat outside it, or create a new one-run Project with no prior knowledge/files.

## Preferred connector-linked steps

1. Open the fresh chat.
2. Select Fable 5 high/xhigh and enable Research only when ready to submit the task.
3. In the chat input, click `+` -> `Add from GitHub`.
4. Select repository `08822407d/Mnemosyne` and branch `master`.
5. Confirm the repository link appears in the chat.
6. Send the startup text below.
7. The run must verify all mandatory paths at commit `67eb96d5317a2bb589236a4a8b2e75be2508d830` before analysis.
8. If the task returns an input/repository integrity failure, do not ask it to guess or continue; use the explicit selection fallback.

## Copyable startup instruction

```text
Use the GitHub connector read-only. First read:

handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/task.md

Then read and execute exactly the canonical task it identifies. Verify every mandatory repository path at the pinned commit before substantive analysis. Do not use prior Pro/Fable reports, other ready-task directories, Project Memory as evidence, or any GitHub write action. If any required file cannot be read completely at the pinned commit, return only the task-defined input/repository integrity failure.
```

## Explicit GitHub selection fallback

If the current GitHub UI provides a file/folder browser, select exactly:

```text
handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/task.md
notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
notes/frontier-clarification-validation-package/                  [entire folder]
notes/validation-designs/frontier-planning-clarification-handoff-read-only-validation-v0.1.md
notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/03-cross-report-consensus-conflict-and-adjudication.md
notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/04-interim-architecture-and-validation-decision.md
```

The package folder contains 15 files. Including the ready entrypoint, canonical task and three external evidence files produces 20 selected files. Do not add the whole repository.

## Manual upload fallback

If GitHub connector reads fail:

1. download the exact files listed in `input-manifest.yaml` from the pinned commit;
2. preserve original filenames and paths in a transfer receipt;
3. upload no more than the exact set;
4. do not add the files to a reusable Project shared with A2;
5. start a new one-run chat/project and submit the same startup instruction, replacing connector reads with the uploaded-file receipt.

## Independence and contamination controls

Do not attach or expose:

- the foundational Pro report;
- the foundational Fable report;
- A2's task or future report;
- hidden material outside the package under audit;
- current maintainer conclusions not listed by the task;
- unrelated Mnemosyne project files.

## Return

Return the complete Fable5 report to the Mnemosyne frontier-clarification validation route. Do not merge it into Project Files or reuse the same project for A2 before both independent reports are complete.
