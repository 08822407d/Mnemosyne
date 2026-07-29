# User Operation / Next-Step / Capability / Research / Clarification / Intent Guard — v0.2 Amendment Record

> Non-execution-source amendment record for the user-approved behavior guard. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
amendment_id: MNEMOSYNE-USER-OPERATION-NEXT-STEP-CAPABILITY-INTENT-002
implementation_task: MNEMOSYNE-178
amends_guard: current/user-operation-next-step-capability-and-intent-guard.md
previous_guard_version: v0.1
new_guard_version: v0.2
initial_adoption_PR: 229
initial_merge_commit: 1b563d13dbd7db7ce1456ee8bdc9ab1927b942ab
amendment_status: pending_MNEMOSYNE_178_merge
execution_source: current/human-approved-spec.md
execution_source_modified: false
```

## 1. Explicit user wording

The user added two requirements to the previously adopted behavior guard:

1. when a frontier model plans work and presents the next step, it must also consider whether Pro Deep Research is advisable; when it is, the Agent should automatically provide the research deliverable needed to proceed;
2. when human clarification, confirmation, or explanation is needed, the frontier model must provide not only the questions but their context and meaning, so the user can remember what is being decided and a next-tier model can conduct the interactive clarification without losing quality.

The user explained that human short-term memory and attention are more limited than an LLM context window, so a bare question or unexplained option is often not usable after a long multi-step project.

The intended quota pattern is:

```text
frontier model reconstructs the problem and prepares the question/decision structure
  -> next-tier model handles multi-turn clarification and explanations
  -> frontier model returns only when a new high-impact judgment or final adjudication is needed
```

## 2. Proposed restated intent

```yaml
intent_analysis:
  explicit_constraints_and_decisions:
    - assess_Deep_Research_need_for_each_meaningful_next_stage
    - avoid_an_extra_frontier_turn_merely_to_generate_the_research_task
    - include_background_and_meaning_for_human_questions
    - make_the_question_set_usable_by_a_next_tier_interviewer
    - preserve_human_correction_and_context

  likely_underlying_need:
    - reduce_unnecessary_Pro_quota_consumption_without_losing_problem_reconstruction_quality
    - prevent_context_loss_between_frontier_planning_and_lower_tier_interaction
    - compensate_for_human_memory_and_attention_limits
    - route_external_evidence_gaps_to_research_and_owner_decisions_to_the_user

  competing_interpretation:
    - literal_automatic_report_generation_could_mean_execute_research_without_user_action

  proposed_restated_intent:
    - automatically_assess_research_need_and_generate_a_ready_to_run_task_and_report_contract_when_recommended
    - do_not_execute_quota_consuming_research_or_fabricate_a_report_without_a_real_run
    - automatically_prepare_a_context_rich_clarification_handoff_when_next_tier_interaction_is_safe

  confidence: high_for_quota_and_handoff_goal_moderate_for_literal_automatic_report_wording
  user_correction_or_confirmation_needed: only_before_changing_research_execution_or_quota_authority
