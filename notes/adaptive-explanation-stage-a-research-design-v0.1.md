# Adaptive Explanation Stage A Research Design v0.1

> Non-execution-source research-design artifact. It accepts the MNEMOSYNE-168 synthesis as the basis for one bounded research stage. It does not execute Deep Research, assess the user, approve a teaching policy, configure GPT Live, create persistent learner memory, or select a target project.

```yaml
research_design_id: ADAPTIVE-EXPLANATION-STAGE-A-RESEARCH-DESIGN-001
created_by_task: MNEMOSYNE-169
source_synthesis: notes/learner-state-and-adaptive-explanation-synthesis-v0.1.md
source_research: PRO-DR-LEARNER-COGNITIVE-COACHING-001
source_raw: raw/chatgpt-discussion-059.md
user_disposition: ACCEPT_SYNTHESIS_AS_RESEARCH_DESIGN_BASIS
status: research_task_ready_not_executed
execution_source: current/human-approved-spec.md
execution_source_modified: false
```

## 1. Purpose

Stage A investigates how an AI text-dialogue tutor can select and repair explanations for a learner whose relevant foundations are uneven, uncertain or locally misunderstood.

The problem is not “use simpler words.” It is a closed-loop decision problem:

```text
current learning target and question
  -> candidate prerequisite routes
  -> local evidence and uncertainty
  -> provisional explanation action
  -> learner response and task evidence
  -> learner-gap / explanation-defect / confounder diagnosis
  -> adapted explanation
  -> transfer, retention, independence and burden evaluation
```

The research should produce an evidence-calibrated candidate framework and a controlled experiment design. It must not claim that a validated universal teaching algorithm already exists.

## 2. Initial domain and generalization boundary

```yaml
initial_domain:
  primary: foundational_university_mathematics
  example_courses:
    - calculus
    - linear_algebra
    - probability_and_statistics
  interaction_surface: text_dialogue
  target_population: adult_or_university_level_learners
  intended_generalization: candidate_principles_for_later_science_and_engineering_transfer
```

Starting with foundational university mathematics is deliberate:

- prerequisites and abstraction transitions are visible;
- multiple representations are common;
- notation can be a distinct barrier;
- near-transfer and unfamiliar-transfer tasks can be constructed;
- correctness and conceptual understanding can often be evaluated separately;
- the user's motivating examples come from these courses.

The report must distinguish mathematics-specific evidence from claims intended to generalize to science, engineering or other domains.

## 3. Objects that research must keep separate

```yaml
separate_objects:
  learner_state_evidence:
    meaning: what_the_learner_has_demonstrated_over_time
  local_explanation_context:
    meaning: what_is_relevant_to_this_question_and_this_turn
  explanation_action:
    meaning: the_entry_point_representation_sequence_step_size_and_probe_selected_by_the_Agent
  explanation_outcome_evidence:
    meaning: whether_the_action_improved_understanding_transfer_retention_and_independence
  presentation_preference:
    meaning: what_the_user_prefers_not_what_the_user_is_capable_of
```

Research must not collapse these objects into a single global “learner level,” “learning style” or stable cognitive type.

## 4. Stage A question clusters

### A. Local difficulty and failure diagnosis

Investigate what observable evidence can help distinguish:

- a genuinely missing prerequisite;
- temporary retrieval failure;
- a connection gap between known components;
- notation or terminology barriers;
- misconception candidates;
- unsupported abstraction jumps;
- representation mismatch;
- question or task misunderstanding;
- excessive cognitive load, pacing or environmental interference;
- defects in the Agent's own explanation;
- insufficient evidence.

The output must identify which distinctions are empirically supported, which are only plausible hypotheses, and which may be non-identifiable from ordinary dialogue.

### B. Prerequisite routes and required mastery

Investigate:

- how prerequisite graphs, knowledge spaces, Q-matrices, learning progressions or other representations can support a local explanation decision;
- how to represent multiple valid prerequisite routes;
- how “required mastery” depends on the target concept and chosen explanation route;
- how partial knowledge, misconceptions and connection gaps differ;
- how to avoid diagnosing every failure as prerequisite absence;
- when domain-expert validation is required.

### C. Low-burden diagnostic interaction

Compare the diagnostic value and user burden of:

- one focused clarification question;
- teach-back or paraphrase;
- a minimal isolating example;
- a forced choice between two interpretations;
- a counterexample check;
- a near-transfer item;
- asking for the first step that no longer follows;
- proceeding with a provisional explanation and adapting from the response.

The research should seek decision value, not maximize testing. It must examine when asking no diagnostic question is preferable.

### D. Explanation-action selection

Investigate evidence for selecting and sequencing:

- concrete examples;
- geometric or visual structure;
- physical or engineering meaning;
- historical or problem motivation;
- analogies with explicit limits;
- formal definitions;
- symbolic derivations;
- counterexamples;
- worked examples and fading;
- comparison with a nearby known concept;
- prerequisite bridge first versus target overview first;
- progressive formalization;
- error-first repair.

The report must treat these as context-dependent actions, not fixed learner styles.

### E. Explanation-failure recovery

Investigate what should happen after a learner says an explanation is unclear or produces evidence of misunderstanding:

