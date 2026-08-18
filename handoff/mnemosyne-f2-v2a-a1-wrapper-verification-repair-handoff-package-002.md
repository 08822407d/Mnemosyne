# Mnemosyne F2 / V2-A A1 Wrapper-Verification and Source-Identity Repair — Handoff Package 002

```yaml
handoff_package_id: MNE-F2-V2A-A1-WRAPPER-REPAIR-HANDOFF-002
package_tier: route_specific_corrected
package_status: non_execution_source_transfer_artifact
prepared_by_task: MNEMOSYNE-233
route: FABLE5_MNE_CROSS_REPOSITORY_SAFE_CONCURRENCY_F2_V2A_A1
handoff_status: PREPARED_REQUIRES_POST_MERGE_RECEIVE_REHEARSAL
source_branch: mnemosyne-233-v2a-a1-package004-handoff-repair
source_base_master: b70acfc8ab190f18fdd987f034963039728ca887
execution_source: current/human-approved-spec.md
handoff_is_execution_source: false
intended_receiver: fresh_ChatGPT_Pro_conversation_with_GitHub_read_access
intended_receiver_action: receive_only_then_stop
```

The originating conversation remains responsible until the post-merge receive rehearsal passes. This package replaces handoff package 001 for future use; package 001 remains immutable historical evidence.

## Receiver guidance contract

```yaml
receiver_guidance_load:
  project_guidance: not_applicable
  mnemosyne_guidance: required
  ordered_operations:
    - receive_authorized_handoff_package_002
    - emit_mnemosyne_handoff_receive_report
    - stop_and_return_report_to_originating_conversation
    - wait_for_explicit_rehearsal_acceptance
    - execute_Load_Mnemosyne_guidance_as_separate_operation
    - emit_mnemosyne_guidance_refresh
    - confirm_received_F2_task_preserved
    - continue_only_after_all_prerequisites
```

Guidance is not loaded during receive. The broader future design requirement for self-loading guidance in one startup flow is recorded separately as a TODO and is not implemented here.

## Exact source identities

```yaml
execution_source:
  path: current/human-approved-spec.md
  blob: 01f64a8223677829320c66dd46d3f172cc9155cc
handoff_receive_command:
  path: commands/receive-mnemosyne-handoff.md
  blob: fa7fd7d31fdfd1663ea328db6c82e5c3a7b46cde
guidance_load_command:
  path: commands/load-mnemosyne-guidance.md
  blob: 1124c2e058bba339688641c45ddf18a65f97e1ef
source_identity_defect:
  path: notes/validation-protocol-defects/MNE-V2A-A1-PACKAGE003-SOURCE-ARCHIVE-MANIFEST-IDENTITY-DEFECT-001.md
  blob: d9a35c0a6691689a50be821e0783b00dc9904eb2
run_decision_candidate_004:
  path: notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-004.md
  blob: 87f110c5f99ba702a93cd38ca78bb6bfbff002db
package_004_manifest:
  path: notes/cross-repository-safe-concurrency-v2a-a1-execution-package-004/01-package-and-source-manifest.md
  blob: 8a978e1a075674e9f6d3909a1530c483abaf428d
package_004_file_count: 6
source_archive_manifest:
  path: raw/validation-reviews/MNE-DR-005-A1-package002-readiness-review/exact-source/source-artifact-receipt-and-reconstruction-manifest.yaml
  blob: 6e90c8f1384657939d5dcd9e7e30177e3c2e7b2a
independent_archive_reconstruction_receipt:
  path: notes/cross-repository-safe-concurrency-v2a-a1-execution-package-004/02-independent-archive-reconstruction-and-identity-receipt.md
  blob: 47a8a5508000135ea267814b9e0d0e564558e230
source_review_original_bytes: 37074
source_review_original_sha256: 6e639f7b49c8bfd6d47e950a7eb6cce54cf41c07903fb57fae3d0a29b7c2a4e0
```

Packages 001–003 remain preserved and control all non-delta semantics.

## Current task transferred

```yaml
current_task_from_package:
  task: perform_fresh_Pro_execution_time_readiness_review_of_packages_004_003_002_001
  current_gate: post_merge_receive_rehearsal_then_guidance_refresh
  review_must_verify:
    - Package_004_source_identity_correction
    - Package_003_wrapper_transport_and_three_way_comparison
    - inherited_Package_002_model_binding
    - inherited_Package_001_fixture_effect_order_and_ten_output_contract
    - then_current_refs_branches_PRs_tool_and_model_surface
  on_ready: return_to_Owner_gate_without_issuing_G2A
```

## Minimum receive evidence

Read only:

1. `commands/receive-mnemosyne-handoff.md`;
2. this package;
3. candidate 004;
4. Package 004 manifest and six-file directory;
5. the canonical archive-manifest path and Package 004 reconstruction receipt;
6. current F2 status only as needed to confirm A1 remains unauthorized;
7. no cold archive parts or old full review unless a mismatch specifically requires them.

Do not require current `master` to equal `b70acfc8ab190f18fdd987f034963039728ca887`. Publication moves `master`; validity is based on current-master presence and exact path/blob identities.

## Required receive report

Output one `mnemosyne_handoff_receive` object with at least:

```yaml
handoff_receive_status: RECEIVED | BLOCKED_PACKAGE_ABSENT | BLOCKED_PACKAGE_ID_MISMATCH
identity_verification_status: PASS | BLOCKED_LOAD_BEARING_IDENTITY_MISMATCH | INCOMPLETE
package_present:
package_id:
package_blob_match:
execution_time_master:
candidate_004:
package_004_manifest:
package_004_file_count:
source_archive_manifest:
archive_reconstruction_receipt:
A1_status:
receiver_guidance_load:
current_task_from_package:
forbidden_actions:
substantive_continuation_status:
safe_next_action:
limitations_or_unknowns:
```

A successful receive still uses:

```yaml
substantive_continuation_status: BLOCKED_PENDING_REHEARSAL_ACCEPTANCE_AND_GUIDANCE
```

The receiver must stop and the Owner must return the complete report to the originating conversation.

## Forbidden automatic actions

Do not:

- load guidance during receive;
- perform the Package 004 substantive readiness review;
- issue G2A;
- create or move validation branches;
- execute controller, workers or A1;
- modify packages or expected values;
- write any repository;
- import unrelated routes;
- read cold originals without a mismatch trigger;
- run Pro/Fable/Deep Research or use external quota;
- retry a blocked receive.

## Safe next action

Return the complete receive report to the originating conversation for the mandatory rehearsal acceptance oracle. Only explicit acceptance permits the separate guidance-refresh operation.
