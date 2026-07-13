# Handoff Guidance Loading Scope — Open Question

```yaml
record_type: non_execution_source_open_question
created_by_task: MNEMOSYNE-116
recorded_at: 2026-07-13
execution_source: current/human-approved-spec.md
question_id: OQ-HANDOFF-GUIDANCE-LOAD-001
status: open_requires_careful_review
```

## Settled rule for Mnemosyne handoffs

For a handoff whose receiving task is Mnemosyne maintenance, review, validation, replay, design-factory work, or another Mnemosyne-governed continuation, the handoff package and startup prompt must explicitly require the receiving conversation to execute:

- `Load Mnemosyne guidance`; or
- `加载 Mnemosyne 指导约束`.

This refreshes approved behavior constraints before substantive continuation. It does not replace explicit handoff receive, does not make the handoff package an execution source, and does not import an unrelated maintenance route into a local task.

## Unresolved target-project business-conversation scope

For a handoff between business conversations that belong to a specific target project:

- the receiving conversation should load the target project's own confirmed constraint guidance, execution source, owner rule, or equivalent project-local authority;
- whether it should **also** load Mnemosyne guidance remains undecided and requires careful review.

The unresolved issue is not whether project-local constraints are required; they are. The unresolved issue is whether adding Mnemosyne guidance to a project-business continuation improves governance and memory-system safety or instead introduces unnecessary method-level context and task contamination.

## Temporary handling while unresolved

Until a later user-approved decision closes this question, target-project business handoff packages should record one explicit task-local value:

```yaml
receiver_guidance_load:
  project_guidance: required
  mnemosyne_guidance: yes | no | unknown_requires_user_decision
```

Do not silently assume that Mnemosyne guidance is always required for every project-business conversation. Do not silently omit the question and later claim the scope was decided. A task-local `yes` or `no` does not become a global precedent.

## Decision factors for later review

- whether the receiving task is ordinary project business work or Mnemosyne-governed memory-system design/review;
- whether project-local constraints already incorporate the relevant Mnemosyne-derived safety and authority rules;
- risk of importing unrelated Mnemosyne maintenance context into the project task;
- need for execution-source, provenance, no-write, privacy, handoff, or review-gate controls;
- whether `Load Mnemosyne guidance` can remain behavior-only without changing the project's local task mainline;
- whether separate project and Mnemosyne guidance can conflict, and which owner rule resolves the conflict.

## Boundary

This record is not execution source and does not decide the open project-business scope. It does not authorize target workspace creation, material ingestion, target repository write, operational build, automatic writeback, or any project action.