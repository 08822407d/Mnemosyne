# Ready Task — FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001

```yaml
queue_status: PREPARED_AFTER_MNEMOSYNE_188_MERGE_DEFERRED_PENDING_A1_ADJUDICATION
task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
display_name: MNE-DR-002 表面威胁
display_name_registry: notes/registries/project-research-display-name-registry-v0.1.md
canonical_threat_model_specification: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
active_execution_contract: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.3.md
operator_guide: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/OPERATOR.md
input_manifest: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml
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
  R0_Project_knowledge_probe: required_after_later_selection
  R1_substantive_report: allowed_only_after_R0_PASS
Project_Files: exact_manifest_set_only
chat_level_GitHub_during_Research: prohibited
canonical_research_question_and_output_contract_changed: false
```

## Dependency and preventive repair

```yaml
A2:
  attempts: 0
  selected_now: false
  current_disposition: DEFERRED_PENDING_VALID_A1_ADJUDICATION
  reason:
    - A1_may_require_package_amendments_that_change_A2_inputs
    - avoid_spending_quota_on_a_likely_invalidated_surface_audit
```

A2 originally inherited the same ordinary-chat-to-Research transition that failed A1. v0.3 replaces that unqualified transition before any A2 run:

```yaml
v0_3:
  primary_inputs: exact_Project_Files_and_Project_knowledge
  Research_access: direct_R0_probe_inside_Research
  chat_level_GitHub_inheritance: not_used
```

## Required run after later explicit selection

1. create a new one-run Project named `MNE-DR-002 表面威胁`, separate from A1;
2. add exactly the manifest-listed files to Project Files and sync;
3. select `Fable 5` and `Max`;
4. disable GitHub and all other connectors;
5. enable Research and run R0;
6. cancel if R0 begins broad external collection before binding Project files;
7. continue to R1 only after 15/15 Project files pass;
8. do not create live V0 worker, reviewer, adjudicator or connector-test contexts;
9. return the complete threat-model report and probe receipt.

This file prepares the workflow but does not currently select or authorize A2 execution.
