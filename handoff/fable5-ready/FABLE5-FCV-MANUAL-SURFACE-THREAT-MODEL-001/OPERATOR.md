# Operator Guide — FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001

## Purpose

Run one independent Fable5 threat model of the manual multi-conversation V0 surface candidate. Do not create worker chats, execute V0, modify GitHub, or provide the A1 report before A2 completes.

## Recommended Claude environment

```yaml
preferred_surface: separate_fresh_standalone_chat_or_new_one_run_Project
existing_Mnemosyne_复合评审_Project: not_recommended_for_independent_run
A1_chat_or_Project_reuse: prohibited_before_both_reports_complete
Project_Files: leave_empty_for_preferred_route
GitHub_access: chat_level_plus_Add_from_GitHub
```

## Preferred connector-linked steps

1. Open a new chat that is separate from A1.
2. Select Fable 5 high/xhigh and enable Research only when ready to submit the task.
3. In the chat input, click `+` -> `Add from GitHub`.
4. Select repository `08822407d/Mnemosyne` and branch `master`.
5. Confirm the repository link appears.
6. Send the startup text below.
7. The run must audit exact commit `5e556c2a6dacb41d68bf6209dbf8156b92b79e72`.
8. If any required file cannot be read completely at that commit, stop and use the explicit selection fallback.

## Copyable startup instruction

```text
Use the GitHub connector read-only. First read:

handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/task.md

Then read and execute exactly the canonical task it identifies. Resolve its audit commit to 5e556c2a6dacb41d68bf6209dbf8156b92b79e72 and verify every mandatory path before substantive analysis. Do not use prior Pro/Fable reports, the A1 report, other ready-task directories, Project Memory as evidence, or any GitHub write action. Do not create or test fresh worker contexts. If any required file cannot be read completely at the pinned commit, return only the task-defined input/repository integrity failure.
```

## Explicit GitHub selection fallback

If the current GitHub UI provides a file/folder browser, select exactly:

```text
handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/task.md
notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
notes/validation-designs/frontier-clarification-validation-manual-surface-preparation-candidate-v0.1.md
notes/frontier-clarification-validation-package/                  [entire folder]
current/human-approved-spec.md
```

The package folder contains 15 files. Including the ready entrypoint, canonical task, manual candidate and execution source produces 19 selected files. The canonical task requires only a subset of the package, but selecting the complete package folder is less error-prone and keeps the audit object coherent. Do not add the whole repository.

## Manual upload fallback

If GitHub connector reads fail:

1. download the exact 19-file selection from commit `5e556c2a6dacb41d68bf6209dbf8156b92b79e72`;
2. preserve filenames and record original paths;
3. upload only this set to a new one-run chat/project;
4. do not reuse the A1 project/chat or expose the A1 report;
5. submit the same startup instruction with an uploaded-file receipt.

## Independence and current-product-fact controls

A2 may use current official Anthropic documentation and web research for product facts. It must separate:

- verified official documentation;
- the user's dated UI observations;
- general architecture reasoning;
- unknown or non-attestable product state.

Do not treat the visible repository hyperlink as proof that file reads, context isolation or no-write evidence succeeded.

## Return

Return the complete Fable5 report to the Mnemosyne frontier-clarification validation route. Do not execute the surface, prepare worker packets, authorize V0 or update Project Files with the report before A1 and A2 are independently complete.
