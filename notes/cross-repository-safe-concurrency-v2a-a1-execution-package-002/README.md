# V2-A A1 Positive Independent Pair — Additive Execution Package 002

```yaml
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-002
validation_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-STAGED-VALIDATION-001
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
stage: V2_A
selected_cells: [A1]
task_id: MNEMOSYNE-231
status: additive_repair_not_authorized_not_executed
material_class: public_synthetic_only
```

## Purpose

Package 002 repairs one pre-execution temporal/provenance defect in package 001:

```text
package 001 required Alpha/Beta actual operator-selected labels in controller G2A,
but opened the Alpha/Beta conversations only after that G2A.
```

Package 002 introduces staged model binding:

- controller actual selection is bound at controller G2A/startup;
- Alpha/Beta Owner-authorized labels are bound at controller G2A;
- each worker's actual selection is bound only when that worker conversation is opened;
- each worker verifies exact label equality before any repository write.

## Additive precedence

Package 001 remains immutable historical evidence.

Package 002 supersedes package 001 only for:

- controller G2A model-label fields;
- Alpha/Beta `operator_selected_visible_label` timing;
- worker-opening and startup flow;
- result-receipt interpretation for staged model binding.

Every other package-001 field remains controlling, including:

- fixture and validation refs;
- five-branch map;
- Alpha/Beta task, read, write, effect and authority contracts;
- expected blobs and Git trees;
- two-order oracle;
- ten-file controller output paths;
- no-PR, no-retry and retention rules;
- evidence ceilings and fresh-Pro adjudication requirement.

## Package contents

```text
README.md
00-delta-precedence-and-defect-contract.md
01-package-and-source-manifest.md
02-staged-model-binding-contract.md
03-revised-operator-flow-and-startup-messages.md
04-package-integrity-and-non-execution-checklist.md
```

Required file count: 6.

## Controlling hierarchy

1. future exact Owner controller G2A/startup authorization;
2. `MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-002` at the blob named by G2A;
3. this package at the source-manifest blob named by G2A;
4. package 001 at its frozen candidate/manifest identities for inherited fields;
5. accepted F2/V2/A0 sources listed in the manifest;
6. exact validation-repository refs and Git object identities.

No chat summary or planned worker selection may substitute for current worker-conversation selection evidence.

## Non-effects

Publishing package 002 does not:

- issue A1 G2A;
- create or modify a validation branch;
- execute controller or worker tasks;
- modify package 001;
- authorize A2–A7, V2-B or V2-C;
- write Meta-Agent or a real target;
- enable Web, Deep Research, Fable, another app or external quota;
- authorize retry, package/fixture repair, PR creation in validation, merge or cleanup.
