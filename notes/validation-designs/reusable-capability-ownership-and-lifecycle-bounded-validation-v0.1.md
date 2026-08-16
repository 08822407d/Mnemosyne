# Reusable Capability Ownership and Lifecycle — Bounded Validation Design v0.1

> Public/synthetic validation design for the Owner-accepted provisional model in `notes/reusable-agent-capability-ownership-and-lifecycle-model-candidate-v0.1.md`. This file prepares validation only. It does not build the business-function code-library Agent, modify Meta-Agent, write a real target repository, run validation, create a validation repository, or authorize external quota.

```yaml
validation_id: MNE-REUSABLE-CAPABILITY-OWNERSHIP-LIFECYCLE-BOUNDED-VALIDATION-001
package_id: MNE-REUSABLE-CAPABILITY-OWNERSHIP-VALIDATION-PACKAGE-001
task_id: MNEMOSYNE-225
source_master: 9157c476e8bf785f6440af4aaefbc44532d47c14
candidate:
  path: notes/reusable-agent-capability-ownership-and-lifecycle-model-candidate-v0.1.md
  blob: accb13ccb57677d316f5f94ef58f7939ad69521b
Owner_decision:
  path: notes/owner-decision-results/MNE-REUSABLE-CAPABILITY-OWNERSHIP-OWNER-DECISION-001.md
  blob: e75fa69cbbaa206e480a889ff3eb1302a6780d80
status: prepared_not_selected_not_executed
material_class: public_synthetic_only
real_target_construction: prohibited
Meta_Agent_write: prohibited
validation_execution_authorized: false
execution_profile_selected: false
```

## 1. Question being tested

The accepted F1 model proposes that:

- Mnemosyne currently owns the reusable capability catalogue;
- each target owns its own selected capability revisions, adaptations, implementation and current truth;
- a Mnemosyne-side impact view is derived and non-authoritative;
- upstream capability changes create review candidates, not automatic target writes;
- stable IDs and explicit revision, split, merge, supersession, deprecation and retirement relations may make long-lived target evolution safer;
- the mechanism must remain proportionate and must not become a large schema maintained for its own sake.

The validation asks whether these semantics work in a small realistic synthetic case and whether their decision value exceeds their maintenance burden.

## 2. What this validation is not

This is not the construction of the business-function code-library Agent.

A synthetic code-library target is used only because the Owner has already confirmed a useful high-level domain shape: requirements, decisions, implementation/tests, reusable-versus-local boundaries, API compatibility and change documentation. No real code, repository identity, customer material, private source, credentials, actual API or target instruction is used.

Future real construction belongs to the Meta-Agent route and the target's own repository authority. It is not started, required or pre-empted here.

## 3. Staged evidence plan

### Stage B0 — package and source integrity

Before any run:

- bind the exact candidate, Owner decision and package blobs;
- select an exact public/synthetic execution surface;
- prove that no real target, Meta-Agent or execution-source write is authorized;
- confirm the synthetic capability IDs cannot be mistaken for current `ACAP-*` catalogue entries;
- freeze the scoring, stop conditions and output paths.

B0 preparation is not execution authorization.

### Stage B1 — bounded synthetic lifecycle run

Run six small cells against one synthetic code-library target. The cells test selection, compatible revision, breaking revision, split/merge/retire relations, stale derived impact views and record burden.

B1 must use public/synthetic materials only. The exact repository/surface is a later Owner decision.

### Stage B2 — future real-use observation

If Meta-Agent later begins the separately authorized construction of a real business-function code-library Agent, the target route may collect limited observations about whether capability-selection and lifecycle records were useful.

B2 is not authorized by this design. It must not become a prerequisite that delays target construction once the target route is otherwise ready.

## 4. Invariants

Every selected profile and cell must preserve:

1. **Target-local authority** — only the synthetic target-local selection/current record controls the target's adopted capability state.
2. **Derived-view non-authority** — the Mnemosyne-side impact view may identify possible effects but cannot repair, overwrite or substitute for target truth.
3. **No automatic propagation** — an upstream revision may create an impact record or review candidate, never an automatic target change.
4. **Stable identity** — published synthetic capability IDs are not reused; relation changes are explicit.
5. **Decision-shaped records** — a required field must support an actual decision, verification, migration, recovery or impact question.
6. **Fail-closed uncertainty** — missing target selection, stale view, ambiguous relation or identity mismatch stops the affected action.
7. **Public/synthetic isolation** — no private material, real target files or provider/account secrets.
8. **Preserved failures** — an executor may not silently repair a failed cell and report only the repaired state.

## 5. Cells

