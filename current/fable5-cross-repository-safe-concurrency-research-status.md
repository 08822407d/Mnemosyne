# Fable F2 Cross-Repository Safe Concurrency Research — Current Status

```yaml
status_id: MNE-FABLE5-CROSS-REPOSITORY-CONCURRENCY-STATUS-001
created_by_task: MNEMOSYNE-214
last_updated_by_task: MNEMOSYNE-242
canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
display_name: MNE-DR-005 跨仓库并发
roadmap_priority: F2
status: A1_READINESS_PASS_CORRECTED_G2A_TEMPLATE_PUBLISHED_VIA_PR_303_PENDING_SEPARATE_OWNER_G2A_DECISION
```

## Preserved F2 and A0 state

```yaml
Fable_report_received: true
fresh_Pro_F2_adjudication_completed: true
Owner_F2_option_A_accepted: true
V2_staged_design_prepared: true
V2_A_A0:
  executed: true
  controller_branch: v2a-sentinel-001-controller
  final_head: d936cd2d4acd3f5b71f6f7f0d86ae6ffe93ab58c
  Owner_accepted_disposition: PASS_WITH_BOUNDED_EVIDENCE_DEFECTS
  rerun_required: false
  historical_outputs_rewritten: false
```

## V2-A A1 package lineage

```yaml
V2_A_A1:
  run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
  package_001: {preserved_immutable: true, candidate_blob: bb140196a38d8b14f6eba9e2175cd45744efb23b, manifest_blob: 12a480449b1dac45cd265864a812f399d19ec15c}
  package_002: {preserved_immutable: true, candidate_blob: a8b627b8aa74b5a1a5af19d3af485a17aa2cd0b7, manifest_blob: 1f54f4711a44129c3dfee066aa2ab297f94718b7, staged_model_binding_repair: accepted, ready_for_G2A_as_written: false}
  package_003: {preserved_immutable: true, candidate_blob: 28da6ab6a3f3638292e83a7df511100d8d23b4b0, manifest_blob: 7611773d861e065f539118853ec93026515f4065, wrapper_transport_and_three_way_comparison_repair: accepted, ready_for_G2A_as_written: false}
  package_004:
    preserved_immutable: true
    id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-004
    candidate_blob: 87f110c5f99ba702a93cd38ca78bb6bfbff002db
    manifest_blob: 8a978e1a075674e9f6d3909a1530c483abaf428d
    role: additive_source_identity_and_handoff_publication_closure_repair
    independent_archive_reconstruction_receipt_blob: 47a8a5508000135ea267814b9e0d0e564558e230
    source_original_bytes: 37074
    source_original_sha256: 6e639f7b49c8bfd6d47e950a7eb6cce54cf41c07903fb57fae3d0a29b7c2a4e0
  package_005_created: false
  execution_authorized: false
  G2A_issued: false
  controller_or_worker_launched: false
  validation_repository_written: false
  A1_branches_created: false
```

## Handoff 003 behavioral state

```yaml
handoff_003:
  package_id: MNE-F2-V2A-A1-WRAPPER-REPAIR-HANDOFF-003
  package_blob: bb60b9c18acb9035491eeb3af5e521fe14714ddb
  startup_blob: 76db593d8c3a62a7ff8e90a32f418d8ad3bfe0ad
  canonical_schema_blob: 52e2ce60f471be492175f8725a0ed39ddf3daad1
  rehearsal_contract_blob: d8c07a69d03173b85c644628ef4aa497c871e8e7
  receive_rehearsal_run: true
  guidance_loaded_in_receiver: true
handoff_003_behavioral_evidence:
  receive_only_phase_exercised: true
  separate_guidance_phase_exercised: true
  transferred_task_preserved: true
  substantive_continuation_separately_authorized: true
  originating_oracle_transcript_durably_archived: false
  disposition: POSITIVE_BEHAVIORAL_EXERCISE_WITH_ARCHIVAL_LIMITATION
```

## Fresh Pro A1 readiness and G2A composition

```yaml
fresh_Pro_A1_readiness:
  adjudication_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-004-FRESH-PRO-READINESS-ADJUDICATION-001
  package_lineage: 004_003_002_001
  disposition: PASS_RETURN_TO_OWNER_GATE
  G2A_issued: false
G2A_composition_closure:
  Fable_task: WORK-ULTRA-FABLE-MNE-DR-005-G2A-COMPOSITE-CLOSURE-001
  Fable_candidate_sha256: e51af7f7c175bf9ce43171a56921f77a51dfe5d05cff973ae4f05ceadf3a2516
  Fable_candidate_direct_issue_status: BLOCKED_MATERIAL_NONAUTHORIZATION_TRANSFORMATION_DEFECT
  Pro_adjudication_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-COMPOSITE-G2A-PRO-ADJUDICATION-001
  Pro_corrected_template_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-CONTROLLER-G2A-ISSUANCE-TEMPLATE-CANDIDATE-001
  template_publication_complete: true
  template_publication_carrier_task: MNEMOSYNE-241
  template_publication_PR: 303
  published_template_blob: da36d22f35a2614dd9bb0a4f7030b73e7be27fb0
  post_merge_template_blob_readback_complete: true
  post_merge_template_blob_readback_task: MNEMOSYNE-242
  dynamic_fill_and_validator_required: true
  separate_Owner_G2A_required: true
  G2A_issued: false
  A1_execution_authorized: false
```

## Publication result (PR #303)

