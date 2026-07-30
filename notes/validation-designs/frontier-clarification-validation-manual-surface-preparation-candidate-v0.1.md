# Frontier Clarification Validation — Manual Surface Preparation Candidate v0.1

> Candidate preparation design for the `SURFACE-MANUAL` option in the merged frontier-clarification validation package. It does not select the option, verify current product capability, authorize V0, open worker contexts, transfer packets, spend quota or execute any validation cell.

```yaml
candidate_id: FRONTIER-CLARIFICATION-VALIDATION-MANUAL-SURFACE-CANDIDATE-001
created_by_task: MNEMOSYNE-182
version: 0.1.0
status: prepared_candidate_not_selected_not_verified_not_authorized
source_package: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
source_package_merge_commit: 67eb96d5317a2bb589236a4a8b2e75be2508d830
source_decision_package: notes/frontier-clarification-validation-package/12-execution-surface-and-user-decision-package-v0.1.md
source_V0_taskbook: notes/frontier-clarification-validation-package/08-v0-sentinel-context-isolation-taskbook-v0.1.md
material_class: public_or_synthetic_only
substantive_cells: 0
V0_selected: false
V0_authorized: false
V0_executed: false
```

## 1. Decision this candidate supports

This file reduces the work needed to answer `FCV-SURFACE-Q1` without deciding it:

> Is a manually orchestrated set of fresh conversations worth preparing and verifying as the V0 execution surface, or are its isolation, identity, no-write and operator-burden limits severe enough to prefer an API/runtime route or defer?

Possible owner dispositions after review:

```yaml
owner_surface_disposition:
  - PREPARE_AND_VERIFY_MANUAL_V0_PREFLIGHT
  - REVISE_MANUAL_CANDIDATE
  - PREFER_API_OR_RUNTIME_PREPARATION
  - DEFER_SURFACE_SELECTION
  - STOP_ROUTE
```

None of these is selected here.

## 2. Why manual is a plausible first candidate

Potential advantages:

- no API credential decision is inherently required;
- each packet transfer is visible to the operator;
- V0 has five sentinel workers and zero substantive scenario cells;
- failure can be detected before the 40-cell V1 burden;
- the route can expose whether ordinary product surfaces are sufficiently observable without first building a harness.

Material disadvantages:

- manual transfer and context creation are error-prone;
- project memory, prior chat context, attachments, connected tools or hidden product state may be difficult to exclude or attest;
- exact packet identity can be lost through copy/paste or formatting;
- proving no repository write may remain incomplete;
- V1 would require much higher operator burden;
- a manual V0 pass would not prove manual V1 is acceptable.

This candidate is therefore a low-implementation-cost diagnostic, not a presumed best surface.

## 3. Proposed V0-only context graph

```yaml
manual_context_graph:
  package_preparation_context:
    role: freeze_exact_packets_and_receipts
    may_execute_worker_output: false
    hidden_key_access: no_by_default

  human_operator_controller:
    role:
      - create_fresh_contexts
      - transfer_exact_packets
      - release_only_scripted_sentinel_turns
      - preserve_exact_outputs
    may_interpret_or_rewrite_worker_output: false
    may_improvise_scripted_owner_turns: false

  sentinel_workers:
    count: 5
    contexts:
      - Q0_worker
      - Q1_worker
      - Q2_worker
      - Q3_worker
      - Q4_worker
    fresh_context_per_worker: required
    connected_apps_or_repository_access: prohibited
    hidden_key_access: prohibited
    other_condition_access: prohibited

  reviewer_context:
    separate_from_all_workers: required
    sees:
      - exact_worker_inputs
      - exact_worker_outputs
      - sentinel_expected_key
      - V0_rubric

  adjudicator_context:
    created_only_if_triggered: true
    must_not_be_a_worker_context: true
```

The operator may know the sentinel script but must transfer it literally and must not generate or repair worker responses.

## 4. Candidate clean-context contract

For every worker context, record:

