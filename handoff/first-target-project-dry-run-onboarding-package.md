# First Target-Project Dry-Run Onboarding Package

## Positioning

- Positioning: non-execution-source onboarding package.
- Purpose: design-only first target-project dry-run entry point.
- This package is not execution source.
- This package is not a target-project delivery package.
- This package does not prove a real dry-run has occurred.

## 1. Package metadata

- package_id: MNEMOSYNE-048-first-target-project-dry-run-onboarding
- version: 2026-06-22
- status: active_non_execution_source_onboarding_entry
- supersedes: `handoff/first-mnemosyne-application-test-handoff-package.md`
- design_only: true

## 2. Authority map

- Mnemosyne execution source: `current/human-approved-spec.md` is the only Mnemosyne execution source.
- Task-local user decisions: apply inside the bounded task/run unless they require later execution-source promotion, which needs separate user approval.
- Target source materials: may inform target design only when safe, user-approved, and mapped to an authority level.
- Target execution source: the target project's runtime truth source when it exists; if unknown, mark unknown instead of inventing it.
- Evidence-only research: research reports and derived views constrain assumptions but are not execution source.
- Non-execution templates/checklists: run manifest template, fresh replay protocol, minimal profile, dry-run checklist, review instruments, issue log, and result template guide review but do not create runtime truth.
- D-01-D-07 coverage map boundary: use only to understand Mnemosyne reflection/promotion coverage; it is not a target-project execution source.
- Handoff strategy / scorecard instruments: `notes/handoff-package-strategy-v0.1.md` and `notes/handoff-replay-scorecard-v0.1.md` guide package generation and maintainer review; they are not execution source and do not independently close a gate.

## 3. Exact read order

1. `current/human-approved-spec.md`
2. `handoff/first-target-project-dry-run-onboarding-package.md`
3. `notes/first-target-project-fresh-replay-protocol.md`
4. `notes/first-target-project-dry-run-manifest-template.md`
5. `notes/first-target-project-dry-run-minimal-profile.md`
6. `notes/first-target-project-dry-run-checklist.md`
7. `notes/first-target-project-dry-run-review-instruments.md`
8. `notes/memory-system-issue-log-template.md`
9. `notes/first-target-project-dry-run-result-template.md`
10. `notes/target-project-intake-form-filling-guide-v0.1.md`
11. `notes/first-target-project-intake-records/README.md`
12. `notes/first-target-project-intake-records/meta-agent/meta-agent-first-target-draft-run-manifest-package.md` (current pre-workspace draft record for maintainer/user review; not approved for real dry-run)
13. Actual approved run manifest, when one exists.
14. Target safe sources, when selected and approved.

An ordinary executor should not need to read full large template packs before starting. Use large template packs only as references when a specific design detail requires them.

Reviewer-only / package-author references:

- `notes/handoff-package-strategy-v0.1.md` for handoff package generation or tier selection.
- `notes/handoff-replay-scorecard-v0.1.md` for maintainer review after the fresh replay output is returned.

The ordinary replay executor does not need to read these two files unless a separately approved test explicitly evaluates strategy-file comprehension.

## 4. Target and scope

- First target is now Meta-Agent for draft manifest preparation only; no real dry-run is approved.
- This package is design-only.
- Do not write to any target project.
- Use safe input only: public, synthetic, or explicitly redacted material unless separately approved for the current repository visibility/use.


## 4.1 Target-project workspace boundary

- Before a real target-project dry-run, the user must approve the target workspace root and user-input storage policy.
- Default target workspace root after MNEMOSYNE-057: `target-projects/<target_project_id>/`.
- The target workspace stores project-specific input, Mnemosyne-generated intermediate work, dry-run records, delivery package, feedback, and lesson candidates.
- The target workspace is not Mnemosyne execution source and is not automatically the target runtime truth source.
- If repository visibility is public or unverified, store only public, synthetic, or explicitly redacted target material.
- If originals are unsafe for the repository or not approved, store only a redacted reference or external pointer.
- No target workspace is created until target selection, authority/source map, safety/privacy boundary, no-target-write, and run manifest are approved.
- This boundary authorizes no target repository write.

## 5. Actor permissions

- ordinary ChatGPT / ordinary Thinking conversation:
  - reads the GitHub repository;
  - analyzes, discusses, and drafts content in chat or downloadable files;
  - does not directly write repository files in this workflow;
  - must not claim a repository write occurred.
- Codex Cloud:
  - writes only files explicitly authorized by a reviewed, fresh-latest-master task;
  - must not infer permission to write target-project files.
- user:
  - selects/approves target, authority, privacy, input use, no-target-write, and manual transfers;
  - notifies conversations/tasks after manually adding files.
