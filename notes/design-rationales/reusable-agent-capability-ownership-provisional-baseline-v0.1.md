# Design Rationale — Reusable Capability Ownership Provisional Baseline v0.1

```yaml
rationale_id: MNE-REUSABLE-CAPABILITY-OWNERSHIP-RATIONALE-001
decision_candidate: MNE-REUSABLE-CAPABILITY-OWNERSHIP-DISPOSITION-CANDIDATE-001
status: recorded_pending_Owner_disposition
```

## Problem and goal

The reusable capability catalogue now influences several target designs, while Mnemosyne, Meta-Agent and target repositories have distinct authority roles. The system needs version/impact continuity without creating duplicate truth or premature infrastructure.

## Fixed constraints

- Mnemosyne and Meta-Agent each retain their existing execution/target-truth boundaries.
- Targets remain sole owners of their current truth and adaptations.
- No automatic downstream propagation.
- No cross-repository ownership migration without Owner authorization and validation.

## Alternatives considered

1. Keep all reusable capability semantics permanently in Mnemosyne.
2. Move all general capability semantics immediately to Meta-Agent.
3. Create a dedicated common capability repository now.
4. Replicate most capability content into each target.
5. Use current role federation plus a minimal identity/relation/selection layer.

## Selected candidate

Option 5, with no physical ownership cutover now.

## Selection reason

It preserves current authority, captures the report's strongest lifecycle findings, and creates a falsifiable low-cost baseline. Immediate relocation would assume ownership not present in current Meta-Agent truth; a new repository would add governance before demand is demonstrated; target replication would create semantic drift.

## Risks

- Mnemosyne may remain an awkward home for general capabilities.
- A light relation ledger may miss indirect impacts.
- Natural-language revision compatibility may remain subjective.
- Future cutover may become more expensive if delayed too long.

## Validation and falsification

Track at least two target selections and one capability revision/split/retirement. Reconsider the architecture when relation/selection records produce missed impacts, repeated cross-repository contention, or publication/version burden that justifies a dedicated owner.
