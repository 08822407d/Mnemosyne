# Adaptive Explanation Stage A — Report Review and Convergence Instrument v0.1

> Non-execution-source maintainer instrument for reviewing the returned `PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001` report. It does not accept evidence in advance, replace source inspection, approve a teaching policy, execute Stage B, or authorize learner profiling, GPT Live, persistent memory or cross-Agent sharing.

```yaml
instrument_id: ADAPTIVE-EXPLANATION-STAGE-A-REPORT-REVIEW-001
created_by_task: MNEMOSYNE-174
research_id: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001
research_design: notes/adaptive-explanation-stage-a-research-design-v0.1.md
research_prompt: notes/research-prompts/PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001.md
execution_package: notes/adaptive-explanation-stage-a-execution-and-return-package-v0.1.md
status: ready_not_used
execution_source: current/human-approved-spec.md
execution_source_modified: false
```

## 1. Review objective

Determine whether the returned report is:

- the requested Stage A research rather than a substitute topic;
- structurally complete;
- supported by identifiable and portable sources;
- calibrated to evidence maturity and domain limits;
- useful for a candidate adaptive-explanation framework and a controlled text-dialogue experiment;
- safe to store as non-execution-source evidence;
- sufficient to prepare a Stage B decision package without pretending an experiment has already been validated.

The review must preserve the original report bytes. Corrections, source recovery and maintainer inference belong in separate records.

## 2. Artifact receipt

```yaml
artifact_receipt:
  report_filename:
  report_bytes:
  report_sha256:
  report_line_count:
  report_word_count:
  literal_https_URL_count:
  citation_marker_count:
  unique_citation_reference_count:
  required_section_count_found:
  source_table_row_count:
  run_metadata_received: yes | no | partial
  native_plan_received: yes | no
  downloaded_copy_matches_inline_report: yes | no | unknown
```

When inline and downloaded reports differ, preserve both and identify which one is complete. Do not silently merge them.

## 3. Gate A — Input and task binding

All blocking identity checks must pass:

```yaml
Gate_A:
  exact_research_ID: pass | fail
  exact_topic: pass | fail
  input_integrity_receipt: pass | fail
  substantive_research_completed: pass | fail
  generic_or_substitute_topic_absent: pass | fail
  previous_failed_outputs_not_used_as_evidence: pass | fail | unknown
  current_user_not_assessed_or_profiled: pass | fail
  GPT_Live_persistence_or_cross_Agent_scope_not_substituted: pass | fail
```

Any failure in exact ID, exact topic or substantive completion yields:

```yaml
disposition: CLEAN_RERUN_REQUIRED_OR_INVALID_TASK_OUTPUT
```

A plan, outline or readiness receipt is not a report.

## 4. Gate B — Required output contract

Review all nineteen required sections:

```yaml
required_sections:
  1_executive_conclusion:
  2_operational_problem_model_and_terminology:
  3_object_separation:
  4_evidence_review_by_research_tradition:
  5_local_failure_hypothesis_validity_and_confounder_matrix:
  6_prerequisite_route_and_required_mastery_options:
  7_low_burden_diagnostic_policy_candidates:
  8_explanation_action_selection_framework:
  9_explanation_failure_recovery_framework:
  10_accessibility_without_false_simplification:
  11_outcome_and_measurement_framework:
  12_controlled_experiment_design:
  13_minimum_viable_text_dialogue_pilot:
  14_safety_fairness_privacy_autonomy_and_non_manipulation:
  15_later_memory_system_implications_without_persistence_design:
  16_findings_that_must_remain_open:
  17_adoption_stop_rollback_and_falsification_criteria:
  18_portable_source_table:
  19_confidence_calibrated_final_verdict:
```

For each section record:

```yaml
section_review:
  status: complete | partial | absent | off_topic
  load_bearing_claims: []
  unsupported_or_overstated_claims: []
  required_correction_or_addendum:
```

A section heading alone is not completion.

## 5. Gate C — Core conceptual integrity

The report must keep separate:

```yaml
objects:
  learner_state_evidence:
  local_explanation_context:
  explanation_action:
  explanation_outcome_evidence:
  presentation_preference:
```

Reject or correct claims that:

- turn a broad self-description into a global learner level;
- infer a fixed visual/verbal/intuitive/formal learning style;
- treat fluent dialogue, satisfaction or immediate agreement as proof of mastery;
- assume every explanation failure is a learner deficit;
- treat model-generated hypotheses as confirmed learner truth;
- imply psychological, intelligence, personality or clinical diagnosis;
- present one explanation sequence as universally optimal.

## 6. Gate D — Local failure-hypothesis validity

The report should evaluate, not merely list:

- missing prerequisite;
- retrieval failure;
- connection gap;
- notation or terminology barrier;
- misconception candidate;
- unsupported abstraction jump;
- representation mismatch;
- learner task misunderstanding;
- tutor misunderstanding of the question;
- cognitive load, pacing or environmental confounder;
- defective or incorrect Agent explanation;
- insufficient/non-identifiable evidence.

For each category review whether the report provides:

