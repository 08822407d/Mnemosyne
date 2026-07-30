# Ready Task — FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001

```yaml
queue_status: READY_NOT_EXECUTED
canonical_task: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
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
execution_setting_precedence: this_ready_packet_supersedes_only_the_canonical_task_older_high_or_xhigh_surface_label
canonical_research_question_and_output_contract_changed: false
```

This file is the human-visible queue entrypoint. The complete research task remains at the canonical task path above. The ready packet changes only the operator delivery/access workflow and requests the current visible `Fable 5` + `Max` condition; it does not change the research question, evidence gate or report contract.

The run must:

1. use a fresh standalone Claude chat or a new one-run Project with no prior task chats and empty Project Files by default;
2. link or select GitHub in that chat;
3. pass the exact-path preflight in `OPERATOR.md` while Research is off;
4. read the canonical task and every mandatory path in `input-manifest.yaml`;
5. enable Research only after the preflight passes;
6. return the complete report to the Mnemosyne frontier-clarification validation route.

A visible repository link is not a file-read receipt. If the audit object cannot be bound to the required files and package identity, return the canonical task's integrity-failure object and stop.
