# Fable5 A1 Project-Knowledge R0 — Search-Mode and Cost Adjudication

> Mnemosyne maintainer adjudication of the user-returned Research-direct Project-knowledge probe for `FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001`. This file records execution-surface evidence only. It is not a package audit, validation result, execution source, or authorization to spend additional Fable quota.

```yaml
adjudication_id: MNEMOSYNE-FABLE5-A1-R0-PROJECT-KNOWLEDGE-SEARCH-MODE-001
created_by_task: MNEMOSYNE-195
recorded_at: 2026-08-07
task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
display_name: MNE-DR-001 验证包审计
run_role: Research_direct_Project_knowledge_probe
report_role: execution_surface_evidence_only
substantive_A1_audit_started: false
repository_write_performed: false
```

## 1. Evidence received

The operator returned the complete model-visible R0 receipt and a progress trace showing repeated internal `Searched project for ...` operations. The operator also supplied these facts:

```yaml
operator_reported:
  visible_model_selection: Fable_5
  visible_effort_selection: Max
  Research_enabled: true
  Project_Search_mode_visible: true
  operator_reported_cost_USD_approx: 7
  external_web_sources_used: 0
  destination_or_repository_write: 0
```

The model-side receipt reported:

```yaml
Project_Files_used: true
chat_level_GitHub_used: false
other_connectors_enabled: false
support_paths_complete: 3
mandatory_audit_inputs_complete: 19
canonical_specification_complete: true
package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
package_version: 0.1.0
external_web_sources_used: 0
repository_write_performed: false
substantive_audit_started: false
result: PASS
```

The receipt also disclosed `chunked_RAG_retrieval`, inability to attest byte completeness, and several files whose interior sections or repeated records were not individually surfaced.

## 2. Extra `OPERATOR.md` variance

The Project included one extra same-task support file, `OPERATOR.md`, beyond the 22 manifest-counted paths. The user later confirmed this was an operator file-selection mistake.

```yaml
extra_file:
  path: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/OPERATOR.md
  cause: operator_selection_error
  Fable_fault: false
  Project_Search_mode_fault: false
  malicious_or_cross_task_contamination: false
  model_detected_and_disclosed: true
```

The extra file prevents describing the exact Project input set as a mechanically perfect 22-file set for that run. It does not undermine the conclusion that Research could search the required Project knowledge.

## 3. Search-mode interpretation

The visible Claude Project message stated that Project knowledge exceeded what Claude could read all at once and therefore used Search mode. In this mode, the product retrieves relevant chunks rather than placing every file byte in the context simultaneously.

Therefore these propositions are distinct:

```yaml
supported:
  - each_required_path_could_be_located_in_Project_knowledge
  - file_identity_start_end_or_required_markers_could_be_retrieved
  - canonical_final_heading_was_retrieved
  - package_identity_was_recovered
  - Research_used_Project_knowledge_without_live_GitHub

not_attestable:
  - every_byte_of_every_file_was_loaded
  - every_interior_section_was_retrieved
  - every_scenario_and_hidden_key_was_individually_examined
```

The v0.3 Boolean field `complete_read: true | false` is too coarse for Search mode. A truthful Search-mode receipt needs path resolution, identity markers, required semantic coverage, gaps, and limitations rather than a byte-complete claim.

## 4. Cost adjudication

```yaml
cost_gate:
  intended_role: low_cost_visibility_probe
  operator_reported_cost_USD_approx: 7
  result: FAIL
  reason: exhaustive_22_file_RAG_coverage_is_not_a_lightweight_probe
```

The prior failed Research run cost approximately USD 8. A separate paid R0 followed by a separate paid R1 risks spending nearly a full run merely to prove access. The same full R0 must not be repeated.

## 5. Final disposition

```yaml
adjudication:
  Research_can_access_selected_Project_knowledge: PASS
  all_22_manifest_paths_locatable: PASS
  canonical_and_package_identity_binding: PASS
  no_external_web_during_probe: PASS
  no_live_connector_or_write_reported: PASS_WITH_SELF_REPORT_LIMITATION
  exact_22_file_input_set: PASS_WITH_OPERATOR_VARIANCE
  exhaustive_content_or_byte_read: NOT_ATTESTABLE_UNDER_SEARCH_MODE
  low_cost_probe_design: FAIL
  substantive_A1_report: ABSENT
  retroactive_R1_authorization: false
  identical_R0_rerun: prohibited
```

The Project-knowledge route solves the original run-001 access discontinuity at the path/retrieval level. It does not justify a byte-completeness claim, and the separate paid-probe architecture is not cost-proportionate.

## 6. Required workflow repair

The replacement workflow must:

1. use a no-quota operator setup/inventory receipt;
2. allow Project Search mode explicitly;
3. replace byte-complete claims with a semantic-coverage ledger;
4. combine the internal coverage gate and substantive work in one Research invocation;
5. forbid external web collection until the internal coverage gate passes;
6. fail closed without a package disposition if required semantic coverage is missing;
7. avoid repeating the already-completed Research-access experiment;
8. preserve the current A1/A2 canonical research questions unchanged.

The corresponding replacement is `notes/research-operations/claude-fable5-project-knowledge-research-v0.4.md` and the task-specific v0.4 execution contracts.

## 7. Current execution state

```yaml
A1:
  state: PAUSED_QUOTA_NOT_SELECTED
  Research_access_surface: empirically_supported
  valid_substantive_report_received: false
  next_paid_run: single_combined_coverage_and_audit_run_only_after_explicit_user_selection

A2:
  state: DEFERRED_PENDING_VALID_A1_ADJUDICATION
```

No Fable run, validation cell, package amendment, execution-surface selection, V0, or V1 is authorized by this adjudication.
