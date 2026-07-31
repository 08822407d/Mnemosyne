# Frontier Clarification Validation — Staged Fable5 Research Plan v0.3

> Non-execution-source plan. It updates the Stage-A execution surface and run state after A1 run 001. The underlying A1/A2 questions and allowed substantive dispositions are unchanged.

```yaml
plan_id: FABLE5-FRONTIER-CLARIFICATION-VALIDATION-STAGED-PLAN-001
version: 0.3.0
created_by_task: MNEMOSYNE-186
supersedes_execution_surface_and_run_state_of: notes/research-plans/2026Q3-frontier-clarification-validation-fable5-staged-plan-v0.2.md
source_package: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
source_package_merge_commit: 67eb96d5317a2bb589236a4a8b2e75be2508d830
manual_candidate_merge_commit: 5e556c2a6dacb41d68bf6209dbf8156b92b79e72
status: A1_input_binding_failure_recorded_revised_A1_and_A2_prepared_Stage_B_deferred
research_execution_authority: user_only
```

## 1. A1 run 001

```yaml
A1_run_001:
  ordinary_chat_preflight: PASS
  canonical_task_complete_read: true
  canonical_task_final_heading: "## 17. Delivery and authority boundary"
  Advanced_Research_access:
    canonical_task: accessible
    other_mandatory_inputs: inaccessible_18_of_18
  result: INPUT_OR_REPOSITORY_INTEGRITY_FAILURE
  substantive_analysis_started: false
  substantive_report_received: false
  accepted_role: execution_surface_failure_evidence
  operator_reported_cost_USD_approx: 8
```

The canonical task was delivered correctly. The failure occurred because the later Research executor could not access the package and source files that the ordinary chat had read.

## 2. Revised Stage-A surface

```yaml
surface:
  visible_model: Fable_5
  visible_effort: Max
  Advanced_Research: false_for_entire_run
  Project_Files: empty_by_default
  chat_level_GitHub: required
  repository_gate_and_substantive_work_same_ordinary_chat: required
  ordinary_web_search:
    before_repository_gate_PASS: false
    after_repository_gate_PASS: targeted_only
```

The earlier four-path sample is replaced by a full input gate. A1 must bind all 19 audit inputs. A2 must bind all 12 audit inputs.

## 3. A1 current state

```yaml
task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
run_attempts: 1
substantive_reports_received: 0
state: revised_rerun_ready_after_MNEMOSYNE_186_merge
canonical_specification: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
execution_contract: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.2.md
operator: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/OPERATOR.md
manifest: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml
research_question_changed: false
```

## 4. A2 current state

```yaml
task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
run_attempts: 0
substantive_reports_received: 0
state: preventively_repaired_ready_after_MNEMOSYNE_186_merge
canonical_specification: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
execution_contract: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.2.md
operator: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/OPERATOR.md
manifest: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml
research_question_changed: false
```

A2 uses A1 only as execution-surface evidence. No A1 substantive findings exist to import.

## 5. Recommended order

1. merge or revise MNEMOSYNE-186;
2. run the revised A1 full input gate in one fresh ordinary Fable 5 Max chat;
3. complete A1 in that same chat only after the gate passes;
4. return and adjudicate A1;
5. decide whether A2 still has full decision value;
6. run A2 separately when selected.

## 6. Cost and source discipline

```yaml
cost_and_source_rules:
  prior_operator_reported_cost_USD_approx: 8
  exact_billing_receipt_available: false
  automatic_rerun: false
  Advanced_Research_for_current_tasks: false
  broad_external_search_before_repository_gate: false
  source_count_target: none
  user_retains_run_decision: true
```

Repository artifacts remain primary. Ordinary web search is used only after repository binding and only where it changes a concrete finding.

## 7. Acceptance gate

A report enters substantive adjudication only when:

- the active execution contract is identified;
- the complete canonical specification is read;
- all mandatory inputs are bound in the same ordinary chat;
- every required report section is present;
- no access loss, prohibited repository write, cross-task contamination, or live validation occurred;
- exactly one allowed disposition is returned.

An input-binding failure is surface evidence, not a substantive research report.

## 8. Stage B

The four conditional Stage-B topics remain non-runnable. No Stage-B prompt is generated until valid Stage-A evidence is adjudicated and its trigger is met.

## 9. Safe next action

```yaml
safe_next_action:
  - review_and_merge_MNEMOSYNE_186_or_request_changes
  - after_merge_user_may_run_revised_A1_in_one_fresh_ordinary_Fable_5_Max_chat
  - keep_Advanced_Research_off
  - return_the_full_input_binding_receipt_and_complete_report
  - adjudicate_A1_before_A2_when_practical
  - keep_surface_V0_V1_and_Stage_B_unselected
```
