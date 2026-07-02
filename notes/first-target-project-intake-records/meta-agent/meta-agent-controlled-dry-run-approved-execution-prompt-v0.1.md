# Meta-Agent Controlled No-Target-Write Dry-Run Approved Execution Prompt v0.1

execute_in: new high-reasoning ChatGPT conversation
do_not_execute_in_current_maintainer_thread: true
do_not_execute_in_codex_cloud: true
repository: `08822407d/Mnemosyne`
dry_run_id: `META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001`
output_file: `META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001-result.md`

---

## Prompt to paste into the new high-reasoning conversation

加载 Mnemosyne 指导约束。

你正在执行 **Meta-Agent controlled no-target-write real-target evaluation / design-package generation dry-run**。

执行位置：新的 high-reasoning ChatGPT conversation。不要在当前维护对话执行。不要在 Codex Cloud 执行。

Repository context:

```text
08822407d/Mnemosyne
```

## Execution approval

This dry-run has been approved by the maintainer only within the following scope:

```yaml
dry_run_id: META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001
actual_execution_approved: true
approved_execution_environment: new_high_reasoning_chatgpt_conversation
codex_cloud_execution_approved: false
target_workspace_creation_approved: false
target_material_ingestion_approved: false
target_repository_write_approved: false
operational_memory_system_installation_approved: false
mnemosyne_execution_source_update_approved: false
```

## Required reads

Read or attempt to read these repository files:

```text
current/human-approved-spec.md
commands/load-mnemosyne-guidance.md
current/active-context.md
current/todo.md
current/open-questions.md
handoff/handoff-current.md

notes/first-target-project-intake-records/meta-agent/meta-agent-actual-controlled-dry-run-execution-approval-record.md
notes/first-target-project-intake-records/meta-agent/meta-agent-controlled-dry-run-approved-execution-record-v0.1.md
notes/first-target-project-intake-records/meta-agent/meta-agent-final-run-manifest-candidate-v0.1.md
notes/first-target-project-intake-records/meta-agent/meta-agent-final-manifest-candidate-approval-for-preparation-record.md
notes/first-target-project-intake-records/meta-agent/meta-agent-controlled-dry-run-preparation-plan-v0.1.md
notes/first-target-project-intake-records/meta-agent/meta-agent-controlled-dry-run-evidence-and-no-write-proof-plan-v0.1.md
notes/first-target-project-intake-records/meta-agent/meta-agent-controlled-dry-run-operator-prompt-package-v0.1.md

notes/first-target-project-intake-records/meta-agent/meta-agent-target-project-selection-complete-draft.yaml
notes/first-target-project-intake-records/meta-agent/meta-agent-requirements-analysis-handoff-intake-alignment-package.md
notes/first-target-project-intake-records/meta-agent/meta-agent-first-target-draft-run-manifest-package-v0.2.md
notes/first-target-project-intake-records/meta-agent/meta-agent-post-v0.2-next-gate-decision-record.md
notes/first-target-project-intake-records/meta-agent/meta-agent-analysis-alignment-guard.md

notes/first-real-target-dry-run-evaluation-framework-v0.1.md
notes/first-real-target-dry-run-scorecard-v0.1.md
notes/first-real-target-dry-run-postmortem-template.md
notes/mnemosyne-regression-test-record-template.md
```

If required files are unavailable, record them under `missing_files`. If approval records or execution source cannot be read, return `BLOCKED`.

## Hard prohibitions

You must not:

- write any repository;
- create `target-projects/meta-agent/`;
- create `notes/target-project-dry-runs/`;
- ingest target materials;
- request raw materials;
- write target repository;
- install an operational Meta-Agent memory system;
- modify Mnemosyne execution source;
- claim production-ready status;
- treat research reports, handoff/current files, task results, or this prompt as execution source;
- treat this dry-run as target delivery or target repository write.

## Dry-run objective

Evaluate whether Mnemosyne can use the approved Meta-Agent pre-workspace records and non-execution-source support instruments to produce an offline Meta-Agent memory-system design/evaluation package without target workspace creation, target material ingestion, target repository write, or operational installation.

Expected output:

- offline Meta-Agent memory-system design/evaluation package;
- authority/source map;
- safe-input policy;
- handoff/delivery drafts;
- evidence map;
- assumption log;
- boundary check log;
- scorecard result;
- postmortem draft;
- regression candidate list;
- no-write evidence statement.

## Required output file

Produce a downloadable Markdown file named:

```text
META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001-result.md
```

The file must contain:

```yaml
dry_run_id: META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001
run_kind: controlled_no_target_write_real_target_evaluation_design_package_generation
repository:
tested_at:
visible_model_label:
repo_write_performed: false
codex_cloud_used: false
target_workspace_created: false
notes_target_project_dry_runs_created: false
target_materials_ingested: false
raw_materials_requested: false
target_repository_written: false
operational_memory_system_installed: false
mnemosyne_execution_source_modified: false
dry_run_verdict: PASS | PASS_WITH_WARNINGS | REPAIR_RECOMMENDED | FAIL | BLOCKED
score:
critical_blockers:
```

Then include these sections:

1. Executive summary
2. Files read / missing files
3. Approved scope and hard prohibitions check
4. Meta-Agent target identity and current constraints
5. Authority/source map
6. Safe input policy
7. Offline Meta-Agent memory-system design/evaluation package
8. Memory structure recommendations
9. Handoff/delivery draft package
10. Evidence map
11. Assumption log
12. Boundary check log
13. Scorecard result using `notes/first-real-target-dry-run-scorecard-v0.1.md`
14. Postmortem draft
15. Regression candidate list
16. No-write evidence statement
17. Limitations
18. Recommended next maintainer actions

## No-write evidence statement

The no-write evidence statement must explicitly cover:

```yaml
no_write_evidence_statement:
  repo_write_performed:
  codex_cloud_used:
  target_workspace_created:
  notes_target_project_dry_runs_created:
  target_workspace_written:
  target_materials_ingested:
  target_repository_accessed:
  target_repository_written:
  mnemosyne_execution_source_modified:
  basis:
    - no repository write tools used
    - no Codex Cloud execution
    - read-only repository inspection only, if repository tools were used
    - no target repository or target workspace was created or accessed for writing
```

If the conversation environment cannot produce `git diff`, use equivalent no-write evidence based on tool usage and explicit non-use of write tools. If any write action occurs, mark the result `FAIL` or `BLOCKED` as appropriate.

## Chat response requirement

In chat, output only:

1. short summary;
2. `dry_run_verdict`;
3. download link.

All details must be in the downloadable Markdown file.

If downloadable file generation is unavailable, output chunked Markdown:

```yaml
package_id: META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001-result
chunk: N / total
instruction: wait for all chunks before maintainer review
```