```yaml
worker_context_receipt:
  worker_id:
  visible_product_surface:
  visible_model_or_mode_text:
  exact_backend_identity: unknown_or_not_attestable
  created_as_new_context: true | false | unknown
  prior_chat_count_in_context: 0 | unknown
  project_or_workspace_membership:
  memory_setting_or_observable_scope:
  old_Mnemosyne_or_validation_files_added: false | true | unknown
  GitHub_or_connected_apps_selected: false | true | unknown
  broad_file_or_web_tools_available: false | true | unknown
  only_frozen_packet_received: true | false | unknown
  operator_limitations: []
```

Required candidate rule:

- `true` or `unknown` for prior context, connected apps, broad tools or old validation material is not silently accepted;
- unresolved exposure returns `CONTEXT_ISOLATION_FAILURE` or `BLOCKED`, depending on whether contamination occurred or only proof is incomplete;
- a worker cannot be qualified by asking it to promise that it will ignore visible material.

## 5. Exact packet identity

Before any V0 run, the preparation task must create five immutable worker packets from the merged package and record:

```yaml
packet_receipt:
  packet_id:
  condition_id:
  source_package_commit:
  source_file_blob_SHAs: []
  rendered_packet_filename:
  byte_hash_algorithm: SHA-256_or_equivalent
  rendered_packet_hash:
  byte_length:
  line_count:
  transfer_method:
  worker_receipt_of_packet_id:
  post_transfer_identity_check:
```

Requirements:

- the same common-envelope version is used for all five conditions;
- each worker receives exactly one condition contract;
- no hidden key, another contract, another worker output or future turn is included;
- formatting conversion must be captured as a new rendered-packet identity rather than assumed byte-identical;
- if the product surface transforms an attachment or pasted block in an unobservable way, record the limitation and do not claim exact-byte identity.

## 6. Proposed operator sequence for V0 preparation

This sequence is preparation-only until a later owner authorization names the exact run.

1. Pin the merged package commit and verify all required package files.
2. Re-check the latest default branch and all accessible open PRs.
3. Freeze five worker packets and the reviewer packet; compute identities.
4. Record the visible surface, memory/project configuration and connected-tool state available to the operator.
5. Determine whether five fresh worker contexts can be created without prior task material or connected repository/file tools.
6. Determine whether a separate reviewer context can receive keys and exact worker artifacts without sharing hidden state with workers.
7. Define the literal transfer log and operator checklist.
8. Define pre/post repository-state evidence and any remaining no-write limitation.
9. Return a surface-verification report without opening worker contexts if any required boundary is already unsupported.
10. Ask for a separate owner decision. Do not execute V0 automatically after preparation passes.

## 7. Candidate no-write evidence

The future V0 task has zero repository-write authorization. The strongest manual-route evidence available should combine:

```yaml
no_write_evidence_candidate:
  worker_side:
    - worker_contexts_have_no_GitHub_or_connected_write_tools
    - packets_contain_no_repository_write_instruction
    - worker_outputs_are_returned_to_operator_only
  controller_side:
    - pinned_before_master_SHA
    - complete_accessible_open_PR_enumeration_before
    - pinned_after_master_SHA
    - complete_accessible_open_PR_enumeration_after
    - explicit_list_of_GitHub_actions_invoked
  repository_side:
    - before_after_default_branch_comparison
    - before_after_relevant_ref_comparison
    - before_after_open_PR_set_comparison
```

Limitations:

- model or operator self-report alone is not high-confidence no-write proof;
- inability to enumerate relevant refs or PRs cannot be converted into `PASS` without a separately approved run-scoped exception;
- the historical Meta-Agent no-write exception is not future precedent;
- an unchanged default branch alone does not prove that no branch, PR, issue, comment or label changed.

If default evidence is unavailable, the candidate disposition is `BLOCKED_NO_WRITE_OBSERVABILITY`, `DEFER`, or a separately proposed run-scoped exception. This file does not approve an exception.

## 8. Surface-verification schema

A bounded preparation task must return:

