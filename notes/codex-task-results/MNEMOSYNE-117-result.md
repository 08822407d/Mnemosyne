# MNEMOSYNE-117 Result Record

```yaml
task_id: MNEMOSYNE-117
task_name: Reconcile merged PR 163 with the intended MNEMOSYNE-116 result
task_type: post_merge_reconciliation_and_fresh_replay_package_hardening
action_actor: ChatGPT_GitHub_app
started_from:
  base_branch: master
  base_commit: 6ded129ec7398bfe293fc8f5c6652ace816fc5f7
  PR_163:
    merged: true
    merge_commit: 6ded129ec7398bfe293fc8f5c6652ace816fc5f7
  PR_164:
    merged: false
    state: closed
branch: mnemosyne-117-reconcile-pr163-pr164
user_decision_recorded: true
user_authorization_context:
  - inspect the unexpectedly merged PR 163
  - determine how it differs from the intended PR 164 result
  - repair the repository to the intended outcome
  - state the required model, reasoning strength, and Chat versus Work mode for the five-test fresh replay
selected_reconciliation:
  retain_PR_163_as_valid_foundation: true
  reopen_or_merge_PR_164: false
  port_useful_PR_164_deltas_into_new_clean_branch: true
execution_source_modified: false
current_state_files_modified: true
handoff_commands_modified: true
handoff_files_modified_or_created: true
formal_regression_definitions_modified: false
fresh_replay_executed: false
target_workspace_created: false
target_materials_ingested: false
target_repository_written: false
operational_build_started: false
FABLE5_GREENFIELD_track_resumed_or_taken_over: false
auto_merge_authorized: false
```

## Summary

PR #163 was not unrelated feature work. It was one of two parallel MNEMOSYNE-116 implementations created from the same post-PR-162 base. It implemented the user's handoff-guidance decision, loaded the guidance command in the maintenance conversation, recorded the target-project business-conversation open question, and prepared a fresh-session five-regression replay package.

PR #164 implemented the same goal through a divergent branch with different file names and stronger operational details. Because PR #163 merged first, PR #164 correctly became conflict-prone. The user closed PR #164.

The correct repair is therefore not to revert PR #163 or reopen PR #164. MNEMOSYNE-117 retains PR #163's valid execution-source and startup-guidance work, removes live-state ambiguity, and ports the useful stronger details into a new canonical replay package v2.

## PR #163 verification

Verified facts:

- PR #163 merged into `master` with merge commit `6ded129ec7398bfe293fc8f5c6652ace816fc5f7`.
- Current `master` was identical to that merge commit when MNEMOSYNE-117 began.
- PR #163 changed 12 files and contained the approved Mnemosyne handoff guidance, operational command alignment, open-question record, replay package, startup prompt, current-status updates, and MNEMOSYNE-116 result record.
- `current/human-approved-spec.md` §15 now explicitly requires Mnemosyne-owned handoff packages to instruct receivers to perform a separate guidance refresh after receive.
- `current/handoff-guidance-open-question.md` correctly preserves the undecided target-project business-conversation question.

## Gaps found after PR #163 merge

PR #163 was directionally correct but left three repairable gaps:

1. `current/review-and-validation-status.md` still recorded MNEMOSYNE-116 repository persistence as pending even though PR #163 had merged.
2. Target-project business handoff guidance did not require a visible task-local `yes | no | unknown_requires_user_decision` value for additional Mnemosyne guidance.
3. The v1 replay package compared only the `master` SHA before and after. That was weaker than the intended repository-wide mechanical evidence because branch or PR state could change without moving `master`.

PR #164 also had useful explicit surface/model guidance and stronger branch/open-PR snapshot concepts, but it should not be merged wholesale after PR #163.

## Reconciliation applied

### Handoff guidance

Updated:

- `commands/prepare-mnemosyne-handoff.md`;
- `commands/receive-mnemosyne-handoff.md`;
- `handoff/startup-instructions.md`;
- `current/handoff-guidance-open-question.md`.

The canonical operational schema is now:

```yaml
receiver_guidance_load:
  project_guidance: required | not_applicable | unknown_requires_owner_decision
  mnemosyne_guidance: required | yes | no | unknown_requires_user_decision | not_applicable
  refresh_completed: true | false | pending | not_applicable
```

