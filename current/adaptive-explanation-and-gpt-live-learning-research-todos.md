# Adaptive Explanation and GPT Live Learning — Research TODOs

> Non-execution-source live research-TODO record. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
record_id: ADAPTIVE-EXPLANATION-GPT-LIVE-LEARNING-TODOS-002
created_by_task: MNEMOSYNE-164
last_status_task: MNEMOSYNE-168
source_raw: raw/chatgpt-discussion-059.md
synthesis_ref: notes/learner-state-and-adaptive-explanation-synthesis-v0.1.md
GPT_Live_fact_check_ref: notes/gpt-live-learning-current-product-fact-check-2026-07-28.md
status: fresh_Pro_reanalysis_completed_pending_user_disposition
formal_mainline_selected: learner_state_and_adaptive_explanation_synthesis_only
Deep_Research_prompts_generated: false
implementation_authorized: false
execution_source: current/human-approved-spec.md
```

## Positioning

This record contains two provisional research TODOs adjacent to the existing entries in `current/todo.md#user-requested-product-design-research-todos`:

1. learner-state, prerequisites and mastery evidence;
2. cross-Agent reusable memory;
3. problem-solving strategy and metacognitive coaching.

MNEMOSYNE-168 completed the required fresh high-reasoning re-analysis of `RAW-0059`, compared the problem with those three TODOs, used the accepted learner/cognitive-coaching research, and verified current GPT Live product facts from official OpenAI sources. It did not generate a Deep Research prompt or start an experiment.

The main synthesis is:

> Adaptive explanation is a local closed-loop pedagogical decision problem. Learner-state evidence is only one input. GPT Live is a dependent but separate voice/product surface.

## TODO 1 — Adaptive explanation for weak, uneven or unknown foundations

- [ ] **Research how an AI dialogue should diagnose the local prerequisite state and choose an understandable explanation entry point, especially for foundational university mathematics such as calculus, linear algebra, probability and statistics.**

The problem is not solved by a generic instruction such as “assume weak foundations,” “use simple language,” or “explain intuitively.” The Agent must distinguish, with uncertainty, among possibilities such as:

- the learner lacks a prerequisite concept;
- the learner once knew it but cannot currently retrieve it;
- the learner knows the component ideas but not their connection;
- the current notation or terminology is the blocker;
- the explanation makes an unsupported abstraction jump;
- an analogy or geometric picture conflicts with the formal concept;
- the question itself was misunderstood;
- the learner can follow an example but cannot transfer it;
- the learner's self-description is broader or weaker than their actual local competence;
- the explanation is too verbose, too compressed, too formal, too informal or poorly sequenced;
- the Agent's own explanation is incorrect or pedagogically defective;
- motivation, attention, environment or modality confounds the observed response.

Research should examine at least:

- what minimal questions, micro-tasks, teach-back, counterexamples or transfer checks can estimate relevant prerequisites without turning every explanation into an exam;
- how to represent `known`, `unknown`, `uncertain`, `misconception_candidate`, `retrieval_failure_candidate`, `connection_gap_candidate`, `notation_barrier_candidate` and `explanation_failure_candidate` separately;
- how to choose among concrete examples, visual/geometric interpretation, physical meaning, historical motivation, formal definition, symbolic derivation, analogy, counterexample and worked problem;
- how to control terminology density, abstraction level, step size, pacing, cognitive load and repetition;
- how to recover after the learner says an explanation is unclear, instead of merely repeating it with more words;
- how to distinguish immediate conversational fluency from real understanding, retention and transfer;
- how to preserve learner autonomy and avoid patronizing, oversimplifying or permanently labeling the learner as “weak foundation”;
- how effectiveness should be tested across topics, learners, dialogue modes and delayed outcomes;
- how to separate learner-state evidence, local explanation context, explanation action and explanation-outcome evidence.

```yaml
TODO_1_dependency:
  extends:
    - learning_coaching_Agent_learner_state_prerequisite_and_mastery_evidence
    - problem_solving_strategy_metacognitive_pattern_and_adaptive_methodology_coaching
  does_not_assume:
    - a_stable_global_learner_level
    - that_self_report_alone_is_diagnostic
    - that_simpler_wording_is_always_more_understandable
    - that_a_failed_explanation_proves_a_learner_deficit
  reanalysis_gate:
    fresh_Pro_reanalysis_of_RAW_0059: complete
    scope_and_similarity_review: complete
    accepted_learner_research_synthesis: complete
    staged_research_design: candidate_ready_for_user_review
  required_before_research_prompt:
    - explicit_user_disposition_on_LEARNER_STATE_ADAPTIVE_EXPLANATION_SYNTHESIS_001
    - fresh_bounded_prompt_generation_task
```

