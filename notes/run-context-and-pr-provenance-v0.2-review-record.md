# Run-Context and PR-Provenance v0.2 Review and Amendment Record

> Non-execution-source review, user-disposition, and amendment-lineage record. `current/human-approved-spec.md` remains Mnemosyne's only execution source. The active behavior instrument is `current/run-context-and-pr-provenance-guard.md`.

```yaml
record_id: MNEMOSYNE-RUN-CONTEXT-PR-PROVENANCE-V0-2-REVIEW-001
record_type: bounded_review_user_disposition_and_guard_amendment_record
independent_review_task: WORK-ULTRA-PR198-REVIEW-001
implementation_task: MNEMOSYNE-149
recorded_at: 2026-07-22
reviewed_implementation:
  pull_request: 198
  merge_commit: e895e586fcda6783af567e3513b2c5f03ebd2d1c
later_checkpoint_context:
  pull_request: 199
  merge_commit: 96244617606f2a7afe3c1f0451438720df9f3307
review_verdict: PARTIALLY_FAITHFUL_WITH_BOUNDED_V0_2_REPAIRS_RECOMMENDED
user_disposition: APPROVE_ALL_CANDIDATE_CHANGES_C01_THROUGH_C08
execution_source_modified: false
historical_v0_1_records_rewritten: false
checkpoint_activated: false
GF_STEP_5_substantive_adjudication_started: false
target_project_action_started: false
```

## 1. Source and integrity record

The independent review used the following attached contracts and research evidence:

```yaml
attached_inputs:
  - filename: WORK-ULTRA-PR198-REVIEW-001-task-v2.md
    size_bytes: 19988
    sha256: b190cd8c2f041c8bb4dd3859c49b344e260050f44f93f4bd0348fc2c75349235
    role: independent_review_contract
  - filename: FABLE5-GOV-001-independent-evidence-governance-research-task-v2.md
    size_bytes: 18554
    sha256: 81368ae96a2e716268583a0f4a36d69c476fed7e50add3b25963f68c8c096e96
    role: original_Fable_research_contract
  - filename: FABLE5-GOV-001-independent-governance-research-report.md
    size_bytes: 59630
    sha256: 6a815c6d3c506d630b226fe53e1141057c9d9c1b69bab62b9586e22e67798ffe
    role: complete_Fable_research_report
```

The repository archive identity for FABLE5-GOV-001 remains recorded under:

- `raw/research-reports/cycles/2026Q3-multi-model-adjudication-provenance/fable5-governance-001/archive-index.md`
- `raw/research-reports/cycles/2026Q3-multi-model-adjudication-provenance/fable5-governance-001/manifest.yaml`
- `raw/research-reports/cycles/2026Q3-multi-model-adjudication-provenance/fable5-governance-001/maintainer-receipt.md`

The implementation-relevant Work review findings, C-01 through C-08 patch plan, final determinations, and decision questions were supplied to MNEMOSYNE-149 in the current conversation transcript. The surrounding cross-conversation context explicitly indicated that some earlier conversation content was skipped, so full-output completeness is not mechanically verifiable. No separate immutable review-report file was supplied, and this record does not invent a path or hash:

```yaml
review_output:
  ref: current_conversation_user_supplied_transcript_2026_07_22
  immutable_file_hash: unavailable
  implementation_relevant_findings_C01_through_C08_and_final_determinations_available: true
  full_output_completeness_in_this_run: not_mechanically_verifiable
  limitations:
    - transcript_reference_is_not_an_immutable_repository_artifact
    - earlier_cross_conversation_content_was_explicitly_skipped
```

The load-bearing repository sources are:

