# Target-Lifecycle V1 Evidence Preservation and Cleanup Candidate v0.1

> Provisional design for preserving branch-unique public/synthetic V1 evidence before any optional branch cleanup. This candidate does not authorize archive construction, branch deletion, runtime execution, target adoption, or validation-repository writes.

```yaml
candidate_id: MNE-TARGET-LIFECYCLE-V1-EVIDENCE-PRESERVATION-CANDIDATE-001
version: 0.1.0
task_id: MNEMOSYNE-218
status: PREPARED_NOT_OWNER_ACCEPTED_NOT_EXECUTED
source_run_id: MNE-TARGET-LIFECYCLE-V1-001
source_owner_decision: notes/owner-decision-results/MNE-TARGET-LIFECYCLE-V1-OWNER-ARCHITECTURE-DECISION-001.md
source_manifest: notes/evidence-manifests/MNE-TARGET-LIFECYCLE-V1-BRANCH-EVIDENCE-MANIFEST-CANDIDATE-001.md
validation_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
current_retained_branch_count: 16
cleanup_authorized: false
validation_repository_write_authorized: false
```

## 1. Problem

The Owner accepted the V1 architecture result while explicitly retaining every `tlr-v1-*` evidence branch until all three gates are satisfied:

1. a durable evidence-ref or archive mechanism exists;
2. branch-unique evidence is verified preserved;
3. the Owner gives an explicit cleanup release.

The controller bundle records exact commits and blobs, but a text record of a SHA does not by itself guarantee long-term reachability after every Git ref to that commit is removed. At the same time, the validation repository is public, small (about 95 KiB at observation), and currently has only 16 evidence branches. There is no storage emergency.

The engineering objective is therefore not “delete branches quickly.” It is:

> preserve exact Git history and result identity with the smallest understandable mechanism, keep cleanup reversible until the final Owner gate, and avoid adding more archival complexity than the current branch burden justifies.

## 2. Goals

The design must:

- preserve the exact commit graph for every retained V1 branch;
- preserve the mapping from original branch name to exact head;
- preserve the controller bundle, fixture, scenario results, S8 isolation evidence and S11 restore history;
- keep validation-repository `master` unchanged;
- avoid rewriting historical branches or result files;
- permit mechanical proof before and after any later cleanup;
- separate archive creation from branch deletion;
- stop on concurrent drift rather than reconciling it silently;
- keep the Owner's cleanup decision explicit.

## 3. Non-goals

This design does not:

- prove candidate v0.2 again;
- run synthetic tests or a runtime supplement;
- ingest raw V1 evidence into Mnemosyne;
- move evidence into Meta-Agent or a real target;
- select production backup providers;
- authorize S10, V2, Work, Deep Research, Fable or external quota;
- turn an archive ref into target truth or execution source.

## 4. Considered options

### Option A — Keep all 16 branches indefinitely

Advantages:

- simplest and already working;
- branch names are directly readable;
- no new Git mechanism or deletion risk;
- no implementation work.

Disadvantages:

- branch list remains permanently cluttered;
- later operators may not know which refs are immutable evidence;
- accidental branch movement remains possible unless separately controlled;
- no compact closure artifact exists.

This remains a valid default while branch burden is low.

### Option B — One tag per retained head

Advantages:

- native Git reachability;
- exact one-to-one mapping;
- branches could be removed while tags preserve commits.

Disadvantages:

- creates 16 additional refs;
- tag mutability and naming still need governance;
- the current connected write surface has no verified tag-creation action;
- does not materially reduce ref count.

Not selected as the current recommendation.

### Option C — One reachability-anchor commit and branch

Create a dedicated archive branch whose head is a **reachability-only multi-parent commit**. Its parents are the exact 16 retained branch heads. Its tree is based on the V1 controller tree and adds one self-describing archive manifest.

Advantages:

- one durable ref keeps every original branch head and its ancestry reachable;
- original branch names and heads are preserved in the manifest;
- no scenario branch is merged into `master`;
- original branches remain unchanged;
- the current GitHub connector exposes the low-level blob/tree/commit/ref operations needed to construct it;
- direct-parent equality is mechanically checkable.

