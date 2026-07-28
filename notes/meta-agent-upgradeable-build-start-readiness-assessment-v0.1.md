# Meta-Agent Upgradeable Build-Start Readiness Assessment v0.1

> Non-execution-source readiness assessment. It estimates the shortest responsible path to begin Meta-Agent construction while preserving future upgradeability. It does not select the Meta-Agent product-build route, create a target workspace, approve a target runtime truth source, ingest materials, write a target repository, or authorize an operational build.

```yaml
assessment_id: META-AGENT-UPGRADEABLE-BUILD-START-READINESS-001
created_by_task: MNEMOSYNE-169
assessed_at: 2026-07-28
repository_ref: master@28027d82d2dbaff72b8b966c072b87e2e04d4bf7
status: candidate_readiness_threshold
execution_source: current/human-approved-spec.md
execution_source_modified: false
Meta_Agent_product_build_selected: false
```

## 1. Executive assessment

```yaml
readiness:
  requirements_and_design_continuation:
    status: CAN_BEGIN_AFTER_EXPLICIT_ROUTE_SELECTION
  target_workspace_and_v0_1_memory_system_construction:
    status: NOT_YET_READY_REQUIRES_BUILD_START_GATE
  operational_use:
    status: NOT_YET_READY_REQUIRES_TARGET_BUILD_ACCEPTANCE
```

The key conclusion is:

> Mnemosyne does not need to complete the adaptive-explanation research, GPT Live research, cross-Agent shared-memory implementation, HO-GUIDANCE global policy, automation backlog, or all other TODOs before Meta-Agent construction begins.

To maximize future upgradeability, actual target workspace and v0.1 memory-system creation should begin **after one short Meta-Agent-specific build-start gate**, so stable IDs, authority, versions, migration mapping and rollback are present from the first target write rather than retrofitted later.

## 2. What is already sufficient

### 2.1 Mnemosyne design and governance foundation

Current Mnemosyne already provides:

- target-project intake and memory-system design templates;
- raw/evidence/candidate/decision/execution-source separation;
- repository safety preflight and one-of storage routes;
- handoff and delivery instruments;
- drift, scorecard, postmortem and regression support;
- target/Mnemosyne runtime-truth separation;
- task-local authorization and no-write boundaries;
- model/provenance caution;
- Phase A and Phase B hard-contract propagation across downstream target-project templates.

### 2.2 Meta-Agent-specific evidence already available

The repository already contains:

- a requirements-analysis alignment package;
- revised draft run-manifest package v0.2;
- a user-approved review/preparation baseline;
- a controlled no-target-write dry run with `PASS_WITH_WARNINGS`, score 89/100 and no critical blockers;
- an offline Meta-Agent memory-system design/evaluation package;
- fresh-session behavioral regressions passing all five selected cases;
- explicit evidence that no target workspace, target material, target repository write or operational installation has occurred.

### 2.3 Upgradeability foundation now available

`FIRST-TARGET-MINIMUM-UPGRADE-CONTRACT-001` is accepted as an advisory pilot. It can be attached to the first Meta-Agent design through a target-specific `minimal` or `standard` profile.

It provides candidate controls for:

- stable IDs and object lineage;
- source and authority preservation;
- design/schema/policy/delivery versions;
- migration manifests and old-to-new mappings;
- preserve/transform/recompute/retire decisions;
- validation and behavior/retrieval regression where relevant;
- previous state and rollback;
- rebuildable derived views;
- next-tier model usability and frontier escalation;
- proportionality for small Agents.

This is the main new protection against an early Meta-Agent design becoming difficult to upgrade later.

## 3. Current blockers to actual construction

The major blockers are target-specific, not global Mnemosyne incompleteness:

```yaml
current_blockers:
  explicit_Meta_Agent_product_build_route_selection: missing
  v0_1_requirements_baseline: incomplete
  target_runtime_truth_source_or_owner_rule: unresolved
  target_workspace_and_repository_role: unapproved
  safe_input_and_storage_policy_for_build: not_final_approved
  target_write_scope_and_run_manifest: unapproved
  target_specific_upgrade_contract_profile: not_instantiated
  operational_build_acceptance_criteria: not_approved
```

