# Target-Agent Lifecycle Validation Package v0.2

> Frozen public/synthetic validation package for candidate v0.2. This package prepares execution and result-return materials only. It does not create a validation repository, execute a scenario, use real target material, spend quota, adopt the candidate, modify Meta-Agent, or authorize a PR/merge.

```yaml
package_id: MNE-TARGET-LIFECYCLE-VALIDATION-PACKAGE-002
version: 0.2.0
created_by_task: MNEMOSYNE-209
repository: 08822407d/Mnemosyne
source_candidate: notes/target-agent-container-evolution-and-dependency-model-candidate-v0.2.md
source_validation: notes/validation-designs/target-agent-container-evolution-and-dependency-model-validation-v0.2.md
source_owner_result: notes/owner-decision-results/MNE-TARGET-LIFECYCLE-OWNER-REVIEW-RESULT-001.md
status: prepared_not_selected_not_executed
material_class: public_synthetic_only
validation_repository_created: false
validation_execution_authorized: false
real_target_write_authorized: false
external_quota_authorized: false
```

## Purpose

The package converts the Owner-confirmed provisional target-lifecycle baseline into one reconstructable next-tier validation workflow.

It tests whether a synthetic implementation can preserve:

- target-owned truth and bounded task writers;
- safe conditional concurrency inside one repository;
- fail-closed shared/global/unknown scope;
- no automatic upstream-to-downstream propagation;
- practical change-route evidence without taxonomy over-design;
- human-facing and Agent-facing library change documentation;
- project-owned on-demand migration;
- no substantive downstream content in parent/meta repositories;
- non-authoritative source-identified backup/restore.

It is designed to discover architecture and protocol failures, not to prove universal correctness.

## Package map

```text
notes/target-agent-lifecycle-validation-package-v0.2/
├── README.md
├── 00-run-scope-and-owner-decision.md
├── 01-synthetic-fixture-and-scenario-contracts.md
├── 02-next-tier-executor-taskbook.md
├── 03-mechanical-checks-and-rubric.md
├── 04-run-manifest-and-result-template.md
└── 05-startup-message.md
```

## File roles

| File | Role |
|---|---|
| `00-run-scope-and-owner-decision.md` | Unresolved Owner choices and authorization gates required before any run |
| `01-synthetic-fixture-and-scenario-contracts.md` | Frozen fixture, S0–S11 scenario inputs, expected invariants and failure conditions |
| `02-next-tier-executor-taskbook.md` | Ordered executor procedure, stop rules and no-architecture-invention contract |
| `03-mechanical-checks-and-rubric.md` | Required mechanical evidence, critical blockers and semantic scoring/dispositions |
| `04-run-manifest-and-result-template.md` | Run identity, authorization, cell ledger, incidents, no-write proof and return bundle schema |
| `05-startup-message.md` | Copyable startup instruction for a later separately authorized execution conversation/task |

## Phase state

```yaml
phase_state:
  V0_SURFACE_AND_SENTINEL:
    materials_prepared: true
    selected: false
    authorized: false
    executed: false
    substantive_scenarios: 0

  V1_BOUNDED_SMOKE:
    materials_prepared: true
    selected: false
    authorized: false
    executed: false
    baseline_scenarios:
      - S1
      - S2
      - S3
      - S4
      - S5
      - S6
      - S7
      - S8
      - S9
      - S11
    exploratory_scenarios:
      - S10

  V2_REFINED_OR_REPEAT:
    materials_prepared: false
    authorized: false
    executed: false
```

V0 validates repository/material/surface identity and real-repository no-write proof before substantive work. A valid V0 does not automatically authorize V1.

## Non-negotiable boundaries

- Use a separate temporary public/synthetic repository; do not use Mnemosyne, Meta-Agent or a real business target as the fixture.
- Do not use private source, credentials, real learner data, complete private conversations or customer material.
- Do not let the executor revise candidate semantics during the run.
- Do not infer missing Owner decisions or silently fill TLR-03/TLR-04 deferrals.
- Do not create a substantive parent/meta copy of a synthetic target.
- Do not write run outputs back to Mnemosyne unless a later task separately authorizes material/provenance-reviewed ingestion.
- Do not run Deep Research or Fable as part of validation unless a later explicit task changes the design.
- Do not infer backend model identity from the visible picker, behavior, speed or self-report.
- Preserve failed attempts and incidents; do not overwrite them with a clean retry.

## Execution capability assessment

```yaml
capability_estimate:
  package_semantic_design:
    class: FRONTIER_COMPLETED
  frozen_scenario_execution:
    class: NEXT_TIER_SUFFICIENT_CANDIDATE
    limitation: must be reassessed against the selected product surface before authorization
  mechanical_checks:
    class: MECHANICAL_REQUIRED
  semantic_adjudication:
    class: PRO_FRONTIER_REQUIRED
  Owner_acceptance:
    class: HUMAN_REQUIRED
  exact_backend_identity: unknown_or_not_attestable
```

## Research assessment

```yaml
deep_research_assessment:
  status: NOT_NEEDED_BEFORE_V0_OR_V1
  reason: the remaining gap is controlled execution evidence, not broad external research
```

## Safe next gate

The only eligible continuation after this package is reviewed is an explicit Owner decision using `00-run-scope-and-owner-decision.md`.

That decision may authorize V0, revise the package, defer or stop. It does not automatically authorize V1, target adoption or result ingestion into Mnemosyne.
