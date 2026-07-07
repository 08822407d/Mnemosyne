# ChatGPT GitHub App Capabilities Guide v0.1

```yaml
artifact_id: CHATGPT-GITHUB-APP-CAPABILITIES-GUIDE-v0.1
created_by: ChatGPT GitHub maintenance conversation
created_for: Mnemosyne inserted long work after MNEMOSYNE-085
task_id: MNEMOSYNE-087
status: non_execution_source_platform_guide
last_researched_utc: 2026-07-07
primary_use: update Mnemosyne assumptions about ChatGPT ordinary-conversation GitHub read/write capabilities
```

## 0. Authority and freshness

This guide is a non-execution-source platform guide.

It does not modify or override `current/human-approved-spec.md`.

It does not approve:

- target workspace creation;
- target material ingestion;
- target repository write;
- formal regression conversion;
- operational memory-system build or installation;
- Mnemosyne execution-source updates;
- treating `PASS_WITH_WARNINGS` as production-ready or target-write approval.

ChatGPT app / connector behavior, app names, plan gating, GitHub action availability, and permission prompts are time-sensitive. Re-verify current OpenAI documentation, the connected GitHub app’s action list, and the actual approval card before relying on this guide.

## 1. Current verified update

As of this task, Mnemosyne should no longer assume that a normal ChatGPT conversation with a connected GitHub app is read-only.

Current OpenAI documentation for Apps in ChatGPT says apps can search and reference information, use deep research, sync content, and, for some apps, take write actions such as creating or updating information in a connected service. It also says app permissions apply to ChatGPT conversations and control when ChatGPT must ask before using an app.

OpenAI’s app permissions documentation lists permission options that may include:

- `Always ask`;
- `Any changes`;
- `Important actions`;
- `Never ask`.

The default described by OpenAI is `Important actions`, which allows reading from apps automatically but asks before actions that may have a meaningful effect outside ChatGPT, expose sensitive information, or be difficult to undo.

OpenAI also documents that before an action runs, ChatGPT shows an approval card with information about the app and proposed action; possible buttons include `Deny`, `Allow` / `Allow once`, and sometimes `Always allow`.

Therefore, the current platform assumption is:

```yaml
chatgpt_ordinary_conversation_github_app:
  read_actions: possible_when_connected_and_authorized
  write_actions: possible_for_some_apps_and_configurations
  branch_file_pr_actions: observed_possible_in_this_repository_context
  approval_prompt_required_by_default_for_important_actions: true
  ordinary_chat_read_only_assumption: stale_or_at_least_no_longer_safe_as_global_rule
```

## 2. Mnemosyne observed evidence

This maintenance conversation used the ChatGPT GitHub app to create and merge PR #133, `Add Claude conversation capability settings guide`.

The observed GitHub action chain was:

```yaml
observed_actions:
  - create_branch
  - create_file
  - create_pull_request
  - user_review_and_merge_of_PR_133
```

PR #133 created:

```text
notes/platform-guides/README.md
notes/platform-guides/claude-conversation-capabilities-and-settings-guide-v0.1.md
notes/codex-task-results/MNEMOSYNE-086-result.md
```

This is direct repository-local evidence that a ChatGPT ordinary maintenance conversation can, with user approval and the connected GitHub app, perform GitHub write operations including branch/file/PR creation in this repository context.

This observation does **not** imply that:

- every ChatGPT plan has the same GitHub app capabilities;
- every model can use apps;
- every GitHub app connection is write-capable;
- writes should occur without task-local user approval;
- ChatGPT ordinary conversation is equivalent to Codex Cloud for larger implementation tasks;
- repository writes are safe or authorized by default.

## 3. Relationship to Codex Cloud

Earlier Mnemosyne process notes often treated Codex Cloud as the main remote GitHub file-writing and version-saving assistant.

That can remain historically accurate, but it is no longer sufficient as a global platform capability boundary.

Updated interpretation:

```yaml
codex_cloud:
  role: preferred_for_larger_auditable_implementation_tasks_and_code_execution_style_work
chatgpt_ordinary_conversation_with_github_app:
  role: can_perform_small_explicit_GitHub_app_write_actions_when_available_and_user_approved
  not_recommended_for:
    - large_unreviewed_repository_changes
    - target_workspace_or_material_work_without_separate_approval
    - operational_build_or_regression_formalization_without_task_authority
```

## 4. Approval and safety guidance

For Mnemosyne work, use this permission stance:

```yaml
recommended_permission_choice:
  read_only_checks: allow_read_if_already_connected_or_approve_when_prompted
  one_off_documentation_or_state_marker_write: Allow_once
  large_or_repeated_write_work: prefer_Codex_or_explicit_PR_workflow
  Always_allow: avoid_for_Mnemosyne_unless_user_deliberately_accepts_persistent_write_risk
```

Do not rely on a previous permission grant as task authority. Platform permission and Mnemosyne task authority are separate:

```yaml
platform_permission: ChatGPT is technically allowed to call the GitHub app action
mnemosyne_task_authority: user explicitly approved this repository action under Mnemosyne rules
```

Both are required for repository writes.

## 5. Prompt-preflight requirement for future ChatGPT GitHub tasks

Future Mnemosyne prompts that may use ChatGPT GitHub app writes should include a setup block:

```yaml
chatgpt_github_setup:
  github_app_connected: true_or_false_or_unknown
  intended_action_type: read_only | branch_file_pr_write | issue_pr_comment | other
  repository_write_authorized_by_user: true_or_false
  permission_prompt_expected: true_or_false_or_unknown
  recommended_permission_response: Allow_once_for_this_task
  no_persistent_allow_required: true
  verify_before_write:
    - intended_repository
    - branch_name
    - file_paths
    - protected_paths
    - target_workspace_material_write_boundaries
```

For any write-capable action, the assistant should first state:

```text
This action will write to GitHub or create a PR. It is not merely repository reading. I will only proceed if this specific write is within the user-approved task scope.
```

## 6. Repository-write classification

Use this classification in future Mnemosyne discussions:

```yaml
chatgpt_github_action_classes:
  read_only:
    examples:
      - fetch_file
      - search_repository
      - get_pr_info
      - search_prs
    default_mnemosyne_requirement: cite evidence and do not mutate repository
  write_low_scope:
    examples:
      - create_branch
      - create_file
      - update_file
      - create_pull_request
      - add_comment_to_issue_or_pr
    default_mnemosyne_requirement: explicit task-local user approval plus approval card; prefer Allow once
  write_high_scope_or_sensitive:
    examples:
      - merge_pull_request
      - delete_file
      - close_or_update_issue_state
      - enable_auto_merge
      - label_or_modify_many_issues
    default_mnemosyne_requirement: explicit user approval immediately before action; usually avoid unless task specifically requires it
```

## 7. How this changes prior Mnemosyne guidance

Any Mnemosyne statement that says or implies:

```text
ordinary ChatGPT conversations can only read GitHub and cannot create branches, files, or PRs
```

should now be treated as stale unless it is explicitly scoped to a past date, a past tool surface, or a specific disconnected/no-write environment.

Updated rule:

```yaml
ordinary_chatgpt_github_capability_rule:
  do_not_assume_read_only: true
  check_current_app_capabilities: true
  require_user_approval_for_writes: true
  record_write_actions_as_external_effects: true
```

If stale statements are found in execution-source files, they should not be silently edited by an unapproved task; route them through normal Mnemosyne spec-update or user-decision process.

If stale statements are found in non-execution-source historical records, preserve them as historical context unless they are still part of the live route.

## 8. Suggested future repository update behavior

When ChatGPT ordinary conversation performs GitHub writes in Mnemosyne:

- prefer a branch and PR over direct default-branch edits;
- record a task result when the write changes Mnemosyne-maintenance state or creates durable documentation;
- include `action_actor: ChatGPT_GitHub_app` or equivalent;
- list files created/modified;
- state whether execution source/current-state/handoff/target workspace/material/write/build/regression files were touched;
- cite current OpenAI app permission assumptions if platform capability matters.

## 9. Source basis

Source consulted:

- OpenAI Help Center, `Apps in ChatGPT`, `https://help.openai.com/en/articles/11487775-connectors-in-chatgpt`, accessed 2026-07-07.

Repository-local evidence:

- PR #133, `Add Claude conversation capability settings guide`, created from a ChatGPT ordinary GitHub app workflow and merged into `master`.

## 10. Known uncertainties

Open questions / recheck items:

- exact date when the GitHub app gained create-branch / create-file / create-PR actions in ordinary ChatGPT conversations;
- whether the same write actions are available to every account, plan, workspace, model, or region;
- whether app write availability is disabled for Pro models or specific model surfaces, per current OpenAI documentation;
- whether the connected GitHub app’s action list changes over time;
- whether a user’s app permission setting is `Always ask`, `Any changes`, `Important actions`, or `Never ask`;
- whether workspace admins have limited write actions through app action controls.
