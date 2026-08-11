# Mnemosyne Runtime-Guidance Load Profile — Candidate v0.1

> Non-execution-source candidate design. It proposes a smaller always-loaded core plus task-triggered full guidance modules. It does not modify `commands/load-mnemosyne-guidance.md`, replace `current/human-approved-spec.md`, or authorize automatic routing.

```yaml
candidate_id: MNEMOSYNE-RUNTIME-GUIDANCE-LOAD-PROFILE-001
created_by_task: MNEMOSYNE-199
version: 0.1.0
status: candidate_not_adopted_not_executed
source_review: notes/runtime-guidance-utilization-review-2026-08.md
execution_source: current/human-approved-spec.md
execution_source_modified: false
loader_modified: false
```

## 1. Objective

Reduce unnecessary context, latency and instruction competition without losing critical authority, safety, escalation or user-operation rules.

The candidate separates:

- the sole execution source;
- a small default runtime core;
- detailed modules loaded only when their scope is triggered;
- navigation/current-state artifacts loaded only for an authorized local task;
- preserved cold evidence read only for a specific reconstruction/review trigger.

This is a loading architecture, not a new authority hierarchy.

## 2. Non-negotiable invariants

1. `current/human-approved-spec.md` remains the sole Mnemosyne execution source.
2. A runtime profile, loader, receipt, summary or index does not become a second execution source.
3. Missing or uncertain scope causes more relevant source reading, not silent omission.
4. A conditional module's full source must be read before performing the affected external, repository-write, merge, privacy, authority or high-impact action.
5. `current/active-context.md`, handoff, TODO, open questions and route status are not imported as the local action plan merely because guidance is refreshed.
6. Complete originals and historical records remain preserved but are read only on a task-specific trigger.
7. A target project retains its own truth source and Owner rules; this candidate does not automatically propagate to Meta-Agent or another Agent.

## 3. Candidate profiles

### 3.1 `MNE_GUIDANCE_CORE`

Default files for a substantial Mnemosyne maintenance or target-memory-design conversation:

```text
current/human-approved-spec.md
commands/load-mnemosyne-guidance.md
current/user-operation-next-step-capability-and-intent-guard.md
```

Purpose:

- recover the sole authority source;
- recover the compact behavior/precedence/trigger index;
- recover the broad user-operation, next-step, capability, research and intent rules used by most substantial work.

`README.md` is not part of the default core. Read it only when repository identity, visibility framing or navigation is needed. Current repository visibility should be verified through the available repository surface rather than inferred from README prose.

### 3.2 `MNE_GUIDANCE_ARTIFACT`

Trigger:

- downloadable artifact requested;
- long structured content is intended for transfer/archive;
- complete-response transfer semantics matter;
- same-response local artifact generation is considered.

Read:

```text
current/artifact-delivery-and-direct-generation-guard.md
```

### 3.3 `MNE_GUIDANCE_EXTERNAL_FLOW`

Trigger:

- another ChatGPT conversation, Codex task, Fable task, replay, validation, review, handoff or external Agent workflow is analyzed, prepared or launched.

Read:

```text
current/cross-conversation-execution-intent-and-operator-flow-guard.md
```

If an operator artifact is also created, load `MNE_GUIDANCE_ARTIFACT`.

### 3.4 `MNE_GUIDANCE_EXTERNAL_RESEARCH`

Trigger:

- the response asks the user to create or name a Deep Research, Fable-class or one-run external research/review workspace.

Read:

```text
current/external-research-display-name-guard.md
notes/registries/project-research-display-name-registry-v0.1.md
```

If the work is Deep Research, also load `MNE_GUIDANCE_DEEP_RESEARCH`.

### 3.5 `MNE_GUIDANCE_DEEP_RESEARCH`

Trigger:

- a Deep Research task is designed, delivered, returned, exported, archived or reviewed.

Read:

```text
current/deep-research-report-delivery-correction-guard.md
```

This specific correction controls Deep Research single-report semantics over conflicting older general complete-response wording.

### 3.6 `MNE_GUIDANCE_SOURCE_AND_RATIONALE`

Trigger:

- material user-supplied source file, conversation export, report, task original or migration input;
- important architecture, behavior, authority, methodology, schema or migration choice;
- exact-versus-normalized preservation claim;
- historical rationale backfill selected for an active review.

Read:

```text
current/source-artifact-preservation-and-design-rationale-guard.md
```

### 3.7 `MNE_GUIDANCE_CLARIFICATION`

Trigger:

