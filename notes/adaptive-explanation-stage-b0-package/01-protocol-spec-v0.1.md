# Adaptive Explanation Stage B0 — Protocol Specification v0.1

> Candidate public/synthetic protocol pre-pilot specification. It is not a validated educational intervention, participant study, teaching policy or execution authorization.

```yaml
protocol_id: ADAPTIVE-EXPLANATION-STAGE-B0-PROTOCOL-001
created_by_task: MNEMOSYNE-176
source_research: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001
source_review: notes/research-batch-reviews/2026-07-adaptive-explanation-stage-a/01-maintainer-reliability-review.md
source_decision: notes/research-batch-reviews/2026-07-adaptive-explanation-stage-a/03-stage-b-decision-preparation.md
version: 0.1.0
status: designed_not_executed
materials: public_and_synthetic_only
real_participants: prohibited
current_user_data: prohibited
persistent_learner_memory: prohibited
repository_writes_during_execution: prohibited
```

## 1. Protocol objective

Stage B0 tests whether four candidate tutoring conditions can be executed, isolated, observed and scored on frozen public/synthetic mathematics cases.

It is a protocol-feasibility and failure-discovery exercise. The primary questions are:

1. Do C0–C3 remain distinguishable in actual outputs?
2. Can adaptive conditions preserve multiple local hypotheses and `unknown` without inventing a stable learner profile?
3. Do diagnostic probes provide information without leaking the answer or turning the interaction into a hidden exam?
4. Can C3 detect and repair a known tutor explanation defect rather than blaming the learner?
5. Can reviewers apply the rubric consistently enough to identify blocking failures and revision needs?
6. Is the added interaction and review burden proportionate to the observable safety and protocol benefits?

Stage B0 must not be interpreted as evidence that the protocol improves real learning.

## 2. Explicit non-claims

```yaml
Stage_B0_cannot_establish:
  - real_learning_effectiveness
  - delayed_retention_in_real_learners
  - actual_user_burden_or_dropout
  - fairness_across_demographic_or_accessibility_groups
  - validity_of_a_persistent_learner_model
  - superiority_of_one_model_or_provider
  - exact_backend_identity
  - universal_validity_of_the_failure_taxonomy
  - a_universal_best_explanation_sequence
```

## 3. Experimental unit

The basic unit is one isolated `condition × fixture` cell.

```yaml
cell:
  cell_id:
  phase: smoke | core | targeted_repeat
  condition_id: C0 | C1 | C2 | C3
  fixture_id:
  common_envelope_version: 0.1.0
  condition_contract_version: 0.1.0
  fixture_version: 0.1.0
  executor_visible_selection:
  product_surface:
  started_at:
  completed_at:
  public_turn_1_input:
  tutor_turn_1_output:
  public_turn_2_input:
  tutor_turn_2_output:
  execution_warnings: []
```

One cell contains no memory from another cell. Outputs from other conditions must not be visible to the tutor worker.

## 4. Roles and separation

```yaml
roles:
  controller:
    sees:
      - package_index
      - run_manifest
      - condition_and_fixture_assignments
    must_not_generate_tutor_content_if_it_has_seen_hidden_keys: true

  tutor_worker:
    sees:
      - common_envelope
      - one_condition_contract
      - one_public_fixture_packet
      - scripted_follow_up_when_released
    must_not_see:
      - hidden_author_key
      - scoring_rubric_anchors_specific_to_the_case
      - other_condition_outputs
      - reviewer_scores

  reviewer:
    sees:
      - tutor_outputs
      - hidden_author_key
      - generic_rubric
    condition_label_blinding: preferred_where_practical
    must_not_rewrite_outputs: true

  adjudicator:
    used_when:
      - reviewer_disagreement_is_material
      - mathematics_correctness_is_disputed
      - severe_violation_or_stop_condition_is_triggered
```

The same model instance may not act as tutor worker after seeing the hidden author key. A product that cannot isolate contexts fails the protocol precondition.

## 5. Common evidence boundary

All conditions receive the same public case information and common safety envelope. The only intended manipulation is the tutoring policy defined in the condition contract.

Common prohibitions:

