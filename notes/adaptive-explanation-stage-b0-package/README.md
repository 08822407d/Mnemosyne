# Adaptive Explanation Stage B0 Protocol Package

> Non-execution-source design package for a public/synthetic protocol pre-pilot. This package does not run an experiment, assess the current user, recruit participants, configure GPT Live, create persistent learner memory, or modify any target project.

```yaml
package_id: ADAPTIVE-EXPLANATION-STAGE-B0-PROTOCOL-PACKAGE-001
created_by_task: MNEMOSYNE-176
source_research: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001
source_decision_package: notes/research-batch-reviews/2026-07-adaptive-explanation-stage-a/03-stage-b-decision-preparation.md
user_disposition: SELECT_STAGE_B0_SYNTHETIC_PREPILOT_DESIGN
status: protocol_design_complete_pending_PR_merge_and_owner_execution_decision
execution_source: current/human-approved-spec.md
execution_source_modified: false
Stage_B0_executed: false
Stage_B1_selected: false
```

## Purpose

Stage A found enough evidence to justify testing an adaptive explanation protocol, but not enough to deploy one. Stage B0 is therefore a protocol and safety pre-pilot using only public mathematics content and synthetic learner traces.

The package is designed to determine whether the proposed conditions can be implemented and distinguished without:

- inventing stable learner traits;
- confusing sparse dialogue with validated diagnosis;
- leaking answers through diagnostic probes;
- ignoring `unknown`;
- failing to detect a known tutor explanation error;
- creating an excessive review and execution burden;
- using private learning history or real participant data.

Stage B0 cannot establish real learning efficacy, delayed retention, real-user burden, fairness across populations, or the validity of persistent learner memory.

## Package map

```text
notes/adaptive-explanation-stage-b0-package/
├── README.md
├── 01-protocol-spec-v0.1.md
├── 02-condition-contracts-v0.1.md
├── 03-synthetic-fixture-set-v0.1.md
├── 04-rubric-and-decision-rules-v0.1.md
├── 05-execution-taskbook-v0.1.md
├── 06-run-manifest-template-v0.1.md
└── 07-return-and-review-package-v0.1.md

notes/research-prompts/
└── ADAPTIVE-EXPLANATION-STAGE-B0-SMOKE-EXECUTION-001.md

current/
├── adaptive-explanation-stage-a-research-status.md
└── adaptive-explanation-stage-b0-status.md
```

## Package roles

| File | Role |
|---|---|
| `01-protocol-spec-v0.1.md` | Scope, experimental unit, smoke/core phases, isolation requirements, stop and rollback rules |
| `02-condition-contracts-v0.1.md` | Frozen common envelope and C0–C3 condition definitions |
| `03-synthetic-fixture-set-v0.1.md` | Public case packets, hidden author keys and smoke/core fixture selection |
| `04-rubric-and-decision-rules-v0.1.md` | Blocking invariants, scoring rubric, condition-separation and disposition rules |
| `05-execution-taskbook-v0.1.md` | Controller/worker/reviewer workflow and exact execution order |
| `06-run-manifest-template-v0.1.md` | Visible model/surface, input identity, cell inventory, failures and artifact receipt |
| `07-return-and-review-package-v0.1.md` | Consolidated result bundle and maintainer review contract |
| `ADAPTIVE-EXPLANATION-STAGE-B0-SMOKE-EXECUTION-001.md` | One self-contained execution task that reads the package and runs only the smoke phase after an explicit execution decision |

## Selected route and boundary

The user instructed the maintainer to continue according to the recommended scheme after PR #227 merged. The immediately preceding recommendation was:

```yaml
selected_option: SELECT_STAGE_B0_SYNTHETIC_PREPILOT_DESIGN
meaning: design_but_do_not_execute_a_public_or_synthetic_B0_protocol
```

This task therefore prepares the complete design and execution package. It does not infer authorization to run the smoke phase.

## Efficiency design

The package reduces future frontier-model conversation use by separating work by capability:

```yaml
frontier_or_high_reasoning:
  - review_protocol_and_fixture_validity
  - adjudicate_ambiguous_or_conflicting_cases
  - review_severe_failures_and_condition_contamination
  - decide_whether_to_expand_from_smoke_to_core

validated_next_tier_executor:
  - execute_frozen_cells_when_context_isolation_is_available
  - preserve_exact_prompts_and_outputs
  - complete_run_manifest_fields
  - perform_non_semantic_packaging

mechanical_checks:
  - path_and_file_identity
  - case_condition_matrix_completeness
  - missing_output_detection
  - schema_and_ID_validation
  - forbidden_material_scan

human_decision:
  - authorize_execution
  - approve_any_change_to_conditions_or_fixture_scope
  - decide_whether_B0_evidence_supports_core_expansion_or_later_B1_preparation
```

A next-tier model is not assumed adequate merely because the task is bounded. The smoke execution must record the visible condition and must stop if strict isolation or contract adherence cannot be achieved.

## Phase structure

```yaml
B0_SMOKE:
  cases: 8
  conditions: 4
  primary_cells: 32
  purpose: protocol_feasibility_and_blocking_failure_detection
  authorization: not_granted_by_this_package

B0_CORE:
  additional_cases: 8
  conditions: 4
  additional_primary_cells: 32
  prerequisite: smoke_review_and_fresh_user_decision

B0_TARGETED_REPEATS:
  purpose: inspect_nondeterminism_or_reproduce_severe_failures
  default: only_failed_or_ambiguous_cells
  automatic_blanket_repetition: prohibited
```

## Non-negotiable isolation rule

The tutor worker for a cell must receive only:

- the common envelope;
- the assigned condition contract;
- the public fixture packet;
- the scripted learner follow-up at the proper turn.

It must not receive:

- the hidden author key;
- expected diagnosis labels;
- scoring anchors;
- outputs from other conditions;
- the final reviewer decision.

If the available product surface cannot guarantee this separation, the run must return `CONTEXT_ISOLATION_FAILURE` without manufacturing results.

## Exactly one current safe next action

```yaml
safe_next_action:
  current:
    - review_and_merge_the_single_MNEMOSYNE_176_PR
  after_merge:
    - record_one_explicit_execute_or_defer_disposition_for_ADAPTIVE_EXPLANATION_STAGE_B0_SMOKE_EXECUTION_001
  automatic_execution: false
  Stage_B1_preparation: prohibited
```
