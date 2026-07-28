# Learner State and Adaptive Explanation Synthesis v0.1

> Non-execution-source high-reasoning synthesis. This file re-analyses `RAW-0059` against the accepted learner/cognitive-coaching research and existing learning TODOs. It does not assess the user's mathematics level, create a learner profile, approve a teaching policy, generate a Deep Research prompt, configure GPT Live, or authorize implementation.

```yaml
synthesis_id: LEARNER-STATE-ADAPTIVE-EXPLANATION-SYNTHESIS-001
created_by_task: MNEMOSYNE-168
source_raw: raw/chatgpt-discussion-059.md
accepted_research_cycle: RC-2026Q3-target-memory-governance-and-learning
accepted_learner_report: PRO-DR-LEARNER-COGNITIVE-COACHING-001
status: candidate_ready_for_user_review
execution_source: current/human-approved-spec.md
execution_source_modified: false
Deep_Research_prompts_generated: false
GPT_Live_configuration_approved: false
user_profile_created: false
```

## 1. Restated user intent

The user's concern is not adequately represented as:

> “The learner has weak foundations, so use simpler language.”

That instruction is too broad to determine what a useful explanation should do for a specific question. The user is reporting a recurring failure of high-capability ordinary dialogue models:

1. the model does not know which prerequisites matter for the current concept;
2. it cannot reliably tell which of those prerequisites are present, missing, temporarily inaccessible or misunderstood;
3. it treats “easy to understand” as a vague style preference rather than a pedagogical decision problem;
4. it often changes wording without locating why the previous explanation failed;
5. it can mistake smooth conversation or immediate agreement for real understanding;
6. it lacks a validated method for selecting an explanation entry point, representation, step size and recovery strategy.

The user also intends to use GPT Live heavily for future learning. That introduces a separate product-surface problem: how a real-time voice system should be instructed, scoped, supplied with materials and learner-state evidence, coordinated with text/visual media, and evaluated. The GPT Live question depends on the general adaptive-explanation problem but should not be merged into it.

## 2. Core synthesis: this is a closed-loop pedagogical control problem

The central problem is not static simplification and not a global learner-level classification. It is a repeated local loop:

```text
identify the current learning target and question
  -> identify plausible prerequisite routes
  -> estimate the local prerequisite state with uncertainty
  -> choose a provisional explanation action
  -> observe the learner's response and task evidence
  -> diagnose why the explanation or understanding failed
  -> adapt one or more explanation dimensions
  -> test understanding, transfer and later retention
  -> update only the evidence-supported local state
```

This loop should treat the Agent's own explanation as a possible failure source. A poor response must not automatically be interpreted as a learner deficit.

## 3. Objects that must remain separate

### 3.1 Learner-state evidence

Longer-lived, domain- and time-scoped evidence about knowledge or skill:

- independent task performance;
- explanations and error diagnosis;
- produced artifacts with assistance provenance;
- unfamiliar transfer;
- delayed retest;
- repeated cross-context performance;
- user/teacher confirmation.

Dialogue fluency and broad self-description are weak evidence by themselves.

### 3.2 Local explanation context

Short-lived state for the current concept and question:

- target concept and current question;
- candidate prerequisite routes;
- notation and terminology in use;
- current modality and environmental constraints;
- the learner's current mental-model fragments as actually evidenced;
- assistance already given in this session;
- current uncertainty and competing explanations of the difficulty.

### 3.3 Explanation action

The teaching move selected by the Agent:

- entry representation;
- abstraction level;
- step size;
- sequence;
- terminology density;
- example or counterexample choice;
- prerequisite bridge;
- question/probe type;
- pace and turn length;
- text, voice, diagram, formula or worked-problem modality.

### 3.4 Explanation-outcome evidence

Evidence about whether the selected explanation helped:

- learner paraphrase or teach-back;
- correct application to a near example;
- transfer to an unfamiliar example;
- error type after the explanation;
- delayed retention;
- learner burden, confusion and autonomy;
- whether the apparent improvement depended on hints or AI completion.

