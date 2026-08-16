# Cross-Repository Safe Concurrency V2-A A0 Sentinel — Execution Package 003

> Additive repair package for the model-selection authorization/provenance gap found during fresh Pro review of package 002. Package 003 is prepared, not Owner-authorized and not executed.

```yaml
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-003
version: 0.3.0
task_id: MNEMOSYNE-226
parent_package: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-002
parent_package_path: notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-002/
source_review: notes/adjudications/MNEMOSYNE-224-PACKAGE-002-FRESH-PRO-REVIEW-001.md
source_incident: notes/run-context-incidents/MNEMOSYNE-224-OPERATOR-SELECTION-MISREPRESENTATION-001.md
status: prepared_not_owner_authorized_not_executed
selected_stage: V2_A
selected_cells: [A0]
sentinel_only: true
validation_execution_authorized: false
```

## 1. Scope

Package 003 preserves every repository, fixture, branch, write-set, no-retry, no-PR, no-hidden-continuation and fresh-Pro-return boundary in package 002.

It supersedes package 002 only for:

```yaml
superseded_scope:
  - exact_G2A_candidate_identity
  - model_selection_authorization_binding
  - startup_message_dynamic_fields
  - controller_model_selection_evidence
  - MNEMOSYNE_224_Pro_review_provenance_assumption
```

Package 002 remains historical evidence of the technically correct source-binding repair and the incomplete model-binding protocol.

## 2. Controlling precedence

For a future A0 run:

1. exact Owner G2A/startup message bound to candidate 003 and manifest 003;
2. package 003;
3. package 002 for all inherited semantics not explicitly changed by package 003;
4. parent V2 design/package and load-bearing source blobs;
5. exact validation repository refs.

Any conflict in package 003 scope is resolved in favor of package 003. Package 003 cannot broaden A0 beyond package 002.

## 3. Required G2A dynamic fields

The same exact message sent to the fresh controller must contain:

```yaml
required_G2A_fields:
  run_decision_candidate_003_blob:
  package_003_source_manifest_blob:
  protected_Mnemosyne_master:
  protected_Meta_Agent_master:
  authorized_visible_model_label:
```

The authorized visible model label is not a hidden UI assumption. It must appear verbatim in the Owner instruction received by the controller.

The controller separately records:

```yaml
model_selection_receipt:
  Owner_authorized_visible_label:
  operator_observed_or_reported_selected_label:
  equality_result:
  backend_identity: unknown_or_not_attestable
```

A missing label or mismatch blocks before any validation-repository write.

## 4. Files

```text
README.md
00-delta-precedence-and-provenance-contract.md
01-package-and-source-manifest.md
02-next-tier-controller-amendment.md
03-startup-message.md
04-package-integrity-and-non-execution-checklist.md
```

## 5. Inherited A0 topology

```yaml
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
validation_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
validation_master: e8e3296922185b4b70997c2351d6f39423f2cd4f
read_only_fixture: tlr-v1-fixture-base@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
future_controller_branch: v2a-sentinel-001-controller
output_file_count: 7
worker_branches: []
PR_creation: prohibited
```

## 6. Scheduling gate

At package preparation time another independent Mnemosyne write branch exists:

```text
mnemosyne-225-f1-bounded-validation-design-and-next-step-write-visibility
```

Package 003 publication may proceed because changed paths are separate. A0 G2A must wait until every route expected to move Mnemosyne `master` during the A0 window is merged, abandoned, or explicitly paused.

## 7. Non-authorization

This package does not authorize:

- G2A;
- creation of the controller branch;
- any validation-repository write;
- A0 or A1–A7;
- V2-B or V2-C;
- connector/account changes;
- web, Research, Fable or external quota;
- private/real-target material;
- modification of Mnemosyne execution source, Meta-Agent or a real target;
- automatic retry, compensation, reset or force-push.
