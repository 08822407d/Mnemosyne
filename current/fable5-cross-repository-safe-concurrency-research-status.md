# Fable F2 Cross-Repository Safe Concurrency Research — Current Status

```yaml
status_id: MNE-FABLE5-CROSS-REPOSITORY-CONCURRENCY-STATUS-001
created_by_task: MNEMOSYNE-214
last_updated_by_task: MNEMOSYNE-228
canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
display_name: MNE-DR-005 跨仓库并发
roadmap_priority: F2
status: PACKAGE_003_MERGED_G2A_AND_A0_SEPARATELY_GATED
Fable_report_received: true
fresh_Pro_F2_adjudication_completed: true
Owner_F2_option_A_accepted: true
V2_staged_design_prepared: true
V2_A_A0_plan_prepared: true
MNEMOSYNE_224_provenance_incident_recorded: true
MNEMOSYNE_224_fresh_Pro_review_completed: true
package_002_core_technical_repair_accepted: true
package_002_direct_G2A_readiness: false
package_003_prepared: true
package_003_merged: true
package_003_merge_PR: 294
package_003_merge_commit: 5ca091e1c52bb1e7483b2d54e9259d3ec85b7b93
package_003_post_merge_tree_identity_verified: true
MNEMOSYNE_226_PR_created: true
MNEMOSYNE_226_PR_merged: true
G2A_execution_authorized: false
G2A_dynamic_fields_bound: false
execution_window_frozen: false
V2_A_A0_execution_authorized: false
controller_branch_created: false
validation_repository_written: false
external_quota_authorized: false
automatic_retry: false
real_target_adoption_authorized: false
```

## 1. Preserved research and accepted F2 direction

The exact Fable report, input snapshot, fresh Pro F2 adjudication and Owner Option A remain controlling historical evidence:

```text
raw/research-reports/cycles/2026Q3-cross-repository-safe-concurrency/
notes/research-adjudications/MNE-DR-005-CROSS-REPOSITORY-SAFE-CONCURRENCY-PRO-ADJUDICATION-001.md
notes/cross-repository-safe-concurrency-and-ordered-work-amendment-candidate-v0.1.md
notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-OWNER-DECISION-001.md
```

MNEMOSYNE-228 changes no architecture, target-adoption decision or validation disposition. It only closes the stale publication state left after PR #294 merged.

## 2. Package-001 defect and package-002 repair

Package 001 incorrectly coupled immutable source identity to a pre-publication Mnemosyne `master` and therefore invalidated itself when PR #291 merged.

Package 002 correctly repaired that by separating:

```yaml
immutable_source_integrity: exact_path_blob_pairs
execution_window_no_write: Owner_frozen_current_refs_checked_before_and_after_A0
```

Fresh Pro review in MNEMOSYNE-226 accepted this core repair, the hard-pinned validation dependencies, A0-only scope, seven-file write set, no-worker/no-PR boundary, no retry/repair and fresh-Pro return gate.

## 3. MNEMOSYNE-224 provenance incident

The Owner reported that the MNEMOSYNE-224/PR #292 work was produced while a next-tier model option was selected, not Pro. PR #292's `operator_selection_verbatim: Pro` and `PASS_Pro_protocol_repair` claims are therefore invalid for attribution scope.

Additive records remain:

```text
notes/run-context-incidents/MNEMOSYNE-224-OPERATOR-SELECTION-MISREPRESENTATION-001.md
notes/adjudications/MNEMOSYNE-224-PACKAGE-002-FRESH-PRO-REVIEW-001.md
```

The exact prior UI label and hidden backend remain unknown. Historical artifacts are not rewritten.

## 4. Package-002 model-binding defect

Package 002's decision/status identified five G2A dynamic fields, including `authorized_visible_model_label`, but its startup template supplied only four placeholders and omitted the model label from the message delivered to the fresh controller.

The omission is material because a consumer-chat assistant cannot reliably infer current UI selection from prior context. Package 002 therefore remains not independently ready for G2A.

## 5. Package 003 publication and post-merge identity

PR #294 published the controlling repair:

```yaml
PR: 294
state: closed
merged: true
draft: false
head_branch: mnemosyne-226-correct-mne224-provenance-and-model-binding
head_SHA: 9ac0e7ca185a5d9844c0c1d4357a5a409ed8f89b
merge_commit: 5ca091e1c52bb1e7483b2d54e9259d3ec85b7b93
head_tree: f3377b2668f931310b488ac91ad48f09b8c84528
merged_master_tree: f3377b2668f931310b488ac91ad48f09b8c84528
exact_tree_integrated: true
former_head_branch_present_after_merge: false
```

The merged controlling artifacts are:

```text
notes/validation-run-decisions/
MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-003.md

notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-003/
```

Exact merged identities re-read during closeout:

```yaml
candidate_003_blob: 9e46dd849c3c8604f5e2fa7fce9c02c5504ff202
package_003_source_manifest_blob: 967c7a9ce38883ab897bf856fa4004b987e7d911
package_003_file_count: 6
```

Package 003:

- inherits package 002's accepted technical repair and all A0 boundaries;
- requires the exact Owner-authorized and actual operator-selected visible labels in the same G2A/startup message;
- preserves both raw strings and exact equality result;
- blocks before branch creation when either label is absent, uncertain or mismatched;
- keeps backend identity unknown/not attestable;
- adds no eighth validation output file;
- does not modify the validation repository.

## 6. Durable post-publication route state

Package 003 publication is complete. No additional F2 design-publication repair is mandatory before the Owner may separately consider G2A.

This does not authorize or imply execution:

```yaml
package_003_publication_complete: true
G2A_authorized_by_PR_294_merge: false
A0_authorized_by_PR_294_merge: false
controller_branch_creation_authorized: false
validation_repository_write_authorized: false
current_execution_window_bound: false
```

Transient branch or PR publication state is intentionally not encoded as the durable route gate. Future unrelated Mnemosyne writes may move `master`; the future G2A must bind the then-current execution window instead of requiring another publication closeout solely because `master` moved.

## 7. Current gate

```yaml
current_gate: OWNER_SEPARATE_G2A_DECISION_AFTER_WRITE_QUIESCENCE_AND_DYNAMIC_FIELD_RECHECK
G2A_execution_authorized: false
V2_A_A0_execution_authorized: false
required_future_G2A_fields:
  - run_decision_candidate_003_blob
  - package_003_source_manifest_blob
  - protected_Mnemosyne_master
  - protected_Meta_Agent_master
  - authorized_visible_model_label
  - operator_selected_visible_model_label
required_pre_G2A_checks:
  - candidate_and_manifest_exact_blobs_still_match
  - all_known_routes_expected_to_move_Mnemosyne_master_during_A0_are_merged_abandoned_or_explicitly_paused
  - current_Mnemosyne_and_Meta_Agent_refs_are_re_read_and_frozen
  - authorized_and_operator_selected_visible_labels_are_present_and_exactly_equal
```

The Owner's statement that the MNEMOSYNE-228 closeout conversation is using a Pro selection is provenance for this closeout only. It does not pre-bind or substitute for the two exact visible-label fields required in a future G2A/startup message.

No repository publication follows the future G2A before A0.

## 8. Explicit boundaries

No current artifact or PR #294 merge authorizes:

- creation of `v2a-sentinel-001-controller`;
- validation-repository writes;
- A0 or A1–A7 execution;
- V2-B/V2-C;
- connector/account changes;
- web, Research, Fable or external quota;
- private/real-target material;
- execution-source, Meta-Agent, architecture or target modification;
- automatic retry, repair, compensation, reset or force-push.