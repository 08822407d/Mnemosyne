# Mnemosyne F2 / V2-A A1 Wrapper-Verification Repair — Handoff Package 003

```yaml
handoff_package_id: MNE-F2-V2A-A1-WRAPPER-REPAIR-HANDOFF-003
package_tier: route_specific_schema_oracle_repair
package_status: non_execution_source_transfer_artifact
prepared_by_task: MNEMOSYNE-234
route: FABLE5_MNE_CROSS_REPOSITORY_SAFE_CONCURRENCY_F2_V2A_A1
handoff_status: PREPARED_REQUIRES_POST_MERGE_RECEIVE_REHEARSAL
source_base_master: cc06e929515e6bcae8f4997cc6bb6e165bcdd151
execution_source: current/human-approved-spec.md
handoff_is_execution_source: false
intended_receiver: completely_fresh_ChatGPT_Pro_conversation_with_GitHub_read_access
intended_receiver_action: receive_only_emit_exact_schema_report_then_stop
```

Handoff Package 003 supersedes Handoff Package 002 only for future route transfer. Handoff Packages 001–002, Startup Prompts 001–002 and Rehearsal Contract 001 remain immutable historical evidence. Candidate/packages 001–004 are unchanged.

## Canonical report schema

The receiver must emit exactly one top-level `mnemosyne_handoff_receive` object conforming to:

```yaml
schema_id: MNE-F2-V2A-A1-HANDOFF-RECEIVE-REPORT-SCHEMA-001
schema_path: handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-receive-report-schema-001.md
schema_blob: 52e2ce60f471be492175f8725a0ed39ddf3daad1
```

The schema defines the only authorized field paths, types and comparison semantics. Do not rename, flatten, alias or supplement it with a second receive-report schema.

The one schema-defined self-reference exception is `mnemosyne_handoff_receive.package.blob.expected`: Handoff Package 003 cannot embed its own Git blob. The exact merged Startup Prompt 003 supplies that one expected value after this package blob is known.

## Receiver guidance contract

Expected values for the canonical schema:

```yaml
receiver_guidance_load.project_guidance.expected: not_applicable
receiver_guidance_load.mnemosyne_guidance.expected: required
receiver_guidance_load.loaded_during_receive.expected: false
```

Guidance is not loaded during receive. After a successful receive-only rehearsal, the receiver must stop and return the exact report to the originating conversation. Only explicit rehearsal acceptance may authorize the later, separate guidance-refresh operation.

## Exact expected values for canonical schema

The following dotted paths are the authoritative source for every static `expected` value except `package.blob.expected`, which comes only from exact merged Startup Prompt 003.

```yaml
report_schema.id.expected: MNE-F2-V2A-A1-HANDOFF-RECEIVE-REPORT-SCHEMA-001
report_schema.path.expected: handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-receive-report-schema-001.md
report_schema.blob.expected: 52e2ce60f471be492175f8725a0ed39ddf3daad1

execution_time_master.repository.expected: 08822407d/Mnemosyne
execution_time_master.branch.expected: master

package.present.expected: true
package.path.expected: handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-handoff-package-003.md
package.id.expected: MNE-F2-V2A-A1-WRAPPER-REPAIR-HANDOFF-003
package.status.expected: non_execution_source_transfer_artifact

execution_source.path.expected: current/human-approved-spec.md
execution_source.blob.expected: 01f64a8223677829320c66dd46d3f172cc9155cc

supporting_commands.handoff_receive_command.path.expected: commands/receive-mnemosyne-handoff.md
supporting_commands.handoff_receive_command.blob.expected: fa7fd7d31fdfd1663ea328db6c82e5c3a7b46cde
supporting_commands.guidance_load_command.path.expected: commands/load-mnemosyne-guidance.md
supporting_commands.guidance_load_command.blob.expected: 1124c2e058bba339688641c45ddf18a65f97e1ef

identities.candidate_004.path.expected: notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-004.md
identities.candidate_004.blob.expected: 87f110c5f99ba702a93cd38ca78bb6bfbff002db
identities.package_004_manifest.path.expected: notes/cross-repository-safe-concurrency-v2a-a1-execution-package-004/01-package-and-source-manifest.md
identities.package_004_manifest.blob.expected: 8a978e1a075674e9f6d3909a1530c483abaf428d
identities.source_archive_manifest.path.expected: raw/validation-reviews/MNE-DR-005-A1-package002-readiness-review/exact-source/source-artifact-receipt-and-reconstruction-manifest.yaml
identities.source_archive_manifest.blob.expected: 6e90c8f1384657939d5dcd9e7e30177e3c2e7b2a
identities.archive_reconstruction_receipt.path.expected: notes/cross-repository-safe-concurrency-v2a-a1-execution-package-004/02-independent-archive-reconstruction-and-identity-receipt.md
identities.archive_reconstruction_receipt.blob.expected: 47a8a5508000135ea267814b9e0d0e564558e230

package_004_file_count.expected: 6
source_review.original_bytes.expected: 37074
source_review.original_sha256.expected: 6e639f7b49c8bfd6d47e950a7eb6cce54cf41c07903fb57fae3d0a29b7c2a4e0

A1_status.execution_authorized.expected: false
A1_status.executed.expected: false
A1_status.G2A_issued.expected: false
A1_status.controller_or_worker_launched.expected: false
A1_status.validation_branches_created.expected: false
A1_status.validation_repository_written.expected: false

repository_or_service_writes_during_receive.expected: []
current_task_from_package.task_id.expected: package_004_fresh_Pro_execution_time_readiness_review

safe_next_action.expected: return_complete_receive_report_to_originating_conversation_for_rehearsal_acceptance
```

