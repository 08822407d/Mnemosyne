# First Target Project Intake Records

## Positioning

- Non-execution-source pre-workspace holding area.
- This folder records first-target selection/intake artifacts before an approved target workspace exists.
- It is not Mnemosyne execution source.
- It is not a target workspace.
- It must not contain raw target materials, secrets, credentials, private source, unredacted personal/confidential data, or customer/confidential material.
- Once a target workspace is explicitly approved and created, relevant safe records may be copied/migrated to `target-projects/<target_project_id>/00-project-meta/` or another approved target-local path.
- Storing an intake record here does not authorize real dry-run, target workspace creation, target material ingestion, or target repository write.

## Current records

- `meta-agent/`: Meta-Agent was selected as a real/semi-real Mnemosyne test target. No workspace has been created, no target materials have been ingested, no target repository has been written, and no operational Meta-Agent build is authorized.

## Meta-Agent alignment guard and current revised draft

- `meta-agent/meta-agent-analysis-alignment-guard.md` records the Meta-Agent analysis alignment boundary.
- `meta-agent/meta-agent-requirements-analysis-handoff-intake-alignment-package.md` is the ingested external alignment package.
- `meta-agent/meta-agent-draft-manifest-revision-record-2026-07-01.md` records the v0.2 revision decision.
- `meta-agent/meta-agent-first-target-draft-run-manifest-package-v0.2.md` is the current revised draft for user review, not approved for real dry-run.
- `meta-agent/meta-agent-v0.2-review-only-approval-record.md` records the v0.2 review-only approval.
- `meta-agent/meta-agent-post-v0.2-next-approval-gates.md` lists the remaining post-v0.2 approval gates.
- `meta-agent/meta-agent-post-v0.2-next-gate-decision-record.md` records the user-provided post-v0.2 next gate decision.
- `meta-agent/meta-agent-final-run-manifest-candidate-v0.1.md` is the current final run manifest candidate for user review only.
- `meta-agent/meta-agent-final-run-manifest-candidate-review-checklist.md` is the review checklist for the final run manifest candidate.
- `meta-agent/meta-agent-first-target-draft-run-manifest-package.md` remains preserved as the v0.1 draft.
- Do not use v0.2 as completed requirements analysis, approved design specification, operational memory-system build plan, or approved real dry-run manifest.

Meta-Agent v0.2 is approved as the current review/preparation baseline only. This does not approve real dry-run, workspace creation, material ingestion, target repository write, operational memory-system installation, or execution-source update.

Meta-Agent final run manifest candidate v0.1 is the current candidate for user review only. It is not approved for real dry-run and does not create target workspace, ingest materials, or write target repository.

## MNEMOSYNE-076 Meta-Agent preparation package

- `meta-agent/meta-agent-final-manifest-candidate-approval-for-preparation-record.md`
- `meta-agent/meta-agent-controlled-dry-run-preparation-plan-v0.1.md`
- `meta-agent/meta-agent-controlled-dry-run-evidence-and-no-write-proof-plan-v0.1.md`
- `meta-agent/meta-agent-controlled-dry-run-operator-prompt-package-v0.1.md`

Meta-Agent final manifest candidate is approved for controlled no-target-write dry-run preparation only. MNEMOSYNE-078 later approved actual controlled dry-run execution for a separate high-reasoning ChatGPT conversation only; Codex Cloud execution is not approved. No target workspace/material/target-write is authorized.

## MNEMOSYNE-078 Meta-Agent approved execution package

- `meta-agent/meta-agent-actual-controlled-dry-run-execution-approval-record.md`
- `meta-agent/meta-agent-controlled-dry-run-approved-execution-record-v0.1.md`
- `meta-agent/meta-agent-controlled-dry-run-approved-execution-prompt-v0.1.md`
- `meta-agent/meta-agent-controlled-dry-run-result-return-and-ingestion-preflight-v0.1.md`

Meta-Agent actual controlled dry-run execution is approved for a separate high-reasoning ChatGPT conversation only; Codex Cloud execution is not approved. No target workspace/material/target-write is authorized.

## MNEMOSYNE-079 Meta-Agent controlled dry-run result ingestion

- `meta-agent/controlled-dry-run-results/README.md`
- `meta-agent/controlled-dry-run-results/META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001-result.md`
- `meta-agent/controlled-dry-run-results/META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001-maintainer-review.md`
- `meta-agent/meta-agent-controlled-dry-run-approval-chain-clarification-v0.1.md`

The returned Meta-Agent controlled no-target-write dry-run result is accepted as non-execution-source target-specific evidence with `PASS_WITH_WARNINGS`, score `89/100`, and no critical blockers. This acceptance does not approve production-ready status, target delivery, target workspace creation, target material ingestion, target repository write, operational memory-system installation, or Mnemosyne execution-source update.

## MNEMOSYNE-081 pre-handoff stabilization planning

- `meta-agent/meta-agent-post-079-pre-handoff-stabilization-roadmap-v0.1.md`
- `meta-agent/controlled-dry-run-results/META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001-regression-candidate-triage-v0.1.md`

MNEMOSYNE-081 adds pre-handoff stabilization planning and regression-candidate triage only. It does not close the phase, formalize regression tests, create workspace/material phase, or generate the final handoff package.

## MNEMOSYNE-082 phase closure and baseline freeze

- `meta-agent/meta-agent-post-079-phase-closure-decision-record.md`
- `meta-agent/meta-agent-post-079-baseline-freeze-for-handoff-v0.1.md`

MNEMOSYNE-082 closes the current Meta-Agent controlled dry-run evidence phase for handoff preparation only. The PASS_WITH_WARNINGS dry-run result is accepted as the current non-execution-source evidence baseline, and high-risk follow-ups are deferred until after handoff. MNEMOSYNE-082 does not create the handoff package, formalize regression tests, create a target workspace, ingest target materials, write a target repository, install an operational memory system, or modify Mnemosyne execution source.

## MNEMOSYNE-083 official handoff artifacts

- `../../handoff/meta-agent-post-079-phase-closure-handoff-package.md`: official Meta-Agent phase-closure handoff package created by MNEMOSYNE-083.
- `../../handoff/meta-agent-next-conversation-startup-prompt.md`: official next-conversation startup prompt created by MNEMOSYNE-083.

These artifacts supersede local/sandbox handoff drafts. They do not approve target workspace creation, target material ingestion, target repository write, operational build, regression formalization, or execution-source update.

## MNEMOSYNE-115 post-handoff test-route resumption

- `meta-agent/meta-agent-post-handoff-test-route-resumption-and-next-step-decision.md` records the current user's decision to resume the route under the verified test-only interpretation.
- `meta-agent/controlled-dry-run-results/formal-regression-records/` stores the first formalized regression batch: `REG-META-DRYRUN-001`, `002`, `004`, `005`, and `007`.
- The five definitions passed a current-repository definition-level static replay. This is not an independent fresh-session behavioral replay.
- `REG-META-DRYRUN-003` remains conditional on a future explicitly approved material phase; `006` remains deferred until more real target feedback exists.

MNEMOSYNE-115 does not continue Meta-Agent product requirements, create a target workspace, ingest materials, write a target repository, start an operational build, modify the execution source, or promote target-specific tests into global rules.