### 3.5 Presentation preference

A user's stated preference—such as concise replies, more intuition, more geometry or fewer formulas—can guide presentation, but it must not be treated as proof of capability or as a fixed “learning style.” Preference, proficiency and evidence-supported need are distinct.

## 4. Why “weak foundations” is not a sufficient learner model

A broad self-description should be treated only as a prior that encourages caution and low-burden checking. It does not prove that a specific prerequisite is absent.

For a particular question, the Agent may need to distinguish at least:

```yaml
local_state_hypotheses:
  prerequisite_missing:
  retrieval_failure_candidate:
  connection_gap_candidate:
  notation_or_terminology_barrier:
  misconception_candidate:
  abstraction_step_too_large:
  representation_mismatch:
  question_or_task_misunderstood:
  explanation_defect_candidate:
  cognitive_load_or_pacing_problem:
  motivation_attention_or_environment_confounder:
  insufficient_evidence:
```

These are hypotheses, not labels. Multiple hypotheses may coexist; each requires evidence, scope, recency and a route to revision.

## 5. Candidate local prerequisite representation

This is an analysis aid, not an approved schema:

```yaml
local_prerequisite_state:
  learning_target:
  current_question:
  prerequisite_route_candidates:
    - route_id:
      rationale:
      prerequisite_nodes:
        - concept_or_skill:
          required_level_for_this_route:
          evidence_state: observed_known | observed_gap | uncertain | misconception_candidate | retrieval_failure_candidate | connection_gap_candidate | notation_barrier_candidate
          evidence_refs: []
          assistance_provenance:
          recency:
          confidence: qualitative_only
  selected_explanation_route:
  competing_failure_hypotheses: []
  user_or_teacher_corrections: []
  expiry_or_recheck_trigger:
```

Important constraints:

- there may be several valid prerequisite routes to the same concept;
- “required level” is target- and explanation-route-specific;
- a learner can know component ideas but not their relation;
- an Agent must be allowed to record `insufficient_evidence` rather than guess;
- the structure should remain small enough for ordinary teaching dialogue.

## 6. Candidate explanation-decision dimensions

An adaptive explanation policy should select among dimensions rather than choose a single permanent style.

### Entry point

- concrete instance;
- visual/geometric structure;
- physical or engineering meaning;
- historical/problem motivation;
- familiar analogy with an explicit limit;
- formal definition;
- counterexample;
- worked problem;
- comparison with a nearby known concept.

### Structure

- prerequisite bridge before the target;
- target-first overview followed by prerequisites on demand;
- progressive formalization;
- worked example followed by rule extraction;
- rule followed by contrasting examples;
- error-first repair.

### Granularity and load

- conceptual step size;
- number of new terms per turn;
- symbolic density;
- number of simultaneously active dependencies;
- turn length;
- amount of repetition;
- modality switches.

### Interaction

- direct explanation;
- one low-burden diagnostic question;
- teach-back;
- micro-task;
- forced choice between two interpretations;
- counterexample check;
- transfer check;
- learner-controlled request for more or less detail.

No single ordering or representation should be assumed to work for all learners or all topics.

## 7. Low-burden diagnosis without turning teaching into an exam

The Agent should not interrogate the learner before every explanation. A candidate policy is:

1. use existing evidence when it is recent, scoped and relevant;
2. offer a provisional explanation when the risk of a wrong entry point is low;
3. ask at most one focused diagnostic question when two materially different explanation routes are plausible;
4. explain why the question is being asked;
5. allow the learner to request a direct explanation instead;
6. use micro-evidence embedded in the teaching process rather than a full assessment;
7. update persistent learner state only when the evidence warrants it.

Useful probes may include:

- “Which part is unfamiliar: the symbol, the operation or why the operation is valid?”
- asking for a one-sentence paraphrase;
- asking the learner to choose between two conceptual interpretations;
- one minimal example that isolates a prerequisite;
- asking the learner to identify the first step that no longer follows;
- a near-transfer or counterexample check after explanation.

