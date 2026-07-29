# Deep Research Single-Report Delivery — Correction Record

```yaml
decision_id: MNEMOSYNE-DEEP-RESEARCH-SINGLE-REPORT-DELIVERY-001
implementation_task: MNEMOSYNE-179
decision_date: 2026-07-29
decision_source: current_Mnemosyne_maintenance_conversation
status: pending_MNEMOSYNE_179_merge
active_guard_after_merge: current/deep-research-report-delivery-correction-guard.md
execution_source_modified: false
```

## Failure corrected

Earlier guidance and generated research tasks described the complete inline Deep Research report and a separately named `complete-response.md` file as two required deliverables. The product reliably produces one canonical report; supported Markdown/Word/PDF downloads are exports of that same report. A separate arbitrary file is not a second research conclusion and is not a universally guaranteed Deep Research capability.

## Corrected rule

```yaml
canonical_substantive_output:
  count: one
  type: complete_Deep_Research_report
representations:
  - product_report_surface
  - operator_exported_Markdown
  - operator_exported_Word
  - operator_exported_PDF
mandatory_arbitrary_second_file: false
```

A custom named file may be requested only when the current surface explicitly supports file creation and successful creation can be verified. It may not replace the canonical report or be described as another research result.

## Historical handling

Completed task files remain historical evidence. Missing custom `complete-response` files do not trigger a research rerun when the canonical report is complete and correctly bound.

## Scope

This correction is Deep-Research-specific. The general complete-response transfer-file rule can still apply to other artifact-generating tasks when the final reply genuinely differs from named artifacts and the surface supports verified file creation.
