# Target-Lifecycle V1 Baseline Run — Pro-Recommended Owner Decision Candidate 001

> Pro/frontier recommendation prepared after V0 adjudication. This file is not Owner authorization, V1 execution, architecture acceptance, target adoption, external-quota authority or a change to candidate/validation semantics.

```yaml
decision_candidate_id: MNE-TARGET-LIFECYCLE-V1-RUN-DECISION-CANDIDATE-001
task_id: MNEMOSYNE-212
source_master: 930b5ed0c8d1db82e46fd9439035db3f2dd20c46
source_V0_adjudication: notes/validation-adjudications/MNE-TARGET-LIFECYCLE-V0-ADJUDICATION-001.md
source_V0_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
source_V0_head: e8e3296922185b4b70997c2351d6f39423f2cd4f
package_id: MNE-TARGET-LIFECYCLE-VALIDATION-PACKAGE-002
candidate_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-002
validation_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-VALIDATION-002
proposed_run_id: MNE-TARGET-LIFECYCLE-V1-001
status: PRO_RECOMMENDATION_READY_NOT_OWNER_AUTHORIZED
V1_authorized: false
V1_executed: false
V2_authorized: false
external_quota_authorized: false
target_adoption_authorized: false
```

## 1. Recommendation

Authorize one **complete baseline V1** in the existing public synthetic repository, using the three-conversation staged multi-cell profile:

```text
notes/target-agent-lifecycle-v1-execution-package-001/README.md
```

Selected scenario set:

```yaml
baseline_scenarios:
  - S1
  - S2
  - S3
  - S4
  - S5
  - S6
  - S7
  - S8
  - S9
  - S11
exploratory_scenarios_not_selected:
  - S10
```

A complete baseline disposition requires all selected baseline-critical scenarios. S10 is optional exploration and is intentionally excluded from this first V1.

## 2. Why V1 may proceed

V0 has been Pro-adjudicated as a valid sentinel pass:

- exact package and Owner authorization binding succeeded;
- the public synthetic repository is accessible and isolated;
- material remained public/synthetic;
- only V0 evidence paths were written;
- Mnemosyne and Meta-Agent default-branch refs remained unchanged;
- no substantive scenario started;
- no candidate or package revision is required before V1.

V0 does not establish substantive architecture correctness. V1 generates that evidence.

## 3. Recommended decisions

### D1 — Repository and pinned base

```yaml
validation_repository_decision:
  disposition: RUN
  repository_or_store: 08822407d/mnemosyne-target-lifecycle-validation-002
  visibility: public
  repository_exists: true
  V1_base_ref: master
  V1_pinned_base_sha: e8e3296922185b4b70997c2351d6f39423f2cd4f
  V0_evidence_preserved: true
  repository_write_authorized: pending_Owner_confirmation
  allowed_scope:
    - V1_controller_fixture_and_task_branches_named_by_execution_profile
    - runs/MNE-TARGET-LIFECYCLE-V1-001/
    - exact_public_synthetic_fixture_and_scenario_outputs
  prohibited_repositories:
    - 08822407d/Mnemosyne
    - 08822407d/Meta-Agent
    - any_real_business_target
    - any_real_language_learning_target
  material_class: public_synthetic_only
```

Reuse avoids another repository-creation dependency and preserves V0→V1 lineage. V1 must pin the exact V0 final head before its first write.

### D2 — Execution surface, logical cells and actual conversations

```yaml
execution_surface_decision:
  controller_and_worker_surface: standard_ChatGPT_conversation_with_GitHub_connector
  execution_profile: staged_multicell_three_conversations
  logical_cells:
    - controller_and_fixture
    - core_S1_S2_S3_S4_S5_S6_S9
    - positive_documentation_S7
    - fresh_negative_documentation_S8
    - backup_restore_S11
    - final_mechanical_closeout
  actual_conversations:
    - name: MNE-DR-003 Execute
      role: main_next_tier_executor_controller_core_S7_S11_and_closeout
    - name: MNE-DR-003 S8
      role: mandatory_fresh_negative_documentation_worker
    - name: MNE-DR-003 Review
      role: mandatory_fresh_Pro_adjudicator
  recommended_next_tier_visible_selection_if_still_available: gpt-5.6 sol extra high
  each_conversation_visible_selection_verbatim: RECORD_AT_LAUNCH
  each_conversation_reasoning_setting_verbatim: RECORD_AT_LAUNCH
  exact_backend_status: unknown_or_not_attestable
```

Logical cells retain separate task branches, inputs, write sets and results even when the main executor runs compatible cells in one conversation.

Use Pro/frontier for:

- the current V1 design and Owner decision package;
- final V1 semantic adjudication in a fresh conversation;
- any protocol, authority, contamination or candidate conflict.

Use a next-tier model for the main execution conversation and fresh S8 conversation unless failure evidence triggers escalation.

### D3 — Phase and scenario scope

