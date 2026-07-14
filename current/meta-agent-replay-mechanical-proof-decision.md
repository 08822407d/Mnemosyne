# Meta-Agent Replay Mechanical-Proof Decision

> Non-execution-source live decision record. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
record_type: live_non_execution_source_decision_point
question_id: META-AGENT-REPLAY-MECHANICAL-PROOF-001
created_by_task: MNEMOSYNE-121
status: open_user_decision_required
route: post_handoff_Meta_Agent_test_route
Meta_Agent_product_build_selected: false
execution_source: current/human-approved-spec.md
automatic_Replay_005_authorized: false
```

## 1. Settled evidence

```yaml
settled:
  definition_level_static_replay:
    result: PASS_all_five
  independent_fresh_behavioral_replays:
    Replay_002:
      case_results: PASS_5_of_5
      overall: BLOCKED_mechanical_coverage
    Replay_003:
      case_results: PASS_5_of_5
      overall: BLOCKED_mechanical_coverage
    Replay_004:
      case_results: not_executed
      overall: BLOCKED_precondition_and_master_source_inconsistency
  replicated_behavioral_recovery:
    independent_runs: 2
    five_of_five_in_each: true
  repository_write_detected_in_any_replay: false
  complete_mechanical_no_write_proof_obtained: false
  combined_package_gate_closed: false
```

The five behavior definitions have been recovered correctly in two independent fresh Chat sessions. Replay 004 did not add another behavioral sample because its mandatory before-snapshot prerequisite failed.

## 2. Instrumentation ceiling

Three successive ordinary-Chat attempts show a stable proof-transport limitation:

1. connected GitHub branch enumeration returned no complete branch list;
2. REST response bodies were unavailable in Replay 003;
3. literal user-supplied URLs in Replay 004 produced partial and stale/inconsistent repository state;
4. all-state PR pagination and complete branch-ref coverage were not established.

Therefore another ordinary-Chat retry that only changes URLs, ordering, or wording is not authorized by default. It would repeat the same instrument class without new evidence that the blocker has changed.

## 3. Decision options

### Option A — Accept the behavioral-validation result and pause the operational proof gate

```yaml
option_id: A
recommended: true
result_if_selected:
  behavioral_recovery_subgate: accepted_as_replicated_two_fresh_runs
  mechanical_no_write_subgate: remains_BLOCKED
  combined_package_gate: remains_open
  further_fresh_replay: not_required_now
  Meta_Agent_build_authority: false
```

Use this when the original objective is to learn whether fresh Mnemosyne conversations recover the five boundaries. It avoids spending additional effort on a platform observability problem while preserving that no high-confidence no-write claim was proven.

### Option B — Require a final observer-assisted proof run

```yaml
option_id: B
recommended_when: high_assurance_combined_gate_is_still_valuable
requires:
  - user_controlled_external_observer_or_local_git_environment
  - complete_before_and_after_ref_snapshot
  - complete_relevant_GitHub_metadata_snapshot
  - explicit_run_start_and_end_pairing
  - no_ordinary_Chat_endpoint_cache_as_the_only_proof_source
execution_source_change_required: false
```

A future package would separate roles:

- the fresh Chat performs the behavioral replay;
- an external observer with reliable Git/CLI access captures mechanical before/after evidence;
- the maintenance conversation reviews both artifacts together.

No observer package is generated until the user selects this option and confirms an available local/CLI or equivalent environment.

### Option C — Approve a one-run no-write-proof exception

```yaml
option_id: C
requires_explicit_current_user_approval: true
execution_source_basis: current/human-approved-spec.md#19
not_future_precedent: true
```

Any exception must record the run, why default proof is unavailable, substitute evidence, approver, scope, confidence, human-verification status, and non-precedent status. No such exception is currently approved, and prior DRY-RUN-001 exception evidence cannot be reused automatically.

### Option D — Change the durable proof policy

```yaml
option_id: D
requires_separate_user_approved_execution_source_task: true
current_status: not_selected
```

This would evaluate whether a platform-enforced read-only action surface plus auditable tool logs should become an accepted default proof class. It is a methodology change, not a repair that may be made silently from one target-specific replay series.

## 4. Recommendation

Option A is recommended for the current test-only Meta-Agent route because:

- the user clarified that Meta-Agent is a Mnemosyne test target, not a product to build now;
- two independent fresh sessions already recovered all five behaviors;
- Replay 004 confirms the remaining blocker is instrumentation, not behavioral logic;
- no final package PASS or no-write claim needs to be invented to preserve the useful evidence.

Select Option B only if closing the combined package gate is worth an additional externally observed run.

## 5. Forbidden automatic actions

Until the user selects an option:

- do not generate or execute Replay 005;
- do not reinterpret Replay 002, 003, or 004 as package-level PASS;
- do not approve a run-scoped exception;
- do not modify `current/human-approved-spec.md`;
- do not create a target workspace, ingest materials, access/write a target repository, or build/install Meta-Agent;
- do not resume or take over `FABLE5-GREENFIELD-001`.
