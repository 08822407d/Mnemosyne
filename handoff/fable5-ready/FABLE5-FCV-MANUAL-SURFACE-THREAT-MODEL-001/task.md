# Ready Task — FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001

```yaml
queue_status: READY_AFTER_MNEMOSYNE_186_MERGE_NOT_EXECUTED
task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
canonical_threat_model_specification: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
active_execution_contract: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.2.md
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
Advanced_Research: prohibited_for_revised_run
ordinary_web_search: allowed_after_full_repository_gate_PASS_for_current_product_facts
canonical_research_question_and_output_contract_changed: false
```

## Preventive repair before first run

A2 has not been executed. It previously used the same ordinary-chat preflight followed by an Advanced Research context switch that failed during A1 run 001. The active execution contract removes that unqualified transition before A2 spends quota.

## Required run

1. use a fresh standalone Claude chat or a new one-run Project that has never been used for A1;
2. select visible `Fable 5` and `Max` effort;
3. keep Advanced Research off for the entire run;
4. keep Project Files empty and avoid prior Project Memory/chats;
5. link `08822407d/Mnemosyne`, branch `master`, through chat-level `+ -> Add from GitHub`;
6. in that same ordinary chat, read this entrypoint, the manifest, the active execution contract, the complete canonical threat-model specification, and all mandatory audit inputs;
7. return the full repository-input binding receipt defined by the execution contract;
8. continue only after `PASS`, in the same chat and without changing mode;
9. use ordinary web search only after the gate, for current authoritative product facts and targeted external support;
10. do not create any live V0 worker, reviewer, adjudicator, or connector experiment;
11. return the complete report to the current Mnemosyne frontier-clarification validation route.

A visible repository link or sample-path preflight is insufficient. If the complete repository gate fails, return `INPUT_OR_REPOSITORY_INTEGRITY_FAILURE` and stop before web research or substantive threat modeling.
