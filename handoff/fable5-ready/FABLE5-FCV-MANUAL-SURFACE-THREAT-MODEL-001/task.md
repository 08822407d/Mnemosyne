# Ready Task — FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001

```yaml
queue_status: READY_NOT_EXECUTED
canonical_task: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
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
execution_setting_precedence: this_ready_packet_supersedes_only_the_canonical_task_older_high_or_xhigh_surface_label
canonical_research_question_and_output_contract_changed: false
```

This file is the human-visible queue entrypoint. The complete research task remains at the canonical task path above. The ready packet changes only the operator delivery/access workflow and requests the current visible `Fable 5` + `Max` condition; it does not change the research question, threat-model scope or report contract.

The run must:

1. use a fresh standalone Claude chat or a new one-run Project separate from A1;
2. keep Project Files empty by default and link or select GitHub at chat level;
3. pass the exact-path preflight in `OPERATOR.md` while Research is off;
4. read the canonical task and every mandatory path in `input-manifest.yaml`;
5. enable Research only after the preflight passes;
6. review current product/platform facts from authoritative sources without conducting a live V0 run;
7. return the complete report to the Mnemosyne frontier-clarification validation route.

A visible repository link is not a file-read receipt. If the manual-surface candidate and required package files cannot be bound reliably, return the canonical task's integrity-failure object and stop.
