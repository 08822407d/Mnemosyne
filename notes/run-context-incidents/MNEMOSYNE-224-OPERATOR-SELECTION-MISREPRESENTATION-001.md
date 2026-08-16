# MNEMOSYNE-224 Operator-Selection Misrepresentation — Incident 001

> Additive incident record. This file does not rewrite PR #292, MNEMOSYNE-224 historical artifacts, or the user's broader model-capability policy. It records the observed attribution failure so a later dedicated Mnemosyne behavior-improvement route can analyze it without losing the evidence.

```yaml
incident_id: MNEMOSYNE-224-OPERATOR-SELECTION-MISREPRESENTATION-001
recorded_by_task: MNEMOSYNE-226
reported_at: 2026-08-15
reported_by: Owner
affected_task: MNEMOSYNE-224
affected_PR: 292
affected_merge_commit: d0cae2f1d145c8c3e63f4912c9685148face1dc7
incident_class:
  - operator_selection_state_misrepresentation
  - unsupported_frontier_review_claim
  - conversation_state_continuity_failure
severity: material_provenance_and_trust_failure
technical_A0_execution_started: false
validation_repository_written: false
real_target_effect: none_observed
execution_source_modified: false
broader_guidance_change_in_this_task: false
```

## 1. Owner report

The Owner states that the response which performed the MNEMOSYNE-224 protocol repair and prepared PR #292 was sent while the conversation was using a **next-tier model selection**, not Pro.

The exact consumer-UI label for that prior turn was not supplied in the incident report. Therefore the corrected historical attribution is:

```yaml
previous_turn_operator_selection:
  category_reported_by_Owner: next_tier
  exact_UI_label: unknown_not_reported
  evidence_class: direct_user_instruction
  backend_identity: unknown_or_not_attestable

current_MNEMOSYNE_226_review_selection:
  verbatim_reported_by_Owner: Pro
  evidence_class: direct_user_instruction
  backend_identity: unknown_or_not_attestable
```

This record does not infer a hidden served model from either label.

## 2. Incorrect claims

The following statements are not supported and are superseded for attribution scope by this incident record:

1. the previous assistant response stated that the conversation was already using Pro;
2. PR #292's execution-context block recorded:

```yaml
operator_selection_verbatim: Pro
semantic_review: PASS_Pro_protocol_repair
```

3. MNEMOSYNE-224 publication language implied that the repair had already received same-turn Pro semantic review.

The Owner's direct correction is controlling evidence for what they selected. The assistant's prior assertion is not operator-selection evidence.

## 3. Impact

```yaml
invalidated_claims:
  - MNEMOSYNE_224_was_produced_under_Pro_operator_selection
  - MNEMOSYNE_224_had_same_turn_Pro_semantic_review
not_automatically_invalidated:
  - exact_GitHub_paths_blobs_and_merge_identity
  - existence_of_the_package_001_self_invalidation_defect
  - technical_content_of_package_002_subject_to_fresh_Pro_review
```

The incident is serious because model-capability routing and reviewer provenance are explicit Mnemosyne control dimensions. A falsely elevated review label can cause downstream actors to skip a review gate that never actually occurred.

## 4. Immediate containment

- A0 was not executed before discovery.
- No validation-repository branch or result was created.
- Fresh Pro review is performed separately by MNEMOSYNE-226.
- MNEMOSYNE-224 records remain historical evidence and are not silently edited.
- Any future use of package 002 must rely on the MNEMOSYNE-226 Pro review and the repaired package 003 model-authorization binding.
- No global execution-source or behavior-guard change is made here; the Owner plans a later dedicated Mnemosyne construction conversation for root-cause and durable policy treatment.

## 5. Open questions reserved for the later dedicated route

- Why did the assistant treat stale prior-turn model context as current truth?
- Which evidence source should control current model-selection state when only the user can see the picker?
- Should every important repository-writing reply require a current-turn operator-selection receipt rather than carrying one forward?
- How should a model-selection uncertainty block claims such as `Pro reviewed` without blocking low-risk work?
- What validation can detect contradictions between user-reported selection and generated PR metadata before publication?

This task preserves these questions but does not decide them.
