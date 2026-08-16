# Cross-Repository Safe Concurrency V2-A — A0 Sentinel Execution Package 001

> Frozen execution package candidate for the Owner-selected V2-A sentinel route. This package is prepared only. It does not authorize branch creation, repository writes, validation execution, quota use or any A1–A7 scenario.

```yaml
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-001
version: 0.1.0
task_id: MNEMOSYNE-223
run_decision_candidate: notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-001.md
source_validation_package: notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/README.md
proposed_run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
selected_stage: V2_A
selected_cells:
  - A0
status: prepared_not_owner_authorized_not_executed
controller_branch_created: false
validation_repository_written: false
validation_execution_authorized: false
worker_branch_creation_authorized: false
PR_creation_authorized: false
external_quota_authorized: false
```

## 1. Purpose

This package reduces the future A0 run to one bounded controller task. It tests only whether the exact package, repository, branch, material, permission and no-write evidence contract can be established on the selected GitHub surface.

It deliberately does not test concurrency behavior itself. A0 success is a prerequisite candidate for later V2-A preparation, not evidence that A1–A7 will pass.

## 2. Selected surface

```yaml
repository: 08822407d/mnemosyne-target-lifecycle-validation-002
visibility: public
controller_base: master@e8e3296922185b4b70997c2351d6f39423f2cd4f
read_only_fixture: tlr-v1-fixture-base@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
read_only_fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
future_controller_branch: v2a-sentinel-001-controller
future_controller_PR: null
product_surface: standard_ChatGPT_conversation_with_GitHub_connector
recommended_visible_selection_if_available: gpt-5.6 sol extra high
fresh_review: separate_ChatGPT_Pro_conversation
```

If any pinned source or product prerequisite differs at execution time, the controller stops. It does not refresh this package itself.

## 3. Package files

```text
README.md
00-controller-receive-and-surface-contract.md
01-package-and-source-manifest.md
02-next-tier-controller-task.md
03-mechanical-checks-and-result-template.md
04-startup-message.md
05-package-integrity-and-non-execution-checklist.md
```

## 4. Future A0 output files

Only the following paths may be written, on the future controller branch only:

```text
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/00-controller-receive.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/01-product-and-permission-receipt.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/02-package-and-material-receipt.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/03-repository-and-ref-baseline.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/04-mechanical-checks.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/05-sentinel-result-bundle.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/incidents/incident-ledger.yaml
```

No fixture, target, library, shared, root-config, V1 evidence or master path may be changed.

## 5. Execution sequence after future G2A authorization

1. open one fresh next-tier ChatGPT conversation with the GitHub connector;
2. record the visible model and reasoning labels verbatim;
3. read the exact merged Mnemosyne package and pinned GitHub refs;
4. complete a read-only receive gate;
5. if and only if the receive gate passes, create `v2a-sentinel-001-controller` from the pinned validation-repository master;
6. write only the seven output files;
7. repeat protected-ref checks;
8. stop with no worker branch, PR, retry or next cell;
9. return the complete result bundle to a fresh Pro conversation.

## 6. Current gate

```yaml
current_gate: OWNER_G2A_EXECUTION_AUTHORIZATION_AFTER_PACKAGE_MERGE_AND_IDENTITY_RECHECK
G1A_surface_decision_prepared: true
G2A_execution_authorized: false
A0_started: false
A1_to_A7_authorized: false
```

Package merge will make the plan durable. It will not authorize or begin the run.