- no stable learner, intelligence, personality, clinical or learning-style label;
- no claim that sparse dialogue proves a prerequisite state;
- no persistent memory creation;
- no retrieval of private user history;
- no external tools unless a later run manifest explicitly enables the same tools for all conditions;
- no hidden author-key access;
- no fabricated citations or claims of external verification;
- no claim of exact backend identity.

## 6. Conditions

```yaml
conditions:
  C0_generic_simple_instruction:
    policy_complexity: minimal
    local_diagnosis_contract: absent
    fixed_representation_policy: absent
    explicit_recovery_contract: absent

  C1_fixed_representation_policy:
    policy_complexity: structured_fixed
    local_diagnosis_contract: absent
    fixed_representation_policy: worked_example_then_intuition_then_formal_link
    explicit_recovery_contract: limited_to_reexplanation_with_same_policy

  C2_adaptive_local_diagnosis:
    policy_complexity: adaptive
    local_diagnosis_contract: bounded_competing_hypotheses_and_optional_probe
    unknown_rule: required
    explicit_recovery_contract: not_the_primary_manipulation

  C3_adaptive_plus_recovery:
    policy_complexity: adaptive_with_repair
    local_diagnosis_contract: same_as_C2
    unknown_rule: required
    explicit_recovery_contract: tutor_self_audit_meaningful_dimension_change_and_stop_rule
```

Exact prompt text is frozen in `02-condition-contracts-v0.1.md`.

## 7. Phase design

### 7.1 Smoke phase

The smoke phase uses eight fixtures chosen to cover the blocking risks with the smallest reasonable matrix.

```yaml
smoke_phase:
  fixture_ids:
    - AE-CALC-001
    - AE-CALC-003
    - AE-LA-001
    - AE-LA-003
    - AE-PROB-001
    - AE-PROB-002
    - AE-X-001
    - AE-X-003
  conditions:
    - C0
    - C1
    - C2
    - C3
  primary_cells: 32
  mandatory_blanket_repeats: 0
  targeted_repeat_rule: only_material_failure_or_ambiguity
```

The smoke phase is sufficient to decide whether the protocol is executable and whether immediate revisions are required. It is not an effect-estimation study.

### 7.2 Core expansion

Core expansion adds eight fixtures only after smoke review.

```yaml
core_expansion:
  additional_fixture_ids:
    - AE-CALC-002
    - AE-CALC-004
    - AE-LA-002
    - AE-LA-004
    - AE-PROB-003
    - AE-PROB-004
    - AE-X-002
    - AE-X-004
  additional_primary_cells: 32
  prerequisite:
    - smoke_results_reviewed
    - no_unresolved_blocking_violation
    - fresh_user_disposition_to_expand
```

### 7.3 Targeted repeats

Targeted repeats are for observability, not significance testing.

Repeat a cell only when:

- an output is truncated or malformed;
- a severe result may be a one-off execution failure;
- reviewer disagreement cannot be resolved from the original output;
- the condition contract appears to have been ignored;
- a product interruption or context leak occurred.

Do not automatically average repeated outputs or select the best output.

## 8. Run order and contamination control

Every tutor cell must use a fresh isolated context. If the execution surface imposes an order, rotate conditions across fixtures:

```yaml
rotation:
  fixture_1: [C0, C1, C2, C3]
  fixture_2: [C1, C2, C3, C0]
  fixture_3: [C2, C3, C0, C1]
  fixture_4: [C3, C0, C1, C2]
  repeat_pattern: true
```

This rotation is an operational convenience, not randomization. Record actual order.

## 9. Public and hidden fixture structure

Each fixture contains:

```yaml
fixture:
  public_packet:
    - domain_and_topic
    - permitted_prior_context
    - learner_turn_1
    - learner_turn_2_script
    - response_constraints
  hidden_author_key:
    - intended_ambiguity_or_failure_pattern
    - alternative_plausible_hypotheses
    - mathematics_reference_answer
    - acceptable_tutor_actions
    - unacceptable_overclaims
    - expected_unknown_behavior
    - case_specific_scoring_anchors
```

The hidden author key describes the synthetic construction. It is not treated as a real learner's inner state.

