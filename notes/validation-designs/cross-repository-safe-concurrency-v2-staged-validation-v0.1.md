# Cross-Repository Safe Concurrency and Ordered Work — Staged V2 Validation Design v0.1

> Public/synthetic design for the Owner-accepted provisional F2 amendment. This file prepares falsifiable validation stages and evidence contracts only. It does not create repositories, execute validation, change connector permissions, spend external quota, modify an architecture candidate, or authorize any real-target write.

```yaml
validation_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-STAGED-VALIDATION-001
version: 0.1.0
task_id: MNEMOSYNE-222
Owner_decision_ref: notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-OWNER-DECISION-001.md
source_amendment_ref: notes/cross-repository-safe-concurrency-and-ordered-work-amendment-candidate-v0.1.md
source_adjudication_ref: notes/research-adjudications/MNE-DR-005-CROSS-REPOSITORY-SAFE-CONCURRENCY-PRO-ADJUDICATION-001.md
relationship_to_target_lifecycle_candidate_v0_2: bounded_validation_extension_not_replacement
status: prepared_not_selected_not_executed
material_class:
  V2_A: public_synthetic_only
  V2_B: public_synthetic_only
  V2_C: design_only_pending_separate_security_and_product_authorization
real_target_material: prohibited
private_material: prohibited
validation_repository_created: false
connector_permissions_changed: false
validation_execution_authorized: false
external_quota_authorized: false
execution_source_modified: false
```

## 1. Objective

The validation asks whether the accepted provisional F2 amendment can distinguish genuinely independent work from hidden interference, preserve correct identity and authority across ordered repository steps, and stop safely when evidence or permissions are insufficient.

It is designed to falsify overconfident claims such as:

- disjoint paths are always safe to execute concurrently;
- a clean final diff proves freshness and semantic correctness;
- a later repository failure can always be automatically rolled back;
- an expired lease alone excludes a stale writer;
- one no-write proof covers unnamed repositories or action surfaces;
- a connector's physical ability implies task authorization;
- package preparation implies run authorization.

The design does not attempt to prove universal distributed-systems correctness or production readiness.

## 2. Stage topology

```yaml
stages:
  V2_A:
    title: core_repository_concurrency_and_stale_state
    material: public_synthetic
    required_repository_count: 1_controller_plus_1_fixture_repository_or_equivalent_isolated_fixture
    execution_authorized: false
    may_be_selected_independently: true

  V2_B:
    title: ordered_cross_repository_failure_and_recovery
    material: public_synthetic
    required_repository_count: 1_controller_plus_2_separate_fixture_repositories
    execution_authorized: false
    depends_on:
      - reviewed_V2_A_result_or_explicit_Owner_exception

  V2_C:
    title: connector_permission_and_privacy_boundary
    material: synthetic_but_permission_sensitive
    execution_authorized: false
    depends_on:
      - separate_security_and_product_contract
      - explicit_connector_or_app_identity
      - explicit_account_and_permission_change_authorization
```

Passing one stage does not authorize or validate another.

## 3. Roles

```yaml
roles:
  Owner:
    owns:
      - stage selection
      - repository creation and visibility
      - model/product surface and quota
      - connector/account permission changes
      - architecture acceptance and target adoption

  Pro_frontier_designer:
    owns:
      - frozen scenario and evidence design
      - explicit limitations and falsification criteria
    may_execute: false_by_design_preparation_alone

  controller:
    owns:
      - pinned fixture identities
      - task/branch/PR map
      - declared read_write_generated_and_semantic_sets
      - stage ordering
      - mechanical evidence collection
      - no-write scope
    must_not:
      - repair the candidate during execution
      - infer missing authorization
      - erase failure evidence

  worker:
    owns:
      - only the selected frozen task
      - exact result and limitation record
    must_not:
      - broaden write scope
      - auto_retry_after_identity_or_semantic_failure
      - use private_or_real_target_material

  fresh_Pro_adjudicator:
    owns:
      - executor_vs_fixture_vs_candidate_failure classification
      - evidence-strength judgment
      - amendment recommendation

  Owner_final_adjudicator:
    owns:
      - accept | revise | defer | reject
      - any later stage or real-target authorization
```

## 4. Shared evidence model

Each scenario must distinguish:

```yaml
evidence_strength:
  declared: true | false
  artifact_present: true | false
  statically_inspected: true | false
  mechanically_verified: true | false
  runtime_executed: true | false
  runtime_passed: true | false
  independently_reproduced: true | false
  platform_signed_or_independently_attested: true | false
  known_limitations: []
```

No report may promote a lower state into a higher one. In particular:

- a test file is not a runtime result;
- a self-attestation is not platform-signed provenance;
- a path-diff pass is not semantic non-interference;
- a controller refusal is not physical connector denial unless the provider surface enforces it and produces evidence.