Disadvantages:

- a many-parent commit is unusual and can be mistaken for a semantic merge;
- the anchor branch itself must be retained and protected by process;
- a moved or deleted anchor ref would weaken reachability unless another archive exists;
- it is more complex than simply keeping the current branches.

Selected as the **preferred future cleanup enabler**, not as an automatically executed action.

### Option D — External `git bundle` or equivalent exact repository archive

Advantages:

- strongest portable recovery artifact;
- preserves refs and commit graph outside GitHub;
- useful for disaster recovery and provider independence.

Disadvantages:

- requires a capable Git/Codex/local surface and exact binary preservation;
- current GitHub connector cannot generate a verified bundle directly;
- storage location, visibility, retention and pointer integrity require separate decisions;
- disproportionate if the only concern is 16 public synthetic branches.

Retained as an optional stronger layer, not required before the first preservation decision.

### Option E — Snapshot files or ordinary merges only

A file snapshot alone loses commit lineage. Merging all scenario branches into `master` or a normal content branch mixes mutually exclusive synthetic outcomes and changes the repository's navigational meaning.

Rejected as the primary preservation mechanism.

## 5. Recommended staged architecture

### Layer 0 — Current safe default

Keep all 16 branches unchanged. The manifest candidate freezes their observed names and heads for drift detection. No cleanup clock is started.

### Layer 1 — Optional reachability anchor

Only after a separate Owner authorization, create:

```text
branch: tlr-v1-evidence-anchor-001
```

Candidate construction:

```yaml
anchor_commit:
  semantic_role: reachability_only_not_a_semantic_merge
  first_parent: e892749fc9e242b24908f89b6a78f1c0f0bed75e
  additional_parents:
    - 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
    - d20f1239784f88072399a3c874800f6c94c0ad2c
    - b0923aedf551262f0b24409611824c526252982f
    - 1a8496893260f35b0b06d32d6b2128a192489ae7
    - 9a77045e77856a25336a664840aeaa984cdb8886
    - 4861cc27e8960353f29af9ca5cfa0927430b89ad
    - 2aa6c0a8a7ac39ab1d3e06a64006e83aff20b5aa
    - c77f20f0320313d1ccb2b4d1272dfa0daba8ef77
    - 8bfd56e5800566b048702d8b8a89e3bd05f9e6e9
    - e90fcc6633bae50236aa96f9c499ba6c7379f53f
    - be627df6a1e633e8c93f25c056b643b603f1aea8
    - 9cfae2953fa8d7b2ff4ab2e14abab263891932de
    - d9c4c88aa17d6edf73955054833bd2738709aec9
    - b16a458339497425387d71c843388ef30aa2eb46
    - 47262b6bf8f89c9ac13d7f488595f8adff250299
  tree_basis: exact_tree_of_controller_head
  only_added_anchor_path: archive/MNE-TARGET-LIFECYCLE-V1-001/evidence-anchor-manifest.yaml
  commit_message: >-
    MNE-TARGET-LIFECYCLE-V1-001 evidence reachability anchor;
    no semantic merge and no cleanup authorization
```

Using every retained head as a direct parent is intentionally redundant. It makes the required parent set exact and avoids relying on a later actor to infer which heads are maximal ancestors.

The archive manifest on the anchor branch must record:

- repository and visibility;
- anchor purpose and non-authority status;
- original branch names and heads;
- controller bundle path/blob;
- fixture commit/tree;
- Owner decision and cleanup prohibition;
- construction tool/surface and run context;
- exact anchor commit/tree/blob identities;
- validation result and limitations.

### Layer 2 — Verification with no deletion

Archive creation and verification form one bounded stage. The stage must leave all 16 original branches unchanged and stop after proving:

- branch heads matched the frozen input at launch;
- the anchor's parent set exactly equals the 16 retained heads;
- the anchor tree differs from the controller tree only by the archive manifest;
- validation `master` did not move;
- every original branch still points to the same head;
- controller bundle and key result blobs remain unchanged;
- no real repository changed because of this route.

