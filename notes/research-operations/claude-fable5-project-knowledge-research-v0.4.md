# Claude/Fable5 Project-Knowledge Research Workflow v0.4

> Non-execution-source operating guidance for the two Mnemosyne frontier-clarification Stage-A Fable tasks. This version incorporates the completed A1 Project-knowledge probe, accepts Claude Project Search mode, removes the separate paid full-inventory probe, and requires one combined Research invocation with an internal semantic-coverage gate. It does not execute Fable, spend quota, modify the validation package, select an execution surface, or authorize V0/V1.

```yaml
workflow_id: MNEMOSYNE-FABLE5-PROJECT-KNOWLEDGE-RESEARCH-001
version: 0.4.0
created_by_task: MNEMOSYNE-195
status: prepared_not_selected_not_executed
repository: 08822407d/Mnemosyne
execution_source: current/human-approved-spec.md
execution_source_modified: false
supersedes_surface_only:
  - notes/research-operations/claude-fable5-project-knowledge-research-v0.3.md
applies_to:
  - FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
  - FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
```

## 1. Evidence incorporated

### Run 001 — ordinary-chat connector transition failure

```text
ordinary chat GitHub read
  -> preflight PASS
  -> enable Research
  -> Research retrieves canonical task only
  -> remaining primary inputs unavailable
  -> INPUT_OR_REPOSITORY_INTEGRITY_FAILURE
```

This disproved ordinary-chat connector inheritance as a sufficient gate for that run.

### A1 Project-knowledge R0 — access succeeded, cost gate failed

The later one-run Project placed the task files in Project knowledge before Research. The Research-direct receipt located all 22 manifest paths, recovered the canonical final heading and package identity, used no external web source, and reported no write or substantive audit.

The same run showed:

- Project Search mode/RAG was active;
- byte-complete reading was not mechanically attestable;
- some repeated records and interior sections were not individually surfaced;
- one extra same-task `OPERATOR.md` was selected by operator error;
- the probe cost approximately USD 7.

Adjudication:

```text
notes/adjudications/
fable5-A1-R0-project-knowledge-search-mode-adjudication-2026-08-07.md
```

## 2. Design correction

v0.3 coupled two expensive goals:

```yaml
- prove_Research_can_use_Project_knowledge
- exhaustively_check_22_long_files_before_substantive_work
```

In Search mode, exhaustive semantic coverage requires many retrievals and is not a low-cost visibility test. A second Research invocation for the report duplicates paid setup and retrieval work.

v0.4 therefore uses:

```text
O0 — operator/UI setup and exact-file receipt, no Research quota
  -> one Research invocation
       G0 — internal semantic-coverage gate, Project knowledge only
       G1 — substantive report, only if G0 passes
```

There is no separate paid R0.

## 3. Required Project surface

```yaml
surface:
  environment: new_one_run_Claude_Project
  Project_prior_chats: 0
  Project_Files_before_setup: 0
  Project_Files_after_setup: exact_manifest_set_only
  existing_continuity_Project: prohibited
  Project_Search_mode: allowed_and_must_be_recorded
  visible_model: Fable_5
  visible_effort: Max
  Research_invocations_planned: 1
  chat_level_GitHub_during_run: disabled
  other_connectors_during_run: disabled
  repository_write: prohibited
  exact_backend_identity: unknown_or_not_attestable
```

Project Search mode is not a failure. It changes the evidence claim from “all bytes loaded at once” to “required semantic coverage retrieved and recorded.”

## 4. O0 operator setup and inventory gate

O0 occurs before Research and does not ask the model to attest UI-only facts.

Required operator receipt:

```yaml
operator_project_setup_receipt:
  task_id:
  display_name:
  Project_name:
  Project_created_new: true
  prior_chat_count: 0
  Project_Files_before_setup: 0
  selected_paths_or_folders: []
  selected_logical_file_count:
  unexpected_Project_files: []
  Project_sync_completed: true
  visible_model_selection:
  visible_effort_selection:
  Project_Search_mode_visible: true | false | unknown
  chat_level_GitHub_disabled: true
  other_connectors_disabled: true
  write_capable_tools_enabled: false
  operator_limitations: []
  result: PASS | BLOCKED | INVALID
```

The operator removes any accidental extra file before starting the Research invocation. UI facts remain operator-observed, not model-attested.

O0 fails on:

- wrong Project or nonzero prior chats;
- missing or extra Project files;
- failed sync;
- wrong task material;
- connector/tool not disabled;
- inability to distinguish A1 and A2 Projects.

