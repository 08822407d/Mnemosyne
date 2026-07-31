# Operator Guide — FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001 v0.2

## Purpose and activation

Run one independent static audit of the merged frontier-clarification validation package without repeating the Advanced Research repository-access failure from run 001.

```yaml
active_after: MNEMOSYNE_186_merge
visible_model: Fable_5
visible_effort: Max
Advanced_Research: off_for_entire_run
repository_write: prohibited
validation_execution: prohibited
prior_Pro_or_Fable_reports: prohibited
```

Do not run this branch-only version before the MNEMOSYNE-186 PR merges unless the maintainer explicitly provides the branch ref and authorizes that non-master run.

## What run 001 established

The canonical task was read completely in the ordinary chat, including its final heading `## 17. Delivery and authority boundary`. The failure occurred after Advanced Research was enabled: its executor reported that only the canonical task remained accessible and that all 18 package/source inputs were inaccessible. No substantive package audit was produced.

The revised run therefore keeps the repository gate and complete audit in the same ordinary chat.

## Required environment

```yaml
preferred_surface: fresh_standalone_Claude_chat_or_new_one_run_Project
existing_Mnemosyne_复合评审_Project: do_not_use
Project_Files: empty
Project_Instructions: none_task_specific
prior_task_chats_or_reports: absent
visible_model: Fable_5
visible_effort: Max
Advanced_Research: off
ordinary_web_search_initially: off
GitHub_access: chat_level_plus_Add_from_GitHub
```

## Ordered operator flow

1. Open a fresh standalone Claude chat, or a new one-run Project with no prior chats, Files, Instructions, or task memory.
2. Select visible `Fable 5` and effort `Max`; record the exact visible text.
3. Keep **Advanced Research off**. Keep ordinary web search off during the repository gate.
4. In the chat input, click `+ -> Add from GitHub`.
5. Link/select repository `08822407d/Mnemosyne`, branch `master`.
6. Confirm that a link or selection receipt appears. This is not yet proof of file access.
7. Send the full same-context repository gate below.
8. Continue only when its result is exactly `PASS`, every required path is complete, and the canonical specification reaches its final heading.
9. Do not change chat, Project, model, effort, GitHub link, or mode.
10. Ordinary web search may now be enabled for targeted external evidence. Advanced Research remains off.
11. Send the substantive launch message below.
12. Return the complete final report and input-binding receipt to the current Mnemosyne frontier-clarification validation conversation.

## Copyable full repository gate

```text
Use the GitHub integration read-only. Keep Advanced Research and ordinary web search off. Do not analyze the package yet and do not read prior Pro/Fable reports or A2 material.

First read completely:

1. handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/task.md
2. handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml
3. notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.2.md

Then follow input-manifest.yaml and read every path in every selection_group in this same ordinary chat. This means all 3 support paths and all 19 mandatory audit inputs. Read the canonical audit specification through its final heading "## 17. Delivery and authority boundary". Do not accept a sample-path check, visible repository link, prior operator claim, or another context's receipt as a substitute.

Return only the repository_input_binding object defined in the execution contract. Set result PASS only when:

- all 3 support paths are completely readable;
- the canonical specification is complete through its final heading;
- all 19 mandatory audit inputs are completely readable;
- task ID FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001 is visible;
- package ID MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001 and version 0.1.0 are bound;
- this exact ordinary chat will execute the audit;
- Advanced Research is false;
- ordinary web search was not used during the gate;
- no write action occurred.

If any condition fails, return INPUT_OR_REPOSITORY_INTEGRITY_FAILURE or SURFACE_NOT_SUPPORTED_FOR_REVISED_RUN and stop. Do not start web research or substantive audit.
```

## Gate acceptance checklist

Proceed only when all are true:

```yaml
result: PASS
support_paths_complete: 3_of_3
mandatory_audit_inputs_complete: 19_of_19
canonical_specification_complete: true
canonical_final_heading: "## 17. Delivery and authority boundary"
Advanced_Research_enabled: false
ordinary_web_search_used_during_gate: false
same_chat_for_future_audit: true
write_action_performed: false
```

A claim such as “the files were accessible before Research” is insufficient. The run must never enter Advanced Research.

## Copyable substantive launch message

```text
The full same-context repository gate passed. Continue in this exact ordinary Fable 5 Max chat. Do not enable Advanced Research, do not change Project/chat/context, and do not write GitHub.

Re-read as needed:

- notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.2.md
- notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
- handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml

Execute every substantive requirement and all 19 required report sections in the canonical audit specification. The execution contract controls the surface and context: Advanced Research remains off for the entire run. Repository artifacts are primary evidence. Ordinary web search is now allowed only where external evidence materially changes a concrete finding; do not target a large source count or begin broad source harvesting.

Do not use prior Pro/Fable reports, A2 material, Project Memory, unrelated repository files, or any GitHub write action. If repository access is lost or a required file becomes unreadable, return RUN_INVALIDATED_BY_REPOSITORY_ACCESS_LOSS and do not issue a final disposition.

The complete report body must appear in the final response. Include the repository_input_binding receipt, exact visible model/effort text, Advanced_Research_enabled: false, web/source limitations, any quota/fallback warning, and exactly one allowed static-audit disposition. The exact served backend remains unknown or not attestable unless exact-request provider metadata exists.
```

## Explicit file/folder selection fallback

When the GitHub UI exposes explicit selection, select:

```text
handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/task.md
handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml
notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.2.md
notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
notes/frontier-clarification-validation-package/                       [entire folder]
notes/validation-designs/frontier-planning-clarification-handoff-read-only-validation-v0.1.md
notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/03-cross-report-consensus-conflict-and-adjudication.md
notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/04-interim-architecture-and-validation-decision.md
```

Do not add the whole repository or use the existing continuity Project.

## Manual upload fallback

The minimum substantive upload set is 20 files:

```yaml
execution_contract: 1
canonical_audit_specification: 1
package_files: 15
external_design_and_adjudication_files: 3
total: 20
```

This may reach a per-chat upload boundary. Prefer connector or folder selection. If manual upload is used:

1. obtain all files from the recorded source refs;
2. preserve path and filename in a transfer receipt;
3. upload exactly the 20 files to a fresh ordinary chat/one-run Project;
4. keep Advanced Research off;
5. stop on any omission, transformation, truncation, or limit warning.

## Stop conditions

Stop without substantive audit when:

- any support or mandatory input is missing or truncated;
- the canonical specification does not reach its final heading;
- Advanced Research is enabled or required;
- the run moves to another context;
- GitHub access is lost;
- prior reports/A2 material/Project Memory contaminate the chat;
- a write action is requested or performed;
- the surface cannot support a same-chat ordinary-mode audit.

## Return

Return the complete ordinary-chat report, repository-input binding receipt, and any supported export to the current Mnemosyne frontier-clarification validation conversation. Do not add the report to reusable Project Files and do not reuse this chat/Project for A2.
