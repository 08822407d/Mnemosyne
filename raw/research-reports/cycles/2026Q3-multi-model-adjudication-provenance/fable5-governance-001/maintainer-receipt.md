# FABLE5-GOV-001 Initial Maintainer Receipt

> Receipt, integrity review, and high-level interpretation only. This is not substantive policy adoption or Fable GF-STEP-5 adjudication.

## Structural and input-integrity receipt

```yaml
report_status_claim: FABLE5_GOV_001_COMPLETE_INDEPENDENT_GOVERNANCE_RESEARCH
required_top_level_sections: 17_of_17
required_final_determinations: 12_of_12
failure_register_entries: 20
required_repository_reads: 4_of_4
extra_repository_reads: 0
repository_blob_SHA_cross_check: pass
task_and_report_exact_archive_reconstruction: pass
```

The four repository blob SHAs reported by Fable match the pinned `94de7427...` commit. The task and report archives were reconstructed locally and matched the received originals byte-for-byte before repository upload.

## Initial value assessment

The report is high-signal heterogeneous-provider evidence. It independently supports the broad direction already present in the DR07 cycle:

- visible product/model labels and model self-reports are not backend attestation;
- behavioral depth is not a reliable backend identifier;
- fresh same-family review has limited independence;
- heterogeneous review should be risk-based rather than universal;
- compact run records are a plausible low-burden candidate;
- a heavyweight cryptographic provenance stack is not currently justified;
- the problem is better treated as evidence, adjudication, and recovery governance than marker formatting alone.

It adds useful candidate detail in four areas:

1. a post-checkpoint artifact recovery matrix;
2. missing checkpoint fields such as contamination windows, affected-artifact inventories, evidence tiers, downstream dependencies, and re-entry validation;
3. a T0–T5 risk/escalation model;
4. a staged GF-STEP-5 review structure separating mechanical verification, preregistered independent scoring, targeted adjudication, and the human decision gate.

## Independence classification

```yaml
different_provider_and_model_family: true
prior_DR07_full_reports_read: false
maintainer_comparison_read: false
complete_blinding: false
disclosed_incidental_exposure:
  - authorized_PR196_checkpoint_contains_backend_identity_unproven_status
  - persistent_project_context_contains_limited_prior_marker-study_history
current_classification: heterogeneous_independent_research_with_bounded_directional_anchoring
```

## Known limitations

- The `[S1]` through `[S24]` ledger lacks a complete portable URL/DOI-to-claim manifest.
- The report states that external research used search retrieval without opening additional source pages; load-bearing facts need a later primary-source verification pass.
- Some fast-changing product-surface wording needs precise qualification before policy use.
- Research convergence does not itself authorize policy adoption, execution-source edits, or acceptance of GF-STEP-5 findings.

## Stage conclusion

```yaml
receipt_status: RECEIVED_COMPLETE_HIGH_SIGNAL
repository_input_integrity: PASS
exact_storage: PASS
source_portability: INCOMPLETE
substantive_policy_acceptance: NOT_PERFORMED
GF_STEP_5_adjudication: NOT_STARTED
recommended_next_gate: portable_source_manifest_then_bounded_three_way_comparison_and_user_decision
```
