# MNEMOSYNE-089 Result Record

```yaml
task_id: MNEMOSYNE-089
task_name: Add ChatGPT GitHub App PR capability and task-authority guidance to execution source
task_type: execution_source_behavior_guidance_update
action_actor: ChatGPT_GitHub_app
started_from: post_MNEMOSYNE_085_inserted_long_work_context
files_modified:
  - current/human-approved-spec.md
files_created:
  - notes/codex-task-results/MNEMOSYNE-089-result.md
execution_source_modified: true
current_state_files_modified: false
handoff_files_modified: false
official_083_artifacts_modified: false
target_workspace_created: false
target_materials_ingested: false
target_repository_written: false
regression_formalized: false
operational_build_started: false
```

## Summary

MNEMOSYNE-089 adds a new execution-source behavior principle to `current/human-approved-spec.md`:

`## 18. ChatGPT GitHub App 写入能力与任务授权原则`

The new principle records that, as of July 2026, Mnemosyne must no longer assume ordinary ChatGPT conversations are globally read-only for GitHub. When the user connects/selects a GitHub app in official ChatGPT web/app and the current model/account/workspace/app-action configuration supports the action, an ordinary ChatGPT conversation may perform GitHub write actions such as branch/file/PR creation.

The principle also records:

- Codex Cloud remains preferred for larger auditable implementation or code-execution-style work, but it is no longer the only possible path for GitHub PR creation.
- Platform permission and Mnemosyne task authority are separate and both are required.
- Future prompts that may use GitHub writes must verify current official OpenAI documentation, ChatGPT UI/app capabilities, approval cards, repository/branch/file paths, protected paths, and target workspace/material/write boundaries.
- Prefer branch + PR over direct default-branch edits.
- Prefer `Allow once` / one-time approval over persistent `Always allow` for Mnemosyne GitHub writes.
- High-scope or sensitive writes such as merge, delete, bulk modification, or auto-merge require immediate explicit approval and should usually be avoided unless task-specific.

## Source basis

External source:

- OpenAI Help Center, `Apps in ChatGPT`, `https://help.openai.com/en/articles/11487775-connectors-in-chatgpt`, consulted 2026-07-07.

Repository-local sources:

- PR #134 / MNEMOSYNE-087 platform guide update documenting ChatGPT GitHub app write capability.
- Current observed ChatGPT GitHub app behavior in this maintenance conversation.

## Verification notes

- `current/human-approved-spec.md` was the only existing file modified.
- No current-state, handoff, official MNEMOSYNE-083 artifact, target workspace, target material, target repository, formal regression, or operational build file was modified.
- This result record was created to document the execution-source behavior guidance update.

## Known limitations

- Exact ChatGPT app write capabilities remain time-sensitive and may vary by account, model surface, workspace, plan, region, GitHub app installation, action controls, and app permission settings.
- Current OpenAI documentation says apps are available with all models except Pro models; therefore future prompts must verify current model/app compatibility instead of assuming availability.
- This task does not resume or close the paused post-handoff route recorded by MNEMOSYNE-085.
