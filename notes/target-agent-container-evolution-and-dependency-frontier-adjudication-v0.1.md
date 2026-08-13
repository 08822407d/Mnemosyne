# Target Agent Container, Evolution, and Dependency Model — Frontier Adjudication v0.1

> Pro/frontier adjudication of the MNEMOSYNE-205 candidate. This is non-execution-source design evidence. It does not adopt the model in any target, authorize validation execution, modify Meta-Agent, create a target repository, or authorize private-material access.

```yaml
adjudication_id: MNE-TARGET-LIFECYCLE-FRONTIER-ADJUDICATION-001
task_id: MNEMOSYNE-206
source_master: c7e97baa39d9f107aab8294aeab0c2581c219e7a
source_PR: 273
source_candidate: notes/target-agent-container-evolution-and-dependency-model-candidate-v0.1.md
source_validation_plan: notes/validation-designs/target-agent-container-evolution-and-dependency-model-validation-v0.1.md
owner_result_ref: notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-RESULT-002.md
status: frontier_adjudication_complete_owner_decisions_pending
execution_source_modified: false
target_adoption_authorized: false
validation_execution_authorized: false
```

## 1. Bottom-line judgment

Candidate v0.1 is directionally coherent and preserves the Owner-confirmed architecture:

- formal destination before substantive target construction;
- no complete target bootstrap in a parent/meta repository;
- logical Agent authority is distinct from the physical repository container;
- several Agents may share one physical repository;
- meta-system, business, library/API, and provider-adapter changes are not the same event;
- exhaustive library-side consumer tracking is not the default;
- backups are required and non-authoritative.

No fatal contradiction was found. The candidate should nevertheless **not be adopted as written** because several fields and process rules can be misread in ways that recreate dual writers, stale reverse indexes, or hidden cross-axis propagation.

The recommended disposition is:

> retain the Owner-confirmed invariants; repair the operational model; obtain five bounded Owner decisions; then freeze a v0.2 candidate and run the prepared public/synthetic validation before any target adoption.

## 2. Fixed decisions not reopened

The review package prepared from this adjudication must not reopen:

1. a business Agent needs a formal repository/store before substantive design/build;
2. complete target construction in Mnemosyne, Meta-Agent, or another parent repository is prohibited by default;
3. one logical Agent does not necessarily require one physical repository;
4. each Agent needs a distinct current-truth and writer-authority boundary;
5. parent/meta systems may retain bounded design/evidence/pointers but not competing target truth;
6. automatic cross-target propagation is not authorized;
7. backups are required and cannot become independent current writers;
8. target and product adoption remain target-owned decisions.

## 3. Required repairs

### F1 — Separate authority ownership from task execution

Candidate v0.1 uses `active_writer` and `allowed_secondary_writers` in one authority map. This can be misread as allowing several independent current writers.

The refined model should separate:

```yaml
target_authority:
  authority_owner:
  canonical_truth_paths: []
  target_root:
  prohibited_writers: []

write_policy:
  permitted_actor_roles: []
  concurrent_write_default:
  task_contract_required: true

task_write_contract:
  task_id:
  primary_target:
  primary_writer:
  exact_write_set: []
  read_set: []
  shared_or_global_objects_touched: []
  conflicting_active_write_sets: []
  decision: proceed | serialize | reconcile | blocked
```

The authority owner decides what is current. A task actor may be permitted to write within a bounded task without becoming a second authority owner.

### F2 — Use write sets and conflict classes for same-repository concurrency

“Different target roots” is necessary but not sufficient. Two tasks can still conflict through repository-wide configuration, a shared schema, generated indexes, lockfiles, or merge ordering.

The refined model should classify every repository-writing task as:

1. **target-local/disjoint** — write sets do not overlap and no shared/global object changes;
2. **shared-object** — a declared shared object changes;
3. **repository-global** — repository governance, common tooling, root configuration, or generated global state changes;
4. **unknown** — scope cannot be established.

Recommended default:

- target-local/disjoint tasks may proceed concurrently;
- shared-object and repository-global changes serialize or use an explicit reconciliation plan;
- unknown scope blocks concurrency;
- final mechanical path/diff verification is required.

This is a per-task concurrency rule, not a global permission for uncontrolled parallel PRs.

### F3 — Do not turn shared-object impact metadata into another manual reverse index

Candidate v0.1 includes `dependent_target_refs` under the shared object. A hand-maintained list could become the same stale consumer registry the Owner questioned.

Recommended default:

- each consuming target owns an explicit dependency declaration in its own truth;
- the shared-object/library owner maintains the object contract, version, changes, migration guidance, and exception notices;
- a repository-level impact view may be mechanically derived from consumer declarations;
- a manual registration list exists only for a bounded, reviewed exception with scope, owner, freshness rule, and release gate;
- an absent or stale impact view does not override the consumer's own dependency truth.

