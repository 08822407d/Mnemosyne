# Fable F2 Cross-Repository Safe Concurrency Research — Current Status

```yaml
status_id: MNE-FABLE5-CROSS-REPOSITORY-CONCURRENCY-STATUS-001
created_by_task: MNEMOSYNE-214
last_updated_by_task: MNEMOSYNE-233
canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
display_name: MNE-DR-005 跨仓库并发
roadmap_priority: F2
status: A1_PACKAGE_004_DURABLE_EXECUTION_NOT_AUTHORIZED_HANDOFF_002_REHEARSAL_REQUIRED
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

  package_001:
    preserved_immutable: true
    candidate_blob: bb140196a38d8b14f6eba9e2175cd45744efb23b
    manifest_blob: 12a480449b1dac45cd265864a812f399d19ec15c

  package_002:
    preserved_immutable: true
    candidate_blob: a8b627b8aa74b5a1a5af19d3af485a17aa2cd0b7
    manifest_blob: 1f54f4711a44129c3dfee066aa2ab297f94718b7
    staged_model_binding_repair: accepted
    ready_for_G2A_as_written: false

  package_003:
    preserved_immutable: true
    candidate_blob: 28da6ab6a3f3638292e83a7df511100d8d23b4b0
    manifest_blob: 7611773d861e065f539118853ec93026515f4065
    wrapper_transport_and_three_way_comparison_repair: accepted
    ready_for_G2A_as_written: false

  package_003_source_identity_defect:
    id: MNE-V2A-A1-PACKAGE003-SOURCE-ARCHIVE-MANIFEST-IDENTITY-DEFECT-001
    blob: d9a35c0a6691689a50be821e0783b00dc9904eb2
    incorrect_blob: 7c2af723c395283aca23a5240847e46e6c97e93b
    actual_blob: 6e90c8f1384657939d5dcd9e7e30177e3c2e7b2a
    underlying_archive_corruption_observed: false
    A1_runtime_failure: false

  package_004:
    id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-004
    candidate_blob: 87f110c5f99ba702a93cd38ca78bb6bfbff002db
    manifest_blob: 8a978e1a075674e9f6d3909a1530c483abaf428d
    required_file_count: 6
    role: additive_source_identity_and_handoff_publication_closure_repair
    independent_archive_reconstruction_receipt_blob: 47a8a5508000135ea267814b9e0d0e564558e230
    source_original_bytes: 37074
    source_original_sha256: 6e639f7b49c8bfd6d47e950a7eb6cce54cf41c07903fb57fae3d0a29b7c2a4e0
    packages_001_002_003_preserved: true

  execution_authorized: false
  G2A_issued: false
  controller_or_worker_launched: false
  validation_repository_written: false
  A1_branches_created: false
```

## Corrected handoff and mandatory rehearsal

```yaml
handoff_002:
  package_id: MNE-F2-V2A-A1-WRAPPER-REPAIR-HANDOFF-002
  package_path: handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-handoff-package-002.md
  package_blob: 30699edcf16228f931f89e9162b2f9bc08d4c4c7
  startup_path: handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-startup-prompt-002.md
  startup_blob: 868974dbc497da689aac48a5768a6de7e1de68b8
  rehearsal_contract_path: handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-post-merge-receive-rehearsal-contract-001.md
  rehearsal_contract_blob: 1cb2f56ca4501040b5e2784e4ad46f58b690b94e
  route_release_before_receive_rehearsal_PASS: false
  failed_pre_repair_receiver_conversations_reused: false
  guidance_load_during_receive: false

handoff_correctness_hardening_todo:
  path: notes/todos/MNE-HANDOFF-CORRECTNESS-VALIDATION-AND-PROTOCOL-HARDENING-TODO-001.md
  blob: fd231986dab84d77f265264f599c98d64a91dbfd
  status: todo_after_current_F2_handoff_succeeds
  generic_guidance_modified_by_MNEMOSYNE_233: false
```

## Current gate

```text
merge Package 004 / handoff 002 repair PR
→ exact merge-commit path/blob readback
→ mandatory fresh receive-only rehearsal
→ originating conversation accepts receive report
→ receiver loads Mnemosyne guidance as a separate operation
→ fresh Pro execution-time review of packages 004/003/002/001
→ separate Owner A1 controller G2A
```

No current record authorizes:

```yaml
A1_execution: false
A2_to_A7_execution: false
V2_B_execution: false
V2_C_execution: false
validation_repository_write: false
Meta_Agent_or_real_target_write: false
generic_handoff_guidance_modification: false
conversation_export_or_Pro_Fable_handoff_audit_execution: false
automatic_retry_repair_cleanup_or_branch_deletion: false
```
