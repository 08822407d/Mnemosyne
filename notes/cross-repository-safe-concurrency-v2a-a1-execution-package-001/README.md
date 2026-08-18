# V2-A A1 Positive Independent Pair — Exact Execution Package 001

```yaml
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-001
validation_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-STAGED-VALIDATION-001
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
stage: V2_A
selected_cells: [A1]
task_id: MNEMOSYNE-230
status: frozen_plan_not_authorized_not_executed
material_class: public_synthetic_only
```

## Purpose

This package freezes one positive independent-pair validation run. It tests whether two target-local tasks with fully disjoint read/write/effect contracts can proceed without a repository-wide serialization rule and whether both selected application orders produce the same exact final Git tree and static semantic oracle.

It does not test A2–A7, wall-clock simultaneous execution, runtime performance, connector permissions, production readiness or any real target.

## Package contents

```text
README.md
00-owner-gates-and-surface-contract.md
01-package-and-source-manifest.md
02-branch-task-and-effect-map.md
03-alpha-worker-task.md
04-beta-worker-task.md
05-controller-task-and-order-construction.md
06-mechanical-checks-and-result-template.md
07-operator-flow-and-startup-messages.md
08-package-integrity-and-non-execution-checklist.md
```

Required file count: 10.

## Controlling hierarchy

1. future exact Owner G2A/startup authorization;
2. `MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-001` at the blob named by G2A;
3. this package at the source-manifest blob named by G2A;
4. the accepted V2 design and A0 adjudication/Owner decision listed in the manifest;
5. exact validation-repository fixture and branch identities.

No newer chat summary, model self-description, historical V1 S3 result or branch-name similarity overrides these identities.

## Exact topology

```yaml
repository: 08822407d/mnemosyne-target-lifecycle-validation-002
controller_branch: v2a-a1-001-controller
alpha_branch: v2a-a1-001-alpha
beta_branch: v2a-a1-001-beta
alpha_then_beta_branch: v2a-a1-001-order-alpha-beta
beta_then_alpha_branch: v2a-a1-001-order-beta-alpha
pull_requests: prohibited
```

The Alpha and Beta branches start from the same frozen fixture commit. The order branches are controller-owned evidence branches created only after both workers finish and are independently verified.

## Evidence ceiling

The required positive result is based on:

- exact path/blob and Git-tree identities;
- explicit read/write/effect intersections;
- exact two-worker branch lineages;
- both order trees equaling the same precomputed combined tree;
- static inspection of exact source and test content;
- protected-ref and no-PR checks.

Runtime tests are not required by this package and must not be claimed unless a later separately bound product surface explicitly runs and preserves them. Hidden model/backend identity remains unknown/not attestable.

## Non-effects

Publishing this package does not:

- create any validation branch;
- execute A1;
- modify the A0 controller branch or historical evidence;
- authorize A2–A7, V2-B or V2-C;
- write Meta-Agent or a real target;
- enable Web, Deep Research, Fable, another app or external quota;
- authorize retry, package repair, PR creation, merge or branch cleanup.
