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

V0 established that the public synthetic repository and the current GitHub connector can preserve package identity, material boundaries and named-repository no-write proof. The next useful evidence must test the candidate's actual semantics through S1–S9 and S11.

The V1 execution design must satisfy two competing needs:

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

### Option A — One long executor conversation

**Advantages**

- lowest operator overhead;
- simplest conversational continuity;
- one place to collect outputs.

**Disadvantages**

- the executor would see S7's sufficient migration guide before S8;
- a long context increases accidental semantic drift and hidden reuse of expected answers;
- one failure can contaminate many dependent scenarios;
- reviewer/executor role separation becomes weaker.

**Disposition:** rejected because it cannot credibly preserve the S8 knowledge firewall.

### Option B — One fresh conversation per scenario

**Advantages**

- strongest context isolation;
- simple attribution and contamination analysis;
- scenario failures remain localized.

**Disadvantages**

- unnecessarily high Owner operating cost;
- repeated fixture/package setup increases transport and input-binding risk;
- many small conversations create avoidable bookkeeping and return-routing burden.

**Disposition:** rejected as the universal topology; retained only where isolation is material.

### Option C — Staged multi-cell execution

Use one controller/setup cell, one grouped core cell, separate positive and negative documentation cells, one backup/restore cell, and one mechanical closeout. S8 alone receives a mandatory fresh-context firewall. Final semantic adjudication occurs in a fresh Pro conversation.

**Advantages**

- preserves the only mandatory knowledge-isolation case;
- groups scenarios with compatible context and authority structure;
- limits Owner launches to a small number of well-defined cells;
- keeps failures and branch lineages reconstructable;
- permits exact controller-side mechanical aggregation without making the controller the final semantic authority.

**Disadvantages**

- more complex than a single conversation;
- controller must enforce exact branch/input allowlists;
- grouped core-cell contamination remains possible among S1–S6/S9, although their expected facts do not create the same negative-test conflict as S7/S8;
- branch retention is required until final adjudication preserves all identities.

**Disposition:** selected.

## Selected topology

```text
V1 Controller / Fixture Cell
  ├─ Core Cell: S1, S2, S3, S4, S5, S6, S9
  ├─ Positive Documentation Cell: S7
  ├─ Fresh Negative Documentation Cell: S8
  ├─ Backup / Restore Cell: S11
  └─ Mechanical Closeout Cell
        ↓
Fresh Pro Adjudication
        ↓
Owner architecture decision
```

The controller may create and pin fixture/task branches but must not reveal S7 sufficient migration facts to the S8 worker. Each writing task retains its own task ID and canonical branch. Scenario PRs are unnecessary and remain prohibited unless a later authorization explicitly requires them.

## Why S10 is excluded

S10 is explicitly exploratory and non-baseline. It investigates optional impact views and registration exceptions and may generate candidate amendments. Including it in the first baseline V1 would:

- add scope that is not required for a baseline disposition;
- risk mixing optional design exploration with pass/fail evidence;
- create additional Pro adjudication work before the baseline mechanisms are known to function.

S10 may be separately selected after baseline V1 results if the Owner wants that evidence.

## Expected effects

- every baseline-critical scenario receives execution evidence;
- S8 remains a credible negative test rather than a memory test the worker has already been taught to pass;
- V1 can be executed by a bounded next-tier model while semantic acceptance remains with Pro and the Owner;
- raw outputs remain in the synthetic repository;
- Mnemosyne receives only a later reviewed summary and references under separate authority;
- V0 evidence remains immutable and distinguishable from V1.

## Known risks and controls

| Risk | Control |
|---|---|
| S8 worker sees S7 guide | fresh conversation; exact branch/file allowlist; no broad repository search; contamination check in result |
| grouped core cell drifts across scenarios | frozen inputs; separate task branches; per-scenario contracts and dispositions |
| controller silently repairs protocol | protocol-defect stop; proposed amendments marked non-adopted |
| branch proliferation | fixed branch map; one canonical branch per task; retain only through adjudication; later explicit cleanup decision |
| artifact identity inconsistency | require both blob SHA and creation/update commit for every output |
| unsupported no-write claim | exact before/after refs only for named repositories; disclose unnamed-target limitation |
| next-tier executor overreaches | exact stop rules and return-to-Pro triggers |
| same-context final review | fresh Pro adjudication conversation required |

## Validation / falsification plan

The topology is invalid or must be revised if:

- the product surface cannot keep S8 in a fresh context with exact input restrictions;
- scenario workers cannot read/write only their authorized branches;
- branch or output identity cannot be preserved;
- the controller cannot produce exact declared-versus-actual write-set evidence;
- real-repository before/after proof cannot be reconstructed;
- grouped scenarios show material cross-contamination;
- the operator flow imposes substantially more human work than the one-conversation alternative without adding useful evidence.

## Affected artifacts

- adds one V1 Owner decision candidate;
- adds one V1 execution-profile package that supplements but does not amend the frozen validation package;
- updates the current route status and backlog after V0 review;
- does not modify candidate v0.2, validation v0.2, the frozen package, Meta-Agent or any real target.

## Owner decision and review limitations

Owner confirmation is required before V1 runs. The current rationale is a Pro recommendation produced in the same conversation that executed V0 under a prior visible selection; exact backend identities are unknown. Final V1 adjudication should therefore use a fresh Pro conversation and must preserve this limitation.