# V1 Controller, Fixture and Branch Contract

> Historical controller/fixture profile for `MNE-TARGET-LIFECYCLE-V1-001`, prospectively amended after Owner acceptance. The historical run remains bound to blob `7068b5efc0d484baf48824c5692ee1b3b2d8a634`; the current file corrects the fixture-root README allowlist only for future reuse.

```yaml
execution_package_id: MNE-TARGET-LIFECYCLE-V1-EXECUTION-PACKAGE-001
file_role: controller_fixture_branch_allocation
created_by_task: MNEMOSYNE-212
last_amended_by_task: MNEMOSYNE-215
status: HISTORICAL_RUN_COMPLETE_FUTURE_REUSE_AMENDED
historical_blob: 7068b5efc0d484baf48824c5692ee1b3b2d8a634
amendment_ref: notes/target-agent-lifecycle-v1-execution-package-001/08-owner-accepted-post-v1-amendment.md
new_V1_authorized: false
```

## 1. Controller role

The controller is a bounded executor and evidence aggregator. It is not the architecture author or final semantic adjudicator.

After an exact run authorization it may:

- verify execution-time Mnemosyne package identities;
- verify the synthetic repository and pinned base;
- record before-run refs for named real repositories;
- create the public/synthetic fixture on the fixture branch;
- allocate the exact task branches below from pinned commits;
- create exact task input contracts;
- receive cell result refs;
- run final mechanical aggregation and no-write comparison;
- preserve the complete bundle.

It must not:

- run a scenario outside the selected set;
- expose S7 sufficient migration facts to the S8 worker;
- revise candidate/package semantics;
- merge scenario branches merely for convenience;
- create scenario PRs without separate authority;
- write a real repository;
- act as final Pro adjudicator.

## 2. Historical pre-run identity gate

The completed historical V1 used:

```yaml
historical_V1_preflight:
  Mnemosyne_master: 1a61414bbe86a9a1b2a37c2ae1d22caf21c39dea
  candidate_blob: 1eaeffaf01b3eae878cd0a97cb5d1884b7dba3cc
  validation_blob: 364482a28ab9218c3a6beddb072be2545779132f
  package_README_blob: 444b7e7186e6e90002a1b9966bc69ff0e1b49aaa
  V1_authorization_blob: 361b3d110f41f53098ccbd6f8705c494fc2df0b6
  synthetic_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  synthetic_repository_visibility: public
  V0_final_head: e8e3296922185b4b70997c2351d6f39423f2cd4f
```

A future run must create a new receipt using current exact identities and a new Owner authorization. The historical values are evidence, not standing execution authority.

## 3. Controller and fixture branches

```yaml
branches:
  controller:
    task_id: TLR-V1-CONTROLLER-001
    branch: tlr-v1-controller
    historical_base: e8e3296922185b4b70997c2351d6f39423f2cd4f
    allowed_write_roots:
      - runs/MNE-TARGET-LIFECYCLE-V1-001/

  fixture_base:
    task_id: TLR-V1-FIXTURE-001
    branch: tlr-v1-fixture-base
    historical_base: e8e3296922185b4b70997c2351d6f39423f2cd4f
    allowed_write_roots:
      - README.md
      - repository-governance/
      - targets/
      - libraries/
      - shared/
      - backups-fixture/
      - run-evidence/fixture/
```

The addition of root `README.md` reconciles this exact write set with the required initial fixture tree. The historical executor created only the public/synthetic fixture overview at that path. This amendment is prospective and does not erase the recorded historical protocol discrepancy.

The fixture branch contains only the frozen public/synthetic initial fixture. It must not contain scenario outcomes. The controller branch contains manifests, receipts, task contracts, cell result pointers, incidents and the final bundle.

## 4. Scenario task branch map

All scenario branches are created from the exact fixture commit unless a dependency explicitly names another base.

