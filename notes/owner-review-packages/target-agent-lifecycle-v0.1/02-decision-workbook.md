# Decision Workbook — TLR-01 through TLR-05

> Ask in order, one question at a time. Option labels are navigation aids; the Owner may answer in ordinary language, modify an option, defer, reject the premise, or request item-by-item explanation.

```yaml
package_id: MNE-TARGET-LIFECYCLE-OWNER-REVIEW-001
question_set_version: 0.1.0
repository_write_during_interview: false
```

# TLR-01 — Same-repository concurrency

## Question

When two tasks modify different logical Agent roots in the same physical repository, should they be allowed to proceed concurrently under a strict write-set contract?

## Recommended candidate

Allow concurrency only when all are true:

- each task has a distinct task ID and canonical branch/PR lineage;
- exact write sets are declared;
- write sets are mechanically disjoint;
- neither task changes a shared object, repository-wide governance, common configuration, generated global state, or the other's root;
- neither depends on the other's uncommitted result;
- final path/diff checks confirm isolation.

Serialize or reconcile when:

- write sets overlap;
- a shared or repository-global object changes;
- the scope is unknown;
- one task changes an authority map, target-root migration, or common capability selection used by the other.

## Why it matters

Rejecting all same-repository concurrency would make one physical repository a global bottleneck even when targets are independent. Allowing it without a write-set contract could create silent cross-target edits and ambiguous merges.

## Choices

- accept the recommended conditional-concurrency rule;
- require serialization until bounded validation passes, then reconsider;
- allow a narrower or broader rule described by the Owner;
- defer;
- reject multiple-Agent same-repository concurrency despite OR-06's permission for co-location.

The final option materially revises the confirmed architecture and requires frontier re-entry.

---

# TLR-02 — Shared objects and dependency responsibility

## Question

Should consumer-owned dependency declarations be the authoritative default, with shared-object/library impact views derived from them rather than maintained as an exhaustive manual reverse index?

## Recommended candidate

- each target/consumer owns its dependency declaration and selected version;
- the shared-object or library owner publishes the contract, version, breaking changes, migration guidance, deprecation/security notices, and contract tests;
- a repository-level impact view may be mechanically derived from consumer declarations;
- a manual registration list is permitted only for a bounded exception such as a fixed organizational migration, security notification, contractual support set, or case where usage cannot be rediscovered;
- every exception states scope, owner, freshness rule, and release gate;
- the derived or registered view does not override consumer-owned truth.

## Why it matters

A library-maintained universal consumer list is likely to become stale and duplicate information already present in target projects. No impact information at all can make shared-object changes unsafe.

## Choices

- accept the recommended consumer-owned/derived-view default;
- require a bounded registry for every co-located shared object but not external library consumers;
- require a complete library-side reverse index;
- remove all impact views and rely only on consumers at upgrade time;
- modify, defer, or reject the premise.

A complete mandatory reverse index reopens the Owner's OR-04-B/6 disposition and requires frontier review of the new rationale.

---

# TLR-03 — Primary change axis and secondary effects

## Question

Should every material change be assigned one primary evolution axis, while cross-axis consequences are recorded as separate evidence-backed secondary-effect candidates requiring their own adoption/approval?

## Axes

- meta-system/capability change;
- business requirement change;
- managed library/API change;
- provider/product adapter change;
- physical repository/container change.

## Recommended candidate

For each change:

1. identify the primary axis and direct object;
2. record direct effects;
3. list any possible effects on another axis separately;
4. state evidence/reason and required approval for each secondary effect;
5. prohibit automatic cross-axis propagation.

Examples:

- a Mnemosyne memory-layout improvement may require an Agent-internal migration but does not automatically change its API;
- a business requirement may separately justify an API change;
- a provider adapter failure may expose a portable capability defect, but the capability changes only after review.

## Choices

- accept the primary-axis/secondary-effect model;
- keep axes separate but allow one event to have multiple co-primary axes;
- keep only separate axes without a secondary-effect record;
- merge some axes;
- modify, defer, or reject.

Merging the Agent-internal, business, and API axes would conflict with the confirmed OR-04 correction and requires frontier re-entry.

---

# TLR-04 — Parent-owned design brief exception

## Question

While complete target bootstrap in a parent/meta repository remains prohibited, may the parent system retain a narrow design brief that it genuinely owns?

## Recommended allowed content

- source requirement or safe pointer;
- design problem, target identity, constraints, alternatives, and rationale;
- unresolved questions and target destination requirement;
- delivery manifest or pointers to the target-owned package;
- later safe generalized feedback and impact references.

## Prohibited content

- target execution source;
- target current state or handoff;
- target business truth or editable target memory;
- a complete live target directory tree awaiting migration;
- a second current capability-selection record that can drift from the target;
- any representation that lets a fresh session operate the target from the parent repository alone.

## Why it matters

Prohibiting every parent record would prevent Mnemosyne and Meta-Agent from retaining their own design rationale and evidence. A broad exception would recreate the migration problem under a different name.

## Choices

- accept the narrow design-brief exception;
- allow only pointers and no substantive design brief;
- allow a broader parent-side design package with stated limits;
- prohibit all parent-side target-related records;
- modify or defer.

A broader package that can function as live target truth requires frontier re-entry.

---

# TLR-05 — Provisional baseline and validation/adoption sequence

## Question

After TLR-01 through TLR-04 are resolved, should the repaired semantics become a provisional Mnemosyne architecture baseline before synthetic validation, while all target adoption remains blocked until validation is executed and reviewed?

## Recommended sequence

1. Owner confirms the repaired semantic model;
2. Pro/frontier creates candidate v0.2 and validation v0.2;
3. a frozen next-tier public/synthetic validation package is prepared;
4. the Owner separately authorizes any validation repository/write/run;
5. next-tier executes bounded scenarios with mechanical checks;
6. Pro/frontier adjudicates failures and revises the candidate;
7. the Owner decides whether the architecture is accepted for future target-specific adoption;
8. each target separately decides adoption and migration.

## Why it matters

Validation needs a sufficiently frozen contract; otherwise every result can be explained away by changing the design. Conversely, provisional baseline status must not be mistaken for target adoption.

## Choices

- accept the recommended provisional-baseline-then-validation sequence;
- require validation before calling any semantic model a baseline;
- accept the architecture without validation;
- defer validation indefinitely while keeping v0.1 only;
- define another sequence.

Accepting target operation or automatic propagation from this interview is out of scope and requires frontier/Owner re-entry.

---

# Completion rule

After TLR-01 through TLR-05:

- show the complete ledger;
- distinguish confirmed, provisional, deferred, rejected, and frontier-reentry items;
- summarize the resulting candidate-v0.2 direction in natural Chinese;
- list what remains unimplemented and unauthorized;
- wait for the Owner to correct or confirm;
- do not write GitHub until separate save authorization is given.
