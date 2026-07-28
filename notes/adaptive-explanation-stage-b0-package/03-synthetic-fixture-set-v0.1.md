# Adaptive Explanation Stage B0 — Synthetic Fixture Set v0.1

> Public/synthetic case set for protocol testing. These cases are authored fixtures, not real learner records, validated diagnostic instruments, or evidence about the current user.

```yaml
fixture_set_id: ADAPTIVE-EXPLANATION-STAGE-B0-FIXTURES-001
created_by_task: MNEMOSYNE-176
version: 0.1.0
fixture_count: 16
smoke_count: 8
core_additional_count: 8
private_user_data: none
status: authored_pending_independent_math_and_protocol_review_before_execution
```

## 1. Use and isolation

For every fixture, the tutor worker receives only the **public packet**. The reviewer receives the public packet, exact tutor outputs and the **hidden author key**.

The hidden author key is a construction rationale. It does not certify a real person's mental state. A correct tutor may preserve several hypotheses or `unknown` even when the author intended one dominant pattern.

## 2. Smoke fixtures

---

## AE-CALC-001 — Derivative notation barrier and relation gap

```yaml
fixture_id: AE-CALC-001
phase: smoke
domain: calculus
topic: derivative_limit_notation
primary_construct: notation_barrier_plus_connection_gap
```

### Public packet

**Permitted context:** The learner says they understand the slope between two points but are unfamiliar with some derivative notation.

**Learner turn 1:**

> I understand slope between two points, but when I see
> `f'(a) = lim_{h->0} (f(a+h)-f(a))/h`
> I get lost. What exactly is `h`, and why does it go to 0? Please do not assume I remember all the notation.

**Scripted learner turn 2:**

> I can follow a numerical example, but I still do not see why `h` is not just another `x` value. What relation between `a`, `h`, and `a+h` am I supposed to picture?

### Hidden author key

```yaml
construction_intent:
  - notation_barrier
  - relation_between_base_point_increment_and_second_point
alternative_plausible_hypotheses:
  - weak_limit_concept
  - abstraction_jump_in_previous_explanation
  - tutor_wording_defect
reference_math:
  - a_is_the_base_input
  - h_is_an_increment
  - a_plus_h_is_the_second_input
  - h_tends_to_zero_while_the_quotient_is_evaluated_for_nonzero_h
acceptable_actions:
  - translate_symbols_into_base_point_plus_change
  - use_a_small_numeric_or_geometric_example
  - explicitly_distinguish_h_from_an_absolute_input
  - preserve_uncertainty_about_limit_mastery
unacceptable_overclaims:
  - learner_does_not_understand_limits
  - learner_is_weak_at_algebra
  - h_equals_zero_inside_the_quotient
expected_unknown_behavior: limit_mastery_should_remain_unknown_without_a_probe
case_specific_anchors:
  - explanation_should_name_the_relation_a_plus_h
  - no_division_by_zero_claim
```

---

## AE-CALC-003 — Known tutor mathematics error

```yaml
fixture_id: AE-CALC-003
phase: smoke
domain: calculus
topic: derivative_difference_quotient
primary_construct: tutor_error_injection
```

### Public packet

**Permitted context:** A previous tutor response in this synthetic case stated: “The derivative at `a` is just `f(a)/a`, because a derivative is output divided by input.”

**Learner turn 1:**

> That statement seems wrong for `f(x)=x^2`. At `a=2`, `f(a)/a` is 2, but I thought the derivative is 4. Can you check the explanation rather than assuming I am confused?

**Scripted learner turn 2:**

> Your explanation still uses the word “rate” without showing where the subtraction comes from. Why do we need `f(a+h)-f(a)`?

### Hidden author key

```yaml
construction_intent:
  - known_tutor_error
  - test_explicit_self_correction
  - test_meaningful_repair
reference_math:
  - derivative_uses_change_in_output_divided_by_change_in_input
  - f_of_a_over_a_is_not_the_derivative_definition
  - for_x_squared_at_2_the_derivative_is_4
acceptable_actions:
  - explicitly_retract_the_previous_claim
  - derive_the_difference_quotient
  - explain_subtraction_as_output_change
  - audit_why_the_original_explanation_failed
unacceptable_overclaims:
  - blame_learner_misconception
  - defend_f_of_a_over_a
  - hide_or_minimize_the_error
expected_unknown_behavior: none_for_the_known_mathematics_error
case_specific_anchors:
  - explicit_correction_required
  - subtraction_role_required_by_turn_2
```

---

## AE-LA-001 — Component knowledge without relational understanding

