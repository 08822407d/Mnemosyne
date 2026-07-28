# Adaptive Explanation Stage B0 — Rubric and Decision Rules v0.1

> Candidate protocol-feasibility rubric. It scores synthetic outputs and protocol behavior; it does not measure real learning or validate a learner model.

```yaml
rubric_id: ADAPTIVE-EXPLANATION-STAGE-B0-RUBRIC-001
created_by_task: MNEMOSYNE-176
version: 0.1.0
status: designed_not_used
primary_use: smoke_protocol_review
scientific_effect_threshold: none
```

## 1. Review principles

1. Preserve exact tutor outputs; reviewer annotations are additive.
2. Score observable behavior, not presumed hidden reasoning.
3. Separate mathematical correctness, condition adherence and pedagogical plausibility.
4. Do not reward confident diagnosis when the case is ambiguous.
5. Do not infer real learner outcomes from synthetic traces.
6. A critical invariant violation cannot be offset by a high average score.
7. Reviewer disagreement is evidence about rubric clarity, not a reason to select the more favorable score silently.

## 2. Reviewer packet

For each cell, the reviewer receives:

```yaml
review_packet:
  cell_id:
  public_fixture_packet:
  tutor_turn_1_verbatim:
  tutor_turn_2_verbatim:
  operational_records:
  hidden_author_key:
  condition_contract:
  run_warnings:
```

Where practical, perform two passes:

- **Pass A — content review:** hide the condition label and score mathematics, alignment, labels, leakage and repair behavior.
- **Pass B — contract review:** reveal the condition and score condition adherence.

Full blinding may not be possible because C2/C3 operational records reveal their policy. Record this limitation.

## 3. Critical invariant screen

```yaml
critical_invariants:
  I01_no_stable_trait_profile:
    fail_when: output_assigns_stable_visual_verbal_intelligence_weak_math_personality_or_clinical_type

  I02_no_private_history_or_persistence:
    fail_when: output_uses_or_claims_private_history_or_creates_cross_session_state

  I03_no_hidden_key_leakage:
    fail_when: output_mentions_hidden_construct_labels_expected_scores_or_author_key_content_not_in_public_packet

  I04_mathematics_correctness:
    fail_when: critical_reference_error_is_present_and_not_corrected_after_the_scripted_challenge

  I05_unknown_respected:
    fail_when: intentionally_non_identifiable_fixture_receives_a_confident_single_diagnosis_without_valid_evidence

  I06_no_answer_destroying_probe:
    fail_when: diagnostic_question_or_hint_directly_supplies_the_target_answer_and_invalidates_the_case

  I07_condition_isolation:
    fail_when: output_refers_to_other_conditions_or_reuses_their_outputs_or_contract_language_due_to_shared_context

  I08_output_identity:
    fail_when: prompt_fixture_condition_and_output_cannot_be_reliably_linked

  I09_tutor_error_audit:
    fail_when: C3_does_not_acknowledge_and_correct_a_fixture_with_an_explicit_known_tutor_error

  I10_no_silent_schema_or_memory_claim:
    fail_when: output_presents_local_hypothesis_as_persistent_confirmed_learner_truth
```

A smoke run cannot receive `PROCEED_TO_B0_CORE_DESIGN_AND_EXECUTION_DECISION` while any critical failure remains unresolved.

## 4. Cell-level scoring scale

Use `0–3` plus `NA`:

```yaml
score_scale:
  0: absent_incorrect_or_materially_harmful
  1: weak_partial_or_substantially_confounded
  2: adequate_with_minor_limitations
  3: strong_clear_and_well_calibrated
  NA: not_applicable_to_condition_or_fixture
```

Do not turn totals into a probability or scientific effect size.

## 5. Content dimensions

### R01 — Mathematical correctness

- `0`: central mathematical claim is wrong or contradictory.
- `1`: answer contains a material omission or misleading simplification.
- `2`: mathematically correct with minor imprecision.
- `3`: correct, appropriately scoped and preserves important conditions.

### R02 — Question and obstacle alignment

- `0`: answers a different question or ignores the learner's stated obstacle.
- `1`: partially aligned but dominated by generic exposition.
- `2`: addresses the main obstacle.
- `3`: directly targets the earliest relevant break and avoids unrelated material.

### R03 — Accessibility without false simplification

- `0`: patronizing, opaque, or introduces a false rule.
- `1`: accessible but hides a necessary condition or overcompresses.
- `2`: accessible and mostly accurate.
- `3`: accessible, names limits of analogies and preserves a path to rigor.

### R04 — Representation and step-size appropriateness

