# Frontier Clarification Validation — Execution-Surface and User-Decision Package v0.1

> Owner decision package for use only after the validation package is reviewed and merged. It does not select a surface, authorize quota, execute V0/V1, or create a production clarification policy.

```yaml
decision_package_id: FRONTIER-CLARIFICATION-VALIDATION-SURFACE-DECISION-001
package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
created_by_task: MNEMOSYNE-181
version: 0.1.0
status: prepared_unanswered
current_selected_surface: none
V0_authorized: false
V1_authorized: false
```

## 1. Why a separate decision is required

The package freezes what to test, but not where or under which visible model/mode conditions to run it. Surface selection changes:

- whether worker, controller and reviewer contexts can be isolated;
- whether hidden-key and file access can be constrained;
- how exact inputs/outputs and tool calls are captured;
- whether credentials, external cost or manual orchestration are required;
- what no-write evidence is available;
- what reviewer-independence limitations remain.

These are owner, trust, cost and platform decisions. They cannot be silently defaulted by the package author.

## 2. Candidate surface routes

The options below are architecture classes, not verified current product claims. Current capability must be checked at decision time.

### SURFACE-API — Provider API harness

```yaml
option_id: SURFACE-API
meaning: Build or use a harness that constructs isolated requests from exact packets and captures exact responses.
advantages:
  - strong_packet_and_output_identity
  - explicit_tool_and_file_boundary
  - repeatable_context_creation
  - easier_mechanical_hash_and_access_logging
risks_or_costs:
  - credentials_and_secret_handling_decision
  - external_usage_cost
  - implementation_and_review_burden
  - provider_metadata_semantics_must_be_understood
required_before_use:
  - approved_credential_location_and_secret_boundary
  - cost_limit
  - exact_request_and_storage_plan
  - no_repository_write_configuration
  - V0_authorization
```

### SURFACE-RUNTIME — Isolated agent/runtime harness

```yaml
option_id: SURFACE-RUNTIME
meaning: Use an agent runtime that can create isolated workers, restrict tools/files and preserve run artifacts.
advantages:
  - lower_manual_orchestration
  - explicit_role_and_permission_model_possible
  - controller_worker_reviewer_graph_can_be_automated
risks_or_costs:
  - runtime_trust_boundary_must_be_verified
  - hidden_state_or_shared_cache_may_be_unclear
  - connected_tool_permissions_may_expand_scope
  - implementation_specific_evidence_required
required_before_use:
  - context_and_cache_isolation_evidence
  - exact_permission_map
  - artifact_capture_and_no_write_proof
  - cost_and_quota_boundary
  - V0_authorization
```

### SURFACE-MANUAL — Manual multi-conversation package

```yaml
option_id: SURFACE-MANUAL
meaning: An operator opens fresh conversations/contexts and transfers only one prepared packet to each worker, then returns exact outputs to a separate reviewer context.
advantages:
  - may_require_no_API_credentials
  - low_harness_implementation_cost
  - visible_human_control_of_each_transfer
risks_or_costs:
  - high_operator_burden
  - copy_paste_identity_and_omission_risk
  - harder_to_prove_hidden_file_and_cross_context_separation
  - product_surface_may_not_expose_required_audit_evidence
  - accidental_context_or_attachment_leakage
required_before_use:
  - exact_packet_files_and_hashes
  - fresh_context_receipts
  - operator_checklist_and_transfer_log
  - separate_reviewer_context
  - accepted_limitations_or_run_scoped_exception_if_default_proof_unavailable
  - V0_authorization
```

### SURFACE-OTHER — Another equivalent isolated mechanism

```yaml
option_id: SURFACE-OTHER
meaning: Propose another surface only with an explicit equivalence argument against every V0 isolation and identity requirement.
required_before_use:
  - context_graph
  - access_and_tool_boundary
  - exact_identity_capture
  - no_write_evidence
  - reviewer_separation
  - cost_and_authorization
```

### DEFER

