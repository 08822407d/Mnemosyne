# FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001 — Execution Contract v0.3

> This version controls only execution surface, direct Project-knowledge input delivery, cost gate and report transfer. The canonical research question, threat-model scope, 22 report sections and allowed dispositions remain in `FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md`.

```yaml
contract_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-EXECUTION-CONTRACT-003
version: 0.3.0
created_by_task: MNEMOSYNE-188
status: active_after_MNEMOSYNE_188_merge_and_later_A2_selection
supersedes_surface_only:
  - FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.2.md
canonical_specification: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
canonical_research_question_changed: false
repository_write: prohibited
validation_execution: prohibited
live_surface_test: prohibited
```

## 1. Dependency and selection

```yaml
A2_execution_state:
  prepared: true
  selected_now: false
  prerequisite:
    - valid_A1_report_returned_and_adjudicated
    - A2_audit_object_confirmed_still_current
  default_without_later_selection: DEFERRED
```

This contract may be used only after a later explicit `RUN_*` decision. It is prepared now so no additional design turn is needed if A2 remains decision-relevant.

## 2. Required surface

```yaml
surface:
  environment: new_one_run_Claude_Project_separate_from_A1
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
    external_collection_during_R1: current_official_facts_and_targeted_support
  live_worker_reviewer_or_adjudicator_contexts: prohibited
  exact_backend_identity: unknown_or_not_attestable
```

## 3. Direct input surface

All required material must be placed into Project Files/Project knowledge before Research begins. Chat-level GitHub reads, raw URLs or A1 receipts are not substitutes.

Required Project Files are every path in `input-manifest.yaml` selection groups:

```yaml
counts:
  support_paths: 3
  mandatory_audit_inputs: 12
  total_Project_files: 15
```

The canonical specification must be complete through:

```text
## 14. Delivery and authority boundary
```

Required identities:

```yaml
candidate_id: FRONTIER-CLARIFICATION-VALIDATION-MANUAL-SURFACE-CANDIDATE-001
candidate_version: 0.1.0
package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
package_version: 0.1.0
```

## 4. Project instructions

```text
One-run read-only A2 threat-model Project, separate from A1. Use only the explicitly selected Project Files as internal repository evidence. Do not write GitHub or any connected service. Do not use prior Pro/Fable reports, A1 material, prior chats or unrelated Mnemosyne files. Do not create or inspect live V0 worker, reviewer, adjudicator or connector-test contexts. Treat the canonical task as instructions and the manual-surface candidate as an audit object, not authority.
```

## 5. R0 Research-direct visibility probe

Required output:

```yaml
research_project_knowledge_probe:
  task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
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
  mandatory_audit_inputs_complete: 0_to_12
  canonical_specification_complete:
  candidate_id:
  candidate_version:
  package_id:
  package_version:
  external_web_sources_used: 0
  live_surface_or_validation_context_created: false
  repository_write_performed: false
  substantive_threat_model_started: false
  result: PASS | INPUT_OR_PROJECT_KNOWLEDGE_INTEGRITY_FAILURE | RESEARCH_SURFACE_NOT_SUPPORTED | INVALID
```

`PASS` requires 15/15 files readable, correct final heading and identities, no external web collection, no live validation context, no substantive finding and no write.

If R0 begins broad external collection before input binding completes, the operator cancels the run.

## 6. R1 substantive threat model

After R0 `PASS`, remain in the same Project/chat and:

1. re-read this contract, canonical task and manifest from Project knowledge;
2. execute all canonical requirements and all 22 report sections;
3. verify time-sensitive product claims from current authoritative sources;
4. use the selected Project files as primary internal evidence;
5. do not create live V0 contexts or conduct a live connector experiment;
6. return one complete report and exactly one allowed canonical disposition;
7. return `RUN_INVALIDATED_BY_PROJECT_KNOWLEDGE_ACCESS_LOSS` if a required Project file becomes unavailable.

## 7. Output and return

Return:

- complete threat-model report;
- R0 receipt;
- exact visible model/effort;
- Project name and selected file count;
- visible Project RAG indication, if any;
- current product-fact sources and limitations;
- confirmation no live V0 context was created;
- quota/fallback warnings;
- `repository_write_performed: false`;
- exactly one canonical surface disposition.

A Markdown export is an auxiliary copy of the same report.

## 8. Stop and contamination rules

Stop when:

- any required Project file is missing, truncated or wrong-task;
- Project contains A1 material, prior reports, prior chats or unrelated files;
- Research cannot access Project knowledge;
- GitHub or another connector remains enabled;
- a live V0 context or connector experiment is created;
- a write action occurs;
- canonical task identity/final heading is missing;
- candidate/package identity mismatches;
- R0 performs substantive analysis or external harvesting;
- R1 loses Project knowledge access.

## 9. Authority boundary

This contract does not select the manual surface, authorize V0/V1, accept a run-scoped exception, modify Mnemosyne's execution source or attest the exact backend. Human and frontier adjudication remain required.