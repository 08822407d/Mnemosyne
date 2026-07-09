# MNEMOSYNE-100 — Higher-Model Transfer Prompt

```yaml
prompt_id: MNEMOSYNE-100-HIGHER-MODEL-TRANSFER-PROMPT
created_by_task: MNEMOSYNE-100
authority_level: non_execution_source_transfer_prompt
intended_recipient:
  - future_higher_reasoning_ChatGPT_conversation
  - restored_Pro_quota_conversation
  - GPT-5.6_or_later_if_available
purpose: execute_review_package_MNEMOSYNE_099_without_relying_on_prior_chat_context
```

## Prompt to send

```markdown
Load Mnemosyne guidance as behavior guidance only. Do not import the paused maintenance live route as this conversation's task unless explicitly instructed later.

We are continuing the Mnemosyne Fable 5 follow-up review track. The immediate task is to review the non-execution-source MNEMOSYNE-099 decision package for Q2-2 and R3. Do not write repository files. Do not generate Codex tasks. Do not update execution source. Do not create target workspace/material/write/build/regression artifacts. Do not resume or close the paused post-handoff route.

Repository:

```text
08822407d/Mnemosyne
```

First read:

```text
current/human-approved-spec.md
commands/load-mnemosyne-guidance.md
notes/chatgpt-github-write-preflight-checklist.md
notes/cross-model-review-results/README.md
notes/cross-model-review-results/FABLE5-TRIAGE-001/manifest.yaml
notes/cross-model-review-results/FABLE5-TRIAGE-001/01-fable-response-after-human-answers-summary.md
notes/cross-model-review-results/FABLE5-TRIAGE-001/raw/00-raw-preservation-manifest.yaml
notes/cross-model-review-results/FABLE5-TRIAGE-001/evidence-audits/MNEMOSYNE-097-q2-2-r3-readonly-audit.md
notes/cross-model-review-results/FABLE5-TRIAGE-001/review-packages/MNEMOSYNE-099-higher-model-q2-r3-decision-package.md
notes/codex-task-results/MNEMOSYNE-095-result.md
notes/codex-task-results/MNEMOSYNE-096-result.md
notes/codex-task-results/MNEMOSYNE-097-result.md
notes/codex-task-results/MNEMOSYNE-098-result.md
notes/codex-task-results/MNEMOSYNE-099-result.md
```

Then inspect any additional files named by the MNEMOSYNE-099 package if needed.

Your task:

1. Verify that the MNEMOSYNE-099 package has enough evidence for higher-model review.
2. Evaluate Q2-2 using the options in MNEMOSYNE-099:
   - single canonical warning layer;
   - layered canonicalization;
   - defer for explicit user rule clarification.
3. Evaluate R3:
   - R3-F-001 current repair need;
   - R3-F-003 leave vs mark superseded vs delete vs ask user;
   - R3-F-004 add live pointer vs no pointer vs ask user.
4. Produce only an advisory recommendation. Do not write files or generate tasks.

Required output:

```yaml
higher_model_decision_response:
  repository_access:
    status: accessed | partial | not_accessed
    files_checked:
      - path
    missing_files:
      - path
  q2_2_recommendation:
    decision_status: recommend_now | defer_for_user_rule | defer_for_stronger_evidence
    recommended_model:
      type: single_layer | layered_canonicalization | no_change
      details: text
    should_modify_frozen_082_083_artifacts: false
    recommended_recording_location:
      - path_or_none
    rationale:
      - point
    unresolved_risks:
      - point
  r3_recommendation:
    R3-F-001:
      recommended_action: no_action | repair | defer
      rationale: text
    R3-F-003:
      recommended_action: leave | mark_superseded | delete | ask_user
      rationale: text
    R3-F-004:
      recommended_action: add_pointer | no_pointer | ask_user | defer
      rationale: text
  repair_bundle_advice:
    generate_repair_task_now: true_or_false
    if_true_minimal_paths:
      - path
    if_false_reason: text
  boundary_statement: >
    This response is advisory only. It does not itself authorize repository
    writes, execution-source updates, target workspace/material/write/build/
    regression work, auto-merge, or paused-route resumption.
```
```

## Boundary

This prompt is not execution source. It does not authorize repository writes, repair tasks, execution-source updates, Codex Cloud tasks, target workspace/material/write/build/regression actions, auto-merge, or paused-route resumption.
