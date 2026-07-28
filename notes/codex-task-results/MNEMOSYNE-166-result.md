# MNEMOSYNE-166 Result

## 1. Task summary

```yaml
task_id: MNEMOSYNE-166
task_name: repair_four_topic_research_archive_and_prepare_first_target_minimum_upgrade_contract
status: COMPLETE_PENDING_CANONICAL_PR_CREATION_AND_HUMAN_MERGE
task_type: bounded_post_merge_storage_repair_and_candidate_design_preparation
repository: 08822407d/Mnemosyne
base_branch: master
pinned_base_sha: a66d92c572f178de52e3b3b238324decf279b7fb
canonical_branch: mnemosyne-166-repair-research-archive-and-prepare-upgrade-contract
execution_source_modified: false
target_project_selected: false
target_project_action: false
```

## 2. User intent and authorization

The user instructed this conversation to continue along the maintainer-recommended route after the four-topic research batch and asked whether the four original Deep Research conversation contexts were still needed.

The merged decision-preparation package ranked `FIRST_TARGET_MINIMUM_UPGRADE_CONTRACT` first for near-term value. MNEMOSYNE-166 therefore:

1. verifies the MNEMOSYNE-165 storage merge;
2. repairs storage defects that would otherwise prevent reliable archival/reconstruction;
3. prepares a non-execution-source minimum upgrade-contract candidate;
4. records the safe retention/archival boundary for the four source conversations.

```yaml
user_authorization:
  decision_ref: current_conversation_user_instruction_2026-07-28
  authorized_actions:
    - verify_PR_216_and_latest_master
    - repair_the_four_topic_research_archive_and_live_storage_paths
    - prepare_the_FIRST_TARGET_MINIMUM_UPGRADE_CONTRACT_candidate
    - create_one_canonical_branch_and_at_most_one_PR
  excluded_actions:
    - merge_or_auto_merge
    - execution_source_change
    - target_project_selection_or_build
    - target_material_ingestion_or_target_write
    - template_pack_adoption_without_later_user_disposition
    - automatic_migration_or_writeback
    - takeover_of_other_conversation_owned_routes
```

## 3. Repository and lineage preflight

```yaml
repository_preflight:
  visibility: public
  default_branch: master
  PR_216:
    state: merged
    merge_commit: a66d92c572f178de52e3b3b238324decf279b7fb
    merged_at: 2026-07-28T02:39:37Z
  master_relation_to_PR_216_merge_commit: identical
  accessible_open_PRs_before_branch_creation: []
```

```yaml
github_write_lineage_preflight:
  task_id: MNEMOSYNE-166
  intended_scope_summary: repair_MNEMOSYNE_165_research_storage_and_prepare_first_target_upgrade_contract_candidate
  default_branch: master
  pinned_default_branch_sha: a66d92c572f178de52e3b3b238324decf279b7fb
  intended_branch: mnemosyne-166-repair-research-archive-and-prepare-upgrade-contract
  open_pr_enumeration:
    method: GitHub_get_users_recent_prs_in_repo_state_open_limit_100
    pagination_complete: true
    all_accessible_open_prs_checked: true
  matches:
    by_exact_task_id: []
    by_intended_head_branch: []
    by_equivalent_open_scope: []
    false_positive:
      - GitHub_PR_number_166_is_MNEMOSYNE_118_not_task_MNEMOSYNE_166
  decision: create_new_lineage
```

## 4. MNEMOSYNE-165 storage verification and defect

PR #216 merged the four accepted reports, maintainer review, evidence ledger and decision preparation. Its manifest declared an eight-part exact archive:

```yaml
manifest_declared:
  archive_format: tar.bz2
  archive_bytes: 56573
  archive_sha256: f46cf54b923c00e86d8e539a290f76312ed287742ee9b713f9167db03e3cbd24
  tar_bytes: 235520
  tar_sha256: b63b62b2a397c31bff6a57aeefec6b0cccdd1a477e93550435bb34b75f2a8168
  base64_chars: 75432
  base64_sha256: bdb9292b9626afd3e76aa3a6f79086f92c0296309e4231f623d515fa92000138
  part_count: 8
  member_count: 8
```

The merged PR changed-path set contained only parts 1 through 6. Parts 7 and 8 were absent. The cycle README also named five cycle-local review/source files that did not exist; the actual canonical records were stored under `notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/`.

```yaml
post_merge_defect:
  archive_reconstructable_from_master_before_repair: false
  missing_parts:
    - part-007-of-008.txt
    - part-008-of-008.txt
  stale_or_invalid_pointers: true
  report_interpretation_changed_by_defect: false
  repair_required: true
```

## 5. Exact archive repair and mechanical verification

The archive was independently regenerated from the eight exact local prompt/report inputs identified by `manifest.json`. Deterministic metadata was fixed to PAX tar, member order from the manifest, mode `0644`, uid/gid `0`, empty uname/gname, mtime `0`, and no directory entries.

