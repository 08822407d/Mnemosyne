# Validation Test-Evidence Strength Levels v0.1

> Owner-accepted non-execution-source validation guidance. It prevents test files, static review and actual runtime execution from being conflated. It does not itself authorize a test run, repository write, runtime supplement or target adoption.

```yaml
record_id: MNE-VALIDATION-TEST-EVIDENCE-STRENGTH-001
version: 0.1.0
task_id: MNEMOSYNE-215
status: OWNER_ACCEPTED_FOR_FUTURE_VALIDATION_PROFILE_USE
source_adjudication: notes/validation-adjudications/MNE-TARGET-LIFECYCLE-V1-ADJUDICATION-001.md
source_owner_decision: notes/owner-decision-results/MNE-TARGET-LIFECYCLE-V1-OWNER-ARCHITECTURE-DECISION-001.md
execution_source_modified: false
runtime_execution_authorized: false
```

## 1. Purpose

A repository may contain a plausible test file even when:

- it is not syntactically valid;
- an import is missing;
- the test runner cannot discover it;
- the environment lacks dependencies;
- the test fails;
- no command was ever run.

Validation records must therefore state the strongest evidence level actually established and must not silently upgrade it.

## 2. Evidence levels

### Level T1 — `TEST_ARTIFACT_PRESENT`

Established facts:

- a test or check artifact exists at an exact path;
- its blob and containing commit are known.

Not established:

- syntax or import correctness;
- test discovery;
- execution;
- pass/fail result.

Minimum fields:

```yaml
test_evidence:
  level: TEST_ARTIFACT_PRESENT
  repository:
  commit:
  path:
  blob:
```

### Level T2 — `STATICALLY_INSPECTED`

Established facts:

- T1 is satisfied;
- an identified reviewer or deterministic static tool inspected the artifact within a stated scope;
- observed issues and limitations are recorded.

Not established:

- runtime execution;
- runner discovery;
- environment compatibility;
- passing assertions.

Minimum additional fields:

```yaml
test_evidence:
  level: STATICALLY_INSPECTED
  reviewer_or_tool:
  review_scope:
  findings: []
  unresolved_runtime_questions: []
```

Static inspection may find a defect, but “no defect found” is not runtime proof.

### Level T3 — `RUNTIME_EXECUTED`

Established facts:

- the exact source/test commit is pinned;
- a specific command ran in a described environment;
- exit status and logs or an equivalent immutable result are preserved.

This level does not itself mean success. The result must be recorded as passed, failed, error, timeout or inconclusive.

Minimum additional fields:

```yaml
test_evidence:
  level: RUNTIME_EXECUTED
  source_commit:
  runtime_or_toolchain:
  environment_identity:
  working_directory:
  command:
  selected_tests:
  started_at:
  completed_at:
  exit_code:
  stdout_stderr_or_log_ref:
  result: passed | failed | error | timeout | inconclusive
```

### Level T4 — `RUNTIME_PASSED`

Established facts:

- T3 is satisfied;
- all tests required by the frozen claim completed with the accepted success condition;
- no selected failure was omitted;
- result artifacts are bound to the exact tested source.

Minimum additional fields:

```yaml
test_evidence:
  level: RUNTIME_PASSED
  required_test_set_complete: true
  passing_result_ref:
  failures_or_skips: []
  claim_scope:
```

`RUNTIME_PASSED` is scoped to the named environment, command, commit and test set. It is not production readiness.

### Optional Level T5 — `INDEPENDENTLY_REPRODUCED`

A separate actor/context or independently provisioned environment reproduces a T4 result from the same identified source and documented procedure. This level is optional and requires its own authorization when it creates material cost or external action.

## 3. Claim rules

1. `tests exist` requires only T1.
2. `tests were reviewed` requires T2 and a stated review scope.
3. `tests ran` requires T3.
4. `tests passed` requires T4.
5. A PR, commit or generated test file does not establish T3 or T4.
6. A model's statement that it “checked” tests must specify whether the check was T1, T2, T3 or T4.
7. A runtime failure or missing import must be preserved; do not downgrade it to a formatting issue.
8. When runtime correctness is outside the frozen validation objective, absence of T3/T4 is a limitation, not automatically a blocker.
9. When runtime correctness is part of the claimed result, lack of T3/T4 blocks that claim.
10. No later static review may retroactively convert a historical run into a runtime-tested result.

## 4. V1 historical application

For `MNE-TARGET-LIFECYCLE-V1-001`:

```yaml
historical_application:
  S6:
    level: STATICALLY_INSPECTED
    runtime_executed: false
    finding: test_calls_sort_invoices_without_import
    architecture_scope_result: target_locality_passed
    runtime_success_claim: prohibited
  S7_library_and_Alpha_tests:
    level: STATICALLY_INSPECTED
    runtime_executed: false
    architecture_scope_result: documentation_and_project_local_migration_evidence_passed
    runtime_success_claim: prohibited
```

The historical synthetic branches remain unchanged.

## 5. Future runtime supplement gate

Before any runtime supplement:

- correct known import/discovery defects;
- pin the exact synthetic branch/commit/tree;
- select the runtime/toolchain and dependency versions;
- state whether the test environment itself is synthetic, local or external;
- freeze the command and selected test set;
- state write permissions and prohibited repositories;
- preserve exit code and logs;
- compare named real-repository refs if the supplement uses connected tools;
- return results for review without implying target adoption.

A runtime supplement remains separately authorized and is not required for the current Owner architecture decision.

## 6. Boundaries

This guidance does not:

- authorize test execution;
- require runtime testing for every documentation or governance validation;
- convert synthetic runtime success into production readiness;
- replace semantic, privacy, authority, migration or no-write review;
- modify candidate v0.2;
- authorize any real target.