```yaml
repository_sources:
  - ref: current/human-approved-spec.md@e895e586fcda6783af567e3513b2c5f03ebd2d1c
    blob_sha: 01f64a8223677829320c66dd46d3f172cc9155cc
    role: sole_execution_source_and_actor_authorization_review_rules
  - ref: current/run-context-and-pr-provenance-guard.md@e895e586fcda6783af567e3513b2c5f03ebd2d1c
    blob_sha: e2c9ecf01cbb09d84b9cafb700062db527be0fe2
    role: v0_1_guard_under_review
  - ref: notes/run-context-and-pr-provenance-adoption-record.md@e895e586fcda6783af567e3513b2c5f03ebd2d1c
    blob_sha: 7cf5b614fb74566d37aec48b55f00d7560ce1c96
    role: original_user_adoption_and_deferred_scope
  - ref: notes/codex-task-results/MNEMOSYNE-147-result.md@e895e586fcda6783af567e3513b2c5f03ebd2d1c
    blob_sha: 570f524bf00bc25429f127c454fd8c02b41262fb
    role: first_v0_1_instance
  - ref: commands/load-mnemosyne-guidance.md@e895e586fcda6783af567e3513b2c5f03ebd2d1c
    blob_sha: 524dc282cb605756bb396aa144df2e5af119830a
    role: loader_trigger_under_review
  - ref: current/multi-model-adjudication-provenance-research-status.md@e895e586fcda6783af567e3513b2c5f03ebd2d1c
    blob_sha: cae759da879a8aa9536982b94e1606bdffa7ad83
    role: PR_198_status_at_merge_with_stale_pending_merge_gate
  - ref: current/multi-model-adjudication-provenance-research-status.md@96244617606f2a7afe3c1f0451438720df9f3307
    blob_sha: d00a5095e9571fd36a61fd036adf70c03c89c423
    role: pre_MNEMOSYNE_149_live_status_with_stale_pending_PR_199_merge_gate
  - ref: current/pr198-pro-switch-model-quality-restart-checkpoint.md@96244617606f2a7afe3c1f0451438720df9f3307
    blob_sha: 2e8910f80fe580b3a8b4e21e8ca1a788016655a0
    role: later_checkpoint_relationship_only
  - ref: notes/codex-task-results/MNEMOSYNE-148-result.md@96244617606f2a7afe3c1f0451438720df9f3307
    blob_sha: a9838eb3ddd62555d7592ea0133fc949dabf0629
    role: later_checkpoint_result_context_only
```

## 2. Review independence and limitations

The Work review is more context-independent than the original same-conversation implementation review, but it is not heterogeneous-provider review and does not attest a hidden backend:

```yaml
review_events:
  - review_id: WORK-ULTRA-PR198-REVIEW-001
    actor: ChatGPT_Work_review_lead
    actor_kind: model
    role: bounded_evidence_and_governance_review
    context_relation_to_producer: fresh_task_project
    model_relation_to_producer: unknown
    provider_relation_to_producer: same
    criteria_fixed_before_exposure: true
    review_scope: PR_198_fidelity_evidence_separation_burden_switching_independence_and_recovery_boundary
    evidence:
      - class: operator_reported
        ref: current_conversation_user_supplied_transcript_2026_07_22
        observed_or_accessed_at: 2026-07-22
        claim_scope: review_output_and_verdict_supplied_to_MNEMOSYNE_149
        detail: implementation_relevant_findings_and_C01_through_C08_were_supplied
    result_ref: current_conversation_user_supplied_transcript_2026_07_22
    limitations:
      - default_memory_project_did_not_mechanically_guarantee_total_outside_context_exclusion
      - model_and_snapshot_relation_cannot_be_inferred_from_UI_labels
      - same_provider_review_does_not_remove_all_correlated_blind_spots
      - transcript_output_has_no_separate_immutable_file_hash
      - full_review_output_completeness_in_this_implementation_run_is_not_mechanically_verifiable
  - review_id: WORK-ULTRA-PR198-REVIEW-001-MULTI-AGENT-CROSS-CHECKS
    actor: three_Work_review_subaudits
    actor_kind: model
    role: review_cross_checks
    context_relation_to_producer: fresh_task_project
    model_relation_to_producer: unknown
    provider_relation_to_producer: same
    criteria_fixed_before_exposure: unknown
    review_scope: authorized_repository_paths_and_finding_consistency
    evidence:
      - class: operator_reported
        ref: current_conversation_user_supplied_transcript_2026_07_22
        observed_or_accessed_at: 2026-07-22
        claim_scope: occurrence_of_three_multi_agent_cross_checks
        detail: supplied_review_reported_three_read_only_subaudits
    result_ref: current_conversation_user_supplied_transcript_2026_07_22
    limitations:
      - same_provider
      - model_relations_unknown
      - not_heterogeneous_provider_review
  - review_id: MNEMOSYNE-149-SOURCE-AND-REPOSITORY-VERIFICATION
    actor: local_validation_process
    actor_kind: mechanical_process
    role: attached_input_hash_and_commit_pinned_repository_verification
    context_relation_to_producer: not_applicable
    model_relation_to_producer: not_applicable
    provider_relation_to_producer: not_applicable
    criteria_fixed_before_exposure: not_applicable
    review_scope: exact_hash_path_ref_and_repository_identity_properties_only
    evidence:
      - class: mechanically_verified_repository_evidence
        ref: notes/run-context-and-pr-provenance-v0.2-review-record.md#1-source-and-integrity-record
        observed_or_accessed_at: 2026-07-22
        claim_scope: recorded_attachment_hashes_and_commit_pinned_source_identities
        detail: mechanically_rechecked_during_MNEMOSYNE_149
    result_ref: notes/run-context-and-pr-provenance-v0.2-review-record.md#1-source-and-integrity-record
    limitations:
      - verifies_only_listed_input_and_repository_identity_properties

review_context_summary:
  operator_selected_effort: Ultra
  backend_model_identity: UNKNOWN_OR_NOT_ATTESTABLE
  model_relation_to_original_producer: unknown
  provider_relation_to_original_producer: same
  heterogeneous_provider_review: false
```

