# Agent-Product Ready-PR, Owner Feedback, Frontier-Turn Efficiency, and Post-Merge Closeout Guard

> User-approved Mnemosyne behavior guard for completed Agent-product changes, human oversight, scarce frontier-model use, and post-merge route closure. This file is not an execution source; `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
guard_id: MNEMOSYNE-AGENT-PRODUCT-READY-PR-FRONTIER-EFFICIENCY-001
created_by_task: MNEMOSYNE-210
status: active_after_MNEMOSYNE_210_merge
execution_source: current/human-approved-spec.md
execution_source_modified: false
applies_to:
  - Mnemosyne_maintenance_and_self_development
  - Meta_Agent_or_other_meta_Agent_product_work_when_the_target_owner_adopts_or_explicitly_loads_this_guard
  - branch_backed_Owner_review_and_frontier_consolidation
  - important_Agent_generated_documentation_or_behavior_changes
  - PR_creation_review_merge_instruction_and_post_merge_closeout
  - scarce_frontier_or_Pro_conversation_segments
user_decision_source:
  - current_conversation_after_PR_277_workflow_failure_review
  - current_conversation_Owner_evidence_comparing_passive_behavior_feedback_with_full_PR_review
specific_controls:
  - completed_work_Ready_PR_default
  - Draft_PR_exception_only
  - Owner_merge_is_authority_gate_not_full_content_review
  - Agent_pre_merge_quality_assurance
  - user_observed_behavior_feedback_as_first_class_evidence
  - frontier_turn_completion_and_quota_efficiency
  - explicit_model_requirement_before_new_user_gate
  - mandatory_post_merge_state_closeout
```

## 1. Problem addressed

For Mnemosyne and similar meta-Agent products, the product is primarily the Agent's later behavior, memory use, routing, authority handling, and generated work. A large PR may contain thousands of lines of natural-language rules, decision records, validation packages, and state files. Requiring the Owner to read every changed file or line before every merge is impractical and is often a weak predictor of the combined runtime behavior.

The Owner can usually detect user-visible behavioral deviations quickly during real use and report a concrete failure at much lower personal cost. That feedback path is valuable evidence, but it does not remove the need for Agent-side semantic review, mechanical checks, privacy/authority safeguards, validation where needed, rollback, or explicit Owner control over merges.

PR #277 exposed four failures that this guard prevents:

1. a completed work package was presented as Draft and the Owner was implicitly asked to turn it Ready;
2. Draft-to-Ready was treated as if it could stand in for substantive human review;
3. a scarce Pro/frontier segment ended with mechanical follow-up while authorized frontier-level review could still have been completed;
4. after the Owner merged the PR, the repository route status remained stale until a later complaint exposed it.

## 2. Completed work uses a Ready PR by default

### 2.1 Ready criteria

Create one canonical **Ready PR** with `draft: false` when all of the following are true:

- the authorized task scope is substantively complete;
- required Agent semantic review has completed;
- required mechanical/path/reference/identity checks have completed;
- known limitations, deferrals, unexecuted validation, and prohibited adjacent actions are disclosed;
- no unresolved decision would materially change the submitted contents;
- the Agent can give an evidence-bound recommendation to merge, request changes, or stop.

A later stage being separately gated does not make the current stage incomplete. For example, a completed validation design may be merged as a Ready PR while validation execution remains explicitly unauthorized.

### 2.2 Draft exceptions

Use a Draft PR only when at least one recorded condition applies:

- substantive work is still incomplete;
- a material Owner decision is pending and will change the PR contents;
- required semantic, safety, heterogeneous, or mechanical review is still pending;
- further substantive commits are intentionally expected before review;
- the Owner explicitly requests Draft status for the current PR.

Generic caution, large diff size, Agent authorship, unexecuted future stages, or an assumption that the Owner should read everything are not valid Draft reasons.

### 2.3 Tool and generic-default override

When the current GitHub tool or generic skill defaults to Draft, the Mnemosyne actor must explicitly request `draft: false` after the Ready criteria pass. The generic Draft default does not override this user-approved project rule.

If a Draft is created accidentally for Ready work, correct it to Ready after verifying that no Draft exception applies and record the correction. Do not ask the Owner to perform a meaningless manual Ready transition.

