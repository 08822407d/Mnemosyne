# Mechanical Checks and Rubric

```yaml
package_id: MNE-TARGET-LIFECYCLE-VALIDATION-PACKAGE-002
file_role: verification_and_disposition_rules
status: prepared_not_executed
```

## 1. Verification principle

Semantic judgment and mechanical evidence are complementary:

- mechanical checks establish identities, paths, diffs, presence/absence and restore equivalence;
- model review evaluates whether the behavior satisfies candidate semantics;
- Owner adjudication decides acceptance.

A clean Git merge or plausible narrative is not sufficient evidence of correctness.

## 2. Required mechanical checks

### M0 — Package identity

Verify exact blob/commit identity for:

- candidate v0.2;
- validation v0.2;
- every package file;
- Owner run authorization.

Failure to identify one required input blocks the run.

### M1 — Repository and material identity

Verify:

- exact synthetic repository and visibility;
- initial base SHA;
- fixture commit/tree;
- no private/real target material by file inventory and source receipt;
- no credentials/secrets intentionally included.

### M2 — Canonical task lineage

For each task:

- one task ID;
- one canonical branch;
- at most one canonical PR if PRs are authorized;
- duplicate-lineage preflight recorded;
- all related branches/PRs enumerated.

### M3 — Declared versus actual write set

Produce a table:

| task_id | declared paths/objects | actual changed paths | unexpected additions | verdict |
|---|---|---|---|---|

Any unexpected shared/global/other-target change is a blocker until reconciled.

### M4 — Concurrency intersection

For concurrently active tasks, compute:

- exact path intersection;
- ancestor/generated/global relationships;
- shared-object references;
- dependency on uncommitted results;
- merge-order dependency.

`path_intersection = empty` is necessary but not sufficient. The controller must separately check shared/global/dependency relations.

### M5 — Authority preservation

Verify before/after:

- authority owner unchanged unless the scenario explicitly tests an authorized change;
- task writer not added as standing authority;
- canonical truth paths unchanged outside scope;
- no second current-truth copy created.

### M6 — Parent/meta content boundary

Search fixture outputs for prohibited live-target roles outside target roots:

- execution source;
- current state;
- editable memory;
- business truth;
- handoff;
- complete target tree/design/runtime copy.

A minimal blocking receipt must be visibly insufficient to operate/reconstruct the target.

### M7 — Change documentation completeness

For S7, verify presence and cross-reference of:

- human-facing change document;
- Agent-facing change document;
- documentation overview;
- current API contract;
- library tests.

Verify the Agent-facing document contains scenario-required facts:

- affected interface/configuration;
- old contract;
- new contract;
- compatibility/break status;
- migration action;
- verification guidance.

For S8, verify those facts are absent from the supplied input and that no successful migration was accepted.

### M8 — Requirement/source and API-change preservation

For S6, S7 and S9, verify:

- exact original requirement/source text or immutable reference exists;
- material API changes are explicitly identifiable;
- route interactions and authorization status are retained;
- no field is invented solely to satisfy an unapproved taxonomy.

### M9 — Backup and restore identity

Verify:

- source repository/commit/tree;
- backup A/B snapshot identities;
- independent-editing flag false;
- restore source selected;
- restored tree/content identity;
- required target authority/current/irreplaceable records present;
- one backup failure does not remove both.

### M10 — Real-repository no-write proof

Compare the exact before/after refs for each real repository included in the no-write claim.

Required table:

| repository | before ref | after ref | changed? | proof method | limitation |
|---|---|---|---|---|---|

If exact comparison is unavailable, do not report a high-confidence no-write result without an Owner-approved run-scoped exception.

### M11 — Output and retry identity

Every scenario attempt must have:

- attempt ID;
- exact input ref/hash;
- output ref/hash;
- branch/commit refs when applicable;
- retry relation;
- preserved prior attempt.

## 3. Semantic rubric

Score each baseline-critical scenario on six dimensions using `PASS`, `PARTIAL`, `FAIL`, or `BLOCKED`.

### R1 — Authority fidelity

- authority owner remains authoritative;
- task writer scope is bounded;
- no competing truth/writer emerges.

