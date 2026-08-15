# Reusable Agent Capability Ownership — Owner Decision 001

> Durable record of the Owner's disposition on `MNE-REUSABLE-CAPABILITY-OWNERSHIP-DISPOSITION-CANDIDATE-001`. This accepts the Pro-corrected model as a modified provisional baseline for later bounded validation. It does not implement a lifecycle schema, migrate repository ownership, modify Meta-Agent or any target, or authorize validation execution.

```yaml
decision_id: MNE-REUSABLE-CAPABILITY-OWNERSHIP-OWNER-DECISION-001
task_id: MNEMOSYNE-220
decision_status: OWNER_CONFIRMED_OPTION_A
selected_option: A_ACCEPT_MODIFIED_PROVISIONAL_BASELINE
source_read_only_master_confirmed_by_Owner: 94072794cb67eb90034a19569d4716fc18aa635d
execution_time_base_master: cafb080293d9525dd186a550f8ffcf98e1e4478d
source_adjudication:
  path: notes/research-adjudications/MNE-DR-004-CAPABILITY-OWNERSHIP-PRO-ADJUDICATION-001.md
  blob: 9b0abf20517e843ddeb2a35319e4774e1061827b
source_corrected_candidate:
  path: notes/reusable-agent-capability-ownership-and-lifecycle-model-candidate-v0.1.md
  blob: accb13ccb57677d316f5f94ef58f7939ad69521b
source_decision_candidate:
  path: notes/owner-decision-candidates/MNE-REUSABLE-CAPABILITY-OWNERSHIP-DISPOSITION-CANDIDATE-001.md
  blob: 19284743cd64e3dd0e956c4aca1a6e8f3aa19960
candidate_status_after_decision: OWNER_ACCEPTED_MODIFIED_PROVISIONAL_BASELINE_PENDING_BOUNDED_VALIDATION
implementation_authorized: false
validation_authorized: false
shared_repository_creation_or_migration_authorized: false
Meta_Agent_modified_or_authorized: false
real_target_modified_or_authorized: false
target_adoption_authorized: false
execution_source_modified_or_authorized: false
external_research_or_quota_authorized: false
```

## 1. Owner decision

The Owner explicitly accepts the Pro-corrected modified provisional baseline with the following current direction:

- Mnemosyne continues to own the reusable capability catalogue for now;
- no new shared capability repository is created at the current evidence maturity;
- Meta-Agent methodology and target-truth authority remain unchanged;
- each target owns its own capability selection, adaptation, implementation and current truth;
- stable capability ID, catalogue version, object revision and explicit split/merge/supersede/retire relationships are accepted as candidate mechanisms to validate, not as an implemented universal schema;
- the target capability selection record is authoritative only within the target boundary that adopts it;
- any meta-side impact view is derived and non-authoritative;
- upstream capability change creates review candidates and impact analysis, not automatic downstream writes or standing writer authority;
- any future catalogue-ownership cutover still requires a separately selected design, migration, validation, destination-only recovery, no-dual-writer closure and explicit Owner decision.

## 2. Meaning of acceptance

This is architecture selection for the next evidence stage, not implementation acceptance.

The accepted provisional baseline may now be used to design a bounded validation package that tests whether the proposed identity, lifecycle, selection and impact semantics are useful and safe in practice. Until such validation is separately selected and authorized, the current repositories and authority boundaries remain unchanged.

The Owner does not accept the uncorrected Fable report as an implementation specification. The controlling model is the Pro-corrected candidate identified above.

## 3. Current ownership boundary

```yaml
current_ownership:
  reusable_capability_catalogue: Mnemosyne
  Mnemosyne_research_and_rationale: Mnemosyne_for_Mnemosyne_owned_evidence
  Meta_Agent_methodology: Meta_Agent_under_its_own_authority
  Meta_Agent_target_truth: Meta_Agent_current_approved_spec
  target_capability_selection_and_adaptation: each_target_repository_or_store
  target_implementation_and_current_truth: each_target_repository_or_store
  target_specific_provider_adapter: target_local_unless_later_promoted
  dated_provider_fact: evidence_owning_project_or_cycle
  material_original_evidence: legitimate_source_or_receiving_owner_under_privacy_rules
```

Physical location and semantic authority remain separate concepts. A future dedicated shared repository is not prohibited in principle; it is simply not justified or authorized now.

## 4. Candidate lifecycle semantics accepted for validation

The validation candidate may use this minimum model:

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

Rules accepted for validation:

1. published IDs are not reused;
2. revision changes do not automatically update targets;
3. split, merge, supersession and retirement are explicit;
4. full Semantic Versioning is optional until a capability family has a stable, testable public contract;
5. target-side review is required before a selected revision changes target behavior.

## 5. Target selection and upstream-change boundary

A target-local selection record may identify the exact catalogue version, object revision, adaptation, implementation, validation and Owner decision used by that target.

A meta-side impact view may derive a list of potentially affected targets from those records, but it must remain non-authoritative and cannot substitute for target truth.

Upstream change flow remains review-first:

1. publish a candidate capability revision or relation change;
2. derive a non-authoritative affected-target view;
3. create a target-specific review candidate;
4. target authority decides no action, future-only use, review, migration, recomputation, completed-work re-evaluation or rejection;
5. validation occurs inside the target boundary if selected;
6. no upstream actor acquires standing target-write authority.

## 6. Concurrent F2 relationship

At execution time, another Mnemosyne conversation had active `MNE-DR-005` branches for cross-repository-safe-concurrency research intake and Project-knowledge snapshot work.

Those branches use disjoint canonical write paths from this F1 decision task. One frozen Project-knowledge snapshot contains the pre-decision F1 corrected candidate as an input. This Owner decision does **not** rewrite that launch-time snapshot, invalidate it retroactively, or authorize edits to the F2 branches.

Any later F2 adjudication must distinguish:

- the F1 candidate identity that was actually supplied to the F2 run; and
- the later Owner acceptance recorded here.

The F2 route retains its own research, quota, adjudication and publication gates.

## 7. Explicitly not authorized

This decision does not authorize:

- implementation of the capability lifecycle schema;
- execution of capability-ownership validation;
- creation or migration of a shared repository;
- catalogue transfer to Meta-Agent;
- modification of Meta-Agent or any real target;
- target adoption, migration or activation;
- modification of `current/human-approved-spec.md`;
- automatic downstream propagation or standing cross-target writer authority;
- F2 execution, Work, Deep Research, Fable, Scheduled Tasks or external quota;
- auto-merge or Agent merge.

## 8. Next gate

The next substantive F1 gate is **bounded validation design**, followed by a separately authorized validation execution if the Owner later selects it.

A future validation should test at minimum:

- one capability through revision, target selection, upstream change and retirement;
- split/merge relation handling;
- target-local selection authority versus non-authoritative impact views;
- no-target-write behavior during upstream impact review;
- whether the mechanism reduces rework without imposing excessive schema burden.

No validation is selected or authorized by this decision.