```yaml
failure_hypothesis_review:
  observable_evidence:
  confounders:
  false_positive_risk:
  false_negative_risk:
  dialogue_only_identifiability:
  stronger_evidence_needed:
  unknown_or_stop_rule:
```

A report that claims reliable fine-grained diagnosis from ordinary dialogue alone requires strong direct evidence and should otherwise be downgraded.

## 7. Gate E — Prerequisite and mastery representation

Review treatment of:

- multiple valid prerequisite routes;
- route-specific required mastery;
- partial knowledge;
- misconceptions;
- component knowledge without relational understanding;
- alternative valid solution strategies;
- granularity;
- cold start;
- evidence decay;
- domain-expert validation.

The report should not imply that one universal prerequisite graph or mastery threshold fits all explanations or learners.

## 8. Gate F — Diagnostic burden and explanation actions

The report must compare the information value and burden of focused questions, teach-back, isolating examples, forced choices, counterexamples, transfer checks, first-broken-step questions, provisional explanation and no-question defaults.

Review whether the candidate policy:

- asks only when competing explanation routes would materially change the action;
- explains the purpose of a diagnostic question;
- permits a direct explanation when the learner does not want assessment;
- uses teaching interactions as evidence without turning every exchange into an exam;
- distinguishes preference from need;
- can change entry point, representation, sequence, abstraction step, terminology density, pacing and modality.

## 9. Gate G — Explanation-failure recovery

A sufficient recovery framework must do more than paraphrase. It should:

1. locate the earliest unsupported or misunderstood step;
2. maintain competing failure hypotheses;
3. include Agent error as a candidate;
4. change a meaningful explanation dimension;
5. use a discriminating low-burden check;
6. switch representation or modality when justified;
7. stop and preserve uncertainty when evidence is inadequate;
8. correct the Agent's own factual or pedagogical error.

Review whether claimed repair strategies are supported by tutoring, feedback, conceptual-change, refutation, self-explanation or human-AI repair evidence rather than generic prompt advice.

## 10. Gate H — Outcome and experiment design

### Outcome framework

The report should distinguish:

```yaml
outcomes:
  immediate_comprehension:
  near_transfer:
  unfamiliar_transfer:
  delayed_retention:
  independent_performance:
  calibration:
  error_reduction:
  explanation_repair_success:
  burden_and_cognitive_load:
  autonomy_and_overreliance:
```

### Controlled conditions

```yaml
required_conditions:
  C0_generic_simple_instruction:
  C1_fixed_representation_policy:
  C2_adaptive_local_diagnosis:
  C3_adaptive_plus_recovery:
```

### Design review

Review:

- representative calculus, linear algebra and probability/statistics topics;
- prerequisite structures;
- population assumptions;
- pretest and local evidence;
- assistance provenance;
- task-difficulty matching;
- within-subject versus between-subject versus sequential/adaptive tradeoffs;
- immediate, transfer and delayed assessment;
- blind/independent scoring where practical;
- burden and dropout;
- carryover, practice and demand characteristics;
- tutor-model contamination;
- prompt/model/tool/date recording without backend overclaim;
- public/synthetic pre-pilot before real participant data;
- safety, consent, privacy and stop conditions;
- a defensible minimum viable pilot;
- no invented numerical power claim.

A detailed experiment is still a candidate until separately accepted and executed.

## 11. Gate I — Source portability and source sampling

### Portable source table

Every load-bearing source row should include:

- full literal `https://` URL;
- title;
- authors or organization;
- DOI, arXiv or stable identifier where available;
- publication/update date;
- access date;
- source type;
- claim/section mapping;
- direct versus analogical support;
- access or verification limitation.

Opaque local citation IDs, bare titles, bare DOI strings and non-clickable domain/path text do not satisfy portability.

### Source-sampling rule

This is an audit-workload rule, not a scientific threshold:

```yaml
source_sample:
  if_load_bearing_sources_15_or_fewer: inspect_all
  if_more_than_15: inspect_at_least_15_across_all_major_claim_clusters
  always_inspect:
    - every_source_supporting_the_final_disposition
    - every_current_or_volatile_product_claim
    - every_surprising_effect_size_or_strong_causal_claim
    - every_source_used_to_claim_diagnostic_validity
    - every_source_used_to_generalize_from_math_to_other_domains
    - every_source_that_appears_misnamed_or_inaccessible
```

Prefer original papers, systematic reviews, validated instruments and official standards. Search snippets, marketing pages and secondary summaries cannot carry central claims when primary sources are available.

## 12. Gate J — Evidence calibration

For each major conclusion record:

```yaml
claim_calibration:
  claim:
  support_class:
    - direct_empirical
    - adjacent_empirical
    - systematic_review_or_meta_analysis
    - validated_measurement_or_standard
    - conceptual_framework
    - official_guidance
    - engineering_inference
  maturity:
    - replicated_peer_reviewed
    - peer_reviewed_bounded
    - preprint_or_unreplicated
    - qualitative_or_small_sample
    - conceptual_only
  population_and_domain:
  direct_or_analogical:
  contradictory_or_null_evidence:
  heterogeneity:
  confidence: low | moderate | moderate_to_high | high
  maintainer_disposition:
```