- material ambiguity changes authority, privacy, architecture, trust, product goal or acceptance criteria;
- a structured Owner decision package is needed;
- next-tier interviewing or semantic escalation is considered;
- a research trigger is being adjudicated.

Read:

```text
current/frontier-planning-clarification-handoff-adjudication-guard.md
```

### 3.8 `MNE_GUIDANCE_REPOSITORY_WRITE`

Trigger:

- important GitHub/connected-repository write;
- current-state or reusable behavior record;
- checkpoint, review, validation, research interpretation or important task prompt is published.

Read:

```text
current/run-context-and-pr-provenance-guard.md
```

Repository permission and task-local authority must remain separate.

### 3.9 `MNE_GUIDANCE_BRANCH_PR`

Trigger:

- branch or pull-request creation, continuation, reconciliation or finalization.

Read:

```text
current/github-single-active-pr-lineage-guard.md
```

This profile extends `MNE_GUIDANCE_REPOSITORY_WRITE`.

### 3.10 `MNE_GUIDANCE_PR_MERGE`

Trigger:

- the response asks the user to review/merge a PR;
- branch retention may be required;
- a previous explicit retention obligation reaches its release gate.

Read:

```text
current/pr-merge-branch-disposition-guard.md
```

If branch/PR state is also being changed, load `MNE_GUIDANCE_BRANCH_PR`.

## 4. Trigger-resolution procedure

Before substantive action:

1. read `MNE_GUIDANCE_CORE`;
2. identify the current local task from the user's current instruction and authorized artifacts;
3. evaluate every module trigger;
4. load the union of all triggered modules;
5. stop the affected action if a required module cannot be read;
6. record the actual load receipt;
7. read route/current/cold material only when the local task independently requires it.

Do not infer a handoff or maintenance route merely because a matching file exists.

### Conservative uncertainty rule

When a task may trigger a module and the distinction is material, load the module. Context reduction is subordinate to authority, privacy, source integrity and safe action.

## 5. Runtime guidance receipt

Every important task should be able to record a compact receipt:

```yaml
runtime_guidance_receipt:
  receipt_id:
  repository: 08822407d/Mnemosyne
  repository_ref:
  execution_source_loaded:
  loader_loaded:
  broad_core_guard_loaded:
  detected_task_scope: []
  triggered_modules:
    - module_id:
      trigger_evidence:
      source_paths_loaded: []
  navigation_or_current_state_files_loaded: []
  cold_sources_read:
    - path_or_ref:
      trigger_reason:
  deliberately_not_loaded: []
  missing_or_stale_sources: []
  conflicts_or_precedence_applied: []
  affected_action_blocked: true | false
  limitations: []
```

The receipt does not prove perfect rule compliance. It establishes the inputs and routing basis that later review can inspect.

## 6. Source mapping and stable identity

Near-term mapping should use existing durable identities rather than introduce hundreds of new rule IDs:

- execution source path and section heading;
- guard `guard_id`;
- exact file path;
- section heading/anchor;
- Git blob or repository commit when material.

Do not retroactively assign a stable ID to every sentence before real use demonstrates that finer-grained rule identity is needed.

A future machine-generated rule index may be justified if repeated profile validation finds ambiguity at section level.

## 7. Invalidation and freshness

A receipt/profile must be refreshed when:

- `current/human-approved-spec.md` changes;
- `commands/load-mnemosyne-guidance.md` changes;
- an applicable guard changes version or scope;
- the local task changes from analysis to external launch/write/merge;
- a new privacy, authority, target or product-surface condition appears;
- a task failure indicates a missed trigger.

A profile should record the exact repository ref. A profile prepared against an old ref is evidence, not current guidance.

## 8. User-facing readability

Repository schemas may remain structured and machine-friendly. Ordinary user-facing explanations should:

- lead with concise natural-language conclusions;
- avoid large English-key YAML blocks unless the user needs to make several explicit choices or transfer machine-readable content;
- explain every decision option and consequence in ordinary language;
- avoid duplicating long repository schemas in chat;
- use a short structured block only when it improves action visibility.

This candidate does not reduce safety or omit material uncertainty merely to shorten replies.

## 9. Options considered

### Option A — Keep the current universal full-load set

Advantages:

- lowest risk of missing a narrow guard because of trigger failure;
- easiest to explain procedurally.

Disadvantages:

- context and latency grow with every new guard;
- unrelated route and narrow behavior content competes for attention;
- next-tier reliability may degrade;
- no observability of what actually mattered.

Disposition: retain as validation baseline, not recommended long-term default.

