# V1 Controller, Fixture and Branch Contract

```yaml
execution_package_id: MNE-TARGET-LIFECYCLE-V1-EXECUTION-PACKAGE-001
file_role: controller_fixture_branch_allocation
status: prepared_not_executed
V1_authorized: false
```

## 1. Controller role

The controller is a bounded executor and evidence aggregator. It is not the architecture author or final semantic adjudicator.

The controller may, after exact Owner authorization:

- verify the execution-time latest Mnemosyne package identities;
- verify the synthetic repository and pinned V0 final head;
- record before-run refs for named real repositories;
- create the public/synthetic fixture on the fixture branch;
- allocate the exact task branches below from pinned commits;
- create exact task input contracts;
- receive cell result refs;
- run final mechanical aggregation and no-write comparison;
- preserve the complete bundle.

The controller must not:

- run a scenario outside the selected set;
- expose S7 sufficient migration facts to the S8 worker;
- revise candidate/package semantics;
- merge scenario branches merely for convenience;
- create scenario PRs;
- write a real repository;
- act as final Pro adjudicator.

## 2. Pre-run identity gate

Required exact identities at launch:

```yaml
V1_preflight:
  Mnemosyne_master: RECORD_AT_LAUNCH
  candidate_blob_expected: 1eaeffaf01b3eae878cd0a97cb5d1884b7dba3cc
  validation_blob_expected: 364482a28ab9218c3a6beddb072be2545779132f
  package_README_blob_expected: 444b7e7186e6e90002a1b9966bc69ff0e1b49aaa
  V0_authorization_blob_expected: 25e330445c18cdd0833411d259a093c7a3ccfc61
  V0_adjudication_ref: notes/validation-adjudications/MNE-TARGET-LIFECYCLE-V0-ADJUDICATION-001.md
  V1_authorization_ref: REQUIRED
  synthetic_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  synthetic_repository_visibility: public
  V0_final_head_expected: e8e3296922185b4b70997c2351d6f39423f2cd4f
```

The MNEMOSYNE-212 merge commit and the exact V0-adjudication/V1-decision/execution-package blobs are recorded at launch after the PR is merged. Any mismatch blocks V1.

## 3. Controller and fixture branches

```yaml
branches:
  controller:
    task_id: TLR-V1-CONTROLLER-001
    branch: tlr-v1-controller
    base: e8e3296922185b4b70997c2351d6f39423f2cd4f
    allowed_write_roots:
      - runs/MNE-TARGET-LIFECYCLE-V1-001/

  fixture_base:
    task_id: TLR-V1-FIXTURE-001
    branch: tlr-v1-fixture-base
    base: e8e3296922185b4b70997c2351d6f39423f2cd4f
    allowed_write_roots:
      - repository-governance/
      - targets/
      - libraries/
      - shared/
      - backups-fixture/
      - run-evidence/fixture/
```

The fixture branch contains only the frozen public/synthetic initial fixture. It must not contain V1 scenario outcomes.

The controller branch contains manifests, receipts, task contracts, cell result pointers, incidents and the final bundle. It must not contain a substantive target copy outside the synthetic fixture repository; this repository itself is the selected target-owned validation destination.

## 4. Scenario task branch map

All scenario branches are created from the exact fixture commit unless a dependency below explicitly names another base.

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

A task branch may be created only once. If the branch already exists unexpectedly, stop and reconcile; do not create a numbered replacement.

## 5. Result branches / files

Cells write their cell-level result to their scenario/task branches and return exact refs. The controller records normalized pointers under:

```text
runs/MNE-TARGET-LIFECYCLE-V1-001/
```

Recommended controller paths:

```text
00-controller-receive.yaml
01-fixture-receipt.yaml
02-branch-and-task-map.yaml
03-real-repository-no-write-baseline.yaml
cells/
  core-cell-result.yaml
  s7-positive-cell-result.yaml
  s8-negative-cell-result.yaml
  s11-backup-cell-result.yaml
mechanical/
  declared-vs-actual-write-sets.yaml
  branch-and-output-identities.yaml
  contamination-and-isolation-checks.yaml
  final-no-write-proof.yaml
incidents/
  incident-ledger.yaml
06-v1-result-bundle.yaml
```

Every pointer includes:

- repository;
- branch;
- commit SHA;
- tree SHA when relevant;
- file path;
- blob SHA;
- attempt/retry relation.

## 6. Initial fixture contract

Create exactly the tree and synthetic contracts defined in the frozen `01-synthetic-fixture-and-scenario-contracts.md`:

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

The fixture must include CommonLib v1, Alpha's v1 usages, Beta's initial non-use, authority files, dependency declarations and deterministic tests needed by the selected scenarios.

Do not add:

- S7 v2 sufficient guide to the fixture base;
- S8 expected answer;
- a complete Gamma target;
- real code, conversations, credentials or target data;
- a universal consumer registry;
- a parent/meta downstream copy.

## 7. S8 input preparation firewall

The controller prepares the S8 branch from the fixture commit with only:

- the v2 API/behavior change needed to make migration relevant;
- the intentionally insufficient human-only note;
- Alpha's v1 usage;
- the S8 task instruction and stop rules;
- no `CHANGES-AGENT.md` sufficient guide;
- no S7 worker output;
- no file, comment or controller summary containing the required migration actions.

The controller records a branch inventory and a negative search/absence receipt before the S8 worker launches.

The S8 worker is not told the required migration facts. Its correct outcome is to block and identify the missing categories, not to reconstruct the hidden answer.

## 8. Real-repository no-write baseline

Before any V1 synthetic write, record exact default-branch refs for:

```yaml
named_real_repositories:
  - 08822407d/Mnemosyne
  - 08822407d/Meta-Agent
```

Do not enumerate or access other real repositories merely to enlarge the claim. The final claim remains exact for these two named repositories and limited for unnamed targets.

## 9. Controller stop rules

Return `V1_CONTROLLER_BLOCKED` and perform no scenario write when:

- V1 Owner authorization is absent or mismatched;
- synthetic repository `master` is not the pinned V0 final head;
- V0 evidence paths changed;
- expected package identities differ;
- existing branches/PRs conflict with the branch map;
- visibility or material class is wrong;
- no-write baseline cannot be recorded;
- S8 isolation cannot be prepared;
- any required fixture fact is semantically ambiguous rather than format-only.

## 10. Controller completion receipt

Before launching cells, return and store:

```yaml
V1_controller_receipt:
  run_id:
  execution_package_id:
  Owner_authorization_ref:
  Mnemosyne_master:
  synthetic_repository:
  V0_final_head_verified:
  fixture_branch:
  fixture_commit:
  fixture_tree:
  controller_branch:
  task_branch_map_ref:
  named_real_repository_before_refs: []
  S8_isolation_input_prepared:
  material_safety_pass:
  disposition: PASS | BLOCKED
```
