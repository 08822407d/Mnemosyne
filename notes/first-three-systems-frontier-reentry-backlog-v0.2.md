# First Three Systems — Frontier Re-entry and Evidence Backlog v0.2

> Current non-execution-source routing record after Owner-confirmed TLR review, V0 execution and Pro adjudication. It does not authorize V1, result ingestion, architecture acceptance or target adoption.

```yaml
backlog_id: MNE-FIRST-THREE-SYSTEMS-FRONTIER-BACKLOG-002
version: 0.2.4
created_by_task: MNEMOSYNE-209
last_updated_by_task: MNEMOSYNE-212
owner_result_ref: notes/owner-decision-results/MNE-TARGET-LIFECYCLE-OWNER-REVIEW-RESULT-001.md
candidate_ref: notes/target-agent-container-evolution-and-dependency-model-candidate-v0.2.md
validation_ref: notes/validation-designs/target-agent-container-evolution-and-dependency-model-validation-v0.2.md
validation_package_ref: notes/target-agent-lifecycle-validation-package-v0.2/README.md
V0_authorization_ref: notes/validation-run-decisions/MNE-TARGET-LIFECYCLE-V0-RUN-AUTHORIZATION-001.md
V0_adjudication_ref: notes/validation-adjudications/MNE-TARGET-LIFECYCLE-V0-ADJUDICATION-001.md
V1_decision_candidate_ref: notes/validation-run-decisions/MNE-TARGET-LIFECYCLE-V1-RUN-DECISION-CANDIDATE-001.md
V1_execution_package_ref: notes/target-agent-lifecycle-v1-execution-package-001/README.md
V1_display_name: MNE-DR-003 生命周期验证
status: priority_1_V0_valid_sentinel_pass_V1_baseline_profile_prepared_pending_Owner_confirmation_and_publication_other_priorities_preserved
execution_source: current/human-approved-spec.md
```

## Priority 1 — Target lifecycle, container, evolution and dependency responsibility

### Completed evidence

- Owner review and candidate v0.2 formalization are complete.
- Candidate v0.2, validation v0.2 and the frozen public/synthetic package are merged.
- V0 ran in `08822407d/mnemosyne-target-lifecycle-validation-002` and stopped before any substantive scenario.
- Raw V0 evidence remains in the synthetic repository at `master@e8e3296922185b4b70997c2351d6f39423f2cd4f`.
- Pro adjudication accepts V0 only as a valid surface/identity/material/permission/no-write sentinel pass.
- No candidate/package repair is required before the V1 Owner decision.

### V0 evidence boundary

```yaml
V0:
  disposition: ACCEPT_V0_AS_VALID_SENTINEL_PASS
  package_and_authorization_identity: pass
  public_synthetic_material: pass
  write_allowlist: pass
  named_real_repository_no_write_proof: pass
  S1_through_S11_started: false
  architecture_accepted: false
```

Named real-repository refs remained unchanged:

- Mnemosyne: `930b5ed0c8d1db82e46fd9439035db3f2dd20c46`;
- Meta-Agent: `1fdbd7af9437f72f7c8106714ad1e64908983fb7`.

Other real targets were prohibited but not named by full repository identity. No per-repository commit proof is claimed for them.

### Current V1 recommendation

Run one complete baseline V1 in the existing public synthetic repository, pinned to the V0 final head.

```yaml
recommended_V1:
  run_id: MNE-TARGET-LIFECYCLE-V1-001
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  pinned_base: e8e3296922185b4b70997c2351d6f39423f2cd4f
  scenario_scope:
    selected:
      - S1
      - S2
      - S3
      - S4
      - S5
      - S6
      - S7
      - S8
      - S9
      - S11
    excluded:
      - S10
  logical_profile: staged_multicell
  actual_conversations:
    - MNE-DR-003 Execute
    - MNE-DR-003 S8
    - MNE-DR-003 Review
  final_review: fresh_Pro_adjudication
  raw_output: synthetic_repository_only
  web_research_or_external_quota: prohibited
```

`MNE-DR-003 Execute` performs controller/fixture, Core, S7 and S11, prepares the isolated S8 branch, pauses, and later performs closeout after exact S8 refs return. `MNE-DR-003 S8` is the only fresh next-tier worker required. `MNE-DR-003 Review` is a separate fresh Pro adjudicator.

S8 must not receive the Execute transcript, S7 output or exact sufficient migration facts. S10 remains optional exploration and is not needed for the first baseline disposition.

### Current gate

```yaml
priority_1_gate:
  V0_Pro_adjudicated: true
  V1_decision_candidate_prepared: true
  V1_execution_package_prepared: true
  V1_owner_authorized: false
  V1_executed: false
  S10_selected: false
  V2_authorized: false
  raw_result_ingestion_authorized: false
  architecture_globally_accepted: false
  target_adoption_authorized: false
```

The next true gate is Owner acceptance or correction of:

```text
notes/validation-run-decisions/MNE-TARGET-LIFECYCLE-V1-RUN-DECISION-CANDIDATE-001.md
```

The MNEMOSYNE-212 branch must also be published and merged through one separately authorized Ready PR before its files can become the execution-time package.

### Explicit deferrals preserved

1. TLR-04 parent-side minimum-content question.
2. TLR-03 detailed universal change schema.
3. Real production concurrency automation beyond validated task contracts.
4. Final human/Agent change-document schema and synchronization method.
5. Optional proactive consumer notification/registration mechanisms.
6. Real backup providers, accounts, credentials and synchronization.

V1 may generate evidence or non-adopted amendment proposals; it may not silently close these deferrals.

## Priority 2 — Meta-Agent target-owned readiness

Preserved blockers remain target-owned. Candidate v0.2 and validation runs do not modify or activate Meta-Agent.

## Priority 3 — Language-learning professional basis

Still requires target-specific education review, privacy/retention design and product verification. No research or target work is authorized by this backlog.

## Priority 4 — Backup implementation

S11 may test synthetic backup/restore semantics only. Real implementation still requires independent locations, source identity, controlled non-authoritative synchronization, restore tests, target-specific scope and credential/privacy review.

## Priority 5 — Change documentation and record evidence

S7/S8 will test positive and negative downstream-Agent migration behavior. S9 will test practical route evidence without a brittle taxonomy. Later quantitative or external research remains optional and should be triggered only by a precise evidence question after V1.

## Platform observation — GitHub access versus ChatGPT sync

Current OpenAI documentation and V0 behavior indicate that GitHub-side repository authorization and ChatGPT-side sync selection are separate. A repository authorized by the GitHub installation may remain accessible even when it is not selected for sync. Recheck after installation-scope, repository-visibility/ownership or product changes.

## Closure rule

V0 pass is not V1 authorization. V1 execution evidence is not Pro acceptance. Pro acceptance is not Owner architecture acceptance. Architecture acceptance is not target adoption or automatic propagation. Each later gate remains separate.
