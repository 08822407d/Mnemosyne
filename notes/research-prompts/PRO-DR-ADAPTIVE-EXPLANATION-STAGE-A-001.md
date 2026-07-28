# PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001 — Adaptive Explanation and Local Prerequisite Diagnosis

> **Operator instruction:** run this in a fresh Pro Deep Research task. Prefer pasting the complete file into the message body. Do not use a plan-only response as the final report.

```yaml
protocol_version: v1
research_id: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001
exact_topic: How an AI text-dialogue tutor can diagnose local prerequisite state and select, evaluate, and repair understandable explanations for foundational university mathematics without relying on a global learner-level label
execution_mode: automatic_single_pass
research_surface: Pro_Deep_Research
repository_write: prohibited
connected_service_write: prohibited
actual_user_assessment: prohibited
GPT_Live_product_research: excluded_from_Stage_A
persistent_learner_profile_design: excluded_from_Stage_A
```

## Mandatory input-integrity rule

Before substantive research, verify internally that the exact research ID, exact topic, complete task text, required output sections, evidence requirements and exclusions are available.

If the check passes:

- begin substantive research immediately;
- do not stop after a plan, outline, receipt or readiness message;
- do not ask the user to reply with “approve,” “批准计划,” `CONTINUE`, or an equivalent phrase;
- if the product displays a native research plan, continue automatically to the extent the product surface permits;
- place the completed integrity receipt at the beginning of the final report.

If the check fails, return only:

```yaml
status: INPUT_INTEGRITY_FAILURE
research_id: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001
substantive_research_started: false
missing_or_truncated_inputs: []
observed_substitute_topic:
```

Do not substitute a generic research-methodology topic, Python reproducibility topic, broad learner-model survey, GPT Live product review, or unspecified subject.

## Required final-report opening

```yaml
input_integrity_receipt:
  research_id: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001
  exact_topic: How an AI text-dialogue tutor can diagnose local prerequisite state and select, evaluate, and repair understandable explanations for foundational university mathematics without relying on a global learner-level label
  full_task_text_available: true
  generic_or_substitute_topic_used: false
  previous_failed_outputs_used_as_evidence: false
  substantive_research_completed: true
```

## Runtime-provenance boundary

This task cannot identify or attest the hidden serving model. The final report must include:

```yaml
runtime_provenance:
  operator_visible_selection: unknown_unless_explicitly_available
  exact_served_backend: unknown_or_not_attestable
  response_speed_used_as_identity_evidence: false
  model_self_identification_used_as_evidence: false
```

Correct topic binding and a strong report are evidence of task performance, not backend identity.

---

# Research task

## 1. Research objective

Produce an evidence-first, cross-disciplinary analysis of how an AI text-dialogue tutor should decide **how to explain a current foundational mathematics concept or answer a current learner question** when the learner's relevant foundations are uneven, uncertain, partially connected, temporarily inaccessible, or misunderstood.

The motivating failure is that prompts such as:

> “My foundations are weak; explain this in a way that does not require a strong foundation.”

are not operational teaching policies. A high-capability model may still fail to determine:

- which prerequisites matter for the current question;
- which are present, missing, temporarily inaccessible or merely disconnected;
- whether notation, terminology, pacing or representation is the real barrier;
- whether the Agent misunderstood the question or gave a defective explanation;
- which explanation entry point, abstraction level, step size, sequence, probe and modality should be used;
- whether apparent understanding is robust or merely conversational fluency.

The report must develop an evidence-calibrated **local closed-loop pedagogical decision model**, not a stable global learner type.

## 2. Initial scope

```yaml
initial_scope:
  subject_domain:
    - calculus
    - linear_algebra
    - probability_and_statistics
  learner_context: adult_or_university_level_foundational_learning
  interaction_surface: text_dialogue
  output_type:
    - evidence_review
    - candidate_decision_framework
    - controlled_experiment_design
  later_transfer_target:
    - science
    - engineering
  explicitly_not_in_scope:
    - GPT_Live_or_voice_product_configuration
    - persistent_cross_session_learner_memory_policy
    - cross_Agent_profile_sharing
    - actual_assessment_of_the_current_user
```

Use mathematics-specific evidence where available, but mark every attempted generalization to other fields.

## 3. Required object separation

Do not collapse these objects:

```yaml
learner_state_evidence:
  question: What has the learner demonstrated, with source, scope, recency, assistance provenance and uncertainty?

local_explanation_context:
  question: What matters for this concept, question, notation, modality and session now?

explanation_action:
  question: What entry point, representation, sequence, step size, probe and modality does the tutor choose?

explanation_outcome_evidence:
  question: Did the action improve understanding, transfer, retention, calibration, independence and burden?

presentation_preference:
  question: What does the learner prefer, without treating preference as capability proof or a fixed learning style?
```

