# Adaptive Explanation Stage B0 — Isolated Execution-Surface Decision Package

> Non-execution-source recovery and decision preparation after `CONTEXT_ISOLATION_FAILURE`. This package does not select, provision, or run an external model/API/agent surface.

```yaml
decision_package_id: ADAPTIVE-EXPLANATION-STAGE-B0-ISOLATED-SURFACE-DECISION-001
created_by_task: MNEMOSYNE-177
source_preflight: notes/adaptive-explanation-stage-b0-package/08-context-isolation-preflight-result.md
smoke_task: notes/research-prompts/ADAPTIVE-EXPLANATION-STAGE-B0-SMOKE-EXECUTION-001.md
status: candidate_ready_for_future_surface_selection
smoke_executed: false
cells_started: 0
```

## 1. Decision to be made later

A later task must identify a surface that can prove, by construction and records, that:

1. every Tutor cell has a fresh isolated context;
2. Tutor workers never see hidden author keys, scoring anchors, other condition prompts, or other outputs;
3. Reviewer contexts are separate from Tutor contexts;
4. exact prompt, fixture, condition, output, and visible execution-condition identity are preserved;
5. no controller that has read hidden keys later generates Tutor content;
6. failure returns partial evidence without best-of selection or hidden retries.

## 2. Candidate surface classes

### Option A — Provider API harness

```yaml
option: provider_API_harness
strengths:
  - one_stateless_or_fresh_request_per_cell
  - exact_request_and_response_storage
  - explicit_controller_reviewer_separation_possible
  - repeatable_matrix_execution
risks:
  - API_cost_and_credentials
  - provider_specific_context_semantics
  - implementation_and_logging_errors
  - exact_backend_may_still_be_only_provider_attested_at_identifier_level
requirements:
  - user_approved_provider_and_budget
  - secrets_outside_repository
  - request_level_cell_IDs
  - separate_Tutor_and_Reviewer_clients_or_processes
  - isolation_harness_test_before_smoke
```

### Option B — Agent runtime with demonstrable child contexts

```yaml
option: agent_runtime_with_child_contexts
strengths:
  - native_worker_or_subagent_orchestration
  - controller_and_reviewer_roles_may_be_explicit
  - less_custom_request_plumbing
risks:
  - hidden_shared_context_or_memory
  - unclear_subagent_isolation_semantics
  - orchestration_layer_may_rewrite_prompts_or_outputs
requirements:
  - documented_or_mechanically_tested_context_boundaries
  - hidden_memory_disabled_or_scoped
  - raw_input_output_capture
  - stop_on_context_uncertainty
```

### Option C — Manual multi-conversation execution

```yaml
option: manual_multi_conversation_execution
strengths:
  - conceptually_simple_fresh_chat_per_cell
  - no_custom_API_harness_required
risks:
  - at_least_32_Tutor_conversations_plus_review_conversations
  - high_operator_burden_and_copy_error_risk
  - difficult_exact_identity_and_condition_control
  - expensive_frontier_conversation_usage_if_wrong_model_is_selected
requirements:
  - pre_generated_cell_files
  - strict_naming_and_manifest
  - no_hidden_key_in_Tutor_conversations
  - separate_review_conversations
recommendation: not_default
```

## 3. Required isolation-only harness test

Before B0 smoke authorization is reissued, run a non-substantive isolation test with synthetic sentinel strings rather than mathematics answers.

```yaml
isolation_harness_test:
  Tutor_A_receives:
    - condition_A_sentinel
    - public_fixture_sentinel
  Tutor_A_must_not_reveal:
    - hidden_key_sentinel
    - condition_B_sentinel
    - reviewer_sentinel
  Reviewer_receives:
    - Tutor_A_output
    - hidden_key_sentinel
  reviewer_output_must_not_feed_back_into_Tutor_A:
    - required
  exact_request_and_response_identity:
    - required
  pass_criteria:
    - no_cross_context_sentinel_leakage
    - separate_context_or_request_IDs
    - reproducible_cell_lineage
    - no_unrecorded_prompt_rewriting
```

A conversational assurance that contexts are separate is insufficient when the platform supplies no observable separation evidence.

## 4. Capability and quota plan

```yaml
capability_plan:
  surface_selection_and_security_boundary:
    capability_class: FRONTIER_RECOMMENDED
    next_step_requires_frontier: recommended
    reason: provider_surface_semantics_credentials_isolation_and_trust_boundary_judgment

  harness_implementation:
    capability_class: NEXT_TIER_SUFFICIENT_CANDIDATE
    next_step_requires_frontier: no
    reason: bounded_engineering_after_surface_and_contract_are_frozen

  isolation_mechanical_test:
    capability_class: MECHANICAL_ONLY
    next_step_requires_frontier: no
    reason: sentinel_and_identity_checks

  Tutor_cells:
    capability_class: NEXT_TIER_SUFFICIENT_CANDIDATE
    next_step_requires_frontier: no
    reason: frozen_cell_contract

  final_review_and_smoke_disposition:
    capability_class: FRONTIER_RECOMMENDED
    next_step_requires_frontier: recommended
    reason: semantic_condition_comparison_math_review_and_failure_adjudication
```

The split is a planning estimate, not a validation of any named model.

## 5. Future user decision options

```yaml
user_options:
  PREPARE_PROVIDER_API_HARNESS:
    meaning: choose_a_provider_and_prepare_but_do_not_run_an_isolated_harness
  PREPARE_AGENT_RUNTIME_HARNESS:
    meaning: choose_an_agent_surface_and_prepare_but_do_not_run_an_isolation_test
  PREPARE_MANUAL_MULTI_CONVERSATION_PACKAGE:
    meaning: accept_high_operator_burden_and_generate_cell_transfer_files
  DEFER_B0_UNTIL_ISOLATED_SURFACE_EXISTS:
    meaning: preserve_Stage_A_and_B0_design_without_execution
  STOP_B0_ROUTE:
    meaning: close_the_experimental_route_without_results
```

No option is selected by this file.

## 6. Boundaries

- No credentials or API keys may enter the repository.
- No provider is selected.
- No external cost is authorized.
- No isolation test or Tutor cell is run.
- No Stage B0 smoke execution authorization is carried forward automatically.
- Stage B1, GPT Live, persistent learner memory, and Meta-Agent remain out of scope.
