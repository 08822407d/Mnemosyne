# FABLE5-GREENFIELD-001 Maintainer-Triage Model-Quality Restart Checkpoint

> Non-execution-source operational checkpoint. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
checkpoint_id: FABLE5-GREENFIELD-001-MODEL-QUALITY-RESTART-001
created_by_task: MNEMOSYNE-144
record_type: user_confirmed_model_quality_restart_checkpoint
authority_level: non_execution_source_user_instruction_and_wayfinding
recorded_at: 2026-07-21
repository: 08822407d/Mnemosyne
trusted_repository_baseline:
  pull_request: 194
  pull_request_title: MNEMOSYNE-143 preserve Fable GF-STEP-5 result
  merged: true
  merge_commit: 12f2a00fa746485dcdbb99e2c6569549e894f0c0
  master_identical_to_merge_commit_at_checkpoint_creation: true
trusted_work_scope:
  through: merge_of_PR_194
  includes:
    - FABLE5-GREENFIELD-001 independent design steps through GF-STEP-5
    - staged Fable task preparation under the existing conversation
    - receipt, integrity checking, storage-only preservation, and PR creation through MNEMOSYNE-143
    - user review and merge of PR 194
  user_assessment: no_known_intelligence_level_problem_before_or_at_this_baseline
reported_model_context_before_baseline:
  user_reported_selection_or_label: gpt5.6sol thinking very high
  use_of_model: execute_pre_designed_staged_Fable_workflow_and_storage_only_result_handling
  backend_model_identity_independently_verified: false
  interpretation: user_confirmed_operational_confidence_not_backend_attestation
post_baseline_intended_model_switch:
  target_selection: GPT Pro
  known_risk_reported_by_user: official_entry_may_show_Pro_while_a_less_deliberative_or_5.5_instant_like_model_appears_to_take_over
```

## 1. Purpose

This checkpoint records the user's explicit trust boundary before switching the current conversation to GPT Pro for the maintainer-triage work that follows the completed Fable greenfield comparison.

The user considers the work through the successful merge of PR #194 trustworthy with respect to model intelligence level. During that interval, the conversation was reportedly using `gpt5.6sol thinking very high` and was mainly executing already-designed, bounded steps: issuing staged Fable tasks, receiving the outputs, checking and preserving them, creating storage PRs, and waiting for the user to merge those PRs.

This record does not claim that the platform backend model can be independently proven from a UI label, self-report, or observed behavior. It records the user's operational judgment and the repository baseline to use if a later model-quality incident is declared.

## 2. Trusted restart baseline

The trusted restart point is:

```text
master@12f2a00fa746485dcdbb99e2c6569549e894f0c0
```

This is the merge commit of PR #194. It includes the completed and stored FABLE5-GREENFIELD-001 independent-design and bounded-comparison track through GF-STEP-5.

The Fable design steps and their stored artifacts through this commit are not to be redone merely because a later Pro-switch incident is reported. They remain the trusted input baseline unless the user separately and explicitly says that a pre-PR-194 artifact itself is invalid.

## 3. Incident trigger semantics

This checkpoint becomes active only when the user explicitly communicates both of the following meanings, using any reasonably equivalent wording:

1. after switching to Pro, the conversation's intelligence level or actual model behavior appears wrong, unexpectedly shallow, `5.5急速`-like, or otherwise inconsistent with the intended Pro-quality work; and
2. work should restart from the last known-correct point, the correct time point, the pre-switch point, or the PR #194 baseline.

Examples of activating language include:

- `在切换到 Pro 后发现智能程度出现问题，需要从正确的时间点重新开始`;
- `Pro 实际上好像被急速模型接管了，从 PR194 之后重做`;
- another explicit statement carrying the same two meanings.

A generic disagreement with an answer, a request for more detail, or dissatisfaction without a restart instruction does not automatically activate this checkpoint.

## 4. Required behavior when activated

When the trigger is activated, the receiving model or conversation must:

1. treat `master@12f2a00fa746485dcdbb99e2c6569549e894f0c0` as the last user-confirmed model-quality baseline;
2. preserve all Git history and records—do not rewrite or erase later work;
3. identify all substantive work initiated after that baseline, especially:
   - GPT Pro substantive adjudication or maintainer triage;
   - research-topic selection or research execution;
   - bounded repair-task preparation;
   - execution-source change proposals;
   - any repository PRs, merges, decisions, or status changes derived from those activities;
4. mark post-baseline work as `requires_reassessment_due_to_declared_model_quality_incident` until reviewed;
5. restart the maintainer-triage reasoning from the trusted GF-STEP-5 input state, rather than continuing from potentially affected conclusions;
6. inspect any post-baseline repository changes before deciding whether to retain, supersede, revert through a new reviewed change, or redo them;
7. require the user's normal authorization for new repository writes, merges, research, repairs, or execution-source changes;
8. avoid re-running Fable GF-STEP-1 through GF-STEP-5 unless the user separately authorizes that broader rollback.

## 5. Scope of redo

Default redo scope after activation:

```yaml
redo_scope:
  starts_after: merge_commit_12f2a00fa746485dcdbb99e2c6569549e894f0c0
  primary_work_to_redo:
    - maintainer_triage_of_GF_STEP_5
    - substantive_adjudication_started_after_the_baseline
    - downstream_research_or_repair_route_selection_based_on_that_adjudication
  trusted_and_not_redone_by_default:
    - Fable_greenfield_outputs_through_GF_STEP_5
    - MNEMOSYNE_storage_records_through_MNEMOSYNE_143
    - merged_PR_194_contents
```

If later work was only mechanical storage with independently verified byte identity, the incident review may preserve it after explicit inspection. If later work involved judgment, prioritization, acceptance/rejection, task design, or architectural changes, it should be redone from the baseline unless the user explicitly narrows the redo scope.

## 6. Current next gate

At this checkpoint, the Fable independent-design and comparison mainline is complete. The next work is separate maintainer triage, potentially using GPT Pro. No triage route is selected or executed by this checkpoint.

```yaml
next_gate:
  baseline_input: stored_GF_STEP_5_report_at_PR_194
  intended_route: GPT_Pro_substantive_adjudication_or_other_user_selected_maintainer_triage
  started_by_this_record: false
  substantive_acceptance: not_performed
  research_started: false
  repair_task_generated: false
```

## 7. Boundary statement

This record is not an execution source, backend-model attestation, model-version proof, substantive adjudication, or repair authorization. It does not declare that a model incident has occurred. It records the user's trusted baseline and the interpretation to apply only if the user later explicitly declares a post-switch model-quality problem and requests restart from the correct point.

It does not modify `current/human-approved-spec.md`, accept Fable findings, select research, generate repairs, authorize target work, merge a PR, or enable auto-merge.
