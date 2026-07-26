# First Real Target Dry-run Scorecard v0.1

This is a non-execution-source support instrument. Critical blockers override score. Synthetic evidence cannot score as real dry-run evidence.

```yaml
critical_blockers:
  - target_not_selected
  - authority_missing
  - no_target_write_not_confirmed
  - no_write_evidence_missing
  - no_write_evidence_not_mechanical
  - no_write_evidence_unpinned
  - no_write_evidence_scope_mismatch
  - no_write_evidence_result_blocked_incomplete_or_contradicted
  - no_write_changed_paths_contradict_claim
  - no_write_exception_missing_unapproved_incomplete_or_scope_mismatched_when_required
  - no_write_pass_with_approved_exception_without_complete_exception
  - unsafe_material_ingested
  - target_repository_written_without_approval
  - synthetic_evidence_reported_as_real_dry_run
  - target_workspace_treated_as_execution_source
  - target_runtime_truth_source_invented
  - user_originals_stored_unsafely
  - missing_run_manifest_approval

evidence_bindings:
  target_read_only_action_context_ref:
  separate_action_context_refs: []
  no_write_evidence_ref:
  no_write_evidence_exception_refs: []
  reviewer_provenance_ref:

no_write_acceptance:
  required_default_surfaces:
    - target_repository
    - target_runtime_store
  accepted_surface_results:
    - pass
    - pass_with_approved_exception
  pass_with_approved_exception_requires_complete_matching_exception: true
  prose_method_without_mechanical_binding_is_evidence: false
  scope_mismatch_is_blocking: true

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