- target agent:
  - not used in the first dry-run unless a later separately approved stage changes this.

If platform capabilities change later, they must be reverified and updated through the normal Mnemosyne process.

## 6. Procedure

1. Preflight: confirm target, owner, bounded scope, input safety, approved run manifest, source map/authority, and stale/conflict challenge.
2. Baseline recovery: recover execution source, non-execution sources, stage, constraints, pending work, and one next action from files only.
3. Conflict test: apply source-priority review to a real stale/conflict item or synthetic `test_fixture_not_target_truth` challenge.
4. Target-tailored design: select only the target-specific memory roles/files justified by the target, not a fixed Mnemosyne-shaped schema.
5. Fresh-session handoff replay: verify a new ordinary session can resume without hidden conversation context.
6. Triage: classify failures by severity, primary cause class, and route.

## 7. Expected outputs

Future run folder structure, but do not create it now:

```text
target-projects/<target_project_id>/04-dry-runs/<dry_run_id>/
  00-run-manifest.md
  01-intake-and-design-draft.md
  02-delivery-and-handoff-draft.md
  03-result-and-postmortem.md
```

## 8. Hard stop conditions

- unsafe/private material;
- unclear authority;
- missing target facts that would be invented;
- target write requested;
- unverified automation/tool assumption;
- P0 failure.

## 9. Acceptance gate

Check result enum: `pass | fail | unknown | not_tested | not_applicable`.

Definitions: `pass` means evidence proves expected behavior; `fail` means evidence proves a violation; `unknown` means the check was attempted but evidence is insufficient or ambiguous; `not_tested` means the check was not attempted; `not_applicable` means outside the approved bounded scope with recorded rationale.

Mechanical rule: `critical_check := blocking: yes`.

- all `blocking: yes` checks are `pass` with evidence;
- fresh ordinary replay succeeds with replay verdict `PASS | FAIL | BLOCKED` kept separate from check results;
- no `unknown`, `not_tested`, or `fail` on `blocking: yes` checks;
- `not_applicable` on a blocking check prevents PASS unless the user-approved scope explicitly reclassifies that row to `blocking: no`, with rationale;
- severity describes impact and does not define criticality;
- target schema tailored;
- no real dry-run PASS claim without actual run evidence.

For the post-MNEMOSYNE-053 replay gate:

- reviewed replay verdict is `PASS`;
- all handoff critical checks are `pass`;
- normalized handoff score is at least 70;
- `quality_band: strong`, or `quality_band: usable_with_warnings` with explicit user acceptance of documented non-blocking warnings;
- the reviewed scorecard and evidence map are retained as verification evidence.

## 10. Failure logging

Use:

- `notes/memory-system-issue-log-template.md` for issue entries;
- `notes/first-target-project-dry-run-review-instruments.md` for drift, handoff, source-conflict, and triage review;
- the triage rubric severity/cause classes;
- routing rules that separate Codex small fixes, user clarification, open questions, candidates, capability checks, deferral, and target-specific design containment.

## 11. Manual-import branch

Reference only; do not copy the full inbox rules here:

- `manual-import-inbox/README.md`
- `notes/manual-import-inbox-workflow.md`
- `manual-import-inbox/BATCH-MANIFEST-template.md`

## 12. Completion statement

Producing this package does not start or pass a dry-run. The user must still select a target, approve the target workspace root or exception, approve authority/source map, safe input/user originals storage policy, no-target-write, and approve the run manifest before a real dry-run.


## MNEMOSYNE-058 user-input storage and conflict-priority notes

- Read `notes/user-input-storage-governance-v0.1.md` when deciding target user-input storage policy.
- If support instruments conflict, follow `current/human-approved-spec.md`, then the user-approved actual run manifest, then onboarding/manifest templates; record conflict instead of merging instructions.
- AI/human restatements are explanatory layer and cannot replace originals or user-approved decisions.
- Sensitive originals/raw requirements default outside Git; use redacted references or external pointers unless safe and user-approved.
- This package remains non-execution-source and does not authorize target selection, target workspace creation, target material ingestion, target repository writes, or a real dry-run.

## MNEMOSYNE-063 pre-target hardening references

Additional non-execution-source references:

- `notes/synthetic-smoke-test-result-template.md`
- `notes/manual-import-artifact-classification-v0.1.md`
- `notes/target-project-workspace-skeleton-templates-v0.1.md`

Rules for later use:

