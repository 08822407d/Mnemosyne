# Meta-Agent Dedicated Repository Migration Preparation — Superseded Startup Prompt

> Historical startup prompt for the combined Pro task. The task was executed once and correctly stopped with `BLOCKED_INCOMPLETE_REPOSITORY_ENUMERATION` because the selected GitHub connector could not prove recursive tree/blob closure. Do not run this prompt again on the same surface.

```yaml
original_task_id: META-AGENT-DEDICATED-REPOSITORY-MIGRATION-PREPARATION-001
execution_result: BLOCKED_INCOMPLETE_REPOSITORY_ENUMERATION
result_ref: notes/codex-task-results/META-AGENT-DEDICATED-REPOSITORY-MIGRATION-PREPARATION-001-blocked-result.md
adjudication_ref: notes/adjudications/meta-agent-migration-preparation-enumeration-blocker-adjudication-2026-08-06.md
superseded_by:
  E0:
    task_id: META-AGENT-DEDICATED-REPOSITORY-MECHANICAL-INVENTORY-001
    prompt: handoff/meta-agent-dedicated-repository-mechanical-inventory-codex-startup-prompt.md
  E1:
    task_id: META-AGENT-DEDICATED-REPOSITORY-MAPPING-RESUME-001
    prompt: handoff/meta-agent-dedicated-repository-mapping-resume-startup-prompt.md
```

## Current operator route

1. Run E0 on OpenAI Codex Code mode or an equivalent complete local Git checkout.
2. Human-review and merge the one E0 Mnemosyne PR.
3. Run E1 in the dedicated Meta-Agent GPT Pro conversation.
4. E1 must reuse the merged E0 manifest and must not repeat full recursive enumeration unless identity verification fails.
5. Neither phase may write or initialize `08822407d/Meta-Agent`.

The original combined taskbook remains in Git history and may be consulted for design context, but it is no longer the runnable entrypoint.
