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
- Non-execution templates/checklists: minimal profile, dry-run checklist, review instruments, issue log, and result template guide review but do not create runtime truth.
- D-01-D-07 coverage map boundary: use only to understand Mnemosyne reflection/promotion coverage; it is not a target-project execution source.

## 3. Exact read order

1. `current/human-approved-spec.md`
2. `handoff/first-target-project-dry-run-onboarding-package.md`
3. `notes/first-target-project-dry-run-minimal-profile.md`
4. `notes/first-target-project-dry-run-checklist.md`
5. `notes/first-target-project-dry-run-review-instruments.md`
6. `notes/memory-system-issue-log-template.md`
7. `notes/first-target-project-dry-run-result-template.md`
8. Actual run manifest, when one exists.
9. Target safe sources, when selected.

An ordinary executor should not need to read full large template packs before starting. Use large template packs only as references when a specific design detail requires them.

## 4. Target and scope

- Target not selected yet.
- This package is design-only.
- Do not write to any target project.
- Use safe input only: public, synthetic, or explicitly redacted material unless separately approved for the current repository visibility/use.

## 5. Actor permissions

- Ordinary Thinking model: may read, design, check, and record dry-run artifacts inside the allowed Mnemosyne paths for a future run.
- Codex: in future tasks, may write only explicitly listed Mnemosyne files; Codex must not write target-project files unless a separate task explicitly approves that boundary.
- User: selects target, confirms authority, privacy, repository visibility/use, and approval for source materials.
- Target agent: not used in the first run.

## 6. Procedure

1. Preflight: confirm target, owner, bounded scope, input safety, source map/authority, and stale/conflict challenge.
2. Baseline recovery: recover execution source, non-execution sources, stage, constraints, pending work, and one next action from files only.
3. Conflict test: apply source-priority review to a real stale/conflict item or synthetic `test_fixture_not_target_truth` challenge.
4. Target-tailored design: select only the target-specific memory roles/files justified by the target, not a fixed Mnemosyne-shaped schema.
5. Fresh-session handoff replay: verify a new ordinary session can resume without hidden conversation context.
6. Triage: classify failures by severity, primary cause class, and route.

## 7. Expected outputs

Future run folder structure, but do not create it now:

```text
notes/target-project-dry-runs/<dry_run_id>/
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

- all critical checks pass with evidence;
- fresh ordinary replay succeeds;
- no `not_tested` critical checks;
- target schema tailored;
- no real dry-run PASS claim without actual run evidence.

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

Producing this package does not start or pass a dry-run. The user must still select a target and provide safe input.
