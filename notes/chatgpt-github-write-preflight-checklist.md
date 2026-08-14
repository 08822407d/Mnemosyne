# ChatGPT GitHub Write Preflight Checklist

```yaml
record_type: operational_preflight_checklist
authority_level: non_execution_source_support_instrument
created_by_task: MNEMOSYNE-098
last_aligned_by_task: MNEMOSYNE-210
active_ready_PR_guard: current/agent-product-ready-pr-and-frontier-efficiency-guard.md
active_lineage_guard: current/github-single-active-pr-lineage-guard.md
applies_to:
  - ordinary_ChatGPT_GitHub_app_writes_for_Mnemosyne
  - low_scope_documentation_PRs
not_execution_source: true
```

## Purpose

This checklist exists because ordinary ChatGPT GitHub App write actions in this maintenance track accidentally created default-branch files when the `branch` argument was omitted. It also records the Owner's durable preference that completed ordinary ChatGPT Mnemosyne work should be submitted as a Ready PR by default, not as a Draft PR requiring a manual transition.

The Ready-vs-Draft rule, Owner-review semantics and post-merge closeout are now controlled by the active guard `current/agent-product-ready-pr-and-frontier-efficiency-guard.md`. This file remains a support instrument. It does not replace `current/human-approved-spec.md` or active guards and does not authorize any write by itself.

## Mandatory write preflight

Before any ordinary ChatGPT GitHub App write action that affects the Mnemosyne repository:

```yaml
preflight:
  1_confirm_task_authority:
    - identify current user authorization or task scope
    - confirm the write is low-scope or explicitly authorized
    - confirm no execution-source/current-state/handoff/target/regression/build boundary is crossed unless that exact scope is approved
  2_define_branch:
    - choose a branch name before the first write
    - create the branch with GitHub.create_branch
    - fetch a known file from that branch using ref=<branch_name> to confirm the branch exists
  3_prepare_write_calls:
    - every create_file/update_file/delete_file call must include branch=<branch_name>
    - never rely on the default branch parameter implicitly
    - if a file action schema says branch is optional, treat it as mandatory for Mnemosyne writes unless the user explicitly approves direct default-branch write
  4_open_pr:
    - compare master..branch before PR if possible
    - complete the active-guard PR-readiness preflight
    - create a pull request with draft=false when the task is complete and no recorded Draft exception applies
    - create Draft only for incomplete work, a content-changing pending Owner decision/review, expected substantive commits, or an explicit Owner request
    - do not auto-merge unless explicitly authorized for that PR
  5_result_record:
    - record files created/modified/deleted
    - record whether execution source/current-state/handoff/target workspace/material/write/build/regression files changed
    - record whether a Codex task was generated
    - record whether paused route was resumed or closed
    - record the Ready/Draft decision and any exception
    - do not represent Ready transition, approval or merge as comprehensive human content review
    - after merge, verify latest master and repair stale current-status records through a follow-up task when needed
```

## Default PR policy

```yaml
ordinary_chatgpt_mnemosyne_pr_policy:
  default_draft: false
  create_ready_pr_by_default: true
  create_draft_only_if:
    - substantive_work_incomplete
    - content_changing_Owner_decision_or_required_review_pending
    - further_substantive_commits_expected
    - Owner_explicitly_requests_draft
  Owner_full_diff_review_assumed: false
  auto_merge_default: false
```

## Direct default-branch exception rule

```yaml
direct_default_branch_write:
  default: prohibited_for_ordinary_ChatGPT_Mnemosyne_writes
  allowed_only_if:
    - user explicitly approves direct default-branch write for the specific action
    - risk is very low
    - result record explains why PR branch was not used
  if_accidental:
    - stop and disclose the deviation promptly
    - record the exact file paths and commit/result context
    - avoid further direct default-branch writes
    - if possible, repair through a later PR or record why cleanup is not appropriate
```

## Boundary

This checklist does not authorize repository repairs, execution-source updates, target workspace creation, target material ingestion, target repository write, operational build, regression formalization, auto-writeback, auto-merge, validation execution, or resumption/closure of a paused route.