The existing controlled dry-run explicitly warned that requirements analysis remains incomplete and no Meta-Agent runtime truth source is approved. Those are the two strongest blockers.

## 4. Maximum-upgradeability build-start gate

Actual target workspace or v0.1 memory-system creation should wait until all **MUST** items below are completed.

### MUST-01 — Explicit product-build route selection

```yaml
required_decision:
  route: META_AGENT_PRODUCT_BUILD
  scope: requirements_and_design | design_only_workspace | bounded_v0_1_build
  relation_to_test_route: new_route_not_automatic_continuation
```

The historical Meta-Agent test route is complete for behavioral testing; product construction requires a fresh explicit selection.

### MUST-02 — v0.1 requirements baseline

Produce and approve a bounded baseline containing:

- identity, purpose and non-goals;
- general-purpose scope and software-engineering-heavy incubation distinction;
- single-Agent versus multi-Agent/team design role;
- methodology, case, feedback and evaluation needs;
- user learning-goal preservation;
- confirmed requirements;
- pending requirements;
- unknowns and unsupported assumptions;
- what may be deferred to later versions.

The baseline need not settle every future implementation detail. It must be sufficient to avoid inventing core product purpose or authority during the build.

### MUST-03 — Target runtime truth source and owner rule

Approve:

```yaml
target_authority:
  owner: user
  runtime_truth_source:
  Mnemosyne_role: design_archive_and_control_plane_not_second_runtime_truth
  evidence_and_research_role:
  conflict_precedence:
  update_and_supersession_rule:
```

A target workspace path must not silently become the target runtime truth source merely because it exists.

### MUST-04 — Workspace, repository and safe-input boundary

Decide:

- whether the first v0.1 lives under `target-projects/meta-agent/`, a dedicated external repository, or another approved location;
- whether that location is only a Mnemosyne design workspace or also the target runtime truth source;
- repository visibility and sensitivity boundary;
- permitted materials: public, synthetic, redacted, external pointer or approved private storage;
- whether any raw originals may be stored and where;
- who may write and under what task-local authorization.

### MUST-05 — Approved build/run manifest

The manifest should state:

```yaml
build_manifest:
  exact_target_and_scope:
  design_only_or_target_write:
  allowed_inputs:
  prohibited_inputs:
  files_or_roles_to_create:
  source_and_authority_map:
  target_runtime_truth_source_ref:
  user_decisions_required:
  acceptance_criteria:
  stop_conditions:
  rollback_or_revision_plan:
  no_write_or_target_write_evidence_plan:
  model_capability_split:
```

### MUST-06 — Target-specific upgrade-contract profile

Select one:

```yaml
upgrade_profile: minimal | standard | enhanced | not_applicable_with_rationale
```

For a first Meta-Agent v0.1, `standard` is the default candidate because the target is expected to be long-lived and methodology-bearing. A `minimal` profile is acceptable if the first build is deliberately narrow and disposable.

At minimum, the first target write should already know:

- which objects need stable IDs;
- current design/schema/policy/delivery versions;
- how future rename/split/merge/retire is mapped;
- what is authoritative versus derived;
- how derived summaries/indexes can be rebuilt;
- previous-state and rollback references;
- how next-tier execution escalates high-uncertainty or authority-changing work.

### MUST-07 — Open high-severity review findings checked

Before the first **operational** Meta-Agent use or broad target write:

- check whether the separately owned non-FABLE health review has produced P0/P1 or equivalent must-fix findings;
- incorporate applicable findings, or record explicit deferral and residual risk;
- do not take over that review route in this conversation.

The absence of an ingested result does not block requirements work, design work or a synthetic/design-only pilot.

## 5. Work that does not need to block Meta-Agent

