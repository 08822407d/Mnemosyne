# MNE V2-A A1 Model-Binding and Worker-Opening Order Defect 001

```yaml
defect_id: MNE-V2A-A1-MODEL-BINDING-ORDER-DEFECT-001
task_id: MNEMOSYNE-231
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
status: CONFIRMED_PRE_EXECUTION_BLOCKER
classification: validation_protocol_and_package_profile_defect
severity: material_pre_execution_blocker
architecture_candidate_defect: false
A1_runtime_failure: false
repository_side_effect: none
package_001_modified: false
package_repair_required: true
repair_form: additive_package_version
```

## 1. Affected frozen artifacts

The defect is present across the following package-001 contracts:

```text
notes/validation-run-decisions/
MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-001.md

notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/
00-owner-gates-and-surface-contract.md
07-operator-flow-and-startup-messages.md
```

Candidate 001 and the gate contract require a single controller G2A/startup message to bind all three execution conversations' Owner-authorized and operator-selected visible labels.

The operator flow separately requires:

```text
controller conversation and G2A
→ controller preflight
→ controller creates controller / Alpha / Beta branches
→ only then open Alpha and Beta worker conversations
```

## 2. Temporal unsatisfiability

At the moment the controller G2A is sent:

- the controller conversation exists, so its current operator-selected visible label can be observed or reported;
- the Alpha worker conversation does not yet exist;
- the Beta worker conversation does not yet exist;
- therefore Alpha and Beta do not yet have current operator-selected visible-label evidence.

A future intention to select a label is not evidence that the label was actually selected in a specific worker conversation.

The current package therefore creates an impossible requirement:

```text
bind Alpha/Beta actual selected labels before G2A
while opening Alpha/Beta conversations only after G2A
```

## 3. Provenance consequence

The following substitution is prohibited:

```yaml
invalid:
  planned_or_recommended_label: treated_as_operator_selected_label
```

The valid evidence objects remain separate:

```yaml
Owner_authorized_visible_label:
  evidence_class: direct_user_instruction
operator_selected_visible_label:
  evidence_class: operator_observed_or_operator_reported_for_that_specific_conversation
backend_identity:
  status: unknown_or_not_attestable
```

Neither repository recommendation, memory, response style, speed nor model self-identification may supply the worker's actual selected label.

## 4. Disposition of prior readiness review

The prior fresh-Pro execution-time review remains accepted for its independently verified findings concerning:

- source/package identity;
- A0 prerequisite;
- validation refs and branch absence;
- effect-contract completeness;
- worker and combined Git-tree oracle;
- controller output contract;
- GitHub tool-surface availability.

Its final `ready_for_Owner_G2A: true` disposition is rejected for package 001 as written because it did not reconcile the dynamic worker-label requirement with the frozen worker-opening order.

```yaml
prior_mechanical_findings: preserved
prior_G2A_readiness_boolean: superseded_by_this_defect
new_full_research_required: false
A1_rerun_required: false
```

## 5. Required correction

The correction must use staged binding:

### Controller phase

The controller G2A binds:

- controller Owner-authorized visible label;
- controller current operator-selected visible label;
- Alpha Owner-authorized visible label;
- Beta Owner-authorized visible label.

It does not claim that Alpha or Beta has already selected a model.

### Worker phase

After controller preflight passes, the controller creates the three initial branches and preserves both immutable worker task payloads before the first worker result.

At each worker's actual launch:

- the Owner-authorized label is already frozen;
- the operator observes or reports the selected label in that worker conversation;
- the worker compares the two raw strings before any repository write;
- mismatch, missing evidence or uncertainty produces `WORKER_BLOCKED_BEFORE_WRITE`.

The dynamic wrapper may add only the current selected-label receipt. It may not change task semantics, paths, blobs, branch identity, oracle or prohibitions.

## 6. Preserved scope

This defect does not reopen or change:

- fixture, base commit or tree;
- five-branch map;
- Alpha/Beta read, write, effect or authority contracts;
- worker expected blobs or trees;
- two-order combined-tree oracle;
- ten-file controller output manifest;
- no-PR, no-retry or retention rules;
- A0 accepted disposition;
- A2–A7, V2-B or V2-C authorization.

Package 001 remains immutable historical evidence. Package 002 supersedes only the model-binding timing and operator-flow fields named above.
