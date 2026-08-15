# Target-Lifecycle V1 Staged Multi-Cell Execution — Design Rationale v0.1

```yaml
rationale_id: MNE-TARGET-LIFECYCLE-V1-MULTICELL-RATIONALE-001
task_id: MNEMOSYNE-212
design_or_decision_ref: notes/validation-run-decisions/MNE-TARGET-LIFECYCLE-V1-RUN-DECISION-CANDIDATE-001.md
status: Pro_recommended_pending_Owner_confirmation
execution_source: false
V1_authorized: false
```

## Problem and user goal

V0 established that the public synthetic repository and current GitHub connector can preserve package identity, material boundaries and named-repository no-write proof. The next useful evidence must test candidate semantics through S1–S9 and S11.

The V1 design must satisfy two competing needs:

- keep the Owner's manual operating burden and model cost proportionate;
- prevent context contamination, especially the S8 negative documentation test, whose worker must not know the sufficient migration facts revealed in S7.

It must also preserve one canonical branch per writing task, exact artifact identity, real-repository no-write proof, all failures/retries and a fresh Pro return route.

## Fixed constraints

- reuse `08822407d/mnemosyne-target-lifecycle-validation-002`;
- preserve V0 evidence at `master@e8e3296922185b4b70997c2351d6f39423f2cd4f`;
- use only public/synthetic material;
- do not write Mnemosyne, Meta-Agent or real targets during V1;
- do not run web research, Deep Research, Fable or external quota;
- do not change candidate v0.2 or validation-package semantics during execution;
- run all baseline-critical S1–S9 and S11 for a complete baseline V1;
- do not select exploratory S10 by default;
- S8 must use a fresh conversation and an input branch that does not contain the sufficient S7 guide;
- V1 pass/fail remains provisional until a fresh Pro adjudicator reviews the complete bundle;
- V1 execution requires a new Owner authorization.

## Alternatives considered

### Option A — One conversation for every execution and review role

**Advantages**

- lowest launch count;
- simplest conversational continuity.

**Disadvantages**

- the same executor would see S7's sufficient migration guide before S8;
- S8 would cease to be a credible missing-information negative test;
- final review would not be context-independent from execution;
- long context increases accidental reuse of expected answers.

**Disposition:** rejected because it violates the S8 firewall and review-separation goals.

### Option B — One fresh conversation per scenario or logical cell

**Advantages**

- strongest context isolation;
- simple attribution and contamination analysis;
- scenario failures remain localized.

**Disadvantages**

- unnecessarily high Owner operating cost;
- repeated setup increases transport and input-binding risk;
- many small conversations create avoidable bookkeeping and return-routing burden;
- most scenarios do not have a planted knowledge-isolation requirement.

**Disposition:** rejected as the default topology.

### Option C — Three-conversation staged execution

Use one next-tier main executor conversation for controller/fixture work, Core, S7, S11 and final mechanical closeout; one mandatory fresh next-tier conversation for S8; and one mandatory fresh Pro conversation for final adjudication.

The main executor prepares the isolated S8 branch and launch receipt, performs all non-S8 logical cells on their separate canonical task branches, pauses for the fresh S8 result, then resumes mechanical closeout.

**Advantages**

- preserves the only mandatory worker knowledge firewall;
- preserves fresh final review;
- reduces the Owner's required conversations from six or more to three;
- keeps task and evidence isolation in Git branches rather than forcing unnecessary chat proliferation;
- permits exact controller-side aggregation without making the controller final semantic authority;
- keeps all compatible frozen execution in one bounded next-tier context.

**Disadvantages**

- the main executor context is longer;
- Core, S7 and S11 share conversational context, although none is a negative knowledge test against another;
- a main-executor failure may affect several logical cells and must be preserved rather than hidden;
- controller branch/input allowlists remain essential.

**Disposition:** selected. It provides the minimum conversation separation needed for valid evidence while respecting the Owner's operating cost.

## Selected topology

```text
Conversation 1 — MNE-DR-003 Execute (next-tier)
  Controller / fixture
  Core: S1, S2, S3, S4, S5, S6, S9
  Positive documentation: S7
  Backup / restore: S11
  Prepare isolated S8 branch and receipt
  Pause for S8
       ↓
Conversation 2 — MNE-DR-003 S8 (fresh next-tier)
  Negative documentation: S8 only
       ↓
Return S8 exact result refs to Conversation 1
  Mechanical closeout and complete V1 bundle
       ↓
Conversation 3 — MNE-DR-003 Review (fresh Pro)
  Semantic adjudication
       ↓
Owner architecture decision
```

Logical cells and task branches remain separate even when the main executor runs them in one conversation. Each writing task retains its own task ID, branch, write set, result and provisional disposition. Scenario PRs are unnecessary and remain prohibited unless a later authorization explicitly requires them.

## Why S10 is excluded

S10 is explicitly exploratory and non-baseline. It investigates optional impact views and registration exceptions and may generate candidate amendments. Including it in the first baseline V1 would:

- add scope not required for a baseline disposition;
- mix optional design exploration with pass/fail evidence;
- increase execution and adjudication burden before baseline mechanisms are known to function.

S10 may be separately selected after baseline V1 results if the Owner wants that evidence.

## Expected effects

- every baseline-critical scenario receives execution evidence;
- S8 remains a credible negative test rather than a memory test the worker has already been taught to pass;
- the Owner operates only three conversations;
- V1 execution can use a bounded next-tier model while semantic acceptance remains with fresh Pro and the Owner;
- raw outputs remain in the synthetic repository;
- Mnemosyne receives only a later reviewed summary and references under separate authority;
- V0 evidence remains immutable and distinguishable from V1.

## Known risks and controls

| Risk | Control |
|---|---|
| S8 worker sees S7 guide | fresh conversation; exact branch/file allowlist; no broad repository search; contamination check |
| long main-executor context drifts | frozen inputs; separate task branches/contracts/results; stop on semantic conflict |
| failure contaminates later main-executor cells | preserve incident; stop dependent work; do not clean-rewrite history |
| controller silently repairs protocol | protocol-defect stop; amendments remain non-adopted |
| branch proliferation | fixed map; one branch per task; retain through adjudication only |
| artifact identity inconsistency | require blob SHA plus creation/update commit for every output |
| unsupported no-write claim | exact before/after refs only for named repositories; disclose unnamed-target limitation |
| same-context final review | separate fresh Pro adjudication conversation |

## Validation / falsification plan

The topology is invalid or must be revised if:

- the product surface cannot keep S8 in a fresh context with exact input restrictions;
- the main executor cannot pause and later resume closeout from exact S8 refs;
- scenario tasks cannot remain mechanically separated by branch and write contract;
- branch/output identity cannot be preserved;
- no-write proof cannot be reconstructed;
- the main context shows material cross-scenario contamination;
- the three-conversation flow still imposes disproportionate Owner work without useful evidence.

## Affected artifacts

- adds one V1 Owner decision candidate;
- adds one V1 execution package that supplements but does not amend the frozen validation package;
- allocates one display alias with Execute/S8/Review suffixes;
- updates current route status and backlog after V0 review;
- does not modify candidate v0.2, validation v0.2, the frozen package, Meta-Agent or any real target.

## Owner decision and review limitations

Owner confirmation is required before V1 runs. The current rationale is a Pro recommendation produced in the same conversation that executed V0 under a prior visible selection; exact backend identities are unknown. Final V1 adjudication therefore uses a fresh Pro conversation.