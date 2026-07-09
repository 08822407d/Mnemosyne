# MNEMOSYNE-099 — Higher-Model Q2-2 / R3 Decision Package

```yaml
package_id: MNEMOSYNE-099-HIGHER-MODEL-Q2-2-R3-DECISION-PACKAGE
created_by_task: MNEMOSYNE-099
authority_level: non_execution_source_review_package
intended_execution_location:
  - future_higher_reasoning_ChatGPT_conversation
  - restored_Pro_quota_context
  - GPT-5.6_or_later_if_available
not_intended_for:
  - immediate_low_strength_canonicalization
  - Codex_Cloud_execution
  - automatic_repository_repair
```

## 1. Purpose

This package prepares a future higher-strength review of the remaining Fable follow-up issues after MNEMOSYNE-097.

It is deliberately a **decision package**, not a decision record. It does not choose a canonical warning layer, approve R3 cleanup, update execution source, generate a Codex task, or resume/close the paused post-handoff route.

## 2. Required repository evidence to read

Read these files first:

```text
current/human-approved-spec.md
commands/load-mnemosyne-guidance.md
notes/chatgpt-github-write-preflight-checklist.md
notes/cross-model-review-results/README.md
notes/cross-model-review-results/FABLE5-TRIAGE-001/manifest.yaml
notes/cross-model-review-results/FABLE5-TRIAGE-001/01-fable-response-after-human-answers-summary.md
notes/cross-model-review-results/FABLE5-TRIAGE-001/raw/00-raw-preservation-manifest.yaml
notes/cross-model-review-results/FABLE5-TRIAGE-001/evidence-audits/MNEMOSYNE-097-q2-2-r3-readonly-audit.md
notes/codex-task-results/MNEMOSYNE-095-result.md
notes/codex-task-results/MNEMOSYNE-096-result.md
notes/codex-task-results/MNEMOSYNE-097-result.md
notes/codex-task-results/MNEMOSYNE-098-result.md
```

For Q2-2 evidence verification, also read:

```text
notes/first-target-project-intake-records/meta-agent/controlled-dry-run-results/META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001-result.md
notes/first-target-project-intake-records/meta-agent/controlled-dry-run-results/META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001-maintainer-review.md
notes/first-target-project-intake-records/meta-agent/meta-agent-post-079-baseline-freeze-for-handoff-v0.1.md
handoff/meta-agent-post-079-phase-closure-handoff-package.md
notes/codex-task-results/MNEMOSYNE-082-result.md
notes/codex-task-results/MNEMOSYNE-083-result.md
```

For R3 recheck / repair-proposal planning, also read:

```text
notes/cross-model-review-results/FABLE5-REVIEW-001/manifest.yaml
notes/cross-model-review-results/FABLE5-REVIEW-002/manifest.yaml
notes/cross-model-review-results/FABLE5-REVIEW-003/manifest.yaml
notes/codex-task-results/MNEMOSYNE-091-result.md
manual-import-inbox/README.md
current/active-context.md
current/todo.md
handoff/handoff-current.md
```

## 3. Known state from MNEMOSYNE-097

```yaml
mnemosyne_097_known_state:
  q2_2:
    evidence_table_completed: true
    canonical_layer_selected: false
    status: open
    priority: high
    tension:
      pro_version_rule: favors_maintainer_review_layer_but_only_indirectly
      latest_version_rule: favors_freeze_package_layer
      frozen_artifact_discipline: favors_not_modifying_082_083_frozen_artifacts
  r3:
    R3-F-001:
      current_residue_found: false
      reason: current FABLE5 manifests do not show the stale line; stale coexistence remains historical in MNEMOSYNE-091 result only
    R3-F-003:
      current_residue_found: partially_yes
      reason: manual-import transfer artifacts remain but MNEMOSYNE-091 documents intentional retention
      user_decision_needed: label_delete_or_leave
    R3-F-004:
      current_residue_found: likely_yes
      reason: no live-file pointer to cross-model review tree found in checked live files
```

## 4. Higher-model review questions

### 4.1 Q2-2 canonical warning-layer question

Do **not** assume that one layer must replace all others. Evaluate whether the correct output is one of:

```yaml
q2_2_possible_outcomes:
  A_single_canonical_warning_layer:
    description: choose either maintainer-review layer or freeze/package layer as the canonical warning list for future audits
    risk: may conflict with either Pro-version rule, latest-version rule, or frozen-artifact discipline
  B_layered_canonicalization:
    description: define each layer's role without rewriting frozen artifacts
    possible_mapping:
      source_layer: dry-run original warning source and model-origin evidence
      maintainer_review_layer: acceptance-gate/provenance-preserving review layer
      freeze_package_layer: handoff-carry baseline layer
      live_annotation_layer: future lightweight pointer/clarification if approved
    risk: may be more complex but may avoid false single-source collapse
  C_defer_for_user_rule_clarification:
    description: ask user to resolve Pro-version vs latest-version vs frozen-artifact priority explicitly
    risk: delays repair but avoids model overreach
```

The review should decide only whether a recommendation is now evidence-supported. It must not edit files by itself.

### 4.2 R3 repair proposal split

Evaluate whether the later repair proposal, if any, should split R3 items as:

```yaml
r3_possible_split:
  R3-F-001:
    likely_action: no_current_repair
    rationale: current manifests no longer show stale line
  R3-F-003:
    decision_type: user_preference
    choices:
      - leave transfer artifacts with MNEMOSYNE-091 explanation
      - add per-file superseded/processed markers
      - delete processed transfer copies
  R3-F-004:
    decision_type: low_scope_live_pointer_repair_candidate
    choices:
      - add one pointer in a live/index file to notes/cross-model-review-results/FABLE5-TRIAGE-001/
      - leave discoverability through notes/cross-model-review-results/README.md and result records only
```

## 5. Required higher-model output format

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

## 6. Boundaries

The reviewer must not:

- treat Fable review as truth voting;
- treat this package as execution source;
- update `current/human-approved-spec.md`;
- modify frozen 082/083 artifacts unless a later task explicitly approves a scoped annotation strategy;
- create target workspace/material/write/build/regression artifacts;
- resume or close the paused post-handoff route;
- generate a Codex task unless the user/current maintenance conversation explicitly routes to repair execution.