```yaml
publication_result:
  publication_carrier_task: MNEMOSYNE-241
  PR: 303
  PR_state: closed
  merged: true
  merged_at: 2026-08-21T01:24:47Z
  PR_head_branch: mnemosyne-241-f2-g2a-handoff-hval-publication
  PR_head_sha: 2a361d0c91ab54102d4243ca6bbd219e649e3175
  base_before_merge: e726dea818dca9418181775d0e7dcd62eb6c464a
  merge_commit: 3ea2b97c369837d27d0e4a65c38c252e755954b5
  master_tree: f0cf511069eb9ec9be83579766c3990e89976100
  PR_commits: 1
  changed_paths: 91
  additions: 87
  modifications: 4
  publication_complete: true
  post_merge_path_and_blob_readback_complete: true
  readback_task: MNEMOSYNE-242
```

```yaml
merged_artifact_identities:
  corrected_G2A_template:
    path: notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-CONTROLLER-G2A-ISSUANCE-TEMPLATE-CANDIDATE-001.md
    blob: da36d22f35a2614dd9bb0a4f7030b73e7be27fb0
    declared_sha256: ae3c2f7a4d56195eec9faa99c2041404718d1d557c20a3d13ea56a66fe252265
    authority: non_authorizing_outer_template
  G2A_template_manifest:
    path: notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-CONTROLLER-G2A-ISSUANCE-TEMPLATE-MANIFEST-001.yaml
    blob: 53269416730b21243d083acb40930a8d5352f2c6
  mechanical_validator:
    path: notes/validation-tools/validate_and_fill_mne_v2a_a1_controller_g2a.py
    blob: d17b47821a61aaa8d97df9a6541db1576631bcfc
  HVAL_design_002:
    path: notes/validation-designs/MNE-HVAL-001-PRO-CORRECTED-VALIDATION-DESIGN-002.md
    blob: 260f9bafefc6eadeae28b2e440433399d31c2d10
    status: DESIGNED_NOT_EXECUTED_ACCEPTED_FOR_SEPARATE_OWNER_AUTHORIZATION
```

Publication of the corrected outer template does not authorize anything. The post-merge invariants below are unchanged by the merge.

```yaml
post_merge_invariants:
  G2A_issued: false
  A1_execution_authorized: false
  controller_or_worker_launched: false
  validation_repository_written: false
  validation_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  validation_repository_master: e8e3296922185b4b70997c2351d6f39423f2cd4f
  A1_branches_created: false
  HVAL_fixture_publication_authorized: false
  HVAL_scenario_execution_authorized: false
```

## Publication incidents and recovery

```yaml
publication_closeout:
  MNEMOSYNE_235: BLOCKED_CLOSED_NO_RETRY
  MNEMOSYNE_236: BLOCKED_CLOSED_NO_RETRY
  MNEMOSYNE_237: BLOCKED_CLOSED_NO_RETRY
  MNEMOSYNE_238: BLOCKED_CLOSED_NO_RETRY
  MNEMOSYNE_239: BLOCKED_CLOSED_NO_RETRY
  MNEMOSYNE_240: HISTORICAL_RECOVERY_ARCHITECTURE_AND_DURABLE_STAGING_CAPSULE_SOURCE_NOT_THE_PUBLICATION_CARRIER
  MNEMOSYNE_241: PUBLICATION_CARRIER_SUCCEEDED_MERGED_AS_PR_303
  forensic_audit: DUAL_FAILURE_PARTIAL_CAUSE_RECOVERY_ARCHITECTURE_READY_WITH_UNKNOWNS
  Pro_forensic_adjudication: MNE-235-236-DUAL-FAILURE-FORENSIC-PRO-ADJUDICATION-001
  execution_surface_adjudication_237_238: MNE-MNEMOSYNE-237-238-EXECUTION-SURFACE-PRO-ADJUDICATION-001
  execution_surface_adjudication_239: MNE-MNEMOSYNE-239-EXECUTION-SURFACE-PRO-ADJUDICATION-001
  selected_architecture: UBUNTU_24_04_LOCAL_DETERMINISTIC_GIT_PHASE_A_THEN_ORIGINATING_CONNECTOR_READY_PR
  recovery_task: MNEMOSYNE-240
  planned_publication_branch_not_used: mnemosyne-240-f2-g2a-and-handoff-audit-closeout
  actual_publication_branch: mnemosyne-241-f2-g2a-handoff-hval-publication
  historical_incident_lineage: MNEMOSYNE_235_through_MNEMOSYNE_240_retained_as_history
  mnemosyne_235_branch_disposition: MAY_DELETE_no_unique_unpreserved_work
  mnemosyne_235_branch_observed_at_MNEMOSYNE_242: absent_on_origin
  mnemosyne_240_preservation_capsule_branch: RETAIN_pending_immutable_canonical_substitute_or_Owner_archival_decision
  prior_unreferenced_objects_reused: false
  cleanup_authorized: false
```

## Current gate

```text
prepare only the authorized dynamic G2A values from current direct evidence
→ run the merged mechanical validator notes/validation-tools/validate_and_fill_mne_v2a_a1_controller_g2a.py
→ obtain a separate explicit Owner decision whether to issue the A1 controller G2A
→ only after an actual Owner G2A: fresh controller preflight, then Package 001–004 execution flow
```

The publication steps of the previous gate are complete and are recorded above as history. MNEMOSYNE-240 is no longer an executable instruction on this route.

No current record authorizes:

```yaml
A1_execution: false
A2_to_A7_execution: false
V2_B_execution: false
V2_C_execution: false
validation_repository_write: false
Meta_Agent_or_real_target_write: false
generic_handoff_command_or_guard_modification: false
MNE_HVAL_fixture_publication_or_execution: false
conversation_export_or_god_view_study: false
automatic_retry_repair_cleanup_or_branch_deletion: false
```
