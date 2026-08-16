# Cross-Repository Safe Concurrency V2-A Sentinel — Pro-Recommended Owner Run Decision Candidate 003

> Fresh-Pro-reviewed repair of candidate 002's model-selection authorization binding. This file is not Owner G2A authorization and does not execute A0.

```yaml
decision_candidate_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-003
task_id: MNEMOSYNE-226
source_incident: MNEMOSYNE-224-OPERATOR-SELECTION-MISREPRESENTATION-001
source_fresh_Pro_review: notes/adjudications/MNEMOSYNE-224-PACKAGE-002-FRESH-PRO-REVIEW-001.md
parent_decision_candidate: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-002
parent_package: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-002
source_package: notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-003/README.md
supersedes_for_scope:
  - G2A_model_selection_authorization_binding
  - startup_message_dynamic_fields
  - controller_model_selection_evidence
  - reliance_on_MNEMOSYNE_224_Pro_provenance_claim
status: PRO_RECOMMENDATION_READY_NOT_OWNER_AUTHORIZED
selected_stage_candidate: V2_A
selected_cells_candidate: [A0]
sentinel_only: true
validation_execution_authorized: false
validation_repository_write_authorized: false
external_quota_authorized: false
real_target_adoption_authorized: false
```

## 1. Technical disposition on candidate/package 002

Candidate/package 002's source-binding repair is accepted:

- exact load-bearing blobs establish source integrity;
- execution-window Mnemosyne/Meta-Agent refs are frozen after publication;
- validation master, fixture and V1 ref inventory remain hard-pinned;
- A0-only, seven-path, no-worker, no-PR, no-retry boundaries remain valid.

Candidate 003 does not reopen those decisions.

## 2. Required model-selection repair

The exact Owner-authorized visible model label and the exact operator-selected visible model label must both be supplied in the same G2A/startup message delivered to the fresh controller.

```yaml
model_binding:
  Owner_authorized_label:
    evidence_class: direct_user_instruction
  operator_selected_label:
    evidence_class: operator_observed_or_operator_reported
  comparison: exact_raw_string_equality
  mismatch_or_missing: BLOCKED_before_branch_creation
  backend_identity: unknown_or_not_attestable
```

The controller cannot infer the current selection from prior-turn state, assistant memory, model self-report, response behavior or a recommendation stored in GitHub.

## 3. Exact future G2A fields

After candidate 003/package 003 merge and fresh execution-time recheck, the Owner message must contain:

```yaml
G2A_required_dynamic_fields:
  run_decision_candidate_003_blob:
  package_003_source_manifest_blob:
  protected_Mnemosyne_master:
  protected_Meta_Agent_master:
  authorized_visible_model_label:
  operator_selected_visible_model_label:
```

The same message is sent to the fresh controller; no hidden prior authorization is assumed.

## 4. Inherited run topology

```yaml
run:
  validation_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-STAGED-VALIDATION-001
  package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-003
  run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
  selected_stage: V2_A
  selected_cells: [A0]
  sentinel_only: true
  validation_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  validation_master: e8e3296922185b4b70997c2351d6f39423f2cd4f
  read_only_fixture: tlr-v1-fixture-base@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
  fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
  controller_branch: v2a-sentinel-001-controller
  worker_branches: []
  PR_creation: prohibited
  output_file_count: 7
```

The exact seven paths and all other inherited boundaries are those in package 002.

## 5. Scheduling gate

At candidate preparation time, another known branch exists:

```text
mnemosyne-225-f1-bounded-validation-design-and-next-step-write-visibility
```

It has no path overlap with MNEMOSYNE-226, so package publication may proceed. The Owner G2A must wait until any route expected to move Mnemosyne `master` during A0 is merged, abandoned or explicitly paused.

## 6. Product/model disposition

```yaml
A0_execution:
  capability_class: NEXT_TIER_SUFFICIENT_CANDIDATE
  recommended_visible_selection_if_available: gpt-5.6 sol extra high
  exact_authorized_label: supplied_by_future_Owner_G2A
  exact_selected_label: supplied_by_operator_in_same_startup_message
  silent_substitution: prohibited
A0_post_run_review:
  capability_class: FRONTIER_REQUIRED
Deep_Research: NOT_NEEDED
parallel_frontier_research: NOT_NEEDED_BEFORE_A0
```

## 7. Non-authorization

This candidate does not authorize:

- G2A or any validation write;
- controller branch creation;
- A0 or A1–A7;
- V2-B/V2-C;
- connector/account changes;
- external quota or Research;
- real/private target access;
- execution-source or architecture modification;
- automatic retry/repair/compensation.

## 8. Recommended future Owner action

After package 003 is merged and the scheduling/freshness gate passes, use the fully populated message in:

```text
notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-003/03-startup-message.md
```

Do not issue G2A while a known parallel route is expected to publish to Mnemosyne during the A0 window.