## 3. Human oversight and review evidence

### 3.1 Owner role

The Owner's default role is to:

- retain authority over whether and when a PR merges;
- confirm or correct explicit architecture, scope, risk, privacy, authority, quota, and adoption decisions;
- inspect summaries, identified risks, unresolved decisions, and selected samples when desired;
- report unexpected behavior observed during real use;
- request changes, stop, rollback, or reopen design questions.

The Owner is not assumed to have performed comprehensive file-by-file or line-by-line review merely because the Owner:

- opened the PR;
- changed Draft to Ready;
- approved the PR;
- clicked Merge;
- later used the resulting Agent.

### 3.2 Agent responsibility before merge

Before asking for merge, the responsible Agent must perform and report, as applicable:

- comparison against the Owner's confirmed decisions and current execution source;
- semantic consistency review across changed behavior, status, handoff, candidate, validation, and result records;
- changed-path and protected-boundary verification;
- reference, identifier, version, and state consistency checks;
- security, privacy, authority, irreversibility, and migration risk review;
- explicit known limitations, deferrals, and unexecuted tests;
- a clear disposition: `RECOMMEND_MERGE`, `REQUEST_CHANGES`, `BLOCKED`, or an equivalent evidence-bound result.

“Please review the PR” is not a substitute for this work. The Agent should reduce the Owner's review burden to the decisions and risks that genuinely require human authority or judgment.

### 3.3 Evidence semantics

A Draft-to-Ready transition, approval, or merge is repository-state evidence only. It does not prove:

- complete human content review;
- technical correctness;
- behavioral correctness;
- validation success;
- target adoption;
- backend/model identity.

Run-context and result records must name the actual reviewer and reviewed scope. Do not relabel Agent review as fully manual human review.

## 4. Real-use behavioral feedback

### 4.1 First-class evidence

Concrete Owner-observed behavior is a first-class defect and improvement signal for Agent products. A useful feedback record should preserve:

```yaml
behavior_feedback:
  observed_behavior:
  expected_behavior:
  user_cost_or_consequence:
  triggering_context_or_safe_ref:
  reproducibility:
  suspected_layers: []
  immediate_containment:
  root_cause_status:
  repair_task_or_PR:
  regression_or_validation_need:
```

The repair route should connect the observed behavior to the responsible rules, state, prompts, code, or process and should add focused prevention where proportionate.

### 4.2 Limits of passive detection

Real-use feedback does not replace proactive safeguards for failures that may remain hidden or cause unacceptable harm before detection, including:

- privacy or credential exposure;
- unauthorized writes or authority expansion;
- data corruption or silent truth-source divergence;
- irreversible migration or deletion;
- execution-source or security-boundary modification;
- misleading provenance or validation claims;
- failures whose consequences are not readily visible to the Owner.

Use mechanical checks, synthetic validation, isolated trials, heterogeneous review, or explicit Owner gates according to risk. The policy is not “test only in production”; it is “do not transfer comprehensive static review of Agent-generated material to the Owner when better Agent/mechanical/behavioral evidence channels exist.”

## 5. Frontier-turn completion and quota efficiency

### 5.1 Required completion check

Before ending a Pro/frontier segment or asking the Owner for a new gate, record or visibly answer:

```yaml
frontier_turn_completion_check:
  authorized_frontier_scope:
  substantive_frontier_work_completed: true | false
  substantive_frontier_work_remaining: []
  additional_work_possible_without_new_Owner_decision: []
  bounded_work_suitable_for_next_tier: []
  mechanical_work_remaining: []
  current_user_requested_continue_if_possible_honored: true | false
  reason_frontier_turn_ends_now:
  next_user_action:
  next_action_model_requirement:
```

Do not end a scarce frontier turn merely because an internal substep completed when other authorized, relevant frontier-level synthesis, review, repair, package design, or failure analysis can still be completed safely.

### 5.2 User instruction to continue

When the Owner explicitly asks the Agent to continue or automatically perform all currently available work:

