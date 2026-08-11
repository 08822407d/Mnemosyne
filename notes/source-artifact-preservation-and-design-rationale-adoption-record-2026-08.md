# Source-Artifact Preservation and Design-Rationale Guard — Adoption Record

```yaml
record_id: MNEMOSYNE-SOURCE-ARTIFACT-PRESERVATION-RATIONALE-ADOPTION-001
task_id: MNEMOSYNE-198
status: adopted_on_human_merge_of_MNEMOSYNE_198_PR
execution_source_modified: false
guard: current/source-artifact-preservation-and-design-rationale-guard.md
source_audit: notes/source-artifact-preservation-audit-2026-08.md
owner_instruction_refs:
  - current_conversation_2026_08_11_request_to_repair_source_preservation_and_task_recording
  - current_conversation_2026_08_11_request_to_verify_attachment_to_repository_exactness
  - issue_265_temporary_idea_comments
```

## Owner requirement recorded

The Owner can manually preserve complete conversation exports, research reports and external-model conversation/research files. The Owner cannot be expected to invent and perform every automatic task-side provenance or rationale step. Mnemosyne-related conversations and tasks therefore need durable behavior guidance that tells them what material records to create and how honestly to describe artifact preservation.

The Owner also requested a factual verification of whether sending a locally saved research report to a conversation inherently prevents exact repository preservation. The audit found that it does not: exact preservation is possible when raw attachment bytes are accessible and a byte-preserving Git path is used, while historical Mnemosyne workflows used a mixture of exact, reconstructable, normalized and identity-only storage.

## Adopted behavior

After merge, important Mnemosyne work should:

1. classify material source artifacts and record an explicit preservation level;
2. preserve exact supplied bytes when safe, authorized, proportionate and mechanically verifiable;
3. use manual import or approved outside-Git storage when direct exact preservation is unavailable or unsuitable;
4. never call a normalized copy or hash-only receipt an exact original;
5. preserve Deep Research report-export identity without claiming equality to an unobserved internal product representation;
6. capture a compact, externally stated design rationale for material architecture, behavior, authority, migration and methodology decisions;
7. avoid requesting or claiming hidden chain-of-thought;
8. keep exact originals cold/on-demand by default so preservation does not force routine context loading;
9. avoid mass historical backfill unless an active review, migration, incident or user-selected archival task needs it.

## Not adopted

This task does not adopt:

- automatic capture of every conversation or task;
- automatic upload or repository write;
- mandatory exact Git storage for every file;
- public storage of private originals;
- automatic reading of all preserved source files;
- automatic reconstruction of historical design reasoning;
- a RAG, database, MCP, indexing or background archival service;
- a claim that every historical research artifact is already exactly reconstructable.

## Relationship to existing rules

- `current/deep-research-report-delivery-correction-guard.md` continues to define one canonical Deep Research report and operator exports as representations of that report.
- `current/artifact-delivery-and-direct-generation-guard.md` continues to govern file-first delivery and local artifact creation.
- `current/run-context-and-pr-provenance-guard.md` continues to govern actor, model/surface and authorization provenance.
- The new guard controls exact-versus-normalized preservation claims, source-artifact receipts, compact design-rationale capture and on-demand reading of cold originals.

## Boundary

This record is non-execution-source evidence of the Owner-approved behavior repair. The guard remains subordinate to `current/human-approved-spec.md`, and external writes still require task-local authorization.