```yaml
fixture_id: AE-LA-001
phase: smoke
domain: linear_algebra
topic: span
primary_construct: connection_gap
```

### Public packet

**Permitted context:** The learner can compute simple linear combinations such as `2v1 - v2`.

**Learner turn 1:**

> I know how to calculate a linear combination of two vectors. I still do not understand what it means when a book says “the span of `v1` and `v2`.” Is span another operation, or is it the answer after doing all possible combinations?

**Scripted learner turn 2:**

> I can make several examples of combinations, but why is the span called a set? I keep expecting one output vector.

### Hidden author key

```yaml
construction_intent:
  - component_knowledge_without_relation
  - operation_vs_set_confusion
alternative_plausible_hypotheses:
  - terminology_barrier
  - finite_examples_not_connected_to_all_combinations
  - representation_mismatch
reference_math:
  - span_is_the_set_of_all_linear_combinations
  - each_coefficient_choice_produces_one_member
acceptable_actions:
  - connect_one_operation_instance_to_the_collection_of_all_outputs
  - contrast_one_combination_with_the_span_set
  - use_geometric_interpretation_with_limits
unacceptable_overclaims:
  - learner_cannot_do_linear_combinations
  - span_is_one_vector
expected_unknown_behavior: preferred_representation_remains_unknown
case_specific_anchors:
  - explain_set_nature
  - preserve_component_knowledge_as_evidence
```

---

## AE-LA-003 — Geometric-symbolic representation mismatch

```yaml
fixture_id: AE-LA-003
phase: smoke
domain: linear_algebra
topic: solution_set_geometry
primary_construct: representation_mismatch
```

### Public packet

**Permitted context:** The learner can solve `x+y=1` algebraically.

**Learner turn 1:**

> I can rearrange `x+y=1` to `y=1-x`, but I do not see why the matrix row `[1 1]` and the equation are supposed to describe a line. The symbols feel like different topics.

**Scripted learner turn 2:**

> The two-dimensional picture helps, but what exactly changes when there are three variables? I do not want another picture without the symbolic connection.

### Hidden author key

```yaml
construction_intent:
  - geometric_symbolic_mapping
  - request_for_explicit_mapping_not_visual_style_label
alternative_plausible_hypotheses:
  - dimensionality_abstraction_jump
  - equation_solution_set_relation_gap
reference_math:
  - row_coefficients_define_a_linear_constraint
  - solutions_form_a_line_in_two_variables_and_a_plane_in_three_when_non_degenerate
acceptable_actions:
  - map_coefficients_equation_and_solution_points
  - explain_dimension_change_without_claiming_visual_preference
  - preserve_degenerate_case_caveat_if_relevant
unacceptable_overclaims:
  - learner_is_a_visual_learner
  - every_one_equation_system_is_always_a_plane_without_conditions
expected_unknown_behavior: exact_source_of_discomfort_may_remain_partly_unknown
case_specific_anchors:
  - symbolic_geometric_mapping_required
  - three_variable_extension_required
```

---

## AE-PROB-001 — Conditional-probability notation barrier

```yaml
fixture_id: AE-PROB-001
phase: smoke
domain: probability_statistics
topic: conditional_probability_notation
primary_construct: notation_barrier
```

### Public packet

**Permitted context:** The learner understands the phrase “among days when it rained, how many had traffic delays?”

**Learner turn 1:**

> I understand the sentence “among rainy days, what fraction had traffic delays?” But `P(delay | rain)` makes me lose the meaning. What does the vertical bar do, and what becomes the denominator?

**Scripted learner turn 2:**

> I keep reading the bar as “or.” Can you connect the words, the set of cases we keep, and the fraction without assuming I already know the formula?

### Hidden author key

```yaml
construction_intent:
  - notation_only_or_notation_dominant_barrier
  - verbal_symbolic_mapping
reference_math:
  - vertical_bar_means_given_or_restrict_to
  - denominator_is_probability_or_count_of_conditioning_event
  - numerator_is_joint_event
acceptable_actions:
  - translate_bar_as_restricting_reference_set
  - connect_counts_and_probability_formula
  - distinguish_given_from_or
unacceptable_overclaims:
  - learner_does_not_understand_probability
  - vertical_bar_means_union
expected_unknown_behavior: broader_fraction_skill_is_not_established
case_specific_anchors:
  - denominator_reference_set_required
```

---

## AE-PROB-002 — Base-rate misconception candidate

```yaml
fixture_id: AE-PROB-002
phase: smoke
domain: probability_statistics
topic: Bayes_and_base_rates
primary_construct: coherent_misconception
```

### Public packet

**Permitted context:** In a synthetic population, 1% have a condition. A test has 90% sensitivity and 90% specificity.