```yaml
scenario_branches:
  S1:
    task_id: TLR-V1-S1-001
    branch: tlr-v1-s1-destination-block
    base: fixture_commit
  S2:
    task_id: TLR-V1-S2-001
    branch: tlr-v1-s2-bounded-writer
    base: fixture_commit
  S3_alpha:
    task_id: TLR-V1-S3-ALPHA-001
    branch: tlr-v1-s3-alpha
    base: fixture_commit
  S3_beta:
    task_id: TLR-V1-S3-BETA-001
    branch: tlr-v1-s3-beta
    base: fixture_commit
  S4_shared:
    task_id: TLR-V1-S4-SHARED-001
    branch: tlr-v1-s4-shared-schema
    base: fixture_commit
  S4_dependent:
    task_id: TLR-V1-S4-DEPENDENT-001
    branch: tlr-v1-s4-alpha-dependent
    base: fixture_commit
  S4_unknown:
    task_id: TLR-V1-S4-UNKNOWN-001
    branch: tlr-v1-s4-unknown-global
    base: fixture_commit
  S5:
    task_id: TLR-V1-S5-001
    branch: tlr-v1-s5-upstream-proposal
    base: fixture_commit
  S6:
    task_id: TLR-V1-S6-001
    branch: tlr-v1-s6-beta-requirement
    base: fixture_commit
  S7_library:
    task_id: TLR-V1-S7-LIBRARY-001
    branch: tlr-v1-s7-commonlib-v2
    base: fixture_commit
  S7_alpha:
    task_id: TLR-V1-S7-ALPHA-001
    branch: tlr-v1-s7-alpha-migration
    base: S7_library_final_commit
  S8_input_and_worker:
    task_id: TLR-V1-S8-001
    branch: tlr-v1-s8-insufficient-docs
    base: fixture_commit
  S9:
    task_id: TLR-V1-S9-001
    branch: tlr-v1-s9-imperfect-route
    base: fixture_commit
  S11:
    task_id: TLR-V1-S11-001
    branch: tlr-v1-s11-backup-restore
    base: fixture_commit
```

A task branch may be created only once. If it already exists unexpectedly, stop and reconcile; do not create a numbered replacement.

## 5. Result files

Cells write results to their scenario/task branches and return exact refs. The controller records normalized pointers under the authorized run root, including repository, branch, commit, tree when relevant, file path, blob and attempt/retry relation.

## 6. Initial fixture contract

Create exactly the public/synthetic tree and contracts defined by the frozen scenario package:

```text
README.md
repository-governance/
targets/agent-alpha/
targets/agent-beta/
libraries/common-lib/
shared/common-schema/
backups-fixture/
run-evidence/
```

The fixture includes CommonLib v1, Alpha's v1 usages, Beta's initial non-use, authority files, dependencies and deterministic test artifacts needed by selected scenarios.

Do not add:

- S7 v2 sufficient guide to the fixture base;
- S8 expected answer;
- a complete Gamma target;
- real code, conversations, credentials or target data;
- a universal consumer registry;
- a parent/meta downstream copy.

Test artifacts in the fixture establish only `TEST_ARTIFACT_PRESENT` until a stronger evidence level is recorded under `notes/validation-evidence-strength-levels-v0.1.md`.

## 7. S8 input firewall

The controller prepares the S8 branch from the fixture commit with only the authorized intentionally insufficient packet and Alpha's v1 usage. It must exclude the sufficient Agent guide, S7 output and concrete hidden migration actions. It records branch inventory and absence receipts before launch.

The S8 worker's correct outcome is to block and identify missing information categories, not reconstruct hidden answers.

## 8. Real-repository no-write baseline

Before any synthetic write, record exact default-branch refs for the named real repositories in the current authorization. Do not access unnamed targets merely to enlarge the proof claim.

## 9. Controller stop rules

Return a blocked receipt and perform no scenario write when:

- run authorization is absent or mismatched;
- repository/base, visibility or material class is wrong;
- expected package identities differ;
- existing branches/PRs conflict with the branch map;
- a required path is outside the declared write set;
- no-write baseline cannot be recorded;
- S8 isolation cannot be prepared;
- a required fixture fact is semantically ambiguous rather than format-only;
- a requested test claim exceeds the available evidence level.

## 10. Completion receipt

Before launching cells, store a receipt containing run ID, execution package, Owner authorization, exact Mnemosyne source, synthetic repository/base, fixture branch/commit/tree, controller branch, task map, named real-repository before refs, S8 isolation state, material-safety result, test-evidence contract version and PASS/BLOCKED disposition.

## 11. Boundaries

This current contract does not authorize a new run, runtime supplement, branch cleanup, target adoption, Meta-Agent write, execution-source change, S10, V2, external research or quota.
