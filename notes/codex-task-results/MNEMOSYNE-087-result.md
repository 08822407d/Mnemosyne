# MNEMOSYNE-087 Result Record

```yaml
task_id: MNEMOSYNE-087
task_name: Record ChatGPT ordinary-conversation GitHub app write capability update
task_type: non_execution_source_platform_guide_update
action_actor: ChatGPT_GitHub_app
started_from: post_MNEMOSYNE_085_inserted_long_work_context
files_created:
  - notes/platform-guides/chatgpt-github-app-capabilities-guide-v0.1.md
  - notes/codex-task-results/MNEMOSYNE-087-result.md
files_modified:
  - notes/platform-guides/README.md
execution_source_modified: false
current_state_files_modified: false
handoff_files_modified: false
target_workspace_created: false
target_materials_ingested: false
target_repository_written: false
regression_formalized: false
operational_build_started: false
```

## Summary

MNEMOSYNE-087 records that Mnemosyne should no longer assume a normal ChatGPT conversation with a connected GitHub app is globally read-only.

The update creates a non-execution-source platform guide documenting:

- OpenAI's current Apps in ChatGPT documentation for app write actions and app permissions;
- the default Important actions approval behavior described by OpenAI;
- permission options such as Always ask, Any changes, Important actions, and Never ask;
- approval-card behavior such as Allow once / Always allow;
- repository-local observed evidence from PR #133 showing branch/file/PR operations from a ChatGPT GitHub app workflow;
- updated Mnemosyne prompt-preflight and safety rules for ChatGPT GitHub writes.

## Source basis

External source:

- OpenAI Help Center, `Apps in ChatGPT`, `https://help.openai.com/en/articles/11487775-connectors-in-chatgpt`, accessed 2026-07-07.

Repository-local evidence:

- PR #133, `Add Claude conversation capability settings guide`, created through a ChatGPT ordinary GitHub app workflow and merged into `master`.

## Interpretation

Earlier Mnemosyne statements that treated Codex Cloud as the main remote GitHub write assistant can remain historically valid, but any live assumption that ordinary ChatGPT conversations are read-only should now be treated as stale unless scoped to a past date, past product surface, or no-write environment.

This task does not modify `current/human-approved-spec.md`. The guide states that if stale platform-capability statements are found in execution-source files, they should be routed through normal Mnemosyne spec-update or user-decision processes rather than silently edited by an unapproved task.

## Authority / boundary notes

This guide is not execution source.

It does not approve:

- target workspace creation;
- target material ingestion;
- target repository write;
- formal regression conversion;
- operational memory-system build or installation;
- Mnemosyne execution-source updates;
- treating `PASS_WITH_WARNINGS` as production-ready or target-write approval.

Platform permission and Mnemosyne task authority remain separate. A GitHub app permission prompt means ChatGPT may be technically able to perform an action; it is not itself Mnemosyne task authorization.

## Known limitations

- The exact date when GitHub app branch/file/PR write actions became available in ordinary ChatGPT conversations was not established.
- Availability can vary by plan, workspace, model surface, region, app configuration, and user/admin permissions.
- This task does not exhaustively search all historical raw discussion files for stale read-only statements.
- This task did not resume or close the paused post-handoff route.

## Verification notes

- `current/human-approved-spec.md` was not modified.
- `current/active-context.md`, `current/todo.md`, `current/open-questions.md`, and `handoff/handoff-current.md` were not modified.
- No `target-projects/` or `notes/target-project-dry-runs/` files were created.
- The new guide explicitly marks itself as non-execution-source and product-time-sensitive.