Uncalibrated numerical confidence values should not be preserved as probabilities.

## 13. Gate K — Consistency with existing Mnemosyne evidence

Compare the report against:

- `PRO-DR-LEARNER-COGNITIVE-COACHING-001` and its maintainer corrections;
- `notes/learner-state-and-adaptive-explanation-synthesis-v0.1.md`;
- `notes/adaptive-explanation-stage-a-research-design-v0.1.md`;
- the learner-state, metacognitive coaching and cross-Agent reuse TODO boundaries;
- current privacy, source, authority and no-automatic-promotion rules.

Record:

```yaml
consistency_review:
  confirms_existing_evidence: []
  refines_existing_evidence: []
  conflicts_with_existing_evidence: []
  new_claims: []
  claims_requiring_user_decision: []
  claims_outside_Stage_A: []
```

Do not force agreement. Preserve reliable conflicts for adjudication.

## 14. Final report dispositions

```yaml
allowed_dispositions:
  ACCEPT_STAGE_A_AND_PREPARE_STAGE_B_DECISION_PACKAGE:
    meaning: report_is_reliable_enough_for_non_execution_source_ingestion_and_a_candidate_Stage_B_decision_package

  ACCEPT_WITH_CORRECTIONS_AND_PREPARE_STAGE_B_DECISION_PACKAGE:
    meaning: original_report_is_preserved_and_bounded_maintainer_corrections_do_not_require_research_scope_reopening

  ACCEPT_EVIDENCE_ONLY_DEFER_STAGE_B:
    meaning: useful_evidence_but_experiment_design_or_policy_basis_is_not_ready

  BOUNDED_ADDENDUM_REQUIRED:
    meaning: topic_is_correct_but_missing_portability_or_limited_sections_can_be_repaired_without_full_rerun

  CLEAN_RERUN_REQUIRED:
    meaning: wrong_topic_input_loss_major_scope_failure_or_unrecoverable_source_problem

  REJECT:
    meaning: report_is_not_reliable_or_not_useful_for_the_route
```

No disposition makes the report execution source or approves an experiment.

## 15. Same-turn convergence after an accepted report

When the user returns the report with the execution package's consolidated instruction, and the verdict is one of the first two accepted dispositions, the same maintainer turn may prepare one bounded PR containing:

```yaml
conditional_single_PR_contents:
  - exact_original_prompt_and_report_storage_or_manifest_governed_archive
  - run_metadata_and_artifact_receipt
  - maintainer_reliability_review
  - claim_and_evidence_calibration_ledger
  - current_Stage_A_status_closeout
  - Stage_B_decision_preparation_only
  - task_result_and_PR_lineage_records
```

`Stage_B_decision_preparation_only` may summarize:

- candidate pilot objective;
- candidate C0–C3 conditions;
- report-supported measures;
- unresolved choices;
- safety and data boundaries;
- whether a synthetic/public pre-pilot is justified;
- what user decision is still required.

It must not:

- execute Stage B;
- enroll or assess the current user;
- create a persistent learner profile;
- configure GPT Live;
- authorize real participant data;
- select cross-Agent sharing;
- make a teaching policy an execution source.

If the report requires a new research-scope, privacy, participant or intervention decision, stop after the review and present one compact decision package.

## 16. Proposed ingestion boundary after acceptance

Candidate paths, subject to latest-master and duplicate checks at the time:

```text
raw/research-reports/cycles/2026Q3-adaptive-explanation-stage-a/
notes/research-batch-reviews/2026-07-adaptive-explanation-stage-a/
current/adaptive-explanation-stage-a-research-status.md
notes/codex-task-results/<fresh-task-id>-result.md
notes/codex-task-results/<fresh-task-id>-pr-finalization.md
```

The exact archive layout must be chosen after the real report size and files are known. Do not pre-create empty archives or fabricate report identities.

## 17. Review output contract

```yaml
Stage_A_maintainer_review:
  artifact_receipt:
  Gate_A_input_binding:
  Gate_B_output_contract:
  Gate_C_conceptual_integrity:
  Gate_D_failure_hypotheses:
  Gate_E_prerequisite_representation:
  Gate_F_diagnostic_and_action_policy:
  Gate_G_recovery:
  Gate_H_outcomes_and_experiment:
  Gate_I_sources:
  Gate_J_evidence_calibration:
  Gate_K_consistency:
  blocking_defects: []
  nonblocking_corrections: []
  accepted_findings: []
  unresolved_findings: []
  rejected_findings: []
  final_disposition:
  confidence: low | moderate | moderate_to_high | high
  repository_ingestion_recommended: yes | no | after_repair
  Stage_B_decision_preparation_recommended: yes | no | after_user_decision
```

## 18. Boundaries

- This instrument does not predetermine the report verdict.
- It does not validate a model or backend.
- It does not replace source inspection.
- It does not assess or profile the current user.
- It does not approve a learner-state schema or adaptive-teaching algorithm.
- It does not execute Stage B or generate a final experiment protocol before evidence review.
- It does not configure GPT Live or persistent/cross-Agent memory.
- It does not authorize repository ingestion before the returned report is reviewed.
