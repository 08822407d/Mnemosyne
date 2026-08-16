# Fable F2 Cross-Repository Safe Concurrency Research — Current Status

```yaml
status_id: MNE-FABLE5-CROSS-REPOSITORY-CONCURRENCY-STATUS-001
created_by_task: MNEMOSYNE-214
last_updated_by_task: MNEMOSYNE-226
canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
display_name: MNE-DR-005 跨仓库并发
roadmap_priority: F2
status: PACKAGE_003_BRANCH_PREPARED_PR_PUBLICATION_WAITING_FOR_ACTIVE_PR_293_EXECUTION_NOT_AUTHORIZED
Fable_report_received: true
fresh_Pro_F2_adjudication_completed: true
Owner_F2_option_A_accepted: true
V2_staged_design_prepared: true
V2_A_A0_plan_prepared: true
MNEMOSYNE_224_provenance_incident_recorded: true
MNEMOSYNE_224_fresh_Pro_review_completed: true
package_002_core_technical_repair_accepted: true
package_002_direct_G2A_readiness: false
package_003_prepared_on_branch: true
package_003_merged: false
MNEMOSYNE_226_PR_created: false
blocking_open_PR: 293
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

No architecture or target-adoption status changes in MNEMOSYNE-226.

## 2. Package-001 defect and package-002 repair

Package 001 incorrectly coupled immutable source identity to a pre-publication Mnemosyne `master` and therefore invalidated itself when PR #291 merged.

Package 002 correctly repaired that by separating:

```yaml
immutable_source_integrity: exact_path_blob_pairs
execution_window_no_write: Owner_frozen_current_refs_checked_before_and_after_A0
```

Fresh Pro review in MNEMOSYNE-226 accepts this core repair, the hard-pinned validation dependencies, A0-only scope, seven-file write set, no-worker/no-PR boundary, no retry/repair and fresh-Pro return gate.

## 3. MNEMOSYNE-224 provenance incident

The Owner reports that the MNEMOSYNE-224/PR #292 work was produced while a next-tier model option was selected, not Pro. PR #292's `operator_selection_verbatim: Pro` and `PASS_Pro_protocol_repair` claims are therefore invalid for attribution scope.

Additive records:

```text
notes/run-context-incidents/MNEMOSYNE-224-OPERATOR-SELECTION-MISREPRESENTATION-001.md
notes/adjudications/MNEMOSYNE-224-PACKAGE-002-FRESH-PRO-REVIEW-001.md
```

The exact prior UI label and hidden backend remain unknown. Historical artifacts are not rewritten.

## 4. Package-002 model-binding defect

Package 002's decision/status identified five G2A dynamic fields, including `authorized_visible_model_label`, but its startup template supplied only four placeholders and omitted the model label from the message delivered to the fresh controller.

The omission is material because a consumer-chat assistant cannot reliably infer current UI selection from prior context. The present incident demonstrates that risk.

Therefore package 002 is not independently ready for G2A.

## 5. Package 003

Prepared on:

```text
mnemosyne-226-correct-mne224-provenance-and-model-binding
```

Future controlling candidate after publication:

```text
notes/validation-run-decisions/
MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-003.md

notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-003/
```

Package 003:

- inherits package 002's accepted technical repair and all A0 boundaries;
- requires the exact Owner-authorized and actual operator-selected visible labels in the same G2A/startup message;
- preserves both raw strings and exact equality result;
- blocks before branch creation when either label is absent, uncertain or mismatched;
- keeps backend identity unknown/not attestable;
- adds no eighth validation output file;
- does not modify the validation repository.

## 6. Parallel-route publication and scheduling gates

Ready PR #293 currently publishes the independent MNEMOSYNE-225 F1/response-guidance task. Its paths do not overlap with MNEMOSYNE-226 and its PR body records that it should publish first.

Therefore:

```yaml
MNEMOSYNE_226_branch_content_complete: true
MNEMOSYNE_226_PR_publication_allowed_while_293_open: false
parallel_PR_exception: none
next_publication_action: wait_for_293_then_integrate_latest_master_and_create_one_Ready_PR
```

Even after package 003 publishes, G2A must wait until every route expected to move Mnemosyne `master` during A0 is merged, abandoned or explicitly paused.

## 7. Current gate

```yaml
current_gate: WAIT_FOR_PR_293_THEN_PUBLISH_MNEMOSYNE_226_THEN_FRESH_PRO_G2A
G2A_execution_authorized: false
required_future_G2A_fields:
  - run_decision_candidate_003_blob
  - package_003_source_manifest_blob
  - protected_Mnemosyne_master
  - protected_Meta_Agent_master
  - authorized_visible_model_label
  - operator_selected_visible_model_label
```

No repository publication follows the future G2A before A0.

## 8. Explicit boundaries

No current artifact authorizes:

- creation of `v2a-sentinel-001-controller`;
- validation-repository writes;
- A0 or A1–A7 execution;
- V2-B/V2-C;
- connector/account changes;
- web, Research, Fable or external quota;
- private/real-target material;
- execution-source, Meta-Agent, architecture or target modification;
- automatic retry, repair, compensation, reset or force-push.