- Synthetic smoke tests do not close the real target dry-run gate and must not be reported as real dry-run PASS.
- If manual-imported PRO/DR files are used, classify full report vs summary/link stub vs prompt original vs Pro result before moving to canonical paths; use `notes/manual-import-artifact-classification-v0.1.md`.
- Before creating a target workspace later, use target workspace skeleton templates to preserve pointer-only originals and non-execution-source banners.
- Redacted excerpts require redaction manifests.
- External pointers must not leak sensitive locations, credentials, tokens, signed URLs, private absolute paths, or unapproved personal/confidential details.
- This onboarding package remains non-execution-source and does not authorize target selection, target workspace creation, target material ingestion, target repository writes, or a real dry-run.

## MNEMOSYNE-066 intake and first real dry-run evaluation instruments

Before a real dry-run, use `notes/first-target-project-intake-and-approval-forms-v0.1.md` and the run manifest approval flow. During and after a real dry-run, use `notes/first-real-target-dry-run-evaluation-framework-v0.1.md` and `notes/first-real-target-dry-run-scorecard-v0.1.md`. After a dry-run, use `notes/first-real-target-dry-run-postmortem-template.md` and `notes/mnemosyne-regression-test-record-template.md` for lessons, repairs, and regression candidates.

PASS does not authorize target repository write, target delivery acceptance, or execution-source updates.

## MNEMOSYNE-068 Meta-Agent draft-manifest preparation note

- For Meta-Agent, read `notes/first-target-project-intake-records/meta-agent/meta-agent-analysis-alignment-guard.md` before approving any real dry-run or workspace creation. The current draft package is provisional while external requirements analysis remains pending.
- First target is now Meta-Agent for draft manifest preparation only.
- Use `notes/target-project-intake-form-filling-guide-v0.1.md` for consistent target-intake completion.
- Use `notes/first-target-project-intake-records/README.md` to understand the non-execution-source pre-workspace intake-record holding area.
- Use `notes/first-target-project-intake-records/meta-agent/meta-agent-first-target-draft-run-manifest-package.md` as the current pre-workspace draft manifest package after maintainer verification.
- Still do not create target workspace, ingest materials, start a real dry-run, or write a target repository before explicit approvals.

## MNEMOSYNE-071 Meta-Agent v0.2 revised draft note

For Meta-Agent, read `notes/first-target-project-intake-records/meta-agent/meta-agent-first-target-draft-run-manifest-package-v0.2.md` and the alignment package before using the older v0.1 draft. v0.2 is still a revised draft for user review, not an approved real-dry-run manifest.


## MNEMOSYNE-073 Meta-Agent v0.2 review-only approval note

For Meta-Agent after MNEMOSYNE-073, read `notes/first-target-project-intake-records/meta-agent/meta-agent-v0.2-review-only-approval-record.md` and `notes/first-target-project-intake-records/meta-agent/meta-agent-post-v0.2-next-approval-gates.md`. v0.2 is approved only as the current review/preparation baseline, not as a real-dry-run manifest.


## MNEMOSYNE-074 Meta-Agent final manifest candidate note

For Meta-Agent after MNEMOSYNE-074, read `notes/first-target-project-intake-records/meta-agent/meta-agent-final-run-manifest-candidate-v0.1.md` and `notes/first-target-project-intake-records/meta-agent/meta-agent-final-run-manifest-candidate-review-checklist.md`. The candidate is not approved for real dry-run until the user explicitly approves it.


## MNEMOSYNE-076 Meta-Agent controlled dry-run preparation note

For Meta-Agent after MNEMOSYNE-076, read the preparation plan, evidence/no-write proof plan, and operator prompt package. They prepare a controlled no-target-write dry-run but do not approve executing it. Actual execution requires a later explicit user approval and operator no-target-write confirmation.

## MNEMOSYNE-078 Meta-Agent approved execution prompt note

For Meta-Agent after MNEMOSYNE-078, use `notes/first-target-project-intake-records/meta-agent/meta-agent-controlled-dry-run-approved-execution-prompt-v0.1.md` only in a new high-reasoning ChatGPT conversation. Do not execute it in Codex Cloud. After the result returns, use `notes/first-target-project-intake-records/meta-agent/meta-agent-controlled-dry-run-result-return-and-ingestion-preflight-v0.1.md` before any ingestion.


## MNEMOSYNE-079 Meta-Agent dry-run result ingestion note

For Meta-Agent after MNEMOSYNE-079, the first controlled no-target-write dry-run result is ingested as non-execution-source evidence under `notes/first-target-project-intake-records/meta-agent/controlled-dry-run-results/`. Review the maintainer review and no-write evidence review before using it. PASS_WITH_WARNINGS does not approve target workspace creation, target material ingestion, target repository write, operational memory-system installation, or execution-source updates.
