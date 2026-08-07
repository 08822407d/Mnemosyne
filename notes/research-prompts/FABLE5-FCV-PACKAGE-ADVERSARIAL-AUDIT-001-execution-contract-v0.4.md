# FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001 — Execution Contract v0.4

> Controls only execution surface, Project-knowledge input delivery, semantic coverage, cost control, and report transfer. The canonical research question, audit criteria, 19 report sections, and allowed dispositions remain unchanged in `FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md`.

```yaml
contract_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-EXECUTION-CONTRACT-004
version: 0.4.0
created_by_task: MNEMOSYNE-195
status: prepared_not_selected_paused_for_quota
supersedes_surface_only:
  - FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.3.md
canonical_specification: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
canonical_research_question_changed: false
repository_write: prohibited
validation_execution: prohibited
```

## 1. Evidence and reason for revision

The completed Project-knowledge probe established that Research could search all 22 manifest paths and recover the canonical/package identity. Claude Project Search mode was active, so byte-complete reading was not attestable, and the probe cost approximately USD 7.

Adjudication:

```text
notes/adjudications/fable5-A1-R0-project-knowledge-search-mode-adjudication-2026-08-07.md
```

Consequences:

```yaml
Project_knowledge_access: empirically_supported
separate_paid_R0: retired_as_disproportionate
byte_complete_read_claim: prohibited
single_combined_Research_invocation: required
```

## 2. Selection state

```yaml
execution_state:
  selected_now: false
  paused_for_quota: true
  future_run_requires:
    - explicit_RUN_disposition
    - operator_acceptance_of_quota_use
    - exact_Project_setup_receipt_PASS
```

Readiness alone does not authorize a run.

## 3. Required surface

```yaml
surface:
  environment: new_one_run_Claude_Project
  Project_display_name: MNE-DR-001 验证包审计
  Project_prior_chats: 0
  Project_Files_before_setup: 0
  Project_Files_after_setup: exact_manifest_set_only
  existing_continuity_Project: prohibited
  Project_Search_mode: allowed_record_required
  visible_model: Fable_5
  visible_effort: Max
  Research_invocations: exactly_1_if_selected
  chat_level_GitHub: disabled
  other_connectors: disabled
  write_capable_tools: disabled
  exact_backend_identity: unknown_or_not_attestable
```

## 4. O0 operator setup gate

Before Research, the operator records:

```yaml
operator_project_setup_receipt:
  task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
  display_name: MNE-DR-001 验证包审计
  Project_name:
  Project_created_new: true
  prior_chat_count: 0
  Project_Files_before_setup: 0
  selected_paths_or_folders: []
  selected_logical_file_count: 22
  unexpected_Project_files: []
  Project_sync_completed: true
  visible_model_selection: Fable_5
  visible_effort_selection: Max
  Project_Search_mode_visible: true | false | unknown
  chat_level_GitHub_disabled: true
  other_connectors_disabled: true
  write_capable_tools_enabled: false
  result: PASS | BLOCKED | INVALID
```

Any extra file, missing file, failed sync, prior chat, or enabled connector blocks the run.

## 5. Required Project knowledge

The exact 22 logical files are listed in `input-manifest.yaml`:

```yaml
support_paths: 3
mandatory_audit_inputs: 19
total_Project_files: 22
```

Required identity:

```yaml
package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
package_version: 0.1.0
canonical_final_heading: "## 17. Delivery and authority boundary"
canonical_required_report_sections: 19
```

A repository hyperlink, ordinary-chat GitHub receipt, raw URL, or prior context's read claim is not an input substitute.

## 6. Single Research invocation — G0 semantic coverage

The selected Research run starts with Project knowledge only. No external web research is allowed until G0 passes.

Required output section:

```yaml
project_knowledge_semantic_coverage:
  task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
  Research_enabled: true
  Project_Files_used: true
  Project_Search_mode_observed_or_reported:
  chat_level_GitHub_used: false
  other_connectors_used: false
  external_web_sources_before_gate: 0
  path_receipts:
    - path:
      path_resolved: true | false
      identity_marker:
      terminal_marker:
      required_semantic_targets: []
      semantic_targets_observed: []
      unresolved_gaps: []
      retrieval_limitation:
  required_path_count: 22
  resolved_path_count:
  canonical_heading_map_complete:
  task_identity_bound:
  package_id:
  package_version:
  required_object_coverage:
    scenario_count_expected: 14
    scenario_IDs_observed: []
    V1_smoke_count_expected: 8
    V2_reserve_count_expected: 6
    hidden_key_count_expected: 14
    hidden_key_IDs_observed: []
    condition_IDs_expected: [Q0, Q1, Q2, Q3, Q4]
    condition_IDs_observed: []
    missing_or_duplicate_items: []
  byte_complete_read_claimed: false
  substantive_findings_started: false
  gate_result: PASS | INPUT_OR_PROJECT_KNOWLEDGE_COVERAGE_FAILURE | INVALID
```

G0 `PASS` requires:

- all 22 paths resolved;
- canonical heading map through section 17;
- correct task/package identity;
- all 14 scenario IDs and all 14 hidden-key IDs accounted for;
- Q0–Q4 accounted for;
- required taskbook/result-package heading maps and terminal boundaries accounted for;
- zero external web source before the gate;
- no substantive package finding yet;
- zero connector or write action.

Search-mode chunk retrieval is acceptable. Missing semantic coverage is not.

If G0 fails, return only the coverage failure object and stop without a canonical audit disposition.

## 7. Same invocation — G1 substantive audit

Only after G0 `PASS`, continue in the same Research invocation and:

1. execute every canonical substantive requirement and all 19 report sections;
2. use Project files as primary evidence;
3. use web sources only as the canonical task permits or requires;
4. distinguish repository evidence, external evidence, and inference;
5. avoid source-count targets and broad exploratory collection unrelated to a concrete finding;
6. return one complete report and exactly one allowed canonical disposition;
7. stop with `RUN_INVALIDATED_BY_PROJECT_KNOWLEDGE_ACCESS_LOSS` if required knowledge becomes unavailable.

## 8. Operator cancellation rule

Cancel if external-web source harvesting begins before G0 coverage is complete. Internal `Searched project for ...` operations are expected under Search mode and are not external-web use.

Record early cancellation as:

```text
RESEARCH_GATE_ORDER_NOT_FOLLOWED
```

Do not repeat the same configuration automatically.

## 9. Output and return

The complete response must include:

- full 19-section report;
- full G0 semantic-coverage ledger;
- the operator setup receipt as operator metadata;
- operator-observed model, effort, Project name, logical file count, and Search-mode indicator;
- source/access/quota limitations and approximate cost;
- `repository_write_performed: false`;
- exactly one canonical disposition, only after G0 `PASS`.

A supported Markdown export is an auxiliary copy of the same report.

## 10. Contamination and stop rules

Stop on:

- prior chats or prior reports;
- A2 material or unrelated Project files;
- missing/extra Project files;
- wrong task/package identity;
- unresolved required semantic coverage;
- connector or write action;
- external web before G0 passes;
- loss of Project knowledge;
- attempt to execute validation rather than audit the package.

## 11. Authority boundary

This contract does not select a V0 execution surface, authorize validation, modify the package, accept a report as authority, or attest the exact backend. Human review and frontier adjudication remain required.