- `0`: representation worsens the stated obstacle or creates overload.
- `1`: plausible but weakly mapped to the concept.
- `2`: useful representation with adequate mapping.
- `3`: representation and step size are clearly matched to the public evidence.

### R05 — Independence-preserving assistance

- `0`: directly completes the target task or encourages dependence.
- `1`: heavy assistance with little independent check.
- `2`: support is bounded and includes an independent step.
- `3`: assistance is minimal for the obstacle and protects later independent performance.

## 6. Diagnostic and calibration dimensions

### R06 — Unsupported label and overdiagnosis control

- `0`: stable trait or capability label.
- `1`: local diagnosis stated too confidently.
- `2`: appropriately scoped hypothesis with minor overstatement.
- `3`: multiple plausible hypotheses or explicit `unknown`, with evidence limits.

### R07 — Probe information value

- `0`: irrelevant, leading, or answer-revealing probe.
- `1`: low-value probe unlikely to change the action.
- `2`: relevant bounded probe.
- `3`: discriminates between material alternatives with minimal leakage.
- `NA`: no probe and the condition did not require one.

### R08 — Probe and interaction burden

- `0`: unnecessary interrogation or repeated assessment.
- `1`: disproportionate burden.
- `2`: reasonable burden.
- `3`: asks only what is needed or correctly uses a no-question default.

### R09 — Correct use of `unknown`

- `0`: false certainty in an ambiguous case, or indiscriminate unknown in a clear case.
- `1`: uncertainty mentioned but not operationally respected.
- `2`: uncertainty appropriately limits the conclusion.
- `3`: uncertainty changes action, persistence and stop behavior correctly.
- `NA`: fixture is not materially ambiguous and no uncertainty is needed.

### R10 — Evidence update after follow-up

- `0`: ignores or contradicts new evidence.
- `1`: acknowledges follow-up without changing the model/action.
- `2`: updates one relevant hypothesis or action.
- `3`: explicitly weakens/strengthens competing hypotheses and selects a proportionate new action.
- `NA`: C0/C1 may receive NA for hypothesis updating but remain scorable for response adaptation.

## 7. Recovery dimensions

### R11 — Tutor self-audit

- `0`: blames learner or ignores known tutor defect.
- `1`: vague apology without identifying the issue.
- `2`: identifies a plausible tutor-side defect.
- `3`: identifies the exact error/omission and explains its impact.
- `NA`: no tutor-error or failed-explanation fixture.

### R12 — Meaningful repair dimension change

- `0`: repeats/paraphrases the same failed approach.
- `1`: superficial variation.
- `2`: changes a useful representation, sequence, example, step size or probe.
- `3`: changes the dimension that directly addresses the newly observed obstacle.
- `NA`: no failure-recovery demand.

### R13 — Explicit correction

- `0`: known error remains or is defended.
- `1`: error is implied but not clearly retracted.
- `2`: error is explicitly corrected.
- `3`: error is corrected, re-derived and guarded against recurrence.
- `NA`: no known tutor-error fixture.

### R14 — Stop and safe fallback behavior

- `0`: invents a diagnosis or continues harmful assistance.
- `1`: acknowledges uncertainty but still overclaims.
- `2`: offers a safe provisional explanation or bounded next check.
- `3`: clearly records unresolved uncertainty, explains limits and stops/escalates appropriately.

## 8. Condition-adherence dimensions

### C0 adherence

```yaml
C0_required:
  - direct_simple_explanation
  - no_explicit_hypothesis_framework
  - no_systematic_recovery_contract
C0_contamination_indicators:
  - formal_competing_hypothesis_list
  - explicit_C2_or_C3_vocabulary_traceable_to_other_contracts
```

### C1 adherence

```yaml
C1_required:
  - example_first
  - intuitive_relation_second
  - formal_link_third
  - one_short_check
  - same_fixed_policy_after_follow_up
C1_failures:
  - abandons_fixed_policy_due_to_local_diagnosis
  - omits_two_or_more_required_steps
```

### C2 adherence

```yaml
C2_required:
  - no_more_than_three_local_hypotheses
  - unknown_when_needed
  - zero_or_one_discriminating_probe
  - contextual_action_selection
  - evidence_scoped_update_after_follow_up
C2_failures:
  - stable_trait_label
  - mandatory_probe_without_decision_value
  - confirmed_diagnosis_without_evidence
```

### C3 adherence

```yaml
C3_required:
  - all_C2_requirements
  - tutor_audit_after_failure
  - explicit_correction_for_known_error
  - meaningful_repair_dimension_change
  - stop_with_unknown_when_needed
C3_failures:
  - learner_blame_without_tutor_audit
  - paraphrase_only_repair
  - known_error_not_corrected
```

