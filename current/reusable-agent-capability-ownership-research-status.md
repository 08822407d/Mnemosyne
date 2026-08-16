# Reusable Agent Capability Ownership Research — Current Status

```yaml
status_id: MNE-REUSABLE-CAPABILITY-OWNERSHIP-STATUS-001
last_updated_by_task: MNEMOSYNE-225
source_master_at_validation_design_start: 9157c476e8bf785f6440af4aaefbc44532d47c14
canonical_task_id: FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001
canonical_display_name: MNE-DR-004 能力归属
historical_run_display_name: MNE-DR-003 能力归属
research_complete: true
report_preserved: true
Pro_adjudication: ACCEPT_WITH_MATERIAL_CORRECTIONS
corrected_candidate_prepared: true
Owner_disposition: OWNER_CONFIRMED_OPTION_A_ACCEPT_MODIFIED_PROVISIONAL_BASELINE
Owner_decision_ref: notes/owner-decision-results/MNE-REUSABLE-CAPABILITY-OWNERSHIP-OWNER-DECISION-001.md
candidate_status: OWNER_ACCEPTED_MODIFIED_PROVISIONAL_BASELINE
bounded_validation_design_prepared: true
bounded_validation_package_prepared: true
validation_disposition_pending: true
execution_profile_selected: false
validation_execution_authorized: false
implementation_authorized: false
shared_repository_creation_or_migration_authorized: false
execution_source_modified_for_F1_semantics: false
Meta_Agent_modified: false
real_target_modified: false
```

## Current result

The independent Fable report and fresh Pro adjudication produced a corrected role-federated model. The Owner accepted that model as a modified provisional baseline:

- Mnemosyne currently owns the reusable capability catalogue;
- no new shared capability repository is created now;
- Meta-Agent retains its own methodology and target-truth authority;
- each target owns its capability selection, adaptation, implementation and current truth;
- stable capability identity, revisions and explicit lifecycle relations are candidates for evidence;
- target-local selection is authoritative for the target;
- meta-side impact views are derived and non-authoritative;
- upstream change creates review candidates, not automatic target writes or standing writer authority;
- any future ownership cutover remains separately gated.

Controlling candidate:

```text
notes/reusable-agent-capability-ownership-and-lifecycle-model-candidate-v0.1.md
```

## Prepared bounded validation design

MNEMOSYNE-225 prepared:

```text
notes/validation-designs/
reusable-capability-ownership-and-lifecycle-bounded-validation-v0.1.md

notes/reusable-capability-ownership-validation-package-v0.1/

notes/owner-decision-candidates/
MNE-REUSABLE-CAPABILITY-OWNERSHIP-VALIDATION-DISPOSITION-CANDIDATE-001.md
```

The design uses one public/synthetic code-library-shaped target only as a domain fixture. It tests:

1. initial target-local capability selection;
2. compatible upstream revision;
3. breaking upstream revision;
4. split, merge and retirement relations;
5. stale/incorrect derived impact view;
6. minimum-record versus excessive-schema burden.

It explicitly does not build the business-function code-library Agent. Future real construction remains a Meta-Agent/target-repository task under separate authority.

## Current gate

```yaml
next_gate: OWNER_VALIDATION_DISPOSITION
Owner_decision_candidate: notes/owner-decision-candidates/MNE-REUSABLE-CAPABILITY-OWNERSHIP-VALIDATION-DISPOSITION-CANDIDATE-001.md
default_recommendation: A_accept_design_and_authorize_exact_execution_profile_preparation_only
validation_execution_selected: false
validation_execution_authorized: false
real_target_construction_selected: false
```

Design acceptance, exact run-profile preparation, validation execution, fresh-Pro adjudication, implementation and real-target adoption remain separate gates.

## Construction boundary

This F1 route may use the already Owner-confirmed high-level code-library domain shape as synthetic validation context. It must not:

- identify or open the real target repository by guess;
- read private code or requirements;
- create target instructions or target truth;
- modify Meta-Agent;
- start construction, migration, activation or a real pilot.

When real construction is later selected, Meta-Agent may conduct target design, while the target's own approved repository/store remains the authority for its selection, adaptation, implementation and current truth.

## Parallel F2/V2 boundary

At validation-design start, another conversation owned:

```text
mnemosyne-224-repair-v2a-sentinel-publication-freshness
```

Its observed write set was limited to F2/V2 status and a V2-A sentinel repair package. It did not overlap the F1 candidate, Owner decision, F1 status, F1 package or next-step repository-write guard.

This design does not adjudicate, authorize or execute F2/V2. Before PR publication or any future run-profile preparation, latest master, active branches, open PRs, read/write dependencies, authority scope and merge-order effects must be rechecked.

## Reply-guidance amendment in the same task

MNEMOSYNE-225 also records a narrow user-approved behavior guard:

```text
current/next-step-repository-write-visibility-guard.md
```

It requires a meaningful closing `## 下一步` section to state, near the model recommendation, whether the next stage writes a repository. This is a response-planning clarification, not an F1 semantic change or validation execution.

## Still not authorized

- exact validation execution-profile preparation until Owner selects it;
- validation execution;
- public validation repository creation or modification;
- capability lifecycle schema implementation;
- new shared repository creation or migration;
- catalogue transfer to Meta-Agent;
- Meta-Agent or real-target modification;
- target adoption, migration or activation;
- automatic downstream propagation;
- private-material ingestion;
- F2/V2 action through this route;
- Work, Deep Research, Fable, Scheduled Tasks or external quota;
- auto-merge.

## Safe next action

Review and publish the MNEMOSYNE-225 preparation package. After merge, the Owner may select A, B, C or D in the validation disposition candidate. No run follows automatically.
