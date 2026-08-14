# Target-Lifecycle V0 Run — Pro-Recommended Owner Decision Candidate 001

> Pro/frontier recommendation that fills the D1–D7 run-decision structure after PR #277 merged. This is not Owner authorization, repository-creation authority, validation execution, quota authority, or a result. It is designed to reduce the next Owner action to one bounded decision plus recording the exact visible model/mode at launch.

```yaml
decision_candidate_id: MNE-TARGET-LIFECYCLE-V0-RUN-DECISION-CANDIDATE-001
task_id: MNEMOSYNE-210
source_master: 9432a4415cefeb7c605b73a94042ba1763e15f06
source_PR: 277
source_package: notes/target-agent-lifecycle-validation-package-v0.2/README.md
source_decision_gate: notes/target-agent-lifecycle-validation-package-v0.2/00-run-scope-and-owner-decision.md
candidate_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-002
validation_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-VALIDATION-002
status: PRO_RECOMMENDATION_READY_NOT_OWNER_AUTHORIZED
validation_repository_created: false
V0_authorized: false
V0_executed: false
V1_authorized: false
external_quota_authorized: false
```

## 1. Recommendation

Use one new public, synthetic-only GitHub repository and authorize **V0 only**.

Recommended repository name:

```text
08822407d/mnemosyne-target-lifecycle-validation-002
```

The repository name returned `Not Found` during MNEMOSYNE-210 preparation and therefore appeared unused at that time. Availability must be rechecked immediately before creation.

V0 should perform only repository/material/surface/identity/no-write sentinel checks. It must stop before any substantive S1–S11 scenario. A valid V0 result returns to the Owner/Pro route for review and does not authorize V1.

This is the lowest-risk useful continuation because:

- the candidate and package are already merged;
- the remaining immediate uncertainty is whether the execution surface, repository isolation, identity capture, and no-write proof are workable;
- V0 uses no real target material and no substantive architecture scenario;
- failure is cheap and informative;
- pre-authorizing V1 would unnecessarily combine two gates.

## 2. Recommended D1–D7 decisions

### D1 — Repository/store

```yaml
validation_repository_decision:
  disposition: RUN
  repository_or_store: 08822407d/mnemosyne-target-lifecycle-validation-002
  visibility: public
  creation_authorized: pending_Owner_confirmation
  repository_write_authorized: pending_Owner_confirmation
  allowed_paths_or_scope:
    - repository_initialization_and_V0_sentinel_material_only
    - runs/MNE-TARGET-LIFECYCLE-V0-001/
    - exact_public_synthetic_files_copied_from_the_merged_package_when_required_by_V0
  prohibited_repositories:
    - 08822407d/Mnemosyne
    - 08822407d/Meta-Agent
    - any_real_business_target
    - any_real_language_learning_target
  material_class: public_synthetic_only
```

Why public: the package is explicitly public/synthetic, a public repository makes path/diff/commit evidence easy to inspect, and no private material is needed. If the Owner prefers private visibility, that is a valid correction, but it should not be selected merely from generic caution because private access can complicate independent evidence review.

### D2 — Execution surface and visible selection

```yaml
execution_surface_decision:
  product_surface: standard_ChatGPT_conversation_with_GitHub_connector
  visible_model_or_mode_verbatim: RECORD_AT_LAUNCH_AFTER_OWNER_SELECTS_A_CURRENT_NEXT_TIER_OPTION
  reasoning_setting_verbatim: RECORD_AT_LAUNCH
  exact_backend_status: unknown_or_not_attestable
```

Recommendation: use a current next-tier/non-Pro model rather than Pro. V0 is frozen, bounded and primarily mechanical. The exact visible picker label is time-sensitive and must be copied verbatim at launch; this candidate does not invent or normalize it.

Escalate to Pro only if V0 exposes a semantic contradiction, authority ambiguity, no-write-proof design failure, or product-surface limitation that changes the architecture or run contract.

### D3 — Phase scope

```yaml
phase_authorization:
  phase_scope: V0_ONLY
  V1_pre_authorized: false
  stop_after_V0: true
  return_for_review: required
```

### D4 — Tool and network boundary

```yaml
tool_boundary:
  GitHub_read_on_Mnemosyne: allowed_only_to_read_merged_package_inputs
  GitHub_write_on_Mnemosyne: prohibited
  GitHub_read_write_on_synthetic_validation_repository: allowed_within_exact_V0_scope_after_authorization
  local_or_mechanical_tools: allowed_for_hash_path_diff_schema_and_identity_checks
  web_access: prohibited_not_needed
  Deep_Research_or_Fable: prohibited
  other_connected_apps: prohibited
  private_files_or_conversations: prohibited
```

### D5 — Quota

```yaml
quota_decision:
  paid_or_external_quota_authorized: false
  exact_surface_or_budget: no_separate_paid_or_external_run
```

This field does not claim that the user's ordinary ChatGPT plan has no internal usage limits. It means V0 is not authorized to create a separately paid Project, Deep Research/Fable run, API budget, or other external quota-consuming execution.

### D6 — Output and ingestion

