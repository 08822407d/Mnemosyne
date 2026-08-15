# V1 Execution Package Integrity Checklist

> Historical V1 integrity checklist, prospectively amended for future profile reuse. The historical V1 remains bound to blob `2f0023dd20543a1b6d1213411cabdcdfa3d0d07b` and its exact result bundle.

```yaml
execution_package_id: MNE-TARGET-LIFECYCLE-V1-EXECUTION-PACKAGE-001
file_role: pre_merge_pre_authorization_pre_run_and_post_run_integrity
created_by_task: MNEMOSYNE-212
last_amended_by_task: MNEMOSYNE-215
status: HISTORICAL_RUN_COMPLETE_FUTURE_REUSE_AMENDED
historical_blob: 2f0023dd20543a1b6d1213411cabdcdfa3d0d07b
amendment_ref: notes/target-agent-lifecycle-v1-execution-package-001/08-owner-accepted-post-v1-amendment.md
```

## 1. Required-file inventory

Verify all package files exist at one pinned Mnemosyne commit:

- `README.md`;
- `00-controller-fixture-and-branch-contract.md`;
- `01-core-cell-s1-s6-s9.md`;
- `02-positive-documentation-cell-s7.md`;
- `03-fresh-negative-documentation-cell-s8.md`;
- `04-backup-restore-cell-s11.md`;
- `05-mechanical-closeout-and-return.md`;
- `06-startup-messages.md`;
- `07-integrity-checklist.md`;
- `08-owner-accepted-post-v1-amendment.md`.

Also verify:

- V0 and V1 adjudication records;
- V1 decision and Owner authorization;
- Owner architecture decision;
- candidate v0.2 and validation v0.2;
- `notes/validation-evidence-strength-levels-v0.1.md`;
- display-name registry entry for `MNE-DR-003 生命周期验证`.

## 2. Historical versus future identity

A historical V1 review uses the original exact blobs and controller bundle. A future reuse uses the current amended package at a newly pinned commit plus a new Owner authorization.

Do not:

- substitute current package blobs into the historical run manifest;
- describe prospective amendments as if they were present during V1;
- convert historical static inspection into runtime execution;
- infer standing execution authority from Owner acceptance of the architecture baseline.

## 3. Decision and authorization integrity

Confirm:

- V0 accepted only a sentinel pass;
- V1 historical execution was separately authorized;
- Owner global acceptance does not authorize a new V1, S10, V2 or target adoption;
- a future run names the exact repository, base, scenario set, materials, model/surface, write permissions, no-write scope, result retention and test-evidence claim;
- raw-result ingestion and evidence cleanup remain separately gated.

A missing field affecting repository, scenario scope, material, write authority, S8 isolation, test claim or phase blocks execution.

## 4. Scenario-scope integrity

Historical selected scenarios were exactly S1–S9 and S11; S10 was excluded and V2 unauthorized. A future authorization must state its own exact scope and may not inherit the historical selection implicitly.

## 5. Frozen-semantics integrity

Check:

- destination before substantive design/build;
- no parent/meta substantive target copy;
- bounded writer distinct from authority owner;
- proven disjoint concurrency allowed;
- shared/global/unknown scope serializes, reconciles or blocks;
- Owner-initiated upstream direction without standing write authority;
- target-local requirement remains local unless separately justified;
- library owns change documentation and project migrates on demand;
- human-facing and Agent-facing roles plus navigation;
- insufficient documentation blocks rather than causes invention;
- imperfect classification preserves source without forced taxonomy;
- backups remain non-authoritative and restore from exact source identity;
- TLR-03/TLR-04 deferrals remain explicit.

A contradiction returns a protocol-profile conflict and blocks execution.

## 6. Branch and write-set integrity

Verify every writing task has one task ID, one canonical branch and one recorded base. S3 uses two distinct task IDs by design. S7 Alpha depends on the preserved S7 library final commit. S8 branches from the fixture and excludes S7 ancestry.

For the fixture task, the exact allowed set must include:

