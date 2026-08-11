# Target-Local Repository Operating Model — Candidate v0.1

> Non-execution-source design for conducting Mnemosyne/Meta-Agent target work primarily in each target’s own repository while keeping only bounded reusable/evidence records in the meta-system repositories. It does not create a target repository, authorize cross-repository writes, activate Meta-Agent, or change any existing truth source.

```yaml
candidate_id: MNEMOSYNE-TARGET-LOCAL-REPOSITORY-OPERATING-MODEL-001
task_id: MNEMOSYNE-200
version: 0.1.0
status: candidate_not_adopted_not_validated_generally
source_evidence:
  - Meta_Agent_dedicated_repository_migration_and_no_dual_writer_result
  - current_conversation_owner_requirements_2026_08_11
execution_source_modified: false
Meta_Agent_modified: false
target_repository_write_authorized: false
```

## 1. Problem

Co-locating several target projects inside Mnemosyne created unnecessary coupling:

- unrelated project conversations competed for one repository write lineage;
- task-local authorization had to distinguish many target paths inside the same repository;
- concurrent work risked stale state, overlapping PRs and accidental cross-project edits;
- business Agents could be tempted to read Mnemosyne construction material that was irrelevant to their runtime;
- Mnemosyne risked becoming both design archive and target truth source.

Meta-Agent’s dedicated-repository migration demonstrated that a conversation can work across repositories and that a target can recover from its destination repository with a single active writer. That evidence is meaningful but scoped to the migration; it is not yet a general validation of all future cross-repository design/build workflows.

## 2. Core rule

For a real target Agent or system:

> **The target repository or approved target store owns target truth, target-specific implementation and current operational state. Mnemosyne and Meta-Agent may retain only bounded generic design, provenance, delivery, feedback and impact records; neither remains a competing target writer.**

## 3. Repository roles

### 3.1 Target repository or target store

Candidate contents:

- sole target execution/truth source;
- target-specific requirements and owner decisions;
- selected capability record and target adaptations;
- target prompts, instructions, Skills or provider adapters;
- current state and handoff;
- target memory schema and data-management rules;
- business-domain memory and implementation artifacts;
- tests, evaluations, issue/postmortem records and migrations;
- target-local privacy, access and write rules.

The target repository should not depend on live draft files in Mnemosyne or Meta-Agent for ordinary operation.

### 3.2 Mnemosyne repository

Candidate retained records:

- reusable persistent-memory and Agent-operating capability definitions;
- target memory-system design/delivery manifests or safe summaries;
- source/evidence pointers and preservation receipts allowed by material policy;
- target capability selection reference and version;
- memory-system evaluation/postmortem findings relevant to Mnemosyne improvement;
- target impact and migration candidates when an upstream memory capability changes;
- generalized lessons only after portability review and owner approval.

Mnemosyne should not retain:

- the target’s live business truth;
- private source or complete personal conversations in public Git;
- duplicate current target state that can drift;
- an active target writer path after cutover.

### 3.3 Meta-Agent repository

Candidate retained records:

- accepted general Agent-design methodology;
- target case/feedback records at the approved sensitivity and abstraction level;
- capability-selection/design rationale used to build an Agent;
- candidate methodology changes derived from reviewed cases;
- provider-neutral packaging/design patterns;
- impact candidates when a Meta-Agent method change may affect designed Agents.

Meta-Agent should not retain:

- the target’s sole runtime truth;
- the target’s complete business memory by default;
- automatic authority to rewrite a target after methodology changes;
- a second copy of all Mnemosyne evidence or all target files.

## 4. Primary-write rule for each bounded task

Every repository-writing task should declare one **primary write repository**.

```yaml
cross_repository_task_context:
  task_id:
  purpose:
  primary_write:
    repository:
    branch_or_ref:
    exact_paths: []
    truth_effect:
    task_authorization_ref:
  secondary_actions:
    - repository:
      action: read | bounded_evidence_write | result_link | none
      exact_paths: []
      task_authorization_ref:
      order:
  prohibited_repositories_or_paths: []
  no_dual_writer_statement:
  result_and_rollback_refs:
```

Default behavior:

1. design/build work that changes a target uses the target repository as primary writer;
2. a Mnemosyne or Meta-Agent evidence update is a separate secondary action with its own exact authorization;
3. a secondary evidence write cannot silently change target truth or common methodology;
4. if one repository write depends on the committed identity from another, order the writes and stop if the first result cannot be verified;
5. use immutable commit/path references rather than keeping a live branch solely for cross-repository pointers when practical.

## 5. Concurrency model

The old single-repository bottleneck should not become a universal “only one project conversation may work at a time” rule.

### Safe candidate concurrency

Different target projects may proceed concurrently when:

- each has a different primary repository and target truth;
- neither task writes the same shared common-methodology files;
- each task has independent branch/PR lineage and authorization;
- no task depends on an uncommitted result from another;
- shared provider quota or human review capacity is accounted for separately.

