# Model-Capability-Aware Work Planning — Open Question

> Non-execution-source live open-question record. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
open_question_id: MODEL-CAPABILITY-PLANNING-001
record_type: live_non_execution_source_open_question
created_by_task: MNEMOSYNE-163
status: preparation_only_requires_research_and_controlled_validation
user_decision_recorded: true
source_raw: raw/chatgpt-discussion-058.md
execution_source: current/human-approved-spec.md
formal_mainline_selected: false
implementation_authorized: false
```

## 1. User constraint now recorded

Mnemosyne and future target-Agent artifacts must not state or imply that the user will always execute work with the most capable available model or highest reasoning tier.

The user's intended operating pattern is:

- concentrate genuinely deep, large-scale, high-impact reasoning into visible stages;
- notify the user before those stages so the user can choose Pro or another provider's frontier model;
- use a next-tier model for bounded, lower-difficulty, routine or mechanical work when adequate;
- preserve scarce frontier-model quota rather than spend it on every small Agent request;
- design and validate instructions so that a next-tier executor can meet the required contract where the task is classified as suitable.

This is a user resource and workflow constraint, not a permanent mapping from a task type to a named provider model.

## 2. Existing coverage and remaining gap

### Already covered

1. `current/run-context-and-pr-provenance-guard.md`
   - records the actual product surface and operator-visible/reported selection;
   - separates UI selection, provider mapping and backend attestation;
   - records review and human adjudication.

2. `current/human-approved-spec.md` §17
   - stages dependent Pro / Deep Research / cross-conversation prompt batches;
   - requires an explicit model-strength switch reminder before high-risk prompt generation when needed;
   - records `execute_in` for cross-conversation prompts.

3. `notes/chatgpt-work-mode-assessment-2026-07.md`
   - provides candidate Chat / Work / Codex surface-selection guidance;
   - is not execution source and contains time-sensitive platform assumptions.

4. `notes/idea-capture-buffer.md` / `IDEA-2026-0019`
   - records that model capability differences and work allocation require dynamic verification.

### Not yet covered

The repository does not yet have an approved answer for:

- how to classify the reasoning/capability demand of a task independently of a provider model name;
- how to split one Agent-building route into frontier-reasoning and routine-execution components;
- what evidence permits a next-tier model to be treated as adequate for an instruction set;
- how taskbooks should expose escalation triggers, verification requirements and fallback behavior;
- whether key Mnemosyne guidance is understandable and reliably executable by a next-tier model;
- when the cost of verification makes delegation counterproductive;
- how the user should be alerted without making every task stop for a model-choice question;
- how to prevent the model used during Mnemosyne construction from becoming an implicit runtime dependency of its target products.

## 3. Distinction from model provenance

```yaml
model_provenance_question:
  asks: what_surface_selection_actor_and_review_context_were_used
  current_guard: current/run-context-and-pr-provenance-guard.md

model_capability_planning_question:
  asks: what_capability_the_task_requires_and_how_to_allocate_or_escalate_work
  current_status: open

lower_tier_executability_question:
  asks: whether_a_non_frontier_executor_can_reliably_follow_the_artifact_and_meet_acceptance_criteria
  current_status: requires_controlled_validation
```

Recording that a Pro/Fable/frontier model produced an artifact does not prove that the artifact requires such a model to execute. Conversely, a task being mechanically described does not prove that a lower-tier model will preserve all semantic and authority boundaries.

## 4. Candidate investigation dimensions — not an approved schema

Future design may evaluate dimensions such as:

```yaml
candidate_dimensions:
  task_reasoning_demand:
    - mechanical_or_exact_transformation
    - bounded_rule_application
    - localized_judgment
    - multi_source_synthesis
    - architecture_or_policy_adjudication
    - open_ended_research_or_novel_design
  decomposition:
    - frontier_reasoning_components
    - next_tier_execution_components
    - mechanical_verification_components
    - human_decision_components
  escalation:
    - uncertainty_or_conflict_trigger
    - authority_or_safety_trigger
    - context_scale_trigger
    - novel_architecture_trigger
    - failed_validation_trigger
  executor_support:
    - self_contained_inputs
    - explicit_authority_and_forbidden_actions
    - acceptance_criteria
    - deterministic_checks
    - stop_on_ambiguity
    - return_to_frontier_reviewer
  fallback:
    - block_and_request_stronger_review
    - narrow_scope
    - produce_candidate_only
    - perform_mechanical_substeps_only