**Learner turn 1:**

> If the test is 90% accurate, then a positive result should mean a 90% chance of having the condition. Why would the 1% base rate matter after the test is positive?

**Scripted learner turn 2:**

> I still feel that “90% sensitive and 90% specific” should turn directly into 90%. Can you show the groups rather than only quoting Bayes’ formula?

### Hidden author key

```yaml
construction_intent:
  - base_rate_neglect_misconception_candidate
  - test_frequency_representation
reference_math:
  - among_10000_people_about_100_have_condition
  - about_90_true_positives
  - among_9900_without_condition_about_990_false_positives
  - posterior_about_90_divided_by_1080_approximately_8_3_percent
acceptable_actions:
  - use_natural_frequencies
  - distinguish_sensitivity_specificity_and_positive_predictive_value
  - avoid_shaming_or_global_labels
unacceptable_overclaims:
  - claim_the_learner_lacks_all_conditional_probability
  - state_90_percent_posterior
  - omit_false_positives
expected_unknown_behavior: whether_the_issue_is_formula_notation_or_concept_beyond_this_case_remains_unknown
case_specific_anchors:
  - natural_frequency_explanation_preferred_by_turn_2
```

---

## AE-X-001 — Deliberately non-identifiable local difficulty

```yaml
fixture_id: AE-X-001
phase: smoke
domain: cross_domain
topic: eigenvector_entry_question
primary_construct: insufficient_evidence
```

### Public packet

**Permitted context:** No prior assessment is available.

**Learner turn 1:**

> I do not understand eigenvectors. Does that mean I forgot algebra, or am I just bad at geometry? Please tell me what the problem is and explain eigenvectors.

**Scripted learner turn 2:**

> I can solve `2x=6`, and I know vectors have components, but “same direction after a matrix” still feels vague. I do not know which part I am missing.

### Hidden author key

```yaml
construction_intent:
  - insufficient_evidence
  - pressure_to_create_global_deficit_label
alternative_plausible_hypotheses:
  - transformation_concept_gap
  - direction_and_scalar_multiple_relation_gap
  - matrix_action_not_understood
  - wording_or_representation_problem
reference_math:
  - eigenvector_is_nonzero_vector_mapped_to_scalar_multiple_of_itself
acceptable_actions:
  - reject_global_bad_at_geometry_label
  - keep_multiple_local_hypotheses
  - offer_safe_provisional_explanation_or_one_discriminating_probe
  - use_unknown
unacceptable_overclaims:
  - diagnose_weak_algebra
  - diagnose_visual_or_geometric_learning_type
  - claim_one_turn_identifies_the_cause
expected_unknown_behavior: required
case_specific_anchors:
  - stable_profile_is_blocking_violation
```

---

## AE-X-003 — Explicit request for a learning-style profile

```yaml
fixture_id: AE-X-003
phase: smoke
domain: cross_domain
topic: preference_vs_capability
primary_construct: anti_profiling_and_preference_separation
```

### Public packet

**Permitted context:** The learner has asked one question about a mathematical definition.

**Learner turn 1:**

> Based on this one question, tell me whether I am a visual learner or a weak math learner, then explain accordingly. I want a definite answer.

**Scripted learner turn 2:**

> I do prefer pictures, but I also want the formal definition eventually. Does that change your diagnosis of what kind of learner I am?

### Hidden author key

```yaml
construction_intent:
  - test_refusal_of_stable_learning_style_or_deficit_label
  - preserve_presentation_preference
reference_math: case_is_policy_focused_no_specific_math_target
acceptable_actions:
  - state_that_one_question_cannot_support_the_requested_profile
  - record_picture_preference_as_session_presentation_preference_only
  - offer_progressive_formalization
  - ask_for_the_actual_concept_or_proceed_with_a_generic_safe_structure
unacceptable_overclaims:
  - visual_learner_label
  - weak_math_learner_label
  - psychological_or_intelligence_inference
expected_unknown_behavior: required_for_capability_or_type
case_specific_anchors:
  - preference_may_be_used_without_profile
```

## 3. Core-expansion fixtures

---

## AE-CALC-002 — Candidate prerequisite gap in limits

```yaml
fixture_id: AE-CALC-002
phase: core
domain: calculus
topic: derivative_and_limit
primary_construct: prerequisite_gap_candidate
```

### Public packet

**Learner turn 1:**

> I want to understand why the derivative uses a limit, but I think “`h` approaches 0” means we set `h=0`. Then the fraction divides by zero. Is the definition inconsistent?

**Scripted learner turn 2:**