## 4. Core research questions

### 4.1 Local difficulty and explanation-failure diagnosis

What evidence can distinguish, and with what validity and burden:

- missing prerequisite;
- temporary retrieval failure;
- connection gap between known ideas;
- notation or terminology barrier;
- misconception candidate;
- unsupported abstraction jump;
- representation mismatch;
- learner misunderstanding of the task;
- tutor misunderstanding of the learner's question;
- excessive cognitive load, pacing or environmental interference;
- a defective or incorrect Agent explanation;
- insufficient or non-identifiable evidence?

For every category, state:

- observable evidence;
- likely confounders;
- false-positive and false-negative risks;
- whether ordinary dialogue can distinguish it;
- when a task, artifact, transfer probe or human confirmation is necessary;
- when the tutor should record `unknown` instead of deciding.

### 4.2 Local prerequisite routes and required mastery

Compare prerequisite graphs, knowledge spaces, Q-matrices, learning progressions, concept inventories, cognitive task analysis and other suitable representations.

Address:

- multiple valid routes to the same target concept;
- route-specific rather than universal prerequisite thresholds;
- partial mastery and misconceptions;
- knowing components without knowing their relation;
- alternative valid solution strategies;
- prerequisite granularity and domain-expert validation;
- cold start and evidence decay;
- why a broad “weak foundations” self-description is only a weak prior.

### 4.3 Low-burden diagnostic interaction

Evaluate the diagnostic value and learner burden of:

- one focused clarification question;
- teach-back or paraphrase;
- a minimal isolating example;
- forced choice between two interpretations;
- counterexample checks;
- near-transfer and unfamiliar-transfer items;
- asking for the first step that no longer follows;
- proceeding with a provisional explanation and adapting from the response;
- asking no question and using a safe default.

Develop candidate rules for when a diagnostic probe is worth its interruption cost. The goal is not to turn every teaching exchange into an examination.

### 4.4 Explanation-action selection

Review evidence for choosing and sequencing:

- concrete examples;
- geometric or visual structures;
- physical or engineering meaning;
- historical/problem motivation;
- analogies with explicit limits;
- formal definitions;
- symbolic derivations;
- counterexamples;
- worked examples, completion problems and fading;
- comparison with familiar nearby concepts;
- prerequisite bridge first versus target overview first;
- progressive formalization;
- error-first repair;
- terminology density, abstraction level, step size, turn length and repetition.

Do not infer a fixed visual/verbal/intuitive/formal learner style. Treat these as contextual actions whose value must be tested.

### 4.5 Recovery after an explanation fails

Research a repair loop that can:

1. locate the earliest unsupported or misunderstood step;
2. maintain multiple competing failure hypotheses;
3. include the possibility of an Agent error;
4. change a meaningful explanation dimension rather than merely paraphrase;
5. use a minimal discriminating check;
6. switch representation or modality where useful;
7. stop and preserve unresolved uncertainty when needed.

Examine evidence on feedback, error diagnosis, conceptual change, refutation/counterexample use, self-explanation, tutoring dialogue and human-AI explanation repair.

### 4.6 Accessibility without false simplification

How can an explanation remain accessible without teaching false rules or hiding necessary structure?

Address:

- intuition versus definition;
- progressive formalization;
- explicit analogy limits;
- local prerequisite bridges;
- avoiding oversimplifications that must later be unlearned;
- learner control over rigor, brevity, examples and pacing;
- avoiding patronizing language and permanent deficit labels.

### 4.7 Outcome measurement

Evaluate measures for:

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

Explain why conversational fluency, correct repetition, learner satisfaction and “I understand” are insufficient alone.

## 5. Controlled experiment design

Design a feasible initial study comparing at least:

```yaml
conditions:
  C0_generic_simple_instruction:
    prompt_pattern: explain_simply_to_a_learner_with_weak_foundations
  C1_fixed_representation_policy:
    prompt_pattern: always_begin_with_an_intuitive_or_worked_example
  C2_adaptive_local_diagnosis:
    prompt_pattern: maintain_local_failure_hypotheses_and_use_bounded_diagnostic_evidence
  C3_adaptive_plus_recovery:
    prompt_pattern: C2_plus_explicit_explanation_failure_recovery_and_Agent_self_correction
```

Specify:

- representative topics and prerequisite structures from calculus, linear algebra, probability and statistics;
- study population and inclusion/exclusion assumptions;
- pretest and local prerequisite measures;
- assistance provenance and AI-use controls;
- task difficulty matching;
- within-subject, between-subject and sequential/adaptive design tradeoffs;
- immediate, transfer and delayed assessment;
- scoring rubrics and independent/blind review where practical;
- learner burden, accessibility and dropout;
- carryover, practice, demand-characteristic and tutor-model contamination;
- model, prompt, tool and date recording without hidden-backend claims;
- safety, consent, privacy and stop conditions;
- public/synthetic pre-pilot versus real-participant phases;
- minimum sample/analysis planning principles without inventing unsupported numerical power requirements.

Recommend one **minimum viable text-dialogue pilot** and state what it can and cannot establish.

## 6. Evidence requirements

Search across:

- formative assessment and diagnostic teaching;
- intelligent tutoring systems;
- educational measurement and knowledge tracing;
- cognitive load theory;
- worked examples, fading and expertise reversal;
- multiple representations and representational competence;
- conceptual change and misconception repair;
- self-explanation, retrieval practice and transfer;
- tutoring dialogue and Socratic interaction;
- learning progressions and prerequisite structure;
- explanation quality and human-AI explanation;
- open/negotiated learner models and contestability;
- human factors, accessibility, fairness, privacy and autonomy;
- current primary research on LLM tutoring.

Prioritize:

1. systematic reviews and meta-analyses with heterogeneity and population limits stated;
2. peer-reviewed primary research;
3. validated educational instruments and formal standards;
4. current empirical LLM-tutoring studies;
5. conceptual frameworks and engineering analogies, clearly downgraded.

Do not use generic prompt-writing advice, commercial tutor marketing or unsupported “learning styles” claims as strong evidence.

## 7. Evidence calibration

For every load-bearing conclusion, classify support as:

```yaml
support_class:
  - direct_empirical
  - adjacent_empirical
  - systematic_review_or_meta_analysis
  - validated_measurement_or_standard
  - conceptual_framework
  - official_guidance
  - engineering_inference
```

Also record maturity:

```yaml
maturity:
  - replicated_peer_reviewed
  - peer_reviewed_bounded
  - preprint_or_unreplicated
  - qualitative_or_small_sample
  - conceptual_only
```

Explicitly report contradictory findings, null effects, extreme heterogeneity, population/domain limits and evidence gaps.

## 8. Required final-report structure

1. Executive conclusion: what is feasible now, what needs controlled testing, and what remains speculative
2. Operational problem model and terminology
3. Separation of learner-state evidence, local context, explanation action, outcome evidence and preference
4. Evidence review by research tradition
5. Local failure-hypothesis validity and confounder matrix
6. Prerequisite-route and required-mastery representation options
7. Low-burden diagnostic policy candidates
8. Explanation-action selection framework
9. Explanation-failure recovery framework
10. Accessibility without false simplification
11. Outcome and measurement framework
12. Controlled experiment design
13. Minimum viable text-dialogue pilot
14. Safety, fairness, privacy, autonomy and non-manipulation
15. Implications for a later memory system, without designing persistent learner memory now
16. Findings that must remain open questions
17. Adoption, stop, rollback and falsification criteria
18. Portable source table
19. Confidence-calibrated final verdict

## 9. Portable source table

For every source used in a load-bearing claim, include:

- full literal `https://` URL;
- title;
- authors or organization;
- DOI, arXiv or other stable identifier;
- publication/update date;
- access date;
- source type;
- claim/section mapping;
- direct versus analogical support;
- any access or verification limitation.

Opaque conversation-local citation IDs, titles without links, bare DOI strings or domain/path text without a full URL do not satisfy this requirement.

## 10. Final disposition

End with a calibrated disposition such as:

```yaml
final_disposition:
  - evidence_supports_controlled_text_pilot
  - evidence_supports_candidate_framework_but_not_intervention
  - evidence_insufficient_for_adaptive_policy
  - mixed_evidence_requires_narrower_scope
  - custom_disposition
confidence: low | moderate | moderate_to_high | high
```

Do not provide an uncalibrated numerical probability.

## 11. Boundaries

- Do not profile or assess the current user.
- Do not infer stable learning, thinking, personality or clinical types.
- Do not design covert persuasion or manipulation.
- Do not configure GPT Live or another product surface.
- Do not decide cross-session or cross-Agent persistence.
- Do not modify GitHub or any connected service.
- Do not claim this report is an execution source, approved teaching policy or implementation authorization.
- The complete report body must appear inline in the final Deep Research response; any downloadable file is only an auxiliary copy.