```yaml
phase_authorization:
  phase_scope: V1_BASELINE_ONLY
  selected_scenarios:
    - S1
    - S2
    - S3
    - S4
    - S5
    - S6
    - S7
    - S8
    - S9
    - S11
  S10_selected: false
  V2_pre_authorized: false
  candidate_amendment_during_run: prohibited
  stop_after_complete_V1_bundle: true
  return_for_fresh_Pro_adjudication: required
```

### D4 — Tool, branch and network boundary

```yaml
tool_boundary:
  GitHub_read_on_Mnemosyne: allowed_only_for_exact_merged_candidate_validation_package_and_authorization_inputs
  GitHub_write_on_Mnemosyne: prohibited
  GitHub_read_on_Meta_Agent: allowed_only_for_before_after_default_branch_ref_no_write_proof
  GitHub_write_on_Meta_Agent: prohibited
  GitHub_read_write_on_synthetic_repository: allowed_only_within_execution_profile
  local_or_mechanical_tools: allowed_for_hash_path_diff_schema_identity_and_restore_checks
  web_access: prohibited_not_needed
  Deep_Research_or_Fable: prohibited
  other_connected_apps: prohibited
  private_files_or_conversations: prohibited
  scenario_PRs: prohibited_unless_separately_authorized
  task_branch_rule: one_task_ID_one_canonical_branch
```

### D5 — Quota

```yaml
quota_decision:
  paid_or_external_quota_authorized: false
  exact_surface_or_budget: no_separate_paid_Project_Deep_Research_Fable_API_or_external_run
```

Ordinary plan/model use remains subject to the user's product limits, but no separate external quota is authorized.

### D6 — Output and Mnemosyne ingestion

```yaml
result_storage_decision:
  raw_output_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  raw_output_root: runs/MNE-TARGET-LIFECYCLE-V1-001/
  scenario_output_locations: exact_task_branches_and_controller_result_refs
  required_identity_for_each_file:
    - git_blob_sha
    - creation_or_update_commit_sha
  raw_outputs_written_to_Mnemosyne: false
  Mnemosyne_ingestion_authorized: false
  later_reviewed_summary_candidate: allowed_only_after_fresh_Pro_material_and_provenance_review_and_separate_write_authority
  complete_return_bundle:
    - controller_manifest
    - fixture_identity_and_material_safety_receipt
    - exact_logical_cell_inputs_and_outputs
    - task_write_contracts
    - branches_commits_trees_and_blob_identities
    - declared_vs_actual_write_set_tables
    - scenario_dispositions
    - S8_contamination_and_isolation_receipts
    - incidents_retries_and_protocol_defects
    - real_repository_before_after_no_write_proof
    - backup_restore_evidence
    - complete_V1_result_bundle
```

### D7 — Retention and cleanup

```yaml
retention_plan:
  repository_owner: 08822407d
  preserve_V0_master_history: true
  retain_V1_task_branches_until:
    - complete_V1_bundle_reviewed_by_fresh_Pro
    - every_required_commit_tree_and_blob_identity_preserved
    - Owner_decides_architecture_or_rerun_route
  branch_deletion_after_gate:
    separately_authorized_or_Owner_default_after_explicit_release: true
  repository_archive_or_delete:
    separately_authorized_later: true
  identities_that_must_survive:
    - V0_final_head
    - V1_controller_and_fixture_commits
    - every_scenario_task_branch_head
    - every_output_blob
    - all_failed_attempt_and_retry_refs
    - before_after_no_write_refs
    - backup_snapshot_and_restore_identities
    - reviewed_Pro_disposition
```

Because V1 raw evidence is distributed across task branches, branches remain until final Pro adjudication confirms that unique evidence is preserved and issues a release decision.

## 4. Required execution topology

```text
MNE-DR-003 Execute — next-tier main executor
  Controller / fixture
  Core S1,S2,S3,S4,S5,S6,S9
  Positive S7
  Backup/restore S11
  Prepare isolated S8 branch
  Pause
       ↓
MNE-DR-003 S8 — fresh next-tier conversation
  Negative S8 only
       ↓
Return S8 exact refs to MNE-DR-003 Execute
  Mechanical closeout and complete bundle
       ↓
MNE-DR-003 Review — fresh Pro conversation
  Semantic adjudication
       ↓
Owner — accept, revise, defer or reject
```

S8 must not receive:

- S7's sufficient Agent-facing migration guide;
- S7 worker output;
- expected migration actions beyond the intentionally insufficient input;
- prior chat context containing those facts.

Any breach invalidates S8 and requires a separately adjudicated clean rerun.

## 5. Normalized pending authorization

