# Adaptive Explanation Stage B0 — Execution Taskbook v0.1

> Read-only execution taskbook for a future smoke run. This file does not authorize execution by itself and does not permit GitHub or target-project writes.

```yaml
taskbook_id: ADAPTIVE-EXPLANATION-STAGE-B0-EXECUTION-TASKBOOK-001
created_by_task: MNEMOSYNE-176
version: 0.1.0
status: ready_pending_explicit_execution_disposition
smoke_cells: 32
real_participants: prohibited
repository_write_during_run: prohibited
```

## 1. Required inputs

At execution time, pin one repository commit containing:

```text
notes/adaptive-explanation-stage-b0-package/README.md
notes/adaptive-explanation-stage-b0-package/01-protocol-spec-v0.1.md
notes/adaptive-explanation-stage-b0-package/02-condition-contracts-v0.1.md
notes/adaptive-explanation-stage-b0-package/03-synthetic-fixture-set-v0.1.md
notes/adaptive-explanation-stage-b0-package/04-rubric-and-decision-rules-v0.1.md
notes/adaptive-explanation-stage-b0-package/05-execution-taskbook-v0.1.md
notes/adaptive-explanation-stage-b0-package/06-run-manifest-template-v0.1.md
notes/adaptive-explanation-stage-b0-package/07-return-and-review-package-v0.1.md
```

Do not execute from a moving branch without recording the exact commit SHA.

## 2. Mandatory preflight

```yaml
execution_preflight:
  explicit_user_execution_authorization:
  package_commit_sha:
  package_files_readable: yes | no
  package_versions_all_0_1_0: yes | no
  fixture_math_review_completed: yes | no
  public_hidden_packet_separation_verified: yes | no
  tutor_context_isolation_available: yes | no
  reviewer_context_separate_from_tutor: yes | no
  private_or_current_user_material_present: no_required
  repository_write_permissions_disabled_or_unused: yes | no
  same_visible_executor_condition_for_all_primary_cells: yes | no
  exact_backend_attestation_available: usually_no
```

Return only `PREFLIGHT_FAILURE` when any required field fails. Do not improvise a weaker execution mode.

## 3. Capability split

```yaml
recommended_roles:
  controller:
    capability: reliable_file_identity_and_context_orchestration
    frontier_required: no_by_default
  tutor_workers:
    capability: strict_contract_following_and_mathematics_correctness
    frontier_required: no_by_default
    same_visible_condition_across_primary_cells: required
  reviewers:
    capability: mathematics_and_protocol_judgment
    frontier_or_domain_expert_review: recommended
  final_adjudicator:
    capability: high_reasoning_for_material_disagreement_or_stop_condition
```

The goal is to preserve frontier quota for review and adjudication rather than use it automatically for every frozen cell. This is a candidate operational split, not proof that a next-tier model is adequate.

## 4. Context-isolation implementations

Allowed implementations:

1. separate fresh conversation/context for each cell;
2. orchestrator with isolated worker contexts that cannot see controller hidden data;
3. API or local harness that constructs each tutor request from only the common envelope, one condition and one public fixture;
4. another mechanism with demonstrable equivalent isolation.

Disallowed:

- one long context that includes all hidden keys and asks the model to “pretend not to know” them;
- one context containing all four condition prompts and all prior outputs;
- reviewer scoring in the tutor context before all tutor turns are complete;
- passing other condition outputs as examples;
- using the current user's real learning dialogue as a fixture.

If isolation is uncertain, return:

```yaml
status: CONTEXT_ISOLATION_FAILURE
cells_started: 0
reason:
```

## 5. Smoke matrix and order

### Fixtures

```yaml
smoke_fixtures:
  - AE-CALC-001
  - AE-CALC-003
  - AE-LA-001
  - AE-LA-003
  - AE-PROB-001
  - AE-PROB-002
  - AE-X-001
  - AE-X-003
```

### Conditions

```yaml
conditions:
  - C0
  - C1
  - C2
  - C3
```

### Cell IDs and rotation

```yaml
cell_order:
  - [B0S-AE-CALC-001-C0, B0S-AE-CALC-001-C1, B0S-AE-CALC-001-C2, B0S-AE-CALC-001-C3]
  - [B0S-AE-CALC-003-C1, B0S-AE-CALC-003-C2, B0S-AE-CALC-003-C3, B0S-AE-CALC-003-C0]
  - [B0S-AE-LA-001-C2, B0S-AE-LA-001-C3, B0S-AE-LA-001-C0, B0S-AE-LA-001-C1]
  - [B0S-AE-LA-003-C3, B0S-AE-LA-003-C0, B0S-AE-LA-003-C1, B0S-AE-LA-003-C2]
  - [B0S-AE-PROB-001-C0, B0S-AE-PROB-001-C1, B0S-AE-PROB-001-C2, B0S-AE-PROB-001-C3]
  - [B0S-AE-PROB-002-C1, B0S-AE-PROB-002-C2, B0S-AE-PROB-002-C3, B0S-AE-PROB-002-C0]
  - [B0S-AE-X-001-C2, B0S-AE-X-001-C3, B0S-AE-X-001-C0, B0S-AE-X-001-C1]
  - [B0S-AE-X-003-C3, B0S-AE-X-003-C0, B0S-AE-X-003-C1, B0S-AE-X-003-C2]
```

