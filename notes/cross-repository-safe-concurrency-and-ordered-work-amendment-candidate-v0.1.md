# Cross-Repository Safe Concurrency and Ordered Work — Pro Amendment Candidate v0.1

```yaml
candidate_id: MNEMOSYNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-PRO-AMENDMENT-001
version: 0.1.0
task_id: MNEMOSYNE-221
source_research: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
source_adjudication: notes/research-adjudications/MNE-DR-005-CROSS-REPOSITORY-SAFE-CONCURRENCY-PRO-ADJUDICATION-001.md
status: Pro_corrected_candidate_pending_Owner_disposition
relationship_to_target_lifecycle_candidate_v0_2: proposed_bounded_amendment_not_replacement
execution_source: false
validation_design_authorized: false
validation_execution_authorized: false
real_target_adoption_authorized: false
lock_or_lease_service_adopted: false
automatic_compensation_authorized: false
```

## 1. Purpose

This candidate preserves the accepted direction of Target Lifecycle candidate v0.2 and proposes only the additional semantics justified by MNE-DR-005.

It does not reopen Owner-confirmed invariants. It does not create a new orchestrator, lock service, schema implementation or validation run.

## 2. Minimum task-local contract semantics

A material repository-writing task should preserve at least:

```yaml
cross_repository_write_contract:
  task_id:
  authority_object_or_target:
  authority_owner:
  primary_repository:
  primary_base_ref:
  primary_base_identity:
  canonical_branch:
  canonical_PR:
  primary_writer:
  exact_write_set: []
  read_and_version_set:
    - repository:
      object_or_path:
      observed_identity:
      must_still_match_before_publication:
  generated_or_derived_effects: []
  shared_or_repository_global_objects: []
  semantic_contracts_affected: []
  active_conflicts_or_dependencies: []
  connector_or_tool_permissions:
    permitted_repositories: []
    permitted_actions: []
  ordered_repository_steps: []
  authorization_refs: []
  concurrency_disposition: proceed | serialize | reconcile | blocked
  failure_and_recovery_plan:
  final_diff_and_identity_evidence:
```

The exact serialization may remain task-specific. The meanings above must not be lost.

## 3. Corrected concurrency condition

Two tasks may proceed concurrently only when all relevant evidence supports non-interference:

- write/write intersections are empty;
- neither task writes a versioned object read by the other;
- pinned read/base identities remain current at publication;
- generated and derived outputs do not collide;
- no shared, repository-global, common authority or common provider/capability object changes;
- no semantic contract changed by one task is assumed unchanged by the other;
- neither depends on the other's uncommitted result;
- merge order does not change the intended result;
- task and PR lineages are distinct and canonical;
- final path/diff checks remain inside both declared contracts.

Unknown evidence means `serialize`, `reconcile` or `blocked`, not presumed independence.

## 4. Publication and stale-ref rule

For every publication step:

1. record the observed base/read identities;
2. immediately before write, push or merge, re-read the identities material to correctness;
3. use the strongest available conditional mechanism on that tool surface;
4. stop if the expected identity no longer matches;
5. do not automatically rebase or retry when the task assumptions may have changed;
6. verify the final repository and PR identities.

Tool-specific facts are dated evidence, not portable architecture:

- a REST ref update with only fast-forward protection requires an application-level expected-old check;
- a PR branch update may use `expected_head_sha`;
- a GraphQL ref update may use `beforeOid` when the selected surface exposes it.

## 5. Shared/global/unknown scope

Current default:

- serialize through the existing branch/PR/Owner gate;
- or perform explicit reconciliation;
- or block.

Do not introduce a distributed lease service merely to encode the current low-volume human serialization rule.

A future lease candidate requires all of:

- repeated measured contention;
- a named protected resource;
- a monotonic fencing/epoch token;
- destination-side stale-token rejection;
- failure and recovery tests;
- explicit Owner adoption.

TTL without fencing is insufficient.

## 6. Ordered cross-repository work

Cross-repository work is a sequence of separately authoritative repository actions, not a distributed ACID transaction.

Each step should record:

```yaml
ordered_step:
  step_id:
  repository:
  base_identity:
  write_scope:
  authorization_ref:
  predecessor_result_identity:
  publication_identity:
  reversible: true | false
  predeclared_recovery:
  retry_policy:
  next_step_gate:
```

Rules:

- a later step begins only after the predecessor's committed identity is verified;
- failure stops the sequence;
- forward repair or explicit revert is preferred;
- automatic compensation is permitted only if predeclared, authorized, idempotent and tested;
- destructive reset or force-push is not the default recovery for canonical/shared branches;
- a failed recovery escalates to a human/Owner gate with an incident record;
- evidence is corrected or superseded rather than silently erased.

## 7. No-dual-writer and cutover proof

A cutover should preserve:

- old and new authority identities;
- exact point at which the old writer authorization ends;
- exact point at which the new writer authorization begins;
- rejection evidence for any stale former writer;
- destination-only recovery;
- no competing current-truth copy;
- rollback/forward-repair boundary;
- Owner decision.

No-write evidence is scoped to named repositories, refs, actor surface and time window.

## 8. Evidence-strength vocabulary

Do not label ordinary task attestations as SLSA levels.

Use project-native evidence states such as:

```yaml
evidence_strength:
  declared:
  artifact_present:
  statically_inspected:
  mechanically_verified:
  runtime_executed:
  runtime_passed:
  independently_reproduced:
  platform_signed_or_independently_attested:
  known_limitations: []
```

A task records only states it can support.

## 9. Candidate validation stages

### V2-A candidate

Core concurrency, stale state, generated/semantic conflicts and duplicate lineage.

### V2-B candidate

Ordered cross-repository partial failure, recovery failure, cutover stale-writer rejection and backup authority misuse.

### V2-C candidate

Connector permission and private-material isolation under a separate security/product authorization.

No stage is authorized by this file. No stage automatically unlocks the next one or a real target.

## 10. Boundaries

This candidate does not:

- modify Target Lifecycle candidate v0.2;
- create a lock/lease/orchestration service;
- require GitHub Actions or a merge queue;
- permit automatic compensation;
- authorize V2 design or execution;
- authorize a real-target write;
- change Mnemosyne or Meta-Agent authority;
- change the execution source.
