# RAW-0056 — 学习状态依赖与跨 Agent 可复用记忆 TODO 输入

## metadata

```yaml
raw_id: RAW-0056
task_id: MNEMOSYNE-158
source_type: user_request
captured_at: 2026-07-26
language: zh-CN
execution_source: false
intended_derived_record:
  - current/todo.md
```

## repository capture safety preflight

```yaml
repository_capture_safety_preflight:
  preflight_id: MNEMOSYNE-158-PREFLIGHT-001
  source_contract_refs:
    - current/human-approved-spec.md §14
    - current/human-approved-spec.md §16
    - notes/object-templates-and-id-rules.md::Repository capture 安全预检
  checked_at: 2026-07-26
  checked_by: ChatGPT_GitHub_app
  repository_visibility_evidence_ref: GitHub.get_repo_2026-07-26
  current_repository_visibility: public
  source_or_material_ref: current_conversation_user_message_2026-07-26
  material_sensitivity_evidence_refs:
    - conceptual_Mnemosyne_product_design_requirements_only
    - no_credentials_secrets_tokens_private_source_customer_or_confidential_material_observed
  material_sensitivity_assessed: true
  contains_credentials_or_secrets: false
  contains_personal_private_customer_or_confidential_data: false
  intended_repository_path: raw/chatgpt-discussion-056.md
  storage_route: repository_original
  redaction_or_pointer_safety_checked: not_applicable
  git_history_persistence_acknowledged: true
  residual_risk: public_repository_permanently_preserves_the_user_wording_in_Git_history
  result: pass
```

## positioning

- 本文件保存本轮用户输入，作为非执行源 raw 证据。
- 它不是最终设计、不是已批准 schema、不是研究结论，也不授权自动推断、跨 Agent 共享服务、目标项目写入或执行源更新。
- `current/todo.md` 中的两条 TODO 是在查阅既有学习系统与跨项目复用材料后形成的去重合并版。
- 若本记录与 `current/human-approved-spec.md` 冲突，以后者为准。

## user input

> 此外你在TODO列表中追加一条：对帮助学习类型的Agent，如何记录用户的学习进度和知识/技能掌握程度，如果是科学和工程类的知识和技能那就有比较强的“基础-高级”依赖关系，也就是说掌握一些较高级的知识和技能需要前置知识和技能，根据学习目标预先构建这样的依赖关系（还需要具体到各前置需要掌握到什么程度，是否掌握的判断指标）对于这样的“教练agent”来说应该是很有必要的。同时教学对话从用户的回复中是否能判断出用户的掌握程度也是一个需要核实的问题。这点在mnemosyne构建之初应该就提过，不过很简略，你注意将我叙述的这部分和旧内容适当合并，不要造成重复冗余的TODO。此外再加一条TODO：像刚刚说的用户的知识面/技能栈以及相应的掌握程度是可以在不同的学习/练习agent对话中复用的，而基于同一行业的多个agent辅助开发软件中一些需求和要求也是可以复用的（不只是在“将常用功能整理封装成一个业务库”这种层次上，用户偏好，运行时环境特点，我的开发环境特点，我的开发偏好等也是需要复用的），如何在业务agent的建设和工作中实现这种可复用也是需要仔细研究和构思的。

## deduplication and derivation notes

### Learning / coaching Agent item

Existing material already identifies learning-specific memory such as learner profile, course progress, mistakes, vocabulary or knowledge mastery, and recurrence rate. The new input materially extends that earlier sketch by requiring:

- a learning-goal-specific prerequisite/dependency structure for scientific and engineering knowledge and skills;
- required mastery levels for each prerequisite;
- explicit mastery criteria and evidence;
- verification of whether ordinary dialogue replies can support reliable mastery inference;
- separation of observed evidence, model inference, and human-confirmed mastery.

The resulting TODO therefore extends the earlier item instead of duplicating it.

### Cross-Agent reuse item

Existing material already distinguishes reusable memory-system modules from project specialization and cautions against premature universal abstraction. The new input materially extends that work by requiring shared, reusable records for:

- knowledge/skill profiles and mastery evidence across learning/practice Agents;
- domain requirements and constraints across same-industry development Agents;
- user preferences;
- runtime-environment characteristics;
- development-environment characteristics;
- development preferences.

The resulting TODO keeps project-specific truth separate and adds authority, privacy, freshness, conflict, projection, synchronization, and promotion questions rather than creating a parallel generic “reuse” item.

## existing related evidence

- `raw/concept-origin-extract-001.md`
- `notes/target-project-memory-system-template-pack.md`
- `raw/research-reports/cycles/2026Q2-initial/review-records/MNEMOSYNE-031-R4B-item09-multi-project-reuse-and-specialization.md`
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/01_non_dev_long_term_memory_cases.md`
