# Target-Lifecycle V1 Evidence Preservation and Cleanup Validation v0.1

> Validation design for the preservation candidate. It defines a no-deletion archive-anchor stage and a separately gated cleanup stage. It is not execution authorization.

```yaml
validation_id: MNE-TARGET-LIFECYCLE-V1-EVIDENCE-PRESERVATION-VALIDATION-001
version: 0.1.0
task_id: MNEMOSYNE-218
status: PREPARED_NOT_SELECTED_NOT_EXECUTED
source_candidate: notes/evidence-preservation-designs/target-lifecycle-v1-evidence-preservation-and-cleanup-candidate-v0.1.md
source_manifest: notes/evidence-manifests/MNE-TARGET-LIFECYCLE-V1-BRANCH-EVIDENCE-MANIFEST-CANDIDATE-001.md
source_owner_decision: notes/owner-decision-results/MNE-TARGET-LIFECYCLE-V1-OWNER-ARCHITECTURE-DECISION-001.md
validation_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
archive_creation_authorized: false
cleanup_authorized: false
```

## 1. Validation question

Can the exact histories and identities of all retained Target-Lifecycle V1 evidence branches be anchored behind a smaller durable ref set without changing validation `master`, rewriting historical evidence, or authorizing deletion prematurely?

A second, independently authorized question is:

Can selected scenario branches later be deleted while every approved head, tree, result blob and ancestry remains reachable and mechanically recoverable from the anchor?

These questions must not be collapsed into one run.

## 2. Phase model

```yaml
phases:
  P0_READ_ONLY_PREFLIGHT:
    writes: none
  P1_CREATE_AND_VERIFY_ANCHOR:
    writes:
      - synthetic_archive_manifest_blob
      - synthetic_anchor_tree
      - synthetic_reachability_commit
      - tlr-v1-evidence-anchor-001_ref
    deletions: none
  P2_OWNER_CLEANUP_DECISION:
    writes: Owner_decision_record_only_if_separately_authorized
    deletions: none
  P3_DELETE_APPROVED_SCENARIO_REFS:
    writes: exact_ref_deletions_only
    prerequisites:
      - P1_passed
      - P2_explicit_cleanup_release
  P4_POST_DELETE_RECOVERY_PROOF:
    writes: none_unless_a_separate_result_storage_action_is_authorized
```

P1 must stop before P2. P3 must never be auto-triggered by a P1 pass.

## 3. Frozen P0 inputs

At execution time, P0 must re-read rather than trust the candidate snapshot.

Required objects:

- `08822407d/Mnemosyne@master`;
- Owner decision `MNE-TARGET-LIFECYCLE-V1-OWNER-ARCHITECTURE-DECISION-001`;
- preservation candidate and validation design exact blobs;
- public repository metadata for `08822407d/mnemosyne-target-lifecycle-validation-002`;
- validation `master`;
- all branches matching `tlr-v1-*`;
- controller bundle and branch/output inventory exact blobs;
- existing PRs, archive refs or concurrent preservation/cleanup tasks.

Required baseline expectations:

```yaml
expected_validation_master: e8e3296922185b4b70997c2351d6f39423f2cd4f
expected_controller_head: e892749fc9e242b24908f89b6a78f1c0f0bed75e
expected_controller_bundle_blob: 8a5f3644707ae518182ed352174e58d1ca419067
expected_branch_identity_blob: b881836d1a6dd7b7d2f748ad082048219b6d8337
expected_retained_branch_count: 16
expected_anchor_absent: true
```

## 4. P0 stop conditions

Return `PRESERVATION_PREFLIGHT_BLOCKED` and perform no write when:

- Mnemosyne source identities differ from the selected authorization;
- validation repository visibility is not public as expected;
- validation `master` moved;
- branch enumeration is incomplete;
- retained branch count, names or heads differ;
- controller bundle or branch-identity blob differs;
- an archive anchor already exists unexpectedly;
- another preservation/cleanup branch or PR is active;
- private or real-target material appears;
- exact low-level commit/tree writes are unavailable;
- the parent set or manifest cannot be frozen before the first write.

## 5. P1 construction contract

P1 may run only under a later Owner authorization naming:

- exact Mnemosyne candidate/validation blobs;
- exact validation repository;
- exact 16 input heads;
- anchor branch `tlr-v1-evidence-anchor-001`;
- allowed path `archive/MNE-TARGET-LIFECYCLE-V1-001/evidence-anchor-manifest.yaml`;
- no-deletion boundary;
- stop and return requirements.

Required sequence:

1. record before refs for Mnemosyne, Meta-Agent and validation `master`;
2. re-run P0 immediately before writes;
3. create the archive-manifest blob;
4. create a tree based on the exact controller-head tree, changing only the archive-manifest path;
5. create one commit with the controller head as first parent and the remaining 15 retained heads as additional parents;
6. verify the commit object before publishing a ref;
7. create `tlr-v1-evidence-anchor-001` at the exact collector commit;
8. re-read the anchor ref and all original refs;
9. run A0–A12;
10. store or return the complete result without deleting anything;
11. stop.

The commit must be labelled as a reachability anchor, not a semantic merge or accepted scenario state.

## 6. P1 mechanical checks

### A0 — Authorization and input identity

- exact Owner authorization exists;
- candidate/validation/manifest identities match;
- no deletion authorization is present or inferred.

### A1 — Repository and material class

- exact public synthetic repository;
- no private, real-target, learner, customer, credential or secret material.