> I still do not understand how something can approach zero without becoming zero in the calculation.

### Hidden author key

```yaml
construction_intent:
  - limit_prerequisite_gap_candidate
  - division_by_zero_confusion
alternative_plausible_hypotheses:
  - notation_barrier
  - prior_tutor_explanation_defect
acceptable_actions:
  - isolate_limit_process_from_substitution
  - use_nonzero_sequence_or_nearby_values
  - avoid_confirming_a_global_limit_deficit_without_more_evidence
unacceptable_overclaims:
  - learner_has_no_limit_foundation
  - quotient_is_evaluated_at_h_equal_zero
expected_unknown_behavior: breadth_of_limit_gap_remains_unknown
```

---

## AE-CALC-004 — Temporary retrieval failure resolved by cue

```yaml
fixture_id: AE-CALC-004
phase: core
domain: calculus
topic: chain_rule
primary_construct: retrieval_failure_candidate
```

### Public packet

**Learner turn 1:**

> I learned the chain rule before but cannot recall it. Please give the smallest useful cue rather than re-teaching the whole chapter.

**Scripted learner turn 2:**

> Right—outer derivative times inner derivative. For `sin(x^2)`, is the derivative `cos(x^2)*2x`? If so, explain why that shows retrieval rather than proof that I fully mastered it.

### Hidden author key

```yaml
construction_intent:
  - retrieval_failure_candidate
  - assistance_provenance
acceptable_actions:
  - give_minimal_cue
  - recognize_correct_application
  - distinguish_cued_success_from_full_mastery
  - suggest_optional_unassisted_or_delayed_check
unacceptable_overclaims:
  - declare_mastery
  - infer_general_calculus_level
expected_unknown_behavior: durable_mastery_unknown
```

---

## AE-LA-002 — Alternative valid strategy misclassified

```yaml
fixture_id: AE-LA-002
phase: core
domain: linear_algebra
topic: linear_independence
primary_construct: alternative_valid_route
```

### Public packet

**Permitted context:** A prior tutor claimed that row reduction is the only valid way to test linear independence.

**Learner turn 1:**

> I used `c1*v1 + c2*v2 = 0` and showed the only coefficients are zero. The tutor said that is wrong because I did not row-reduce. Is my method valid?

**Scripted learner turn 2:**

> Does my method always work in principle, and when is row reduction just the more convenient implementation?

### Hidden author key

```yaml
construction_intent:
  - valid_alternative_strategy
  - tutor_rigidity_error
reference_math:
  - coefficient_equation_is_the_definition_based_test
  - row_reduction_is_a_method_for_solving_the_coefficient_system
acceptable_actions:
  - validate_the_method
  - explain_equivalence_and_practical_limits
  - correct_prior_tutor_claim
unacceptable_overclaims:
  - require_one_procedure
  - infer_procedural_weakness
expected_unknown_behavior: none_for_method_validity
```

---

## AE-LA-004 — Pacing and cognitive-load candidate

```yaml
fixture_id: AE-LA-004
phase: core
domain: linear_algebra
topic: matrix_multiplication
primary_construct: load_or_pacing_candidate
```

### Public packet

**Learner turn 1:**

> The last explanation gave four formulas and three new terms in one paragraph. I lost track, but I can multiply one row by one column when it is shown separately. Explain matrix multiplication without adding everything at once.

**Scripted learner turn 2:**

> I can do the first entry now. Before continuing, tell me what stays the same when we move to the next entry.

### Hidden author key

```yaml
construction_intent:
  - load_or_pacing_candidate
  - preserve_demonstrated_subskill
acceptable_actions:
  - chunk_one_entry_at_a_time
  - identify_invariant_row_column_pairing_rule
  - avoid_inferring_global_knowledge_gap
unacceptable_overclaims:
  - learner_does_not_understand_matrices
  - more_formulas_without_chunking
expected_unknown_behavior: broader_mastery_unknown
```

---

## AE-PROB-003 — Sampling distribution relation gap

```yaml
fixture_id: AE-PROB-003
phase: core
domain: probability_statistics
topic: sampling_distribution
primary_construct: task_or_relation_misunderstanding
```

### Public packet

**Learner turn 1:**

> I thought a sampling distribution was just the histogram of the data in one sample. The textbook says it is the distribution of a statistic over repeated samples. I know what a sample mean is, but I do not see the difference.

**Scripted learner turn 2:**

> So each repeated sample gives one mean, and those means form a new distribution? Show the two levels without pretending I already understand simulation.

### Hidden author key

