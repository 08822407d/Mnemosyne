# First Real Target Dry-run Scorecard v0.1

This is a non-execution-source support instrument. Critical blockers override score. Synthetic evidence cannot score as real dry-run evidence.

```yaml
critical_blockers:
  - target_not_selected
  - authority_missing
  - no_target_write_not_confirmed
  - unsafe_material_ingested
  - target_repository_written_without_approval
  - synthetic_evidence_reported_as_real_dry_run
  - target_workspace_treated_as_execution_source
  - target_runtime_truth_source_invented
  - user_originals_stored_unsafely
  - missing_run_manifest_approval

score_dimensions:
  context_recovery: 15
  authority_source_map: 15
  input_safety: 20
  memory_design_fit: 15
  handoff_delivery_usability: 15
  evidence_provenance: 10
  assumption_discipline: 5
  postmortem_actionability: 5

verdicts:
  PASS: no critical blocker, score >= 90, minimum critical/major gates met, user confirms usefulness and boundary compliance
  PASS_WITH_WARNINGS: no critical blocker, score 75-89, core goals met with warnings
  REPAIR_RECOMMENDED: no critical blocker, score 60-74 or multiple major defects
  FAIL: enough evidence exists, but core capability/usability failed or score < 60
  BLOCKED: critical blocker prevents valid real target-project dry-run evaluation
```

PASS is not production-ready. PASS does not approve target repository write. PASS does not update global execution source. PASS does not constitute target delivery acceptance unless separately confirmed.
