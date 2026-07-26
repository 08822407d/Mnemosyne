# RAW-0058 — 模型能力预算、任务拆分与次一档模型可执行性输入

## metadata

```yaml
raw_id: RAW-0058
task_id: MNEMOSYNE-163
source_type: user_request
captured_at: 2026-07-26
language: zh-CN
execution_source: false
intended_derived_records:
  - current/model-capability-aware-work-planning-open-question.md
  - notes/model-capability-aware-work-planning-preparation-v0.1.md
```

## repository capture safety preflight

```yaml
repository_capture_safety_preflight:
  preflight_id: MNEMOSYNE-163-PREFLIGHT-001
  source_contract_refs:
    - current/human-approved-spec.md §6
    - current/human-approved-spec.md §14
    - notes/object-templates-and-id-rules.md::Repository capture 安全预检
  checked_at: 2026-07-26
  checked_by: ChatGPT_GitHub_app
  repository_visibility_evidence_ref: GitHub.get_repo_2026-07-26
  current_repository_visibility: public
  source_or_material_ref: current_conversation_user_message_2026-07-26
  material_sensitivity_evidence_refs:
    - conceptual_Mnemosyne_process_and_Agent_design_input_only
    - no_credentials_secrets_private_source_customer_or_confidential_material_observed
    - no_hidden_backend_claim_or_provider_internal_information
  material_sensitivity_assessed: true
  contains_credentials_or_secrets: false
  contains_personal_private_customer_or_confidential_data: false
  intended_repository_path: raw/chatgpt-discussion-058.md
  storage_route: repository_original
  redaction_or_pointer_safety_checked: not_applicable
  git_history_persistence_acknowledged: true
  residual_risk: public_repository_permanently_preserves_the_user_wording_and_model_usage_preferences_in_Git_history
  result: pass
```

## positioning

- 本文件保存用户关于 Mnemosyne 与未来 Agent 建设中模型能力预算、任务拆分和执行模型选择的原始要求。
- 它不是模型性能结论、provider backend attestation、已批准模型路由策略、成本政策、task schema 或执行源。
- 它不要求用户在任何情况下都使用尖端模型，也不要求自动降级、自动切换模型或由 Agent 擅自消耗高价值额度。
- 它不授权修改目标项目、执行源、模型设置、账户设置或第三方服务。
- 若本记录与 `current/human-approved-spec.md` 冲突，以后者为准，并通过 candidate/open-question 流程处理。

## user input

> 最近一个半月在mnemosyne的建设和复核评审等关键工作过程中基本都是用的gpt pro和fable5这类最尖端的模型进行工作的，为的就是像mnemosyne和以后的meta-agent能够尽可能完善。但不应该在mnemosyne的建设结果中明确记录或者暗示在任何情况下我都会用这些最尖端模型进行工作，比如一个临时的很小的具体需求的agent实现时我不大会消耗这些宝贵的“尖端额度”，因此在关键agent建设过程中必须要考虑自身给出的行为指导给最尖端以下一档的模型执行，其结果是否能满足要求。在规划工作时也应当考虑将工作内容分割整理，将需要深度和大规模推理的工作集中起来并提示我，我就会主动切换到pro模型或者交给其他厂商的尖端模型（比如最近用过的fable5），而剩余“低难度”工作我就会选择次一档的模型以节约额度。这个问题和稍早做的“记录特定工作使用的模型和智能程度”有一定的关联性。这个问题不需要你立即给出方案，你可以先进行准备，并告诉我需要我做什么。这次你给出的几个深度研究课题我会同时开展，等它们完成后我会把研究报告发回给你。

## normalized intent without policy promotion

```yaml
user_intent:
  quality_goal:
    - use_frontier_models_for_concentrated_high_value_reasoning_when_warranted
    - keep_Mnemosyne_and_key_Agent_architecture_work_high_quality
  resource_goal:
    - avoid_spending_scarce_frontier_quota_on_small_or_routine_work_by_default
    - allow_next_tier_models_to_handle_bounded_lower_difficulty_work
  design_goal:
    - do_not_assume_frontier_model_availability_in_Mnemosyne_outputs
    - design_guidance_and_taskbooks_with_lower_tier_executability_in_mind
    - decompose_work_so_deep_large_scale_reasoning_is_concentrated_and_visible
    - notify_the_user_before_a_frontier_level_stage_is_needed
    - leave_the_model_or_provider_switch_to_the_user
  validation_goal:
    - determine_whether_next_tier_execution_meets_required_quality_and_boundary_adherence
  relation_to_existing_work:
    - execution_context_provenance_is_related_but_not_sufficient
    - staged_Pro_Deep_Research_prompt_guidance_is_related_but_not_sufficient
  immediate_solution_requested: false
  preparation_requested: true
```

## relation to existing repository material

### IDEA-2026-0019

`notes/idea-capture-buffer.md` already records that model capability differences and work allocation require dynamic verification. The present input substantially extends that earlier idea from time-sensitive product facts to a design and validation problem:

- what capability class a task actually requires;
- which parts require frontier-level synthesis or adjudication;
- which parts can be delegated to a next-tier model or mechanical executor;
- how an artifact should declare escalation and verification needs without hard-coding a provider model;
- how to test that a next-tier model can follow the resulting guidance.

The derived records should extend IDEA-2026-0019 rather than create a duplicate “which model is currently available” question.

### Run-context and PR provenance

`current/run-context-and-pr-provenance-guard.md` records what surface/selection was used and what can honestly be attested. It does not decide what capability a task requires or whether a lower-tier executor is adequate.

### Staged Pro / Deep Research guidance

`current/human-approved-spec.md` §17 already requires dependency-aware prompt staging and a model-strength switch reminder when high-risk prompt design needs it. The current input broadens the issue to general Agent construction, task decomposition, routine implementation, review, validation and lower-tier executability.

## boundaries for derivation

- Do not turn “frontier” or “next tier” into a permanent provider/model mapping.
- Do not infer exact backend identity from UI labels or output quality.
- Do not require frontier models for every Mnemosyne or target-project task.
- Do not promise that a lower-tier model is adequate without controlled evidence.
- Do not define cost or quota values as stable facts.
- Do not authorize automatic model switching or quota consumption.
- Do not make the four isolated Pro Deep Research tasks dependent on this preparation item.
