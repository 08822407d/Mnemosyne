# Context and Fixed Boundaries

```yaml
package_id: MNE-TARGET-LIFECYCLE-OWNER-REVIEW-001
question_range: TLR-01_through_TLR-05
```

## 1. Why this review exists

PR #273 preserved the Owner-confirmed OR-02 through OR-09 result and created candidate v0.1 for one combined architecture line:

- several logical Agents may share one physical repository;
- each Agent still needs a distinct truth/writer boundary;
- changes to Agent internals, business requirements, library APIs, provider adapters, and physical containers must not be conflated;
- a library should not default to an exhaustive manually maintained consumer/API reverse index;
- parent/meta repositories must not become temporary live target workspaces;
- backups are required and non-authoritative.

A Pro/frontier adjudication found no fatal contradiction, but identified implementation ambiguities that require repair and five bounded Owner decisions.

## 2. Decisions already fixed and not reopened

The interviewer must not ask the Owner to re-decide:

- formal destination repository/store before substantive target design/build;
- default prohibition on complete parent-repository bootstrap followed by migration;
- permission for several logical Agents to share one physical repository;
- distinct target authority and current truth for each Agent;
- no competing parent/meta writer;
- no automatic cross-target propagation after Mnemosyne/Meta-Agent changes;
- required non-authoritative backups;
- target-specific product and operational adoption decisions;
- OR-01 through OR-09 capability selections.

If the Owner explicitly revises one of these, record the new statement and mark `FRONTIER_REENTRY_REQUIRED`; do not silently treat it as an ordinary clarification.

## 3. What the five questions decide

- `TLR-01`: same-repository concurrency for mechanically disjoint write sets;
- `TLR-02`: consumer-owned dependency declarations, derived impact views, and bounded registration exceptions;
- `TLR-03`: primary change axis plus separately approved secondary effects;
- `TLR-04`: the narrow parent-owned design-brief exception;
- `TLR-05`: provisional semantic acceptance before synthetic validation, while target adoption remains blocked.

## 4. What this review does not do

It does not:

- create candidate v0.2;
- run the validation plan;
- create a synthetic repository;
- modify or activate Meta-Agent;
- create or modify code-library or language-learning target repositories;
- approve a specific monorepo layout;
- approve private-material storage or access;
- configure GitHub, Claude, ChatGPT, Skills, Projects, connectors, or backups;
- start Deep Research or Fable;
- update Mnemosyne's execution source or active guards.

## 5. Source and context-fidelity boundary

The exact long ChatGPT conversation export was not stored when result 002 was written. The repository source for this review is therefore the Owner-confirmed normalized result plus the later candidate/adjudication files—not the interviewer's recollection of the old conversation.

This package deliberately makes the next-tier interaction self-contained. The interviewer must not claim that being in the same conversation proves access to every earlier message. If a later exact export is supplied, it may support a bounded transcript-to-result audit, but it is not required unless a concrete discrepancy is alleged.

## 6. Current authority

`current/human-approved-spec.md` remains Mnemosyne's only execution source. All package, result, candidate, status, validation, and handoff files are non-execution-source records.

## 7. Safe default on deferral

If the Owner defers a question:

- preserve candidate v0.1 and the frontier adjudication;
- do not create v0.2 for the deferred scope;
- do not run validation that depends on the unresolved choice;
- do not adopt the candidate in any target;
- continue only with independent questions whose answers are not invalidated.
