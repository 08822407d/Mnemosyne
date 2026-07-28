# ADAPTIVE-EXPLANATION-STAGE-B0-SMOKE-EXECUTION-001

```yaml
task_id: ADAPTIVE-EXPLANATION-STAGE-B0-SMOKE-EXECUTION-001
task_type: read_only_public_synthetic_multi_condition_protocol_smoke_run
execute_only_after: explicit_user_execution_authorization
preferred_surface: agent_environment_with_demonstrable_isolated_worker_contexts
ordinary_single_context_chat: unsuitable
repository_write: prohibited
real_participants: prohibited
current_user_data: prohibited
persistent_learner_memory: prohibited
Stage_B1: prohibited
```

## Mandatory input-integrity and isolation gate

Before generating any tutor response, read the following files from one exact pinned Mnemosyne commit:

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

Verify internally:

```yaml
input_integrity:
  exact_task_id_available: true
  package_commit_sha_available: true
  all_eight_package_files_available: true
  package_version_0_1_0: true
  fixture_set_contains_16_cases: true
  smoke_fixture_set_contains_8_cases: true
  condition_set_contains_C0_C1_C2_C3: true
  explicit_user_execution_authorization_available: true
  repository_write_prohibited: understood
```

Verify isolation:

```yaml
isolation_gate:
  fresh_tutor_worker_context_per_cell: required
  tutor_worker_hidden_author_key_access: prohibited
  tutor_worker_other_condition_access: prohibited
  reviewer_context_separate_from_tutor: required
  controller_may_read_hidden_keys_only_if_it_never_generates_tutor_content_after_that_access: required
```

If any input requirement fails, return only:

```yaml
status: INPUT_INTEGRITY_FAILURE
cells_started: 0
missing_or_invalid_inputs: []
```

If isolation cannot be guaranteed, return only:

```yaml
status: CONTEXT_ISOLATION_FAILURE
cells_started: 0
reason:
```

Do not use a single context that has seen hidden keys and then “pretend” not to know them.

## Execution scope

Run only the smoke matrix:

```yaml
fixtures:
  - AE-CALC-001
  - AE-CALC-003
  - AE-LA-001
  - AE-LA-003
  - AE-PROB-001
  - AE-PROB-002
  - AE-X-001
  - AE-X-003
conditions:
  - C0
  - C1
  - C2
  - C3
primary_cells: 32
blanket_repeats: prohibited
targeted_repeats: only_for_malformed_truncated_or_decision_changing_ambiguity
```

Use the exact cell order in the execution taskbook.

## Worker construction

For each cell:

1. create a fresh isolated tutor context;
2. provide the common envelope;
3. provide exactly one condition addendum;
4. provide only the fixture public packet through learner turn 1;
5. capture tutor turn 1 verbatim;
6. provide the scripted learner turn 2;
7. capture tutor turn 2 verbatim;
8. close the tutor context;
9. save the exact operational records;
10. do not score inside the tutor context.

The tutor worker must never receive the hidden author key, condition comparison, other outputs or expected score.

## Reviewer construction

Use at least one independent reviewer and preferably two.

Pass A:

- score content and critical invariants;
- hide condition identity where practical;
- use the public packet, tutor outputs, hidden author key and generic rubric.

Pass B:

- reveal the assigned condition;
- score condition adherence and contamination.

Use independent adjudication for critical-invariant disagreement, disputed mathematics, material contamination, or any disagreement that changes the smoke disposition.

## Visible execution condition

Use the same visible executor model/mode condition for all 32 primary cells. Record:

- product surface;
- visible model/mode wording;
- visible reasoning/intelligence wording;
- start/end time;
- quota or fallback notice;
- actual order;
- package commit SHA.

Do not infer or claim the exact served backend from speed, style or self-identification.

A validated next-tier executor is permitted for frozen tutor cells to conserve frontier quota. This run does not validate that executor for other tasks. Frontier or domain-expert review is recommended for disputed mathematics and final adjudication.

## Output artifacts

Create a local result package matching:

```text
stage-b0-smoke-run-<date>/
├── manifest.yaml
├── package-receipt.md
├── cells/
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

No GitHub or connected-service write is permitted.

Preserve all failed, malformed, repeated and unfavorable outputs. Do not rewrite or select the best attempt.

## Critical stop conditions

Stop and return a partial package when:

- hidden author key leaks to a tutor worker;
- condition prompts or outputs contaminate another cell;
- private/current-user material appears;
- context isolation fails;
- output identity is lost;
- mathematics reference answers cannot be validated;
- repeated critical errors make remaining cells uninformative;
- the visible model/mode condition changes and cannot be restored;
- review or execution burden exceeds the approved smoke scope.

## Final result

Return one complete result bundle in the final response:

1. status;
2. completed manifest;
3. downloadable archive or exact file collection;
4. cell count and identities;
5. critical invariant screen;
6. reviewer and adjudication summaries;
7. condition comparison;
8. warnings/incidents;
9. proposed smoke disposition;
10. the copyable return instruction from `07-return-and-review-package-v0.1.md`.

Allowed proposed dispositions:

```yaml
- PROCEED_TO_B0_CORE_DESIGN_AND_EXECUTION_DECISION
- REVISE_AND_REPEAT_SMOKE
- ACCEPT_PARTIAL_PROTOCOL_EVIDENCE_AND_DEFER
- STOP_B0_ROUTE
```

The executor proposes; the Mnemosyne maintainer adjudicates. Do not prepare or execute core or Stage B1.

## Final boundary

This task does not:

- measure real learning;
- assess the current user;
- create a learner profile;
- create persistent or cross-Agent memory;
- configure GPT Live;
- modify Meta-Agent;
- modify Mnemosyne;
- attest a backend.
