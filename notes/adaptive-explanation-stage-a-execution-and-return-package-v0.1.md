# Adaptive Explanation Stage A — Execution and Return Package v0.1

> Non-execution-source operator package for one external Pro Deep Research run and one consolidated return to the Mnemosyne maintenance conversation. It does not execute research, attest a backend, accept a report, generate Stage B, assess the user, or authorize repository ingestion.

```yaml
package_id: ADAPTIVE-EXPLANATION-STAGE-A-EXECUTION-RETURN-001
created_by_task: MNEMOSYNE-174
research_id: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001
research_prompt: notes/research-prompts/PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001.md
research_design: notes/adaptive-explanation-stage-a-research-design-v0.1.md
review_instrument: notes/adaptive-explanation-stage-a-report-review-and-convergence-v0.1.md
status: ready_for_one_external_research_run
execution_source: current/human-approved-spec.md
execution_source_modified: false
research_executed: false
repository_ingestion_authorized: false
```

## 1. Purpose and efficiency constraint

The user asked the current Mnemosyne route to proceed while reducing avoidable frontier-model conversation turns. The safe consolidation is:

```text
one external Stage A Deep Research run
  -> one return message containing the complete report and run metadata
  -> one Mnemosyne maintainer turn for all non-dependent review steps
```

This package therefore prepares:

- one exact launcher;
- one pre-run topic-binding check;
- one runtime evidence receipt;
- one complete return bundle;
- one consolidated post-return review contract;
- a conditional path to prepare Stage B decision material in the same maintainer turn when the report passes and no new substantive user decision is required.

It does **not** collapse research production and independent maintenance review into one run. It also does not pre-generate Stage B before Stage A evidence exists.

## 2. Required execution surface

```yaml
execute_in:
  product_surface: fresh_Pro_Deep_Research_task
  task_count: one
  ordinary_chat_substitute: not_recommended_for_this_research_contract
  attachment_only_input: avoid_when_practical
  preferred_input: paste_complete_prompt_body
```

Use the exact current prompt from:

```text
notes/research-prompts/PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001.md
```

Do not combine this task with GPT Live research, persistent learner-memory design, cross-Agent sharing, model-capability validation or Meta-Agent product work.

## 3. Pre-run product and quota check

Before starting, record what is visible without treating it as backend attestation:

```yaml
pre_run_receipt:
  research_id: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001
  date:
  local_time:
  product_surface_visible_text:
  operator_visible_model_or_mode_text:
  visible_reasoning_or_intelligence_text:
  usage_or_quota_counter_before:
  complete_prompt_pasted_in_message_body: yes | no
  attachment_also_used: yes | no
  attachment_filename_if_any:
```

If the product reports that full Pro/Deep Research capacity is unavailable, do not assume a fallback has equivalent capability. Either defer the run or record the visible fallback state explicitly and treat the report as requiring heightened review.

The visible selection, quota counter, latency and output style do not prove the exact served backend.

## 4. Copyable launch message

After pasting or attaching the complete prompt, send:

```text
Execute the complete PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001 task exactly.

After the internal input-integrity check passes, continue through substantive research to the complete final report. Do not stop at a plan-only response and do not substitute a generic, unspecified, Python-reproducibility, broad learner-model, GPT Live, persistent-memory, or adjacent topic.

If the complete task is unavailable or truncated, return INPUT_INTEGRITY_FAILURE and do not research a substitute topic.

The final report must include the complete inline report body and a portable source table with literal https:// URLs, stable identifiers, dates, source type, claim mapping, and direct-versus-analogical support.
```

Do not add a separate conversational `CONTINUE` or `批准计划` protocol.

If the product UI displays a native proposed plan and requires a product-level button, inspect the plan and use the product control only when it is correct. A product-level confirmation is not a second research-chat instruction. Do not treat the plan as the final report.

## 5. Native-plan acceptance gate

The native plan must visibly bind to both:

```yaml
required_plan_identity:
  research_id: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001
  exact_topic: AI_text_dialogue_tutor_local_prerequisite_diagnosis_explanation_selection_evaluation_and_repair_for_foundational_university_mathematics_without_global_learner_level
```

It should cover at least:

- local difficulty/failure hypotheses;
- prerequisite routes and required mastery;
- low-burden diagnostic interaction;
- explanation-action selection;
- explanation-failure recovery;
- accessibility without false simplification;
- outcome measurement;
- a four-condition controlled experiment;
- portable sources and evidence calibration.

Cancel or stop the run when the plan instead centers on:

- an unspecified topic;
- generic research methodology;
- Python reproducibility;
- a broad learner-model survey without adaptive explanation;
- GPT Live product configuration;
- persistent learner memory or cross-Agent sharing;
- assessment of the current user.

## 6. Evidence to preserve during and after the run