```text
README.md
repository-governance/
targets/
libraries/
shared/
backups-fixture/
run-evidence/fixture/
```

Any other root file or path requires explicit authorization.

## 7. Three-conversation topology integrity

When this topology is selected, verify:

- Execute handles controller/fixture, Core, S7, S11, S8 preparation and closeout;
- S8 is a new next-tier conversation and receives no Execute transcript/S7 facts;
- Review is a new Pro conversation that executed no cell;
- visible model/mode and reasoning setting are recorded without backend claims;
- pause/resume and exact-result transfer work without ad hoc duplicate chats.

## 8. S8 knowledge firewall

Verify sanitized input, branch ancestry, absent sufficient guide, absent S7 output, fresh conversation attestation, Alpha write prohibition, exact worker diff and invalidation-on-contamination behavior.

## 9. Evidence identity integrity

Every produced artifact records repository, branch, base/head commit, path, blob, creation/update commit, attempt/retry relation and declared/actual write set. Both blob and commit identities are required where available.

## 10. Test-evidence claim integrity

For every test reference, record exactly one strongest established level from:

- `TEST_ARTIFACT_PRESENT`;
- `STATICALLY_INSPECTED`;
- `RUNTIME_EXECUTED`;
- `RUNTIME_PASSED`;
- optional `INDEPENDENTLY_REPRODUCED`.

Verify:

- T1/T2 are not described as “tests ran” or “tests passed”;
- T3 includes exact source, runtime/toolchain, environment, working directory, command, selected tests, time, exit code and log/result;
- T4 includes T3 plus complete success for the frozen required set;
- failures, missing imports, skips and inconclusive outcomes remain visible;
- no later static review retroactively upgrades a historical claim.

If runtime correctness is required by the selected validation claim and T3/T4 evidence is missing, block that claim. If runtime correctness is out of scope, record the limitation rather than inventing a pass.

## 11. Material and connector integrity

Verify public/synthetic material, no credentials/private/real data, exact connector repository, platform permission distinct from task authority, and no unauthorized Web/Deep Research/Fable/other app use. Visible selections are not backend attestations.

## 12. Real-repository no-write integrity

Record before/after refs for exact named real repositories. Keep claims limited to observed names and connector actions. A changed ref requires investigation and blocks a simple no-write pass.

## 13. Logical-cell and return integrity

Verify receive before writes, S8 preparation before contamination, exact cell scopes, closeout only after S8 refs, no silent repair/rerun, complete bundle, fresh Pro review and Owner decision separation.

## 14. Operator-flow integrity

Startup instructions must expose the selected topology, exact model/surface recording, stop conditions, prohibited actions, test-evidence claim level and result handoff. Repository navigation alone is not an operating procedure.

## 15. Pre-run receipt

```yaml
V1_execution_package_integrity_receipt:
  Mnemosyne_commit:
  package_version:
  amendment_ref:
  required_files_present:
  source_identities_match:
  new_Owner_authorization_present:
  selected_scenario_set_matches:
  frozen_semantics_match:
  fixture_README_write_scope_match:
  branch_map_unique:
  conversation_profile_match:
  S8_firewall_pass:
  test_evidence_contract_ref:
  requested_test_claim_level:
  material_safety_pass:
  connector_and_surface_pass:
  evidence_identity_contract_pass:
  no_write_contract_pass:
  operator_flow_pass:
  defects: []
  disposition: PASS | BLOCKED
```

Do not create branches or execute a cell unless disposition is PASS.

## 16. Post-run integrity

Before adjudication verify every selected cell stopped, bundle/no-write proof are complete, all identities and attempts are preserved, S8 contamination audit is complete, V0 evidence unchanged, excluded phases did not run, no raw result was written to Mnemosyne, no target adoption/cleanup occurred, and every test claim is supported by its recorded evidence level.

## 17. Current boundary

This checklist does not authorize a future run, runtime supplement, branch cleanup, target adoption, Meta-Agent write, execution-source change, Work pilot, S10, V2 or external quota.