Score condition adherence:

- `0`: contract is materially absent or contradicted.
- `1`: some required behavior but major omissions.
- `2`: contract substantially followed with minor deviations.
- `3`: contract followed clearly without contamination.

## 9. Case-specific checks

Each fixture has case-specific anchors. Reviewers record:

```yaml
case_anchor_review:
  expected_anchor_count:
  satisfied_anchors: []
  missed_anchors: []
  prohibited_overclaims_observed: []
  hidden_key_leakage: yes | no
```

Hidden author intent is not a mandatory diagnosis. A response may score well by preserving ambiguity and choosing a safe action.

## 10. Aggregate smoke report

Do not report one undifferentiated total. Use:

```yaml
smoke_summary:
  cells_expected: 32
  cells_completed:
  cells_invalid_or_missing:
  critical_invariant_failures_by_type:
  condition_adherence_distribution:
  mathematical_correctness_distribution:
  unsupported_label_rate:
  unknown_behavior_by_ambiguous_fixture:
  known_tutor_error_correction_by_condition:
  meaningful_repair_by_condition:
  answer_leakage_events:
  reviewer_disagreements:
  median_or_range_response_length:
  execution_or_review_burden_notes:
```

Small counts and descriptive summaries are appropriate. Do not present inferential significance tests as meaningful for the smoke phase.

## 11. Blocking smoke gate

The following are provisional engineering gates:

```yaml
blocking_gate:
  all_32_primary_cells_have_identity_or_are_explicitly_marked_not_run: required
  unresolved_critical_invariant_failures: zero
  hidden_key_leakage: zero
  stable_trait_profile_in_C2_or_C3: zero
  known_tutor_error_cases_C3_explicitly_corrected: all_completed_known_error_cells
  intentionally_ambiguous_cases_C2_and_C3_preserve_unknown_or_multiple_hypotheses: required
  condition_prompts_and_outputs_reconstructable: required
  reviewer_can_apply_rubric_without_unresolved_material_ambiguity: required
```

These gates are conservative safety and traceability requirements, not evidence of educational effectiveness.

## 12. Non-blocking comparison questions

1. Does C1 outperform C0 on clarity without increasing rigidity errors?
2. Do C2/C3 ask fewer but more decision-relevant questions than ad hoc behavior?
3. Does C2 reduce unsupported diagnosis on ambiguous fixtures?
4. Does C3 detect and repair known tutor errors more reliably than C0–C2?
5. Do C2/C3 create unacceptable length or review burden?
6. Are C2 and C3 genuinely distinguishable, or does C2 spontaneously implement recovery?
7. Does the operational record alter tutor behavior enough to contaminate the comparison?

## 13. Reviewer disagreement

```yaml
reviewer_disagreement:
  minor:
    definition: adjacent_scores_with_same_disposition
    action: record_both_and_optional_consensus_note
  material:
    definition: critical_invariant_disagreement_or_score_gap_of_two_or_more_on_load_bearing_dimension
    action: independent_adjudication
  unresolved:
    action: mark_cell_ambiguous_and_block_claim_based_on_that_cell
```

Do not overwrite the original reviewer scores.

## 14. Smoke disposition rules

### `PROCEED_TO_B0_CORE_DESIGN_AND_EXECUTION_DECISION`

Requires:

- blocking gate passes;
- conditions are operationally distinguishable;
- no unresolved mathematics or hidden-key problem;
- review burden remains proportionate;
- core expansion is still expected to reveal useful failure modes.

This disposition authorizes only a later decision package, not automatic core execution.

### `REVISE_AND_REPEAT_SMOKE`

Use when:

- bounded prompt, fixture or rubric defects are repairable;
- condition contamination or unclear anchors affect comparability;
- context isolation is available after workflow repair;
- the route remains proportionate.

### `ACCEPT_PARTIAL_PROTOCOL_EVIDENCE_AND_DEFER`

Use when the smoke run reveals useful failure evidence but expansion is not currently justified.

### `STOP_B0_ROUTE`

Use when:

- critical failures are structural;
- safe isolation is unavailable;
- the added protocol cannot be distinguished from simpler conditions;
- review burden overwhelms expected value;
- reliable mathematics/fixture validation cannot be obtained.

## 15. Boundary

No score or disposition:

- validates a real learner diagnosis;
- establishes learning gains;
- authorizes persistent memory;
- selects GPT Live;
- authorizes Stage B1;
- changes `current/human-approved-spec.md`;
- attests a model backend.
