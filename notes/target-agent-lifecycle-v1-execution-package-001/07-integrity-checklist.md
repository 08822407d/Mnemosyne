# V1 Execution Package Integrity Checklist

```yaml
execution_package_id: MNE-TARGET-LIFECYCLE-V1-EXECUTION-PACKAGE-001
file_role: pre_merge_pre_authorization_pre_run_integrity
status: prepared_not_executed
```

## 1. Required-file inventory

Verify all files exist at one pinned Mnemosyne commit:

- `README.md`
- `00-controller-fixture-and-branch-contract.md`
- `01-core-cell-s1-s6-s9.md`
- `02-positive-documentation-cell-s7.md`
- `03-fresh-negative-documentation-cell-s8.md`
- `04-backup-restore-cell-s11.md`
- `05-mechanical-closeout-and-return.md`
- `06-startup-messages.md`
- `07-integrity-checklist.md`

Also verify the same commit contains:

- `notes/validation-adjudications/MNE-TARGET-LIFECYCLE-V0-ADJUDICATION-001.md`;
- `notes/validation-run-decisions/MNE-TARGET-LIFECYCLE-V1-RUN-DECISION-CANDIDATE-001.md`;
- `notes/design-rationales/target-lifecycle-v1-staged-multicell-execution-v0.1.md`;
- the current display-name registry entry for `MNE-DR-003 生命周期验证`.

## 2. Source identity and lineage

Verify:

```yaml
source_contract:
  Mnemosyne_base_for_MNEMOSYNE_212: 930b5ed0c8d1db82e46fd9439035db3f2dd20c46
  V0_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  V0_final_head: e8e3296922185b4b70997c2351d6f39423f2cd4f
  candidate_blob: 1eaeffaf01b3eae878cd0a97cb5d1884b7dba3cc
  validation_blob: 364482a28ab9218c3a6beddb072be2545779132f
  frozen_package_README_blob: 444b7e7186e6e90002a1b9966bc69ff0e1b49aaa
  V0_authorization_blob: 25e330445c18cdd0833411d259a093c7a3ccfc61
```

Before V1 launch, replace branch-local identities with the exact merged MNEMOSYNE-212 commit and blobs and verify the synthetic repository still pins to the V0 final head.

## 3. Decision and authorization integrity

Confirm:

- V0 has a Pro adjudication accepting it only as a valid sentinel pass;
- V1 decision candidate is a recommendation, not authorization;
- this execution package does not self-authorize V1;
- V1 Owner authorization must name the exact candidate, package, repository, pinned base, selected scenarios and execution profile;
- S10 and V2 remain unauthorized;
- raw-result ingestion into Mnemosyne remains unauthorized;
- global architecture acceptance and target adoption remain separate Owner gates.

If an authorization field affecting repository, scenario scope, material, write authority, context isolation or phase is missing, return `V1_BLOCKED_MISSING_OWNER_DECISION`.

## 4. Scenario-scope integrity

Verify selected baseline scenarios are exactly:

```yaml
selected:
  - S1
  - S2
  - S3
  - S4
  - S5
  - S6
  - S7
  - S8
  - S9
  - S11
excluded:
  - S10
```

Verify no startup message or cell contract silently adds S10, V2 or candidate amendments.

## 5. Frozen-semantics integrity

Check the execution package against candidate v0.2 and the frozen validation package:

- destination before substantive design/build;
- no parent/meta substantive target copy;
- bounded writer distinct from authority owner;
- proven disjoint concurrency allowed;
- shared/global/unknown scope serializes, reconciles or blocks;
- Owner-initiated upstream direction without standing write authority;
- target-local business requirement remains local unless separately justified;
- library owns its change documentation and project migrates on demand;
- human-facing and Agent-facing documentation roles plus navigation;
- insufficient documentation blocks rather than causes invention;
- imperfect classification preserves source and avoids forced taxonomy;
- backups remain non-authoritative and restore from exact source identity;
- TLR-03/TLR-04 deferrals remain explicit.

Any semantic contradiction returns `V1_PROTOCOL_PROFILE_CONFLICT` and blocks execution.

## 6. Branch-map integrity

Verify every writing task has exactly one canonical branch and base rule:

- controller;
- fixture;
- S1;
- S2;
- S3 Alpha;
- S3 Beta;
- S4 shared;
- S4 dependent;
- S4 unknown;
- S5;
- S6;
- S7 library;
- S7 Alpha;
- S8;
- S9;
- S11.

Rules:

- no task gets a numbered fallback branch after collision;
- S3 uses two distinct tasks, not parallel variants of one task;
- S7 Alpha depends on the preserved S7 library final commit;
- S8 branches directly from the fixture commit and excludes S7 ancestry;
- scenario PRs remain absent unless a later authorization explicitly changes the profile;
- controller result refs point to immutable task-branch identities.

## 7. S8 knowledge-firewall integrity

Before package acceptance and again before S8 launch, verify:

- S8 contract contains no concrete hidden v2 signature, argument replacement, removed key or return-object fields;
- S8 startup message does not instruct the worker to read frozen package `01`;
- S8 worker receives only the sanitized branch/input files;
- sufficient S7 guide and output are absent;
- S7 commits are not S8 ancestors;
- the worker chat is fresh and has not received S7 facts;
- Alpha writes are prohibited;
- contamination causes invalidation, not an in-context retry.

If any condition fails or is unknown, S8 must not run.

## 8. Evidence identity integrity

Every produced V1 artifact must include:

- exact repository;
- branch;
- base and head commit;
- path;
- Git blob SHA;
- creation or update commit SHA;
- attempt/retry relation;
- declared and actual write set.

A commit identity alone does not substitute for file-content identity. A file/blob identity alone does not preserve the branch/run transition. Both are required.

## 9. Material and connector integrity

Verify:

- synthetic repository remains public;
- all materials are public/synthetic;
- no credentials/secrets/private conversations/real source/real learner or customer data;
- connector can resolve and write the exact synthetic repository in every writing cell;
- GitHub permission does not substitute for task authorization;
- ChatGPT repository-sync selection is treated separately from GitHub access;
- no Web, Deep Research, Fable or other app is enabled or used;
- exact visible model/mode is recorded per cell, without backend inference.

## 10. Real-repository no-write integrity

Controller records before and after refs for:

- `08822407d/Mnemosyne`;
- `08822407d/Meta-Agent`.

The claim must remain explicitly limited:

- exact commit-level no-write proof for the two named repositories;
- no connector access/write action to unnamed real targets;
- no per-repository SHA claim for unnamed targets.

A changed named ref requires investigation and blocks the simple no-write pass. Do not assume every concurrent repository change was caused by V1.

## 11. Cell and return integrity

Verify:

- Controller setup stops before scenarios;
- Core runs only S1–S6 and S9;
- S7 runs only positive library/Alpha flow;
- S8 runs only isolated negative flow;
- S11 runs only synthetic backup/restore;
- closeout does not run or repair scenarios;
- final bundle contains every selected scenario, incident, retry, branch and proof;
- fresh Pro review is mandatory and has not executed any cell;
- Owner architecture decision remains pending after Pro review.

## 12. Operator-flow integrity

Confirm `06-startup-messages.md`:

- states `DO_NOT_RUN` before authorization;
- exposes `MNE-DR-003` names;
- gives exact model/surface recording instructions;
- includes all cell launch messages and timing;
- keeps S8 instructions isolated;
- names stop conditions and prohibited actions;
- returns to a fresh Pro conversation;
- does not rely on repository navigation as the only operating procedure.

## 13. Pre-run receipt

```yaml
V1_execution_package_integrity_receipt:
  Mnemosyne_commit:
  required_files_present:
  source_identities_match:
  V0_adjudication_allows_V1_decision_only:
  V1_Owner_authorization_present:
  selected_scenario_set_matches:
  frozen_semantics_match:
  branch_map_unique:
  S8_firewall_pass:
  material_safety_pass:
  connector_and_surface_pass:
  evidence_identity_contract_pass:
  no_write_contract_pass:
  operator_flow_pass:
  defects: []
  disposition: PASS | BLOCKED
```

Do not create V1 branches or run a cell unless disposition is `PASS`.

## 14. Post-run integrity

Before fresh Pro adjudication, verify:

- every selected cell stopped;
- V1 result bundle and no-write proof are complete;
- all exact identities are preserved;
- S8 contamination audit completed;
- V0 evidence unchanged;
- S10/V2 not executed;
- no raw result was written to Mnemosyne;
- no target adoption or cleanup occurred.
