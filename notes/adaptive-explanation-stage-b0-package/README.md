# Adaptive Explanation Stage B0 Protocol Package

> Non-execution-source design package for a public/synthetic protocol pre-pilot. This package does not run an experiment, assess the current user, recruit participants, configure GPT Live, create persistent learner memory, or modify any target project.

```yaml
package_id: ADAPTIVE-EXPLANATION-STAGE-B0-PROTOCOL-PACKAGE-001
created_by_task: MNEMOSYNE-176
last_status_task: MNEMOSYNE-177
source_research: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001
source_decision_package: notes/research-batch-reviews/2026-07-adaptive-explanation-stage-a/03-stage-b-decision-preparation.md
user_disposition:
  protocol_design: SELECT_STAGE_B0_SYNTHETIC_PREPILOT_DESIGN
  smoke_execution: EXECUTE_STAGE_B0_SMOKE
status: protocol_designed_smoke_blocked_CONTEXT_ISOLATION_FAILURE_zero_cells
execution_source: current/human-approved-spec.md
execution_source_modified: false
Stage_B0_executed: false
Stage_B0_cells_started: 0
Stage_B1_selected: false
```

## Purpose

Stage A found enough evidence to justify testing an adaptive explanation protocol, but not enough to deploy one. Stage B0 is therefore a protocol and safety pre-pilot using only public mathematics content and synthetic learner traces.

The package is designed to determine whether the proposed conditions can be implemented and distinguished without:

- inventing stable learner traits;
- confusing sparse dialogue with validated diagnosis;
- leaking answers through diagnostic probes;
- ignoring `unknown`;
- failing to detect a known Tutor explanation error;
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
├── 07-return-and-review-package-v0.1.md
├── 08-context-isolation-preflight-result.md
└── 09-isolated-execution-surface-decision-package.md

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
| `08-context-isolation-preflight-result.md` | Exact reason the current standard conversation could not start smoke; records `CONTEXT_ISOLATION_FAILURE`, zero cells |
| `09-isolated-execution-surface-decision-package.md` | Provider-API, agent-runtime and manual-isolation recovery options plus model-capability estimates |
| `ADAPTIVE-EXPLANATION-STAGE-B0-SMOKE-EXECUTION-001.md` | Self-contained smoke task, executable only after a suitable isolated surface and fresh authorization exist |

## Selected route and current block

The user selected protocol design and later explicitly authorized smoke subject to a strict isolation preflight.

```yaml
selected:
  - SELECT_STAGE_B0_SYNTHETIC_PREPILOT_DESIGN
  - EXECUTE_STAGE_B0_SMOKE
required_failure_behavior:
  - return_CONTEXT_ISOLATION_FAILURE_when_true_worker_isolation_is_unavailable
  - do_not_degrade_to_single_context_pseudo_experiment
```

The current surface was:

```yaml
surface: standard_ChatGPT_conversation_with_GitHub_app
fresh_isolated_Tutor_worker_contexts: unavailable
separate_Reviewer_context: unavailable
provider_API_or_agent_runtime: unavailable_in_current_task
result: CONTEXT_ISOLATION_FAILURE
cells_started: 0
```

No experimental output exists. The execution authorization is consumed by the failed preflight and does not automatically carry to another surface.

## Efficiency and capability design

```yaml
frontier_or_high_reasoning:
  - select_and_review_surface_trust_and_isolation_boundary
  - review_protocol_and_fixture_validity
  - adjudicate_ambiguous_or_conflicting_cases
  - review_severe_failures_and_condition_contamination
  - decide_whether_to_expand_from_smoke_to_core

validated_next_tier_executor:
  - implement_a_frozen_harness_after_surface_selection
  - execute_frozen_cells_when_context_isolation_is_available
  - preserve_exact_prompts_and_outputs
  - complete_run_manifest_fields

mechanical_checks:
  - sentinel_isolation_checks
  - path_and_file_identity
  - case_condition_matrix_completeness
  - missing_output_detection
  - schema_and_ID_validation
  - forbidden_material_scan

human_decision:
  - select_or_defer_an_execution_surface
  - authorize_external_cost_or_credentials_if_applicable
  - authorize_smoke_on_the_selected_surface
  - decide_whether_B0_evidence_supports_core_expansion
```

A next-tier model is not assumed adequate merely because the task is bounded. The smoke execution must record the visible condition and stop if isolation or contract adherence cannot be achieved.

## Phase structure

```yaml
B0_SMOKE:
  cases: 8
  conditions: 4
  primary_cells: 32
  purpose: protocol_feasibility_and_blocking_failure_detection
  current_state: blocked_before_cell_start

B0_CORE:
  additional_cases: 8
  conditions: 4
  additional_primary_cells: 32
  prerequisite:
    - valid_smoke_execution
    - smoke_review
    - fresh_user_decision

B0_TARGETED_REPEATS:
  purpose: inspect_nondeterminism_or_reproduce_severe_failures
  default: only_failed_or_ambiguous_cells
  automatic_blanket_repetition: prohibited
```

## Non-negotiable isolation rule

The Tutor worker for a cell must receive only:

- the common envelope;
- the assigned condition contract;
- the public fixture packet;
- the scripted learner follow-up at the proper turn.

It must not receive:

- the hidden author key;
- expected diagnosis labels;
- scoring anchors;
- outputs from other conditions;
- the final Reviewer decision.

If the available product surface cannot guarantee this separation, the run must return `CONTEXT_ISOLATION_FAILURE` without manufacturing results. A context that has seen hidden keys cannot be reused as a Tutor by claiming to forget.

## Current safe next action

```yaml
safe_next_action:
  current:
    - review_and_merge_the_single_MNEMOSYNE_177_PR
  after_merge:
    - choose_PREPARE_PROVIDER_API_HARNESS_or_PREPARE_AGENT_RUNTIME_HARNESS_or_PREPARE_MANUAL_MULTI_CONVERSATION_PACKAGE_or_DEFER_or_STOP
  automatic_execution: false
  Stage_B1_preparation: prohibited
```
