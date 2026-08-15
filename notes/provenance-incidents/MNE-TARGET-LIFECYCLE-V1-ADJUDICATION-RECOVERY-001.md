# MNE-TARGET-LIFECYCLE-V1 Adjudication Recovery Incident 001

> Provenance record for the accidental regenerate/stop event and the later recovered fresh-Pro adjudication attachment. This record distinguishes exact file identity, semantic verification and the unprovable byte identity of the pre-regeneration chat answer.

```yaml
incident_id: MNE-TARGET-LIFECYCLE-V1-ADJUDICATION-RECOVERY-001
task_id: MNEMOSYNE-215
incident_class: model_response_regeneration_and_recovery_provenance
source_run_id: MNE-TARGET-LIFECYCLE-V1-001
source_review_role: fresh_Pro_semantic_adjudicator
status: RECOVERED_RESULT_ACCEPTED_AFTER_INDEPENDENT_EVIDENCE_RECHECK
rerun_required: false
normalized_adjudication_ref: notes/validation-adjudications/MNE-TARGET-LIFECYCLE-V1-ADJUDICATION-001.md
owner_decision_ref: notes/owner-decision-results/MNE-TARGET-LIFECYCLE-V1-OWNER-ARCHITECTURE-DECISION-001.md
```

## 1. Operator-reported sequence

1. A genuinely new Pro conversation completed `v1_adjudication_receive: PASS`.
2. The same fresh-Pro conversation completed the formal semantic adjudication.
3. After completion, the Owner accidentally selected the product's regenerate/re-answer action.
4. The Owner immediately stopped that regeneration attempt.
5. The Owner asked the same fresh-Pro conversation to recover the completed result.
6. The recovered/reconstructed answer was exported and uploaded to the current Mnemosyne task.
7. The current task hashed the uploaded file and independently rechecked its nontrivial findings against the exact repository evidence.

This incident occurred after the V1 scenario cells and mechanical bundle were complete. It did not write or alter the synthetic validation repository.

## 2. Supplied attachment identity

```yaml
source_artifact_receipt:
  artifact_id: MNE-TARGET-LIFECYCLE-V1-FRESH-PRO-RECOVERED-ADJUDICATION-001
  operator_filename: MNE-TARGET-LIFECYCLE-V1-001-fresh-Pro-formal-semantic-adjudication.md
  media_type_or_extension: text/markdown
  bytes: 33867
  lines: 701
  sha256: d9aea362e9a780e24a453c51287f06b9ad6e22ab492cdc1a332b4cbb5bd8dcb4
  preservation_level: IDENTITY_RECEIPT_ONLY
  exact_attachment_body_stored_in_repository: false
  byte_identity_verified_for_uploaded_task_input: true
  source_device_identity_verified: unknown
  content_review_scope: complete_decision_relevant_document_plus_key_repository_reproduction
  limitations:
    - repository_does_not_reconstruct_the_uploaded_attachment_bytes
    - pre_regeneration_chat_answer_byte_identity_is_not_attestable
    - local_turn_file_citations_in_the_attachment_are_not_durable_repository_references
```

The exact file bytes exposed to this task were available at intake and were hashed before normalization. The public repository stores the identity receipt and a normalized durable adjudication rather than the attachment body.

## 3. Identity and transformation assessment

```yaml
source_transformation_assessment:
  byte_identity:
    status: changed_or_not_applicable_between_attachment_and_normalized_record
    evidence_refs:
      - sha256:d9aea362e9a780e24a453c51287f06b9ad6e22ab492cdc1a332b4cbb5bd8dcb4
  transformation_class: substantive_normalization_to_durable_repository_refs
  substantive_content:
    status: unchanged_as_reviewed
    review_scope: global_disposition_scenario_results_defect_classification_rerun_decision_Owner_gate_and_key_nontrivial_findings
  preservation_level_before: exact_uploaded_file_available_to_current_task
  preservation_level_after: IDENTITY_RECEIPT_ONLY_plus_NORMALIZED_DURABLE_ADJUDICATION
  exact_received_source_retained_separately: false
  limitations:
    - normalized_record_is_not_a_byte_identical_copy
    - original_pre_regenerate_answer_cannot_be_compared_byte_for_byte
```

The normalization removes conversation-local `turnXXfileY` citations and replaces them with durable repository, commit, branch, path and blob identities.

## 4. Independent semantic verification

The current task independently reproduced the two most consequential non-obvious findings:

1. The historical controller/fixture contract at blob `7068b5efc0d484baf48824c5692ee1b3b2d8a634` both:
   - omitted root `README.md` from fixture `allowed_write_roots`; and
   - required root `README.md` in the frozen initial fixture tree.
2. The S6 test artifact at synthetic commit `e90fcc6633bae50236aa96f9c499ba6c7379f53f` calls `sort_invoices` without importing it, while the source file defines the function.

The controller branch remains at `e892749fc9e242b24908f89b6a78f1c0f0bed75e`; no regenerate/recovery action changed the V1 evidence.

The recovered result's global disposition, scenario matrix, no-rerun conclusion, TLR-03/TLR-04 treatment, no-write result and evidence limitations are consistent with the exact V1 bundle and frozen criteria.

## 5. Reliability disposition

```yaml
reliability_assessment:
  exact_verbatim_recovery_of_pre_regeneration_answer: not_attestable
  same_fresh_Pro_conversation_recovery_or_reconstruction: Owner_attested
  complete_document_structure: verified
  exact_repository_evidence_unchanged: verified
  key_findings_independently_reproduced: verified
  material_conflict_with_frozen_evidence: none_found
  semantic_reliability: high_for_decision_relevant_scope
  accepted_for_formalization: true
  duplicate_fresh_Pro_rerun_required: false
```

A new rerun would produce another answer but would not prove the lost pre-regeneration text. Because the evidence is unchanged and the result is independently reproducible, a rerun would add cost without resolving the only unprovable property.

## 6. Boundaries

This recovery disposition does not:

- prove the exact text of the original completed response;
- prove hidden model/backend identity;
- convert the recovered attachment into an execution source;
- authorize V1 rerun, S10, V2, runtime supplement, target adoption or evidence cleanup;
- preserve the exact uploaded file body in the public repository.
