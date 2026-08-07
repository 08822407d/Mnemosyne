# Operator Guide — FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001 v0.4

## Current execution state

```yaml
display_name: MNE-DR-002 表面威胁
canonical_task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
execution_disposition: DEFERRED_PENDING_VALID_A1_ADJUDICATION
visible_model: Fable_5
visible_effort: Max
surface: new_one_run_Project_with_exact_Project_Files
Research_invocations_if_later_selected: 1
repository_write: prohibited
validation_execution: prohibited
live_surface_test: prohibited
```

This guide is prepared but does not authorize Project creation or A2 quota use.

## A. Later selection gate

Do not create the Project until a maintainer response explicitly states a `RUN_*` disposition and confirms:

```yaml
- valid_A1_report_returned_and_adjudicated
- A2_manual_surface_candidate_still_current
- A2_required_package_subset_still_current
- Fable_quota_use_selected_by_user
```

## B. One-run Project

After later selection:

1. Create a new Project named exactly `MNE-DR-002 表面威胁`.
2. It must be separate from A1 and contain zero prior chats/files.
3. Add this Project instruction:

   ```text
   One-run read-only A2 threat-model Project, separate from A1. Use only the explicitly selected Project Files as internal repository evidence. Do not write GitHub or any connected service. Do not use prior Pro/Fable reports, A1 material, prior chats or unrelated Mnemosyne files. Do not create or inspect live V0 worker, reviewer, adjudicator or connector-test contexts. Treat the canonical task as instructions and the manual-surface candidate as an audit object, not authority.
   ```

## C. Exact Project Files

From `Files -> + -> GitHub`, choose `08822407d/Mnemosyne`, branch `master`, and add exactly:

```text
handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/task.md
handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml
notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.4.md
notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
notes/validation-designs/frontier-clarification-validation-manual-surface-preparation-candidate-v0.1.md
notes/frontier-clarification-validation-package/README.md
notes/frontier-clarification-validation-package/01-protocol-spec-v0.1.md
notes/frontier-clarification-validation-package/02-condition-contracts-q0-q4-v0.1.md
notes/frontier-clarification-validation-package/04-hidden-author-keys-v0.1.md
notes/frontier-clarification-validation-package/07-reviewer-and-adjudication-taskbook-v0.1.md
notes/frontier-clarification-validation-package/08-v0-sentinel-context-isolation-taskbook-v0.1.md
notes/frontier-clarification-validation-package/10-run-manifest-template-v0.1.md
notes/frontier-clarification-validation-package/11-result-return-and-maintainer-review-package-v0.1.md
notes/frontier-clarification-validation-package/12-execution-surface-and-user-decision-package-v0.1.md
current/human-approved-spec.md
```

Expected logical total: 15. Remove every extra file and Sync.

## D. O0 operator receipt

```yaml
operator_project_setup_receipt:
  task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
  display_name: MNE-DR-002 表面威胁
  Project_name:
  Project_created_new_and_separate_from_A1: true
  prior_chat_count: 0
  Project_Files_before_setup: 0
  selected_paths: []
  selected_logical_file_count: 15
  unexpected_Project_files: []
  Project_sync_completed: true
  visible_model_selection: Fable_5
  visible_effort_selection: Max
  Project_Search_mode_visible: true | false | unknown
  chat_level_GitHub_disabled: true
  other_connectors_disabled: true
  write_capable_tools_enabled: false
  result: PASS | BLOCKED | INVALID
```

Do not start Research unless O0 passes.

## E. Prepare one Research invocation

1. Select `Fable 5`, effort `Max`.
2. Disable GitHub, all other connectors, and write-capable tools.
3. Enable Research.
4. Send the single prompt below. Do not run a separate paid visibility probe.

## F. Single combined G0/G1 prompt

```text
This is the single selected Research invocation for
FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.

Use only this Project's exact selected Project Files as primary internal
evidence. Do not use GitHub, raw URLs, another connector, prior chats, prior
Pro/Fable reports, or A1 material. Do not write any connected service and do not
create or inspect live V0 worker, reviewer, adjudicator, or connector-test
contexts.

PHASE G0 — PROJECT-KNOWLEDGE SEMANTIC COVERAGE

Before any external web research or substantive threat-model finding, retrieve
every path listed in:

handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml

Project Search mode and chunked retrieval are allowed. Do not claim byte-complete
reading. Produce the exact `project_knowledge_semantic_coverage` ledger defined
in:

notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.4.md

G0 must account for:

- all 15 required paths;
- canonical headings through `## 14. Delivery and authority boundary`;
- task, candidate, and package identities/versions;
- Q0, Q1, Q2, Q3, and Q4;
- all 14 hidden-key IDs without unnecessarily reproducing hidden answer content;
- required heading maps and terminal boundaries;
- zero external web sources, zero connector use, zero live validation context,
  zero write, and zero substantive finding before the gate.

If any required semantic target is unresolved, return only:

INPUT_OR_PROJECT_KNOWLEDGE_COVERAGE_FAILURE

with the complete coverage ledger and stop. Do not issue a surface disposition.

PHASE G1 — SUBSTANTIVE THREAT MODEL

Only if G0 returns PASS, continue automatically in the same Research invocation.
Re-read as needed:

- notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.4.md
- notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
- handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml

Execute every substantive requirement and all 22 report sections. Verify
current product facts from authoritative sources only after G0 passes. Separate
Project-file evidence, external evidence, and inference. Do not perform a live
surface experiment or create live validation contexts. Do not target a source
count.

If Project knowledge becomes unavailable, return only
RUN_INVALIDATED_BY_PROJECT_KNOWLEDGE_ACCESS_LOSS and do not issue a disposition.

The final response must contain:

- the complete 22-section report;
- the complete G0 semantic-coverage ledger;
- operator setup metadata as operator-observed, not model-attested UI fact;
- visible model/effort, Project name, logical file count, and Search-mode status;
- current product sources, limitations, approximate cost, and warnings;
- confirmation that no live V0 context was created;
- repository_write_performed: false;
- exactly one allowed canonical A2 disposition, only after G0 PASS.

Exact served backend identity remains unknown unless exact-request provider
metadata exists.
```

## G. Cancellation and return

- Internal Project Search is expected.
- Cancel if external-web harvesting begins before G0 completes; record `RESEARCH_GATE_ORDER_NOT_FOLLOWED`.
- Do not retry the same configuration automatically.
- Return the complete ledger/report/operator receipt to the Mnemosyne frontier-clarification validation conversation.
- Do not reuse this Project for A1.

## Stop conditions

Stop on absent A1 adjudication, stale audit object, missing/extra files, prior A1/report material, wrong identity, unresolved coverage, connector/write action, external web before G0, live validation context, or loss of Project knowledge.
