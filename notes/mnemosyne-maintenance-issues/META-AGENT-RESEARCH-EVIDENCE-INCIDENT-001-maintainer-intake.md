---
intake_id: META-AGENT-RESEARCH-EVIDENCE-INCIDENT-001-MAINTAINER-INTAKE
artifact_role: cross_conversation_read_only_incident_analysis_intake
status: ready_after_repair_PR_merge
owner_route: separate_Mnemosyne_maintenance_conversation
execution_source: false
target_runtime_truth_source: false
created_by_task: META-AGENT-RESEARCH-EVIDENCE-REPAIR-003
---

# Mnemosyne Maintainer Intake — Meta-Agent Research-Evidence Incident

## Operation for the receiving conversation

Read the following independently from current `master` after the repair PR is merged:

1. `notes/mnemosyne-maintenance-issues/META-AGENT-RESEARCH-EVIDENCE-INCIDENT-001.md`
2. `notes/codex-task-results/META-AGENT-RESEARCH-EVIDENCE-REPAIR-003-result.md`
3. `notes/codex-task-results/META-AGENT-RESEARCH-EVIDENCE-REPAIR-003-pr-finalization.md`
4. `target-projects/meta-agent/research/meta/manifest.yaml`
5. `current/github-single-active-pr-lineage-guard.md`
6. `current/run-context-and-pr-provenance-guard.md`
7. `current/artifact-delivery-and-direct-generation-guard.md`
8. `commands/load-mnemosyne-guidance.md`
9. `current/human-approved-spec.md`

## First response contract

Return a read-only receipt and analysis plan. Do not immediately modify the repository.

The first substantive analysis should contain:

```yaml
incident_adjudication:
  verified_facts:
  unsupported_or_overstated_claims:
  direct_causes:
  contributing_factors:
  controls_already_present_but_not_followed:
  genuinely_missing_controls:
  severity:
  residual_risk:

control_matrix:
  existing_controls:
  missing_or_ambiguous_controls:
  proposed_minimal_repairs:
  controls_rejected_as_excessive:

validation_plan:
  synthetic_cases:
  expected_fail_closed_behavior:
  PR_creation_and_reread_test:
  manifest_remote_integrity_test:
  parallel_branch_staleness_test:
  sandbox_link_attestation_test:
```

## Scope boundaries

The receiving conversation must not:

- treat this intake as execution source;
- take over Meta-Agent product design or Owner disposition;
- modify `target-projects/meta-agent/current/approved-spec.md`;
- delete historical failed branches before evidence review;
- infer hidden model/backend identity;
- assume every proposed control must be adopted;
- modify Mnemosyne execution source before explicit user adjudication.

## Decision questions

The maintainer should distinguish:

1. existing guidance that was adequate but violated;
2. guidance that was too implicit or hard to execute;
3. missing connector-/PR-specific attestation;
4. excessive controls that would create more process burden than risk reduction;
5. controls that should be validated before adoption.

## Expected next gate

After the read-only analysis, present the user with:

- one recommended minimal repair set;
- alternatives and tradeoffs;
- exact files that would change;
- whether execution-source change is needed;
- a bounded validation package;
- explicit separation from the Meta-Agent route.