Human adjudication and repository-write authorization are recorded separately in §5. Neither is inferred from the review events.

## 3. Finding-to-evidence ledger

| Finding | Severity | Exact authorized evidence | Disposition |
|---|---:|---|---|
| PR198-F01 — evidence vocabulary, schema enum, and first instance disagree | P1 | v0.1 guard §§2, 4; `MNEMOSYNE-147-result.md` current run context; FABLE5-GOV-001 §§4, 7, 14 | Repair through C-01 |
| PR198-F02 — backend-attestation branch is overbroad and not representable | P1 | v0.1 guard §2 rule 6 and §4; FABLE5-GOV-001 §4 E3/E4, §7, §17 | Repair through C-01 |
| PR198-F03 — reviewer, human adjudication, authorization, and independence are mixed | P1 | v0.1 guard §§4, 8; `MNEMOSYNE-147-result.md`; human-approved spec §§18–19; FABLE5-GOV-001 §§5, 7, 12–13 | Repair through C-04 |
| PR198-F04 — switch sketch cannot reliably attribute artifacts or commits | P2 | v0.1 guard §7; FABLE5-GOV-001 §§9, 11 | Repair through C-03 |
| PR198-F05 — low-risk/important overlap and silent omission are ambiguous | P2 | v0.1 guard §§3–4; FABLE5-GOV-001 §§10–12 | Repair through C-02 |
| PR198-F06 — authorization and heterogeneous-review exception are not persistently auditable | P2 | v0.1 guard §§3.3–4; human-approved spec §§18–19; FABLE5-GOV-001 §§7, 12, 17 | Repair through C-02 and C-04 |
| PR198-F07 — loader trigger is narrower than repository-write coverage | P2 | `commands/load-mnemosyne-guidance.md` required files and behavior 19; v0.1 guard front matter; human-approved spec §18 | Clarify through C-05 |
| PR198-F08 — research-to-rule traceability and amendment lineage are partial | P2 | v0.1 guard front matter and §§8–9; original adoption record; FABLE5-GOV-001 §§9–11, 16–17 | Clarify through C-06 |
| PR198-F09 — live wayfinding retained completed merge gates | P2 | PR #198 merge metadata; PR #199 merge `96244617606f2a7afe3c1f0451438720df9f3307`; `current/multi-model-adjudication-provenance-research-status.md@96244617606f2a7afe3c1f0451438720df9f3307` still recorded `pending_human_merge_of_PR_199` | Clarify through C-07 |
| PR198-N01 — full incident machinery should remain outside the general guard | NOTE | v0.1 guard §10; original adoption record deferred scope; PR #199 checkpoint; FABLE5-GOV-001 §§8–10 | Accept boundary; add only C-08 cross-reference |
| PR198-N02 — historical naming preservation is correct | NOTE | v0.1 guard §6; original adoption record; FABLE5-GOV-001 §§4, 9, 14 | Preserve as-is; remove product-tier maturity only from the live guard |

