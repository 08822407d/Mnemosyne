# Ready Task — FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001

```yaml
queue_status: PAUSED_QUOTA_READY_NOT_SELECTED_V0_4_SINGLE_RESEARCH_RUN
task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
display_name: MNE-DR-001 验证包审计
display_name_registry: notes/registries/project-research-display-name-registry-v0.1.md
canonical_audit_specification: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
active_execution_contract: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.4.md
operator_guide: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/OPERATOR.md
input_manifest: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml
workflow: notes/research-operations/claude-fable5-project-knowledge-research-v0.4.md
exact_topic: Independent adversarial static audit of the Mnemosyne frontier-clarification validation package before any execution-surface or V0 authorization
source_package_commit: 67eb96d5317a2bb589236a4a8b2e75be2508d830
repository_access: read_only
repository_write: prohibited
validation_execution: prohibited
prior_Pro_or_Fable_reports: prohibited
preferred_visible_model: Fable_5
preferred_effort: Max
Research:
  separate_paid_visibility_probe: prohibited
  planned_invocations_after_future_selection: 1
  G0_semantic_coverage: first_phase
  G1_substantive_report: only_after_G0_PASS_in_same_invocation
Project_Files: exact_manifest_set_only
Project_Search_mode: allowed_record_required
chat_level_GitHub_during_Research: prohibited
canonical_research_question_and_output_contract_changed: false
```

## Evidence and repair history

```yaml
run_001:
  surface: ordinary_chat_GitHub_then_Research
  result: INPUT_OR_REPOSITORY_INTEGRITY_FAILURE
  non_task_inputs_accessible_in_Research: 0_of_18
  substantive_audit_started: false
  operator_reported_cost_USD_approx: 8

Project_knowledge_probe:
  surface: one_run_Project_Files_plus_Research
  required_paths_locatable: 22_of_22
  canonical_and_package_identity: PASS
  Project_Search_mode: true
  exhaustive_byte_or_content_read: NOT_ATTESTABLE
  substantive_audit_started: false
  operator_reported_cost_USD_approx: 7
  adjudication: notes/adjudications/fable5-A1-R0-project-knowledge-search-mode-adjudication-2026-08-07.md

v0_4:
  repair:
    - no_quota_operator_setup_receipt
    - one_paid_Research_invocation
    - Search_mode_semantic_coverage_ledger
    - substantive_audit_only_after_in_run_G0_PASS
  status: prepared_paused_not_selected
```

## Future run only after explicit selection

1. create a new one-run Claude Project named `MNE-DR-001 验证包审计`;
2. add exactly the manifest-listed 22 logical files and remove every extra file;
3. sync and complete the operator setup receipt;
4. select visible `Fable 5` and `Max`;
5. disable GitHub, all other connectors, and write-capable tools;
6. enable Research and send the single combined G0/G1 prompt from `OPERATOR.md`;
7. allow internal Project Search operations, but cancel if external-web harvesting starts before G0 coverage passes;
8. if G0 fails, accept only the coverage-failure object and stop;
9. if G0 passes, the same Research invocation produces the complete 19-section report;
10. return the full report, semantic-coverage ledger, operator receipt, cost, and limitations to the Mnemosyne frontier-clarification validation route.

This task is not currently selected. Readiness does not authorize Fable quota use.