The probe must be chosen to discriminate between competing failure hypotheses; arbitrary questions add burden without improving the model.

## 8. Explanation-failure recovery

When the learner reports that an explanation is unclear, repeating the same explanation with more words is not a sufficient repair strategy.

A candidate recovery loop is:

```text
locate the earliest unclear or unjustified step
  -> classify the leading failure hypotheses
  -> acknowledge uncertainty and the possibility of an explanation defect
  -> change one important explanation dimension
  -> use a minimal check
  -> either continue, bridge a prerequisite, switch modality or stop and record unresolved uncertainty
```

Possible repairs:

- replace a verbal abstraction with a concrete example;
- replace a misleading analogy with a direct structural explanation;
- introduce the missing relation between already-known components;
- define notation before continuing;
- reduce the abstraction jump;
- show a counterexample to expose a misconception;
- switch from voice to text or a diagram for formula-heavy material;
- ask the learner to state the exact point where the reasoning stops following;
- correct the Agent's own earlier error.

## 9. “Understandable” must not mean falsely simple

An explanation can be accessible while remaining honest about rigor.

Candidate requirements:

- label analogies as analogies and state where they stop matching;
- do not remove a necessary prerequisite without replacing it with an explicit local bridge;
- distinguish intuitive motivation from formal definition;
- avoid introducing false rules that later have to be unlearned;
- allow progressive formalization rather than demanding full formalism immediately;
- preserve the learner's autonomy to request more rigor, examples or brevity;
- avoid patronizing language and stable “weak learner” labels.

## 10. Evaluation model

Immediate agreement is not sufficient evidence. A research or pilot evaluation should separate:

```yaml
outcomes:
  immediate_comprehension:
  near_transfer:
  unfamiliar_transfer:
  delayed_retention:
  independent_performance:
  calibration_between_confidence_and_performance:
  error_reduction:
  learner_burden_and_cognitive_load:
  autonomy_and_overreliance:
  explanation_repair_success:
```

A useful controlled comparison would compare the same model and content under:

- generic “explain simply” instruction;
- fixed intuitive-first policy;
- adaptive local-diagnosis policy;
- adaptive policy with explicit explanation-failure recovery.

The comparison should hold the learning objective, material and assessment constant where practical.

## 11. Relationship to existing TODOs

### Learner-state / mastery-evidence TODO

The existing learner-state TODO asks what the learner knows and what evidence supports that conclusion. The adaptive-explanation problem asks what teaching action should follow for the current question. Learner state is an input, not the whole decision rule.

### Problem-solving / metacognitive coaching TODO

Cognitive coaching asks how to observe and train task strategies over time. Adaptive explanation is more local: how to make the current concept understandable and repair a failed explanation. Task-strategy evidence can inform explanation, but the Agent must not infer a stable thinking type.

### Cross-Agent reuse TODO

Only scoped, provenance-bearing and user-authorized learner evidence may later become a shared projection. Session-local confusion hypotheses and explanation traces should remain local by default.

### GPT Live learning TODO

GPT Live is a delivery and interaction surface for the adaptive loop. It does not replace the underlying learner-state, explanation-decision and evaluation model.

## 12. Recommended staged research programme

This synthesis does not generate the actual Deep Research prompts. It recommends the dependency order.

### Stage A — General adaptive explanation and local prerequisite diagnosis

Research questions:

1. What evidence can efficiently distinguish missing prerequisite, retrieval failure, connection gap, notation barrier, misconception and explanation defect?
2. How should prerequisite requirements be scoped to a chosen explanation route?
3. Which low-burden probes maximize diagnostic value without making tutoring feel like constant testing?
4. How should an Agent select representation, sequencing, step size and progressive formalization?
5. What explanation-repair strategies work after an initial explanation fails?
6. How should effectiveness be measured beyond immediate conversational fluency?

