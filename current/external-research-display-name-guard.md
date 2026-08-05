# External Research and One-Run Work Display-Name Guard

> User-approved Mnemosyne behavior guard for assigning compact, stable UI names to Deep Research, Fable-class research, and equivalent one-run external work. This file is not a standalone execution source; `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
guard_id: MNEMOSYNE-EXTERNAL-RESEARCH-DISPLAY-NAME-001
created_by_task: MNEMOSYNE-189
status: active_after_MNEMOSYNE_189_merge
execution_source: current/human-approved-spec.md
execution_source_modified: false
source_issue: 250
registry: notes/registries/project-research-display-name-registry-v0.1.md
applies_to:
  - GPT_Deep_Research
  - Fable_or_other_independent_frontier_research
  - one_run_Claude_or_ChatGPT_Project
  - one_run_external_review_validation_or_adjudication_workspace
  - future_equivalent_external_research_surfaces
```

## 1. Problem addressed

Deep Research runs, Fable-class research, one-run Projects, and similar external work remain visible in product sidebars, Project lists, task lists, or chat history. Long natural-language titles make it difficult to distinguish:

- which project owns the task;
- which numbered research unit it is;
- whether two similarly worded runs are the same task or different tasks;
- which Project/chat should be retained, archived, or returned to later.

Canonical task IDs and report titles may remain long and precise. A separate compact display name is required for UI navigation.

## 2. Required display-name form

Every in-scope task must have one stable display alias before the user is asked to create or name the external Project, chat, research task, or one-run workspace.

```text
<PROJECT_ABBR>-DR-<SEQUENCE> <SHORT_TOPIC>
```

Required fields:

```yaml
display_name:
  project_abbreviation:
  sequence:
  short_topic:
  full_value:
  canonical_task_id:
  registry_ref:
```

Rules:

1. `PROJECT_ABBR` is a stable project-specific abbreviation recorded in the registry.
2. `DR` is the shared UI category for Deep Research, independent frontier research, or an equivalent one-run research/review unit.
3. `SEQUENCE` is unique within that project and is never reassigned to a different task.
4. New projects default to a three-digit zero-padded sequence such as `001` or `002`.
5. A project with an established canonical numbering convention may preserve that width. Existing Meta-Agent IDs such as `MA-DR-08` through `MA-DR-15` are not renamed merely to add another zero.
6. `SHORT_TOPIC` should normally be one short phrase. It must not reproduce the full task title.
7. The display alias is navigation metadata, not execution source, task authority, report identity, or backend attestation.

## 3. Adopted project abbreviations

```yaml
project_abbreviations:
  Mnemosyne:
    abbreviation: MNE
    status: owner_adopted_by_MNEMOSYNE_189
  Meta_Agent:
    abbreviation: MA
    status: established_preserved
```

`MNE` is adopted instead of `MN` because it is more distinctive while remaining compact. `MNEM` is not prohibited, but it is not the adopted abbreviation for this registry.

## 4. Canonical identity remains separate

The short name does not replace:

- the canonical task or research ID;
- a repository path;
- the report's required opening identity;
- run metadata;
- provider/model/surface/effort records;
- a branch, PR, issue, or artifact ID.

Example:

```yaml
canonical_task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
display_name: MNE-DR-001 验证包审计
```

Renaming only the UI alias cannot repair a wrong-topic or wrong-task run.

## 5. Run and phase suffixes

The base alias remains stable across phases and reruns. A short suffix may be appended:

```text
MNE-DR-001 R0
MNE-DR-001 R1
MNE-DR-001 Run-02
MNE-DR-001 Review
```

Rules:

- R0/R1 are phases of one task and do not receive new DR numbers;
- a rerun keeps the same base alias unless the research question materially changes and a new canonical task is issued;
- provider, model, effort, and Research-mode labels remain separate run metadata and do not enter the stable prefix.

## 6. Operator-flow requirement

When an in-scope task is selected for execution, the dedicated operator-flow section must state the display name before the long prompt or file-selection instructions.

Minimum form:

```yaml
external_task_identity:
  display_name:
  canonical_task_id:
  project_or_chat_name_to_create:
  run_suffix_if_any:
```

The user must not be required to inspect a repository file merely to discover the short UI name.

## 7. Allocation and registry rules

1. Allocate the sequence before publishing the runnable task.
2. Check the project registry for collision before allocation.
3. Do not infer a free number from the absence of a visible UI item alone.
4. Retired, failed, superseded, or completed tasks retain their assigned sequence.
5. A canonical task and its display alias must remain linked in the registry.
6. When a project migrates to another repository, its abbreviation and issued sequence history migrate with it; the old registry becomes historical and must not remain an active allocator.
7. If the registry cannot be read or its authority is unclear, do not allocate a new number; return `DISPLAY_NAME_ALLOCATION_BLOCKED`.

## 8. Verification before delivery

```yaml
display_name_delivery_check:
  project_abbreviation_registered: true
  sequence_unique: true
  canonical_task_linked: true
  short_topic_present: true
  operator_flow_shows_name: true
  provider_or_backend_not_encoded_as_identity: true
  historical_task_IDs_not_silently_renamed: true
```

A missing display alias does not invalidate research evidence already produced, but it is a delivery defect that must be corrected before the next external run is launched.

## 9. Boundaries

This guard does not:

- authorize research, quota use, Project/chat creation, connector use, repository write, or model switching;
- rename existing canonical task IDs or reports;
- make every external chat a Deep Research task;
- establish backend identity;
- transfer project ownership or target truth;
- automatically close, archive, delete, or rename existing UI items;
- replace execution-intent, operator-flow, provenance, artifact-delivery, or repository-lineage controls.
