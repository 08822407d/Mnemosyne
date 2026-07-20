# Mnemosyne Non-FABLE Comprehensive Health Review Handoff Package

```yaml
package_id: MNEMOSYNE-NON-FABLE-COMPREHENSIVE-HEALTH-REVIEW-HANDOFF-001
created_by_task: MNEMOSYNE-140
package_status: non_execution_source_transfer_artifact
intended_receiver_action: receive_mnemosyne_handoff
repository: 08822407d/Mnemosyne
prepared_from: master@3cf6e5116a360c3f131ad4dfd472a819300ba461
current_execution_source: current/human-approved-spec.md
transferred_local_task_id: MNEMOSYNE-NON-FABLE-COMPREHENSIVE-HEALTH-REVIEW-001
transferred_local_task_type: read_only_comprehensive_maintenance_health_review
source_conversation_status_after_handoff: handoff_sender_waiting_for_PR_merge_then_retired
FABLE5_work_in_scope: false
repository_write_authorized_for_receiver_review: false
```

## 1. Purpose

The source maintenance conversation has become too long for reliable browser use. This package transfers the next selected non-FABLE maintenance task to a fresh conversation without relying on chat history or model memory as repository truth.

The selected next task is the previously unfinished large **ordinary comprehensive Mnemosyne health review**, now bounded to non-FABLE maintenance only. The review is read-only. It must identify current repository-health findings and propose a repair bundle, but it must not modify the repository.

This package is not execution source. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

## 2. Receiver guidance sequence

```yaml
receiver_guidance_load:
  project_guidance: not_applicable
  mnemosyne_guidance: required
  ordered_operations:
    - receive_authorized_handoff_package
    - execute_Load_Mnemosyne_guidance_as_separate_operation
    - continue_received_task_under_refreshed_constraints
```

The receiver must keep handoff receive and guidance refresh separate.

1. First receive this package and output the required `mnemosyne_handoff_receive` YAML report.
2. Stop.
3. The user will then send `加载 MNEMOSYNE 约束指导` as a separate message.
4. After guidance refresh, preserve this package's transferred task and begin the read-only review.

## 3. Completed source-conversation work

The following current maintenance sequences are complete and must not be repeated:

```yaml
completed:
  artifact_delivery_repair:
    guard_implemented: true
    fresh_behavior_validation: PASS
    issues_170_171: closed_completed
    PR_188: merged
    PR_189: merged
    route_status: complete
  post_interruption_wayfinding:
    task: MNEMOSYNE-139
    PR_190: merged
    merge_commit: 3cf6e5116a360c3f131ad4dfd472a819300ba461
    Meta_Agent_behavioral_test_only_objective: complete
    additional_ordinary_Chat_replay_required: false
    mechanical_no_write_proof: BLOCKED_optional_future
    automatic_Meta_Agent_continuation: false
```

The Meta-Agent mechanical proof is not the selected next task. It remains an optional future observer-assisted route requiring separate authorization and reliable external or local Git evidence.

## 4. Transferred local task

```yaml
transferred_task:
  id: MNEMOSYNE-NON-FABLE-COMPREHENSIVE-HEALTH-REVIEW-001
  objective: perform_a_bounded_read_only_comprehensive_health_review_of_current_Mnemosyne_maintenance_state
  primary_language: Chinese
  repository_access: read_only
  repository_writes: prohibited
  issue_or_PR_mutation: prohibited
  execution_source_update: prohibited
  target_project_actions: prohibited
  FABLE5_substantive_review_or_design: prohibited
```

The review must assess whether current Mnemosyne maintenance information is coherent, auditable, appropriately scoped, and ready for the next non-FABLE maintenance phase.

### 4.1 Required review domains

1. **Execution-source integrity**
   - confirm the unique execution-source boundary;
   - identify unsupported behavior claims, silent promotions, or conflicts between execution source and non-execution-source records;
   - do not propose an execution-source edit unless a finding demonstrates a concrete need.

2. **Live wayfinding and handoff consistency**
   - verify current route records after MNEMOSYNE-139;
   - identify stale, contradictory, or misleading high-signal guidance;
   - distinguish live precedence from retained historical evidence.