No finding authorizes rewriting PR #198, the original adoption decision, or historical v0.1 run records.

## 4. Clause-to-change disposition

| Change | User-authorized implementation | Evidence and reason | Historical treatment |
|---|---|---|---|
| C-01 | Replace evidence and backend schema | F01/F02; FABLE5-GOV-001 §4 and §7 | v0.1 instances remain historical |
| C-02 | Replace field list with eight core groups, conditional groups, precedence, and auditable omissions | F05/F06; FABLE5-GOV-001 §11 Option B and §12 | no backfill |
| C-03 | Add stable `switch_history` and `segments` schema | F04; FABLE5-GOV-001 §§9, 11 | old empty array retained with documented variance |
| C-04 | Add component `review_events`, separate human adjudication and authorization, structured exception, and capability-neutral maturity | F03/F06; human-approved spec §§18–19; FABLE5-GOV-001 §§5, 7, 12 | original reviewer wording retained |
| C-05 | Trigger provenance guard for any repository write or important record intended for publication; retain lineage guard for branch/PR work | F07 | historical loader calls unchanged |
| C-06 | Create this review record and append only a cross-reference to the original adoption record | F08 | original record not rewritten or superseded |
| C-07 | Refresh live status and remove completed PR #199 merge gate/product-tier maturity | F09 | PR #198/#199 historical status remains in Git history |
| C-08 | Add a lightweight checkpoint cross-reference | N01 | activation trigger and recovery semantics unchanged |

## 5. Human disposition and task-local authorization

The user explicitly authorized all suggested modifications and stated that no other conversation would modify Mnemosyne before this task completed.

```yaml
human_adjudication:
  status: recorded
  actor: user
  decision: approve_all_candidate_changes_C01_through_C08
  evidence:
    - class: direct_user_instruction
      ref: current_conversation_user_instruction_2026_07_22
      observed_or_accessed_at: 2026-07-22
      claim_scope: human_disposition_of_WORK_ULTRA_PR198_review_candidates
      detail: all_suggested_modifications_approved
  limitations:
    - human_disposition_is_terminal_authority_but_not_independent_technical_verification

user_authorization:
  status: authorized
  actor: user
  decision_ref: current_conversation_user_instruction_2026_07_22
  authorized_actions:
    - implement_C01_through_C08_in_Mnemosyne
    - create_one_canonical_branch_and_pull_request
    - create_required_review_result_and_finalization_records
    - perform_mechanical_validation
  excluded_actions:
    - modify_current/human-approved-spec.md
    - merge_or_enable_auto_merge
    - activate_the_PR198_checkpoint
    - create_an_incident_or_activation_record
    - adjudicate_Fable_GF_STEP_5
    - perform_target_project_work
    - rewrite_Git_history_or_historical_v0_1_records
  evidence:
    - class: direct_user_instruction
      ref: current_conversation_user_instruction_2026_07_22
      observed_or_accessed_at: 2026-07-22
      claim_scope: MNEMOSYNE_149_repository_write_authorization
      detail: bounded_v0_2_repairs_and_normal_single_PR_publication_workflow
  expires_with_task: true
  not_future_precedent: true

concurrency_assurance:
  source: user
  statement_scope: no_other_conversation_will_modify_Mnemosyne_until_this_task_finishes
  does_not_replace_latest_default_branch_verification: true

high_impact_classification:
  triggered: true
  reason: C01_and_C04_change_backend_attestation_and_authorization_trust_boundary_representation

heterogeneous_review_exception:
  decision_ref: current_conversation_user_instruction_2026_07_22
  exact_scope:
    - C01_backend_attestation_representation_repair
    - C04_review_adjudication_and_authorization_representation_repair
  reason: user_approved_all_disclosed_candidate_repairs_after_receiving_the_review_that_explicitly_recorded_same_provider_and_no_heterogeneous_provider_review
  expires_with_task: true
  compensating_controls:
    mechanical_verification_refs:
      - notes/run-context-and-pr-provenance-v0.2-review-record.md#1-source-and-integrity-record
      - notes/codex-task-results/MNEMOSYNE-149-result.md#validation
    human_adjudication_ref: notes/run-context-and-pr-provenance-v0.2-review-record.md#5-human-disposition-and-task-local-authorization
  residual_risk:
    - same_provider_review_may_retain_correlated_blind_spots
    - current_implementation_cross_checks_are_not_heterogeneous_review
  not_future_precedent: true
```