```yaml
regeneration_receipt:
  tar:
    bytes: 235520
    sha256: b63b62b2a397c31bff6a57aeefec6b0cccdd1a477e93550435bb34b75f2a8168
  tar_bz2:
    bytes: 56573
    sha256: f46cf54b923c00e86d8e539a290f76312ed287742ee9b713f9167db03e3cbd24
  Base64_after_removing_CR_LF:
    chars: 75432
    sha256: bdb9292b9626afd3e76aa3a6f79086f92c0296309e4231f623d515fa92000138
  manifest_level_identity: pass
  logical_parts:
    lengths:
      - 10000
      - 10000
      - 10000
      - 10000
      - 10000
      - 10000
      - 10000
      - 5432
```

The first six generated parts matched the existing archive payload. The missing final parts were created with line breaks only for transport readability; reconstruction removes CR/LF.

```yaml
new_part_blob_checks:
  part_007_wrapped_Git_blob_SHA: 0bbad5e3b569e81cfa0a47654130be7b70dda544
  part_008_wrapped_Git_blob_SHA: a7ca34ee2d38ede17883e208f8f8e5b7ca544c5f
  unwrapped_part_007_SHA256: cf9f696f14cd8fea48f19c8a74e5baa55f7f14b80657187ab33c6baf04cda295
  unwrapped_part_008_SHA256: b5ec7860ddf620b1d91ec47c5924dad1475713cd7ce27761d9e8027709b30b24
```

Repair record:

- `notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/04-post-merge-storage-integrity-repair.md`

## 6. Selected candidate route

The candidate is stored at:

- `notes/first-target-minimum-upgrade-contract-v0.1.md`

Its purpose is to let a first real target-Agent memory system begin before Mnemosyne is perfect while preserving the ability to upgrade without losing evidence, authority or rollback.

Candidate minimum:

```yaml
candidate_minimum:
  - stable_identity_for_authority_bearing_objects
  - source_refs_and_object_lineage
  - design_schema_policy_and_delivery_versions
  - preserved_raw_and_approved_authority
  - migration_manifest
  - explicit_old_to_new_mapping
  - preserve_transform_recompute_retire_decisions
  - validation_and_acceptance_criteria
  - previous_state_and_rollback_refs
  - rebuildable_derived_views_where_practical
  - change_class_and_escalation_gates
conditional_not_universal:
  - full_event_sourced_runtime
  - dual_write
  - shadow_cutover
  - bitemporal_storage
  - automated_migration_service
```

The candidate maps to existing template hooks but does not edit the target-project template pack. Its live status is:

- `current/first-target-minimum-upgrade-contract-status.md`

## 7. Deep Research conversation context disposition

After the exact archive and maintainer review package are complete, the four original Deep Research conversations are not required as active working contexts for the selected upgrade-contract route.

```yaml
conversation_disposition:
  routine_dependency_after_archive_repair: none
  archive_in_ChatGPT_UI: safe
  permanent_deletion_now: not_recommended
  preserve_for_exceptional_use:
    - conversation_local_citation_resolution
    - source_panel_and_activity_history
    - native_research_plan_or_runtime_timing_evidence
    - future_Deep_Research_product_incident_review
```

The user may archive the four chats after this repair is merged. They do not need to remain in the active conversation list. Keeping the archived chats is prudent until source portability repairs and any product incident review are explicitly waived or complete.

## 8. Files

```yaml
created:
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/parts/part-007-of-008.txt
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/parts/part-008-of-008.txt
  - notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/04-post-merge-storage-integrity-repair.md
  - notes/first-target-minimum-upgrade-contract-v0.1.md
  - current/first-target-minimum-upgrade-contract-status.md
  - notes/codex-task-results/MNEMOSYNE-166-result.md
  - notes/codex-task-results/MNEMOSYNE-166-pr-finalization.md
modified:
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/README.md
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/README.md
  - current/pro-deep-research-four-topic-batch-status.md
explicitly_not_modified:
  - current/human-approved-spec.md
  - notes/target-project-memory-system-template-pack.md
  - all_four_accepted_report_bytes
  - notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/01-maintainer-reliability-review.md
  - notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/02-unified-evidence-ledger.md
  - notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/03-decision-preparation.md
  - target-projects/
  - other_conversation_owned_route_files
```

The PR-finalization file is created after the canonical PR number is known.

## 9. Run context v0.2

