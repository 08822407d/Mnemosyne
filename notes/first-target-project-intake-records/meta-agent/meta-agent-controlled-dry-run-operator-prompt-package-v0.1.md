# Meta-Agent Controlled No-Target-Write Dry-Run Operator Prompt Package v0.1

## Positioning

- Non-execution-source prompt package.
- Do not execute unless the user later explicitly approves actual controlled dry-run execution.
- This package is prepared in advance only.
- It must be run in a separate high-reasoning conversation only if later approved.
- It must not be executed in Codex Cloud.

## Execution precondition

```yaml
execute_only_if:
  actual_controlled_dry_run_execution_approved_by_user: true
  approved_execution_record_path:
  operator_no_target_write_confirmation: true
  allowed_input_list_reviewed: true
  prohibited_actions_reviewed: true
```

## Prompt to use later if explicitly approved

```markdown
加载 Mnemosyne 指导约束。

你正在执行 Meta-Agent controlled no-target-write real-target evaluation / design-package generation dry-run。

执行位置：new high-reasoning ChatGPT conversation, not Codex Cloud.

Repository context: `08822407d/Mnemosyne`.

You must read the approved execution record and these support files if accessible:

- `current/human-approved-spec.md`
- `notes/first-target-project-intake-records/meta-agent/meta-agent-final-run-manifest-candidate-v0.1.md`
- `notes/first-target-project-intake-records/meta-agent/meta-agent-controlled-dry-run-preparation-plan-v0.1.md`
- `notes/first-target-project-intake-records/meta-agent/meta-agent-controlled-dry-run-evidence-and-no-write-proof-plan-v0.1.md`
- `notes/first-real-target-dry-run-evaluation-framework-v0.1.md`
- `notes/first-real-target-dry-run-scorecard-v0.1.md`
- `notes/first-real-target-dry-run-postmortem-template.md`
- `notes/mnemosyne-regression-test-record-template.md`

Hard prohibitions:

- Do not write any repository.
- Do not create `target-projects/meta-agent/`.
- Do not create `notes/target-project-dry-runs/`.
- Do not ingest target materials.
- Do not request raw materials.
- Do not write target repository.
- Do not install an operational Meta-Agent memory system.
- Do not modify Mnemosyne execution source.
- Do not claim production-ready status.

Expected output:

- offline Meta-Agent memory-system design package;
- authority/source map;
- safe-input policy;
- handoff/delivery drafts;
- evidence map;
- assumption log;
- postmortem draft;
- regression candidate list;
- no-write evidence statement.

Final response must include a downloadable Markdown file if available, or chunked Markdown if file generation is unavailable.
```
