# Reusable Agent Capability Ownership Research — Current Status

```yaml
status_id: MNE-REUSABLE-CAPABILITY-OWNERSHIP-STATUS-001
last_updated_by_task: MNEMOSYNE-220
source_master_at_decision_execution: cafb080293d9525dd186a550f8ffcf98e1e4478d
canonical_task_id: FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001
canonical_display_name: MNE-DR-004 能力归属
historical_run_display_name: MNE-DR-003 能力归属
research_complete: true
report_preserved: true
Pro_adjudication: ACCEPT_WITH_MATERIAL_CORRECTIONS
corrected_candidate_prepared: true
PR_281_verified_merged: true
PR_281_merge_commit: 4198d18352a071cbdcc7dc97734e65886da0621b
Owner_disposition: OWNER_CONFIRMED_OPTION_A_ACCEPT_MODIFIED_PROVISIONAL_BASELINE
Owner_decision_ref: notes/owner-decision-results/MNE-REUSABLE-CAPABILITY-OWNERSHIP-OWNER-DECISION-001.md
candidate_status: OWNER_ACCEPTED_MODIFIED_PROVISIONAL_BASELINE_PENDING_BOUNDED_VALIDATION
implementation_authorized: false
validation_authorized: false
shared_repository_creation_or_migration_authorized: false
execution_source_modified: false
Meta_Agent_modified: false
real_target_modified: false
```

## Current result

The independent Fable report recommended role-based federation and no new shared repository. The Pro adjudication accepted that direction with material corrections concerning current catalogue location, Meta-Agent authority, source-local evidence ownership, versioning maturity, provider-adapter ownership and future repository cutover semantics.

The Owner has now accepted the **Pro-corrected modified provisional baseline**. The controlling candidate remains:

```text
notes/reusable-agent-capability-ownership-and-lifecycle-model-candidate-v0.1.md
```

Acceptance selects that model for later bounded validation. It does not implement the proposed lifecycle schema, migrate catalogue ownership, modify a target, or authorize validation execution.

## Accepted provisional ownership model

Current direction:

- Mnemosyne remains the current owner of the reusable capability catalogue;
- no fourth/shared capability repository is created now;
- Meta-Agent keeps its own accepted methodology and target-truth authority without inheriting catalogue ownership;
- each target owns its own capability selection, adaptation, implementation and current truth;
- stable capability IDs, catalogue versions, object revisions and explicit split/merge/supersede/retire relationships are candidate mechanisms for validation;
- target-side selection records are authoritative only inside the adopting target;
- meta-side impact views are derived and non-authoritative;
- upstream changes trigger review candidates, not automatic downstream writes or standing writer authority;
- any future catalogue ownership cutover requires a separately selected migration with destination truth, compatibility, recovery, no-dual-writer closure and explicit Owner acceptance.

Full Semantic Versioning is not required for every natural-language capability at the current maturity. It may later be adopted for capability families with stable, testable contracts and repeated consumers.

## Current gate

The next substantive F1 gate is:

```yaml
next_gate: BOUNDED_VALIDATION_DESIGN
validation_selected: false
validation_execution_authorized: false
implementation_selected: false
```

A future bounded validation should test whether the identity/lifecycle/selection/impact model works in realistic synthetic or public cases without becoming excessive schema burden or target-write authority.

Validation design, validation execution and implementation remain separate decisions.

## Concurrent F2 boundary

At the time of the Owner decision, `MNE-DR-005` cross-repository-safe-concurrency work had active, separate repository branches.

One F2 Project-knowledge snapshot contains the pre-decision F1 corrected candidate as a frozen input. The Owner decision does not rewrite or invalidate that historical launch-time input. Any later F2 adjudication should distinguish its exact run inputs from the later F1 Owner acceptance.

This F1 status does not authorize, merge, modify or adjudicate F2.

## Still not authorized

- capability lifecycle schema implementation;
- capability ownership validation execution;
- new shared repository creation or migration;
- catalogue ownership transfer to Meta-Agent;
- Meta-Agent or real-target modification;
- target adoption, migration or activation;
- execution-source modification;
- automatic upstream-to-downstream propagation;
- Work, Deep Research, Fable, Scheduled Tasks or external quota;
- F2 execution or adjudication through this route.

## Safe next action

After publication of this Owner decision/status package, the F1 route may either stop at the accepted provisional baseline or, under a new explicit Owner instruction, prepare a bounded validation design. No validation run follows automatically.
