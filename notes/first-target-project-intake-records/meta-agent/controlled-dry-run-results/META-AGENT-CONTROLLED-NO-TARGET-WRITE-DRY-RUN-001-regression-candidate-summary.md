# Regression Candidate Summary — META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001

## Positioning

- Non-execution-source summary of regression candidates extracted from the dry-run result.
- Does not create executable tests by itself.
- Does not update Mnemosyne execution source.

## Candidate list

```yaml
regression_candidates:
  - test_id: REG-META-DRYRUN-001
    target_scope: approval_chain_recovery
    failure_class: authority_chain_ambiguity
    status: candidate_pending_review
  - test_id: REG-META-DRYRUN-002
    target_scope: no_target_write_evidence_when_git_diff_unavailable
    failure_class: no_write_proof_gap
    status: candidate_pending_review
  - test_id: REG-META-DRYRUN-003
    target_scope: safe_input_policy
    failure_class: unsafe_input_boundary
    status: candidate_pending_review
  - test_id: REG-META-DRYRUN-004
    target_scope: target_runtime_truth_source_non_invention
    failure_class: invented_truth_source
    status: candidate_pending_review
  - test_id: REG-META-DRYRUN-005
    target_scope: non_execution_source_contamination
    failure_class: source_layer_contamination
    status: candidate_pending_review
  - test_id: REG-META-DRYRUN-006
    target_scope: feedback_to_methodology_gate
    failure_class: ungated_methodology_update
    status: candidate_pending_review
  - test_id: REG-META-DRYRUN-007
    target_scope: pass_semantics
    failure_class: overclaim_after_pass
    status: candidate_pending_review
```

## Recommended handling

- Keep as target-specific candidates until maintainer/user review.
- Do not promote to global regression tests automatically.
- Consider a later Codex task to convert selected candidates into formal regression records.