The rotation does not substitute for context isolation.

## 6. Cell construction algorithm

For each cell:

1. create a fresh tutor-worker context;
2. provide the common envelope;
3. provide only the assigned condition addendum;
4. provide only the fixture public packet up to learner turn 1;
5. capture the exact tutor turn 1 output;
6. provide the scripted learner turn 2 without hidden commentary;
7. capture the exact tutor turn 2 output;
8. close the tutor context;
9. save a cell record with exact input refs and outputs;
10. do not score inside the tutor context.

```yaml
cell_record:
  cell_id:
  fixture_id:
  condition_id:
  package_commit_sha:
  common_envelope_ref:
  condition_ref:
  public_fixture_ref:
  executor_surface:
  visible_model_or_mode:
  started_at:
  completed_at:
  tutor_turn_1_verbatim: |
  tutor_turn_2_verbatim: |
  operational_record_turn_1:
  operational_record_turn_2:
  tool_calls: []
  warnings: []
  truncation: false
```

## 7. Output-format validation

Before review, mechanically check:

- all completed cells have unique IDs;
- exact condition and fixture IDs are present;
- two tutor turns are preserved;
- operational records are present;
- no hidden key appears in the cell input record;
- no output was silently edited;
- incomplete cells are explicitly marked;
- all package versions and commit SHA are recorded.

A malformed output may be repeated once under the targeted-repeat rule, but both attempts must be preserved.

## 8. Reviewer workflow

### Pass A — content and invariant review

For each cell, provide:

- public fixture;
- exact tutor outputs;
- hidden author key;
- generic content/invariant rubric;
- no condition label where practical.

Score:

- critical invariants;
- R01–R14 as applicable;
- case-specific anchors;
- mathematics correctness;
- leakage and profiling.

### Pass B — condition adherence

Reveal the condition contract and score adherence/contamination.

### Adjudication

Use independent adjudication for:

- any critical invariant disagreement;
- disputed mathematics;
- material condition-contamination claim;
- score difference of two or more on a load-bearing dimension;
- any result that would change the smoke disposition.

## 9. Recommended local artifact layout

This is a local/non-repository run layout unless later storage is separately authorized:

```text
stage-b0-smoke-run-<date>/
├── manifest.yaml
├── package-receipt.md
├── cells/
│   └── <cell-id>.md
├── reviews/
│   ├── reviewer-a/
│   ├── reviewer-b/
│   └── adjudication/
├── summaries/
│   ├── invariant-screen.md
│   ├── condition-comparison.md
│   └── smoke-disposition.md
└── warnings-and-failures.md
```

Do not store private data. Repository ingestion requires a later task-local authorization and preflight.

## 10. Failure handling

```yaml
failure_handling:
  tutor_output_missing_or_truncated:
    - preserve_failed_attempt
    - one_targeted_repeat_allowed
  prompt_or_fixture_mismatch:
    - invalidate_cell
    - inspect_controller
  hidden_key_leakage:
    - stop_run
    - preserve_evidence
  critical_math_error:
    - complete_current_cell_capture
    - trigger_immediate_review
    - stop_if_repeated_or_systemic
  condition_contamination:
    - invalidate_affected_cells
    - inspect_context_isolation
  product_or_quota_fallback_notice:
    - record_visible_notice
    - do_not_infer_backend
    - decide_whether_same_visible_condition_can_continue
```

## 11. Cost and quota controls

- Run only smoke, not core.
- Use one primary run per cell.
- Do not repeat every cell for nondeterminism.
- Reserve targeted repeats for failures or decision-changing ambiguity.
- Prefer a validated next-tier executor for frozen cells when isolation and correctness are adequate.
- Use frontier review for ambiguous or high-impact adjudication rather than routine formatting.
- Stop when review burden becomes disproportionate.

## 12. Completion receipt

```yaml
execution_completion:
  status: COMPLETE | PARTIAL_STOP | PREFLIGHT_FAILURE | CONTEXT_ISOLATION_FAILURE
  cells_expected: 32
  cells_completed:
  cells_invalid:
  cells_repeated:
  critical_stop_triggered: yes | no
  run_manifest_path:
  artifact_root:
  repository_writes_performed: false
  current_user_data_used: false
  real_participants_used: false
```

## 13. Boundary

Execution of this taskbook, when later authorized, still does not:

- prove learning efficacy;
- validate persistent learner state;
- authorize Stage B1;
- configure GPT Live;
- modify Meta-Agent;
- change Mnemosyne execution source;
- attest hidden model identity.
