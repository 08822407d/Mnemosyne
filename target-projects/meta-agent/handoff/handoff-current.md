---
target_project_id: meta-agent
artifact_id: META-AGENT-V0.1-HANDOFF-001
artifact_role: fresh_session_handoff
status: v0_1_constructed_pending_owner_acceptance
authority_level: non_execution_navigation
target_runtime_truth_source: false
created_by_task: MNEMOSYNE-171
delivery_version: 0.1.0
source_refs:
  - target-projects/meta-agent/current/approved-spec.md
  - target-projects/meta-agent/current/active-context.md
  - target-projects/meta-agent/authority/source-and-owner-map.md
known_limits:
  - handoff_is_not_execution_source
  - verify_latest_repository_ref_before_use
---

# Meta-Agent Handoff Current v0.1

## 1. Handoff role

This file helps a qualified fresh session recover the target state. It does not grant authority, activate Meta-Agent or replace the target truth source.

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
  effective_for_operational_use: false_pending_owner_acceptance
  Mnemosyne_is_second_target_truth_source: false
```

## 3. Current stage

```yaml
stage:
  route: META_AGENT_PRODUCT_BUILD
  milestone: M2_v0_1_seven_file_build
  state: constructed_pending_owner_acceptance
  versions:
    design: 0.1.0
    schema: 0.1.0
    policy: 0.1.0
    delivery: 0.1.0
  target_materials_ingested: false
  real_cases_recorded: false
  operational_use_authorized: false
```

## 4. Required reading order

Read each file separately and preserve its role:

1. `target-projects/meta-agent/current/approved-spec.md` — designated target truth; check activation status.
2. `target-projects/meta-agent/authority/source-and-owner-map.md` — owner, sources, material and write authority.
3. `target-projects/meta-agent/current/active-context.md` — current stage, blockers and safe next action.
4. `target-projects/meta-agent/methodology/core-methodology.md` — initial method library referenced by the spec.
5. `target-projects/meta-agent/history/decision-version-and-migration-log.md` — decisions, versions, lineage and rollback.
6. `target-projects/meta-agent/cases/case-and-feedback-ledger.md` — empty case/feedback evidence ledger.

Do not import Mnemosyne maintenance routes as Meta-Agent work. Load Mnemosyne guidance only when the current task explicitly requires it and keep it separate from target truth.

## 5. Accepted scope

- Meta-Agent is general-purpose and may design a single Agent, workflow or multi-Agent/team arrangement.
- User remains owner and final authority.
- Initial v0.1 is file-based and human-reviewed.
- Six initial method objects exist: `MA-METHOD-0001` through `MA-METHOD-0006`.
- Stable IDs, versions, migration mapping and rollback are required proportionately.
- Bounded routine work may use a validated next-tier executor; novel or authority-changing work escalates.
- No private material, real case or operational runtime is included.

## 6. Pending and deferred scope

Pending requirements remain `MA-PEND-0001` through `MA-PEND-0008`, including final product surface, dedicated repository, routing thresholds, mature evaluation, private storage, advanced model/tool routing, learner/GPT Live/shared-memory modules and automation.

Deferred from v0.1:

- RAG, MCP, indexes and auto-writeback;
- autonomous methodology changes;
- automatic cross-Agent memory;
- persistent global user/cognitive profile;
- full event sourcing, dual-write and shadow cutover;
- production-grade autonomous runtime.

## 7. Current blockers

```yaml
blockers:
  - owner_operational_acceptance_pending
  - proposed_approved_spec_not_activated
  - health_review_P0_P1_equivalent_check_or_explicit_deferral_required_before_operation
```

## 8. Prohibited actions

A receiving session must not:

- claim Meta-Agent is operational or production-ready;
- modify target truth, owner, privacy or trust boundaries without explicit authorization;
- ingest private or raw target material;
- create paths outside an approved manifest;
- add real cases or feedback without evidence and safety review;
- promote case feedback to methodology automatically;
- infer backend identity from a visible model label, latency or style;
- continue a Mnemosyne maintenance route as though it were Meta-Agent work.

## 9. Fresh-session receive procedure

1. Verify the repository and ref are current.
2. Read this handoff as navigation only.
3. Read `current/approved-spec.md` and check whether `effective_for_operational_use` is true.
4. Read the source/owner map and active context.
5. Report loaded sources, missing sources, conflicts and current blockers.
6. Stop if operational acceptance remains false or the requested action lacks task-local authorization.
7. Continue only within the exact user-approved target scope.

## 10. Exactly one safe next action

```yaml
safe_next_action:
  id: META-AGENT-SAFE-NEXT-0001
  action: owner_review_and_disposition_of_Meta_Agent_v0_1_seven_file_package
  expected_result:
    - ACCEPT_V0_1_FOR_BOUNDED_OPERATIONAL_PILOT
    - ACCEPT_WITH_LIMITATIONS
    - REQUEST_REVISION
    - REJECT_AND_ROLL_BACK
  no_automatic_continuation: true
```