Canonical ordered forbidden-action list:

```yaml
forbidden_actions.expected:
  - do_not_load_guidance_during_receive
  - do_not_run_substantive_readiness_review
  - do_not_issue_G2A
  - do_not_execute_A1
  - do_not_create_or_move_validation_branches
  - do_not_modify_packages_or_expected_values
  - do_not_write_any_repository_or_connected_service
  - do_not_import_unrelated_routes
  - do_not_read_cold_originals_without_mismatch_trigger
  - do_not_retry_blocked_receive
  - do_not_use_Web_Deep_Research_Fable_other_Apps_private_material_or_external_quota
```

## Required receive evidence

Read only the minimum evidence needed to populate the canonical schema:

1. `commands/receive-mnemosyne-handoff.md`;
2. this package;
3. the canonical schema path/blob;
4. `current/human-approved-spec.md` only for execution-source identity;
5. `commands/load-mnemosyne-guidance.md` only for its expected identity; do not execute it;
6. candidate 004;
7. Package 004 manifest and six-file directory listing;
8. canonical source archive manifest;
9. Package 004 independent reconstruction receipt;
10. current F2 state and validation branch/PR state only as needed to establish the A1 fields.

Do not read the five cold archive parts or the old full review unless a mismatch specifically requires them.

## Successful receive-state constants

A successful receive-only report uses exactly:

```yaml
handoff_receive_status: RECEIVED
identity_verification_status: PASS
substantive_continuation_status: BLOCKED_PENDING_REHEARSAL_ACCEPTANCE_AND_GUIDANCE
```

Every canonical `exact_match` field must be `true`, all required fields must be present, `repository_or_service_writes_during_receive.actual` must be exactly `[]`, and `execution_time_master.unchanged_during_receive_check` must be `true`.

The originating conversation additionally applies the canonical schema's dynamic execution-time-master comparison rule. Do not freeze or infer a pre-publication master SHA.

## Current task transferred

```yaml
current_task_from_package:
  task_id: package_004_fresh_Pro_execution_time_readiness_review
  description: perform a fresh Pro execution-time readiness review of Package 004 and inherited Packages 003/002/001 after accepted receive rehearsal and separate Mnemosyne guidance refresh
  current_gate: post_merge_receive_rehearsal_then_guidance_refresh
  on_ready: return_to_Owner_gate_without_issuing_G2A
```

## Forbidden automatic actions

The canonical forbidden-action list above is controlling. In particular, receive does not authorize guidance loading, substantive readiness review, G2A, A1, validation writes, package repair, expected-value refresh, retry, external research or unrelated route import.

## Safe next action

Return the complete canonical-schema receive report to the originating conversation and stop. No substantive continuation occurs until the originating conversation explicitly accepts the rehearsal and separately authorizes guidance refresh.
