# Regression Candidate Triage v0.1 — META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001

## Positioning

- Non-execution-source triage record.
- Based on `META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001-regression-candidate-summary.md`.
- Does not create executable regression tests.
- Does not promote target-specific findings into Mnemosyne global execution source.

## Triage summary

```yaml
formalize_now: false
recommended_before_handoff: triage_only
recommended_after_handoff:
  - consider_formalizing_selected_candidates
  - preserve_target_specific_scope
  - require_user_approval_before_globalization
```

## Candidate triage table

```yaml
candidates:
  - test_id: REG-META-DRYRUN-001
    topic: approval_chain_recovery
    priority: high
    recommended_timing: early_after_handoff
    reason: approval-chain ambiguity was an explicit dry-run warning and may recur in future controlled runs.
    target_specific: true
    global_candidate: possible_after_more_evidence
    formalize_before_handoff: false

  - test_id: REG-META-DRYRUN-002
    topic: no_target_write_evidence_when_git_diff_unavailable
    priority: high
    recommended_timing: early_after_handoff
    reason: equivalent no-write evidence was accepted for this run; future runs should standardize proof handling.
    target_specific: false
    global_candidate: likely
    formalize_before_handoff: false

  - test_id: REG-META-DRYRUN-003
    topic: safe_input_policy
    priority: medium_high
    recommended_timing: after_handoff_if_material_phase_considered
    reason: no materials were ingested in this run, but future material phases depend on this boundary.
    target_specific: partly
    global_candidate: possible
    formalize_before_handoff: false

  - test_id: REG-META-DRYRUN-004
    topic: target_runtime_truth_source_non_invention
    priority: high
    recommended_timing: early_after_handoff
    reason: target runtime truth source remains unresolved and should not be invented by future conversations.
    target_specific: partly
    global_candidate: likely
    formalize_before_handoff: false

  - test_id: REG-META-DRYRUN-005
    topic: non_execution_source_contamination
    priority: high
    recommended_timing: early_after_handoff
    reason: large numbers of non-execution-source support files now exist and future conversations must not overpromote them.
    target_specific: false
    global_candidate: likely
    formalize_before_handoff: false

  - test_id: REG-META-DRYRUN-006
    topic: feedback_to_methodology_gate
    priority: medium
    recommended_timing: after_more_meta_agent_feedback
    reason: important for Meta-Agent methodology, but there is not yet enough real feedback to formalize.
    target_specific: true
    global_candidate: possible_later
    formalize_before_handoff: false

  - test_id: REG-META-DRYRUN-007
    topic: pass_semantics
    priority: high
    recommended_timing: early_after_handoff
    reason: PASS_WITH_WARNINGS must not become production-ready / write approval / execution-source update.
    target_specific: false
    global_candidate: likely
    formalize_before_handoff: false
```

## Recommended next handling

```yaml
next_handling:
  phase_closure: keep_all_as_candidates_pending_review
  handoff: include_triage_summary
  after_handoff:
    first_batch_to_consider:
      - REG-META-DRYRUN-001
      - REG-META-DRYRUN-002
      - REG-META-DRYRUN-004
      - REG-META-DRYRUN-005
      - REG-META-DRYRUN-007
```

## Boundary

Do not formalize these candidates or promote them into global Mnemosyne rules before a later explicit user decision.
