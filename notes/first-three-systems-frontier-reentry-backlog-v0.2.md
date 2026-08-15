# First Three Systems — Frontier Re-entry and Evidence Backlog v0.2

> Current non-execution-source routing record after Owner-confirmed TLR review, PR #278 merge, and explicit Owner authorization of the recommended V0-only validation profile.

```yaml
backlog_id: MNE-FIRST-THREE-SYSTEMS-FRONTIER-BACKLOG-002
version: 0.2.3
created_by_task: MNEMOSYNE-209
last_updated_by_task: MNEMOSYNE-211
owner_result_ref: notes/owner-decision-results/MNE-TARGET-LIFECYCLE-OWNER-REVIEW-RESULT-001.md
candidate_ref: notes/target-agent-container-evolution-and-dependency-model-candidate-v0.2.md
validation_ref: notes/validation-designs/target-agent-container-evolution-and-dependency-model-validation-v0.2.md
validation_package_ref: notes/target-agent-lifecycle-validation-package-v0.2/README.md
V0_decision_candidate_ref: notes/validation-run-decisions/MNE-TARGET-LIFECYCLE-V0-RUN-DECISION-CANDIDATE-001.md
V0_authorization_ref: notes/validation-run-decisions/MNE-TARGET-LIFECYCLE-V0-RUN-AUTHORIZATION-001.md
PR_278_merge_commit: 8e1affee8776709f0673862d8b0203a25c9aaf59
PR_278_post_merge_closeout_ref: notes/codex-task-results/MNEMOSYNE-211-result.md
status: priority_1_V0_owner_authorized_execution_blocked_only_by_repository_creation_tool_other_priorities_preserved
execution_source: current/human-approved-spec.md
```

## Priority 1 — Target lifecycle, container, evolution and dependency responsibility

Owner review is complete. Candidate v0.2, validation v0.2 and the frozen validation package are merged. PR #278 also merged the Ready-PR / Owner-review / frontier-efficiency workflow repair.

The Owner has now explicitly accepted `MNE-TARGET-LIFECYCLE-V0-RUN-DECISION-CANDIDATE-001` and authorized:

- creation of `08822407d/mnemosyne-target-lifecycle-validation-002` as a public synthetic-only repository;
- writes only inside that synthetic repository for the exact V0 scope;
- `V0_ONLY` execution;
- mechanical repository/ref/path/diff/schema/hash/identity/no-write checks;
- retention of raw V0 outputs in the synthetic repository.

The Owner explicitly did **not** authorize:

- V1 or any substantive S1–S11 scenario;
- writes to Mnemosyne, Meta-Agent or real targets during V0;
- private/real target material;
- web research, Deep Research, Fable or external quota;
- raw-result ingestion into Mnemosyne;
- architecture acceptance or target adoption.

### Current V0 execution state

```yaml
priority_1_gate:
  PR_277_verified_merged: true
  PR_278_verified_merged: true
  current_master: 8e1affee8776709f0673862d8b0203a25c9aaf59
  candidate_v0_2_merged: true
  validation_v0_2_merged: true
  frozen_validation_package_merged: true
  V0_owner_authorization_recorded: true
  repository_name: 08822407d/mnemosyne-target-lifecycle-validation-002
  repository_name_exact_recheck: not_found_available_at_recheck
  repository_creation_authorized: true
  synthetic_repository_write_authorized: true
  V0_authorized: true
  V0_executed: false
  V1_authorized: false
  execution_block: BLOCKED_TOOL_CAPABILITY_REPOSITORY_CREATION_UNAVAILABLE
  substitute_store_authorized: false
  architecture_globally_accepted: false
  target_adoption_authorized: false
```

The current GitHub connector exposes repository/file/branch/PR mutations but no repository-creation mutation. Therefore V0 must not start on another store. Resume only on a surface that can create the already-authorized named repository, and record the exact visible model/mode at launch.

### Explicit deferrals preserved

1. **TLR-04 parent-side minimum** — current safe default remains no substantive downstream content in parent/meta repositories.
2. **TLR-03 detailed change schema** — preserve source/requirement and material API changes; learn finer categories/fields from practice.
3. Exact concurrency proof/write-contract mechanics.
4. Exact human/Agent change-document schema and synchronization.
5. Narrow proactive notification/registration exceptions.
6. Real backup provider/account topology and restore implementation.

### Validation-dependent items after V0

V0 is only a sentinel. If it succeeds, later separately authorized V1 is still needed for substantive evidence on:

- write-set/non-interference mechanics;
- shared/global/generated dependency detection;
- downstream Agent migration from Agent-facing change documentation;
- human-facing vs Agent-facing change-document consistency;
- route-based change evidence sufficiency;
- no-parent-content design-history tradeoffs;
- backup independence and restore semantics.

A V0 pass does not authorize V1.

## Priority 2 — Meta-Agent target-owned readiness

Preserved blockers remain target-owned. Candidate v0.2 and V0 do not modify or activate Meta-Agent.

## Priority 3 — Language-learning professional basis

Still requires target-specific professional/education review, privacy/retention design and later product verification. No research is authorized by this backlog entry.

## Priority 4 — Backup implementation

Real backup implementation still requires independent locations, controlled non-authoritative synchronization, source identity, restore tests, target-specific scope and credential/privacy review. V0 does not configure real backups.

## Priority 5 — Change documentation and record evidence

Later evidence should test Agent-facing migration sufficiency, human/Agent semantic consistency, and which change fields prove useful in practice. Do not pre-build a universal schema merely because this backlog exists.

## Closure rule

Preparation is not execution. V0 pass is not V1 authorization. Validation pass is not architecture acceptance. Architecture acceptance is not automatic target adoption or cross-target propagation.