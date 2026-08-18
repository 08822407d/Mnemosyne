# V2-A A1 Positive Independent Pair — Additive Execution Package 004

```yaml
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-004
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
stage: V2_A
selected_cells: [A1]
task_id: MNEMOSYNE-233
status: additive_source_identity_and_handoff_publication_closure_repair_not_authorized_not_executed
material_class: public_synthetic_only
```

Package 004 repairs one Package 003 publication-identity defect:

```text
Package 003 and its first handoff froze source archive manifest blob
7c2af723c395283aca23a5240847e46e6c97e93b,
while the canonical path on the merged PR #300 tree is
6e90c8f1384657939d5dcd9e7e30177e3c2e7b2a.
```

Independent deterministic reconstruction confirms the five archive parts reproduce the 37,074-byte source with SHA-256 `6e639f7b49c8bfd6d47e950a7eb6cce54cf41c07903fb57fae3d0a29b7c2a4e0`.

Package 004 supersedes only:

- the source-archive-manifest path/blob tuple inherited through Package 003;
- receive/startup identities derived from the incorrect tuple;
- the route-specific publication/readback/rehearsal closure needed before the old conversation retires.

Packages 001–003 remain immutable and control all non-delta A1 semantics.

Contents:

```text
README.md
00-delta-precedence-and-source-identity-correction-contract.md
01-package-and-source-manifest.md
02-independent-archive-reconstruction-and-identity-receipt.md
03-corrected-handoff-publication-and-receive-rehearsal-contract.md
04-package-integrity-and-non-execution-checklist.md
```

Publication is not G2A and authorizes no validation write or execution.
