# Reusable Agent Capability Ownership Research — Current Status

```yaml
status_id: MNE-REUSABLE-CAPABILITY-OWNERSHIP-STATUS-001
last_updated_by_task: MNEMOSYNE-227
source_master_at_handoff_preparation: 5ca091e1c52bb1e7483b2d54e9259d3ec85b7b93
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
handoff_prepared: true
handoff_package: handoff/mnemosyne-f1-validation-disposition-handoff-package.md
startup_prompt: handoff/mnemosyne-f1-validation-disposition-startup-prompt.md
source_conversation_role_after_handoff: historical_fallback_and_post_merge_verification_only
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
permitted_dispositions:
  - A_accept_design_and_authorize_exact_execution_profile_preparation_only
  - B_accept_design_and_defer_synthetic_execution_preparation
  - C_revise_design
  - D_reject_bounded_validation_and_stop_at_provisional_baseline
default_recommendation: A_accept_design_and_authorize_exact_execution_profile_preparation_only
Owner_choice_recorded: false
validation_execution_selected: false
validation_execution_authorized: false
real_target_construction_selected: false
```

The route is intentionally blocked on a human Owner decision. Design acceptance, exact run-profile preparation, validation execution, fresh-Pro adjudication, implementation and real-target adoption remain separate gates.

## Handoff state

MNEMOSYNE-227 prepares a Mnemosyne-owned handoff for a fresh Pro conversation. The receiving sequence is:

```text
receive authorized handoff package
→ emit receive report and stop
→ separately load Mnemosyne guidance
→ confirm the F1 task was preserved
→ present A/B/C/D in natural Chinese and obtain the Owner decision
```

The handoff does not itself choose an option or authorize repository writes.

## Construction boundary

This F1 route may use the already Owner-confirmed high-level code-library domain shape as synthetic validation context. It must not:

- identify or open the real target repository by guess;
- read private code or requirements;
- create target instructions or target truth;
- modify Meta-Agent;
- start construction, migration, activation or a real pilot.

When real construction is later selected, Meta-Agent may conduct target design, while the target's own approved repository/store remains the authority for its selection, adaptation, implementation and current truth.

## F2/V2 exclusion

PR #294 merged the separate MNEMOSYNE-226/F2/V2 provenance and package-003 route into `master@5ca091e1c52bb1e7483b2d54e9259d3ec85b7b93` before this handoff was prepared.

That route is not transferred by this package. The receiver must not:

- treat F2/V2 current status as the F1 action plan;
- issue or infer V2-A G2A/A0 authorization;
- create `v2a-sentinel-001-controller`;
- write the validation repository;
- adjudicate or continue F2/V2.

## Reply-guidance state

The user-approved guard is active on `master`:

```text
current/next-step-repository-write-visibility-guard.md
```

A meaningful closing `## 下一步` must state near the model recommendation whether the next stage writes a repository.

## Still not authorized

- exact validation execution-profile preparation until the Owner selects A;
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

After the handoff package is merged, a fresh Pro conversation should receive the package, separately load Mnemosyne guidance, and then present the exact A/B/C/D validation-disposition choices. If the Owner does not choose, the safe state is no repository write and no validation action.