```

The amendment implements the conservative interpretation. It does not infer authority to spend quota or start external research automatically.

## 3. New research-assessment contract

Every meaningful next-stage plan now includes independent decisions about:

- model reasoning capability;
- Pro Deep Research;
- independent Fable-class/other-provider research;
- next-tier execution;
- mechanical verification;
- human owner decisions.

Deep Research is classified as:

```yaml
- NOT_NEEDED
- OPTIONAL_VALUE
- RECOMMENDED
- REQUIRED_BEFORE_HIGH_IMPACT_DECISION
- DEFER_UNTIL_UPSTREAM_DEPENDENCY
- UNAVAILABLE_OR_QUOTA_BLOCKED
```

Parallel frontier research is classified as:

```yaml
- NOT_NEEDED
- OPTIONAL_INDEPENDENT_CHALLENGE
- RECOMMENDED_HETEROGENEOUS_REVIEW
- REQUIRED_FOR_HIGH_IMPACT_ACCEPTANCE
- DEFER_UNTIL_PRIMARY_RESULT
- UNAVAILABLE
```

When research is recommended/required and sufficiently frozen, the planner delivers the full task and report contract in the same response or authorized repository task. It must not fabricate a report or silently spend quota.

## 4. New clarification-handoff contract

The frontier planner prepares:

- a context synopsis;
- current known state;
- decisions already fixed;
- matters not being reopened;
- user wording or safe reference;
- candidate restatement and alternatives;
- uncertainty routing;
- question order and dependencies;
- question-by-question background, meaning, consequences, options, recommendation, deferral/default, and escalation;
- a next-tier interviewer contract;
- a cumulative answer ledger;
- a structured clarification-result package.

The next-tier interviewer may explain and capture. It may not invent or silently decide owner, authority, privacy, architecture, trust-boundary, product-goal, or execution-source matters.

## 5. Research assessment for the amendment itself

The amendment distinguishes explicit user authority from empirical validation.

```yaml
baseline_behavior_amendment:
  external_research_required: false
  reason: the_user_can_authorize_a_workflow_and_communication_rule_without_external_evidence

Pro_Deep_Research:
  status: RECOMMENDED
  research_id: PRO-DR-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001
  task_ref: notes/research-prompts/PRO-DR-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001.md
  role:
    - human_memory_and_decision_context_evidence
    - requirements_elicitation_and_clarification_design
    - frontier_to_next_tier_handoff_evidence
    - research_trigger_and_validation_design
  blocking_for_v0_2_merge: false

Fable_independent_challenge:
  status: OPTIONAL_INDEPENDENT_CHALLENGE
  task_id: FABLE5-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001
  task_ref: notes/research-prompts/FABLE5-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001.md
  role:
    - challenge_delegation_benefit
    - attack_planner_framing_and_packet_bloat
    - compare_alternative_architectures
    - challenge_automatic_research_task_generation
  blocking_for_v0_2_merge: false
```

Both task files are generated in the same amendment task, satisfying the user's request not to spend another frontier turn merely asking for prompts.

## 6. Propagation and validation boundary

The v0.2 guard becomes active for Mnemosyne conversations after merge and guidance refresh. It remains a candidate for target-project designs.

Before making the complete workflow a mandatory default in Meta-Agent, a long-lived business Agent, or another target project's execution source, prefer:

1. Pro Deep Research review;
2. optional independent Fable-class challenge when the impact justifies it;
3. synthetic controlled validation of packet/interviewer fidelity;
4. explicit target-owner decision.

## 7. Files affected by MNEMOSYNE-178

```yaml
modified:
  - current/user-operation-next-step-capability-and-intent-guard.md
  - commands/load-mnemosyne-guidance.md
  - current/model-capability-aware-work-planning-open-question.md
  - notes/user-operation-next-step-capability-intent-guard-adoption-record.md
  - README.md

created:
  - notes/user-operation-next-step-capability-intent-guard-v0.2-amendment-record.md
  - notes/templates/frontier-planned-clarification-package-v0.1.md
  - current/frontier-planning-clarification-handoff-research-status.md
  - notes/research-prompts/PRO-DR-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001.md
  - notes/research-prompts/FABLE5-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001.md
  - notes/codex-task-results/MNEMOSYNE-178-result.md
  - notes/codex-task-results/MNEMOSYNE-178-pr-finalization.md
```

The PR-finalization record is created after the canonical PR number is known.

## 8. Boundary

- This amendment does not modify `current/human-approved-spec.md`.
- It does not execute either research task.
- It does not authorize model switching, quota use, provider selection, API credentials, or external cost.
- It does not prove the clarification handoff works.
- It does not modify Meta-Agent or another target project.
- It does not permit fabricated reports or automatic execution-source updates.
