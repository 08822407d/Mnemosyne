# F2 / V2-A A1 Package 004 — Mandatory Post-Merge Receive-Rehearsal Contract 001

```yaml
rehearsal_contract_id: MNE-F2-V2A-A1-HANDOFF-002-POST-MERGE-RECEIVE-REHEARSAL-001
prepared_by_task: MNEMOSYNE-233
status: required_before_originating_conversation_release
execution_source: false
repository_write_authorized: false
A1_execution_authorized: false
```

## Canonical inputs

```yaml
handoff_package:
  path: handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-handoff-package-002.md
  blob: 30699edcf16228f931f89e9162b2f9bc08d4c4c7
  package_id: MNE-F2-V2A-A1-WRAPPER-REPAIR-HANDOFF-002
startup_prompt:
  path: handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-startup-prompt-002.md
  blob: 868974dbc497da689aac48a5768a6de7e1de68b8
receive_report_key: mnemosyne_handoff_receive
candidate_004_blob: 87f110c5f99ba702a93cd38ca78bb6bfbff002db
package_004_manifest_blob: 8a978e1a075674e9f6d3909a1530c483abaf428d
package_004_file_count: 6
canonical_archive_manifest_blob: 6e90c8f1384657939d5dcd9e7e30177e3c2e7b2a
independent_reconstruction_receipt_blob: 47a8a5508000135ea267814b9e0d0e564558e230
source_original_sha256: 6e639f7b49c8bfd6d47e950a7eb6cce54cf41c07903fb57fae3d0a29b7c2a4e0
```

The startup text supplied to the receiver must be copied from the final merged startup artifact. Do not manually retype or restate it.

## Required timing

1. merge the repair Ready PR;
2. read back the canonical package/startup/rehearsal and all load-bearing identities from the merge commit/current master;
3. open a completely fresh ChatGPT conversation with GitHub read access;
4. send the exact merged startup prompt once;
5. receiver emits only `mnemosyne_handoff_receive` and stops;
6. return the complete receiver report to the originating conversation;
7. originating conversation adjudicates with the exact oracle below;
8. only after explicit `REHEARSAL_ACCEPTED_RECEIVER_MAY_LOAD_GUIDANCE` send `加载 Mnemosyne 指导约束` in the receiver;
9. receiver must output `mnemosyne_guidance_refresh` and confirm the received F2 task remained preserved;
10. only then may the originating conversation retire.

The two failed pre-repair receiver attempts are evidence; neither conversation is reused for the new rehearsal.

## Mechanical acceptance oracle

All must be true:

```yaml
handoff_receive_status: RECEIVED
identity_verification_status: PASS
package_present: true
package_id_exact: true
package_blob: 30699edcf16228f931f89e9162b2f9bc08d4c4c7
candidate_004_blob: 87f110c5f99ba702a93cd38ca78bb6bfbff002db
package_004_manifest_blob: 8a978e1a075674e9f6d3909a1530c483abaf428d
package_004_file_count: 6
source_archive_manifest_blob: 6e90c8f1384657939d5dcd9e7e30177e3c2e7b2a
archive_reconstruction_receipt_blob: 47a8a5508000135ea267814b9e0d0e564558e230
source_original_sha256: 6e639f7b49c8bfd6d47e950a7eb6cce54cf41c07903fb57fae3d0a29b7c2a4e0
A1_execution_authorized: false
A1_executed: false
A1_validation_branches_created: false
validation_repository_written: false
guidance_loaded_during_receive: false
repository_or_service_writes_during_receive: []
current_task_from_package: package_004_fresh_Pro_execution_time_readiness_review
substantive_continuation_status: BLOCKED_PENDING_REHEARSAL_ACCEPTANCE_AND_GUIDANCE
```

No extra route, silent expected-value refresh, artifact substitution, package repair, G2A or execution may appear.

## Capability split

A next-tier originating conversation may apply the exact oracle above and return either:

```yaml
rehearsal_disposition: REHEARSAL_ACCEPTED_RECEIVER_MAY_LOAD_GUIDANCE
```

or:

```yaml
rehearsal_disposition: BLOCKED_REQUIRES_PRO
```

Any missing, unknown, unexpected or conflicting field requires at most one Pro adjudication turn to identify the main blocker and root-cause class.

## Guidance completion check

After accepted rehearsal, the receiver's separate guidance-load response must confirm:

```yaml
mnemosyne_guidance_refresh:
  operation: behavior_constraint_refresh
  current_conversation_task_preserved: true
  handoff_started: false
  maintenance_live_route_imported: false
  execution_source: current/human-approved-spec.md
```

It must also state that the local task remains the Package 004 fresh-Pro readiness route and that A1 remains unauthorized.

## Boundaries

This rehearsal does not authorize repository writes, Package 004 review execution before guidance, G2A, A1, later cells, cleanup or route import.
