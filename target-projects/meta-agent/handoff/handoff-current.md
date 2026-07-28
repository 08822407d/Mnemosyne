---
target_project_id: meta-agent
artifact_id: META-AGENT-V0.1-HANDOFF-001
artifact_role: fresh_session_handoff
status: v0_1_constructed_return_to_dedicated_conversation_pending_receive_and_owner_acceptance
authority_level: non_execution_navigation
target_runtime_truth_source: false
created_by_task: MNEMOSYNE-171
last_updated_by_task: MNEMOSYNE-172
delivery_version: 0.1.0
source_refs:
  - handoff/meta-agent-product-build-return-to-dedicated-conversation-handoff-package.md
  - target-projects/meta-agent/current/approved-spec.md
  - target-projects/meta-agent/current/active-context.md
  - target-projects/meta-agent/authority/source-and-owner-map.md
known_limits:
  - handoff_is_not_execution_source
  - verify_latest_repository_ref_before_use
  - owner_acceptance_and_operational_activation_are_separate
---

# Meta-Agent Handoff Current v0.1

## 1. Handoff role

This target-local file helps the user's existing dedicated Meta-Agent conversation recover the current target state. It does not grant authority, activate Meta-Agent or replace the target truth source.

The detailed repository-level transfer package is:

```text
handoff/meta-agent-product-build-return-to-dedicated-conversation-handoff-package.md
```

## 2. Target identity and truth-source status

```yaml
target:
  id: meta-agent
  name: Meta-Agent
  owner: user
  purpose: general_purpose_Agent_design_and_methodology
  early_incubation: software_engineering_heavy_not_software_only

truth_source:
  designated_path: target-projects/meta-agent/current/approved-spec.md
  designated_as_sole_target_truth: true
  exists_on_master: true
  effective_for_operational_use: false_pending_owner_acceptance
  Mnemosyne_is_second_target_truth_source: false
```

## 3. Current stage and route owner

```yaml
stage:
  route: META_AGENT_PRODUCT_BUILD
  milestone: M2_merged_return_handoff
  state: constructed_pending_dedicated_conversation_receive_and_owner_acceptance
  canonical_M2_PR: 222
  canonical_M2_merge_commit: b8d75150ea2058f0dc0ca88f5666bd95b4e8592e
  versions:
    design: 0.1.0
    schema: 0.1.0
    policy: 0.1.0
    delivery: 0.1.0
  target_materials_ingested: false
  real_cases_recorded: false
  operational_use_authorized: false

route_owner_after_MNEMOSYNE_172_merge:
  Meta_Agent_product_build: existing_dedicated_Meta_Agent_construction_conversation
  Mnemosyne_self_development: current_separate_Mnemosyne_maintenance_conversation
```

## 4. Required reading order

Read each file separately and preserve its role:

1. `handoff/meta-agent-product-build-return-to-dedicated-conversation-handoff-package.md` — transfer authority, baseline and procedure.
2. `handoff/meta-agent-product-build-return-to-dedicated-conversation-startup-prompt.md` — receive-only prompt.
3. `target-projects/meta-agent/current/approved-spec.md` — designated target truth; verify it remains inactive.
4. `target-projects/meta-agent/authority/source-and-owner-map.md` — owner, sources, material and write authority.
5. `target-projects/meta-agent/current/active-context.md` — current stage, blockers and safe next action.
6. `target-projects/meta-agent/methodology/core-methodology.md` — initial proposed method library.
7. `target-projects/meta-agent/history/decision-version-and-migration-log.md` — decisions, versions, lineage and rollback.
8. `target-projects/meta-agent/cases/case-and-feedback-ledger.md` — empty case/feedback evidence ledger.
9. `current/meta-agent-product-build-status.md` and `current/first-target-minimum-upgrade-contract-status.md` — Mnemosyne-side route/pilot state.

Do not bulk-load unrelated historical Meta-Agent or Mnemosyne records unless a conflict or audit need requires them.

