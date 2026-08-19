# V2-A A1 Package 004 — Delta Precedence and Source-Identity Correction Contract

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-004-DELTA-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-004
status: frozen_additive_delta_not_authorization
source_defect: MNE-V2A-A1-PACKAGE003-SOURCE-ARCHIVE-MANIFEST-IDENTITY-DEFECT-001
```

## Historical preservation

Do not edit in place:

```text
notes/validation-run-decisions/
  MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-001.md
  MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-002.md
  MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-003.md

notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/
notes/cross-repository-safe-concurrency-v2a-a1-execution-package-002/
notes/cross-repository-safe-concurrency-v2a-a1-execution-package-003/

handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-handoff-package.md
handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-startup-prompt.md
notes/codex-task-results/MNEMOSYNE-232-verification.md
```

## Exact supersession scope

Package 004 controls only where a predecessor or derived publication artifact asserts:

```yaml
path: raw/validation-reviews/MNE-DR-005-A1-package002-readiness-review/exact-source/source-artifact-receipt-and-reconstruction-manifest.yaml
blob: 7c2af723c395283aca23a5240847e46e6c97e93b
```

The controlling tuple is:

```yaml
path: raw/validation-reviews/MNE-DR-005-A1-package002-readiness-review/exact-source/source-artifact-receipt-and-reconstruction-manifest.yaml
blob: 6e90c8f1384657939d5dcd9e7e30177e3c2e7b2a
```

Package 004 also controls the route-specific handoff package/startup/rehearsal artifacts created by MNEMOSYNE-233.

## Inherited scope

Package 003 continues to control canonical worker-wrapper transport, Owner-sent and worker-received preservation, controller three-way comparison, phase stops and object-side-effect disclosure.

Package 002 continues to control staged model-label binding.

Package 001 continues to control fixture, tasks/effects, expected blobs/trees, order construction, ten outputs, no-PR, no-retry, retention and evidence ceilings.

## Publication closure

No user-visible handoff launch instruction is valid until:

1. all repair files are frozen on the canonical branch;
2. all load-bearing paths/blobs are read back from the final branch head;
3. the Ready PR merges;
4. all load-bearing paths/blobs are read back from the merge commit/current master;
5. a fresh receive-only rehearsal returns an exact PASS-shaped report;
6. the originating conversation accepts the rehearsal before telling the receiver to load guidance.

No step authorizes A1.
