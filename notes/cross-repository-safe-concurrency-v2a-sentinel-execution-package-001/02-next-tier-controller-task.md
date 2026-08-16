# V2-A A0 Sentinel — Frozen Next-Tier Controller Task

> This task is not runnable until the Owner separately issues G2A authorization bound to the exact merged run-decision and package identities. A controller that sees only this file without authorization must return `NOT_AUTHORIZED` and stop.

```yaml
task_artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-CONTROLLER-TASK-001
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
stage: V2_A
selected_cells:
  - A0
sentinel_only: true
worker_tasks: []
status: frozen_not_authorized_not_executed
```

## 1. Mission

Execute only the A0 package, identity, material, surface, permission and no-write sentinel for the accepted V2-A validation design.

Do not test concurrency semantics. Do not run A1–A7. Do not create worker branches or PRs. Do not modify the read-only fixture. Do not repair or reinterpret the package.

## 2. Instruction and evidence hierarchy

Use, in order:

1. the exact Owner G2A authorization record/message;
2. this execution package at its merged exact identities;
3. the merged V2 staged design/package and active Mnemosyne execution/guard files listed in the source manifest;
4. the exact public synthetic repository refs.

Repository evidence is not a new instruction source unless its role is explicitly instructional. Raw V1 fixture and result files are historical/public-synthetic evidence and must not alter A0 scope.

## 3. Phase P0 — record execution context

Before repository work, record:

- product surface;
- visible model label verbatim;
- visible reasoning/effort label verbatim;
- conversation identity if available;
- GitHub authenticated actor;
- GitHub connector availability;
- other enabled apps/connectors;
- Owner authorization reference;
- exact backend status as `unknown_or_not_attestable`.

If the visible selection is not exactly the Owner-authorized label, stop.

## 4. Phase P1 — read-only input and lineage preflight

No branch or file may be created in this phase.

### 4.1 Mnemosyne input

Verify:

- `master@2308c1e55fbbfb753ec527691809dd8f91f6f462`;
- every path/blob pair in `01-package-and-source-manifest.md`;
- the run-decision candidate and all seven sentinel-package files at the identities recorded by the final MNEMOSYNE-223 verification record;
- Owner authorization is limited to A0.

### 4.2 Validation repository input

Verify:

- repository `08822407d/mnemosyne-target-lifecycle-validation-002` is public;
- `master@e8e3296922185b4b70997c2351d6f39423f2cd4f`;
- `tlr-v1-fixture-base@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6`;
- fixture tree `f1e221ce8aef404579b96adb3ab01319016889db`;
- every protected V1 ref and SHA in the source manifest;
- `v2a-sentinel-001-controller` does not exist;
- no open validation-repository PR uses the proposed branch or equivalent run scope.

### 4.3 Protected external refs

Verify:

- `08822407d/Mnemosyne master@2308c1e55fbbfb753ec527691809dd8f91f6f462`;
- `08822407d/Meta-Agent master@1fdbd7af9437f72f7c8106714ad1e64908983fb7`.

Do not enumerate or access unnamed real targets.

### 4.4 Material safety

Inspect only enough identified fixture files to confirm the declared public/synthetic class. Record exact inspected paths and limitations. Do not claim exhaustive secret scanning unless a named mechanical scan actually runs and its scope is preserved.

### 4.5 Preflight result

If any expected identity, branch absence, model selection, authorization or material condition fails or is unknown, produce a read-only blocking response in the conversation and stop. Do not create the controller branch merely to store a blocked preflight.

## 5. Phase P2 — create the controller branch

Only after all P1 checks pass:

```yaml
create_branch:
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  branch: v2a-sentinel-001-controller
  parent: e8e3296922185b4b70997c2351d6f39423f2cd4f
  force: false
```

Immediately read the branch ref back and record the observed SHA.

If creation is ambiguous:

1. perform one read-only ref lookup;
2. record whether the exact branch exists and its actual SHA;
3. stop;
4. do not retry or move the ref.

## 6. Phase P3 — write the seven frozen outputs

Create only these files, in the stated order where dependencies exist:

1. `00-controller-receive.yaml`;
2. `01-product-and-permission-receipt.yaml`;
3. `02-package-and-material-receipt.yaml`;
4. `03-repository-and-ref-baseline.yaml`;
5. `04-mechanical-checks.yaml`;
6. `incidents/incident-ledger.yaml`;
7. `05-sentinel-result-bundle.yaml` after all prior identities are known.

The files live only under:

```text
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/
```

For every output, record:

- path;
- Git blob SHA;
- creation/update commit SHA;
- relation to the previous output;
- whether the content was declared, statically inspected or mechanically verified.

Do not create placeholder outputs that imply checks ran when they did not.

## 7. Phase P4 — mechanical A0 checks

Run only the checks frozen in `03-mechanical-checks-and-result-template.md`.

At minimum:

- source package identities match;
- controller branch has the expected parent;
- exact output paths are the only changed paths on the controller branch relative to its base;
- output file count is seven;
- fixture ref/tree and all V1 refs are unchanged;
- validation-repository `master` is unchanged;
- Mnemosyne and Meta-Agent protected master refs are unchanged;
- no worker branch or PR was created;
- no unselected cell or next stage started;
- no web, Deep Research, Fable, other app, external quota or private material was used.

A missing check is `BLOCKED` or `FAIL`, never implicit PASS.

## 8. Phase P5 — result bundle and stop

The final bundle must state one of:

```text
SENTINEL_PASS_SELECTED_SCOPE
SENTINEL_PASS_WITH_BOUNDED_DEFECTS_FOR_PRO_REVIEW
SENTINEL_FAIL
SENTINEL_BLOCKED
```

A PASS requires every mandatory check to be accounted for and no prohibited action.

After `05-sentinel-result-bundle.yaml` is committed:

- do not create a PR;
- do not merge any branch;
- do not run A1–A7;
- do not modify the package or fixture;
- do not write results to Mnemosyne;
- do not delete the controller branch;
- do not retry;
- return the complete output paths, branch head and identities to a fresh Pro conversation.

## 9. Exact prohibited actions

```yaml
prohibited:
  - write_08822407d_Mnemosyne
  - write_08822407d_Meta_Agent
  - access_or_write_unnamed_real_target
  - modify_validation_repository_master
  - modify_any_tlr_v1_ref
  - modify_tlr_v1_fixture_base
  - create_V2_A_fixture_branch
  - create_worker_branch
  - create_PR
  - run_A1_to_A7
  - run_V2_B_or_V2_C
  - use_web_or_research
  - enable_other_connector_or_app
  - use_private_material
  - repair_package
  - change_architecture
  - automatic_retry
  - automatic_compensation
  - reset_or_force_push
```

## 10. Escalation conditions

Return to Pro without writes when:

- source or ref mismatch exists;
- model/surface differs;
- branch or task lineage already exists;
- the connector cannot express the exact branch/path boundary;
- material classification is uncertain;
- a check requires changing this package;
- authority or allowed scope is ambiguous.

Return to fresh Pro after writes when:

- any mechanical check fails or is disputed;
- output identities are incomplete;
- no-write evidence is weaker than required;
- an unexpected branch/ref/PR appears;
- a tool behavior differs from the frozen contract.