```yaml
validation_run_authorization:
  authorization_status: PENDING_OWNER_CONFIRMATION
  package_id: MNE-TARGET-LIFECYCLE-VALIDATION-PACKAGE-002
  candidate_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-002
  validation_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-VALIDATION-002
  run_id: MNE-TARGET-LIFECYCLE-V1-001
  disposition: RUN
  phase_scope: V1_BASELINE_ONLY
  repository_or_store: 08822407d/mnemosyne-target-lifecycle-validation-002
  visibility: public
  pinned_base_sha: e8e3296922185b4b70997c2351d6f39423f2cd4f
  selected_scenarios:
    - S1
    - S2
    - S3
    - S4
    - S5
    - S6
    - S7
    - S8
    - S9
    - S11
  excluded_scenarios:
    - S10
  product_surface: standard_ChatGPT_conversation_with_GitHub_connector
  execution_profile_ref: notes/target-agent-lifecycle-v1-execution-package-001/README.md
  visible_selection_verbatim: REQUIRED_PER_CONVERSATION_AT_LAUNCH
  allowed_actions:
    - create_only_the_profile_named_controller_fixture_task_and_result_branches
    - initialize_the_frozen_public_synthetic_fixture
    - execute_only_selected_scenarios
    - use_one_main_next_tier_conversation_plus_one_fresh_S8_conversation
    - write_only_the_synthetic_repository_within_exact_task_contracts
    - perform_required_mechanical_and_restore_checks
    - preserve_attempts_failures_incidents_and_complete_bundle
    - read_named_real_repository_refs_only_for_no_write_proof
    - return_for_fresh_Pro_adjudication
  prohibited_actions:
    - write_to_08822407d_Mnemosyne
    - write_to_08822407d_Meta_Agent
    - access_or_write_unnamed_real_targets
    - run_S10_or_V2
    - modify_candidate_validation_or_frozen_scenario_semantics
    - use_private_or_real_target_material
    - use_web_Deep_Research_Fable_other_apps_or_external_quota
    - create_scenario_PRs
    - ingest_raw_results_into_Mnemosyne
    - accept_or_adopt_the_architecture
  material_class: public_synthetic_only
  quota_authorized: false
  output_location: 08822407d/mnemosyne-target-lifecycle-validation-002/runs/MNE-TARGET-LIFECYCLE-V1-001/
  retention_plan: retain_V1_branches_through_fresh_Pro_adjudication_and_identity_preservation_then_release_separately
  decision_ref: pending_Owner_confirmation_of_this_candidate
  expires_with_run: true
  not_future_precedent: true
```

## 6. Owner decision still required

All non-authority design judgments are filled. The Owner must still decide whether to accept this exact V1 profile.

A sufficient confirmation after this candidate and execution package are merged is:

```text
确认 MNE-TARGET-LIFECYCLE-V1-RUN-DECISION-CANDIDATE-001。
授权在 08822407d/mnemosyne-target-lifecycle-validation-002 中，
从 V0 final head e8e3296922185b4b70997c2351d6f39423f2cd4f 开始，
按三段对话的 staged multi-cell profile 运行 V1 baseline：S1–S9 和 S11；不运行 S10 或 V2。

主执行和 S8 使用次一档模型，每段启动时原样记录界面模型/模式；
S8 必须使用未见过 S7 充分迁移说明的全新对话；完成后交给另一段全新的 Pro 对话裁决。
只允许写合成验证仓库，不得写 Mnemosyne、Meta-Agent 或真实目标；
不得使用私有材料、Web/Deep Research/Fable/其他 app 或外部 quota；
不得把原始结果写回 Mnemosyne。
完成后停止。
```

The Owner may instead revise the selected scenarios, conversation topology, model/surface, repository, no-write scope, retention or quota boundary.

## 7. Capability and research assessment

```yaml
model_capability_estimate:
  V1_main_and_S8_execution:
    capability_class: NEXT_TIER_SUFFICIENT_CANDIDATE
    Pro_required: false
    recommended_visible_selection_if_available: gpt-5.6 sol extra high
    escalation_triggers:
      - semantic_or_authority_conflict
      - S8_contamination_or_isolation_failure
      - required_product_surface_capability_missing
      - no_write_proof_cannot_be_established
      - candidate_or_protocol_semantics_need_change
      - private_or_real_material_discovered
  V1_final_adjudication:
    capability_class: FRONTIER_REQUIRED
    fresh_conversation_required: true
  Owner_architecture_decision:
    capability_class: HUMAN_REQUIRED
  exact_backend_identity: unknown_or_not_attestable

deep_research_assessment:
  status: NOT_NEEDED
  reason: V1 requires controlled execution evidence rather than external research
parallel_frontier_research_assessment:
  status: DEFER_UNTIL_V1_RESULT
  reason: any independent challenge should target actual V1 findings rather than duplicate the frozen pre-run design
```

## 8. Current boundary

```yaml
current_state:
  V0_Pro_adjudicated: true
  V1_decision_candidate_prepared: true
  V1_execution_package_prepared: true
  V1_owner_authorization: false
  V1_executed: false
  S10_selected: false
  V2_authorized: false
  raw_result_ingestion_authorized: false
  architecture_globally_accepted: false
  target_adoption_authorized: false
```