This permits impact analysis without making the library Agent responsible for a universal manually curated consumer database.

### F4 — Add primary-axis and secondary-effect records

The four evolution axes are valuable, but real changes can have cross-axis consequences. The refined model should avoid both extremes:

- conflating all change types; and
- pretending they can never affect one another.

Use:

```yaml
change_event:
  change_id:
  primary_axis: meta_capability | business_requirement | library_api | provider_adapter | physical_container
  primary_object:
  direct_effects: []
  secondary_effect_candidates:
    - affected_axis:
      evidence_or_reason:
      adoption_or_approval_required:
      status: proposed | accepted | rejected | not_applicable
  automatic_cross_axis_propagation: false
```

A meta-system change may create a separately justified business-artifact migration; a business change may require an API change; a provider change may expose a capability defect. None of those secondary effects is assumed merely from the primary event.

### F5 — Bound the parent-owned design-brief exception

The no-parent-bootstrap rule should not prohibit a meta-system from recording the design work it actually owns. The exception must be narrow enough that it cannot silently recreate a target workspace.

A parent-owned design brief may contain:

- the source requirement or a safe pointer;
- the design problem and target identity;
- candidate options, constraints, rationale, and unresolved questions;
- destination repository/store requirement;
- delivery manifest or target-package pointer;
- safe generalized feedback after target review.

It must not contain a live-looking target execution source, target current state, target handoff, target business truth, editable target memory, or a complete target directory tree awaiting migration.

### F6 — Define backup authority and independence precisely

“Non-editable backup” should mean **no independent human/Agent evolution**, not that synchronization can never write new snapshots.

Each backup snapshot should carry:

```yaml
backup_snapshot:
  target_id:
  source_repository_or_store:
  source_version:
  created_by_controlled_sync:
  backup_location:
  content_scope:
  integrity_identity:
  independent_editing_allowed: false
  restore_test_ref:
```

The two backup locations should be independent enough that one account, credential, accidental deletion, or provider failure is unlikely to destroy both. The exact provider/account design remains a later product/privacy decision.

## 4. Recommended refined architecture

After Owner review, the v0.2 candidate should use the following compact model:

1. **Authority unit:** logical target root plus authority map; physical repository is only the container.
2. **Write unit:** one task write contract with an explicit write set.
3. **Concurrency:** allowed only for mechanically disjoint target-local write sets; shared/global/unknown work serializes or reconciles.
4. **Shared objects:** explicit owner and contract; consumer-side dependency declarations; derived impact views; bounded registration exceptions.
5. **Evolution:** one primary axis plus explicit secondary-effect candidates; no automatic cross-axis propagation.
6. **Parent/meta record:** bounded design brief and pointers only, never a live target bootstrap.
7. **Library responsibility:** API/version/change/migration contract; consumers own their dependency and upgrade work.
8. **Backup:** one authoritative primary plus two controlled non-authoritative snapshot locations and tested restore.

## 5. Owner decisions still required

The technical repairs above preserve the Owner's already confirmed direction. Five bounded choices remain because they affect architecture, authority, or the adoption gate:

- `TLR-01` — whether mechanically disjoint target-root write sets may proceed concurrently in one physical repository;
- `TLR-02` — whether consumer-owned dependency declarations plus derived impact views replace a default manual reverse index;
- `TLR-03` — whether the primary-axis plus explicit-secondary-effect model is adopted;
- `TLR-04` — whether the narrow parent-owned design-brief exception is acceptable;
- `TLR-05` — whether to accept the repaired semantics as a provisional baseline before running synthetic validation, while prohibiting target adoption until validation is reviewed.

The prepared package explains each question and allows free-form modification, rejection, or deferral.

## 6. What can proceed automatically after the decisions

If the Owner confirms the five decisions without introducing a new architecture:

1. create candidate v0.2;
2. update the bounded validation plan to test the repaired contracts;
3. prepare one frozen next-tier validation task package;
4. do not run it until the Owner separately authorizes repository creation/writes and execution;
5. route semantic failures back to Pro/frontier;
6. keep target adoption separate.

## 7. Context-fidelity boundary

The exact OR conversation export is not stored in the repository. The authoritative basis for this route is therefore:

- the Owner-confirmed normalized result 002;
- capability selection v0.3;
- candidate v0.1 and validation v0.1;
- explicit later corrections in repository records.

Same-conversation model memory is not treated as exact source. A later exact conversation export may be preserved and used for a bounded transcript-to-result audit, but such an audit is not required to continue the current architecture review unless a specific discrepancy is alleged.

## 8. Research and validation assessment

- Deep Research: not needed for the five Owner decisions.
- Independent Fable/frontier review: optional only after the architecture is frozen enough to identify a non-duplicative challenge question.
- Public/synthetic validation: recommended after provisional semantic acceptance and before target adoption.
- Current product verification: not needed for the provider-neutral architecture; defer to target implementation.