- locate the earliest unsupported step;
- re-evaluate the leading failure hypotheses;
- consider an Agent explanation defect;
- change one or more important explanation dimensions;
- switch modality or representation;
- bridge a prerequisite;
- use a minimal discriminating check;
- stop and preserve uncertainty when evidence remains inadequate.

### F. Accessibility without false simplification

Research how to remain accessible while preserving conceptual truth:

- progressive formalization;
- explicit distinction between intuition and definition;
- boundaries of analogies;
- avoiding false rules that must later be unlearned;
- avoiding patronizing language;
- preserving the learner's option to request more rigor, brevity or examples.

### G. Outcome measurement

Evaluate candidate measures for:

```yaml
outcomes:
  immediate_comprehension:
  near_transfer:
  unfamiliar_transfer:
  delayed_retention:
  independent_performance:
  calibration_between_confidence_and_performance:
  error_reduction:
  explanation_repair_success:
  learner_burden_and_cognitive_load:
  autonomy_and_overreliance:
```

The research must explain why conversational fluency and immediate agreement are weak outcome measures by themselves.

## 5. Controlled experiment design requirement

The report must produce a concrete, ethically bounded experiment design comparing at least:

```yaml
conditions:
  C0_generic_simple_instruction:
    description: ask_the_same_model_to_explain_simply_to_a_learner_with_weak_foundations
  C1_fixed_representation_policy:
    description: use_a_fixed_intuitive_or_example_first_policy_without_local_diagnosis
  C2_adaptive_local_diagnosis:
    description: use_bounded_local_prerequisite_and_failure_hypothesis_diagnosis_before_or_during_explanation
  C3_adaptive_plus_recovery:
    description: C2_plus_explicit_explanation_failure_recovery_and_Agent_self_correction
```

The design should specify:

- representative topics from calculus, linear algebra, probability and statistics;
- learner or simulated-participant recruitment assumptions;
- pretest and prerequisite evidence;
- assistance provenance;
- task and difficulty matching;
- immediate, transfer and delayed outcomes;
- user burden and dropout;
- scoring rubrics and blind or independent review where practical;
- contamination and carryover risks;
- model/version/prompt recording without backend overclaim;
- stop criteria and adverse-event handling;
- what can be tested with public/synthetic material before involving real user data.

The report should compare within-subject, between-subject and sequential/adaptive designs and recommend one initial pilot with rationale.

## 6. Evidence traditions to examine

At minimum:

- formative assessment and diagnostic teaching;
- intelligent tutoring systems;
- knowledge tracing and educational measurement;
- cognitive load theory;
- worked examples, fading and expertise reversal;
- multiple representations and representational competence;
- conceptual change and misconception repair;
- self-explanation and retrieval practice;
- tutoring dialogue and Socratic interaction;
- learning progressions and prerequisite structure;
- explanation quality and human-AI explanation;
- open learner models and contestability;
- human factors, accessibility, fairness and learner autonomy;
- recent LLM tutoring studies.

The research must distinguish peer-reviewed evidence, preprints, conceptual frameworks, benchmarks, official guidance and maintainer inference.

## 7. Required report outputs

```yaml
required_outputs:
  - executive_conclusion
  - operational_problem_model
  - definitions_and_object_separation
  - evidence_review_by_research_tradition
  - local_failure_hypothesis_validity_matrix
  - prerequisite_route_and_required_mastery_options
  - low_burden_diagnostic_policy_candidates
  - explanation_action_selection_framework
  - explanation_failure_recovery_framework
  - accessibility_without_false_simplification
  - measurement_and_evaluation_model
  - controlled_experiment_design
  - minimum_viable_text_dialogue_pilot
  - safety_fairness_privacy_and_non_manipulation
  - implications_for_later_memory_system_design
  - findings_that_must_remain_open
  - portable_source_table
  - confidence_calibrated_final_verdict
```

## 8. Explicit exclusions

Stage A must not:

- assess the current user's actual mathematics foundation;
- infer a stable learner, personality, intelligence or cognitive-style profile;
- design psychological or clinical diagnosis;
- configure or evaluate GPT Live as a product surface;
- decide what learner evidence persists across sessions or Agents;
- authorize a knowledge base, Project, memory system or target-project write;
- generate manipulative or covert behavior-shaping techniques;
- claim a universal optimal explanation sequence;
- use a report as execution source.

## 9. Relationship to later stages

```yaml
later_stages:
  Stage_B_controlled_text_dialogue_experiment:
    depends_on: user_review_of_Stage_A_report_and_experiment_design
  Stage_C_GPT_Live_realtime_voice_learning:
    depends_on: a_candidate_general_adaptive_policy_and_fresh_product_fact_check
  Stage_D_longitudinal_memory_and_cross_Agent_integration:
    depends_on: behavioral_evidence_and_separate_user_decision
```

Stage A is not a prerequisite for the core Meta-Agent memory-system build. It may later improve Meta-Agent's ability to design learning Agents, but Meta-Agent upgradeability should allow this capability to be added after the initial build.

## 10. Decision and execution boundary

The accompanying Deep Research task is ready for user execution, but no run is started by MNEMOSYNE-169. A returned report must undergo task-binding, source, completeness and evidence-calibration review before repository ingestion or design adoption.