## 5. Accepted scope

- Meta-Agent is general-purpose and may design a single Agent, workflow or multi-Agent/team arrangement.
- User remains owner and final authority.
- Initial v0.1 is file-based and human-reviewed.
- Six initial method objects exist: `MA-METHOD-0001` through `MA-METHOD-0006`.
- Stable IDs, versions, migration mapping and rollback are required proportionately.
- Bounded routine work may use a validated next-tier executor; novel or authority-changing work escalates.
- No private material, real case or operational runtime is included.
- The existing dedicated conversation may continue only after re-anchoring to this repository state.

## 6. Pending and deferred scope

Pending requirements remain `MA-PEND-0001` through `MA-PEND-0008`, including final product surface, dedicated repository, routing thresholds, mature evaluation, private storage, advanced model/tool routing, learner/GPT Live/shared-memory modules and automation.

Deferred from v0.1:

- RAG, MCP, indexes and auto-writeback;
- autonomous methodology changes;
- automatic cross-Agent memory;
- persistent global user/cognitive profile;
- full event sourcing, dual-write and shadow cutover;
- production-grade autonomous runtime.

## 7. Upgradeability baseline

The current `standard` target-specific upgrade profile includes:

- stable requirement, decision, method, case, feedback, evaluation and migration IDs;
- design/schema/policy/delivery versions `0.1.0`;
- source and authority separation;
- breaking-change old-to-new mapping;
- preserve/transform/recompute/retire decisions;
- semantic validation and rollback;
- replaceable derived views;
- next-tier execution and frontier escalation.

It does not make upgrades automatic or costless, and real migration evidence does not yet exist.

## 8. Existing dedicated-conversation context

The earlier dedicated conversation is useful only as historical or candidate evidence until reconciled with the repository.

It must not:

- override the target spec;
- treat uncommitted prior ideas as approved;
- restart M0/M1/M2;
- reconstruct missing originals as fact.

It should surface conflicts, stale assumptions and uncommitted ideas for user review.

## 9. Current blockers

```yaml
blockers:
  - dedicated_conversation_receive_report_not_completed
  - owner_operational_acceptance_pending
  - proposed_approved_spec_not_activated
  - health_review_P0_P1_equivalent_check_or_explicit_deferral_required_before_operation
```

## 10. Prohibited actions

A receiving session must not:

- claim Meta-Agent is operational or production-ready;
- treat PR #222 merge or this handoff as owner acceptance;
- modify target truth, owner, privacy or trust boundaries without explicit authorization;
- ingest private or raw target material;
- create paths outside an approved manifest;
- add real cases or feedback without evidence and safety review;
- promote case feedback to methodology automatically;
- infer backend identity from a visible model label, latency or style;
- continue a Mnemosyne maintenance route as though it were Meta-Agent work;
- use the old dedicated-conversation context as authority.

## 11. Fresh-session or existing-conversation receive procedure

1. Verify the repository and latest `master`.
2. Read the repository-level return handoff and startup prompt.
3. Read this handoff as navigation only.
4. Read `current/approved-spec.md` and confirm `effective_for_operational_use` is false.
5. Read the source/owner map and active context.
6. Report loaded sources, missing sources, conflicts and stale prior-context assumptions.
7. Confirm no write, owner disposition or operational activation was performed.
8. Stop.
9. Load Mnemosyne guidance only if the user sends a separate task-local refresh instruction; do not import its maintenance route or treat it as target truth.
10. Continue substantive owner review only after another explicit user instruction.

## 12. Exactly one safe next action

```yaml
safe_next_action:
  id: META-AGENT-SAFE-NEXT-0002
  action: existing_dedicated_Meta_Agent_conversation_receives_and_verifies_the_return_handoff_then_stops
  startup_prompt: handoff/meta-agent-product-build-return-to-dedicated-conversation-startup-prompt.md
  no_automatic_owner_disposition: true
  no_automatic_operational_activation: true
  no_automatic_continuation: true
```
