
# Mnemosyne post-PR303 AI-onboarding handoff package 001

```yaml
package_id: MNE-POST-PR303-AI-ONBOARDING-HANDOFF-001
package_role: route_specific_non_execution_source_handoff
source_closeout_task: MNEMOSYNE-242
transferred_task: MNEMOSYNE-243
transferred_task_role: review_and_implement_non_execution_source_AI_onboarding_package
G2A_issued: false
A1_execution_authorized: false
HVAL_fixture_publication_authorized: false
HVAL_execution_authorized: false
validation_repository_write_authorized: false
```

## Received state

- PR #303 merged the 91-path F2/G2A/handoff/HVAL publication.
- Corrected G2A template publication and post-merge readback are complete.
- No G2A has been issued and A1 has not started.
- HVAL Design 002 is published but fixture publication, scenario execution and quota remain separately gated.
- MNEMOSYNE-242 closes stale route metadata and publishes the onboarding candidates.
- `handoff/handoff-current.md` is a deprecated compatibility pointer and does not select this task.

## Minimum evidence

Read:

1. `current/human-approved-spec.md`;
2. `commands/load-mnemosyne-guidance.md` only in the separate guidance-refresh phase;
3. `notes/codex-task-results/MNEMOSYNE-242-post-merge-closeout.md`;
4. `current/fable5-cross-repository-safe-concurrency-research-status.md`;
5. `notes/ai-onboarding-candidates/MNE-AI-ONBOARDING-PACKAGE-DESIGN-001.md`;
6. `notes/ai-onboarding-candidates/MNEMOSYNE-243-AI-ONBOARDING-WORK-ORDER.md`;
7. the candidate archive and its internal manifest only when implementing the onboarding package.

Do not read cold raw originals by default.

## Transferred task

Review and implement `MNEMOSYNE-243`:

- add the repository-native AI onboarding package;
- preserve `current/human-approved-spec.md` as the only execution source;
- do not add root `CLAUDE.md` or `AGENTS.md` without a separately approved spec change;
- validate Claude Web/Fable read-only analysis, local Claude Code maintenance, and unauthorized takeover blocking;
- create a Ready PR and do not merge.

## Receiver guidance load

```yaml
receiver_guidance_load:
  project_guidance: not_applicable
  mnemosyne_guidance: required
  refresh_completed: false
  phase_order:
    - receive_report
    - stop
    - separate_Mnemosyne_guidance_refresh
    - confirm_transferred_task_preserved
    - explicit_Owner_continuation_authorization
```

The execution source remains `current/human-approved-spec.md`. Guidance refresh applies
behavior constraints without replacing the transferred task.

## Receive sequence

1. Receive this exact package and return a compact receive report.
2. Stop.
3. Owner separately requests Mnemosyne guidance refresh.
4. Preserve the transferred task during guidance loading.
5. Continue only after explicit Owner authorization.

## Branch retention

```yaml
release_notice:
  branch: mnemosyne-235-f2-g2a-and-handoff-audit-closeout
  observed_absent_at_MNEMOSYNE_242: true
  no_user_action_required: true
  unique_unpreserved_work: false
active_retention:
  branch: mnemosyne-240-preservation-capsule
  retain: true
  reason: exact outer capsule and manifest remain unique PR_303 provenance
  release_gate: immutable canonical substitute or explicit Owner archival decision
```

## Exclusions

No G2A, A1, HVAL execution, validation-repository write, conversation export, god-view study, branch deletion, unrelated maintenance route, target-project write or automatic follow-on.
