# Adaptive Explanation Stage B0 Status

> Non-execution-source live route status. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
status_id: ADAPTIVE-EXPLANATION-STAGE-B0-STATUS-002
created_by_task: MNEMOSYNE-176
last_status_task: MNEMOSYNE-177
source_stage_A_research: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001
source_decision_package: notes/research-batch-reviews/2026-07-adaptive-explanation-stage-a/03-stage-b-decision-preparation.md
protocol_package: notes/adaptive-explanation-stage-b0-package/README.md
execution_task: notes/research-prompts/ADAPTIVE-EXPLANATION-STAGE-B0-SMOKE-EXECUTION-001.md
preflight_result: notes/adaptive-explanation-stage-b0-package/08-context-isolation-preflight-result.md
surface_decision_package: notes/adaptive-explanation-stage-b0-package/09-isolated-execution-surface-decision-package.md
status: smoke_execution_authorized_but_blocked_CONTEXT_ISOLATION_FAILURE_zero_cells
user_disposition: EXECUTE_STAGE_B0_SMOKE
execution_source: current/human-approved-spec.md
execution_source_modified: false
Stage_B0_protocol_designed: true
Stage_B0_smoke_execution_authorized: true
Stage_B0_smoke_executed: false
Stage_B0_smoke_cells_started: 0
Stage_B0_preflight_status: CONTEXT_ISOLATION_FAILURE
Stage_B0_core_selected: false
Stage_B1_selected: false
current_user_assessed: false
persistent_or_cross_Agent_memory_authorized: false
```

## 1. PR #228 verification

```yaml
PR_228:
  state: merged
  merge_commit: 77b9c01f5ac5b50721f1882f4030da49fbac108a
  merged_at: 2026-07-28T15:44:14Z
master_identical_to_merge_commit_at_MNEMOSYNE_177_start: true
accessible_open_PRs_before_MNEMOSYNE_177_branch: []
```

The complete B0 protocol package is present on `master`. Stage A remains accepted with corrections as non-execution-source evidence.

## 2. User execution decision

After PR #228 merged, the user selected:

```yaml
user_disposition: EXECUTE_STAGE_B0_SMOKE
required_precondition:
  - verify_true_isolated_worker_contexts
failure_rule:
  - return_CONTEXT_ISOLATION_FAILURE_if_not_available
  - do_not_degrade_to_single_context_pseudo_experiment
```

This is task-local authorization to attempt the smoke preflight and, only if isolation passes, execute the 32-cell smoke matrix. It is not authorization to change the protocol, use real participants, or begin Stage B1.

## 3. Isolation preflight result

```yaml
preflight:
  product_surface: standard_ChatGPT_conversation_with_GitHub_app
  fresh_isolated_Tutor_context_per_cell: unavailable
  hidden_key_exclusion_by_construction: unavailable
  independent_Reviewer_context: unavailable
  provider_API_or_agent_worker_runtime: unavailable_in_current_task
  exact_request_level_context_identity: unavailable
  result: CONTEXT_ISOLATION_FAILURE
  cells_started: 0
```

The current conversation cannot spawn 32 fresh Tutor contexts or a separate Reviewer context. The maintainer context can read hidden author keys and scoring rules; it may not then generate Tutor outputs while pretending to forget them.

No C0–C3 output, score, comparison, repeat, or smoke disposition was manufactured.

## 4. Meaning of the failure

The result establishes only that the current execution surface cannot satisfy the protocol's context-isolation contract.

It does **not** establish:

- that the B0 protocol is invalid;
- that one condition is superior;
- that a named model failed;
- that all Tutor cells require a frontier model;
- that Stage B1 should begin;
- that the route should be silently stopped.

The exact backend remains `unknown_or_not_attestable`.

## 5. Protocol package retained

```yaml
package:
  version: 0.1.0
  conditions:
    - C0_generic_simple_instruction
    - C1_fixed_worked_example_and_intuitive_first_policy
    - C2_adaptive_local_diagnosis
    - C3_adaptive_plus_recovery
  fixtures:
    total: 16
    smoke: 8
    core_additional: 8
  smoke_primary_cells: 32
  current_state: designed_not_executed
```

No condition is an approved production teaching policy.

## 6. Material and privacy boundary

```yaml
materials:
  public_mathematics_content: allowed
  synthetic_learner_traces: allowed
  current_user_learning_history: prohibited
  private_chat_or_voice_transcript: prohibited
  customer_or_confidential_material: prohibited
  real_participants: prohibited
  persistent_learner_state: prohibited
```

These boundaries remain unchanged.

## 7. Recovery surface classes

A future run requires a separately selected and task-authorized surface such as:

```yaml
candidate_surface_classes:
  - provider_API_harness_with_fresh_request_per_cell_and_separate_reviewer_requests
  - agent_runtime_with_demonstrable_child_context_isolation
  - manual_multi_conversation_run_with_high_operator_burden
```

Before smoke, the surface must pass a sentinel-based isolation harness test. A natural-language claim that contexts are separate is insufficient when no observable evidence exists.

## 8. Capability estimate

```yaml
capability_plan:
  surface_and_trust_boundary_selection:
    next_step_requires_frontier: recommended
    capability_class: FRONTIER_RECOMMENDED
  bounded_harness_implementation_after_selection:
    next_step_requires_frontier: no
    capability_class: NEXT_TIER_SUFFICIENT_CANDIDATE
  mechanical_sentinel_isolation_test:
    next_step_requires_frontier: no
    capability_class: MECHANICAL_ONLY
  frozen_Tutor_cells:
    next_step_requires_frontier: no
    capability_class: NEXT_TIER_SUFFICIENT_CANDIDATE
  final_math_and_smoke_adjudication:
    next_step_requires_frontier: recommended
    capability_class: FRONTIER_RECOMMENDED
```

This is a planning estimate, not proof that any named next-tier model is adequate.

## 9. Allowed future route decisions

```yaml
future_user_options:
  - PREPARE_PROVIDER_API_HARNESS
  - PREPARE_AGENT_RUNTIME_HARNESS
  - PREPARE_MANUAL_MULTI_CONVERSATION_PACKAGE
  - DEFER_B0_UNTIL_ISOLATED_SURFACE_EXISTS
  - STOP_B0_ROUTE
```

No option is selected by MNEMOSYNE-177.

## 10. Relationship to other routes

```yaml
route_relationships:
  Meta_Agent_product_build:
    owner: dedicated_Meta_Agent_conversation
    modified_by_MNEMOSYNE_177: false
  non_FABLE_health_review:
    owner: separate_health_review_conversation
    takeover: prohibited
  GPT_Live_learning:
    state: deferred
  persistent_learner_memory_and_cross_Agent_reuse:
    state: deferred_requires_behavioral_evidence_and_separate_user_decision
  MODEL_CAPABILITY_PLANNING_001:
    state: interim_user_facing_estimation_rule_being_adopted_controlled_validation_still_open
```

## 11. Exactly one safe next action

```yaml
safe_next_action:
  current:
    - review_and_merge_the_single_MNEMOSYNE_177_PR
  after_merge:
    - choose_whether_to_prepare_an_isolated_execution_surface_or_defer_B0
  automatic_smoke_execution: false
  automatic_surface_or_provider_selection: false
  no_Stage_B1_preparation: true
```

## 12. Boundaries

- No smoke cell has been run.
- No real learner or current user has been assessed.
- No persistent learner model has been created.
- No teaching policy has been promoted into execution source.
- No API, credentials, external cost, GPT Live, or Meta-Agent path is authorized.
