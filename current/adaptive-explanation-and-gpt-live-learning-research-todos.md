# Adaptive Explanation and GPT Live Learning — Research TODOs

> Non-execution-source live research-TODO record. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
record_id: ADAPTIVE-EXPLANATION-GPT-LIVE-LEARNING-TODOS-003
created_by_task: MNEMOSYNE-164
last_status_task: MNEMOSYNE-169
source_raw: raw/chatgpt-discussion-059.md
synthesis_ref: notes/learner-state-and-adaptive-explanation-synthesis-v0.1.md
GPT_Live_fact_check_ref: notes/gpt-live-learning-current-product-fact-check-2026-07-28.md
Stage_A_design_ref: notes/adaptive-explanation-stage-a-research-design-v0.1.md
Stage_A_prompt_ref: notes/research-prompts/PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001.md
status: synthesis_accepted_Stage_A_prompt_ready_not_executed
formal_mainline_selected: Stage_A_research_preparation_only
Deep_Research_prompts_generated: true_one_Stage_A_prompt
Deep_Research_run_started: false
implementation_authorized: false
execution_source: current/human-approved-spec.md
```

## Positioning

This record contains two adjacent but separate research TODOs:

1. adaptive explanation and local prerequisite diagnosis;
2. GPT Live real-time voice learning configuration and validation.

They extend, but do not duplicate, the existing learner-state/mastery, cross-Agent memory and metacognitive-coaching TODOs in `current/todo.md`.

MNEMOSYNE-168 completed the required fresh high-reasoning re-analysis. MNEMOSYNE-169 records `ACCEPT_SYNTHESIS_AS_RESEARCH_DESIGN_BASIS` and prepares one bounded Stage A Deep Research task. No research run or experiment is started.

## TODO 1 — Adaptive explanation for weak, uneven or unknown foundations

- [ ] **Research how an AI dialogue should diagnose local prerequisite state and choose, evaluate and repair an understandable explanation, initially for foundational university mathematics.**

The operational problem is not solved by “assume weak foundations,” “use simple language,” or “explain intuitively.” The Agent must maintain and test competing hypotheses such as:

- missing prerequisite;
- temporary retrieval failure;
- connection gap between known ideas;
- notation or terminology barrier;
- misconception candidate;
- unsupported abstraction jump;
- representation mismatch;
- question or task misunderstanding;
- excessive cognitive load, pacing or environment;
- an incorrect or pedagogically defective Agent explanation;
- insufficient evidence.

Research should examine:

- low-burden diagnostic questions, micro-tasks, teach-back, counterexamples and transfer checks;
- local prerequisite routes and route-specific required mastery;
- multiple valid solution and explanation paths;
- selection among examples, geometry, physical meaning, motivation, analogy, definition, derivation, counterexample and worked problems;
- terminology density, abstraction level, step size, pace and repetition;
- explanation-failure recovery rather than paraphrase-only repetition;
- accessibility without false simplification;
- immediate comprehension, transfer, delayed retention, independence, calibration and learner burden;
- separation of learner-state evidence, local explanation context, explanation action, outcome evidence and presentation preference.

```yaml
TODO_1_status:
  synthesis_disposition: ACCEPT_SYNTHESIS_AS_RESEARCH_DESIGN_BASIS
  Stage_A:
    research_id: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001
    design: notes/adaptive-explanation-stage-a-research-design-v0.1.md
    prompt: notes/research-prompts/PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001.md
    status: prompt_ready_not_executed
    initial_domain:
      - calculus
      - linear_algebra
      - probability_and_statistics
    output:
      - evidence_review
      - candidate_decision_framework
      - controlled_experiment_design
  does_not_assume:
    - stable_global_learner_level
    - self_report_is_diagnostic
    - simpler_wording_is_always_more_understandable
    - failed_explanation_proves_learner_deficit
```

## TODO 2 — GPT Live real-time voice learning Agent configuration and validation

- [ ] **Research how GPT Live or an equivalent real-time voice model should be configured, bounded, supplied with knowledge and evaluated as a long-term learning assistant.**

The 2026-07-28 official snapshot verifies that GPT-Live is a full-duplex continuous voice system and can delegate deeper work to GPT-5.5 at launch. It supports selectable intelligence levels where available and can use web search, memory, text and images in the same chat. This does not establish the backend of a particular session or the effectiveness of GPT Live as a tutor.

Product-specific research should cover:

- current model mapping, selectable intelligence levels and plan/surface differences;
- Project, memory, files and supported knowledge-material access;
- persistent versus session-local instruction behavior;
- voice-session continuity and text/visual handoff;
- interruption, silence, latency, transcription and mathematical-notation errors;
- topic-scope and teaching-mode control;
- privacy, retention and transcript correction;
- configured versus unconfigured Live;
- voice-only versus voice plus text/visual support;
- learning outcomes, burden, accessibility and failure recovery.

```yaml
TODO_2_status:
  relation_to_Stage_A: dependent_but_separate_product_surface
  current_product_claim_status: official_snapshot_verified_2026_07_28_requires_future_recheck
  product_fact_check: notes/gpt-live-learning-current-product-fact-check-2026-07-28.md
  prompt_generated: false
  required_before_product_specific_prompt:
    - completed_and_reviewed_Stage_A_report_or_explicit_user_override
    - current_official_GPT_Live_fact_recheck
    - separate_product_specific_prompt_generation_task
    - decision_whether_text_policy_should_be_tested_before_voice_research
```

## Research sequence

```yaml
research_sequence:
  Stage_A:
    id: GENERAL_ADAPTIVE_EXPLANATION_AND_LOCAL_PREREQUISITE_DIAGNOSIS
    current_state: prompt_ready_not_executed
  Stage_B:
    id: CONTROLLED_TEXT_DIALOGUE_EXPERIMENT
    prerequisite: Stage_A_report_review_and_user_acceptance
  Stage_C:
    id: GPT_LIVE_REALTIME_VOICE_LEARNING_SURFACE
    prerequisite: general_adaptive_policy_candidate_and_fresh_product_fact_check
  Stage_D:
    id: LONGITUDINAL_MEMORY_AND_CROSS_AGENT_INTEGRATION
    prerequisite: behavioral_evidence_and_separate_user_decision
  no_automatic_start: true
```

## Relationship to Meta-Agent

```yaml
Meta_Agent:
  Stage_A_required_before_core_v0_1_build: false
  reason: learning_specific_methodology_can_be_added_later_through_versioned_upgrade
  readiness_assessment: notes/meta-agent-upgradeable-build-start-readiness-assessment-v0.1.md
```

The adaptive-explanation research may run in parallel with Meta-Agent launch preparation. It should not delay authority, requirements, workspace, versioning, rollback or first-target upgradeability work.

## Boundaries

- This record is not an assessment of the user's mathematics level.
- It does not establish a global learner profile, stable learning style or psychological diagnosis.
- One Deep Research prompt is prepared, but no research is executed or accepted in advance.
- It does not approve a GPT Live configuration, knowledge base, persistent memory or shared profile.
- It does not assert that a visible GPT Live setting attests the served backend.
- It does not select a target project or authorize workspace, material ingestion, target write or operational build.
- It does not modify the four accepted research reports or their evidence roles.
