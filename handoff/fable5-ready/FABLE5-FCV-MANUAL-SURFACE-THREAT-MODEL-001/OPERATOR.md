# Operator Guide — FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001 v0.2

## Purpose and activation

Run one independent static threat model of the proposed manual multi-conversation V0 surface without repeating A1's Advanced Research repository-access failure.

```yaml
active_after: MNEMOSYNE_186_merge
visible_model: Fable_5
visible_effort: Max
Advanced_Research: off_for_entire_run
repository_write: prohibited
validation_execution: prohibited
live_surface_test: prohibited
```

A2 has not yet been executed. This is a preventive surface repair based on A1 run 001.

## Required environment

```yaml
preferred_surface: fresh_standalone_Claude_chat_or_new_one_run_Project
must_be_separate_from_A1: true
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

1. Open a new standalone Claude chat, or a new one-run Project that has never been used for A1 or prior Mnemosyne research.
2. Select visible `Fable 5` and effort `Max`; record the exact text.
3. Keep **Advanced Research off**. Keep ordinary web search off during the repository gate.
4. Click `+ -> Add from GitHub` in the chat.
5. Link/select `08822407d/Mnemosyne`, branch `master`.
6. Confirm the repository link/selection receipt appears, but do not treat it as a file-read receipt.
7. Send the full same-context repository gate below.
8. Continue only when the result is exactly `PASS`, every required path is complete, and the canonical specification reaches `## 14. Delivery and authority boundary`.
9. Stay in the same chat with the same model, effort, mode, and GitHub link.
10. Ordinary web search may now be enabled for current authoritative product facts and targeted support. Advanced Research remains off.
11. Send the substantive launch message below.
12. Do not create live V0 worker/reviewer/adjudicator contexts or perform a live connector experiment.
13. Return the complete threat-model report and input-binding receipt to the current Mnemosyne frontier-clarification validation conversation.

## Copyable full repository gate

```text
Use the GitHub integration read-only. Keep Advanced Research and ordinary web search off. Do not analyze the threat model yet, do not read prior Pro/Fable reports or A1 material, and do not create any live validation context.

First read completely:

1. handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/task.md
2. handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml
3. notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.2.md

Then follow input-manifest.yaml and read every path in every selection_group in this same ordinary chat. This means all 3 support paths and all 12 mandatory audit inputs. Read the canonical threat-model specification through its final heading "## 14. Delivery and authority boundary". Do not accept a sample-path check, visible repository link, prior operator claim, or another context's receipt as a substitute.

Return only the repository_input_binding object defined in the execution contract. Set result PASS only when:

- all 3 support paths are completely readable;
- the canonical specification is complete through its final heading;
- all 12 mandatory audit inputs are completely readable;
- task ID FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001 is visible;
- candidate ID FRONTIER-CLARIFICATION-VALIDATION-MANUAL-SURFACE-CANDIDATE-001 and package ID MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001 are bound at version 0.1.0;
- this exact ordinary chat will execute the threat model;
- Advanced Research is false;
- ordinary web search was not used during the gate;
- no live surface/validation context was created;
- no write action occurred.

If any condition fails, return INPUT_OR_REPOSITORY_INTEGRITY_FAILURE or SURFACE_NOT_SUPPORTED_FOR_REVISED_RUN and stop. Do not start web research or substantive threat modeling.
```

## Gate acceptance checklist

```yaml
result: PASS
support_paths_complete: 3_of_3
mandatory_audit_inputs_complete: 12_of_12
canonical_specification_complete: true
canonical_final_heading: "## 14. Delivery and authority boundary"
Advanced_Research_enabled: false
ordinary_web_search_used_during_gate: false
same_chat_for_future_threat_model: true
live_surface_or_validation_context_created: false
write_action_performed: false
```

## Copyable substantive launch message

```text
The full same-context repository gate passed. Continue in this exact ordinary Fable 5 Max chat. Do not enable Advanced Research, do not change Project/chat/context, do not create live V0 contexts, and do not write GitHub.

Re-read as needed:

- notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.2.md
- notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
- handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml

Execute every substantive requirement and all 22 required report sections in the canonical threat-model specification. The execution contract controls the surface and context: Advanced Research remains off for the entire run. Repository artifacts are primary evidence. Ordinary web search is now allowed for current official product facts and targeted external support only; do not target a large source count or perform a live surface experiment.

Do not use prior Pro/Fable reports, A1 material, Project Memory, unrelated repository files, or any GitHub write action. If repository access is lost, return RUN_INVALIDATED_BY_REPOSITORY_ACCESS_LOSS and do not issue a final disposition. If a time-sensitive product fact cannot be verified, mark the exact claim unknown and narrow the conclusion instead of switching to Advanced Research.

The complete report body must appear in the final response. Include the repository_input_binding receipt, exact visible model/effort text, Advanced_Research_enabled: false, current-fact sources and limitations, any quota/fallback warning, confirmation that no live V0 context was created, and exactly one allowed surface disposition. The exact served backend remains unknown or not attestable unless exact-request provider metadata exists.
```

## Explicit file/folder selection fallback

Select only:

```text
handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/task.md
handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml
notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.2.md
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

Do not add the whole repository. Do not use the existing continuity Project.

## Manual upload fallback

The minimum substantive upload set is 13 files:

```yaml
execution_contract: 1
canonical_threat_model_specification: 1
manual_surface_candidate: 1
required_package_files: 9
Mnemosyne_authority_file: 1
total: 13
```

If manual upload is necessary:

1. obtain all files from the recorded source refs;
2. preserve path and filename in a transfer receipt;
3. upload exactly the 13 files to a new clean ordinary chat/one-run Project;
4. keep Advanced Research off;
5. stop on any missing, transformed, or truncated file.

## Stop conditions

Stop without substantive threat modeling when:

- any support or mandatory input is missing or truncated;
- the canonical specification does not reach its final heading;
- Advanced Research is enabled or required;
- the run moves to another context;
- GitHub access is lost;
- A1/prior reports/Project Memory contaminate the chat;
- a live worker/reviewer/adjudicator context is created;
- a write action is requested or performed;
- the surface cannot support a same-chat ordinary-mode threat model.

## Return

Return the complete ordinary-chat threat-model report, repository-input binding receipt, source table, and any supported export to the current Mnemosyne frontier-clarification validation conversation. Do not add the report to reusable Project Files or reuse this chat/Project for A1.
