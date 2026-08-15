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
- the display-name registry entry for `MNE-DR-003 生命周期验证` with `Execute`, `S8` and `Review` suffixes.

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

Before V1 launch, replace branch-local identities with the exact merged MNEMOSYNE-212 commit/blobs and verify the synthetic repository still pins to the V0 final head.

## 3. Decision and authorization integrity

Confirm:

- V0 Pro adjudication accepts only a valid sentinel pass;
- V1 decision candidate is a recommendation, not authorization;
- this package does not self-authorize V1;
- V1 Owner authorization names the exact candidate, package, repository, pinned base, selected scenarios and three-conversation profile;
- S10 and V2 remain unauthorized;
- raw-result ingestion into Mnemosyne remains unauthorized;
- global architecture acceptance and target adoption remain separate Owner gates.

If a field affecting repository, scenario scope, material, write authority, S8 isolation or phase is missing, return `V1_BLOCKED_MISSING_OWNER_DECISION`.

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

No startup message or logical-cell contract may add S10, V2 or candidate amendments.

## 5. Frozen-semantics integrity

Check against candidate v0.2 and the frozen validation package:

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

Any contradiction returns `V1_PROTOCOL_PROFILE_CONFLICT` and blocks execution.

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
- S8 branches from the fixture commit and excludes S7 ancestry;
- scenario PRs remain absent unless later explicitly authorized;
- controller result refs point to immutable task-branch identities.

## 7. Three-conversation topology integrity

Verify actual UI conversations are exactly:

```yaml
conversations:
  - MNE-DR-003 Execute
  - MNE-DR-003 S8
  - MNE-DR-003 Review
```

Requirements:

- Execute runs controller/fixture, Core, S7, S11, prepares S8, pauses, then later performs closeout;
- logical cells remain separated by task branches/contracts/results inside Execute;
- S8 is a new next-tier conversation and receives no Execute transcript or S7 facts;
- Review is a new Pro conversation and has executed no V1 cell;
- actual visible model/mode and reasoning setting are recorded per conversation;
- inability to pause/resume Execute from exact S8 refs blocks or revises the profile rather than creating ad hoc chats.

## 8. S8 knowledge-firewall integrity

Before package acceptance and again before S8 launch, verify:

- S8 contract contains no concrete hidden v2 signature, argument replacement, removed key or return-object fields;
- S8 startup message does not instruct reading frozen package `01`;
- S8 receives only sanitized branch/input files;
- sufficient S7 guide/output are absent;
- S7 commits are not S8 ancestors;
- the S8 chat is fresh and has not received S7 facts;
- Alpha writes are prohibited;
- contamination causes invalidation, not an in-context retry.

If any condition fails or is unknown, S8 must not run.

## 9. Evidence identity integrity

Every produced V1 artifact includes:

- exact repository;
- branch;
- base/head commit;
- path;
- Git blob SHA;
- creation/update commit SHA;
- attempt/retry relation;
- declared and actual write set.

A commit alone does not substitute for file-content identity; a blob alone does not preserve the run transition. Both are required.

## 10. Material and connector integrity

Verify:

- synthetic repository remains public;
- materials remain public/synthetic;
- no credentials, private conversations, real source, learner or customer data;
- connector resolves/writes the exact synthetic repository in Execute and S8;
- GitHub permission does not substitute for task authorization;
- ChatGPT repository-sync selection is treated separately from GitHub access;
- no Web, Deep Research, Fable or other app is used;
- visible selections do not become backend claims.

## 11. Real-repository no-write integrity

Execute records before/after refs for:

- `08822407d/Mnemosyne`;
- `08822407d/Meta-Agent`.

The claim remains limited to:

- exact commit-level proof for those named repositories;
- no connector access/write action to unnamed real targets;
- no per-repository SHA claim for unnamed targets.

A changed named ref requires investigation and blocks the simple no-write pass. Do not assume every concurrent change was caused by V1.

## 12. Logical-cell and return integrity

Verify:

- Execute completes a valid receive before writes;
- fixture and S8 isolated input are prepared before S7 can affect any branch ancestry;
- Core runs only S1–S6 and S9;
- S7 runs only positive library/Alpha flow;
- S11 runs only synthetic backup/restore;
- Execute pauses before S8 and does not run S8 itself;
- S8 runs only isolated negative flow;
- Execute closeout begins only after exact S8 result refs return;
- closeout does not repair or rerun scenarios;
- final bundle contains every selected scenario, incident, retry, branch and proof;
- fresh Pro review is mandatory;
- Owner architecture decision remains pending after Pro review.

## 13. Operator-flow integrity

Confirm `06-startup-messages.md`:

- states `DO_NOT_RUN` before authorization;
- exposes the three `MNE-DR-003` names;
- gives exact model/surface recording instructions;
- includes the Execute launch, S8 launch, Execute closeout continuation and fresh Pro launch;
- keeps S8 instructions isolated;
- names stop conditions and prohibited actions;
- does not rely on repository navigation as the only operating procedure.

## 14. Pre-run receipt

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
  three_conversation_profile_match:
  S8_firewall_pass:
  material_safety_pass:
  connector_and_surface_pass:
  evidence_identity_contract_pass:
  no_write_contract_pass:
  operator_flow_pass:
  defects: []
  disposition: PASS | BLOCKED
```

Do not create V1 branches or run a logical cell unless disposition is `PASS`.

## 15. Post-run integrity

Before fresh Pro adjudication, verify:

- every selected logical cell stopped;
- V1 result bundle and no-write proof are complete;
- all exact identities are preserved;
- S8 contamination audit completed;
- V0 evidence unchanged;
- S10/V2 not executed;
- no raw result was written to Mnemosyne;
- no target adoption or cleanup occurred.