```

These are preparation dimensions only. They are not field names that future taskbooks must use, and they do not define “frontier” or “next tier” by vendor/model.

## 5. Evidence and validation needed before a solution

A future bounded study should combine:

1. **Repository evidence review**
   - identify representative Mnemosyne tasks performed under different visible product selections and surfaces;
   - separate task quality from hidden-backend speculation;
   - classify failures as reasoning, context, instruction, tool, observability, authority or mechanical defects.

2. **Artifact analysis**
   - examine whether important instructions rely on implicit expert knowledge, long context or unstated judgment;
   - identify where exact anchors, schemas, checklists or stop conditions can reduce model-capability dependence.

3. **Controlled read-only replay**
   - use the same pinned inputs and acceptance rubric with a user-selected frontier option and next-tier option visible at test time;
   - do not allow either tested run to judge itself as final;
   - compare correctness, evidence recovery, boundary adherence, hallucination, escalation behavior, output usability and review burden.

4. **Task-decomposition pilot**
   - compare monolithic frontier execution against frontier planning/adjudication plus next-tier bounded execution and mechanical verification;
   - measure whether delegation actually saves scarce quota after review/rework cost.

5. **Target-product portability check**
   - verify that a future Meta-Agent or small business Agent does not silently require the construction model's capability for ordinary runtime use;
   - mark functions that genuinely require escalation rather than treating the whole Agent as frontier-only.

## 6. Questions requiring later user decision

The user does **not** need to answer these now. A later decision package should ask only after evidence and a concrete test plan exist:

- Which currently visible option should be treated as the frontier test condition?
- Which currently visible option should be treated as the next-tier test condition?
- What kinds of errors or review burden are acceptable for next-tier execution?
- Which representative task classes should be included in the first controlled replay?
- Should the default be “next-tier unless escalated,” “frontier for design and next-tier for execution,” or another policy?
- Should model-capability hints remain advisory or become required fields for selected high-impact taskbooks?

Exact product labels must be captured at test time and must not be hard-coded here.

## 7. Relationship to the four isolated Pro Deep Research tasks

The four already prepared research tasks remain separate and may run concurrently:

- `PRO-DR-HO-GUIDANCE-001`;
- `PRO-DR-LEARNER-COGNITIVE-COACHING-001`;
- `PRO-DR-CROSS-AGENT-SHARED-MEMORY-001`;
- `PRO-DR-TARGET-MEMORY-MIGRATION-001`.

Their results may later inform context cost, target-product portability, migration and governance, but they are not inputs required to create this open question and they do not automatically answer it.

No fifth Pro Deep Research task is selected by MNEMOSYNE-163. A dedicated external-research prompt should be generated only after the four reports return or the user separately prioritizes this question.

## 8. Current safe next action

```yaml
safe_next_action:
  now:
    - user_executes_the_four_already_prepared_Pro_Deep_Research_tasks
    - user_returns_complete_reports_and_visible_execution_labels_if_available
    - preserve_future_important_run_visible_selection_and_reasoning_labels_verbatim
  later_after_report_review:
    - prepare_a_bounded_model_capability_planning_research_or_controlled_replay_package
    - ask_the_user_to_select_the_two_visible_test_tiers_at_that_time
    - keep_all_repository_and_target_writes_out_of_the_test_unless_separately_authorized
```

## 9. Boundaries

- This record is not an execution source or approved routing policy.
- It does not require frontier models for all Mnemosyne, Meta-Agent or target-Agent work.
- It does not declare a current model hierarchy or attest any backend.
- It does not authorize automatic model selection, switching, quota consumption or provider routing.
- It does not approve a task-capability schema, threshold, score or mandatory field.
- It does not claim that a next-tier model is adequate before controlled evidence exists.
- It does not modify the four current Pro Deep Research prompts.
- It does not select a target project or authorize target workspace, material ingestion, target write or operational build.
