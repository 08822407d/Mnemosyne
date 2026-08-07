# Operator Guide — FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001 v0.4

## Current execution state

```yaml
display_name: MNE-DR-001 验证包审计
canonical_task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
execution_disposition: PAUSED_QUOTA_READY_NOT_SELECTED
visible_model: Fable_5
visible_effort: Max
surface: new_one_run_Project_with_exact_Project_Files
Research_invocations_if_later_selected: 1
repository_write: prohibited
validation_execution: prohibited
```

This guide prepares a future run. It does not currently request or authorize Fable quota use.

## Why v0.4 uses one Research invocation

The completed Project-knowledge probe proved that Research could search all required paths, but Project Search mode could not attest byte-complete reading and the probe cost approximately USD 7. Do not repeat that full probe.

v0.4 uses:

```text
O0 operator setup receipt, no Research quota
  -> one Research invocation
       G0 semantic coverage using Project knowledge only
       G1 complete audit only after G0 PASS
```

## A. Create the one-run Project

1. Create a new Claude Project named exactly:

   ```text
   MNE-DR-001 验证包审计
   ```

2. Do not use an existing Mnemosyne Project.
3. Confirm zero prior chats and zero Project Files before setup.
4. Add this Project instruction:

   ```text
   One-run read-only A1 audit Project. Use only the explicitly selected Project Files as internal repository evidence. Do not write GitHub or any connected service. Do not use prior Pro/Fable reports, A2 material, prior chats or unrelated Mnemosyne files. Treat the canonical task as instructions and the validation package as the audit object, not authority.
   ```

## B. Add exact Project Files

From Project `Files -> + -> GitHub`, choose `08822407d/Mnemosyne`, branch `master`, and add:

```text
handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/task.md
handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml
notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.4.md
notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
notes/frontier-clarification-validation-package/                 [entire folder, 15 files]
notes/validation-designs/frontier-planning-clarification-handoff-read-only-validation-v0.1.md
notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/03-cross-report-consensus-conflict-and-adjudication.md
notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/04-interim-architecture-and-validation-decision.md
```

Expected logical total: 22 files.

Remove every accidental extra file, including `OPERATOR.md` itself unless it is separately pasted only as operator guidance outside Project knowledge. Click **Sync**.

## C. Complete O0 operator receipt

Before Research, record:

```yaml
operator_project_setup_receipt:
  task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
  display_name: MNE-DR-001 验证包审计
  Project_name:
  Project_created_new: true
  prior_chat_count: 0
  Project_Files_before_setup: 0
  selected_paths_or_folders: []
  selected_logical_file_count: 22
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

Do not start Research unless O0 is `PASS`.

## D. Prepare the Research chat

1. Open the first and only intended chat in the Project.
2. Select `Fable 5`, effort `Max`.
3. Disable GitHub, all other connectors, and all write-capable tools.
4. Enable Research.
5. Send the single prompt below. Do not run a separate visibility probe first.

## E. Single combined G0/G1 prompt

```text
This is the single selected Research invocation for
FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.

Use this Project's exact selected Project Files as primary internal evidence.
Do not use GitHub, raw URLs, another connector, prior chats, prior Pro/Fable
reports, or A2 material. Do not write any connected service.

PHASE G0 — PROJECT-KNOWLEDGE SEMANTIC COVERAGE

Before any external web research or substantive package finding, read and
retrieve from Project knowledge every path in:

handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml

Project Search mode and chunked retrieval are allowed. Do not claim byte-complete
reading. Instead produce the exact `project_knowledge_semantic_coverage` ledger
defined in:

notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.4.md

G0 must account for:

- all 22 required paths;
- canonical headings through `## 17. Delivery and authority boundary`;
- task ID and package ID/version;
- all 14 public scenario IDs with 8 V1-smoke and 6 V2-reserve records;
- all 14 matching hidden-key IDs without unnecessarily reproducing hidden answer content;
- Q0, Q1, Q2, Q3 and Q4;
- required heading maps and terminal boundaries for the package/taskbook/result files;
- zero external web sources, zero connector use, zero write, and zero substantive finding before the gate.

If any required semantic target is unresolved, return only:

INPUT_OR_PROJECT_KNOWLEDGE_COVERAGE_FAILURE

with the complete coverage ledger and stop. Do not issue an audit disposition.

PHASE G1 — SUBSTANTIVE AUDIT

Only if G0 returns PASS, continue automatically in this same Research invocation.
Re-read as needed:

- notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.4.md
- notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
- handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml

Execute every substantive requirement and all 19 report sections in the
canonical specification. The validation package is the audit object, not
authority. External web research is now allowed only when it materially supports
a concrete canonical finding. Separate Project-file evidence, external evidence,
and inference. Do not target a source count.

If Project knowledge becomes unavailable, return only
RUN_INVALIDATED_BY_PROJECT_KNOWLEDGE_ACCESS_LOSS and do not issue a disposition.

The final response must contain:

- the complete 19-section report;
- the complete G0 semantic-coverage ledger;
- operator setup metadata as operator-observed, not model-attested UI fact;
- visible model/effort, Project name, logical file count and Search-mode status;
- source/access/quota limitations and approximate cost;
- repository_write_performed: false;
- exactly one allowed canonical A1 disposition, only after G0 PASS.

Exact served backend identity remains unknown unless exact-request provider
metadata exists.
```

## F. Operator cancellation rule

During the run:

- internal `Searched project for ...` activity is expected;
- if broad external-web source collection begins before G0 coverage is complete, cancel and record `RESEARCH_GATE_ORDER_NOT_FOLLOWED`;
- do not retry the same configuration automatically.

## G. Return to Mnemosyne

Return:

- complete G0 ledger;
- complete G1 report if G0 passed;
- operator setup receipt;
- supported Markdown export of the same report, if available;
- approximate cost, Search-mode indication, warnings, cancellation/fallback events.

Do not reuse this Project for A2.

## Stop conditions

Stop on any missing/extra file, prior chat/report, A2 material, wrong identity, unresolved semantic target, connector/write action, external web before G0, validation execution, or loss of Project knowledge.