## 5. One Research invocation with two phases

### G0 — internal semantic-coverage gate

G0 runs inside the same Research invocation that may later produce the report.

G0 must use Project knowledge only and must not begin external web research. It returns a structured coverage ledger before any canonical disposition.

Required ledger shape:

```yaml
project_knowledge_semantic_coverage:
  task_id:
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
  required_path_count:
  resolved_path_count:
  task_identity_bound:
  package_or_candidate_identity_bound:
  required_object_coverage:
    expected_counts: {}
    observed_IDs_or_heading_maps: {}
    missing_or_duplicate_items: []
  byte_complete_read_claimed: false
  substantive_findings_started: false
  gate_result: PASS | INPUT_OR_PROJECT_KNOWLEDGE_COVERAGE_FAILURE | INVALID
```

The ledger must not use the ambiguous `complete_read: true` field.

Examples of semantic targets:

- manifest: every required path and count;
- canonical specification: complete heading map through the final authority boundary;
- scenario set: all 14 scenario IDs and 8/6 phase counts;
- hidden keys: all 14 matching key IDs without reproducing unnecessary hidden answer content;
- Q0–Q4 contract: all five condition IDs;
- taskbooks and result packages: full heading maps and required terminal boundaries;
- external adjudication inputs: identity and final disposition/boundary headings.

G0 `PASS` means required semantic coverage is sufficient to perform the task; it does not mean every byte was loaded simultaneously.

If any required item is unresolved, return only the coverage failure object and stop without a package/surface disposition.

### G1 — substantive report

Only after G0 `PASS`, the same Research invocation may:

- begin external web research permitted by the canonical task;
- perform the complete audit/threat model;
- distinguish Project-file evidence, external evidence, and inference;
- return every required report section;
- return exactly one canonical disposition;
- include the complete G0 ledger and all access limitations.

If Project knowledge becomes unavailable, return `RUN_INVALIDATED_BY_PROJECT_KNOWLEDGE_ACCESS_LOSS` without a final disposition.

## 6. Operator cancellation rule

Before G0 coverage is complete, cancel if the progress UI shows broad external-web collection or source-count growth unrelated to Project knowledge.

Record:

```text
RESEARCH_GATE_ORDER_NOT_FOLLOWED
```

Do not automatically retry the same configuration.

Internal `Searched project for ...` activity is expected under Project Search mode and is not external-web collection.

## 7. Cost controls

```yaml
cost_controls:
  separate_paid_visibility_probe: prohibited
  one_Research_invocation_per_selected_task: true
  external_web_before_G0_PASS: prohibited
  source_count_target: none
  identical_failed_configuration_retry: prohibited
  automatic_A2_run: prohibited
  operator_records_approximate_cost: true
```

The prior A1 Project-knowledge probe is not repeated. Its access result is retained as product-surface evidence; each future run uses O0 and the in-run G0 gate for task-local correctness.

## 8. A1/A2 independence

- A1 and A2 use separate new Projects and separate Research invocations.
- A2 remains deferred until a valid A1 report is adjudicated and its audit object is confirmed current.
- A2 does not receive A1 material or report.
- Neither task imports prior Pro/Fable reports as evidence.

## 9. Output and transfer

The final task response must contain:

- complete report body;
- complete G0 semantic-coverage ledger;
- operator-observed setup receipt, reproduced as operator metadata rather than model fact;
- visible model/effort and Project name as operator-observed values;
- Search-mode status and retrieval limitations;
- web/source limitations and approximate cost;
- confirmation of zero connector/write actions;
- exactly one canonical disposition if and only if G0 passed.

A supported Markdown export is an auxiliary copy of the same report.

## 10. Current execution state

```yaml
A1:
  state: PAUSED_QUOTA_READY_NOT_SELECTED
  Project_knowledge_access_empirically_supported: true
  valid_substantive_report_received: false
  next_run_contract: v0.4_single_invocation_G0_G1

A2:
  state: DEFERRED_PENDING_VALID_A1_ADJUDICATION
  next_run_contract: v0.4_if_later_selected
```

## 11. Boundaries

This workflow does not:

- execute Fable or spend quota;
- make a Research report authoritative;
- amend the validation package;
- select a V0 execution surface;
- authorize V0/V1;
- modify Meta-Agent or non-FABLE health-review routes;
- attest the exact served backend;
- guarantee future product behavior.
