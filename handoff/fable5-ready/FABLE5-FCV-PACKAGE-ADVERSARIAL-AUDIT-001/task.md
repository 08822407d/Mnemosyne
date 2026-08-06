# Ready Task — FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001

```yaml
queue_status: READY_AFTER_MNEMOSYNE_188_MERGE_RESEARCH_PROJECT_PROBE_REQUIRED
task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
display_name: MNE-DR-001 验证包审计
display_name_registry: notes/registries/project-research-display-name-registry-v0.1.md
canonical_audit_specification: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
active_execution_contract: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.3.md
operator_guide: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/OPERATOR.md
input_manifest: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml
exact_topic: Independent adversarial static audit of the Mnemosyne frontier-clarification validation package before any execution-surface or V0 authorization
source_package_commit: 67eb96d5317a2bb589236a4a8b2e75be2508d830
repository_access: read_only
repository_write: prohibited
validation_execution: prohibited
prior_Pro_or_Fable_reports: prohibited
preferred_visible_model: Fable_5
preferred_effort: Max
Research:
  R0_Project_knowledge_probe: required
  R1_substantive_report: allowed_only_after_R0_PASS
Project_Files: exact_manifest_set_only
chat_level_GitHub_during_Research: prohibited
canonical_research_question_and_output_contract_changed: false
```

## Prior attempt and repairs

```yaml
run_001:
  ordinary_chat_preflight: PASS
  canonical_specification_complete_read: true
  Advanced_Research_repository_inputs_accessible: 1_of_19
  result: INPUT_OR_REPOSITORY_INTEGRITY_FAILURE
  substantive_audit_started: false
  accepted_as_surface_failure_evidence_only: true
  operator_reported_cost_USD_approx: 8

v0_2:
  repair: keep_Research_off_and_complete_in_same_ordinary_chat
  status: conservative_fallback_not_executed

v0_3:
  repair: place_exact_inputs_in_new_one_run_Project_Files_then_probe_Research_direct_Project_knowledge_access
  status: current_candidate_after_MNEMOSYNE_188_merge
```

## Required v0.3 run

1. create a new one-run Claude Project named `MNE-DR-001 验证包审计` with no prior chats, Files or task memory;
2. select visible `Fable 5` and `Max`;
3. add exactly the manifest-listed task inputs to **Project Files** using the Project-level GitHub file/folder selector, then sync;
4. do not add the whole repository;
5. disable chat-level GitHub and all other connectors before Research;
6. enable Research and run the R0 Project-knowledge visibility probe from `OPERATOR.md`;
7. cancel if R0 begins broad external web collection before completing the Project-file gate;
8. continue to R1 only after R0 returns `PASS` for 22/22 required files;
9. keep the same Project/chat/model/effort for R1;
10. return the complete report and R0 receipt to the current Mnemosyne frontier-clarification validation route.

A repository hyperlink, ordinary-chat GitHub receipt, raw URL or prior context's read claim is not accepted as Research input proof. A failed R0 stops the run before the substantive audit.
