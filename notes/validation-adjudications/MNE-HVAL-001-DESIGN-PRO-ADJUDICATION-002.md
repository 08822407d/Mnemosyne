# MNE-HVAL-001 Design — Consolidated Pro Adjudication 002

```yaml
adjudication_id: MNE-HVAL-001-DESIGN-PRO-ADJUDICATION-002
source_design: MNE-HVAL-001-PRO-CORRECTED-VALIDATION-DESIGN-001.md
source_design_sha256: 78419602b6489ced71f165a6991d6873f07dbd5ed914d3a8e12c7f05d10a2142
source_Fable_task: WORK-ULTRA-FABLE-MNE-DR-006-HVAL001-PREEXEC-DESIGN-AUDIT-001
source_Fable_verdict: MNE_HVAL_001_DESIGN_READY_WITH_NONBLOCKING_REPAIRS
review_surface: current_ChatGPT_conversation_operator_reported_Pro
backend_identity: unknown_or_not_attestable
frozen_design_001_disposition: HVAL_DESIGN_REPAIR_REQUIRED
derivative_design_002_disposition: HVAL_DESIGN_ACCEPTED_FOR_SEPARATE_OWNER_AUTHORIZATION
fixture_publication_authorized: false
scenario_execution_authorized: false
quota_authorized: false
repository_write_performed_by_this_adjudication: false
```

## 1. Input verification

All six non-self HVAL output-manifest entries match the uploaded bytes and SHA-256 values exactly. The scenario and budget ledgers parse as YAML. The audit used the intended frozen 21-scenario Pro-corrected source.

## 2. Accepted independent findings

The following are accepted as required repairs to the frozen design:

- **AF-01:** hide scenario assignment behind opaque run tokens and blinded fixture paths; expected outcomes remain only in the committed hidden key.
- **AF-02:** N-family `BLOCKED_REQUIRES_PRO` is the terminal scored next-tier result with zero Pro turns; Pro is actually exercised only by A-031 and key-clean anomalies. A-family cases use fresh adjudicator conversations and may reuse frozen receiver reports.
- **AF-03:** keep the 60-file evidence ceiling by using aggregated run and adjudication ledgers.
- **AF-04:** implement N-017 through a manifest entry for a never-published guard path, not fixture deletion.
- **AF-05:** define fixture-scoped A-mode and manifest-mode guidance messages and the two-phase startup used by N-024; do not imply current generic guidance-command support for manifest mode.
- **AF-06:** make N-022 deterministic by moving the fixture-only commit between receiver return and adjudication re-read, so the four-way equality fails under harness control.
- **AF-07:** state receiver and adjudicator capability requirements per scenario.

## 3. Accepted recommended improvements

The Pro derivative also accepts:

- **BR-01:** add HV-P-004, a positive fixture-scoped manifest-guidance run.
- **BR-02:** strengthen the synthetic fixture adjudication contract with independent re-observation of every load-bearing reported `actual`, and add HV-A-033 using a fabricated all-green report over a seeded defect. This is explicitly a candidate-vNext fixture extension, not a claim that current Contract 002 already requires it.
- **BR-03:** define orphaned-adjudicator loss as `invalid_run`, recoverable only through an Owner-authorized fresh reissue.
- **BR-04:** add `true_BLOCK_wrong_reason`, a dedicated stranded token for N-021, and forced-key-branch handling for N-023.
- **BR-05:** enumerate fixture-harness writes and impose a repository change freeze for each receive/adjudication window; receiver/adjudicator no-write proof is scoped separately from authorized harness writes.
- **BR-06:** restate fresh reissue authorization inside the design.
- **BR-07:** pin the execution-source reference by path and blob.
- **BR-08:** pin observable tokens, declare scripted multi-message exceptions, add the N-019 synthetic banner, record defect side, and frame small-N availability results as directional.
- **BR-09:** publish a complete FC-01..12 coverage/out-of-scope map with the repaired taxonomy.

## 4. Corrected counts and budgets

```yaml
scenario_families:
  positive: 4
  negative: 15
  adjudication: 4
scenario_count: 23
mandatory_receiver_conversations: 19
maximum_invalid_runs: 2
maximum_owner_authorized_reissues: 2
worst_case_receiver_conversations: 23
receiver_conversation_ceiling: 24
Pro_turn_ceiling: 6
fixture_file_ceiling: 30
evidence_file_ceiling: 60
```

The 24-conversation ceiling still holds after adding P-004 because A-family scenarios consume adjudicator conversations and reuse or inject frozen reports rather than new receiver conversations.

## 5. Evidence interpretation

The package is a bounded falsification screen, not a statistical reliability estimate. Zero false PASS on seeded identity/oracle defects remains a hard threshold. Small-N availability observations are directional. Silent extra reads and an echo-only receiver on clean fixtures remain outside the evidence ceiling unless the Owner separately authorizes conversation exports.

## 6. Formal disposition

```yaml
MNE_HVAL_001_design_001: REPAIR_REQUIRED
MNE_HVAL_001_design_002: ACCEPTED_FOR_SEPARATE_OWNER_AUTHORIZATION
fixture_publication: SEPARATELY_GATED_NOT_AUTHORIZED
scenario_execution: SEPARATELY_GATED_NOT_AUTHORIZED
HO_GUIDANCE_001: OPEN_UNCHANGED
P_04_P_05_P_06_adoption: NOT_DECIDED_BY_DESIGN_ACCEPTANCE
safe_next_action: publish_design_002_and_audit_evidence_in_MNEMOSYNE_237_then_return_for_separate_fixture_and_execution_decisions
```