## TODO 2 — GPT Live real-time voice learning Agent configuration and validation

- [ ] **Research how GPT Live or an equivalent real-time voice model should be configured, bounded, supplied with knowledge and evaluated as a long-term learning assistant.**

The official 2026-07-28 product snapshot now verifies that GPT-Live is a full-duplex continuous voice system and can delegate deeper work to GPT-5.5 at launch. The product supports selectable intelligence levels where available and can use web search, memory, text and images in the same chat. This does not establish the exact backend of a particular session or the effectiveness of GPT Live as a tutor.

Product-specific research must continue to track:

- product name and availability;
- current background frontier-model mapping and selectable intelligence levels;
- context, memory, Project, file and supported knowledge-material access;
- instructions or persistent behavior configuration;
- voice-session continuity and handoff to text conversations;
- usage limits, platform differences and privacy behavior;
- changes to connected-app, plugin, video and screen-sharing support.

The substantive research should then cover:

- behavioral mode: Socratic questioning, direct explanation, guided practice, review, oral examination, error diagnosis and reflection;
- topic scope: how to define course, module, current lesson and local question boundaries without uncontrolled topic drift;
- knowledge base: what should be canonical course material, reference notes, learner-state evidence, worked examples and current-session scratch state;
- learner-level estimation: how to infer only the prerequisites relevant to the current topic and how to express uncertainty;
- explanation selection: how real-time voice should choose entry point, pacing and representation based on the adaptive-explanation research;
- voice-specific interaction: interruption, barge-in, pauses, latency, transcription errors, misheard mathematical notation, formula presentation, turn length and confirmation;
- multimodal cooperation: when to switch from voice to text, diagrams, formulas, exercises, files or persistent memory;
- continuity: how sessions record progress, unresolved confusion, evidence and next review without treating the voice transcript as unquestioned truth;
- safety and privacy: consent, sensitive learner information, deletion, retention and cross-Agent reuse boundaries;
- evaluation: comprehension, delayed retention, transfer, calibration, independent performance, conversational burden, accessibility and failure recovery;
- controlled comparison: configured versus unconfigured GPT Live, voice versus text, and different explanation policies under the same learning objectives.

```yaml
TODO_2_dependency:
  depends_on_or_should_be_coordinated_with:
    - TODO_1_adaptive_explanation
    - learning_coaching_Agent_learner_state_prerequisite_and_mastery_evidence
    - problem_solving_strategy_metacognitive_pattern_and_adaptive_methodology_coaching
    - cross_Agent_reusable_learner_user_environment_and_domain_memory
  current_product_claim_status: official_snapshot_verified_2026_07_28_requires_future_recheck
  product_fact_check: notes/gpt-live-learning-current-product-fact-check-2026-07-28.md
  required_before_product_specific_research_prompt:
    - user_accepts_or_modifies_general_adaptive_explanation_synthesis
    - current_official_GPT_Live_fact_recheck
    - separate_product_specific_prompt_generation_task
    - decision_whether_text_policy_should_be_tested_before_voice_research
```

## Research sequencing gate

```yaml
research_sequence:
  current_state: fresh_reanalysis_complete_pending_user_disposition
  completed:
    - read_raw_chatgpt_discussion_059
    - preserve_user_distinction_between_general_explanation_and_GPT_Live
    - identify_missing_questions_without_overwriting_raw_input
    - compare_with_existing_three_learning_related_TODOs
    - use_accepted_learner_cognitive_coaching_research
    - verify_current_official_GPT_Live_product_facts
    - recommend_dependency_aware_research_stages
  recommended_stages:
    - Stage_A_general_adaptive_explanation_and_local_prerequisite_diagnosis
    - Stage_B_controlled_text_dialogue_experiment
    - Stage_C_GPT_Live_realtime_voice_learning_surface
    - Stage_D_longitudinal_memory_and_cross_Agent_integration
  prohibited_until_user_disposition:
    - generate_Deep_Research_prompts
    - start_controlled_experiment
    - configure_GPT_Live
    - create_persistent_learner_profile
  no_automatic_start: true
```

## Boundaries

- This record is not an assessment of the user's mathematics level.
- It does not establish a global learner profile or a stable learning style.
- It does not approve psychological, cognitive or clinical diagnosis.
- It does not approve a GPT Live configuration, knowledge base, persistent memory, shared profile or product implementation.
- It does not assert that a user-visible GPT Live setting attests the exact served backend.
- It does not generate or authorize Deep Research tasks.
- It does not modify the four accepted research reports or their evidence roles.
- It does not select a target project or authorize target workspace, material ingestion, target write or operational build.