```yaml
run_context:
  schema_and_task:
    record_version: v0.2
    task_id: MNEMOSYNE-166
    record_id: MNEMOSYNE-166-RUN-001
  date_or_window:
    started_at: 2026-07-28
    completed_or_recorded_at: 2026-07-28
  action:
    actor: ChatGPT
    actor_kind: mixed
    source: standard_ChatGPT_conversation_with_GitHub_app_and_local_mechanical_archive_regeneration
    switch_history:
      status: unknown
      evidence: []
  product_surface:
    value: standard_ChatGPT_conversation_with_GitHub_app
    evidence:
      - class: operator_observed
        ref: current_conversation_GitHub_app_invocation
        observed_or_accessed_at: 2026-07-28
        claim_scope: product_surface
  operator_selection:
    verbatim: unknown_not_separately_reported_for_this_task
    evidence:
      - class: unknown_or_not_attestable
        ref: null
        claim_scope: operator_visible_product_selection
        detail: no_separate_current_task_model_or_reasoning_label_was_recorded
  backend:
    status: unknown_or_not_attestable
    reason: consumer_Chat_and_GitHub_app_state_do_not_attest_the_exact_request_backend
  artifacts:
    status: recorded
    refs:
      - ref: notes/first-target-minimum-upgrade-contract-v0.1.md
        relation: created
        immutable_identity:
          status: not_available_before_merge
          type: git_blob_sha
          value: null
      - ref: notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/04-post-merge-storage-integrity-repair.md
        relation: created
        immutable_identity:
          status: not_available_before_merge
          type: git_blob_sha
          value: null
      - ref: raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/manifest.json
        relation: reviewed
        immutable_identity:
          status: recorded
          type: git_blob_sha
          value: 03167dc071c4372adc6a08e7543ddaee86c2b426
  user_authorization:
    status: authorized
    actor: user
    decision_ref: current_conversation_user_instruction_2026-07-28
    authorized_actions:
      - bounded_storage_repair
      - candidate_upgrade_contract_preparation
      - one_canonical_branch
      - one_canonical_PR
    excluded_actions:
      - merge
      - auto_merge
      - execution_source_or_template_adoption
      - target_project_actions
      - other_route_takeover
    evidence:
      - class: direct_user_instruction
        ref: current_conversation_user_message_2026-07-28
        observed_or_accessed_at: 2026-07-28
        claim_scope: MNEMOSYNE_166_task_local_repository_write_authorization
    expires_with_task: true
    not_future_precedent: true
  limitations:
    - exact_served_backend_and_switch_history_are_unknown_or_not_attestable
    - the_archive_regeneration_used_the_exact_local_report_and_prompt_files_previously_received_in_this_conversation
    - no_target_project_pilot_has_yet_validated_the_candidate_contract_burden_or_effectiveness
  omissions:
    - field: provider_normalization
      reason: not_applicable
      detail: no_current_provider_model_mapping_claim_is_needed
```

## 10. Review and lineage

```yaml
review_events:
  - review_id: MNEMOSYNE-166-ARCHIVE-REVIEW-001
    actor: local_mechanical_process
    actor_kind: mechanical_process
    role: deterministic_archive_regenerator_and_identity_checker
    context_relation_to_producer: fresh_verification
    model_relation_to_producer: not_applicable
    provider_relation_to_producer: not_applicable
    criteria_fixed_before_exposure: true
    review_scope: tar_tar_bz2_Base64_and_member_identity
    evidence:
      - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/manifest.json
      - exact_local_prompt_and_report_files
    result_ref: notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/04-post-merge-storage-integrity-repair.md
    limitations:
      - verification_does_not_assess_report_truth_or_backend_identity

  - review_id: MNEMOSYNE-166-CANDIDATE-REVIEW-001
    actor: ChatGPT
    actor_kind: model
    role: candidate_designer
    context_relation_to_producer: same_maintenance_conversation_after_research_review
    model_relation_to_producer: unknown
    provider_relation_to_producer: same_provider_as_maintainer_review
    criteria_fixed_before_exposure: true
    review_scope: bounded_upgrade_contract_candidate_against_merged_evidence_ledger_existing_template_hooks_and_user_goal
    evidence:
      - notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/02-unified-evidence-ledger.md
      - notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/03-decision-preparation.md
      - notes/target-project-memory-system-template-pack.md
    result_ref: notes/first-target-minimum-upgrade-contract-v0.1.md
    limitations:
      - candidate_not_heterogeneously_reviewed
      - no_real_target_pilot_evidence

human_adjudication:
  status: recorded
  actor: user
  decision: select_maintainer_recommended_next_route_for_candidate_preparation
  evidence:
    - class: direct_user_instruction
      ref: current_conversation_user_message_2026-07-28
      observed_or_accessed_at: 2026-07-28
      claim_scope: FIRST_TARGET_MINIMUM_UPGRADE_CONTRACT_route_selection
  limitations:
    - candidate_acceptance_and_any_template_or_target_use_remain_pending

lineage:
  review_disposition: amend
  reviews:
    - PR_216
    - RC-2026Q3-target-memory-governance-and-learning
  amends:
    - MNEMOSYNE_165_exact_archive_storage_completeness
    - research_cycle_canonical_path_pointers
    - post_merge_batch_live_status
  preserves:
    - all_four_report_bytes_and_dispositions
    - merged_unified_evidence_ledger
    - all_other_conversation_route_ownership
```

## 11. Boundary and safe next action

This task does not merge its PR, modify the execution source or target-project template pack, select a target project, create a target workspace, ingest target materials, write a target repository, implement migration, start adaptive-explanation/GPT Live research, close `HO-GUIDANCE-001`, or take over another conversation-owned route.

```yaml
safe_next_action:
  - human_review_and_merge_the_single_MNEMOSYNE_166_PR
  - then_review_and_record_one_user_disposition_for_FIRST_TARGET_MINIMUM_UPGRADE_CONTRACT_001
  - create_a_fresh_task_for_any_accepted_template_or_first_target_integration
```