### Layer 3 — Separate cleanup decision and execution surface

Branch deletion is a different task and a different Owner authorization. It must never be inferred from successful anchor creation.

The current standard GitHub connector exposes branch/ref creation and update but **does not expose a branch-ref deletion action**. Therefore any later cleanup task must run in a separately selected surface that can perform exact, auditable ref deletion, such as a suitable Codex/Git environment or a controlled human GitHub operation. The deletion surface, commands/actions, partial-failure handling and exact return evidence must be frozen before P3 begins.

Recommended cleanup scope, if the Owner later wants less branch clutter:

```yaml
retain_named_navigation_refs:
  - tlr-v1-controller
  - tlr-v1-fixture-base
  - tlr-v1-evidence-anchor-001

candidate_delete_after_separate_release:
  - tlr-v1-s1-destination-block
  - tlr-v1-s2-bounded-writer
  - tlr-v1-s3-alpha
  - tlr-v1-s3-beta
  - tlr-v1-s4-alpha-dependent
  - tlr-v1-s4-shared-schema
  - tlr-v1-s4-unknown-global
  - tlr-v1-s5-upstream-proposal
  - tlr-v1-s6-beta-requirement
  - tlr-v1-s7-alpha-migration
  - tlr-v1-s7-commonlib-v2
  - tlr-v1-s8-insufficient-docs
  - tlr-v1-s9-imperfect-route
  - tlr-v1-s11-backup-restore
```

Keeping controller and fixture provides readable navigation and replay inputs while the single anchor preserves all scenario commit histories. A later stronger archive may permit another decision, but this design does not recommend deleting those two branches now.

## 6. Concurrent-write and drift handling

The user reported another Mnemosyne conversation may write concurrently. This design therefore uses a separate Mnemosyne branch and new file paths only.

For the validation repository, any future implementation must fail closed when:

- an original branch is missing;
- any branch head differs from the approved manifest;
- a new V1 evidence branch appears;
- `master` moves;
- the controller bundle/blob changes;
- an existing archive anchor already exists unexpectedly;
- another cleanup or archival task is active.

No actor may silently “refresh” the parent list after drift. It must return a delta for Owner/frontier review.

## 7. Authority and reversibility

```yaml
authority:
  archive_design: candidate_only
  archive_creation: separately_gated
  branch_deletion: separately_gated_after_archive_verification
  target_adoption: not_authorized
  execution_source_change: not_authorized

reversibility:
  design_merge: reversible_by_later_candidate
  anchor_creation: additive_and_no_original_ref_change
  cleanup: destructive_ref_change_requires_explicit_Owner_release
```

## 8. Decision recommendation

The recommended immediate disposition is:

> Accept this as a preservation candidate, keep all current evidence branches unchanged, and do not create the anchor until branch cleanup becomes a real operational goal or the Owner explicitly selects the anchor stage.

This recommendation reflects the repository's small size and the absence of a current storage or navigation emergency. It prepares a mechanically verifiable route without manufacturing urgency.

## 9. Research and model assessment

- Deep Research: not needed. The decision is repository-local and supported by Git object/ref semantics plus current connector capabilities.
- Independent Fable review: not needed before candidate publication. It may be considered only if the Owner proposes deleting irreplaceable evidence without an external archive.
- Future anchor implementation: next-tier capable when the exact parent list, write set and checks are frozen; the current connector appears sufficient for P1 but this must be rechecked at launch.
- Future branch deletion: cannot be executed by the currently exposed standard GitHub connector because no delete-ref action is available; P3 requires another authorized surface.
- Any decision to delete evidence refs: Owner decision with frontier review recommended if the preservation proof is disputed.

## 10. Boundaries

This candidate does not authorize:

- writing the validation repository;
- creating `tlr-v1-evidence-anchor-001`;
- deleting or rewriting any branch;
- creating tags, bundles, releases or external archives;
- runtime supplement, S10, V2 or another validation run;
- Work, Deep Research, Fable, scheduled tasks or external quota;
- Meta-Agent, real-target or execution-source changes.