### Serialization still required

Serialize or explicitly reconcile when:

- two tasks write Mnemosyne’s reusable capability catalogue or execution/behavior guidance;
- two tasks write Meta-Agent’s accepted methodology or current target truth;
- one task changes a shared schema/version used by another active target task;
- a target migration or cutover changes the authoritative writer;
- a common capability update creates unresolved impact on several targets.

The unit of serialization should be the shared truth object or repository write lineage, not every conversation in the entire ecosystem.

## 6. Target bootstrap and cutover

Candidate sequence:

1. **Intake** — preserve source requirements, owner, sensitivity and target purpose.
2. **Repository/store decision** — select target repository/root and visibility; do not request private originals before storage is approved.
3. **Minimum target truth** — create the smallest target-owned authority, current-state, handoff and memory files.
4. **Capability selection** — record the catalogue capabilities selected/adapted/deferred.
5. **Provider packaging** — instantiate prompts, instructions, Skills or tool configuration separately from portable capability semantics.
6. **Destination-only recovery** — a fresh qualified session must recover target identity, truth, current state and boundaries using only approved target inputs.
7. **No-dual-writer check** — remove or freeze any live-looking bootstrap target truth elsewhere.
8. **Bounded real use** — begin selected tasks with feedback, stop and rollback conditions.

A repository cutover or file creation does not by itself authorize operational use.

## 7. Records retained by the meta-systems

### Minimum Mnemosyne target index candidate

```yaml
mnemosyne_target_index_entry:
  target_id:
  target_repository_or_store:
  target_truth_ref:
  current_delivery_version:
  selected_capability_record_ref:
  memory_system_design_and_delivery_refs: []
  latest_evaluation_or_postmortem_refs: []
  upstream_impact_status:
  sensitivity_summary:
  active_writer_repository:
  last_verified_at:
```

### Minimum Meta-Agent case pointer candidate

```yaml
meta_agent_case_pointer:
  case_id:
  target_id:
  safe_target_or_external_refs: []
  design_problem:
  selected_agent_arrangement:
  selected_capability_record_ref:
  outcome_and_feedback_refs: []
  target_specific_lessons: []
  candidate_general_lessons: []
  promotion_status:
  privacy_limitations: []
```

These are pointers/summary records, not duplicated target truth.

## 8. Upstream change and target impact

When Mnemosyne or Meta-Agent changes a reusable capability/method:

1. identify targets whose selection records reference the old capability/method/version;
2. classify the effect as no impact, future-behavior only, review recommended, derived-view rebuild, schema/data migration, completed-work re-evaluation or authority/privacy reapproval;
3. create a target-specific change candidate;
4. require the target owner/current authority to decide adoption;
5. validate and migrate in the target repository;
6. record compatibility and rollback;
7. update the meta-system impact record without becoming the target writer.

Automatic propagation is explicitly deferred.

## 9. Bounded validation needed

A small public/synthetic validation should establish whether one conversation can safely:

- read Mnemosyne or Meta-Agent generic design inputs;
- create or update a target-only candidate package in a separate target repository;
- write a bounded evidence/result pointer back to one meta repository only when separately authorized;
- preserve exact repository/action order and no-dual-writer semantics;
- recover the target in a fresh conversation without reading meta-system history;
- run concurrent work on two different target repositories without a global repository lock.

The Meta-Agent migration is prior evidence, not a substitute for this exact operating-model validation.

## 10. Immediate application to the first two real needs

### Business-function code library

- primary target repository: to be selected by the user;
- target truth, code, tests, business rules and reuse metadata remain there;
- Mnemosyne retains memory-system design/evaluation references;
- Meta-Agent retains safe Agent-design case/method feedback;
- private work source remains outside public Git unless explicitly approved.

### Language teacher/practice Agent

- primary target repository or approved private store: to be selected;
- target teaching policy, learner evidence, plan and handoff remain target-local;
- complete personal conversations default to private cold storage;
- Mnemosyne retains only approved memory-system design/evaluation pointers;
- Meta-Agent retains only safe abstracted design feedback.

## 11. Boundaries

This candidate does not:

- authorize any target repository creation or write;
- choose public versus private storage;
- permit private source or personal conversations in public Git;
- validate arbitrary cross-repository concurrency;
- replace task-local repository action contexts;
- make Mnemosyne or Meta-Agent a shared runtime database;
- automatically update targets after common capability changes;
- change the existing Meta-Agent no-dual-writer state.

## 12. Design rationale

The selected model uses target-local truth with bounded meta-system pointers. Keeping every target inside Mnemosyne reduced initial setup friction but imposed global coordination and context burden. Duplicating target truth in all three repositories would be worse. Target-local authority preserves independent work and makes cross-project concurrency possible, while bounded pointers retain enough lineage for memory-system and methodology improvement.
