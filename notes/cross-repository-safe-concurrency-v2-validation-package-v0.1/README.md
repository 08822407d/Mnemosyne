# Cross-Repository Safe Concurrency V2 — Staged Validation Package v0.1

> Frozen design package for the Owner-accepted provisional F2 amendment. The package is prepared, not selected and not executable by preparation alone.

```yaml
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-PACKAGE-001
version: 0.1.0
task_id: MNEMOSYNE-222
validation_ref: notes/validation-designs/cross-repository-safe-concurrency-v2-staged-validation-v0.1.md
Owner_decision_ref: notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-OWNER-DECISION-001.md
source_amendment_ref: notes/cross-repository-safe-concurrency-and-ordered-work-amendment-candidate-v0.1.md
status: prepared_not_selected_not_executed
public_synthetic_package: true
V2_A_runnable_after_future_authorization: candidate_yes
V2_B_runnable_after_future_authorization_and_dependency_gate: candidate_yes
V2_C_runnable_from_this_package: false_design_only
repository_creation_authorized: false
validation_execution_authorized: false
connector_permission_change_authorized: false
external_quota_authorized: false
real_target_material: prohibited
```

## 1. Package purpose

The package turns the accepted F2 amendment into a frozen, reviewable validation contract. It is intended to prevent a future executor from inventing concurrency rules, recovery behavior, evidence levels or permission assumptions during a run.

It tests failure discovery, not universal correctness.

## 2. Files

```text
README.md
00-owner-gates-and-stage-boundaries.md
01-synthetic-fixture-and-scenario-contracts.md
02-v2-a-core-concurrency-taskbook.md
03-v2-b-ordered-cross-repository-taskbook.md
04-v2-c-connector-security-design-only.md
05-mechanical-checks-and-evidence-rubric.md
06-run-manifest-and-result-template.md
07-package-integrity-and-non-execution-checklist.md
```

## 3. Stage relationship

```text
V2-A
  core single-repository concurrency and stale-state evidence
  public/synthetic
  independently selectable later

V2-B
  ordered multi-repository partial failure and recovery
  public/synthetic
  normally waits for reviewed V2-A or explicit Owner exception

V2-C
  connector/app permission and privacy boundary
  design only
  requires a separate security/product/account authorization
```

No stage authorizes the next stage automatically.

## 4. Recommended future run sequence

The current package does not select a run. If the Owner later chooses to proceed, the recommended sequence is:

1. prepare exact public synthetic repositories and freeze their base identities;
2. run a V2-A sentinel that tests package/identity/no-write gates only;
3. fresh Pro reviews the sentinel;
4. separately authorize the selected V2-A scenario set;
5. fresh Pro adjudicates V2-A;
6. only then decide whether V2-B should be prepared/executed on two separate synthetic repositories;
7. keep V2-C blocked until a separate connector/security contract is accepted.

## 5. Package invariants

- no real or private target material;
- no modification of Mnemosyne, Meta-Agent or any real target by a validation worker;
- exact task/branch/PR lineage per task;
- exact read, write, generated/derived and semantic effects;
- explicit evidence-strength state per claim;
- no automatic retry after identity, scope, semantic or permission failure;
- no automatic compensation unless separately frozen and authorized;
- no force-push/reset as a default recovery;
- no candidate repair during execution;
- raw failures remain preserved;
- all architecture/adoption decisions remain Owner-only.

## 6. Current gate

```yaml
current_gate: PACKAGE_REVIEW_AND_FUTURE_OWNER_RUN_SELECTION
validation_design_prepared: true
validation_execution_selected: false
validation_execution_authorized: false
```

A future startup message, run authorization or synthetic-repository creation must be generated only after the Owner selects a specific stage and surface.
