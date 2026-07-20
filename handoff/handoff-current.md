# Handoff Current

> Non-execution-source high-signal handoff view. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
latest_updated_by_task: MNEMOSYNE-140
handoff_status: non_FABLE_comprehensive_health_review_handoff_prepared
repository: 08822407d/Mnemosyne
prepared_from_master: 3cf6e5116a360c3f131ad4dfd472a819300ba461
selected_next_route: bounded_non_FABLE_comprehensive_Mnemosyne_health_review
package_id: MNEMOSYNE-NON-FABLE-COMPREHENSIVE-HEALTH-REVIEW-HANDOFF-001
package_path: handoff/mnemosyne-non-fable-comprehensive-health-review-handoff-package.md
startup_prompt_path: handoff/mnemosyne-non-fable-comprehensive-health-review-startup-prompt.md
FABLE5_work_in_scope: false
repository_write_authorized_for_receiver_review: false
```

## Selected continuation

The user has explicitly selected a previously unfinished large maintenance task: a bounded, read-only, non-FABLE comprehensive Mnemosyne health review.

The new conversation must use the repository-backed package and startup prompt above. It must not infer the task from old chat context, Project memory, `current/todo.md`, or historical handoff wording.

## Required receive sequence

```yaml
receiver_guidance_load:
  project_guidance: not_applicable
  mnemosyne_guidance: required
  ordered_operations:
    - receive_authorized_handoff_package
    - execute_Load_Mnemosyne_guidance_as_separate_operation
    - continue_received_task_under_refreshed_constraints
```

The first new-conversation message must receive the package and stop after the `mnemosyne_handoff_receive` report. The user will then send `加载 MNEMOSYNE 约束指导` separately.

## Current completed state

```yaml
completed_routes:
  artifact_delivery_repair:
    validation: PASS
    issues_170_171: closed_completed
    mainline: complete
  Meta_Agent_test_only_route:
    behavioral_cases: PASS_all_five
    behavioral_objective: complete
    additional_ordinary_Chat_replay_required: false
    mechanical_no_write_proof: BLOCKED_optional_future
    automatic_continuation: false
  post_interruption_wayfinding:
    task: MNEMOSYNE-139
    PR_190: merged
    merge_commit: 3cf6e5116a360c3f131ad4dfd472a819300ba461
```

Do not repeat these completed routes merely because historical records remain available.

## Current execution source

- `current/human-approved-spec.md` is the only execution source.
- This handoff view, the package, startup prompt, current status files, task-result records, research, and historical artifacts are non-execution-source evidence.
- When a non-execution-source record conflicts with the execution source, follow the execution source and record the conflict.

## Current reference order

For this selected handoff, read:

1. `commands/receive-mnemosyne-handoff.md`;
2. `handoff/mnemosyne-non-fable-comprehensive-health-review-handoff-package.md`;
3. the minimum evidence set defined by the package;
4. `commands/load-mnemosyne-guidance.md` only in the separate guidance-refresh operation.

The package defines the review scope, exclusions, deliverable, and safe next action.

## Review boundaries

The receiving review is read-only. It does not authorize:

- repository file, branch, commit, PR, Issue, comment, label, workflow, automation, or setting changes;
- execution-source modification;
- target workspace creation, material ingestion, target-repository access/write, or operational build;
- observer-assisted mechanical proof or a §19 exception;
- regression promotion;
- rerunning completed Meta-Agent or artifact-delivery campaigns;
- FABLE5 review, independent design, Greenfield, comparison, task generation, or result storage.

FABLE5 remains owned by its separate dedicated conversation.

## Source-conversation disposition

After the MNEMOSYNE-140 handoff PR merges, the source conversation may retire. No post-merge status-only PR is required. The new conversation becomes the owner of the transferred read-only health-review task after successful receive and separate guidance refresh.