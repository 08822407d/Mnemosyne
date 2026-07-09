# ChatGPT GitHub Write Preflight Checklist

```yaml
record_type: operational_preflight_checklist
authority_level: non_execution_source_support_instrument
created_by_task: MNEMOSYNE-098
applies_to:
  - ordinary_ChatGPT_GitHub_app_writes_for_Mnemosyne
  - low_scope_documentation_PRs
not_execution_source: true
```

## Purpose

This checklist exists because ordinary ChatGPT GitHub App write actions in this maintenance track accidentally created default-branch files when the `branch` argument was omitted. It also records the user's later preference that ordinary ChatGPT Mnemosyne PRs should be ready PRs by default, not draft PRs.

This file is a support instrument. It does not replace `current/human-approved-spec.md` and does not authorize any write by itself.

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
    - create a pull request with draft=false unless the user explicitly asks for draft
    - do not auto-merge unless explicitly authorized for that PR
  5_result_record:
    - record files created/modified/deleted
    - record whether execution source/current-state/handoff/target workspace/material/write/build/regression files changed
    - record whether a Codex task was generated
    - record whether paused route was resumed or closed
```

## Default PR policy

```yaml
ordinary_chatgpt_mnemosyne_pr_policy:
  default_draft: false
  create_ready_pr_by_default: true
  create_draft_only_if_user_explicitly_requests_draft: true
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

This checklist does not authorize repository repairs, execution-source updates, target workspace creation, target material ingestion, target repository write, operational build, regression formalization, auto-writeback, auto-merge, or resumption/closure of the paused post-handoff route.