```yaml
non_blockers_before_v0_1_start:
  - adaptive_explanation_Stage_A_report
  - GPT_Live_product_specific_research
  - learner_state_or_cognitive_coaching_implementation
  - cross_Agent_shared_memory_service
  - universal_HO_GUIDANCE_policy
  - full_event_sourcing
  - dual_write_or_shadow_cutover
  - RAG_or_MCP
  - automatic_indexing_or_writeback
  - optional_Meta_Agent_mechanical_no_write_proof_closure
  - completion_of_all_Mnemosyne_TODOs
```

Reasons:

- learning and GPT Live capabilities can enter later as versioned methodology modules;
- HO-GUIDANCE can use a task-local `project_only | trimmed | full | unknown_requires_decision` choice until a global policy is validated;
- shared memory and automation are later capabilities, not prerequisites for a file-based v0.1;
- the upgrade contract exists specifically so later Mnemosyne improvements can be applied through migration rather than requiring a perfect first design.

## 6. Recommended sequence and estimated repository cycles

This is an effort estimate by bounded task/PR cycle, not a calendar-time promise.

### Meta-Agent Launch Preparation Slice

```yaml
M0_requirements_and_authority_closure:
  estimated_cycles: 1_to_2
  outputs:
    - user_reviewed_v0_1_requirements_baseline
    - target_runtime_truth_source_and_owner_rule
    - confirmed_pending_unknown_unsupported_split

M1_workspace_safety_and_build_manifest:
  estimated_cycles: 1
  outputs:
    - workspace_or_repository_role_decision
    - safe_input_and_storage_policy
    - approved_build_manifest
    - upgrade_contract_profile
    - model_capability_split_and_escalation_rules

M2_v0_1_memory_system_construction_and_acceptance:
  estimated_cycles: 1_to_2
  outputs:
    - target_specific_memory_system_v0_1
    - handoff_and_current_state
    - delivery_and_rollback_records
    - upgrade_contract_pilot_record
    - initial_acceptance_or_revision
```

Earliest responsible points:

```yaml
earliest_requirements_and_design_work: after_explicit_Meta_Agent_product_build_selection

earliest_target_workspace_or_v0_1_file_creation: after_M0_and_M1_are_approved

earliest_operational_use: after_M2_acceptance_and_target_owner_disposition
```

Total preparation before first target-file construction is approximately **2–3 bounded repository cycles**. Construction and initial acceptance then require approximately **1–2 additional cycles**.

## 7. Recommended pivot point

After MNEMOSYNE-169 merges:

1. the adaptive-explanation Stage A research task is prepared and can run independently;
2. it should not block Meta-Agent;
3. the next user-selected Mnemosyne route may safely be `META_AGENT_PRODUCT_BUILD_LAUNCH_PREPARATION`;
4. first perform M0 and M1;
5. then begin the v0.1 Meta-Agent memory-system build under the advisory upgrade contract.

This is the recommended point to stop waiting for further general Mnemosyne perfection.

## 8. Why this maximizes practical upgradeability

Waiting for every open Mnemosyne question would delay real evidence indefinitely. Starting without M0/M1 would create avoidable lock-in.

The recommended middle path ensures that the initial Meta-Agent design:

- preserves original and approved requirements separately;
- has stable target authority and one runtime truth source;
- assigns stable identities before objects accumulate history;
- versions design, schema, policy and delivery from v0.1;
- records model/tool assumptions as time-sensitive rather than permanent;
- makes derived summaries and indexes replaceable;
- includes migration mapping and rollback before the first major redesign;
- allows later learner, GPT Live, shared-memory and model-routing improvements to be added as explicit modules or migrations;
- remains usable by a validated next-tier executor for bounded work, with frontier escalation for novel or high-impact decisions.

## 9. Boundaries

- This assessment does not select the Meta-Agent product-build route.
- It does not approve requirements, target truth source, workspace, material ingestion or target writes.
- It does not modify the Meta-Agent test-route status.
- It does not require the other conversation's health review to be taken over.
- It does not approve a final Meta-Agent architecture.
- It does not claim that later upgrades will be automatic or costless.
- It identifies the minimum conditions under which later upgrades should be bounded, traceable and substantially easier than rebuilding from scratch.
