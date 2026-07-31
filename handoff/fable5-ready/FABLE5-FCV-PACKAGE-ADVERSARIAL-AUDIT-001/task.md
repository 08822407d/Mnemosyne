# Ready Task — FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001

```yaml
queue_status: READY_FOR_REVISED_RERUN_AFTER_MNEMOSYNE_186_MERGE
task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
canonical_audit_specification: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
active_execution_contract: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.2.md
operator_guide: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/OPERATOR.md
input_manifest: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml
exact_topic: Independent adversarial static audit of the Mnemosyne frontier-clarification validation package before any execution-surface or V0 authorization
source_package_commit: 67eb96d5317a2bb589236a4a8b2e75be2508d830
repository_access: read_only
repository_write: prohibited
validation_execution: prohibited
prior_Pro_or_Fable_reports: prohibited
preferred_visible_model: Fable_5
preferred_effort: Max
Advanced_Research: prohibited_for_revised_run
ordinary_web_search: allowed_only_after_full_repository_gate_PASS
canonical_research_question_and_output_contract_changed: false
```

## Prior attempt

```yaml
run_001:
  ordinary_chat_preflight: PASS
  canonical_specification_complete_read: true
  canonical_specification_final_heading_observed: "## 17. Delivery and authority boundary"
  Advanced_Research_repository_inputs_accessible: 1_of_19
  result: INPUT_OR_REPOSITORY_INTEGRITY_FAILURE
  substantive_audit_started: false
  report_accepted_as_A1_research: false
  accepted_as_surface_failure_evidence: true
  operator_reported_cost_USD_approx: 8
```

Run 001 showed that ordinary-chat GitHub access did not qualify the later Advanced Research executor. The revised run removes that context switch.

## Required revised run

1. use a fresh standalone Claude chat or a new one-run Project;
2. select visible `Fable 5` and `Max` effort;
3. keep Advanced Research off for the entire run;
4. keep Project Files empty and avoid prior Project Memory/chats;
5. link `08822407d/Mnemosyne`, branch `master`, through chat-level `+ -> Add from GitHub`;
6. in that same ordinary chat, read this entrypoint, the manifest, the active execution contract, the complete canonical specification, and all mandatory audit inputs;
7. return the full repository-input binding receipt defined by the execution contract;
8. continue only after `PASS`, in the same chat and without changing mode;
9. use ordinary web search only after the repository gate and only for targeted external support;
10. return the complete report to the current Mnemosyne frontier-clarification validation route.

A visible repository link, a four-file sample, or an earlier context's receipt is insufficient. If the complete repository gate fails, return `INPUT_OR_REPOSITORY_INTEGRITY_FAILURE` and stop before external source collection or substantive audit.
