---
target_project_id: meta-agent
artifact_id: META-AGENT-V0.1-HANDOFF-001
artifact_role: fresh_session_handoff
status: pre_migration_preservation_checkpoint_ready
authority_level: non_execution_navigation
target_runtime_truth_source: false
last_updated_by_task: META-AGENT-PRE-MIGRATION-PRESERVATION-001
---

# Meta-Agent Handoff Current v0.1

The sole target truth remains:

```text
target-projects/meta-agent/current/approved-spec.md
```

in `08822407d/Mnemosyne` until a separate explicit Owner cutover. It remains inactive for operational use.

## Current route and repository state

```yaml
route: META_AGENT_PRODUCT_BUILD
phase: dedicated_repository_pre_migration_preservation_and_mapping_preparation
owner_disposition: ACCEPT_WITH_LIMITATIONS

source_repository:
  full_name: 08822407d/Mnemosyne
  preservation_base_master: 3fd0861e59cf795dec0d90abe588518872e8c732
  preservation_branch: meta-agent-pre-migration-preservation-001
  preservation_PR: not_created_requires_separate_authorization

destination_repository:
  full_name: 08822407d/Meta-Agent
  access_verified: true
  visibility: public
  commits: 0
  branches: []
  initialized: false
  cutover: false
```

The Owner has selected migration to the dedicated repository as the intended direction, but destination initialization, shadow copy, cutover and operational activation remain separate decisions.

## Required recovery order

Read from the preservation branch while it remains unmerged; after human merge, read from the execution-time latest `master`.

1. `target-projects/meta-agent/current/approved-spec.md` — sole target truth, inactive;
2. `target-projects/meta-agent/authority/source-and-owner-map.md`;
3. `target-projects/meta-agent/current/active-context.md`;
4. `target-projects/meta-agent/migration/pre-migration-preservation-checkpoint-2026-08-06.md`;
5. `target-projects/meta-agent/migration/destination-access-verification-2026-08-06.md`;
6. `target-projects/meta-agent/candidates/p0-static-design-conformance-mvi/README.md`;
7. `target-projects/meta-agent/candidates/p0-static-design-conformance-mvi/candidate-spec-draft-2026-08-05.md`;
8. `target-projects/meta-agent/history/decision-version-and-migration-log.md`;
9. `target-projects/meta-agent/methodology/core-methodology.md`;
10. `target-projects/meta-agent/cases/case-and-feedback-ledger.md`;
11. `target-projects/meta-agent/research/README.md` and its batch/wave manifests, formal adjudications and candidate ledgers;
12. `target-projects/meta-agent/handoff/receipts/handoff-receive-report-2026-08-05.md` as historical receive evidence;
13. `notes/migration-designs/meta-agent-dedicated-repository-migration-assessment-v0.1.md`;
14. `notes/validation-designs/target-project-dedicated-repository-migration-and-pr-validation-v0.1.md`;
15. `notes/migration-designs/meta-agent-pre-migration-readiness-assessment-2026-08-06.md`;
16. `handoff/meta-agent-dedicated-repository-pre-migration-test-package.md`.

The Mnemosyne root execution source and behavior guards apply only as temporary process/repository-safety constraints under the Meta-Agent compatibility guard; they are not Meta-Agent target truth and do not import Mnemosyne maintenance work.

## Completed work recovered by this handoff

```yaml
completed:
  - v0_1_target_truth_authority_method_case_history_and_handoff_baseline
  - Owner_ACCEPT_WITH_LIMITATIONS_disposition
  - DR_01_through_DR_05_preservation_and_synthesis
  - MA_DR_06_and_MA_DR_07_preservation_and_adjudication
  - MA_DR_08_and_MA_DR_10_through_MA_DR_15_preservation_and_adjudication
  - MA_DR_09_exact_transport_formal_intake_and_reviewer_binding
  - post_MA_DR_09_receive_only_handoff_and_guidance_refresh
  - P0_static_design_conformance_scope_selection
  - exact_P0_candidate_specification_and_acceptance_check_draft
  - destination_repository_access_and_empty_state_verification
  - Mnemosyne_PR_253_and_PR_254_migration_design_and_readiness_preparation
  - current_pre_migration_preservation_checkpoint
```

## Current research and archive state

- MA-DR-08, MA-DR-09 and MA-DR-10–15 conversations are archive-eligible.
- MA-DR-09 has final disposition `ACCEPT_WITH_CORRECTIONS_AS_NON_EXECUTION_SOURCE_EVIDENCE`; no clean rerun is required.
- Research reports and convergence records remain evidence only.
- The original MA-DR-09 pre-merge pending labels are historical and superseded for current status by the post-merge verification and report-parts manifest.

## Work in progress

```yaml
preservation:
  status: complete_on_branch_pending_review_and_merge
  branch: meta-agent-pre-migration-preservation-001

migration:
  direction_selected: true
  exact_mapping_pending: true
  recursive_source_path_blob_hash_manifest_pending: true
  destination_initialization_not_authorized: true
  shadow_copy_not_authorized: true
  destination_only_recovery_not_started: true
  cutover_not_selected: true

P0_static_candidate:
  scope_selected: true
  candidate_specification_preserved: true
  frontier_review_pending: true
  implementation_not_authorized: true
  deterministic_fixture_run_not_started: true
```

## Pending, deferred and separately owned work

### Immediate P0

- review and merge this single preservation lineage;
- freeze destination root mapping and history strategy;
- produce the exhaustive recursive source path/blob/hash manifest from a pinned post-merge source commit;
- prepare and obtain Owner authorization for a minimal non-authoritative destination initialization commit;
- perform later shadow migration through one separately authorized branch and Draft PR;
- validate destination-only fresh recovery, behavior/authority equivalence, rollback and no-dual-writer invariants;
- prepare explicit cutover decision package.

### Product P0/P1

- frontier-review and, if accepted for experiment, freeze the static conformance candidate specification;
- separately authorize and run the public/synthetic offline prototype;
- review research-derived candidate method bundles without automatic promotion;
- define minimum active-route capability claims and proportional assurance profiles;
- reconcile the separately owned non-FABLE health-review dependency before pilot or activation.

### Deferred or prohibited

- actual Tier-0/1/2 run without separate Owner authorization;
- private material;
- real external-write pilot;
- automatic methodology promotion;
- operational activation;
- simultaneous live target truth or dual writers in Mnemosyne and the destination.

## Stale and superseded artifacts

```yaml
historical_only:
  - old_receive_only_active_context_and_handoff_status
  - original_MA_DR_09_pre_merge_pending_labels
  - early_superseded_research_evidence_branches
  - incomplete_failed_research_transport_fragments
```

Their existence and dispositions are recorded in the preservation checkpoint. They must not be promoted into the migration source as canonical content.

## Exactly one safe next action

```yaml
safe_next_action:
  current:
    action: review_the_single_preservation_branch
    branch: meta-agent-pre-migration-preservation-001
    PR_creation: requires_separate_explicit_authorization

  after_merge:
    action: freeze_exact_migration_mapping_and_prepare_destination_initialization_Owner_decision

  destination_write_now: false
  target_truth_cutover_now: false
  prototype_or_pilot_now: false
```