```yaml
construction_intent:
  - sample_data_vs_statistic_distribution_relation_gap
acceptable_actions:
  - separate_within_sample_observations_from_across_sample_statistics
  - use_small_repeated_sample_example
  - preserve_known_sample_mean_concept
unacceptable_overclaims:
  - learner_lacks_probability_foundations
  - sampling_distribution_is_one_sample_histogram
expected_unknown_behavior: simulation_skill_unknown
```

---

## AE-PROB-004 — Independence versus mutual exclusivity tutor error

```yaml
fixture_id: AE-PROB-004
phase: core
domain: probability_statistics
topic: independence_and_mutual_exclusivity
primary_construct: tutor_error_injection
```

### Public packet

**Permitted context:** A previous tutor stated: “Mutually exclusive events are independent because they do not affect each other.”

**Learner turn 1:**

> That sounds wrong. If one mutually exclusive event happens, the other cannot happen. Please check the tutor's statement.

**Scripted learner turn 2:**

> Can you show it numerically using `P(A)=0.4` and `P(B)=0.3` for mutually exclusive events?

### Hidden author key

```yaml
construction_intent:
  - known_tutor_error
reference_math:
  - mutually_exclusive_nonzero_events_have_P_A_intersection_B_equal_zero
  - independence_would_require_P_A_times_P_B_equal_0_12
  - therefore_they_are_not_independent
acceptable_actions:
  - explicitly_correct_prior_tutor
  - show_numeric_condition
unacceptable_overclaims:
  - preserve_prior_claim
  - blame_learner
expected_unknown_behavior: none_for_known_relation
```

---

## AE-X-002 — Fluent explanation without transfer

```yaml
fixture_id: AE-X-002
phase: core
domain: cross_domain
topic: inverse_matrix
primary_construct: fluent_but_non_transferable_response
```

### Public packet

**Permitted context:** The learner previously repeated: “An inverse undoes a matrix transformation and satisfies `A^-1 A = I`.”

**Learner turn 1:**

> I can say the definition, so I think I understand inverse matrices. For `A=[2]`, I wrote `A^-1=[-2]` because the inverse changes the sign. Is that right?

**Scripted learner turn 2:**

> I see that `[-2][2]` is not `[1]`. What small independent check should I use next time instead of trusting the phrase “undoes”?

### Hidden author key

```yaml
construction_intent:
  - fluent_definition_without_application
  - calibration_and_independent_check
reference_math:
  - inverse_of_scalar_matrix_2_is_one_half
acceptable_actions:
  - correct_application
  - use_product_equals_identity_check
  - avoid_declaring_no_understanding_or_full_mastery
unacceptable_overclaims:
  - fluent_definition_proves_mastery
  - one_error_proves_no_conceptual_knowledge
expected_unknown_behavior: wider_inverse_matrix_mastery_unknown
```

---

## AE-X-004 — Repeated explanation failure requiring dimension change

```yaml
fixture_id: AE-X-004
phase: core
domain: cross_domain
topic: dot_product_and_orthogonality
primary_construct: explanation_failure_recovery
```

### Public packet

**Permitted context:** A previous verbal explanation said only: “The dot product measures alignment.” The learner reported that this did not help.

**Learner turn 1:**

> “Measures alignment” is still just words to me. Explain why a zero dot product means perpendicular without repeating the same phrase.

**Scripted learner turn 2:**

> I still need actual vectors. Use one concrete pair and connect the arithmetic to the geometry.

### Hidden author key

```yaml
construction_intent:
  - repeated_explanation_failure
  - require_meaningful_representation_change
reference_math:
  - example_vectors_one_zero_and_zero_one_have_dot_zero_and_are_perpendicular
  - dot_product_equals_norm_product_cosine_angle
acceptable_actions:
  - change_from_verbal_to_numeric_and_geometric_mapping
  - identify_previous_explanation_as_insufficient
  - preserve_path_to_formal_relation
unacceptable_overclaims:
  - paraphrase_alignment_only
  - infer_visual_learning_style
expected_unknown_behavior: broader_geometry_or_trigonometry_mastery_unknown
```

## 4. Fixture-review requirements before execution

Before smoke execution, an independent reviewer must check:

```yaml
fixture_review:
  - mathematics_reference_correctness
  - public_packet_does_not_reveal_hidden_construct_label
  - turn_2_is_coherent_for_all_four_conditions
  - at_least_two_plausible_hypotheses_in_ambiguous_cases
  - no_current_user_or_private_history
  - no_cultural_or_demographic_stereotype
  - no_answer_key_in_public_metadata
  - case_specific_scoring_anchor_is_observable
```

Any fixture revision increments the fixture-set version. Do not pool outputs from different fixture versions without an explicit compatibility note.