```yaml
run_receipt:
  research_id: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001
  start_time:
  end_time:
  duration:
  product_surface_visible_text:
  operator_visible_model_or_mode_text:
  visible_reasoning_or_intelligence_text:
  usage_or_quota_counter_before:
  usage_or_quota_counter_after:
  exact_native_plan_text_or_screenshot_available: yes | no
  native_plan_bound_exact_topic: yes | no | unclear
  substantive_search_started: yes | no | unclear
  source_count_visible:
  activity_or_search_history_available: yes | no
  source_panel_available: yes | no
  interruptions_or_user_redirects: []
  inaccessible_sources: []
  citation_or_export_failures: []
  truncation_or_incomplete_report_warning:
  downloaded_report_filename:
```

Do not infer the exact backend from this receipt. Its purpose is to distinguish input binding, product orchestration, source gathering, report synthesis and export failures.

## 7. Final-report minimum acceptance preflight

Before returning the report to Mnemosyne, check only the obvious gates; do not try to adjudicate the research yourself.

```yaml
operator_preflight:
  exact_research_ID_present: yes | no
  exact_topic_present: yes | no
  input_integrity_receipt_present: yes | no
  substantive_research_completed_claimed: yes | no
  final_report_not_plan_only: yes | no
  all_19_required_report_sections_apparently_present: yes | no | unclear
  controlled_experiment_C0_to_C3_present: yes | no
  literal_https_URLs_present: yes | no
  current_user_assessed_or_profiled: yes | no
  GPT_Live_or_persistence_scope_substituted: yes | no
```

A `no` on identity, topic or substantive completion means the output is not a valid Stage A result.

## 8. Complete return bundle

Return all available items in one message to the current Mnemosyne maintenance conversation:

1. complete final report body;
2. downloaded report file;
3. completed pre-run and run receipts;
4. native plan text or screenshot;
5. source count and source-panel availability;
6. all access, citation, export and truncation warnings;
7. any visible quota/fallback notice;
8. the following instruction.

### Copyable return instruction

```text
@GitHub 这是 PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001 的完整最终报告、下载文件和运行元数据。

请在当前同一轮工作中尽量完成所有不依赖新用户政策决定的步骤：
1. 输入绑定、章节完整性和来源可移植性检查；
2. 承重来源抽样核验与证据强度校准；
3. 与既有 learner/cognitive-coaching 研究及 Stage A 设计的冲突检查；
4. 给出接受、修补、补遗、重跑或拒绝裁决；
5. 若报告通过且无需新的实质用户决定，准备一个有边界的单一 PR，统一保存报告、运行记录、维护者审查、状态收口和 Stage B 决策准备材料；不要执行 Stage B 实验，也不要自动批准持久学习者记忆、GPT Live 或跨 Agent 共享。
```

This return instruction supplies fresh task intent for consolidated review. Repository writes still require the maintainer to perform the normal latest-master, open-PR, path and authority preflight.

## 9. Consolidation rule after report return

The next maintainer turn should attempt, in this order:

```yaml
same_turn_pipeline:
  - artifact_receipt_and_hash_inventory
  - input_topic_and_output_contract_review
  - portable_source_manifest_check
  - load_bearing_source_sample_validation
  - evidence_maturity_and_claim_calibration
  - controlled_experiment_design_review
  - safety_privacy_autonomy_review
  - conflict_check_against_existing_research_and_current_status
  - final_report_disposition
  - conditional_single_PR_preparation
```

Conditional single-PR preparation is allowed only when:

- the report is accepted or accepted with bounded corrections;
- the corrections can be kept in a maintainer review without rewriting the original report;
- no owner/authority/privacy decision is being inferred;
- no Stage B experiment is executed;
- no other open PR or path conflict exists;
- the user return instruction authorizes continuation along this route.

If the report requires a clean rerun, a major addendum or a new research-scope decision, the same-turn pipeline stops after producing the recovery package.

## 10. Failure branches

```yaml
failure_branches:
  INPUT_INTEGRITY_FAILURE:
    action: inspect_input_transport_before_any_rerun
  wrong_or_unspecified_topic:
    action: reject_as_invalid_task_output_and_prepare_direct_paste_rerun_only
  plan_only_output:
    action: determine_whether_native_research_can_resume_or_record_product_orchestration_failure
  missing_portable_URLs_but_substantive_report:
    action: acceptability_depends_on_source_identity_recoverability_and_bounded_correction
  major_required_sections_missing:
    action: bounded_completion_addendum_or_clean_rerun_based_on_missing_scope
  quota_or_fallback_anomaly:
    action: preserve_visible_evidence_and_apply_heightened_quality_review
  strong_report_with_mixed_evidence:
    action: preserve_original_and_record_maintainer_calibration_separately
```

## 11. Boundaries

- This package does not identify or attest the runtime model.
- It does not execute or accept the research.
- It does not authorize GitHub or connected-service writes by the research task.
- It does not assess the user or create a learner profile.
- It does not configure GPT Live or persistent/cross-Agent memory.
- It does not generate or execute Stage B.
- It does not make a returned report an execution source.
- It does not change the current single-mainline route.
