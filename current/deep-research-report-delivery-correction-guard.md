# Deep Research Report Delivery — Correction Guard

> User-confirmed correction to the Deep Research-specific interpretation of the artifact-delivery guard. This file is not a standalone execution source; `current/human-approved-spec.md` remains the only execution source.

```yaml
guard_id: MNEMOSYNE-DEEP-RESEARCH-SINGLE-REPORT-DELIVERY-001
created_by_task: MNEMOSYNE-179
last_amended_by_task: MNEMOSYNE-200
status: active_after_MNEMOSYNE_200_merge
execution_source_modified: false
scope_precedence:
  supersedes_for_Deep_Research_only:
    - current/artifact-delivery-and-direct-generation-guard.md_complete_response_requirements
    - current/user-operation-next-step-capability-and-intent-guard.md_auxiliary_complete_response_wording
    - commands/load-mnemosyne-guidance.md_complete_response_requirements
    - previously_generated_Deep_Research_task_delivery_clauses
```

## 1. Corrected model

A completed Deep Research run has one canonical substantive output: the complete research report.

```yaml
canonical_output:
  type: complete_Deep_Research_report
  count: one

representations_of_same_report:
  - inline_or_full_screen_report
  - operator_exported_Markdown
  - operator_exported_Word
  - operator_exported_PDF

separate_second_research_output:
  required: false
```

A standard export is not a second conclusion or second report. Renaming a Markdown export for archival does not create a new substantive output.

## 2. Reliable delivery contract

A Deep Research task should require:

- the complete canonical report body in the product's report/final-answer surface;
- exact task/research ID and topic at the report opening;
- source/access/citation/truncation warnings in the report;
- a portable source table when the task requires one;
- instructions for the operator to export the completed report in a supported format when cross-conversation transfer is needed;
- an expected archival filename for the operator export, if useful.

Recommended form:

```yaml
Deep_Research_delivery:
  canonical_report_required: true
  canonical_report_location: product_final_report_surface
  operator_export_when_transfer_needed:
    format: Markdown
    suggested_filename: <TASK_ID>-report.md
    role: export_of_the_same_canonical_report
  arbitrary_model_generated_second_file:
    required: false
```

## 3. Optional custom file

A separately generated arbitrary named file may be requested only when the current product surface explicitly supports file creation and the Agent can verify that creation succeeded.

```yaml
custom_file:
  may_be_requested: true
  only_if_surface_support_is_observed: true
  must_not_be_claimed_before_creation_success: true
  may_not_replace_canonical_report: true
  may_not_be_presented_as_a_second_research_conclusion: true
```

Deep Research task designers must not assume that generic ChatGPT/Work artifact-generation capability is available inside every Deep Research report surface.

## 4. Failure handling

If only the canonical report is delivered:

- the research run is not incomplete merely because no custom complete-response file exists;
- use the product's supported report export;
- do not send a new message into the research workflow merely to request a custom file when that may start another run;
- preserve the export identity honestly as operator-exported from the canonical report.

If the report's task ID or topic is wrong, renaming or exporting does not repair the run; treat it as wrong-topic/input-binding failure.

## 5. Relationship to non-Deep-Research tasks

The general complete-response transfer-file rule may still apply to Codex tasks, Work tasks, ordinary artifact-generating conversations, handoffs, reviews, or other surfaces when:

- the complete user-visible response differs from named substantive artifacts;
- a file-generation capability is available;
- the task genuinely needs the full response preserved.

This correction is limited to Deep Research's single canonical report semantics.

## 6. Historical task handling

Completed task files that required both the canonical report and a custom `complete-response.md` remain historical evidence. Their report results are accepted based on the canonical report; missing custom files are not rerun triggers.

Future taskbooks and broader guidance must use or point to the corrected contract rather than restating the older Deep Research complete-response interpretation.

## 7. Boundaries

- This guard does not authorize research execution, quota use, model switching or external writes.
- It does not alter the report's research conclusions.
- It does not make an operator-exported file byte-identical to any unobserved internal representation.
- It does not modify a target project's truth source.
