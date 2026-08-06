# Meta-Agent Dedicated Repository E1 Semantic Mapping Resume Taskbook v0.2

```yaml
task_id: META-AGENT-DEDICATED-REPOSITORY-MAPPING-RESUME-001
created_by_task: MNEMOSYNE-193
status: prepared_not_executed
source_inventory_prerequisite: E0_MECHANICAL_INVENTORY_COMPLETE
source_inventory_merge: PR_258
source_inventory_commit: a443940a2ff2425ebb8fc67e084fce5b7b49de58
destination_repository_write: prohibited
cutover: prohibited
```

## Purpose

Resume the Meta-Agent migration preparation after E0 mechanical Git inventory. This task performs semantic classification and Owner decision preparation. It must not repeat recursive Git enumeration.

## Required inputs

Use only:

- E0 source-tree closure manifest;
- E0 blob inventory;
- E0 preliminary preclassification;
- latest Mnemosyne master state;
- Meta-Agent authority, methodology, history and handoff records.

If source inventory is stale relative to `target-projects/meta-agent/`, stop with:

`BLOCKED_SOURCE_TREE_CHANGED_AFTER_E0`

## Required outputs

Create one Mnemosyne PR containing:

1. post-PR-258 source inventory binding receipt;
2. semantic artifact classification;
3. source-to-destination mapping options;
4. behavior guidance adoption matrix;
5. initial memory-system alignment review;
6. Owner decision package.

## Semantic classification

Every source artifact must receive:

```yaml
artifact:
  source_path:
  blob_identity:
  artifact_role:
  authority_class:
  memory_layer:
  material_class:
  migration_zone:
  disposition:
    - preserve
    - transform
    - recompute
    - historical_only
    - retire
  destination_candidate_path:
  unresolved_questions: []
```

## Migration zones

Use these categories:

```yaml
Z1_TARGET_CORE
Z2_TARGET_EVIDENCE
Z3_TARGET_CANDIDATES
Z4_TARGET_MIGRATION_CONTROL
Z5_MNEMOSYNE_BOOTSTRAP_HISTORY
Z6_HISTORICAL_OR_SUPERSEDED
```

## Behavior guidance matrix

Separate:

- adopt unchanged;
- adapt for Meta-Agent ownership;
- exclude because Mnemosyne-specific;
- defer pending Owner decision.

Do not import:

- Mnemosyne maintenance state;
- unrelated target projects;
- Fable frontier routes;
- Mnemosyne TODO/open-question state;
- future Mnemosyne guard changes automatically.

## Initial memory-system alignment

Review candidate components:

```yaml
memory_roles:
  - target_truth
  - authority
  - current_state
  - handoff
  - methodology
  - cases_feedback
  - research_evidence
  - candidates
  - migration_history

candidate_additions:
  - artifact_role_registry
  - memory_object_envelope
  - load_profiles
  - freshness_and_supersession_policy
  - deterministic_memory_index
```

Do not activate these components in Meta-Agent. This task only prepares adoption decisions.

## Stop conditions

Stop if:

- destination repository receives writes;
- target truth changes;
- E0 inventory cannot be reproduced;
- unknown material cannot be classified;
- Owner decision is required but absent.

Final status must be one of:

```yaml
PASS_TO_INITIALIZATION_DECISION
BLOCKED_OWNER_DECISION
BLOCKED_SOURCE_TREE_CHANGED_AFTER_E0
INVALID_INPUT
```
