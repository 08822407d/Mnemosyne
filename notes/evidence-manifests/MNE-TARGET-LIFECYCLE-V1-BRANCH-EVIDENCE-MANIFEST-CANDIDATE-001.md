# Target-Lifecycle V1 Retained-Branch Evidence Manifest — Candidate 001

> Read-only inventory candidate for the retained public/synthetic evidence of `MNE-TARGET-LIFECYCLE-V1-001`. This file records observed refs and durable evidence links; it does not create an archive ref, authorize cleanup, delete a branch, modify the validation repository, or make any evidence branch an execution source.

```yaml
manifest_id: MNE-TARGET-LIFECYCLE-V1-BRANCH-EVIDENCE-MANIFEST-CANDIDATE-001
task_id: MNEMOSYNE-218
status: CANDIDATE_OBSERVED_REFS_NOT_CLEANUP_AUTHORITY
observed_at_Mnemosyne_master: 6c453b547de2f717f5cf1e86b3881aad51e83c6a
source_owner_decision: notes/owner-decision-results/MNE-TARGET-LIFECYCLE-V1-OWNER-ARCHITECTURE-DECISION-001.md
source_validation_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
repository_visibility: public
repository_size_kib_at_observation: 95
default_branch: master
default_branch_head: e8e3296922185b4b70997c2351d6f39423f2cd4f
controller_branch: tlr-v1-controller
controller_head: e892749fc9e242b24908f89b6a78f1c0f0bed75e
controller_bundle_path: runs/MNE-TARGET-LIFECYCLE-V1-001/06-v1-result-bundle.yaml
controller_bundle_blob: 8a5f3644707ae518182ed352174e58d1ca419067
cleanup_authorized: false
archive_anchor_created: false
validation_repository_written_by_MNEMOSYNE_218: false
```

## 1. Current retained refs

The GitHub branch listing and the exact controller result bundle agree on the following retained evidence refs.

| Role | Branch | Observed head |
|---|---|---|
| V1 controller and normalized result bundle | `tlr-v1-controller` | `e892749fc9e242b24908f89b6a78f1c0f0bed75e` |
| Frozen initial fixture | `tlr-v1-fixture-base` | `81f18eb5dcc6a6e68e496f67ae8f8eae782226e6` |
| S1 destination block | `tlr-v1-s1-destination-block` | `d20f1239784f88072399a3c874800f6c94c0ad2c` |
| S2 bounded writer | `tlr-v1-s2-bounded-writer` | `b0923aedf551262f0b24409611824c526252982f` |
| S3 Alpha-local task | `tlr-v1-s3-alpha` | `1a8496893260f35b0b06d32d6b2128a192489ae7` |
| S3 Beta-local task | `tlr-v1-s3-beta` | `9a77045e77856a25336a664840aeaa984cdb8886` |
| S4 dependent Alpha task | `tlr-v1-s4-alpha-dependent` | `4861cc27e8960353f29af9ca5cfa0927430b89ad` |
| S4 shared-schema task | `tlr-v1-s4-shared-schema` | `2aa6c0a8a7ac39ab1d3e06a64006e83aff20b5aa` |
| S4 unknown/global task | `tlr-v1-s4-unknown-global` | `c77f20f0320313d1ccb2b4d1272dfa0daba8ef77` |
| S5 upstream proposal | `tlr-v1-s5-upstream-proposal` | `8bfd56e5800566b048702d8b8a89e3bd05f9e6e9` |
| S6 Beta-local requirement | `tlr-v1-s6-beta-requirement` | `e90fcc6633bae50236aa96f9c499ba6c7379f53f` |
| S7 Alpha migration | `tlr-v1-s7-alpha-migration` | `be627df6a1e633e8c93f25c056b643b603f1aea8` |
| S7 CommonLib v2 | `tlr-v1-s7-commonlib-v2` | `9cfae2953fa8d7b2ff4ab2e14abab263891932de` |
| S8 insufficient-docs negative cell | `tlr-v1-s8-insufficient-docs` | `d9c4c88aa17d6edf73955054833bd2738709aec9` |
| S9 imperfect-route evidence | `tlr-v1-s9-imperfect-route` | `b16a458339497425387d71c843388ef30aa2eb46` |
| S11 backup/restore | `tlr-v1-s11-backup-restore` | `47262b6bf8f89c9ac13d7f488595f8adff250299` |

Total retained `tlr-v1-*` branches: **16**.

## 2. Exact controller evidence

The controller bundle at blob `8a5f3644707ae518182ed352174e58d1ca419067` binds:

- fixture commit and tree;
- every scenario branch/head;
- every scenario result blob;
- cell result blobs;
- declared-versus-actual write sets;
- branch/output identities;
- S8 isolation evidence;
- final no-write proof;
- S11 restore evidence;
- incident ledger;
- the mechanical closeout disposition.

The more detailed branch/output inventory remains:

```text
08822407d/mnemosyne-target-lifecycle-validation-002
tlr-v1-controller@e892749fc9e242b24908f89b6a78f1c0f0bed75e
runs/MNE-TARGET-LIFECYCLE-V1-001/mechanical/branch-and-output-identities.yaml
blob b881836d1a6dd7b7d2f748ad082048219b6d8337
```

This manifest does not duplicate every result blob. It preserves the branch-name-to-head mapping needed to assess later ref cleanup and points to the canonical detailed inventories.

## 3. Evidence-preservation limitation

A commit SHA recorded in a Markdown file identifies an object but does not by itself guarantee that GitHub will retain an otherwise unreachable object forever after all refs are deleted.

Therefore:

```yaml
hash_only_manifest:
  supports:
    - identity_comparison
    - drift_detection
    - branch_head_reconciliation
  does_not_by_itself_support:
    - guaranteed_long_term_object_reachability_after_ref_deletion
    - branch_cleanup_authority
    - recovery_proof_after_ref_deletion
```

The present branches remain the live reachability refs until a separately authorized archive mechanism is created and validated.

## 4. Drift rule

Before any archive-anchor creation or cleanup task:

1. re-enumerate all branches in the validation repository;
2. compare every retained branch head with this manifest;
3. compare the controller bundle and branch/output inventory blobs;
4. stop on any new branch, missing branch, moved head, rewritten evidence, or default-branch change;
5. preserve the delta and return for review rather than silently updating the cleanup input.

This candidate inventory is an observed baseline, not permission to force current refs back to these values.

## 5. Boundaries

This file does not authorize:

- a reachability-anchor commit or branch;
- tags, releases, bundles, exports, or repository archival;
- deletion, rewriting, force-pushing, merging, or closing any evidence branch;
- writes to the validation repository;
- runtime supplement, S10, V2, target adoption, Work, Deep Research, or Fable;
- modification of Meta-Agent, a real target, or `current/human-approved-spec.md`.
