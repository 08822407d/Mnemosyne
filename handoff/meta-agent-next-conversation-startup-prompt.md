# Meta-Agent Next Conversation Startup Prompt

Use this prompt in a new ChatGPT conversation after MNEMOSYNE-083.

Repository: `08822407d/Mnemosyne`

## Required first checks
Before proposing any task, read or ask the user to provide/fetch these repository files:

```text
current/human-approved-spec.md
current/active-context.md
current/todo.md
current/open-questions.md
handoff/handoff-current.md
handoff/meta-agent-post-079-phase-closure-handoff-package.md
notes/codex-task-results/MNEMOSYNE-082-result.md
notes/codex-task-results/MNEMOSYNE-083-result.md
```

## Current known state
```yaml
completed_through: MNEMOSYNE-083
MNEMOSYNE_079: dry_run_result_ingested
MNEMOSYNE_080: post_079_state_residue_repaired
MNEMOSYNE_081: pre_handoff_stabilization_roadmap_and_regression_candidate_triage_created
MNEMOSYNE_082: phase_closure_recorded_and_baseline_frozen
MNEMOSYNE_083: official_handoff_package_and_startup_prompt_created
```

## Current baseline
```yaml
phase: post_first_controlled_no_target_write_dry_run
phase_closed_for_handoff_preparation: true
dry_run_id: META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001
verdict: PASS_WITH_WARNINGS
score: 89/100
critical_blockers: []
evidence_status: current_non_execution_source_evidence_baseline
regression_candidates_status: triaged_candidates_only
target_workspace_created: false
target_materials_ingested: false
target_repository_written: false
operational_memory_system_installed: false
execution_source_modified: false
```

## Critical task-number guard
Do not propose MNEMOSYNE-080, MNEMOSYNE-081, or MNEMOSYNE-082 as next tasks. They are already complete.

After validating MNEMOSYNE-083, the only possible immediate next task number is MNEMOSYNE-084, and only if post-083 residue repair or handoff correction is needed.

## Hard prohibitions
- Do not create `target-projects/meta-agent/`.
- Do not create `notes/target-project-dry-runs/`.
- Do not ingest target materials.
- Do not request raw materials.
- Do not write any target repository.
- Do not formalize regression candidates.
- Do not build or install an operational Meta-Agent memory system.
- Do not modify `current/human-approved-spec.md`.
- Do not treat PASS_WITH_WARNINGS as production-ready or target-write approval.
- Do not treat handoff/current/task result/research files as execution source.

## First response requirement
Your first response should:
1. confirm that MNEMOSYNE-083 is the completed handoff baseline if repository evidence supports it;
2. state whether any post-083 residue repair is needed;
3. propose MNEMOSYNE-084 only if repair is needed;
4. otherwise ask the user which post-handoff path to choose later, without creating workspace/material/write/build tasks.
