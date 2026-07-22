# MNEMOSYNE-149 PR Finalization

> Pull-request binding and single-merge-target record. This file is not execution source; `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
record_type: result_record_PR_finalization
task_id: MNEMOSYNE-149
canonical_PR_number: 200
canonical_branch: mnemosyne-149-repair-run-context-provenance-v0-2
base_branch: master
pinned_base_sha: 96244617606f2a7afe3c1f0451438720df9f3307
initial_content_commit: 21e8eadd4f5973ae63b890b80feaec7eba10f828
draft: true
auto_merge_enabled: false
parallel_variant_authorized: false
related_open_PRs:
  - 200
other_related_open_PRs: []
closed_or_superseded_related_PRs: []
exactly_one_merge_target: true
execution_source_modified: false
checkpoint_activated: false
```

## Duplicate-lineage checks

Before remote branch creation and again immediately before PR creation:

- accessible open-PR enumeration returned no open PR;
- exact `MNEMOSYNE-149` search returned no task-ID match;
- two search false positives, PR #94 and PR #139, contained `149` only as a line count;
- equivalent-scope search returned no open PR;
- the intended branch was absent before branch creation and was the already-designated canonical branch before PR creation;
- remote `master` remained `96244617606f2a7afe3c1f0451438720df9f3307`;
- the canonical branch was ahead by one commit and behind by zero before PR creation.

PR #200 is the only canonical lineage and merge target for MNEMOSYNE-149.

## Pre-finalization branch comparison

```yaml
branch_compare:
  base: master@96244617606f2a7afe3c1f0451438720df9f3307
  head: mnemosyne-149-repair-run-context-provenance-v0-2@21e8eadd4f5973ae63b890b80feaec7eba10f828
  status: ahead
  ahead_by: 1
  behind_by: 0
  changed_files: 7
```

The seven pre-finalization paths were:

- `commands/load-mnemosyne-guidance.md`;
- `current/multi-model-adjudication-provenance-research-status.md`;
- `current/pr198-pro-switch-model-quality-restart-checkpoint.md`;
- `current/run-context-and-pr-provenance-guard.md`;
- `notes/codex-task-results/MNEMOSYNE-149-result.md`;
- `notes/run-context-and-pr-provenance-adoption-record.md`;
- `notes/run-context-and-pr-provenance-v0.2-review-record.md`.

This finalization record is the eighth and final intended path.

## Initial content identity

```yaml
initial_content_blob_manifest:
  commands/load-mnemosyne-guidance.md: 6ffccaeec8bb3e285154c8216985dedcb76b145c
  current/multi-model-adjudication-provenance-research-status.md: ad417fd8f2e4314275d01b63c2a44a4ba8c511c2
  current/pr198-pro-switch-model-quality-restart-checkpoint.md: 366477e8f4c48ef13d231faf106f027a16f7ddbd
  current/run-context-and-pr-provenance-guard.md: 0e588b3f6789d0d941221d33c3eaba1561f6e2a3
  notes/codex-task-results/MNEMOSYNE-149-result.md:
    blob_sha: e3f8dd70db9da6d0b8d077ad144e50d8f4473141
    scope: initial_pre_PR_binding_version
  notes/run-context-and-pr-provenance-adoption-record.md: 2f6848c01d02c13f19e47237fb9213d19d409888
  notes/run-context-and-pr-provenance-v0.2-review-record.md: c114a7710cf1fcf59e1e8f6eab2c78848b83bd4b
```

Git object IDs establish the exact initial content bytes only. They do not establish producer identity, backend identity, correctness, or quality. The result record is intentionally updated after PR creation to bind PR #200.

## Execution context

```yaml
execution_context:
  action_actor: Codex_in_ChatGPT_Work
  product_surface: ChatGPT_Work_mode
  operator_selection_verbatim: unknown_not_reported_or_observed
  provider_normalization_ref: none
  served_model_identifier_status: unknown_or_not_attestable
  review_record_ref: notes/run-context-and-pr-provenance-v0.2-review-record.md
  human_adjudication_status: recorded
  authorization_ref: current_conversation_user_instruction_2026_07_22
  full_run_record: notes/codex-task-results/MNEMOSYNE-149-result.md
```

## Merge instruction

```yaml
merge_instruction:
  task_id: MNEMOSYNE-149
  merge_target_pr: 200
  merge_target_head_branch: mnemosyne-149-repair-run-context-provenance-v0-2
  related_open_prs: []
  closed_or_superseded_related_prs: []
  exactly_one_merge_target: true
  duplicate_preflight_completed: true
  draft: true
  auto_merge: false
```

## Boundary

PR #200 remains a draft for human review. This record does not merge it, mark it ready, enable auto-merge, modify `current/human-approved-spec.md`, rewrite historical v0.1 records, attest a backend, claim heterogeneous-provider review, activate the PR #198 checkpoint, declare an incident, authorize recovery, adjudicate Fable GF-STEP-5, or authorize target-project work.
