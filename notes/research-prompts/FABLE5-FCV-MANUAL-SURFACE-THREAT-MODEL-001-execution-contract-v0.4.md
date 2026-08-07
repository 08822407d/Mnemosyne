# FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001 — Execution Contract v0.4

> Controls only execution surface, Project-knowledge input delivery, semantic coverage, cost control, and report transfer. The canonical research question, threat-model scope, 22 report sections, and allowed dispositions remain unchanged in `FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md`.

```yaml
contract_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-EXECUTION-CONTRACT-004
version: 0.4.0
created_by_task: MNEMOSYNE-195
status: prepared_deferred_not_selected
supersedes_surface_only:
  - FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.3.md
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
  default: DEFERRED_PENDING_VALID_A1_ADJUDICATION
  prerequisite:
    - valid_A1_report_returned_and_adjudicated
    - A2_audit_object_confirmed_current
    - explicit_RUN_disposition
    - operator_acceptance_of_quota_use
```

This contract does not authorize Project creation or Research execution by readiness alone.

## 2. Surface correction inherited from A1 evidence

The A1 Project-knowledge probe established that Research can use selected Project knowledge under Search mode, while a separate exhaustive paid probe is expensive and cannot attest byte-complete reading.

A2 therefore uses the same v0.4 architecture:

```text
O0 operator/UI setup receipt
  -> one Research invocation
       G0 internal semantic-coverage gate
       G1 substantive threat model only after G0 PASS
```

No separate paid R0 is permitted.

## 3. Required surface

```yaml
surface:
  environment: new_one_run_Claude_Project_separate_from_A1
  Project_display_name: MNE-DR-002 表面威胁
  Project_prior_chats: 0
  Project_Files_before_setup: 0
  Project_Files_after_setup: exact_manifest_set_only
  existing_continuity_Project: prohibited
  Project_Search_mode: allowed_record_required
  visible_model: Fable_5
  visible_effort: Max
  Research_invocations: exactly_1_if_later_selected
  chat_level_GitHub: disabled
  other_connectors: disabled
  write_capable_tools: disabled
  live_worker_reviewer_or_adjudicator_contexts: prohibited
  exact_backend_identity: unknown_or_not_attestable
```

## 4. O0 operator setup gate

```yaml
operator_project_setup_receipt:
  task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
  display_name: MNE-DR-002 表面威胁
  Project_name:
  Project_created_new_and_separate_from_A1: true
  prior_chat_count: 0
  Project_Files_before_setup: 0
  selected_paths: []
  selected_logical_file_count: 15
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

Any wrong/missing/extra file, prior chat, failed sync, connector, or A1 material blocks the run.

## 5. Required Project knowledge

```yaml
support_paths: 3
mandatory_audit_inputs: 12
total_Project_files: 15
canonical_final_heading: "## 14. Delivery and authority boundary"
canonical_required_report_sections: 22
candidate_id: FRONTIER-CLARIFICATION-VALIDATION-MANUAL-SURFACE-CANDIDATE-001
candidate_version: 0.1.0
package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
package_version: 0.1.0
```

## 6. Single Research invocation — G0 semantic coverage

G0 uses Project knowledge only. No external web research and no live V0/surface context are allowed before the gate.

Required output section:

```yaml
project_knowledge_semantic_coverage:
  task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
  Research_enabled: true
  Project_Files_used: true
  Project_Search_mode_observed_or_reported:
  chat_level_GitHub_used: false
  other_connectors_used: false
  external_web_sources_before_gate: 0
  live_surface_or_validation_context_created: false
  path_receipts:
    - path:
      path_resolved: true | false
      identity_marker:
      terminal_marker:
      required_semantic_targets: []
      semantic_targets_observed: []
      unresolved_gaps: []
      retrieval_limitation:
  required_path_count: 15
  resolved_path_count:
  canonical_heading_map_complete:
  task_identity_bound:
  candidate_id:
  candidate_version:
  package_id:
  package_version:
  required_object_coverage:
    condition_IDs_expected: [Q0, Q1, Q2, Q3, Q4]
    condition_IDs_observed: []
    hidden_key_count_expected: 14
    hidden_key_IDs_observed: []
    required_heading_maps_complete:
    missing_or_duplicate_items: []
  byte_complete_read_claimed: false
  substantive_findings_started: false
  gate_result: PASS | INPUT_OR_PROJECT_KNOWLEDGE_COVERAGE_FAILURE | INVALID
```

G0 `PASS` requires all 15 paths, correct identities and final heading, Q0–Q4, all 14 hidden-key IDs, complete required heading maps, no external web source, no live context, no substantive finding, and no connector/write action.

If G0 fails, return only the coverage failure and stop without a surface disposition.

## 7. Same invocation — G1 substantive threat model

Only after G0 `PASS`:

1. execute all canonical requirements and all 22 report sections;
2. verify time-sensitive product facts from current authoritative sources;
3. use Project files as primary internal evidence;
4. distinguish Project evidence, external evidence, and inference;
5. create no live worker/reviewer/adjudicator or connector-test context;
6. return one complete report and exactly one allowed canonical disposition;
7. return `RUN_INVALIDATED_BY_PROJECT_KNOWLEDGE_ACCESS_LOSS` if required knowledge is lost.

## 8. Operator cancellation and cost control

Cancel if external-web source harvesting begins before G0 completes. Internal Project Search operations are expected.

```yaml
cost_controls:
  separate_paid_visibility_probe: prohibited
  Research_invocations_if_selected: 1
  source_count_target: none
  identical_failed_configuration_retry: prohibited
  automatic_A2_run: prohibited
```

## 9. Output and return

Return:

- complete 22-section threat-model report;
- complete G0 semantic-coverage ledger;
- operator setup receipt as operator metadata;
- model/effort/Project/Search-mode observations;
- current product sources and limitations;
- confirmation no live V0 context was created;
- approximate cost and quota/fallback warnings;
- `repository_write_performed: false`;
- exactly one canonical disposition only after G0 `PASS`.

## 10. Stop and contamination rules

Stop on:

- absent A1 adjudication or stale A2 audit object;
- prior chats, prior reports, A1 material, or unrelated files;
- missing/extra Project files;
- wrong task/candidate/package identity;
- unresolved semantic coverage;
- connector/write action;
- external web before G0;
- live validation context creation;
- loss of Project knowledge.

## 11. Authority boundary

This contract does not select the manual surface, authorize V0/V1, accept an exception, modify Mnemosyne's execution source, or attest the exact backend. Human and frontier adjudication remain required.