3. **Guidance and command correctness**
   - review receive/load/prepare handoff separation;
   - review artifact-delivery and single-active-PR constraints;
   - verify that commands do not silently import unrelated maintenance routes or authorize writes.

4. **Review and validation state**
   - assess current validation conclusions and their limitations;
   - preserve the distinction between behavioral evidence, mechanical proof, and package-level closure;
   - do not rerun completed validations merely because they exist.

5. **Research-evidence usage**
   - check whether current non-FABLE research findings are mapped and qualified correctly;
   - flag stale platform claims that need later freshness verification;
   - do not perform new web research in the initial repository-health review unless the user separately requests it or a conclusion cannot be responsibly stated without freshness verification.

6. **Backlog and open-question hygiene**
   - distinguish true pending work from historical or superseded TODO wording;
   - identify interrupted work that remains valuable;
   - propose the next one to three non-FABLE tasks in priority order.

7. **Task/result and audit hygiene**
   - sample recent task-result records and current-state updates for scope, authority, evidence, and lineage consistency;
   - identify missing records, overclaims, duplicate closeout chains, or stale canonical pointers.

### 4.2 Required outcome questions

The report must answer:

1. Is the current execution-source boundary intact?
2. Are the current high-signal status and handoff records mutually consistent?
3. Which non-FABLE records are stale or superseded but still likely to mislead a new maintainer?
4. Are recent validations represented with correct limitations?
5. Which open questions are genuinely current?
6. Which historical TODO items should be closed, retained, or rewritten?
7. What are the highest-value next one to three non-FABLE tasks?
8. Is any immediate repository repair required before the next substantive maintenance task?
9. Which actions must explicitly remain deferred?

## 5. Minimum evidence set

Read these paths before broadening the review:

```yaml
minimum_evidence:
  execution_and_entry:
    - README.md
    - current/human-approved-spec.md
    - commands/receive-mnemosyne-handoff.md
    - commands/load-mnemosyne-guidance.md
    - commands/prepare-mnemosyne-handoff.md
  current_live_state:
    - current/post-interruption-live-wayfinding-status.md
    - current/meta-agent-test-route-status.md
    - current/review-and-validation-status.md
    - current/artifact-delivery-repair-status.md
    - current/meta-agent-replay-mechanical-proof-decision.md
    - current/handoff-guidance-open-question.md
    - handoff/handoff-current.md
  active_guards:
    - current/artifact-delivery-and-direct-generation-guard.md
    - current/github-single-active-pr-lineage-guard.md
  mixed_route_backlog_evidence:
    - current/active-context.md
    - current/todo.md
    - current/open-questions.md
  recent_result_samples:
    - notes/codex-task-results/MNEMOSYNE-113-result.md
    - notes/codex-task-results/MNEMOSYNE-122-result.md
    - notes/codex-task-results/MNEMOSYNE-127-result.md
    - notes/codex-task-results/MNEMOSYNE-137-result.md
    - notes/codex-task-results/MNEMOSYNE-138-result.md
    - notes/codex-task-results/MNEMOSYNE-139-result.md
```

Treat `current/active-context.md`, `current/todo.md`, and `current/open-questions.md` as mixed-route evidence, not as an automatic action plan.

Read additional files only when needed to verify a concrete finding. Keep a source manifest of all paths actually read.

## 6. Absolute FABLE5 exclusion

The receiving conversation must not take over or advance the separate FABLE5 route.

```yaml
FABLE5_exclusion:
  substantive_review: prohibited
  independent_design: prohibited
  Greenfield_steps: prohibited
  result_storage: prohibited
  task_generation: prohibited
  comparison_or_adjudication: prohibited
  owner_conversation: separate_dedicated_conversation
```

Do not read FABLE5 report bodies merely for comprehensiveness. A global current-state file may be read even if it contains a brief FABLE5 status reference, but the review must not evaluate that route's substance. Record it only as an excluded concurrent route.

## 7. Forbidden actions

During this transferred review, do not:

- create or update branches, commits, pull requests, issues, comments, labels, workflows, automation, or repository settings;
- modify `current/human-approved-spec.md` or any other repository file;
- create target workspaces;
- ingest target materials;
- access or write a target repository;
- start an operational Meta-Agent build;
- execute observer-assisted no-write proof;
- approve a §19 exception;
- formalize or promote regressions;
- rerun completed Meta-Agent or artifact-delivery behavioral campaigns;
- perform FABLE5 review, design, Greenfield, comparison, or storage work;
- claim that visible model labels prove hidden backend identity.

