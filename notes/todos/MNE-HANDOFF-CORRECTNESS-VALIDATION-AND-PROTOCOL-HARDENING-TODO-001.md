# Mnemosyne Handoff Correctness Validation and Protocol Hardening — Detailed TODO 001

```yaml
todo_id: MNE-HANDOFF-CORRECTNESS-VALIDATION-AND-PROTOCOL-HARDENING-TODO-001
status: R0_and_preexecution_design_audits_complete_Pro_adjudicated_and_published_via_PR_303_pending_separately_gated_fixtures_execution_and_staged_implementation
created_by_task: MNEMOSYNE-233
last_updated_by_task: MNEMOSYNE-242
source: direct_Owner_instruction
execution_source: false
priority: high
current_task_execution_authorized: false
external_review_or_research_authorized: false
```

## Owner requirement

Determine whether Mnemosyne has a reliable handoff-correctness protocol; treat observed incomplete handoffs as falsifying evidence rather than preserving a design merely because it exists.

## Completed R0 evidence

```yaml
repository_audit:
  task: WORK-ULTRA-FABLE-MNE-DR-006-HANDOFF-PROTOCOL-REPOSITORY-AUDIT-001
  verdict: REPOSITORY_AUDIT_COMPLETE_READY_FOR_PRO_OWNER_REVIEW
  Pro_adjudication: MNE-HANDOFF-PROTOCOL-REPOSITORY-AUDIT-PRO-ADJUDICATION-001
  scope: repository_only_no_conversation_exports
failure_forensics:
  task: WORK-ULTRA-FABLE-MNE-DR-005-MNEMOSYNE-235-236-DUAL-FAILURE-FORENSIC-AUDIT-002
  verdict: DUAL_FAILURE_PARTIAL_CAUSE_RECOVERY_ARCHITECTURE_READY_WITH_UNKNOWNS
  Pro_adjudication: MNE-235-236-DUAL-FAILURE-FORENSIC-PRO-ADJUDICATION-001
HVAL_preexecution_design_audit:
  task: WORK-ULTRA-FABLE-MNE-DR-006-HVAL001-PREEXEC-DESIGN-AUDIT-001
  verdict: MNE_HVAL_001_DESIGN_READY_WITH_NONBLOCKING_REPAIRS
  Pro_adjudication: MNE-HVAL-001-DESIGN-PRO-ADJUDICATION-002
  accepted_design: MNE-HVAL-001-PRO-CORRECTED-VALIDATION-DESIGN-002
cross_route_root_cause: BLOCKED_PENDING_EXACT_GOD_VIEW_EXPORTS
```

## Publication of R0 evidence and HVAL Design 002

```yaml
publication:
  complete: true
  carrier_task: MNEMOSYNE-241
  PR: 303
  merged: true
  merge_commit: 3ea2b97c369837d27d0e4a65c38c252e755954b5
  post_merge_readback_task: MNEMOSYNE-242
  published:
    - repository_audit_evidence
    - HVAL_preexecution_design_audit_evidence
    - failure_forensics_evidence
    - MNEMOSYNE_235_through_239_incident_record
    - accepted_design_MNE-HVAL-001-PRO-CORRECTED-VALIDATION-DESIGN-002
  HVAL_design_002_blob: 260f9bafefc6eadeae28b2e440433399d31c2d10
  HVAL_executed: false
  HVAL_fixtures_published: false
  HO_GUIDANCE_001_resolved: false
```

Publication makes the evidence and the accepted design readable. It does not execute HVAL, publish fixtures, grant quota or resolve `HO-GUIDANCE-001`.

## Verified failure classes

- visible startup text can drift from the canonical artifact;
- merged path/blob identities can be wrong while the receiver correctly fails closed;
- report schema and rehearsal oracle can be structurally incompatible;
- executor-side path assembly can change case;
- content-transport failure without raw per-call receipts leaves the cause indeterminate;
- Windows-native full-path limits can block a valid exact-path publication and must be detected before a one-shot task starts.

## Current staged protocol direction

```yaml
guidance_loading:
  A_separate_Owner_message: retain_default_and_fallback
  C_source_selected_exact_manifest: next_additive_candidate
  B2_two_phase_startup: defer_until_validation
  E_high_impact_human_gate: defer_until_trigger_validation
  D_task_local_bundle: reject_as_default
implementation_candidates_after_validation:
  - P-04 publication receipt
  - P-05 startup transfer fidelity
  - P-06 optional source-selected guidance manifest and preserved-task echo
  - P-09b deprecate handoff-current as global route pointer
deferred:
  - generic schema/prepare/receive/oracle migration
  - execution-source amendment
  - god-view export study
```

## HVAL design status

```yaml
package: MNE-HVAL-001
accepted_design: MNE-HVAL-001-PRO-CORRECTED-VALIDATION-DESIGN-002
scenarios: 23
receiver_conversation_ceiling: 24
Pro_turn_ceiling: 6
fixture_file_ceiling: 30
evidence_file_ceiling: 60
fixture_publication_authorized: false
scenario_execution_authorized: false
quota_authorized: false
```

The design includes scenario blinding, positive manifest guidance, fabricated-report re-observation, deterministic dynamic-state timing, bounded harness writes, aggregated evidence, and per-scenario capability fields.

## Required remaining work

1. Separately decide whether to publish synthetic fixtures.
2. Separately decide scenario execution and quota.
3. Run HVAL under a repository change freeze.
4. Use results to decide P-04/P-05/P-06 and any generic schema/oracle migration.
5. Keep the god-view study privacy- and Owner-gated.

Each item above still requires its own explicit Owner decision. Publication of the audit evidence, the 235–239 incident record and HVAL Design 002 is complete through PR #303 and is no longer remaining work.

## Boundaries

This record does not authorize:

- conversation export or public storage of private material;
- command, guard or execution-source changes;
- automatic guidance loading;
- fixture publication;
- scenario execution or quota;
- G2A, A1, validation-repository writes, retry or cleanup.
