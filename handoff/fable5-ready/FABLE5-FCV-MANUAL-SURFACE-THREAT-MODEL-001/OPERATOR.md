# Operator Guide — FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001

## Purpose

Run one independent Fable5 threat model of the proposed manual multi-conversation V0 surface. This is a static review only: do not create V0 worker contexts, transfer live packets, modify GitHub or execute validation.

## Recommended Claude environment

```yaml
preferred_surface: fresh_standalone_chat_or_new_one_run_Project
must_be_separate_from_A1: true
existing_Mnemosyne_复合评审_Project: not_recommended_for_this_independent_run
Project_Files: leave_empty_for_preferred_route
Project_Instructions: none_task_specific
prior_task_chats_or_reports: absent
visible_model: Fable_5
visible_effort: Max
GitHub_access: chat_level_plus_Add_from_GitHub
Research_initially: off
```

## Preferred connector-linked steps

1. Open a new chat or one-run Project that has not been used for A1 or prior Mnemosyne research.
2. Select visible model `Fable 5` and effort `Max`. Record the exact visible text.
3. Keep Research off.
4. Click `+` -> `Add from GitHub` in the chat.
5. Select or link repository `08822407d/Mnemosyne`, branch `master`.
6. Confirm the repository link or selection receipt appears, but do not treat it as proof of file access.
7. Send the connector preflight below.
8. Continue only if all four files are read completely and the expected task/candidate IDs are visible.
9. Enable Research and web search.
10. Send the Research startup instruction.
11. The task must verify every manifest path before analysis and verify current Claude/platform claims from authoritative current sources.
12. If integrity fails, stop and use explicit selection or upload in a new clean run. Do not repair the run inside a contaminated Project.

## Copyable connector preflight

```text
Use the GitHub integration read-only. Research must remain off. Do not analyze the threat model and do not read prior reports.

Read exactly these four files:

1. handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/task.md
2. handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml
3. notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
4. notes/validation-designs/frontier-clarification-validation-manual-surface-preparation-candidate-v0.1.md

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

Expected visible identities include task ID FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001 and candidate ID FRONTIER-CLARIFICATION-VALIDATION-MANUAL-SURFACE-CANDIDATE-001. A visible GitHub hyperlink without complete reads is a failure. Do not write GitHub and do not create any validation context.
```

## Copyable Research startup instruction

```text
Research is now authorized for this one read-only static threat-model report. Use the GitHub integration read-only.

Re-read:

handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/task.md
handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml

Then read and execute exactly the canonical task they identify:

notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md

Before substantive analysis, verify every mandatory repository path. Bind the audit object to candidate ID FRONTIER-CLARIFICATION-VALIDATION-MANUAL-SURFACE-CANDIDATE-001 version 0.1.0 and package ID MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001 version 0.1.0. The candidate was merged at 5e556c2a6dacb41d68bf6209dbf8156b92b79e72. If the current Claude UI exposes only branch-level access, verify exact paths, IDs, versions and consistency and state any remaining commit-attestation limitation explicitly.

Do not use Project Memory as evidence, prior Pro/Fable reports, A1 materials, other ready-task directories or any GitHub write action. Do not create fresh worker/reviewer contexts or execute a live connector experiment; this task is a static threat model. Verify time-sensitive product facts from current authoritative sources and distinguish them from the user's 2026-07-30 UI observations.

If any mandatory file is missing, unreadable, truncated or mismatched, return only the canonical task's INPUT_OR_REPOSITORY_INTEGRITY_FAILURE object.

The final response must contain the complete report body. Record the exact visible model and effort text and any UI fallback or quota warning, but do not infer the exact served backend.
```

## Explicit file/folder selection fallback

Select only:

```text
handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/task.md
handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml
notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
notes/validation-designs/frontier-clarification-validation-manual-surface-preparation-candidate-v0.1.md
notes/frontier-clarification-validation-package/README.md
notes/frontier-clarification-validation-package/01-protocol-spec-v0.1.md
notes/frontier-clarification-validation-package/02-condition-contracts-q0-q4-v0.1.md
notes/frontier-clarification-validation-package/04-hidden-author-keys-v0.1.md
notes/frontier-clarification-validation-package/07-reviewer-and-adjudication-taskbook-v0.1.md
notes/frontier-clarification-validation-package/08-v0-sentinel-context-isolation-taskbook-v0.1.md
notes/frontier-clarification-validation-package/10-run-manifest-template-v0.1.md
notes/frontier-clarification-validation-package/11-result-return-and-maintainer-review-package-v0.1.md
notes/frontier-clarification-validation-package/12-execution-surface-and-user-decision-package-v0.1.md
current/human-approved-spec.md
```

Do not add the whole repository. If persistent selection is unavoidable, use a new one-run Project separate from A1 and the existing continuity Project.

## Manual upload fallback

The minimum upload set is 12 files: the canonical task, manual-surface candidate, nine required package files and `current/human-approved-spec.md`.

1. download them from the recorded source ref;
2. preserve path and filename in a transfer receipt;
3. upload exactly those files to a new clean chat/project;
4. replace connector receipts with the transfer receipt;
5. stop on any missing, transformed or truncated file.

## Independence controls

Do not expose:

- the foundational Pro or Fable reports;
- A1's task or report;
- previous manual-surface conclusions from another model;
- unrelated repository files;
- existing Project Memory or prior Mnemosyne chats.

## Return

Return the complete Fable5 report to the current Mnemosyne frontier-clarification validation conversation. Do not add it to reusable Project Files or reuse this chat/Project for A1.
