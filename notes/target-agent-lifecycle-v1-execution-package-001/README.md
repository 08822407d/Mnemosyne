# Target-Lifecycle V1 Baseline — Staged Multi-Cell Execution Package 001

> Run-specific orchestration supplement for the frozen candidate/validation/package after V0. It does not amend scenario semantics, authorize V1, create branches in the synthetic repository, execute a cell, ingest results into Mnemosyne or accept the architecture.

```yaml
execution_package_id: MNE-TARGET-LIFECYCLE-V1-EXECUTION-PACKAGE-001
version: 0.1.0
task_id: MNEMOSYNE-212
status: prepared_not_selected_not_executed
source_V0_adjudication: notes/validation-adjudications/MNE-TARGET-LIFECYCLE-V0-ADJUDICATION-001.md
source_V1_decision_candidate: notes/validation-run-decisions/MNE-TARGET-LIFECYCLE-V1-RUN-DECISION-CANDIDATE-001.md
source_candidate: notes/target-agent-container-evolution-and-dependency-model-candidate-v0.2.md
source_validation: notes/validation-designs/target-agent-container-evolution-and-dependency-model-validation-v0.2.md
source_frozen_package: notes/target-agent-lifecycle-validation-package-v0.2/README.md
source_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
source_V0_final_head: e8e3296922185b4b70997c2351d6f39423f2cd4f
proposed_V1_run_id: MNE-TARGET-LIFECYCLE-V1-001
material_class: public_synthetic_only
V1_authorized: false
V1_executed: false
S10_selected: false
V2_authorized: false
```

## Purpose

The frozen v0.2 package defines scenario semantics and acceptance rules but leaves execution-time orchestration to a later Owner decision. This supplement freezes one concrete, low-contamination topology for the complete baseline V1:

- all baseline-critical scenarios S1–S9 and S11;
- no exploratory S10;
- one canonical branch per repository-writing task;
- a mandatory fresh-context S8 negative cell;
- exact blob plus commit identity for every output;
- final no-write comparison and fresh Pro adjudication.

This package is operational scaffolding only. If it conflicts with candidate v0.2 or the frozen validation package, execution must stop and return `V1_PROTOCOL_PROFILE_CONFLICT` for Pro review. The supplement may not silently override the frozen source.

## File map

```text
notes/target-agent-lifecycle-v1-execution-package-001/
├── README.md
├── 00-controller-fixture-and-branch-contract.md
├── 01-core-cell-s1-s6-s9.md
├── 02-positive-documentation-cell-s7.md
├── 03-fresh-negative-documentation-cell-s8.md
├── 04-backup-restore-cell-s11.md
├── 05-mechanical-closeout-and-return.md
├── 06-startup-messages.md
└── 07-integrity-checklist.md
```

## Selected run topology

```text
Owner V1 authorization
  ↓
Controller / Fixture Cell
  ↓
Core Cell — S1, S2, S3, S4, S5, S6, S9
  ↓
Positive Documentation Cell — S7
  ↓
Fresh Negative Documentation Cell — S8
  ↓
Backup / Restore Cell — S11
  ↓
Mechanical Closeout
  ↓
Fresh Pro Adjudication
  ↓
Owner architecture decision
```

Cells may be launched in a different order only when the dependency and contamination rules remain satisfied. In particular:

- controller/fixture must complete first;
- S7 library output must precede the S7 Alpha migration segment;
- S8 must branch from its isolated prepared input and must not receive S7 sufficient facts;
- S11 requires a pinned source target state;
- mechanical closeout occurs after every selected cell has stopped;
- final Pro adjudication occurs in a fresh conversation that did not execute a V1 cell.

## Fixed scenario scope

```yaml
selected:
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
not_selected:
  - S10
```

S10 remains available for a later separate exploratory authorization. Its exclusion does not prevent a complete baseline disposition because it is non-baseline in the frozen package.

## Repository and branch model

All V1 writes occur only in:

```text
08822407d/mnemosyne-target-lifecycle-validation-002
```

V1 pins:

```text
master@e8e3296922185b4b70997c2351d6f39423f2cd4f
```

The controller allocates exact branches from pinned commits. Recommended branch names are defined in `00-controller-fixture-and-branch-contract.md`. No V1 scenario PR is required or authorized by this package.

V0 files under:

```text
runs/MNE-TARGET-LIFECYCLE-V0-001/
```

must not be edited, replaced or deleted.

V1 controller/result files use:

```text
runs/MNE-TARGET-LIFECYCLE-V1-001/
```

Scenario code and task evidence live on their exact task branches and are referenced by immutable commit/tree/blob identities in the controller result bundle.

## Model and context model

The frozen execution cells are `NEXT_TIER_SUFFICIENT_CANDIDATE`. The current recommendation, if still visible and available at launch, is the user-reported option:

```text
gpt-5.6 sol extra high
```

Every cell records the actual visible selection and reasoning setting verbatim. A UI label does not attest the served backend.

Mandatory context separation:

- S8 uses a new ChatGPT conversation;
- S8 receives only the exact files/branch permitted by `03-fresh-negative-documentation-cell-s8.md`;
- S8 must not receive S7 output, the sufficient Agent-facing guide or a summary of its migration facts;
- final semantic adjudication uses another fresh Pro conversation.

Other cells may use separate conversations as provided in the startup messages. The controller and final mechanical closeout may share a bounded controller conversation if the exact run ledger remains reconstructable.

## Authority and safety boundary

This package does not authorize:

- V1 or any repository write;
- S10 or V2;
- a PR in the synthetic repository;
- writes to Mnemosyne, Meta-Agent or any real target;
- private/real material;
- web research, Deep Research, Fable, other connected apps or external quota;
- candidate or validation-package amendment;
- raw-result ingestion into Mnemosyne;
- architecture acceptance or target adoption.

A later Owner authorization must name this execution package and exact scenario scope.

## Evidence requirements

Each writing task must preserve:

```yaml
task_evidence:
  task_id:
  scenario_id:
  exact_input_blob_or_commit_refs: []
  authorization_ref:
  canonical_branch:
  base_commit:
  declared_write_set: []
  actual_changed_paths: []
  output_files:
    - path:
      blob_sha:
      creation_or_update_commit_sha:
  mechanical_check_refs: []
  incidents_and_retries: []
  provisional_disposition:
```

The controller must never replace an exact identity with only a narrative summary.

## Stop conditions

Stop the affected cell or the whole run when:

- V1 Owner authorization is absent or does not match the package;
- the repository or pinned V0 head differs;
- a required package file or identity is missing;
- a cell is about to write outside its exact branch/write set;
- private or real-target material appears;
- S8 contamination cannot be ruled out;
- a deferred TLR-03/TLR-04 rule would need to be invented;
- output blob/commit identity cannot be preserved;
- no-write proof for the named real repositories cannot be established;
- a critical failure contaminates dependent scenarios;
- candidate/package semantics would need revision during execution.

## Return route

V1 execution ends with a complete bundle in the synthetic repository and a visible decision-relevant response. The bundle returns to a **fresh Pro conversation** for semantic adjudication. That adjudication may recommend pass, bounded amendment, protocol revision, rerun, rejection or further Owner review, but cannot adopt the architecture into a real target.

## Current execution intent

```yaml
execution_intent:
  response_role: ANALYSIS_AND_PREPARATION
  task_id: MNE-TARGET-LIFECYCLE-V1-001
  execution_disposition: READY_NOT_SELECTED
  current_required_user_action: confirm_or_correct_the_V1_decision_candidate_after_MNEMOSYNE_212_is_merged
  external_execution_or_quota_authorized: false
```