This one message supports both objects because it separately approves the candidate decisions and authorizes their repository implementation. The claim scopes remain distinct.

## 6. Legacy schema variance

The first v0.1 instance is preserved even though it cannot validate against either the written v0.1 enum or v0.2:

```yaml
legacy_schema_variance:
  affected_record: notes/codex-task-results/MNEMOSYNE-147-result.md
  affected_version: v0.1
  observed_variances:
    - v0_1_schema_used_verified_platform_record_and_unknown_outside_its_canonical_vocabulary
    - first_instance_used_operator_reported_plus_provider_terminology_normalization_outside_the_schema
    - normalized_Extra_High_was_mixed_into_a_field_intended_to_preserve_operator_wording
    - reviewer_authorization_and_same_conversation_context_were_compounded_into_scalars
    - empty_switch_array_did_not_distinguish_confirmed_none_from_unknown
  disposition: preserve_and_explain_do_not_rewrite
```

## 7. Amendment and preservation lineage

```yaml
lineage:
  review_disposition: amend
  reviews:
    - current/run-context-and-pr-provenance-guard.md@e895e586fcda6783af567e3513b2c5f03ebd2d1c
    - notes/run-context-and-pr-provenance-adoption-record.md@e895e586fcda6783af567e3513b2c5f03ebd2d1c
    - notes/codex-task-results/MNEMOSYNE-147-result.md@e895e586fcda6783af567e3513b2c5f03ebd2d1c
  amends:
    - ref: current/run-context-and-pr-provenance-guard.md
      scope: prospective_behavior_and_run_record_schema_after_v0_2_is_on_the_default_branch
      decision_ref: current_conversation_user_instruction_2026_07_22
  supersedes_for_scope:
    - ref: current/run-context-and-pr-provenance-guard.md@e895e586fcda6783af567e3513b2c5f03ebd2d1c
      scope: v0_1_normative_schema_for_new_records_created_after_v0_2_is_effective
  preserves:
    - PR_198_and_merge_commit_e895e586fcda6783af567e3513b2c5f03ebd2d1c
    - notes/run-context-and-pr-provenance-adoption-record.md_original_decision
    - notes/codex-task-results/MNEMOSYNE-147-result.md_historical_run_context
    - PR_199_and_merge_commit_96244617606f2a7afe3c1f0451438720df9f3307
    - current/pr198-pro-switch-model-quality-restart-checkpoint.md_activation_and_recovery_semantics
```

`reviewed`, `amended`, and `superseded_for_scope` are not synonyms. The original adoption and execution context remain historical evidence; only the prospective normative schema and live maturity/status are changed.

## 8. Boundary

This record does not become execution source, attest any backend model, claim heterogeneous-provider review, rewrite a historical run record, activate the PR #198 checkpoint, establish that an incident occurred, authorize recovery, modify `current/human-approved-spec.md`, adjudicate Fable GF-STEP-5, authorize target-project work, merge a pull request, or enable auto-merge.