```yaml
result_storage_decision:
  raw_output_location: 08822407d/mnemosyne-target-lifecycle-validation-002/runs/MNE-TARGET-LIFECYCLE-V0-001/
  raw_outputs_written_to_Mnemosyne: false
  Mnemosyne_ingestion_authorized: false
  later_reviewed_summary_candidate: allowed_only_after_material_and_provenance_review
  return_bundle:
    - run_manifest
    - exact_input_and_output_refs
    - commit_and_blob_identities
    - no_write_proof_for_Mnemosyne_Meta_Agent_and_real_targets
    - incident_ledger
    - V0_disposition
```

### D7 — Retention and cleanup

```yaml
retention_plan:
  repository_owner: 08822407d
  retain_until:
    - V0_result_review_completed
    - any_selected_V1_dependency_resolved
    - required_result_identities_preserved
  branch_cleanup:
    allowed_after_results_preserved_and_no_live_dependency: true
  repository_archive_or_delete:
    separately_authorized_later: true
  identities_that_must_survive:
    - repository_creation_identity
    - baseline_commit
    - each_V0_commit_and_tree
    - run_manifest_blob
    - input_and_output_blob_ids
    - no_write_proof
    - incident_records
    - reviewed_disposition
```

## 3. Normalized authorization candidate

```yaml
validation_run_authorization:
  authorization_status: PENDING_OWNER_CONFIRMATION
  package_id: MNE-TARGET-LIFECYCLE-VALIDATION-PACKAGE-002
  candidate_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-002
  validation_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-VALIDATION-002
  run_id: MNE-TARGET-LIFECYCLE-V0-001
  disposition: RUN
  phase_scope: V0_ONLY
  repository_or_store: 08822407d/mnemosyne-target-lifecycle-validation-002
  visibility: public
  product_surface: standard_ChatGPT_conversation_with_GitHub_connector
  visible_selection_verbatim: REQUIRED_AT_LAUNCH
  allowed_actions:
    - create_the_named_public_synthetic_repository_after_rechecking_name_availability
    - initialize_only_the_frozen_V0_material_and_run_paths
    - read_merged_Mnemosyne_package_inputs
    - write_only_the_synthetic_repository_within_V0_scope
    - run_mechanical_identity_path_diff_schema_and_no_write_checks
    - preserve_V0_attempts_failures_and_incidents
    - return_the_complete_V0_bundle
  prohibited_actions:
    - write_to_08822407d_Mnemosyne
    - write_to_Meta_Agent_or_real_targets
    - start_any_substantive_S1_through_S11_scenario
    - run_V1
    - use_private_or_real_target_material
    - use_web_research_Deep_Research_or_Fable
    - spend_external_quota
    - ingest_raw_results_into_Mnemosyne
    - modify_execution_source
    - adopt_candidate_into_any_real_target
  material_class: public_synthetic_only
  quota_authorized: false
  output_location: 08822407d/mnemosyne-target-lifecycle-validation-002/runs/MNE-TARGET-LIFECYCLE-V0-001/
  retention_plan: retain_through_V0_review_and_any_selected_V1_dependency_then_separately_decide_archive_or_delete
  decision_ref: pending_Owner_confirmation_of_this_candidate
  expires_with_run: true
  not_future_precedent: true
```

## 4. Minimal remaining Owner action

All design judgments that do not require Owner authority have been filled above. Before repository creation or V0 execution, the Owner still must explicitly decide whether to accept this profile.

A sufficient confirmation after this file is merged is:

```text
确认 MNE-TARGET-LIFECYCLE-V0-RUN-DECISION-CANDIDATE-001；
授权按推荐方案创建公开合成验证仓库并仅运行 V0。
执行时我会选择次一档模型，并把界面显示的模型/模式原文记录下来。
不要运行 V1，不要写入 Mnemosyne、Meta-Agent 或真实目标。
```

The Owner may instead correct the repository name, visibility, surface, model selection, phase scope, quota, output location, or retention plan.

## 5. Capability and research assessment

```yaml
model_capability_estimate:
  V0_execution:
    capability_class: NEXT_TIER_SUFFICIENT_CANDIDATE
    Pro_required: false
    mechanical_components:
      - repository_and_ref_identity
      - path_and_diff_checks
      - package_file_presence
      - no_write_proof
      - manifest_population
    escalation_triggers:
      - semantic_or_authority_conflict
      - required_product_surface_behavior_missing_or_changed
      - no_write_proof_cannot_be_established
      - private_or_real_material_required
      - executor_needs_to_change_candidate_or_package_semantics
  V0_adjudication:
    capability_class: FRONTIER_REQUIRED_IF_FAILURES_OR_CONFLICTS_OTHERWISE_FRONTIER_RECOMMENDED
  exact_backend_identity: unknown_or_not_attestable

deep_research_assessment:
  status: NOT_NEEDED
  reason: the immediate evidence gap is controlled V0 execution, not literature or external-fact synthesis

parallel_frontier_research_assessment:
  status: NOT_NEEDED_BEFORE_V0
  reason: no distinct non-duplicative research question blocks the sentinel run
```

## 6. Current boundary

This decision candidate advances the mainline by completing the Pro design and recommendation work. It does not cross the remaining Owner authority gate. Until explicit confirmation occurs:

```yaml
current_state:
  repository_creation_authorized: false
  synthetic_repository_write_authorized: false
  V0_authorized: false
  V0_executed: false
  V1_authorized: false
  external_quota_authorized: false
  target_adoption_authorized: false
```
