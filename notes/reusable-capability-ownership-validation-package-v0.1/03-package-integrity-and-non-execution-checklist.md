# Package Integrity and Non-Execution Checklist

```yaml
package_id: MNE-REUSABLE-CAPABILITY-OWNERSHIP-VALIDATION-PACKAGE-001
checklist_id: MNE-RCO-PACKAGE-INTEGRITY-001
task_id: MNEMOSYNE-225
current_disposition: PREPARED_NOT_SELECTED_NOT_EXECUTED
```

## A. Source identities

Before publication or any later run preparation, verify:

```yaml
candidate:
  path: notes/reusable-agent-capability-ownership-and-lifecycle-model-candidate-v0.1.md
  expected_blob: accb13ccb57677d316f5f94ef58f7939ad69521b
Owner_decision:
  path: notes/owner-decision-results/MNE-REUSABLE-CAPABILITY-OWNERSHIP-OWNER-DECISION-001.md
  expected_blob: e75fa69cbbaa206e480a889ff3eb1302a6780d80
catalogue_reference:
  path: notes/reusable-agent-capability-catalog-v0.2.md
  role: background_only_not_mutated_test_object
first_three_selection_reference:
  path: notes/first-three-system-capability-selection-v0.3.md
  role: confirmed_domain_shape_only_not_target_construction
```

Any candidate or Owner-decision blob drift requires semantic revalidation before reusing this package.

## B. Package file inventory

Expected package files:

```text
README.md
01-synthetic-code-library-target-and-scenarios.md
02-checks-and-result-template.md
03-package-integrity-and-non-execution-checklist.md
```

Controlling external files:

```text
notes/validation-designs/reusable-capability-ownership-and-lifecycle-bounded-validation-v0.1.md
notes/owner-decision-candidates/MNE-REUSABLE-CAPABILITY-OWNERSHIP-VALIDATION-DISPOSITION-CANDIDATE-001.md
current/reusable-agent-capability-ownership-research-status.md
```

No startup message, controller task, repository manifest or run authorization is part of v0.1. Their absence is intentional because the execution profile is not selected.

## C. Synthetic namespace checks

- All mutable test capability IDs begin with `SCAP-`.
- No `SCAP-*` identity is represented as a real catalogue entry.
- No active `ACAP-*` entry is edited or simulated as if its current accepted text changed.
- `SYNTH-CODE-LIBRARY-ALPHA` has no real repository mapping.
- No actual business project, customer, learner, credential, API or private dependency appears.

## D. Non-execution checks

At publication time all must remain true:

```yaml
validation_repository_selected: false
validation_repository_created: false
controller_branch_created: false
worker_branch_created: false
validation_execution_started: false
Meta_Agent_modified: false
real_target_modified: false
real_target_repository_read: false
execution_source_modified_by_validation_design: false
external_quota_used: false
Web_or_Deep_Research_used_for_validation: false
Fable_run_started: false
automatic_candidate_update: false
```

The separate user-approved reply-format guard may be published in the same task, but it is not validation execution and does not authorize any target action.

## E. Cross-route independence check

At task start, another conversation owned the F2/V2 repair branch:

```text
mnemosyne-224-repair-v2a-sentinel-publication-freshness
```

Before PR creation, compare the latest visible head and open PR state. The F1 package may proceed only if:

- changed paths do not overlap;
- no F2/V2 change modifies the F1 candidate, F1 Owner decision or the new next-step guard;
- no shared generated index, task registry or execution-source dependency creates a semantic conflict;
- the F1 branch integrates or revalidates the latest `master` when needed;
- only one immediate merge target is presented to the Owner.

If the other route publishes first, rebase/merge the new `master` only after exact-path and semantic revalidation. If it opens an active PR, defer this task's PR publication unless the single-active-PR guard and Owner coordination permit otherwise.

## F. Semantic review checklist

- The design tests F1 ownership/lifecycle semantics rather than rebuilding Target Lifecycle or F2/V2.
- The synthetic code-library domain is an example, not a target-construction authorization.
- Future real construction remains assigned to Meta-Agent and the target repository.
- Target-local authority and derived-view non-authority are explicit in every cell.
- Compatible and breaking revisions are not inferred from version syntax alone.
- Split/merge/retire relations do not force target adoption.
- C5 tests stale-view failure rather than assuming derived-index correctness.
- C6 can reject or simplify the schema based on burden.
- A validation pass does not imply production readiness or universal adoption.
- Design, exact run-profile preparation, execution, adjudication and target adoption remain separate gates.

## G. Publication disposition

Publication may be recommended only when:

- all expected paths exist;
- the branch changed-path set matches the task allowlist;
- latest-master and concurrent-route checks are current;
- semantic review passes;
- no validation execution occurred;
- the PR is Ready rather than Draft only if no content-changing decision remains for this preparation scope.

Merge publishes preparation and the behavior guard only. It does not select any Owner option or run.
