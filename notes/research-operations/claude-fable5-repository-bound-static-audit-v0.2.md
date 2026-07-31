# Claude/Fable5 Repository-Bound Static Audit Workflow v0.2

> Non-execution-source operating guidance derived from A1 run 001. It supersedes the Advanced-Research transition in `claude-project-github-and-fable5-delivery-v0.1.md` for the two current Stage-A repository-bound static audits only. It does not establish a universal Claude product fact, run research, authorize quota, or select a validation surface.

```yaml
workflow_id: MNEMOSYNE-CLAUDE-FABLE5-REPOSITORY-STATIC-AUDIT-002
version: 0.2.0
created_by_task: MNEMOSYNE-186
repository: 08822407d/Mnemosyne
status: active_after_MNEMOSYNE_186_merge
applies_to:
  - FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
  - FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
execution_source: false
research_execution_authority: user_only
repository_write_by_Fable5: prohibited
```

## 1. Run-001 empirical finding

A1 run 001 produced two different access results in one user-visible chat sequence:

```yaml
ordinary_chat:
  four_path_preflight: PASS
  canonical_task_complete_read: true
  reported_full_19_input_read_before_launch: true

Advanced_Research_executor:
  canonical_task_accessible: true
  other_mandatory_inputs_accessible: 0_of_18
  result: INPUT_OR_REPOSITORY_INTEGRITY_FAILURE
  substantive_audit_started: false
```

The failure report explicitly states that the canonical task was read in full through its substantive sections and delivery boundary, while the package/source files were unavailable. Therefore:

```yaml
canonical_task_delivery_failure: false
repository_evidence_delivery_into_Advanced_Research: true
ordinary_chat_preflight_qualifies_Advanced_Research: false_for_run_001
```

This is direct evidence for one run, not proof of every Claude rollout or backend. It is sufficient to reject the current A1/A2 operator assumption because both tasks used the same access transition.

## 2. Cost and fail-closed assessment

```yaml
operator_reported_cost_USD_approx: 8
observed_research_duration: 6m13s
observed_source_activity_label: 151_sources
exact_billing_receipt_available: false
```

The final executor behaved correctly by refusing to fabricate unread package contents. The cost-control design failed because the expensive Research process began before it independently established access to the mandatory audit objects.

A logical input gate in the task body is not a sufficient quota gate when the product may perform expensive source collection before that task-level failure is returned.

## 3. Revised default for current tasks

```yaml
current_Stage_A_surface:
  visible_model: Fable_5
  visible_effort: Max
  Advanced_Research: off_for_entire_run
  chat_level_GitHub: required
  Project_Files: empty_by_default
  repository_gate_and_substantive_work_same_chat: required
  ordinary_web_search:
    during_repository_gate: off
    after_gate_PASS: targeted_only
```

The user-visible ordinary chat is the only surface directly shown to have read all required repository objects in run 001. The revised workflow therefore keeps the audit in that same context instead of transferring it to an unqualified Research executor.

## 4. Full-input gate, not sample preflight

The earlier four-file preflight proved only sample access. The revised gate reads every mandatory audit input before substantive work.

```yaml
A1:
  support_paths: 3
  mandatory_audit_inputs: 19
  total_gate_paths: 22
  canonical_spec_final_heading: "## 17. Delivery and authority boundary"

A2:
  support_paths: 3
  mandatory_audit_inputs: 12
  total_gate_paths: 15
  canonical_spec_final_heading: "## 14. Delivery and authority boundary"
```

The gate and audit must remain in the same ordinary chat. A sample, visible link, earlier operator assertion, or another context's receipt cannot qualify the run.

## 5. Same-context invariants

```yaml
required_constant_state:
  - same_chat
  - same_Project_or_no_Project
  - same_visible_model_and_effort
  - same_chat_level_GitHub_link
  - Advanced_Research_false
  - no_prior_reports_or_other_Stage_A_material
  - no_repository_write
```

The following invalidate the run:

- switching to Advanced Research;
- handing execution to another hidden or visible context;
- moving to another chat/Project/workspace;
- losing repository access;
- adding Project Memory or unrelated files;
- changing visible mode after the gate;
- relying on a gate receipt while the executor cannot re-read the underlying files.

## 6. External evidence sequence

Repository artifacts are primary for both tasks.

```yaml
source_sequence:
  step_1: complete_repository_gate
  step_2: reconstruct_and_analyze_repository_object
  step_3: identify_specific_external_evidence_gaps
  step_4: use_targeted_ordinary_web_search
  step_5: return_complete_report
```

Do not use source count as a quality target. Broad external search before repository binding is prohibited for these runs.

A2 may require more current official product documentation than A1, but it still begins with repository binding and does not need Advanced Research merely to use ordinary web search.

## 7. Advanced Research future route

Advanced Research is not declared generally unusable. A future repository-bound Advanced Research route requires separate validation using direct inputs visible to that exact executor, for example:

- an exact self-contained task bundle attached directly to the Research run;
- task-specific Project Files in a new one-run Project, if empirically shown to reach the Research executor;
- another provider-supported direct context mechanism.

Before a substantive paid rerun, perform a minimal bundle-visibility probe that:

1. uses synthetic/public content;
2. exposes all probe files directly to the exact paid execution surface;
3. verifies retrieval inside that surface rather than in an earlier ordinary chat;
4. stops before broad source collection;
5. has an explicit maximum cost/burden decision.

No such route is selected or validated here.

## 8. Failure semantics

```yaml
repository_gate_failure:
  result: INPUT_OR_REPOSITORY_INTEGRITY_FAILURE
  analysis_started: false
  external_source_collection_started: false
  final_disposition_allowed: false

repository_access_loss_after_PASS:
  result: RUN_INVALIDATED_BY_REPOSITORY_ACCESS_LOSS
  partial_work_may_be_returned_as_non_final_notes: true
  final_disposition_allowed: false

surface_requires_Advanced_Research:
  result: SURFACE_NOT_SUPPORTED_FOR_REVISED_RUN
  quota_experiment_allowed: false
```

## 9. Run-result roles

A failed input-binding run is not a substantive research report. It may be retained as:

- execution-surface evidence;
- operator-workflow evidence;
- cost/burden evidence;
- a task-design repair trigger.

It may not support package amendments, Q0-Q4 findings, scenario/key findings, surface selection, V0 authorization, or target/execution-source changes.

## 10. Current task refs

```yaml
A1:
  ready_entrypoint: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/task.md
  operator: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/OPERATOR.md
  manifest: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml
  execution_contract: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.2.md

A2:
  ready_entrypoint: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/task.md
  operator: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/OPERATOR.md
  manifest: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml
  execution_contract: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.2.md
```

## 11. Boundaries

This workflow does not:

- claim that ordinary Fable chat is generally superior to Advanced Research;
- attest an exact backend;
- authorize a research run or quota;
- modify the validation package;
- accept A1 as completed;
- create A2 results;
- select manual/API/runtime surface;
- execute V0/V1/V2/V3;
- authorize GitHub writes;
- modify a target project or execution source.
