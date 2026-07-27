# Adaptive Explanation and GPT Live Learning — Research TODOs

> Non-execution-source live research-TODO record. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
record_id: ADAPTIVE-EXPLANATION-GPT-LIVE-LEARNING-TODOS-001
created_by_task: MNEMOSYNE-164
source_raw: raw/chatgpt-discussion-059.md
status: captured_waiting_for_Pro_quota_and_fresh_Pro_reanalysis
formal_mainline_selected: false
Deep_Research_prompts_generated: false
implementation_authorized: false
execution_source: current/human-approved-spec.md
```

## Positioning

This record adds two provisional research TODOs adjacent to the existing entries in `current/todo.md#user-requested-product-design-research-todos`:

1. learner-state, prerequisites and mastery evidence;
2. cross-Agent reusable memory;
3. problem-solving strategy and metacognitive coaching.

It does not replace or silently expand those entries. Before any Deep Research prompt is generated, a fresh Pro conversation must re-read `RAW-0059`, restate the user intent, check overlap and dependencies, verify current GPT Live product facts, and obtain any needed user clarification.

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
- the explanation is too verbose, too compressed, too formal, too informal or poorly sequenced.

Research should examine at least:

- what minimal questions, micro-tasks, teach-back, counterexamples or transfer checks can estimate relevant prerequisites without turning every explanation into an exam;
- how to represent `known`, `unknown`, `uncertain`, `misconception_candidate`, `retrieval_failure_candidate` and `explanation_failure_candidate` separately;
- how to choose among concrete examples, visual/geometric interpretation, physical meaning, historical motivation, formal definition, symbolic derivation, analogy, counterexample and worked problem;
- how to control terminology density, abstraction level, step size, pacing, cognitive load and repetition;
- how to recover after the learner says an explanation is unclear, instead of merely repeating it with more words;
- how to distinguish immediate conversational fluency from real understanding, retention and transfer;
- how to preserve learner autonomy and avoid patronizing, oversimplifying or permanently labeling the learner as “weak foundation”;
- how effectiveness should be tested across topics, learners, dialogue modes and delayed outcomes.

```yaml
TODO_1_dependency:
  extends:
    - learning_coaching_Agent_learner_state_prerequisite_and_mastery_evidence
    - problem_solving_strategy_metacognitive_pattern_and_adaptive_methodology_coaching
  does_not_assume:
    - a_stable_global_learner_level
    - that_self_report_alone_is_diagnostic
    - that_simpler_wording_is_always_more_understandable
  required_before_research_prompt:
    - fresh_Pro_reanalysis_of_RAW_0059
    - scope_and_similarity_review
    - staged_research_design
```

## TODO 2 — GPT Live real-time voice learning Agent configuration and validation

- [ ] **Research how GPT Live or an equivalent real-time voice model should be configured, bounded, supplied with knowledge and evaluated as a long-term learning assistant.**

The current product/model statement is operator-reported and time-sensitive. Formal research must first verify current official facts about:

- product name and availability;
- actual supported model and documented capability claims;
- context, memory, Project, file, knowledge-base and app access;
- instructions or persistent behavior configuration;
- voice-session continuity and handoff to text conversations;
- usage limits, platform differences and privacy behavior.

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
  current_product_claim_status: operator_reported_time_sensitive_requires_official_reverification
  required_before_research_prompt:
    - fresh_Pro_reanalysis_of_RAW_0059
    - current_official_GPT_Live_fact_check
    - dependency_and_batch_order_decision
    - decision_whether_product_specific_and_general_voice_tutoring_research_should_be_separate
```

## Research sequencing gate

```yaml
research_sequence:
  current_state: wait_for_Pro_quota_recovery
  next_required_operation: fresh_Pro_conversation_reanalysis_not_Deep_Research
  Pro_reanalysis_must:
    - read_raw_chatgpt_discussion_059
    - preserve_the_user_distinction_between_general_explanation_and_GPT_Live
    - identify_missing_questions_without_overwriting_the_raw_input
    - compare_with_existing_three_learning_related_TODOs
    - verify_current_product_facts_when_relevant
    - recommend_dependency_aware_research_batches
  only_after_reanalysis:
    - generate_research_questions_or_prompt_candidates
    - decide_whether_Deep_Research_Fable_5_Opus_5_or_controlled_trials_are_needed
  no_automatic_start: true
```

## Boundaries

- This record is not an assessment of the user's mathematics level.
- It does not establish a global learner profile or a stable learning style.
- It does not approve psychological, cognitive or clinical diagnosis.
- It does not approve a GPT Live configuration, knowledge base, persistent memory, shared profile or product implementation.
- It does not assert that the user-reported GPT Live model label is the exact served backend.
- It does not generate or authorize Deep Research tasks while Pro quota is unavailable.
- It does not modify the four existing isolated Pro Deep Research tasks.
- It does not select a target project or authorize target workspace, material ingestion, target write or operational build.
