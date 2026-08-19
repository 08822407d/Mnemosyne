# F2 V2-A A1 Handoff 002 Receive-Schema / Rehearsal-Oracle Mismatch 001

```yaml
defect_id: MNE-F2-V2A-A1-HANDOFF002-RECEIVE-SCHEMA-ORACLE-MISMATCH-001
task_id: MNEMOSYNE-234
classification: route_specific_handoff_protocol_contract_defect
severity: material_pre_rehearsal_blocker
receiver_fault: false
Package_004_source_identity_fault: false
A1_runtime_failure: false
validation_repository_affected: false
```

## Observed mismatch

Handoff Package 002 required a `mnemosyne_handoff_receive` object with fields including:

```text
package_id
package_blob_match
candidate_004
package_004_manifest
source_archive_manifest
archive_reconstruction_receipt
A1_status
receiver_guidance_load
current_task_from_package
```

Post-Merge Receive-Rehearsal Contract 001's exact acceptance block independently required fields including:

```text
package_id_exact
package_blob
candidate_004_blob
package_004_manifest_blob
source_archive_manifest_blob
archive_reconstruction_receipt_blob
A1_execution_authorized
A1_executed
A1_validation_branches_created
validation_repository_written
guidance_loaded_during_receive
repository_or_service_writes_during_receive
```

The two artifacts did not freeze an authoritative field mapping, type mapping or object-vs-scalar normalization. `execution_time_master` was required in the receive report but not represented in the exact acceptance YAML block.

A receiver could therefore comply with Handoff Package 002 and still produce a report that a mechanical application of Rehearsal Contract 001 would reject for missing differently named fields. Resolving aliases by model interpretation would defeat the stated mechanical-oracle objective.

## Affected artifacts

```yaml
handoff_package_002:
  path: handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-handoff-package-002.md
  blob: 30699edcf16228f931f89e9162b2f9bc08d4c4c7
startup_prompt_002:
  path: handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-startup-prompt-002.md
  blob: 868974dbc497da689aac48a5768a6de7e1de68b8
rehearsal_contract_001:
  path: handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-post-merge-receive-rehearsal-contract-001.md
  blob: 1cb2f56ca4501040b5e2784e4ad46f58b690b94e
```

## Non-defects preserved

This finding does not invalidate:

- candidate/package 004 source-archive identity correction;
- canonical archive manifest blob `6e90c8f1384657939d5dcd9e7e30177e3c2e7b2a`;
- independent five-part reconstruction receipt;
- Package 003 worker-wrapper transport/three-way comparison;
- Package 002 staged model binding;
- Package 001 fixture/effect/order/ten-output semantics.

## Required repair

Create a route-specific canonical receive-report schema and make Handoff Package 003 and Rehearsal Contract 002 consume that same schema path/blob. Startup Prompt 003 must identify the same schema and exact Handoff Package 003.

No Package 005 is required or authorized. Handoff Packages 001–002, Startup Prompts 001–002 and Rehearsal Contract 001 remain immutable historical evidence.

## Stop condition

If a complete repair requires changing Package 004 or its A1 execution semantics, stop and return to Pro adjudication rather than expanding scope.
