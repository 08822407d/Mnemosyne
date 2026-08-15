# Reusable Agent Capability Ownership and Lifecycle Model — Candidate v0.1

```yaml
candidate_id: MNEMOSYNE-REUSABLE-AGENT-CAPABILITY-OWNERSHIP-LIFECYCLE-001
version: 0.1.0
status: pro_corrected_candidate_pending_Owner_disposition
source_research: FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001
source_adjudication: notes/research-adjudications/MNE-DR-004-CAPABILITY-OWNERSHIP-PRO-ADJUDICATION-001.md
execution_source: false
Meta_Agent_truth_effect: none
target_adoption_effect: none
repository_migration_authorized: false
```

## 1. Provisional decision

Use role-based federation and do not create a new shared capability repository at the current evidence maturity.

This candidate distinguishes current ownership from a possible future cutover. It does not silently implement the Fable report's proposed Meta-Agent ownership.

## 2. Current ownership map

| Object family | Current canonical owner/location | Other repositories may retain |
|---|---|---|
| Mnemosyne reusable capability catalogue | Mnemosyne | references, selected IDs/revisions, reviewed derivatives |
| Mnemosyne memory-system research and rationale | Mnemosyne | safe pointers or target-approved summaries |
| Meta-Agent accepted methodology | Meta-Agent methodology referenced by its approved spec | method IDs/versions and safe references |
| Meta-Agent current target truth | Meta-Agent `current/approved-spec.md` | immutable migration/history pointers only |
| Target capability selection and adaptation | each target repository/store | meta-level safe index/pointer where approved |
| Target implementation and current truth | each target repository/store | no competing live copy |
| Target-specific provider adapter/configuration | each target repository/store | reusable pattern candidate after promotion review |
| Dated provider facts | evidence-owning project/cycle | portable citation/pointer, recheck trigger |
| Material original evidence | legitimate source/receiving owner under privacy rules | identity receipt, safe pointer or reviewed derivative |

## 3. Candidate lifecycle identity model

For each capability object, the minimum candidate record is:

```yaml
capability_identity:
  capability_id:
  catalogue_id:
  catalogue_version:
  object_revision:
  status: candidate | active | deprecated | retired
  relations:
    supersedes: []
    split_from: []
    split_into: []
    merged_from: []
    merged_into:
  compatibility_or_affected_selection_note:
  source_and_rationale_refs: []
```

Rules:

- IDs are never reused.
- Revision changes do not automatically update targets.
- Split/merge/retire relationships are explicit.
- Full SemVer is optional until a capability family has a declared, stable and testable public contract.

## 4. Target selection record

Each target declares what it actually uses:

```yaml
target_capability_selection:
  target_id:
  target_truth_ref:
  capability_id:
  selected_catalogue_version:
  selected_object_revision:
  adaptation_status:
  target_implementation_ref:
  validation_or_real_use_ref:
  owner_decision_ref:
```

A target-local record is authoritative for that target. A meta-side index or impact view is derived convenience only.

## 5. Upstream change flow

1. publish a candidate capability revision and relationship record;
2. derive a non-authoritative list of targets whose own selection records reference the affected identity;
3. create a target-specific review candidate;
4. let target authority decide no action, future-only use, review, migration, recomputation, completed-work re-evaluation or rejection;
5. validate inside the target boundary;
6. record compatibility, migration and optional rollback;
7. refresh the derived impact view without becoming the target writer.

No automatic propagation or standing cross-target write authority is created.

## 6. Provider boundary

- portable behavior semantics are provider-neutral;
- provider-neutral packaging methods may become Meta-Agent methodology only after promotion review;
- dated provider facts remain evidence with a recheck trigger;
- target-specific prompts, Skills, tools and configurations remain target-owned;
- a provider workaround cannot silently become portable semantics.

## 7. Future shared-owner cutover gate

Reconsider a dedicated shared repository or Meta-Agent ownership only when evidence shows several of:

- multiple mature targets repeatedly adopt the same capability family;
- release/version/compatibility work is recurrent and costly;
- current ownership creates repeated writer or publication conflicts;
- target selection plus relation ledger misses material impacts;
- a standalone package provides testable value greater than governance cost.

A selected cutover requires one new Owner-approved migration task and complete no-dual-writer closure.

## 8. Validation before implementation

Minimum validation candidates:

- lifecycle one capability through revision, selection, change and retirement;
- test target-side selection and destination-only recovery;
- change one upstream revision and verify review without target modification;
- compare manual and mechanically derived impact views;
- test split and merge relationships;
- measure whether the candidate record reduces rework without becoming schema burden.

This file prepares the model only. No validation is selected or authorized.