| Cell | Purpose | Expected safe behavior |
|---|---|---|
| C1 | Initial target selection | Target-local selection records exact synthetic capability revisions; derived view remains a pointer/index only. |
| C2 | Compatible upstream revision | Impact review may conclude no action or future-only adoption; target stays unchanged unless its authority selects a revision. |
| C3 | Breaking upstream revision | Derived view identifies a possible impact and creates a target-specific review candidate; no target write occurs before target authority. |
| C4 | Split, merge and retirement | IDs remain stable; relation graph and compatibility notes identify the review path without silent replacement. |
| C5 | Stale or incorrect impact view | Target-local record wins; the stale view is regenerated or marked invalid, never used to rewrite target truth. |
| C6 | Schema-burden comparison | Minimum record is compared with an intentionally over-complex variant; unused/redundant fields are identified rather than normalized into permanent requirements. |

Exact fixtures and failure cases are defined in the package.

## 6. Evaluation dimensions

### R1 — authority fidelity

- Does target-local selection remain the sole target authority?
- Does any meta-side object become a competing truth source?

### R2 — lifecycle fidelity

- Are revision, compatibility, split, merge, supersession, deprecation and retirement represented without ID reuse or silent substitution?

### R3 — impact fidelity

- Can potentially affected targets be identified without claiming certainty beyond the available selection evidence?
- Does missing or stale evidence stop rather than guess?

### R4 — no-propagation fidelity

- Does upstream change stop at review/impact output until target authority acts?
- Is no standing target writer created?

### R5 — usefulness and burden

- Which fields changed a decision or enabled a check?
- How many records/files must change for a routine revision?
- Does the target need to read the whole catalogue?
- Does the model reduce re-explanation or merely add maintenance work?

### R6 — recoverability and provenance

- Can selection and relations be reconstructed from exact identities?
- Are source, candidate, decision, target truth and derived view distinguishable?

## 7. Acceptance boundary

A bounded synthetic pass requires:

- no authority or target-write violation;
- correct stop behavior for missing/stale identity;
- explicit and internally consistent lifecycle relations;
- target-specific review before a breaking revision affects target state;
- at least one demonstrated decision value for each retained required field;
- no critical burden finding that makes the minimum model disproportionate;
- exact output identities and preserved raw failures.

A pass means only:

> the model is suitable for later limited real-use observation.

It does not establish universal correctness, production readiness, target adoption, Meta-Agent adoption, shared-repository need or automatic propagation safety.

## 8. Failure and amendment classes

Classify findings separately as:

- candidate semantic defect;
- validation-protocol defect;
- executor defect;
- contamination or authority violation;
- missing evidence;
- disproportionate schema burden;
- noncritical observation;
- proposed amendment not yet adopted.

A target-domain feature request is not automatically an F1 global defect.

## 9. Stop conditions

Stop the affected run or cell when:

- the exact candidate, Owner decision or package identity does not match;
- the chosen surface would expose private/real target material;
- the execution profile would modify Mnemosyne, Meta-Agent or a real target;
- another active repository-writing route creates unresolved read/write, authority, merge-order or external-effect dependence;
- the worker needs to invent a missing target decision;
- a synthetic ID could be confused with an active catalogue identity;
- the executor attempts to repair a failure outside its declared output scope;
- the selected model repeatedly misses authority or lifecycle semantics.

## 10. Capability and review split

```yaml
capability_split:
  Pro_or_frontier:
    - approve_or_revise_validation_design
    - adjudicate_semantic_or_burden_failures
    - decide_candidate_amendment
  next_tier_candidate:
    - execute_a_frozen_self_contained_B1_package
    - produce_declared_outputs_only
  mechanical:
    - exact_blob_and_path_checks
    - relation_and_ID_checks
    - before_after_target_state_comparison
    - changed_path_and_output_identity_checks
  Owner:
    - select_or_defer_execution_profile
    - authorize_any_run
    - accept_revise_or_reject_architecture_consequence
```

The next-tier estimate is not a run authorization or proof of adequacy.

## 11. Research assessment

Deep Research is not needed. The open questions are design utility, authority behavior and maintenance burden in a frozen synthetic case, not an unresolved external factual question.

A new Fable run is also not needed. F1 already has independent research and fresh Pro adjudication; another research run before bounded evidence would be duplicative.

## 12. Current gate

This design and its package may be reviewed and merged as preparation. The next gate is the Owner disposition in:

```text
notes/owner-decision-candidates/
MNE-REUSABLE-CAPABILITY-OWNERSHIP-VALIDATION-DISPOSITION-CANDIDATE-001.md
```

No validation repository or execution surface is selected here.