## 5. V2-A hypotheses

### A-H1 — useful independent work is not globally serialized

When two distinct tasks have:

- separate task and PR lineages;
- disjoint writes;
- no read/write dependency;
- no generated/derived collision;
- no shared/global/authority effect;
- no merge-order dependence;

both merge orders should produce the same expected semantic result.

### A-H2 — generated or derived collisions defeat path-only independence

Two tasks may write separate source paths while changing the same generated index, lockfile or derived output. The contract must classify the collision before publication or block when it cannot.

### A-H3 — stale reads invalidate otherwise disjoint work

If one task changes an identity in another task's declared read/version set, publication must stop or reconcile even when their write sets are disjoint.

### A-H4 — mechanical green is not semantic green

A scenario with allowed paths and mergeable text but a broken declared interface or invariant must fail semantic acceptance.

### A-H5 — unknown/shared/global scope fails closed

Unknown scope must not be treated as independent. Shared or global work must serialize or use an explicit reconciliation contract.

### A-H6 — duplicate canonical lineage is rejected

A second PR for the same task must not become an alternative merge target.

## 6. V2-B hypotheses

### B-H1 — ordered identity handoff is explicit

A later repository step must record and revalidate the predecessor's committed identity before writing.

### B-H2 — later-step failure does not create false completion

If repository step 1 commits and step 2 fails, the run must preserve the partial state, report failure and stop. It must not claim atomic completion.

### B-H3 — recovery is separately authorized and bounded

A forward repair or explicit revert must have its own task/action identity, exact scope and authorization. The original actor does not gain open-ended rollback authority.

### B-H4 — failed recovery escalates

If the predeclared recovery cannot apply because identities moved or assumptions changed, automation stops and produces an incident/human gate.

### B-H5 — cutover rejects a stale former writer at the strongest proved layer

The validation must distinguish:

- logical task rejection;
- branch/PR protection rejection;
- connector/app permission denial;
- destination-enforced fencing.

V2-B may prove only the layers actually implemented on its synthetic surface. It must not claim provider-enforced stale-writer rejection unless observed.

### B-H6 — backups remain non-authoritative

A backup may restore an identified source state but cannot originate new current truth or become the live writer.

## 7. V2-C hypotheses

V2-C is a design-only stage in this package.

Possible later hypotheses include:

- an allowlisted connector can access only selected repositories/actions;
- an unlisted repository read is denied;
- an unlisted repository write is denied;
- denied actions produce provider-visible evidence sufficient for review;
- private/sensitive fixtures do not cross into public result storage;
- account-level permission changes are recorded separately from task authorization.

These cannot be honestly validated through task prompts alone. They require a separately selected product/app/account surface.

## 8. Failure attribution

Every failed scenario must be classified as one or more of:

```yaml
failure_attribution:
  executor_deviation:
  fixture_or_profile_defect:
  tool_or_product_surface_limitation:
  candidate_or_amendment_defect:
  insufficient_evidence:
  authorization_or_material_blocker:
  unresolved:
```

A controller must not silently edit the package and continue. Repairs create a new package version or a separately identified amendment.

## 9. Stage-level acceptance

### V2-A acceptance candidate

A stage-level PASS requires:

- the positive independent case succeeds without global serialization;
- all selected negative cases fail closed before invalid publication or produce an explicitly accepted semantic-failure result;
- stale identities are detected;
- duplicate lineage is rejected;
- final evidence distinguishes path, identity and semantic checks;
- no prohibited repository changes occur.

### V2-B acceptance candidate

A stage-level PASS requires:

- successful ordered handoff works;
- later-step failure is preserved without false atomicity;
- separately authorized recovery behaves as frozen;
- failed recovery stops and escalates;
- cutover/backup cases preserve authority boundaries at the actually tested enforcement level;
- no destructive default reset/force-push occurs.

### V2-C acceptance candidate

Defined only after a separate permission/security contract. This design does not provide a runnable V2-C PASS rule.

## 10. Required future Owner decisions

Before any run, the Owner must select:

- stage and scenario subset;
- synthetic repositories and visibility;
- exact base refs and permissions;
- executor/controller/adjudicator surfaces;
- whether external quota is allowed;
- retention and cleanup;
- result-storage paths;
- for V2-C, connector/app identity and account-level permission changes.

## 11. Explicit non-goals

This validation design does not:

- create a distributed transaction system;
- prove arbitrary semantic equivalence;
- require a lock service, GitHub Actions or merge queue;
- authorize automatic compensation;
- test private or real-target material;
- modify candidate v0.2 or the execution source;
- authorize a real target;
- make Fable or another provider report self-validating.