```yaml
option_id: DEFER
meaning: Keep the package unexecuted until a surface can demonstrate the required boundary within acceptable cost and burden.
practical_effect: no_cells_run_and_no_evidence_is_fabricated
```

### STOP

```yaml
option_id: STOP
meaning: Stop the delegated-clarification validation route and retain the research/adjudication plus package as historical design evidence.
practical_effect: no_future_V0_or_V1_without_new_owner_decision
```

## 3. Decision Q1 — Surface route

```yaml
question_id: FCV-SURFACE-Q1
plain_language_question: >-
  Which surface route, if any, should be prepared and verified for V0?
why_it_matters: >-
  V0 cannot start unless the surface can prove the required worker/hidden-key/reviewer separation and exact identity.
options:
  - SURFACE-API
  - SURFACE-RUNTIME
  - SURFACE-MANUAL
  - SURFACE-OTHER
  - DEFER
  - STOP
free_form_allowed: true
reject_premise_allowed: true
safe_default_if_deferred: keep_package_unexecuted
```

Selecting a class does not prove current capability. A selected route requires a bounded current verification/preparation task.

## 4. Decision Q2 — V0 visible condition map

For each role, the owner must select or defer the visible model/mode condition:

```yaml
question_id: FCV-SURFACE-Q2
required_fields:
  packet_builder:
  Q0_sentinel_worker:
  Q1_sentinel_worker:
  Q2_sentinel_worker:
  Q3_sentinel_worker:
  Q4_sentinel_worker:
  reviewer:
  adjudicator_if_needed:
```

The record preserves operator-visible text. It does not attest a hidden backend. A stronger visible option does not prove review independence.

## 5. Decision Q3 — Cost, quota and burden

```yaml
question_id: FCV-SURFACE-Q3
plain_language_question: >-
  What run-scoped limits should stop V0 preparation or execution?
owner_fields:
  maximum_external_cost:
  maximum_manual_contexts_or_transfers:
  maximum_elapsed_operator_sessions:
  acceptable_artifact_storage_location:
  allowed_targeted_repeats: 0_recommended_for_V0
  stop_if_product_or_quota_fallback_notice: yes | no
  defer_if_no_default_no_write_proof: yes | no | consider_exception
```

These are owner value and resource decisions. Deep Research cannot choose them.

## 6. Decision Q4 — Reviewer arrangement

```yaml
question_id: FCV-SURFACE-Q4
options:
  - option_id: REVIEW-TWO-SEPARATE
    meaning: Two separate reviewer contexts plus adjudication for material disagreement.
  - option_id: REVIEW-ONE-PLUS-MECHANICAL
    meaning: One substantive reviewer plus mechanical checks, with explicit independence limitation.
  - option_id: REVIEW-HETEROGENEOUS
    meaning: Reviewer from a different provider/family when available, plus mechanical checks.
  - option_id: REVIEW-DEFER
    meaning: Do not execute until an acceptable review arrangement exists.
required_record:
  reviewer_actor_and_context_relation:
  model_and_provider_relation_if_attestable:
  human_sampling_or_adjudication_scope:
  known_limitations: []
```

Heterogeneous review may add value for severe/high-impact adjudication, but it is not a universal requirement for every cell and does not replace human authority.

## 7. Decision Q5 — V0 authorization

Only after Q1–Q4 and surface verification are complete may the owner choose:

```yaml
question_id: FCV-SURFACE-Q5
options:
  - AUTHORIZE_V0_ONLY
  - REVISE_SURFACE_PLAN
  - DEFER_V0
  - STOP_ROUTE
```

`AUTHORIZE_V0_ONLY` must name:

- exact package commit;
- exact surface and context graph;
- exact visible condition map;
- cost/quota and artifact boundary;
- reviewer arrangement;
- no-write evidence method;
- expiration with the V0 run.

It does not authorize V1.

## 8. Separate decision after V0

A valid V0 `PASS` creates one later decision:

```yaml
post_V0_options:
  - AUTHORIZE_V1_SMALL_SMOKE_ONLY
  - REVISE_AND_REPEAT_V0
  - ACCEPT_V0_AND_DEFER_V1
  - STOP_ROUTE
```

