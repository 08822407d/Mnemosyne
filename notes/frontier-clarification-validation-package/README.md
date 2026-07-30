# Frontier Clarification Validation Package

> Non-execution-source, public/synthetic validation package. This package prepares frozen materials for later separately authorized V0/V1 runs. It does not execute validation, select a product surface or model condition, spend quota, use real user data, modify an execution source, modify Meta-Agent, or take over the non-FABLE health-review route.

```yaml
package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
created_by_task: MNEMOSYNE-181
source_validation_id: FRONTIER-PLANNING-CLARIFICATION-HANDOFF-VALIDATION-001
version: 0.1.0
status: prepared_not_selected_not_executed
repository: 08822407d/Mnemosyne
execution_source: current/human-approved-spec.md
execution_source_modified: false
material_class: public_or_synthetic_only
real_user_data: prohibited
private_material: prohibited
validation_execution_authorized: false
repository_write_by_future_validation_executor: prohibited
target_project_write: prohibited
Meta_Agent_modified: false
non_FABLE_health_review_modified: false
```

## Purpose

The package converts the adjudicated validation design into a reconstructable execution-and-review package for testing five clarification conditions:

- `Q0`: bare question / unexplained option baseline;
- `Q1`: structured nonconversational owner package;
- `Q2`: frozen packet plus bounded next-tier interviewer;
- `Q3`: Q2 plus predefined semantic escalation and frontier reentry;
- `Q4`: direct frontier clarification comparator.

The package asks whether context-rich presentation, bounded interviewing and gated escalation reduce burden and frontier turns without degrading intent fidelity, owner authority, correction handling, escalation, answer-ledger integrity or research-trigger judgment.

It is a protocol-feasibility and failure-discovery package. It does not establish a universal clarification architecture, a model hierarchy, or a production default.

## Package map

```text
notes/frontier-clarification-validation-package/
├── README.md
├── 00-scope-manifest-v0.1.md
├── 01-protocol-spec-v0.1.md
├── 02-condition-contracts-q0-q4-v0.1.md
├── 03-public-synthetic-scenario-set-v0.1.md
├── 04-hidden-author-keys-v0.1.md
├── 05-answer-ledger-and-escalation-tests-v0.1.md
├── 06-rubric-and-decision-rules-v0.1.md
├── 07-reviewer-and-adjudication-taskbook-v0.1.md
├── 08-v0-sentinel-context-isolation-taskbook-v0.1.md
├── 09-v1-small-smoke-execution-taskbook-v0.1.md
├── 10-run-manifest-template-v0.1.md
├── 11-result-return-and-maintainer-review-package-v0.1.md
├── 12-execution-surface-and-user-decision-package-v0.1.md
└── 13-package-integrity-checklist-v0.1.md
```

## File roles

| File | Role |
|---|---|
| `00-scope-manifest-v0.1.md` | Package identity, source refs, included/excluded scope, phase state and unresolved human decisions |
| `01-protocol-spec-v0.1.md` | Validation objective, unit, roles, isolation, phases, non-claims, stop and rollback rules |
| `02-condition-contracts-q0-q4-v0.1.md` | Frozen common envelope and exact Q0–Q4 condition behavior contracts |
| `03-public-synthetic-scenario-set-v0.1.md` | Worker-visible synthetic scenario sources and deterministic condition-rendering inputs |
| `04-hidden-author-keys-v0.1.md` | Controller/reviewer-only scripted answers, planted conflicts, expected routes and scoring anchors |
| `05-answer-ledger-and-escalation-tests-v0.1.md` | Ledger schema, correction/supersession rules and semantic escalation test definitions |
| `06-rubric-and-decision-rules-v0.1.md` | Protocol-validity blockers, condition safety blockers, comparative measures and disposition rules |
| `07-reviewer-and-adjudication-taskbook-v0.1.md` | Reviewer passes, provenance, disagreement handling and adjudication workflow |
| `08-v0-sentinel-context-isolation-taskbook-v0.1.md` | Zero-substantive-cell sentinel/isolation preflight; requires later authorization |
| `09-v1-small-smoke-execution-taskbook-v0.1.md` | Forty-cell V1 smoke workflow; requires a valid V0 result and later authorization |
| `10-run-manifest-template-v0.1.md` | Run identity, condition/surface map, artifact identity, cell inventory, incidents and no-write receipt |
| `11-result-return-and-maintainer-review-package-v0.1.md` | Complete return bundle, acceptance gates, allowed dispositions and maintainer review schema |
| `12-execution-surface-and-user-decision-package-v0.1.md` | Options and unresolved owner decisions required before any V0/V1 run |
| `13-package-integrity-checklist-v0.1.md` | Mechanical completeness, reference, forbidden-material and no-execution checks |

## Frozen scenario inventory

