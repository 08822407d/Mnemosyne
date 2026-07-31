# FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001 — Execution Contract v0.2

> Active execution-surface and input-binding contract for the unchanged A2 threat-model specification. This file does not authorize a live V0 surface test, GitHub write, credential use, validation execution, or surface selection.

```yaml
execution_contract_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-EXECUTION-002
version: 0.2.0
created_by_task: MNEMOSYNE-186
task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
canonical_threat_model_specification: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
source_candidate_commit: 5e556c2a6dacb41d68bf6209dbf8156b92b79e72
status: ready_after_MNEMOSYNE_186_merge_not_executed
research_question_changed: false
report_contract_changed: false
repository_access: read_only
repository_write: prohibited
validation_execution: prohibited
live_surface_test: prohibited
real_or_private_material: prohibited
```

## 1. Why this execution contract exists

A1 run 001 showed that a repository preflight performed in an ordinary Fable chat did not qualify the later Advanced Research executor: the ordinary chat read the repository inputs, while the paid Research executor reported that only the canonical task remained accessible.

A2 uses the same repository-bound delivery pattern. It is therefore repaired before first execution rather than repeating the same approximately USD 8 failure mode.

## 2. Required execution surface

```yaml
surface:
  conversation: fresh_standalone_Claude_chat_or_new_one_run_Project_separate_from_A1
  visible_model: Fable_5
  visible_effort: Max
  Advanced_Research: off_for_entire_run
  ordinary_web_search:
    during_repository_input_gate: off
    after_gate_PASS: allowed_for_current_authoritative_product_facts_and_targeted_external_support
  Project_Files: empty_by_default
  Project_Instructions: none_task_specific
  prior_Project_chats_or_memory: absent
  GitHub_access: chat_level_plus_Add_from_GitHub
  repository: 08822407d/Mnemosyne
  branch: master
```

Do not enable Advanced Research. If ordinary web search is unavailable without Advanced Research, mark affected current product claims `unverified_current_fact` or stop with `SURFACE_NOT_SUPPORTED_FOR_REVISED_RUN`; do not switch modes to salvage the run.

## 3. Context and independence invariant

The repository gate and the full static threat model must remain in the same ordinary chat with the same visible model/effort and GitHub link.

A2 must remain separate from A1. Do not expose:

- A1's task outputs or report;
- foundational Pro or Fable reports;
- existing Mnemosyne Project Memory or prior chats;
- unrelated repository files;
- any live V0 worker, reviewer, or adjudicator context.

Switching into Advanced Research, a new chat, hidden worker, or another Project invalidates the repository-binding receipt.

## 4. Canonical task completeness check

Read the complete canonical threat-model specification.

Expected identity signals:

```yaml
path: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
expected_task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
expected_final_task_heading: "## 14. Delivery and authority boundary"
expected_required_report_sections: 22
current_repository_blob_sha_for_reference: df9aec6219efba050bad7285da6ecc1c74d2a464
```

A partial read that does not reach the final task heading fails the gate. The blob SHA is reference evidence only unless the surface actually verifies it.

## 5. Full same-context repository gate

Before substantive threat modeling or external web search, read in the same ordinary chat:

1. the ready entrypoint;
2. the input manifest;
3. this execution contract;
4. the complete canonical threat-model specification;
5. the manual-surface candidate;
6. all nine required validation-package files;
7. `current/human-approved-spec.md`.

The audit-input count is 12: one canonical specification plus 11 audit objects. The three queue/support files are additional navigation and execution-control inputs.

Return only:

```yaml
repository_input_binding:
  task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
  execution_contract_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-EXECUTION-002
  repository: 08822407d/Mnemosyne
  selected_branch_or_ref:
  visible_model_text:
  visible_effort_text:
  Advanced_Research_enabled: false
  ordinary_web_search_used_during_gate: false
  chat_level_GitHub_used: true
  Project_Files_used: false
  same_chat_for_future_threat_model: true
  support_paths_read:
    expected: 3
    complete: 0
    paths: []
  canonical_specification:
    complete_read: true | false
    final_heading_observed:
    limitation:
  mandatory_audit_inputs:
    expected: 12
    complete: 0
    failed_or_conflicting_paths: []
    receipts:
      - path:
        complete_read: true | false
        visible_artifact_id_or_heading:
        source_ref_or_identity_observed:
        byte_or_line_identity_if_available:
        limitation:
  candidate_binding:
    candidate_id:
    candidate_version:
    package_id:
    package_version:
    source_commit_content_verified: true | false
    current_master_equivalence_verified: true | false | not_needed
    commit_attestation_limitations: []
  prior_Pro_or_Fable_reports_used: false
  A1_material_used: false
  live_surface_or_validation_context_created: false
  write_action_performed: false
  result: PASS | INPUT_OR_REPOSITORY_INTEGRITY_FAILURE | SURFACE_NOT_SUPPORTED_FOR_REVISED_RUN
```

`PASS` requires every support path, the complete canonical specification, and all 12 audit inputs to be readable in this exact ordinary-chat context.

## 6. Substantive threat-model launch

After the user sends a separate launch message following `PASS`, re-read this contract and execute every substantive section and output requirement in the canonical specification.

Execution precedence:

1. this file controls surface, context continuity, repository gate, independence, cost protection, and delivery mechanics;
2. the canonical specification controls the threat-model questions, evidence ladder, current-fact requirements, report sections, allowed dispositions, and boundaries;
3. the input manifest controls the exact repository path inventory.

The old `high_or_xhigh_research_conversation` wording does not authorize Advanced Research. The revised condition is ordinary `Fable 5` + `Max` with targeted ordinary web search only after the repository gate passes.

## 7. Current-fact and source discipline

A2 still must verify time-sensitive Claude/product claims from current authoritative sources where those facts change the disposition.

Rules:

- repository inputs are read first;
- ordinary web search begins only after `PASS`;
- prefer official Anthropic/provider documentation and primary technical sources;
- do not target a large source count;
- separate verified current product fact, operator-observed UI, general architecture property, adjacent evidence, original threat-model reasoning, and unknown/non-attestable properties;
- record unavailable official facts as unknown rather than switching to Advanced Research;
- do not create a live surface experiment or inspect real worker chats.

## 8. Failure handling

If the repository gate fails, return only the canonical `INPUT_OR_REPOSITORY_INTEGRITY_FAILURE` object plus this execution-contract ID and exact failed paths. Do not continue with a generic web-only threat model.

If repository access is lost after the gate:

```yaml
status: RUN_INVALIDATED_BY_REPOSITORY_ACCESS_LOSS
analysis_started: true | false
completed_sections: []
missing_or_lost_paths: []
report_disposition_generated: false
```

If a current product fact cannot be verified but the repository-bound analysis remains possible, mark the exact claim unknown and narrow the supported disposition; do not fabricate or silently generalize.

## 9. Final delivery

The complete threat-model report must appear in the ordinary-chat final response. A supported export may be used as a transfer copy, but no arbitrary second output is required.

Record:

- exact visible model and effort text;
- `Advanced_Research_enabled: false`;
- repository access mode and full input-binding receipt;
- web-search sources and current-fact limitations;
- any fallback/quota warning;
- no live V0 context and no GitHub write;
- exact backend identity as unknown or not attestable unless exact-request provider metadata exists.

Return the complete report to the current Mnemosyne frontier-clarification validation conversation.