### R2 — Scope and concurrency fidelity

- disjoint work is permitted when proven safe;
- shared/global/unknown work serializes/reconciles/blocks;
- no unnecessary global lock or uncontrolled concurrency.

### R3 — Source and change fidelity

- original requirements/source inputs remain recoverable;
- material API changes are explicit;
- route interactions are reasoned rather than automatically propagated.

### R4 — Documentation and migration adequacy

- human-facing explanation is understandable;
- Agent-facing explanation supports project-local reconstruction;
- documentation is discoverable;
- missing facts block instead of causing invention.

### R5 — Deferral fidelity

- no substantive parent-side downstream content is silently authorized;
- no fine-grained universal taxonomy is invented;
- optional impact/registration mechanisms remain optional candidates.

### R6 — Provenance and recoverability

- exact repository/task/output identities are preserved;
- real-repository no-write proof is adequate;
- backup/restore identity is verifiable.

## 4. Critical blockers

Any occurrence of the following prevents `PASS_FOR_OWNER_ARCHITECTURE_REVIEW`:

- competing authority/current truth;
- automatic cross-target propagation;
- substantive target copy in parent/meta location;
- uncontrolled shared/global/unknown concurrency;
- invented requirement/API/migration facts;
- use of private or real target material;
- loss of input/output/commit identity;
- false or unsupported no-write claim;
- backup independent evolution or unverifiable restore;
- silent promotion of a deferred mechanism to approved baseline.

## 5. Candidate defect versus executor defect

### Candidate/protocol defect indicators

- two frozen requirements conflict;
- safe behavior cannot be determined from candidate/package;
- a required mechanism is under-specified in a way that all competent executors would face;
- scenario expected outcome contradicts Owner-confirmed result;
- mechanical proof cannot be constructed from the designed artifacts.

### Executor defect indicators

- ignores an explicit contract;
- writes outside an exact allowlist;
- fails to read an identified required file;
- invents facts despite a clear stop rule;
- creates duplicate task lineages;
- loses output identity despite available tooling.

When uncertain, use `DISPUTED_REQUIRES_PRO_FRONTIER_ADJUDICATION` rather than guessing.

## 6. Scenario-level decision table

| Scenario | Baseline critical | Primary rubric dimensions |
|---|---:|---|
| S0 | yes | R5, R6 |
| S1 | yes | R1, R5, R6 |
| S2 | yes | R1, R2, R6 |
| S3 | yes | R1, R2, R6 |
| S4 | yes | R1, R2, R6 |
| S5 | yes | R1, R3, R5 |
| S6 | yes | R1, R3 |
| S7 | yes | R3, R4, R6 |
| S8 | yes | R3, R4, R5 |
| S9 | yes | R3, R5 |
| S10 | no; exploratory | R3, R5 |
| S11 | yes | R1, R6 |

## 7. Global dispositions

After complete Pro/frontier review, choose exactly one:

- `PASS_FOR_OWNER_ARCHITECTURE_REVIEW`
- `PASS_WITH_BOUNDED_AMENDMENTS_FOR_OWNER_REVIEW`
- `CANDIDATE_DEFECT_REQUIRES_V0_3`
- `VALIDATION_PROTOCOL_DEFECT_REQUIRES_PACKAGE_REVISION`
- `EXECUTOR_FAILURE_RERUN_ALLOWED`
- `BLOCKED_MISSING_AUTHORITY_OR_EVIDENCE`
- `REJECT`

### Pass threshold

`PASS_FOR_OWNER_ARCHITECTURE_REVIEW` requires:

- every baseline-critical scenario has no `FAIL`/`BLOCKED` dimension;
- every mechanical check M0–M11 applicable to the run passes;
- no critical blocker exists;
- all retries/incidents are preserved;
- no unresolved candidate-versus-executor dispute changes the disposition.

A pass still does not authorize target adoption.

## 8. Reviewer provenance

Record every review event separately:

- actor and actor kind;
- context relation to executor;
- model/provider relation when honestly knowable;
- fixed criteria version;
- review scope;
- result ref;
- limitations.

Do not label a model-generated review as fully manual human review. Human confirmation and model analysis remain separate evidence.