Primary domains for evidence should include learning science, formative assessment, intelligent tutoring, cognitive load, worked examples and fading, multiple representations, conceptual change, self-explanation, tutoring dialogue and human-AI explanation.

### Stage B — Controlled text-dialogue experiments

Use synthetic/public material and bounded university-foundation topics. Compare fixed and adaptive policies, record assistance provenance, and measure transfer, delayed retention and burden. No persistent user profile is required for the first experiment.

### Stage C — GPT Live / real-time voice learning surface

Only after the general adaptive policy is defined, research:

- real-time turn-taking and interruption;
- speech-recognition and mathematical-notation errors;
- pacing and silence;
- when to move formulas or diagrams into text/visual form;
- how chat memory, manual file input and project context actually behave;
- how reasoning-level selection affects teaching flow;
- privacy and retention of voice/transcript evidence;
- configured versus unconfigured voice tutoring.

### Stage D — Longitudinal memory integration

Only after controlled evidence exists, decide which observations, inferences and confirmations should persist across sessions, which may be shared across Agents, and how they expire or are contested.

## 13. Candidate research-design decision points

Before generating research prompts, user review should decide:

```yaml
research_design_decisions:
  adaptive_explanation_scope:
    options:
      - foundational_university_mathematics_first
      - broader_science_and_engineering
      - cross_domain_general_framework
  first_output:
    options:
      - evidence_review_only
      - evidence_review_plus_controlled_experiment_design
      - controlled_text_pilot_specification
  GPT_Live_route:
    options:
      - separate_product_specific_research_after_Stage_A
      - include_only_a_small_voice_implications_section_in_Stage_A
      - defer_until_text_policy_is_tested
  persistence_scope:
    options:
      - session_local_only_for_first_pilot
      - limited_cross_session_evidence_ledger
      - defer_memory_design_until_behavioral_results
```

The maintainer recommendation is:

```yaml
recommended_candidate_sequence:
  Stage_A_scope: foundational_university_mathematics_first_with_transferable_principles
  Stage_A_output: evidence_review_plus_controlled_experiment_design
  GPT_Live_route: separate_product_specific_research_after_Stage_A
  first_pilot_persistence: session_local_plus_explicitly_scoped_evidence_only
```

This recommendation is not adopted policy.

## 14. What this synthesis resolves

```yaml
resolved_for_research_design:
  - weak_foundations_is_not_an_operational_explanation_policy
  - global_learner_level_is_not_required_for_local_adaptation
  - learner_state_explanation_action_and_outcome_evidence_must_be_separate
  - explanation_failure_can_be_caused_by_the_Agent
  - GPT_Live_is_a_dependent_but_separate_product_surface
  - Deep_Research_should_be_staged_before_longitudinal_memory_or_product_configuration
```

## 15. What remains open

```yaml
open_questions:
  - which_failure_hypotheses_can_be_distinguished_reliably_with_low_burden_dialogue
  - how_to_measure_explanation_entry_point_quality
  - how_much_prerequisite_diagnosis_is_worth_the_user_burden
  - which_representation_selection_rules_generalize_across_topics
  - how_to_detect_and_repair_Agent_explanation_defects
  - how_voice_transcription_and_turn_taking_change_diagnostic_validity
  - which_evidence_is_safe_and_useful_to_persist_or_share
  - whether_adaptation_improves_delayed_transfer_and_independence
```

## 16. Boundaries

- This synthesis is not execution source.
- It does not determine the user's actual mathematics foundation.
- It does not create a stable learner level, learning style, thinking style or psychological profile.
- It does not approve a learner-state schema, explanation policy or coaching intervention.
- It does not generate a Deep Research task or start research.
- It does not configure GPT Live, a Project, a knowledge base or persistent memory.
- It does not authorize target-project work, cross-Agent sharing or automatic writeback.
- A later prompt-generation task requires explicit user disposition on this synthesis and fresh task-local authorization.