### Option B — Core plus triggered full modules

Advantages:

- substantial context reduction without bypassing the sole execution source;
- full detail remains available when applicable;
- module receipt enables review;
- compatible with current files and future model improvements.

Disadvantages:

- requires correct trigger classification;
- needs validation against the full-load baseline.

Disposition: recommended candidate.

### Option C — Load only a compiled digest and omit the full execution source

Advantages:

- potentially much smaller context.

Disadvantages:

- high risk of creating a stale or competing execution source;
- semantic equivalence is not established;
- would require stronger generation, verification and invalidation machinery.

Disposition: defer.

### Option D — Split `human-approved-spec.md` into multiple normative execution modules now

Advantages:

- may eventually improve modularity and maintainability.

Disadvantages:

- changes the execution-source architecture and conflict precedence;
- large migration and validation surface before real-use evidence;
- likely to delay actual target work.

Disposition: defer until measured burden and failures justify it.

## 10. Design rationale

```yaml
design_rationale:
  rationale_id: MNEMOSYNE-199-RATIONALE-001
  design_or_decision_ref: MNEMOSYNE-RUNTIME-GUIDANCE-LOAD-PROFILE-001
  source_conversation_task_and_artifact_refs:
    - current_maintenance_conversation_2026_08_11
    - notes/runtime-guidance-utilization-review-2026-08.md
    - current/source-artifact-preservation-and-design-rationale-guard.md
    - commands/load-mnemosyne-guidance.md
  problem_and_user_goal: make_accumulated_guidance_reliably_usable_without_loading_large_amounts_of_low_value_or_irrelevant_material
  fixed_constraints:
    - current_human_approved_spec_remains_sole_execution_source
    - preserve_cold_originals_without_routine_reading
    - do_not_propagate_automatically_to_target_projects
    - real_use_should_not_wait_for_a_perfect_compiler
  assumptions_and_unknowns:
    - full_load_context_cost_not_yet_measured
    - trigger_recall_not_yet_validated
    - next_tier_cross_provider_consistency_not_yet_measured
  alternatives_considered:
    - option: universal_full_load
      material_advantages: [low_trigger_omission_risk]
      material_disadvantages: [growing_context_precedence_and_attention_burden]
      evidence_refs: [commands/load-mnemosyne-guidance.md]
    - option: core_plus_triggered_modules
      material_advantages: [proportional_context_full_source_on_trigger_observable_receipt]
      material_disadvantages: [requires_trigger_validation]
      evidence_refs: [notes/runtime-guidance-utilization-review-2026-08.md]
    - option: compiled_digest_without_full_execution_source
      material_advantages: [small_context]
      material_disadvantages: [second_truth_and_staleness_risk]
      evidence_refs: []
  selected_option: core_plus_triggered_modules_candidate
  selection_reason: it_reduces_context_at_the_guard_layer_without_changing_the_sole_execution_source_or_deleting_source_detail
  rejected_or_deferred_options:
    - option: universal_full_load_as_permanent_default
      reason: not_scalable_as_guard_count_grows
    - option: digest_only
      reason: semantic_equivalence_and_authority_not_proven
    - option: split_execution_source_now
      reason: premature_high_impact_migration_before_real_use_measurement
  expected_effects:
    - fewer_irrelevant_files_per_task
    - clearer_precedence_and_triggering
    - better_next_tier_usability
    - auditable_loaded_guidance_receipts
  known_risks:
    - missed_module_trigger
    - stale_profile_or_ref
    - false_confidence_from_receipt_without_behavioral_compliance
  validation_or_falsification_plan: notes/runtime-guidance-profile-validation-plan-v0.1.md
  affected_existing_artifacts_or_targets:
    - commands/load-mnemosyne-guidance.md_candidate_future_change_only
    - no_current_target_project
  migration_rebuild_or_compatibility_implication: no_normative_migration_in_this_candidate
  owner_decision_ref: pending
  reviewer_and_independence_limitations:
    - authored_in_same_Mnemosyne_maintenance_conversation_that_identified_the_problem
    - no_cross_provider_challenge_yet
```

## 11. Adoption gate

This candidate may be adopted only after:

- static source mapping passes;
- trigger matrix and stop rules are complete;
- a small synthetic comparison against the current full-load baseline is reviewed;
- no critical authority, privacy, repository-write, Deep Research or merge instruction is omitted;
- the Owner chooses adopt, revise, retain-current, or defer;
- a separate authorized task updates the loader and any supporting records.

No target project inherits this candidate automatically.
