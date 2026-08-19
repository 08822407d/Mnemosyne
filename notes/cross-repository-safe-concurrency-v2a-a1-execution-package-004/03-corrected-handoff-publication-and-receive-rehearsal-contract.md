# V2-A A1 Package 004 — Corrected Handoff Publication and Receive-Rehearsal Contract

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-HANDOFF-PUBLICATION-CLOSURE-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-004
status: frozen_route_specific_contract_not_authorization
```

## Single-source delivery rule

The corrected handoff package and startup prompt are canonical repository artifacts. The user-visible launch message must be copied from the final merged startup artifact; it must not be manually re-authored from memory.

At final branch head and again after merge, mechanically compare:

- exact package path and package ID;
- exact handoff package blob;
- exact startup prompt path and blob;
- exact receive report key;
- candidate 004 and Package 004 manifest identities;
- actual source archive manifest blob `6e90c8f1384657939d5dcd9e7e30177e3c2e7b2a`;
- A1 unauthorized state.

Any difference blocks launch.

## Mandatory post-merge receive rehearsal

The originating conversation must not declare handoff complete or retire immediately after merge.

Required flow:

```text
merge repair PR
→ final merge-commit identity readback
→ open one fresh receive-only conversation
→ send the exact merged startup prompt once
→ receiver emits only mnemosyne_handoff_receive and stops
→ return the complete receive report to the originating conversation
→ originating conversation applies the rehearsal acceptance oracle
→ only on explicit REHEARSAL_ACCEPTED may the same receiver load guidance
→ receiver emits mnemosyne_guidance_refresh and confirms transferred task preserved
→ originating route may retire
```

The failed pre-repair receiver conversation is not reused for the rehearsal.

## Receive/continuation status separation

The receive report must distinguish:

```yaml
handoff_receive_status:
  RECEIVED | BLOCKED_PACKAGE_ABSENT | BLOCKED_PACKAGE_ID_MISMATCH
identity_verification_status:
  PASS | BLOCKED_LOAD_BEARING_IDENTITY_MISMATCH | INCOMPLETE
substantive_continuation_status:
  BLOCKED_PENDING_REHEARSAL_ACCEPTANCE_AND_GUIDANCE |
  BLOCKED_IDENTITY_OR_TASK_RECONSTRUCTION |
  READY_AFTER_SEPARATE_GUIDANCE_REFRESH
```

A package may be received while continuation remains blocked. Do not collapse both facts into one ambiguous scalar.

## Rehearsal acceptance oracle

The originating conversation may accept mechanically when all are exact:

- current master is the observed repair merge commit;
- package path, ID and blob match the merged startup artifact;
- candidate 004 and Package 004 manifest match;
- Package 004 file count is six;
- canonical archive-manifest path has blob `6e90c8f1384657939d5dcd9e7e30177e3c2e7b2a`;
- the independent reconstruction receipt records all five exact part blobs and source SHA-256 `6e639f7b49c8bfd6d47e950a7eb6cce54cf41c07903fb57fae3d0a29b7c2a4e0`;
- A1 remains unexecuted and unauthorized;
- no repository write, guidance load, G2A or unrelated route import occurred;
- the transferred task is the Package 004 fresh-Pro readiness route.

A next-tier originating conversation may apply this exact oracle. Any missing, unknown, extra or conflicting material requires at most one Pro adjudication turn before guidance load.

## Guidance boundary

For this task-specific handoff, guidance remains a separate operation after rehearsal acceptance. The corrected handoff package explicitly names:

```yaml
receiver_guidance_load:
  project_guidance: not_applicable
  mnemosyne_guidance: required
```

The broader Owner requirement to design future startup prompts that load all needed project/Agent guidance themselves is preserved in a separate detailed TODO and is not silently implemented here.

## Non-effects

This contract does not authorize A1, validation branches, G2A, package modification, global handoff-guidance changes, external research, cleanup or branch deletion.
