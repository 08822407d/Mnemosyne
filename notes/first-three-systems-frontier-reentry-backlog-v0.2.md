# First Three Systems — Frontier Re-entry and Evidence Backlog v0.2

> Current non-execution-source routing record after Owner-confirmed TLR-01 through TLR-05, Pro/frontier formalization, and verified merge of PR #277. It supersedes v0.1 for current backlog navigation but does not close items that still require validation, real-use evidence or target-specific adoption.

```yaml
backlog_id: MNE-FIRST-THREE-SYSTEMS-FRONTIER-BACKLOG-002
version: 0.2.1
created_by_task: MNEMOSYNE-209
last_updated_by_task: MNEMOSYNE-210
supersedes_for_current_navigation: notes/first-three-systems-frontier-reentry-backlog-v0.1.md
owner_result_ref: notes/owner-decision-results/MNE-TARGET-LIFECYCLE-OWNER-REVIEW-RESULT-001.md
candidate_ref: notes/target-agent-container-evolution-and-dependency-model-candidate-v0.2.md
validation_ref: notes/validation-designs/target-agent-container-evolution-and-dependency-model-validation-v0.2.md
validation_package_ref: notes/target-agent-lifecycle-validation-package-v0.2/README.md
V0_decision_candidate_ref: notes/validation-run-decisions/MNE-TARGET-LIFECYCLE-V0-RUN-DECISION-CANDIDATE-001.md
PR_277_post_merge_verification_ref: notes/codex-task-results/MNEMOSYNE-210-pr277-post-merge-verification.md
status: priority_1_merged_V0_recommendation_prepared_pending_explicit_Owner_run_authorization_other_priorities_preserved
execution_source: current/human-approved-spec.md
```

## Priority 1 — Target lifecycle, container, evolution and dependency responsibility

### Current state

Owner review is complete and formally recorded. Candidate v0.2, validation v0.2 and the frozen public/synthetic validation package were merged through PR #277 at commit:

```text
9432a4415cefeb7c605b73a94042ba1763e15f06
```

MNEMOSYNE-210 verified the merge, expected artifact identities, absence of a required live-branch dependency, and the fact that no validation had begun. It also prepared a Pro-recommended V0-only run decision candidate so the Owner does not need to reconstruct D1 through D7 or spend another frontier turn merely to obtain a proposed profile.

Confirmed baseline:

- multiple logical Agents may share one physical repository;
- provably disjoint target-local tasks may proceed concurrently;
- shared/global/unknown work serializes, reconciles or blocks;
- task writers remain distinct from authority owners;
- upstream/meta changes enter downstream only through Owner-initiated bounded tasks and never propagate automatically;
- library Agent documents its own changes; projects migrate on demand;
- library change documentation has human-facing and downstream-Agent-facing roles plus a discoverable documentation overview;
- no exhaustive authoritative library-side consumer list is required by default;
- backups remain non-authoritative and source-identified.

### Explicit deferrals

1. **TLR-04 parent-side minimum** — current safe default is no substantive downstream content in parent/meta repositories. Revisit only after real projects or focused evidence identify a specific non-duplicative value.
2. **TLR-03 detailed change schema** — preserve original source/requirement and explicit API changes; learn additional categories/fields from practice rather than adopting a complex classifier now.

### Validation-dependent items

- exact write-set contract and mechanical non-interference proof;
- detection of shared/global/generated dependencies;
- downstream Agent comprehension and migration reliability from Agent-facing change documentation;
- synchronization/consistency between human-facing and Agent-facing change information;
- whether optional proactive notification/registration exceptions are needed;
- whether simple route-based change evidence loses important information;
- whether the no-parent-content default causes meaningful design-history loss;
- backup independence and restore proof.

### Recommended V0 profile

The current Pro recommendation is:

```yaml
recommended_V0:
  decision_candidate: MNE-TARGET-LIFECYCLE-V0-RUN-DECISION-CANDIDATE-001
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  visibility: public
  phase: V0_ONLY
  material: public_synthetic_only
  executor: current_next_tier_non_Pro_selection_recorded_verbatim_at_launch
  tools:
    - GitHub_read_write_only_on_synthetic_repository
    - mechanical_identity_path_diff_schema_and_no_write_checks
  web_or_research: prohibited
  paid_or_external_quota: false
  raw_output: synthetic_repository_only
  Mnemosyne_ingestion: separately_gated
```

This is a recommendation, not authorization. Repository creation and V0 remain blocked until the Owner explicitly confirms the decision candidate and records the exact visible execution selection at launch.

### Current gate

```yaml
priority_1_gate:
  PR_277_verified_merged: true
  merge_commit: 9432a4415cefeb7c605b73a94042ba1763e15f06
  candidate_v0_2_merged: true
  validation_v0_2_merged: true
  frozen_validation_package_merged: true
  V0_owner_decision_candidate_prepared: true
  validation_repository_created: false
  V0_authorized: false
  V1_authorized: false
  validation_executed: false
  architecture_globally_accepted: false
  target_adoption_authorized: false
```

The next true gate is explicit Owner acceptance or correction of:

```text
notes/validation-run-decisions/MNE-TARGET-LIFECYCLE-V0-RUN-DECISION-CANDIDATE-001.md
```

A V0 authorization does not authorize V1.

## Priority 2 — Meta-Agent target-owned readiness

Preserved blockers:

- functionality may be incomplete;
- initial construction has not yet received the required human review;
- first operational task scope, acceptance and stop conditions remain unknown.

Route to the Meta-Agent construction conversation. Candidate v0.2 and the V0 decision candidate do not modify or activate Meta-Agent.

## Priority 3 — Language-learning professional basis

Still needs:

- education/second-language-acquisition review of the provisional evidence model;
- practical teaching/learning feedback;
- target-owned privacy and retention design;
- later current-product verification for time metadata, voice/transcription, storage and implementation facts.

Research should be generated only when the language target has a formal repository, a sufficiently frozen design question and an Owner-selected product/surface/quota disposition.

## Priority 4 — Backup implementation

Owner direction remains strong enough for candidate design, but real implementation still needs:

- two sufficiently independent backup locations;
- controlled non-authoritative synchronization;
- exact source identity and integrity;
- restore tests;
- target-specific content scope;
- private-material, visibility, provider/account and credential review.

The synthetic S11 validation may test semantics. It does not authorize real backup configuration.

## Priority 5 — Evidence about change documentation and change records

Explicit after TLR-02/TLR-03:

- test whether human-facing and Agent-facing change documentation can remain semantically consistent;
- test whether the Agent-facing form supports accurate downstream reconstruction;
- learn which source/change fields are genuinely useful through real operation;
- consider later Pro-designed synthetic comparisons or separately authorized Pro Deep Research only when a precise evidence question exists.

Do not pre-build a universal schema or run broad research merely because this backlog exists.

## Closure rule

A backlog item closes only when:

- a canonical decision record resolves its semantic question;
- required validation/real-use evidence is reviewed;
- the Owner accepts the relevant global or target-specific conclusion;
- each affected target receives a separate adoption decision where applicable;
- the closing reference is recorded here or in a superseding backlog.

Preparation is not execution. Validation pass is not target adoption. A target adoption is not automatic propagation to other targets.