```yaml
scenario_inventory:
  V1_smoke:
    - FCV-AUTH-001
    - FCV-PRIV-001
    - FCV-ARCH-001
    - FCV-FIXED-001
    - FCV-FACT-001
    - FCV-FALSE-001
    - FCV-REST-001
    - FCV-RESEARCH-001
  V2_reserve_not_authorized:
    - FCV-RESEARCH-002
    - FCV-CORR-001
    - FCV-HEDGE-001
    - FCV-TRUST-001
    - FCV-BACKGROUND-001
    - FCV-IDENTITY-001
```

V1 has `8 scenarios × 5 conditions = 40 primary cells`. No blanket repetition is defined. Targeted repeats are limited to malformed, truncated or identity-failed cells and require preservation of every attempt.

The six reserve scenarios help freeze future scope and reveal coverage gaps. This package does not provide a V2 execution taskbook or authorize V2/V3.

## Role separation

```yaml
roles:
  package_author:
    sees:
      - source_adjudication
      - public_scenarios
      - hidden_author_keys
      - condition_contracts
      - rubric
    may_execute_validation: false

  mechanical_controller:
    sees:
      - run_manifest
      - condition_and_scenario_assignment
      - scripted_owner_turn_release_schedule
    must_not_generate_worker_outputs_after_hidden_key_access: true

  worker:
    sees:
      - common_envelope
      - exactly_one_condition_contract
      - exactly_one_worker_visible_scenario_packet
      - scripted_owner_response_only_when_released
    must_not_see:
      - hidden_author_keys
      - other_condition_contracts
      - other_condition_outputs
      - reviewer_scores
      - future_scripted_turns

  reviewer:
    sees:
      - exact_worker_inputs_and_outputs
      - hidden_author_key
      - generic_rubric
    must_not_rewrite_outputs: true

  adjudicator:
    used_when:
      - critical_invariant_disagreement
      - material_score_disagreement
      - disputed_scenario_or_contract_defect
      - disposition_changing_conflict
```

A context that has seen hidden keys cannot later serve as a worker by claiming to forget them.

## Phase state

```yaml
phase_state:
  V0_MECHANICAL_AND_SENTINEL:
    materials_prepared: true
    selected: false
    authorized: false
    executed: false
    substantive_cells: 0

  V1_SMALL_SMOKE:
    materials_prepared: true
    selected: false
    authorized: false
    executed: false
    primary_cells: 40

  V2_CORE:
    reserve_scenarios_frozen: true
    execution_taskbook_prepared: false
    selected: false
    authorized: false
    executed: false

  V3_TARGET_PROJECT_PORTABILITY:
    target_pattern_selected: false
    materials_prepared: false
    selected: false
    authorized: false
    executed: false
```

## Non-negotiable boundaries

- Do not use a normal maintenance conversation as an execution surface merely because it can read the package.
- Do not place the hidden-key file in a worker context.
- Do not allow worker web, repository search, connected apps or broad file access unless a later run contract explicitly authorizes a symmetric tool condition; the default is no tools and package inputs only.
- Do not use real user conversations, voice transcripts, private files, customer data or target-project material.
- Do not infer a particular backend from picker labels, latency, style, self-report or visible reasoning traces.
- Do not write run outputs to this repository unless a later task separately authorizes ingestion after material and provenance review.
- Do not change `current/human-approved-spec.md` or any target-project truth source based on package preparation or a future result.
- Do not modify `target-projects/meta-agent/` or import the non-FABLE health-review route.
- Do not fabricate V0/V1/V2/V3 results.

## Critical distinction: invalid run versus unsafe condition

A protocol-validity failure—such as context leakage, hidden-key exposure, private material, or output-identity loss—invalidates affected evidence and may stop the run.

A condition safety failure—such as inventing an owner decision, converting tentative assent into approval, or missing a planted high-impact escalation—is a substantive result about that condition. It blocks adoption of that condition but does not erase otherwise valid evidence from uncontaminated cells.

## Package preparation capability assessment

```yaml
model_capability_estimate:
  package_design:
    capability_class: FRONTIER_RECOMMENDED
    reason: synthetic scenario authorship, hidden-key design, condition semantics and blocking-invariant adjudication require open-ended architecture judgment
  frozen_file_population:
    capability_class: NEXT_TIER_SUFFICIENT_CANDIDATE
    reason: only after inputs and contracts are frozen and independently reviewable
  integrity_checks:
    capability_class: MECHANICAL_ONLY
  future_V0_or_V1_execution:
    capability_class: UNKNOWN_REASSESS_BEFORE_EXECUTION
    reason: execution surface, isolation proof, visible model/mode mapping and quota remain human decisions
  exact_backend_identity: unknown_or_not_attestable
```

## Research assessment

```yaml
deep_research_assessment:
  status: NOT_NEEDED
  reason: primary and independent research were completed and adjudicated; the remaining evidence gap is direct controlled workflow validation

parallel_frontier_research_assessment:
  status: NOT_NEEDED
  reason: no distinct same-topic research question remains before the controlled validation gate
```

## Safe next gate after package merge

After this package is reviewed and merged, the only eligible continuation is a separate owner decision using `12-execution-surface-and-user-decision-package-v0.1.md`. That decision may authorize V0, defer, revise or stop. It does not automatically authorize V1.
