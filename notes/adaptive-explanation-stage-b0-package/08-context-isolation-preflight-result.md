# Adaptive Explanation Stage B0 — Context-Isolation Preflight Result

> Read-only execution preflight for `ADAPTIVE-EXPLANATION-STAGE-B0-SMOKE-EXECUTION-001`. No Tutor cell was started. This file does not contain experimental results and does not authorize a later run.

```yaml
preflight_id: ADAPTIVE-EXPLANATION-STAGE-B0-CONTEXT-ISOLATION-PREFLIGHT-001
created_by_task: MNEMOSYNE-177
task_id: ADAPTIVE-EXPLANATION-STAGE-B0-SMOKE-EXECUTION-001
package_version: 0.1.0
pinned_package_commit: master@77b9c01f5ac5b50721f1882f4030da49fbac108a
user_execution_authorization: received
status: CONTEXT_ISOLATION_FAILURE
cells_started: 0
cells_completed: 0
repository_write_by_smoke_executor: false
real_participants: false
current_user_data_used: false
```

## 1. Required isolation contract

The smoke task requires:

```yaml
isolation_gate:
  fresh_tutor_worker_context_per_cell: required
  tutor_worker_hidden_author_key_access: prohibited
  tutor_worker_other_condition_access: prohibited
  reviewer_context_separate_from_tutor: required
  controller_may_read_hidden_keys_only_if_it_never_generates_tutor_content_after_that_access: required
  exact_prompt_and_output_identity: required
```

The smoke matrix contains 32 primary condition × fixture cells. A valid run also requires independent scoring and condition-contamination review.

## 2. Available surface inspected

```yaml
available_surface:
  value: standard_ChatGPT_conversation_with_GitHub_app
  capabilities_observed:
    - one_current_conversation_context
    - GitHub_repository_read_and_task_authorized_write_actions
    - local_reasoning_in_the_current_assistant_context
  required_capabilities_not_available:
    - spawn_fresh_isolated_model_worker_context_per_cell
    - prevent_worker_access_to_controller_or_hidden_key_context_by_construction
    - create_a_separate_independent_reviewer_model_context
    - invoke_a_provider_API_or_agent_runtime_for_32_stateless_worker_calls
    - produce_request_level_context_isolation_evidence
```

The current assistant cannot create 32 independent Tutor contexts or a genuinely separate Reviewer context. Reusing the current conversation after reading hidden keys would violate the protocol; pretending to forget is explicitly prohibited.

## 3. Result

```yaml
status: CONTEXT_ISOLATION_FAILURE
cells_started: 0
reason:
  - current_surface_exposes_no_isolated_worker_or_subagent_creation_capability
  - current_context_has_maintainer_and_package_visibility_incompatible_with_Tutor_worker_isolation
  - reviewer_and_Tutor_independence_cannot_be_demonstrated
  - no_model_API_or_agent_harness_is_available_in_this_task
```

No C0, C1, C2, or C3 response was generated. No synthetic fixture was presented to a Tutor worker. No score, condition comparison, or smoke disposition was manufactured.

## 4. What this failure means

This is an execution-surface failure, not evidence that:

- the B0 protocol is substantively invalid;
- any condition is better or worse;
- a particular model/backend failed;
- the user must use a frontier model for frozen Tutor cells;
- Stage B1 should begin.

The exact served backend of the current conversation is unknown or not attestable. The result depends on exposed context-isolation capabilities, not response style or speed.

## 5. Safe recovery options

A later run needs one of the following classes of surface:

```yaml
candidate_surface_classes:
  provider_API_harness:
    requirement: separate_stateless_or_isolated_request_per_Tutor_cell_and_separate_reviewer_requests
  agent_runtime_with_child_contexts:
    requirement: demonstrable_fresh_worker_contexts_and_hidden_key_access_control
  carefully_managed_manual_multi_conversation_run:
    requirement: one_fresh_conversation_per_cell_plus_separate_review_conversations_and_exact_identity_tracking
    burden: very_high
    recommendation: not_default
```

Before executing all 32 cells, the selected surface should pass an isolation-only harness check proving:

- a Tutor cell cannot see hidden keys or other conditions;
- the controller can preserve exact inputs and outputs;
- the Reviewer is separate from the Tutor;
- cell identity cannot be lost;
- visible execution conditions can be kept stable or changes can be recorded and stopped.

## 6. Model-capability estimate

```yaml
model_capability_estimate:
  select_or_implement_isolated_execution_harness:
    next_step_requires_frontier: no
    capability_class: NEXT_TIER_SUFFICIENT_CANDIDATE
    reason: bounded_engineering_with_frozen_isolation_and_identity_contract
    escalation_triggers:
      - ambiguous_security_or_trust_boundary
      - inability_to_prove_context_separation
      - provider_or_surface_semantics_unclear

  frozen_Tutor_cell_execution:
    next_step_requires_frontier: no
    capability_class: NEXT_TIER_SUFFICIENT_CANDIDATE
    reason: exact_condition_fixture_and_output_contract_are_frozen
    limitation: adequacy_must_be_validated_by_smoke_results

  mathematics_and_final_smoke_adjudication:
    next_step_requires_frontier: recommended
    capability_class: FRONTIER_RECOMMENDED
    reason: cross_condition_semantic_judgment_disputed_math_and_severe_failure_analysis
```

## 7. Boundary

- No smoke result exists.
- No core or Stage B1 work is authorized.
- No model or provider is selected by this result.
- No API key, external service, or automation is requested or authorized here.
- A future run requires a fresh task-local execution decision after the surface and isolation evidence are identified.
