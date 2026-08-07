# Ready Task — FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001

```yaml
queue_status: DEFERRED_PENDING_VALID_A1_ADJUDICATION_V0_4_PREPARED
task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
display_name: MNE-DR-002 表面威胁
display_name_registry: notes/registries/project-research-display-name-registry-v0.1.md
canonical_threat_model_specification: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
active_execution_contract: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.4.md
operator_guide: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/OPERATOR.md
input_manifest: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml
workflow: notes/research-operations/claude-fable5-project-knowledge-research-v0.4.md
exact_topic: Independent threat model and evidence audit of a manual multi-conversation surface for Mnemosyne frontier-clarification V0
source_candidate_commit: 5e556c2a6dacb41d68bf6209dbf8156b92b79e72
repository_access: read_only
repository_write: prohibited
validation_execution: prohibited
live_surface_test: prohibited
prior_Pro_or_Fable_reports: prohibited
preferred_visible_model: Fable_5
preferred_effort: Max
Research:
  separate_paid_visibility_probe: prohibited
  planned_invocations_after_later_selection: 1
  G0_semantic_coverage: first_phase
  G1_substantive_report: only_after_G0_PASS_in_same_invocation
Project_Files: exact_manifest_set_only
Project_Search_mode: allowed_record_required
chat_level_GitHub_during_Research: prohibited
canonical_research_question_and_output_contract_changed: false
```

## Dependency and preventive repair

```yaml
A2:
  attempts: 0
  selected_now: false
  current_disposition: DEFERRED_PENDING_VALID_A1_ADJUDICATION
  prerequisites:
    - valid_A1_report_returned_and_adjudicated
    - A2_audit_object_confirmed_current
    - explicit_RUN_disposition
    - operator_acceptance_of_quota_use
```

v0.4 removes the separate paid visibility probe and uses one Research invocation with an internal semantic-coverage gate. It preserves A1/A2 independence and prohibits live V0 contexts.

## Future run only after later explicit selection

1. create a new Project named `MNE-DR-002 表面威胁`, separate from A1;
2. add exactly the manifest-listed 15 logical files and no extras;
3. sync and complete the no-quota operator setup receipt;
4. select `Fable 5` and `Max`;
5. disable GitHub, all other connectors, and write-capable tools;
6. send the single G0/G1 Research prompt from `OPERATOR.md`;
7. if G0 fails, stop without a surface disposition;
8. if G0 passes, complete the 22-section threat model in the same invocation;
9. create no live V0 worker/reviewer/adjudicator or connector-test context;
10. return the complete report, semantic-coverage ledger, operator receipt, cost, and limitations.

This task remains deferred. Readiness does not authorize Project creation or quota use.
