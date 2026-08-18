# MNE Cross-Repository Safe-Concurrency V2-A A1 Package 002 — Owner Preparation Decision 001

```yaml
decision_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-002-PREPARATION-OWNER-DECISION-001
task_id: MNEMOSYNE-231
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
decision_status: OWNER_CONFIRMED_REPAIR_PREPARATION_ONLY
source_instruction: Owner_current_conversation_direct_instruction
recorded_at: 2026-08-18
execution_source_modified: false
```

## Owner authorization

The Owner authorizes this task to:

- record `MNE-V2A-A1-MODEL-BINDING-ORDER-DEFECT-001`;
- prepare `MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-002`;
- prepare additive `MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-002`;
- repair only the timing and provenance contract for:
  - controller G2A model binding;
  - Alpha/Beta `operator_selected_visible_label` binding;
  - worker-conversation opening and startup order;
- preserve package 001 unchanged as historical evidence;
- update the current F2 route state;
- create one Ready PR in `08822407d/Mnemosyne`.

## Frozen scope that must not change

The repair must preserve without semantic alteration:

```yaml
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
validation_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
fixture_commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
branch_map:
  - v2a-a1-001-controller
  - v2a-a1-001-alpha
  - v2a-a1-001-beta
  - v2a-a1-001-order-alpha-beta
  - v2a-a1-001-order-beta-alpha
Alpha_write_and_read_effect_contract: unchanged
Beta_write_and_read_effect_contract: unchanged
worker_expected_blobs_and_trees: unchanged
order_oracle: unchanged
controller_output_manifest: unchanged_10_files
no_PR_rule: unchanged
no_retry_rule: unchanged
retention_rule: unchanged
```

## Explicit exclusions

This authorization does not permit:

- A1 execution or G2A issuance;
- creation, movement, modification or deletion of any validation branch;
- any write to the validation repository;
- modification of package 001 or candidate 001;
- A2–A7, V2-B or V2-C;
- Meta-Agent or real-target write/adoption;
- Web, Deep Research, Fable, another app, private material or external quota;
- package/fixture repair during execution;
- retry, reset, force-push, cleanup, merge or auto-merge.

The authorization expires with MNEMOSYNE-231 and is not precedent for later execution.