For target-project business handoffs, project guidance is mandatory. The Mnemosyne-guidance value is task-local and does not establish global precedent.

### Replay package v2

Created:

- `handoff/meta-agent-regression-fresh-session-replay-package-v2.md`.

Updated:

- `handoff/meta-agent-regression-fresh-session-replay-startup-prompt.md`;
- `current/meta-agent-test-route-status.md`;
- `current/review-and-validation-status.md`;
- the formal-regression index.

The v2 package supersedes the v1 package for future execution. It adds:

- explicit Chat-versus-Work selection;
- explicit model and reasoning recommendation;
- exact visible-model provenance requirements;
- complete accessible branch-head and open-PR snapshots with pagination status;
- a blocked result when mechanical repository-state coverage is incomplete;
- explicit PR #163 / #164 reconciliation preconditions;
- a structured v2 result schema.

The v1 package remains historical and must not be used for a new run.

## Model and surface decision

Official OpenAI sources consulted on 2026-07-13:

- `https://help.openai.com/en/articles/20001275`;
- `https://openai.com/index/gpt-5-6/`.

Decision:

```yaml
fresh_replay_execution:
  surface: Chat
  Work_mode: not_recommended_for_primary_replay
  preferred_model: GPT-5.6 Sol Pro
  reasoning: highest_available_in_Chat
  fallback_model: GPT-5.6 Sol
  fallback_reasoning: highest_available_in_Chat
  record_exact_visible_labels: true
```

Rationale:

- the test object is a fresh receiving conversation, not a long-running research or deliverable agent;
- ordinary Chat minimizes surface variance and preserves the intended conversational handoff test;
- Work is designed for longer research, analysis, and finished materials and would add planning, agentic-action, and artifact variables unrelated to the five behavioral boundaries;
- Sol Pro or the strongest available Sol reasoning is appropriate for subtle authority and evidence-layer distinctions.

## Files created

- `handoff/meta-agent-regression-fresh-session-replay-package-v2.md`
- `notes/codex-task-results/MNEMOSYNE-117-result.md`

## Files modified

- `commands/prepare-mnemosyne-handoff.md`
- `commands/receive-mnemosyne-handoff.md`
- `current/handoff-guidance-open-question.md`
- `current/meta-agent-test-route-status.md`
- `current/review-and-validation-status.md`
- `handoff/meta-agent-regression-fresh-session-replay-startup-prompt.md`
- `handoff/startup-instructions.md`
- `notes/first-target-project-intake-records/meta-agent/controlled-dry-run-results/formal-regression-records/README.md`

## Verification

- Repository visibility was verified as public before writes.
- Branch `mnemosyne-117-reconcile-pr163-pr164` was created from exact current `master@6ded129ec7398bfe293fc8f5c6652ace816fc5f7`.
- Every write explicitly targeted the reconciliation branch.
- Pre-result compare reported `ahead_by: 10`, `behind_by: 0`, with 9 changed files in the intended command, current-status, handoff, open-question, and regression-index scope.
- `current/human-approved-spec.md` is absent from the changed-file set; the valid PR #163 execution-source rule is retained without duplication.
- No official MNEMOSYNE-082/083 frozen artifact, target workspace, target material, target repository, build path, regression definition, or FABLE5-GREENFIELD file is changed.
- A final compare is required after this result record is added and before the PR is opened.

## Known limitations

- The independent fresh-session behavioral replay has not yet run.
- Complete branch/open-PR snapshot capability may not be available on every ChatGPT/GitHub configuration; when unavailable, the v2 package requires `BLOCKED`, not an unsupported no-write PASS.
- One fresh Chat replay does not establish cross-model robustness.
- The target-project business-conversation Mnemosyne-guidance question remains deliberately unresolved.

## Boundary

MNEMOSYNE-117 reconciles repository state and prepares the canonical test instrument. It does not build Meta-Agent, continue product requirements, create target artifacts, execute the replay automatically, promote regressions globally, resume FABLE5-GREENFIELD, merge any PR, or enable auto-merge.
