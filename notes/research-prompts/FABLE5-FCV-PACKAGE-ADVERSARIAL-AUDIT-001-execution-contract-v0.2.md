# FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001 — Execution Contract v0.2

> Active execution-surface and input-binding contract for the unchanged A1 audit specification. This file does not replace the substantive audit questions in the canonical specification, authorize a GitHub write, execute validation, or make a research result authoritative.

```yaml
execution_contract_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-EXECUTION-002
version: 0.2.0
created_by_task: MNEMOSYNE-186
task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
canonical_audit_specification: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
source_package_commit: 67eb96d5317a2bb589236a4a8b2e75be2508d830
status: ready_for_revised_rerun_after_MNEMOSYNE_186_merge
research_question_changed: false
report_contract_changed: false
repository_access: read_only
repository_write: prohibited
validation_execution: prohibited
real_or_private_material: prohibited
```

## 1. Why this execution contract exists

Run 001 established a surface discontinuity:

- the ordinary Fable chat with the chat-level GitHub connector read the canonical task and repository inputs;
- after Advanced Research was enabled, the paid research executor independently reported that only the canonical task remained retrievable and the other 18 mandatory inputs were inaccessible;
- the executor correctly returned `INPUT_OR_REPOSITORY_INTEGRITY_FAILURE` and did not fabricate an audit;
- the operator reported approximately USD 8 of Fable5 quota use for the failed run.

Therefore, an ordinary-chat connector preflight is not accepted as proof that an Advanced Research executor inherits the same repository access. This contract removes that context switch.

## 2. Required execution surface

```yaml
surface:
  conversation: fresh_standalone_Claude_chat_or_new_one_run_Project
  visible_model: Fable_5
  visible_effort: Max
  Advanced_Research: off_for_entire_run
  ordinary_web_search:
    during_repository_input_gate: off
    after_gate_PASS: allowed_only_when_external_evidence_materially_changes_a_finding
  Project_Files: empty_by_default
  Project_Instructions: none_task_specific
  prior_Project_chats_or_memory: absent
  GitHub_access: chat_level_plus_Add_from_GitHub
  repository: 08822407d/Mnemosyne
  branch: master
```

Do not enable Advanced Research at any point in this run. If the current product surface cannot perform the audit without Advanced Research, stop and return `SURFACE_NOT_SUPPORTED_FOR_REVISED_RUN`; do not spend research quota experimentally.

## 3. Context-continuity invariant

The repository gate and the substantive audit must occur in the same ordinary chat, with the same visible model/effort and the same GitHub link.

The following invalidate the run before substantive analysis:

- switching into Advanced Research;
- moving to another chat, Project, workspace, or hidden worker;
- clearing or replacing the conversation context;
- losing the chat-level GitHub link;
- adding Project Memory, prior reports, A2 material, or unrelated repository files;
- relying on a prior turn's claim without re-reading a required file when needed.

## 4. Canonical task completeness check

The canonical audit specification must be read completely before the package audit begins.

Expected identity signals on the current active specification:

```yaml
path: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
expected_task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
expected_final_task_heading: "## 17. Delivery and authority boundary"
expected_required_report_sections: 19
current_repository_blob_sha_for_reference: 88a4c11a7cc041814ee4c9ea804957df475b9d12
```

A partial read that does not reach the final task heading fails the gate. The Git blob SHA is reference evidence only; do not claim it was verified unless the surface actually exposes and checks it.

## 5. Full same-context repository gate

Before any package analysis or external web search, read in the same ordinary chat:

1. the ready entrypoint;
2. the input manifest;
3. this execution contract;
4. the complete canonical audit specification;
5. all 15 package files;
6. the three external design/adjudication files.

The audit-input count is 19: one canonical specification plus 18 audit objects. The three queue/support files are additional navigation and execution-control inputs.

Return only:

```yaml
repository_input_binding:
  task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
  execution_contract_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-EXECUTION-002
  repository: 08822407d/Mnemosyne
  selected_branch_or_ref:
  visible_model_text:
  visible_effort_text:
  Advanced_Research_enabled: false
  ordinary_web_search_used_during_gate: false
  chat_level_GitHub_used: true
  Project_Files_used: false
  same_chat_for_future_audit: true
  support_paths_read:
    expected: 3
    complete: 0
    paths: []
  canonical_specification:
    complete_read: true | false
    final_heading_observed:
    limitation:
  mandatory_audit_inputs:
    expected: 19
    complete: 0
    failed_or_conflicting_paths: []
    receipts:
      - path:
        complete_read: true | false
        visible_artifact_id_or_heading:
        source_ref_or_identity_observed:
        byte_or_line_identity_if_available:
        limitation:
  package_binding:
    package_id:
    package_version:
    pinned_commit_content_verified: true | false
    current_master_equivalence_verified: true | false | not_needed
    commit_attestation_limitations: []
  prior_Pro_or_Fable_reports_used: false
  A2_material_used: false
  write_action_performed: false
  result: PASS | INPUT_OR_REPOSITORY_INTEGRITY_FAILURE | SURFACE_NOT_SUPPORTED_FOR_REVISED_RUN
```

`PASS` requires every support path, the complete canonical specification, and all 19 audit inputs to be readable in this exact ordinary-chat context. A repository hyperlink, earlier Research result, or operator assertion is not a substitute.

## 6. Substantive audit launch

Only after the user sends a separate launch message following `PASS`, re-read this contract and execute all substantive sections and output requirements in the canonical audit specification.

Execution precedence:

1. this file controls surface, context continuity, repository gate, quota protection, and delivery mechanics;
2. the canonical specification controls the research question, audit criteria, mandatory report sections, allowed dispositions, evidence calibration, and authority boundaries;
3. the input manifest controls the exact repository path inventory.

Do not reinterpret the old `high_or_xhigh_research_conversation` wording in the canonical specification as permission to enable Advanced Research. For this revised run, visible `Fable 5` + `Max` in the ordinary chat is the selected condition.

## 7. External evidence and cost discipline

Repository artifacts are the primary evidence. External web sources are supplementary.

Rules:

- complete the repository-input gate before any web search;
- do not target a large source count;
- do not run broad exploratory searches merely to demonstrate research activity;
- use official or primary sources for platform and technical claims;
- use empirical literature only where it materially affects a concrete audit finding;
- distinguish direct evidence, adjacent evidence, analogy, and original engineering reasoning;
- record any quota warning or product fallback;
- if source collection begins to dominate the static package audit, narrow it and state the limitation.

## 8. Failure handling

If the repository gate fails, return only the canonical `INPUT_OR_REPOSITORY_INTEGRITY_FAILURE` object plus the execution-contract ID and exact failed paths. Do not continue with web-only reconstruction.

If access is lost after the gate but before final output:

```yaml
status: RUN_INVALIDATED_BY_REPOSITORY_ACCESS_LOSS
analysis_started: true | false
completed_sections: []
missing_or_lost_paths: []
report_disposition_generated: false
```

Do not convert a partial audit into a final disposition.

## 9. Final delivery

The complete report body must appear in the ordinary-chat final response. A supported export may be used as a transfer copy, but no arbitrary second research output is required.

Record:

- exact visible model and effort text;
- `Advanced_Research_enabled: false`;
- repository access mode;
- input-binding receipt;
- any web-search or source limitations;
- any quota/fallback warning;
- no GitHub write;
- exact backend identity as unknown or not attestable unless exact-request provider metadata exists.

Return the complete report to the current Mnemosyne frontier-clarification validation conversation.