### A2 — Complete branch enumeration

- exactly the expected 16 `tlr-v1-*` branches before anchor creation;
- no duplicate or unexpected preservation lineage.

### A3 — Head equality

- every original branch head equals the authorized head;
- no head is refreshed silently.

### A4 — Parent-set exactness

- collector commit has exactly 16 parents;
- parent set equals the authorized retained-head set;
- first parent is the controller head;
- no parent is omitted or added.

### A5 — Tree scope

- collector tree is based on the exact controller tree;
- only `archive/MNE-TARGET-LIFECYCLE-V1-001/evidence-anchor-manifest.yaml` is added or changed;
- no controller result or V0 path changes.

### A6 — Manifest identity

- manifest blob is recorded;
- branch-name/head mapping is exact;
- controller bundle/blob and fixture identity are exact;
- non-authority/no-cleanup wording is present.

### A7 — Default-branch immutability

- validation `master` before equals after;
- no PR or merge into validation `master` occurred.

### A8 — Original-ref immutability

- all 16 original branches exist after P1;
- all 16 still point to their original heads.

### A9 — Anchor ref identity

- exactly one `tlr-v1-evidence-anchor-001` ref exists;
- it points to the verified collector commit;
- no numbered replacement or alternate anchor exists.

### A10 — Key evidence identity

At minimum re-fetch and compare:

- controller bundle blob;
- branch/output inventory blob;
- fixture tree;
- all scenario result blobs named by the controller bundle;
- S8 result blob;
- S11 restore result blob.

### A11 — Named-real-repository no-write proof

- Mnemosyne before/after default branch equal during the synthetic operation, unless a separately authorized result-ingestion task is explicitly outside the run window;
- Meta-Agent before/after equal;
- unnamed real targets are not accessed merely to enlarge the claim.

### A12 — Deletion gate closed

- deleted refs: none;
- cleanup authorization: false;
- next state: `ANCHOR_VERIFIED_OR_BLOCKED_PENDING_SEPARATE_OWNER_CLEANUP_DECISION`.

## 7. P1 dispositions

```yaml
allowed_P1_dispositions:
  - ANCHOR_PASS_READY_FOR_SEPARATE_OWNER_CLEANUP_DECISION
  - ANCHOR_PASS_WITH_NONCRITICAL_OBSERVATION
  - ANCHOR_BLOCKED_INPUT_DRIFT
  - ANCHOR_BLOCKED_TOOL_CAPABILITY
  - ANCHOR_FAIL_PARENT_OR_TREE_IDENTITY
  - ANCHOR_FAIL_UNAUTHORIZED_WRITE
  - ANCHOR_FAIL_EVIDENCE_MISMATCH
```

No P1 disposition authorizes P3.

## 8. P2 Owner decision package

After P1 passes, the Owner must receive a bounded decision package containing:

- anchor branch, commit, tree and manifest blob;
- all original branch before/after refs;
- validation `master` before/after;
- exact parent-set proof;
- any incidents or retries;
- proposed deletion list;
- proposed retained navigation refs;
- recovery-proof plan;
- explicit `delete none / delete selected scenario refs / defer / reject premise / other` options.

Recommendation remains to retain:

- `tlr-v1-controller`;
- `tlr-v1-fixture-base`;
- `tlr-v1-evidence-anchor-001`.

The Owner may choose to retain all 16 branches instead. P1 success does not create a cleanup obligation.

## 9. P3 deletion contract

P3 requires a new task ID, new exact authorization and an exact branch list. Rules:

1. re-run P0 and verify the anchor unchanged;
2. verify every branch selected for deletion still equals its preserved head;
3. delete one ref at a time or in a tool sequence whose partial progress is fully visible;
4. stop immediately on any failed or ambiguous deletion;
5. never delete validation `master`, controller, fixture or anchor unless the Owner explicitly overrides the recommended retained set;
6. do not force-update any branch;
7. preserve every attempted deletion and result.

## 10. P4 post-delete proof

After P3, verify:

- every deleted branch name is absent;
- retained refs are present and exact;
- the anchor commit and all original head commits are fetchable by SHA;
- every original head is a direct parent of the anchor;
- controller bundle and all key blobs remain fetchable;
- validation `master` is unchanged;
- no real repository changed because of the cleanup;
- no open duplicate cleanup PR or branch remains.

A commit that cannot be fetched after deletion is a critical incident. Do not claim cleanup success.

## 11. Evidence strength

This validation is about Git identity and reachability, not scenario semantics or runtime correctness.

```yaml
evidence_scope:
  exact_ref_and_commit_identity: required
  exact_tree_and_blob_identity: required
  Git_object_reachability_through_anchor: required
  runtime_tests: not_applicable
  candidate_v0_2_revalidation: not_performed
  production_readiness: not_proven
```

## 12. Concurrent-write rule

Immediately before branch creation, immediately before the collector commit, immediately before anchor publication and immediately before any later deletion:

- re-read validation `master`;
- enumerate all relevant refs;
- check for active related PRs/tasks;
- compare exact heads.

If another conversation writes any relevant ref, stop and return the delta. Do not rebase, merge, refresh or delete around concurrent work automatically.

## 13. Boundaries

This design does not authorize:

- P1, P2, P3 or P4 execution;
- validation-repository writes or deletions;
- tags, bundles, releases or external archives;
- runtime supplement, S10, V2, Work, Deep Research or Fable;
- target adoption, Meta-Agent change, real-target change or execution-source change.
