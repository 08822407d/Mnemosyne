# FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001 — Execution Contract v0.3

> This version controls only execution surface, input delivery, cost gate and report transfer. The canonical research question, audit criteria, 19 report sections and allowed dispositions remain in `FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md`.

```yaml
contract_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-EXECUTION-CONTRACT-003
version: 0.3.0
created_by_task: MNEMOSYNE-188
status: active_after_MNEMOSYNE_188_merge
supersedes_surface_only:
  - FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.2.md
canonical_specification: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
canonical_research_question_changed: false
repository_write: prohibited
validation_execution: prohibited
```

## 1. Required surface

```yaml
surface:
  environment: new_one_run_Claude_Project
  Project_prior_chats: 0
  Project_Files_before_setup: 0
  Project_Files_after_setup: exact_manifest_set_only
  existing_continuity_Project: prohibited
  visible_model: Fable_5
  visible_effort: Max
  Research:
    R0_probe: enabled
    R1_substantive_report: enabled_only_after_R0_PASS
  chat_level_GitHub_during_R0_or_R1: disabled
  other_connectors_during_R0_or_R1: disabled
  web_search:
    required_by_product_for_Research: true
    external_collection_during_R0: prohibited
    external_collection_during_R1: allowed_under_canonical_task
  exact_backend_identity: unknown_or_not_attestable
```

## 2. Direct input surface

All required material must be placed into **Project Files/Project knowledge** before Research begins. A chat-level repository link, an ordinary-chat connector receipt, raw GitHub URLs or a prior context's read result do not satisfy this contract.

Required Project Files are every path in `input-manifest.yaml` selection groups:

```yaml
counts:
  support_paths: 3
  mandatory_audit_inputs: 19
  total_Project_files: 22
```

The canonical specification must be complete through:

```text
## 17. Delivery and authority boundary
```

The package identity must be:

```yaml
package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
package_version: 0.1.0
```

## 3. Project instructions

Use a minimal instruction block:

```text
One-run read-only A1 audit Project. Use only the explicitly selected Project Files as internal repository evidence. Do not write GitHub or any connected service. Do not use prior Pro/Fable reports, A2 material, prior chats or unrelated Mnemosyne files. Treat the canonical task as instructions and the validation package as the audit object, not authority.
```

Project instructions do not replace the canonical task or this contract.

## 4. R0 Research-direct visibility probe

R0 must occur inside Research in the same Project intended for R1.

Required output:

```yaml
research_project_knowledge_probe:
  task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
  Project_name:
  visible_model_text:
  visible_effort_text:
  Research_enabled: true
  Project_Files_used: true
  chat_level_GitHub_used: false
  other_connectors_enabled: false
  exact_file_receipts:
    - path:
      complete_read: true | false
      visible_ID_or_first_heading:
      final_heading_or_end_marker:
      limitation:
  support_paths_complete: 0_to_3
  mandatory_audit_inputs_complete: 0_to_19
  canonical_specification_complete:
  package_id:
  package_version:
  external_web_sources_used: 0
  repository_write_performed: false
  substantive_audit_started: false
  result: PASS | INPUT_OR_PROJECT_KNOWLEDGE_INTEGRITY_FAILURE | RESEARCH_SURFACE_NOT_SUPPORTED | INVALID
```

`PASS` requires:

- 22/22 required Project files readable;
- canonical task complete through its final heading;
- package ID/version match;
- no external web source collection;
- no substantive findings or disposition;
- no connector or write action.

If Research starts broad external collection before the Project-file gate completes, the operator cancels the run and records `RESEARCH_SURFACE_NOT_SUPPORTED_OR_NOT_FOLLOWING_GATE`.

## 5. R1 substantive audit

R1 is authorized only after R0 `PASS` and remains in the same Project/chat.

R1 must:

1. re-read this contract, the canonical specification and manifest from Project knowledge;
2. execute every canonical substantive requirement and all 19 report sections;
3. use Project files as primary evidence;
4. use web sources only where the canonical task permits or requires them;
5. distinguish repository evidence, external evidence and inference;
6. return one complete report and exactly one allowed canonical disposition;
7. stop with `RUN_INVALIDATED_BY_PROJECT_KNOWLEDGE_ACCESS_LOSS` if a required file becomes unavailable.

## 6. Output and return

The final response must contain:

- complete report body;
- the R0 `research_project_knowledge_probe` receipt;
- exact visible model and effort text;
- Project name and exact selected file count;
- whether Project RAG was visibly indicated;
- source and access limitations;
- quota/fallback warnings;
- `repository_write_performed: false`;
- exactly one canonical disposition.

A supported Markdown export is an auxiliary copy of the same report, not a second report.

## 7. Stop and contamination rules

Stop when:

- any Project file is missing, truncated or wrong-task;
- Project contains prior chats, prior reports, A2 material or unrelated files;
- Research cannot access Project knowledge;
- GitHub or another connector remains enabled for the run;
- a write action is proposed or performed;
- canonical task identity or final heading is missing;
- package ID/version is mismatched;
- R0 begins substantive analysis or external-web harvesting;
- R1 loses required Project knowledge access.

## 8. Authority boundary

This contract does not select a V0 execution surface, authorize validation, modify the package, accept the report as authority, or attest the exact backend. Human review and frontier adjudication remain required after report return.