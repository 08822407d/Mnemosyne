# Design Rationale — V1 Owner Acceptance, Recovery Provenance, and Bounded Profile Amendments v0.1

```yaml
rationale_id: MNE-TARGET-LIFECYCLE-V1-OWNER-ACCEPTANCE-RATIONALE-001
task_id: MNEMOSYNE-215
decision_refs:
  - notes/validation-adjudications/MNE-TARGET-LIFECYCLE-V1-ADJUDICATION-001.md
  - notes/provenance-incidents/MNE-TARGET-LIFECYCLE-V1-ADJUDICATION-RECOVERY-001.md
  - notes/owner-decision-results/MNE-TARGET-LIFECYCLE-V1-OWNER-ARCHITECTURE-DECISION-001.md
owner_decision_ref: current_conversation_MNE_TARGET_LIFECYCLE_V1_owner_acceptance
execution_source_modified: false
```

## Problem and Owner goal

The V1 synthetic run completed with a full evidence bundle and a fresh-Pro adjudication. The adjudication chat then experienced an accidental regenerate action that was immediately stopped. The same fresh-Pro conversation recovered or reconstructed the result, but the exact pre-regeneration answer could no longer be compared byte-for-byte.

The Owner wanted to preserve a trustworthy architecture decision without wasting another Pro run, while correcting two bounded evidence/protocol weaknesses and keeping target adoption separately gated.

## Fixed constraints

- the synthetic V1 evidence and exact branch/blob identities must not be rewritten;
- the lost pre-regeneration response cannot be declared byte-identical without evidence;
- candidate v0.2 must not be silently changed by a validation executor or follow-up record;
- V1 acceptance must not become production readiness or target adoption;
- TLR-03 and TLR-04 deferrals remain open;
- V1 evidence branches remain retained until explicit cleanup release;
- no runtime supplement, S10, V2, Work pilot, Fable or Deep Research is authorized.

## Alternatives considered

### A. Repeat the complete fresh-Pro adjudication

Advantages:

- creates another independently generated verdict;
- avoids relying on the recovered text as the only narrative record.

Disadvantages:

- cannot prove what the original pre-regeneration answer said;
- duplicates expensive Pro work against unchanged evidence;
- may create a third wording variant and another reconciliation burden.

### B. Accept the recovered result only as an unverified transcript

Advantages:

- minimal additional work.

Disadvantages:

- overstates provenance if called an exact recovery;
- does not independently test the key non-obvious findings;
- weakens later auditability.

### C. Normalize the recovered result, record the recovery incident, independently recheck the decisive findings, and accept bounded amendments

Advantages:

- separates byte identity from semantic reliability;
- preserves the exact attachment hash without publishing the attachment body;
- binds the durable adjudication to repository commits, paths and blobs;
- avoids unnecessary rerun while preserving uncertainty honestly;
- fixes future profile reuse without rewriting historical evidence.

Disadvantages:

- cannot reconstruct the exact pre-regeneration answer;
- requires a durable provenance incident and explicit evidence-strength vocabulary.

## Selected option

Option C.

The decisive trade-off is that repository evidence is unchanged and the key findings are independently reproducible, while a duplicate adjudication cannot restore the one fact that is unavailable: exact byte identity of the lost answer. The reliable engineering response is therefore to lower the provenance claim, not to discard the semantic result.

## Expected effects

- candidate v0.2 becomes an Owner-accepted provisional global baseline for future target-specific consideration;
- the historical run remains immutable and honestly scoped;
- future profile reuse has a coherent fixture write set;
- test-presence, static inspection and runtime claims cannot be conflated;
- no real target changes until a separate target-owned decision.

## Known risks and falsification

The decision should be revisited if:

- a material mismatch is later found between the normalized adjudication and exact V1 evidence;
- S8 contamination evidence emerges;
- a candidate-level defect is discovered in real target use;
- a future runtime supplement materially contradicts the architecture-relevant conclusions;
- the retained evidence branches become unavailable before durable preservation.

## Chat-to-Work observation routing

The Owner's new observation that ordinary Chat may offer or trigger transfer of follow-up work to Work is recorded separately as a platform observation. It is not used to strengthen the V1 verdict and does not authorize a Work pilot. This prevents a current-product hypothesis from contaminating a completed architecture decision.