```yaml
manual_surface_verification:
  verification_id:
  package_commit:
  product_surface_observed_at:
  context_creation_capability:
  worker_context_isolation_evidence: []
  memory_project_and_attachment_boundary: []
  connected_tool_boundary: []
  packet_identity_method:
  reviewer_separation_method:
  no_write_evidence_method:
  operator_transfer_log_method:
  projected_V0_manual_contexts:
  projected_V0_transfers:
  projected_V1_manual_contexts_if_later_considered:
  unresolved_limitations: []
  blocking_failures: []
  result: PASS_FOR_OWNER_DECISION | PASS_WITH_LIMITATIONS_FOR_OWNER_DECISION | BLOCKED | FAIL
  V0_authorized: false
  cells_started: 0
```

`PASS_FOR_OWNER_DECISION` only means the owner has enough verified information to decide whether to authorize V0. It is not a V0 pass.

## 9. Required owner fields before preparation or execution

### Before preparation

```yaml
manual_surface_preparation_decision:
  selected_action: PREPARE_AND_VERIFY_MANUAL_V0_PREFLIGHT | REVISE | DEFER | STOP
  visible_surface_to_check:
  maximum_manual_contexts_or_transfers:
  acceptable_preparation_burden:
  allowed_repository_reads:
  repository_write: prohibited
  expires_with_preparation_task: true
```

### Before V0 execution

A later record must separately settle:

- exact package commit;
- exact visible model/mode for all five workers and reviewer;
- accepted context-isolation evidence;
- accepted packet-identity evidence;
- accepted no-write evidence or explicit run-scoped exception;
- maximum manual burden and quota;
- reviewer arrangement;
- exact stop conditions;
- authorization of V0 only.

## 10. Blocking conditions

```yaml
manual_surface_blockers:
  - worker_context_has_prior_validation_or_hidden_key_material
  - worker_has_connected_repository_or_broad_file_access
  - fresh_context_status_cannot_be_established_to_the_required_standard
  - exact_packet_identity_is_not_reconstructable
  - reviewer_and_worker_state_may_be_shared
  - operator_must_improvise_scripted_responses
  - required_no_write_observability_is_missing_without_exception
  - private_or_real_user_material_enters_the_run
  - product_surface_fallback_or_context_merge_changes_the_run_condition
```

## 11. Relationship to API and runtime routes

This candidate does not claim manual is superior.

```yaml
comparison_rule:
  choose_API_or_RUNTIME_preparation_when:
    - manual_context_or_transfer_burden_is_unacceptable
    - packet_identity_needs_machine_level_capture
    - connected_tool_or_memory_isolation_cannot_be_attested_manually
    - no_write_or_access_logs_require_a_harness
    - later_V1_repeatability_is_a_primary_goal

  retain_MANUAL_as_candidate_when:
    - V0_only_diagnostic_value_is_high
    - no_credentials_or_harness_are_preferred
    - operator_burden_is_accepted
    - all_blocking_boundaries_can_be_verified
```

A manual V0 result does not authorize manual V1. Surface choice may be reconsidered after V0.

## 12. Capability and research assessment

```yaml
capability_assessment:
  candidate_design: FRONTIER_RECOMMENDED
  run_specific_packet_population: NEXT_TIER_SUFFICIENT_CANDIDATE_after_freeze
  packet_hash_and_manifest_checks: MECHANICAL_ONLY
  manual_surface_verification: NEXT_TIER_SUFFICIENT_CANDIDATE_with_frontier_review_of_trust_boundary
  owner_surface_selection: HUMAN_ONLY

research_assessment:
  independent_Fable_adversarial_surface_review: RECOMMENDED_BEFORE_SELECTION
  additional_Pro_Deep_Research: NOT_NEEDED
  reason: the_decision_gap_is_surface_threat_model_and_attestable_evidence_not_broad_literature_coverage
```

## 13. Safe next action

```yaml
safe_next_action:
  - independently_review_this_candidate_and_the_merged_package
  - user_decides_whether_to_prepare_and_verify_manual_V0_preflight
  - if_selected_create_one_bounded_preparation_task_with_zero_cells
  - do_not_authorize_or_execute_V0_in_the_same_automatic_step
```

No current product-surface capability, isolation property or no-write proof is asserted as verified by this candidate.