Before `AUTHORIZE_V1_SMALL_SMOKE_ONLY`, the owner must approve:

- the 40-cell matrix;
- the final Q0–Q4 visible execution map;
- architecture/model-condition confounding limitations;
- target repeat and early-stop limits;
- full artifact and reviewer burden;
- no-write/material boundary;
- V1-specific quota/cost.

## 9. Model-capability estimate

```yaml
model_capability_estimate:
  surface_trust_and_isolation_decision:
    capability_class: FRONTIER_RECOMMENDED
    reason: requires architecture_trust_permission_and_evidence_boundary_judgment

  surface_specific_harness_population:
    capability_class: NEXT_TIER_SUFFICIENT_CANDIDATE
    condition: only_after_surface_and_contract_are_frozen_and_mechanically_reviewable

  V0_sentinel_execution:
    capability_class: MECHANICAL_ONLY_or_NEXT_TIER_SUFFICIENT_CANDIDATE
    condition: validated_isolated_surface_and_exact_taskbook

  V1_Q0_Q1_workers:
    capability_class: NEXT_TIER_SUFFICIENT_CANDIDATE
    status: estimate_not_proof

  V1_Q2_Q3_workers:
    capability_class: NEXT_TIER_SUFFICIENT_CANDIDATE
    status: subject_of_validation_not_assumed_adequate

  V1_Q4_worker:
    capability_class: FRONTIER_REQUIRED_for_intended_comparator

  severe_failure_and_final_adjudication:
    capability_class: FRONTIER_REQUIRED_or_FRONTIER_RECOMMENDED

  mechanical_integrity_checks:
    capability_class: MECHANICAL_ONLY

  exact_backend_identity: unknown_or_not_attestable
```

Reassess after a V0 failure, surface change, permission change, V1 semantic failure or package revision.

## 10. Deep Research assessment

```yaml
deep_research_assessment:
  status: NOT_NEEDED
  recommended: no
  reason: >-
    The completed Pro and independent Fable research were adjudicated. The remaining evidence gap is direct workflow validation.
    Surface capability should first use current authoritative bounded verification; deeper research is justified only if a frozen,
    decision-relevant external question remains unresolved.

parallel_frontier_research_assessment:
  status: NOT_NEEDED
  recommended: no
  distinct_role: none_currently_identified
```

No ready-to-run same-topic research task is generated by this package because no additional research is currently recommended.

## 11. Decision record template

```yaml
execution_surface_decision:
  decision_id:
  owner:
  decision_ref:
  package_commit_sha:
  selected_route: SURFACE-API | SURFACE-RUNTIME | SURFACE-MANUAL | SURFACE-OTHER | DEFER | STOP
  surface_verification_refs: []
  context_graph:
  visible_condition_map:
  cost_quota_and_burden:
  reviewer_arrangement:
  no_write_evidence_method:
  material_boundary: public_or_synthetic_only
  V0_disposition: AUTHORIZE_V0_ONLY | REVISE_SURFACE_PLAN | DEFER_V0 | STOP_ROUTE
  authorized_actions: []
  excluded_actions:
    - V1_execution
    - V2_execution
    - V3_execution
    - repository_ingestion
    - target_write
    - execution_source_change
    - Meta_Agent_change
    - non_FABLE_route_import
  expires_with_run: true
  not_future_precedent: true
```

## 12. Safe default

When any required decision, verification or artifact is missing:

```yaml
safe_default:
  selected_surface: none
  V0_status: not_authorized
  V1_status: not_authorized
  cells_started: 0
  package_state: retained_unexecuted
```

## 13. Boundaries

This decision package does not:

- ask the user to select a surface before the package PR is reviewed/merged;
- make current product-capability claims without verification;
- select a provider or spend quota;
- authorize V0/V1 by itself;
- allow V2/V3;
- authorize credentials, repository writes or target-project ingestion;
- modify Meta-Agent or non-FABLE health-review routes;
- change Mnemosyne execution source.