- complete every authorized, relevant, bounded action that does not cross a separate permission, privacy, quota, product-surface, or irreversible-action gate;
- do not stop after provenance-only or mechanical bookkeeping if substantive authorized work remains;
- prepare downstream bounded artifacts, prompts, decision recommendations, tests, and return contracts during the same frontier segment when they are unlikely to be invalidated;
- disclose the exact gate that prevents further progress rather than using a vague “next step”.

Separate authorization requirements remain real. This rule prevents unnecessary fragmentation; it does not authorize PR creation, merge, external quota, repository creation, validation execution, or target modification unless the current Owner instruction covers that action.

### 5.3 Model requirement before a new gate

Before asking the Owner to perform a new operation, explicitly state whether that operation and its immediate follow-up require Pro/frontier reasoning.

If the remaining work is bounded or mechanical, say that Pro is not required before the Owner spends another frontier turn. Where practical, complete the frontier reasoning first and hand off one self-contained package to a next-tier or mechanical executor.

A response must not leave a mechanical PR creation, metadata update, merge verification, or post-merge status correction as an unexplained reason to keep using Pro.

## 6. Post-merge closeout

After a PR merge becomes observable, the responsible route must perform or explicitly route a bounded closeout:

1. verify the exact merged PR, merge commit, latest default-branch SHA, and expected files;
2. verify whether the head branch still exists and whether any prior retention obligation applies;
3. update stale current-status, backlog, handoff, result, or PR-gate records that still describe the PR as open or unmerged;
4. distinguish merge completion from validation, execution, target adoption, or other separately gated work;
5. identify the next true route gate and its model requirement;
6. record known limitations such as absent CI or incomplete post-merge checks.

Post-merge verification and status repair are normally `MECHANICAL_ONLY` or `NEXT_TIER_SUFFICIENT_CANDIDATE`. If the Owner is already using Pro and explicitly asks the current Agent to continue, complete the closeout in the same authorized task rather than leaving a stale route solely to preserve model separation.

Do not automatically modify `master`; use a new follow-up task/branch when the merged content itself contains stale state that requires correction.

## 7. PR delivery contract for Agent products

Before presenting a merge operation, provide a compact result such as:

```yaml
agent_product_PR_delivery:
  task_id:
  PR:
  PR_state: ready | draft_with_recorded_exception
  substantive_work_complete:
  semantic_review:
  mechanical_verification:
  known_unvalidated_items: []
  Owner_decisions_required_before_merge: []
  merge_recommendation: RECOMMEND_MERGE | REQUEST_CHANGES | BLOCKED
  comprehensive_human_diff_review_assumed: false
  post_merge_closeout_owner:
```

Explain the material behavior changes and risks in natural language. Do not force the Owner to infer the recommendation from repository metadata or read the entire diff to learn what the Agent concluded.

## 8. Relationship and precedence

This guard is more specific for Ready-vs-Draft status, Agent-product human-review semantics, frontier-turn completion, and post-merge closeout than:

- a generic GitHub tool/skill Draft default;
- `current/owner-review-branch-ledger-guard.md`;
- `notes/chatgpt-github-write-preflight-checklist.md`;
- general wording in `current/github-single-active-pr-lineage-guard.md`.

It complements:

- `current/user-operation-next-step-capability-and-intent-guard.md` for model-capability and low-burden progress;
- `current/github-single-active-pr-lineage-guard.md` for one branch/one PR lineage;
- `current/run-context-and-pr-provenance-guard.md` for honest review attribution;
- `current/pr-merge-branch-disposition-guard.md` for post-merge branch retention and release;
- `current/cross-conversation-execution-intent-and-operator-flow-guard.md` for explicit run intent.

The stricter safety, privacy, authority, validation, and separate-authorization boundary always remains controlling.

## 9. Boundaries

This guard does not:

- authorize repository writes, PR creation, merge, auto-merge, branch deletion, model switching, quota use, validation execution, target adoption, or external-service actions;
- make all PRs Ready when work is incomplete;
- make behavioral feedback sufficient for hidden or high-impact risk classes;
- reduce the Owner's authority to inspect any file or demand additional review;
- attest an exact backend or model identity;
- convert a Ready PR or merge into execution source or target truth;
- automatically apply to a separate target repository unless that target's Owner adopts it or the task explicitly loads it.
