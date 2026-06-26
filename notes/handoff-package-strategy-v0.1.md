# Handoff Package Strategy v0.1

## Positioning

- This file is a non-execution-source operational strategy.
- It guides handoff package generation and selection.
- It does not override `current/human-approved-spec.md`.
- If this file conflicts with the execution source, follow the execution source and record an open question.
- Research basis: `RPT-2026Q2-HO-0001`.
- Token ranges are target guidance, not hard compliance limits.

## 1. Correct-handoff objective

A handoff package should be the smallest task-appropriate, high-signal package that allows a fresh receiving session to recover current truth, authority, boundaries, current task intent, and one safe next action without relying on unverified old context.

A longer package is not automatically safer. A package is defective when it preserves large amounts of history but obscures or contradicts execution source, current gate, live state, authority, or forbidden actions.

## 2. Common mandatory fields

Every handoff package should contain or provide a path to:

```yaml
handoff_package_common:
  package_id:
  package_tier: minimum | standard | extended
  status: active_non_execution_source_handoff
  generated_at:
  source_conversation_or_task:
  intended_receiver:
  repository_or_project_ref:
  execution_source_or_owner_rule:
  current_phase_or_stage:
  current_gate_if_any:
  current_task_intent:
  live_truths:
  completed_vs_pending:
  authorities_and_required_approvals:
  forbidden_actions:
  one_safe_next_action:
  unsupported_assumptions:
  stale_or_conflicting_items:
  evidence_map:
  explicitly_excluded:
```

For Mnemosyne itself:

```yaml
execution_source_or_owner_rule:
  path: current/human-approved-spec.md
  status: only_execution_source
```

For a target project, use the target's own confirmed execution source or owner rule. If unknown, record `unknown_requires_owner_decision`.

## 3. Tier selection

### 3.1 Minimum handoff package

Use for:

- ordinary low-risk continuation;
- same project and stable workflow;
- no known stale-state or authority dispute;
- no model/tool migration diagnosis.

Target length guidance:

```text
approximately 250–500 tokens
```

Required content:

```yaml
minimum_handoff_package_v0.1:
  package_id:
  status: active_non_execution_source_handoff
  source_conversation_or_task:
  intended_receiver:
  repository_ref_or_commit:
  visible_model_or_tool_if_known:
  generated_at:

  execution_source_or_owner_rule:
  current_phase:
  current_gate:
  live_truths:
  current_task_intent:
  one_safe_next_action:

  non_execution_boundaries:
  required_user_decisions:
  forbidden_actions:
  unsupported_assumptions:

  evidence_map:
    - claim:
      path:
      authority_level:
      freshness_note:

  explicitly_excluded:
    - full_conversation_export
    - raw_diff_body
    - full_result_record_copy
    - speculative_future_design
```

Escalate to standard if authority, completed/pending state, missing files, Codex execution, or multiple actors must be tracked.

### 3.2 Standard handoff package

Use for:

- Mnemosyne maintenance;
- ordinary ChatGPT → Codex task;
- Codex result → ordinary verification;
- replay review;
- first-target dry-run preparation;
- repository-backed work with explicit permissions.

Target length guidance:

```text
approximately 700–1500 tokens
```

Required content:

```yaml
standard_handoff_package_v0.1:
  package_id:
  status: active_non_execution_source_handoff
  handoff_scope:
  source_conversation_or_task:
  target_conversation_or_task:
  repository_ref_or_commit:
  generated_at:

  provenance:
    tool_or_interface:
    visible_model_label:
    reasoning_effort_if_visible:
    memory_or_history_setting: off | on | unknown
    hidden_prior_context_expected: yes | no | unknown
    files_available:
    files_read:
    limitations:

  read_order:
  execution_source_or_owner_rule:
  current_state:
    current_phase:
    current_gate:
    live_truths:
    current_priority:
    current_task_intent:

  completed_recently:
    - item:
      consequence_for_current_state:
      authority_level:

  still_pending:
    - item:
      why_pending:
      who_can_close_it:

  authorities_and_permissions:
    user_must_approve:
    ordinary_conversation_can:
    ordinary_conversation_cannot:
    codex_or_write_agent_can:
    codex_or_write_agent_cannot:

  forbidden_actions:
  stale_or_conflict_items:
  unsupported_assumptions:
  missing_files_or_access_limits:

  one_safe_next_action:

  evidence_map:
    - claim:
      evidence_path:
      authority_level:
      freshness_note:

  explicitly_excluded:
    - full_old_export_default_import
    - full_raw_diff_embed
    - research_report_as_execution_source
    - hidden_platform_memory_as_truth
```

### 3.3 Extended handoff package

Use only for:

- model-family or tool migration;
- post-failure recovery;
- stale Codex branch diagnosis;
- cross-tool transfer with materially different capabilities;
- old-conversation contamination investigation;
- high-risk authority or source conflict.

Target length guidance:

```text
approximately 1500–3000 tokens
```

Extended package = standard package plus:

```yaml
extended_handoff_package_v0.1:
  escalation_reason:
  validated_execution_source_snapshot:
  stale_conflict_ledger:
  event_timeline:
  selected_historical_excerpts:
  codex_or_agent_transition_notes:
  privacy_and_sensitivity:
  failure_recovery_plan:
  verification_plan:
```

Historical excerpts must be selected, labeled, and scoped:

```yaml
selected_historical_excerpt:
  excerpt_id:
  source_type:
  current_truth_status: non_current_example_only
  relevance:
  contamination_risk:
  evidence_path:
```

Do not use the extended tier merely because a conversation is long.

## 4. Generation rules

1. Generate from current authorized files, not from conversational memory alone.
2. Identify the applicable execution source or owner rule first.
3. Separate current truth from historical context.
4. Separate completed work from pending work.
5. Record approvals and actor permissions explicitly.
6. Include one safe next action, not an unbounded roadmap.
7. Add path-level evidence for critical claims.
8. Mark stale/conflicting/unknown items rather than resolving them by invention.
9. Prefer pointers and selected excerpts over full duplication.
10. Before forwarding long packages, apply the long-transfer file/chunking rule.
11. Re-generate or revalidate a package after changes to execution source, current gate, critical protocol semantics, or target authority.

## 5. Package validity

A package becomes stale when any of these changes:

- execution source;
- current phase/gate;
- critical live truths;
- user approvals or authority;
- target project selection;
- protocol version;
- repository ref where the package claims exact repository state.

A stale package may remain as historical evidence but must not be reused as active handoff without review.

## 6. Relationship to replay

Handoff generation and replay evaluation are separate responsibilities.

- This file guides package generation.
- `notes/handoff-replay-scorecard-v0.1.md` guides reviewer evaluation.
- The tested receiving session does not approve its own final gate closure.
- A maintainer/reviewer checks the output against latest authorized sources.

## 7. Non-goals

This strategy does not create:

- automatic handoff generation;
- automatic writeback;
- automatic gate closure;
- AGENTS.md / CLAUDE.md;
- GitHub Actions;
- MCP / RAG;
- cross-model threshold calibration.