## 8. Review method

Use this sequence:

### Phase A — Receive and bind

- complete handoff receive;
- separately refresh Mnemosyne guidance;
- confirm the transferred task and exclusions remain preserved.

### Phase B — Build the source manifest

- read the minimum evidence set;
- record exact paths and available refs/blob SHAs;
- identify missing or inaccessible evidence;
- do not form final conclusions before the minimum set is reviewed.

### Phase C — Analyze by domain

For each required review domain:

- state the current claimed condition;
- cite repository evidence paths;
- distinguish fact, inference, and recommendation;
- classify each finding by severity and confidence;
- state whether immediate repair is needed.

### Phase D — Cross-check backlog and route truth

- compare mixed-route historical files against current live precedence;
- distinguish stale wording from active unresolved work;
- prevent completed routes from being proposed again;
- preserve separately owned routes and optional future work.

### Phase E — Produce repair agenda, not repairs

- recommend a bounded repair bundle only where findings justify it;
- assign candidate task IDs only as proposals, not authorization;
- identify safe sequencing and stop conditions;
- leave repository writes for later explicit user approval.

## 9. Required deliverable

The review is long and transfer-sensitive. Deliver it file-first as a verified local Markdown artifact in the same response when file tooling is available.

Suggested filename:

`mnemosyne-non-fable-comprehensive-health-review.md`

The chat response should contain only:

- a concise executive summary;
- the verified download link;
- overall verdict;
- top findings and recommended next task sequence;
- all user actions;
- limitations and blocked areas.

Do not duplicate the entire long report inline unless the user explicitly requests that.

The report must include:

1. title and review metadata;
2. executive summary;
3. scope and exclusions;
4. source manifest;
5. methodology;
6. execution-source integrity assessment;
7. live wayfinding and handoff assessment;
8. guidance/command assessment;
9. validation-state assessment;
10. research-evidence usage assessment;
11. backlog and open-question triage;
12. task/result audit sampling;
13. findings table with severity, confidence, evidence, and repair need;
14. immediate-repair decision;
15. prioritized one-to-three-task agenda;
16. explicit non-actions;
17. limitations and unresolved questions;
18. safe next action.

Use a final summary schema:

```yaml
mnemosyne_non_fable_health_review:
  review_id: MNEMOSYNE-NON-FABLE-COMPREHENSIVE-HEALTH-REVIEW-001
  tested_repository_ref:
  review_mode: read_only
  FABLE5_excluded: true
  source_manifest_complete_for_claimed_scope:
  execution_source_boundary:
  live_wayfinding_consistency:
  handoff_consistency:
  guidance_command_consistency:
  validation_state_quality:
  backlog_hygiene:
  task_result_hygiene:
  immediate_repair_required:
  overall_verdict: PASS | PASS_WITH_FINDINGS | REPAIR_RECOMMENDED | BLOCKED
  prioritized_next_tasks:
  explicit_non_actions:
  limitations:
  safe_next_action:
```

## 10. Safe next action after review

After delivering the complete review artifact, stop and wait for the user to choose whether to:

- approve a specific repair task;
- select one prioritized substantive maintenance task;
- request clarification or narrower evidence review;
- defer all action.

Do not convert recommendations into repository changes without a new explicit user authorization and a fresh task ID.

## 11. Freshness and limitations

- This package is prepared from `master@3cf6e5116a360c3f131ad4dfd472a819300ba461` after PR #190 merged.
- Repository state may advance before the receiver starts. The receiver must verify current `master` and record any delta before relying on this package's snapshot.
- Platform/model/tool behavior is time-sensitive. Verify current external facts only when they are material to a finding.
- This package does not claim that every historical TODO or open question is still valid; backlog triage is part of the transferred task.
- This package does not authorize repository writes or FABLE5 work.

## 12. User transfer instruction

In the new conversation, explicitly select the GitHub app for `08822407d/Mnemosyne` and send the paired startup prompt from:

`handoff/mnemosyne-non-fable-comprehensive-health-review-startup-prompt.md`

The new conversation must receive this authorized package first, then load Mnemosyne guidance in a separate operation.