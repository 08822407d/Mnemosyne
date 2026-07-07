# MNEMOSYNE-086 Result Record

```yaml
task_id: MNEMOSYNE-086
task_name: Research and record Claude ordinary-conversation capability settings for Mnemosyne prompt preflight
task_type: non_execution_source_platform_guide
action_actor: ChatGPT_GitHub_tooling_not_Codex
started_from: post_MNEMOSYNE_085_inserted_long_work_context
files_created:
  - notes/platform-guides/README.md
  - notes/platform-guides/claude-conversation-capabilities-and-settings-guide-v0.1.md
  - notes/codex-task-results/MNEMOSYNE-086-result.md
files_modified: []
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

MNEMOSYNE-086 creates a non-execution-source platform guide for future Claude / Fable / Opus ordinary conversation setup in Mnemosyne work.

The guide covers:

- Claude Projects / project knowledge;
- connectors / integrations;
- Research and web search;
- skills;
- plugins;
- artifacts / file output;
- Mnemosyne-specific prompt setup headers;
- recommended settings for cross-model review, product capability research, manual input-pack review, and repository writing boundaries;
- recommended storage and ingestion paths for Claude outputs.

## Source basis

The guide was based on current public Claude / Anthropic product documentation and pages available on 2026-07-07, including:

- Anthropic Projects announcement: `https://www.anthropic.com/news/projects`
- Claude Research announcement: `https://claude.com/blog/research`
- Claude Integrations announcement: `https://claude.com/blog/integrations`
- Claude Connectors directory: `https://claude.com/connectors`
- Claude Skills page: `https://claude.com/skills`
- Claude Code Skills docs: `https://code.claude.com/docs/en/skills`
- Claude Code Plugins docs: `https://code.claude.com/docs/en/plugins`
- Claude Artifacts announcement: `https://claude.com/blog/artifacts`

Product features, availability, plan gating, UI labels, and connector behavior are time-sensitive and require future verification before high-risk use.

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

The guide recommends that future Claude-facing prompts include explicit setup headers and require repository-access self-checks with exact quotes before Claude claims direct repository access.

## Known limitations

- The guide records current public product understanding, not guaranteed future Claude behavior.
- Some Claude UI settings can vary by plan, region, workspace policy, and product surface.
- The guide was created in a branch and should be reviewed before merge.
- This task did not ingest Fable review outputs, did not create a cross-model review result directory, and did not resume or close the paused post-handoff route.

## Verification notes

- `current/human-approved-spec.md` was not modified.
- `current/active-context.md`, `current/todo.md`, `current/open-questions.md`, and `handoff/handoff-current.md` were not modified.
- No `target-projects/` or `notes/target-project-dry-runs/` files were created.
- The created guide explicitly marks itself as non-execution-source and product-time-sensitive.
