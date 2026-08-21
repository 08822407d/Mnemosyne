# Fable F2 Cross-Repository Safe Concurrency Research — Current Status

```yaml
status_id: MNE-FABLE5-CROSS-REPOSITORY-CONCURRENCY-STATUS-001
created_by_task: MNEMOSYNE-214
last_updated_by_task: MNEMOSYNE-240
canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
display_name: MNE-DR-005 跨仓库并发
roadmap_priority: F2
status: A1_READINESS_PASS_CORRECTED_G2A_TEMPLATE_PUBLICATION_PENDING_MNEMOSYNE_240_READY_PR
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
  template_publication_required: true
  post_merge_template_blob_readback_required: true
  dynamic_fill_and_validator_required: true
  separate_Owner_G2A_required: true
  G2A_issued: false
  A1_execution_authorized: false
```

## Publication incidents and recovery

```yaml
publication_closeout:
  MNEMOSYNE_235: BLOCKED_CLOSED_NO_RETRY
  MNEMOSYNE_236: BLOCKED_CLOSED_NO_RETRY
  MNEMOSYNE_237: BLOCKED_CLOSED_NO_RETRY
  MNEMOSYNE_238: BLOCKED_CLOSED_NO_RETRY
  MNEMOSYNE_239: BLOCKED_CLOSED_NO_RETRY
  forensic_audit: DUAL_FAILURE_PARTIAL_CAUSE_RECOVERY_ARCHITECTURE_READY_WITH_UNKNOWNS
  Pro_forensic_adjudication: MNE-235-236-DUAL-FAILURE-FORENSIC-PRO-ADJUDICATION-001
  execution_surface_adjudication_237_238: MNE-MNEMOSYNE-237-238-EXECUTION-SURFACE-PRO-ADJUDICATION-001
  execution_surface_adjudication_239: MNE-MNEMOSYNE-239-EXECUTION-SURFACE-PRO-ADJUDICATION-001
  selected_architecture: UBUNTU_24_04_LOCAL_DETERMINISTIC_GIT_PHASE_A_THEN_ORIGINATING_CONNECTOR_READY_PR
  recovery_task: MNEMOSYNE-240
  publication_branch: mnemosyne-240-f2-g2a-and-handoff-audit-closeout
  historical_empty_branch_retained: mnemosyne-235-f2-g2a-and-handoff-audit-closeout
  prior_unreferenced_objects_reused: false
  cleanup_authorized: false
```

## Current gate

```text
execute MNEMOSYNE-240 from the single Ubuntu operator package; automated preflight occurs before the one-shot Phase A begins
→ exact post-push branch readback by the originating Pro conversation
→ originating conversation creates one Ready PR from the frozen PR body
→ Owner reviews and decides whether to merge
→ exact post-merge readback of the corrected G2A template, manifest, validator and route status
→ fill only authorized dynamic fields and run the mechanical validator
→ separate explicit Owner decision whether to issue the A1 controller G2A
→ only after actual Owner G2A: fresh controller preflight and Package 001–004 execution flow
```

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