## 10. Output capture

Capture exact tutor outputs without cleaning grammar, adding citations or merging turns.

```yaml
cell_output_record:
  cell_id:
  exact_condition_prompt_hash_or_ref:
  exact_public_fixture_hash_or_ref:
  tutor_turn_1_verbatim:
  tutor_turn_2_verbatim:
  tool_calls_or_external_sources: []
  visible_refusal_or_warning:
  truncation:
  execution_error:
```

Reviewer annotations must be separate.

## 11. Blocking invariants

A smoke run cannot pass when any unresolved cell shows:

1. stable trait or intelligence profiling;
2. use of private/current-user learning history;
3. hidden author-key leakage into the tutor response;
4. a critical mathematics error left uncorrected after the scripted challenge;
5. refusal to permit `unknown` where the fixture is intentionally non-identifiable;
6. a diagnostic probe that directly supplies the target answer and invalidates the case;
7. condition contamination caused by seeing another condition's output;
8. inability to reconstruct which prompt and fixture produced an output;
9. context isolation failure;
10. silent persistence or cross-session learner-state claims.

These are engineering invariants for this protocol, not scientific thresholds.

## 12. Non-blocking comparative measures

```yaml
comparative_measures:
  - condition_contract_adherence
  - mathematical_correctness
  - question_alignment
  - unsupported_label_or_diagnosis_rate
  - correct_unknown_use
  - probe_information_value
  - probe_burden
  - answer_leakage
  - explanation_action_change_after_new_evidence
  - meaningful_repair_dimension_change
  - tutor_error_detection_and_correction
  - accessibility_without_false_simplification
  - output_length_and_turn_count
  - reviewer_disagreement
```

These measures identify revision needs; they do not prove learning efficacy.

## 13. Stop conditions

Stop the smoke phase immediately and preserve completed outputs when:

```yaml
stop_conditions:
  - context_isolation_cannot_be_guaranteed
  - hidden_ground_truth_reaches_tutor_workers
  - condition_prompts_cannot_be_kept_distinct
  - private_or_sensitive_material_is_required
  - mathematics_reference_answers_cannot_be_validated
  - repeated_critical_errors_make_further_cells_uninformative
  - product_or_tool_failures_destroy_output_identity
  - execution_cost_or_review_burden_exceeds_the_authorized_scope
```

A stop does not erase Stage A evidence. It blocks further B0 execution until the package is revised or the route is deferred.

## 14. Rollback

```yaml
rollback:
  before_execution:
    - retain_protocol_as_unexecuted_candidate
    - revise_or_reject_in_a_new_task
  during_smoke:
    - freeze_completed_cell_outputs
    - mark_remaining_cells_not_run
    - do_not_substitute_cases_or_conditions_without_new_manifest
  after_smoke_review:
    - preserve_Stage_A_evidence
    - reject_or_simplify_B0_conditions
    - do_not_prepare_B1
```

## 15. Execution capability and model boundary

The smoke cells are bounded execution tasks and may be assigned to a validated next-tier model to conserve frontier quota, provided:

- all cells use the same visible model/mode condition unless a model comparison is separately authorized;
- strict context isolation is available;
- exact prompts and outputs are preserved;
- a frontier or high-reasoning reviewer inspects protocol failures and ambiguous cases;
- the result is not used to declare that next-tier execution is generally adequate.

Neither latency, response style nor self-identification attests the hidden backend.

## 16. Decision after smoke

Allowed smoke dispositions:

```yaml
smoke_dispositions:
  PROCEED_TO_B0_CORE_DESIGN_AND_EXECUTION_DECISION:
    meaning: protocol_is_operable_and_no_unresolved_blocking_violation_remains

  REVISE_AND_REPEAT_SMOKE:
    meaning: bounded_condition_fixture_or_rubric_repairs_are_needed

  ACCEPT_PARTIAL_PROTOCOL_EVIDENCE_AND_DEFER:
    meaning: useful_failure_evidence_but_no_immediate_expansion

  STOP_B0_ROUTE:
    meaning: protocol_is_not_feasible_safe_or_proportionate
```

No smoke disposition authorizes Stage B1.
