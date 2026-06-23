# Mnemosyne 交接包策略研究

## 直接结论

**结论先行：Mnemosyne 目前的 handoff strategy 方向是基本正确的，但还停留在“方向对、量化不足”的阶段。** 它已经具备一个成熟 handoff 体系最关键的基础件：唯一 execution source、明确的 non-execution-source 边界、startup/current/handoff 分层、first target-project dry-run 的 exact read order、fresh replay protocol、run manifest template，以及针对 Codex stale branch / diff verification 的防漂移护栏。外部最佳实践也支持这一路线：高质量 handoff 不只是“传信息”，还必须同时转移当前事实、权责边界、不确定性与下一步计划；长程 agent 也不应把全部历史直接塞进上下文，而应以高信号摘要、可审计 evidence、memory/compaction/just-in-time retrieval 的组合来续接。citeturn9view3turn28view2turn29view0turn29view3turn29view7turn21view9turn25view2turn25view3turn21view5turn21view1

**当前最大的风险不是“没有 handoff 文件”，而是“把过期状态误当作当前真相”。** Mnemosyne 仓库已经明确写出：pre-050 fresh replay 的 PASS 不能关闭 post-050 gate；当前真实状态仍然是“尚未进行 real target-project dry-run、尚未选择 target、尚未上传/摄入 target materials、尚未写入 target repository”，并且 real dry-run 仍被 post-050 replay PASS、用户 target/authority/safe-input/no-target-write/run-manifest 批准所阻塞。与此同时，仓库也记录过更强的失败模式：Codex 旧 task 环境或旧 branch 的结果看起来正确，但 default branch 最终状态并不正确；继续在 stale 环境上工作还可能把旧内容重新带回。对 Mnemosyne 来说，真正危险的是 **stale currentness promotion**：把旧 replay、旧 result record、旧 handoff、旧导出对话、甚至 research report/active-context 当成当前执行真相。citeturn28view4turn28view2turn16view3turn16view5turn29view7turn38view0

**在 first real target-project dry-run 之前，最该做的不是继续堆更多文件，而是把“交接是否正确”做成一次可重复、可记分、可审计的测试。** 具体说，Mnemosyne 应先用 post-050 replay protocol 在 fresh ordinary Thinking / ChatGPT session 中跑一次正式 replay test；要求受测会话仅凭当前允许文件恢复 execution source、current phase/gate、真实 dry-run/target/write 状态、required user decisions、冲突与缺失、以及一个仅模拟不写入的 next action，并为关键结论给出 repository evidence path；随后用本文的 rubric 打分，只要任一 blocking gate 失败，就不能进入 first real target-project dry-run。这个动作与仓库中现有 protocol、acceptance gate、manifest 设计高度一致，也最符合 MemoryArena/LongMemEval/MemoryAgentBench 这类 benchmark 对“记住什么、更新什么、何时停止假设、如何把 memory 用到后续行动上”的评估趋势。citeturn9view0turn29view3turn31view0turn35view0turn36view0turn34view4

从外部视角看，Mnemosyne 现在最应该避免的是两个误区。第一，**误以为更长的 handoff 一定更好**。LangChain 和 Anthropic 都明确提醒：长上下文既会带来 token 成本和速度问题，也会让模型被 stale / off-topic 内容“分心”；Anthropic 进一步把 context engineering 的核心归结为“最小但高信号”的 tokens 组合，而不是上下文越满越安全。第二，**误以为 judge / verifier 可以只靠单次模型判分**。RubricEval、LLM-Rubric 和 Mnemosyne 自己的 open questions 都表明：rubric-based judging 仍不可靠，模型可协助评估、分类和诊断，但不应成为唯一裁判；高风险 handoff 应保留 evidence、trace、回放与必要的人类复核。citeturn21view5turn21view6turn25view2turn25view3turn37view1turn37view0turn38view0

## 正确交接的操作性定义

**交付物 A：正确交接定义**

> **正确交接**，是指在一个 fresh agent/session **不依赖旧对话隐式上下文** 的前提下，仅凭被明确授权的 handoff package 和可访问证据，能够正确恢复：当前 execution source、当前 phase / gate、当前真实状态、权限与禁止动作、已完成与未完成任务、以及一个安全的下一步动作；同时在遇到缺失、冲突、过期或能力不确定时，**显式标注 unknown / unsupported assumption，而不是自行编造**；并且不会把历史材料、non-execution-source、平台隐藏记忆或旧 conversation export 误当作当前真相。这个定义把 AHRQ handoff 强调的权责转移、uncertainty、recent changes 与 contingencies，结合到 Mnemosyne 当前的 execution-source boundary、gate recovery、stale-state resistance 与 next-action recovery 上。citeturn21view9turn21view10turn9view3turn28view2turn9view0turn25view2

这个定义对 Mnemosyne 尤其重要，因为 Mnemosyne 的核心目标不是“保存更多文本”，而是让长期 AI 工作可以在不同 conversation、模型、工具、时间点之间**恢复性续接**。因此，“correct handoff” 不能只定义为“摘要基本没错”，而必须包含至少十个维度：state recovery correctness、execution-source recovery、task intent recovery、boundary recovery、authority / user approval recovery、next-action recovery、stale-state resistance、unsupported-assumption handling、safety/privacy boundary preservation、model/tool provenance recovery，以及“无需重问已回答问题”的续接能力。MemoryAgentBench、LongMemEval、MemBench 与 MemoryArena 也分别从 retrieval、knowledge update、abstention、efficiency 与 action-coupled memory 的角度证明：只考“记住多少”不够，还必须考“记得对不对”“更新得对不对”“不知道时会不会停”“是否把记忆正确地用于后续行动”。citeturn36view0turn34view4turn34view3turn35view0

下面这份 checklist 可以直接作为 Mnemosyne 的操作性定义清单。只要其中任一 **blocking** 项失败，这次 handoff 就不应被判定为“可安全续接”。

| 维度 | 操作性判定问题 | 通过标准 | blocking |
|---|---|---|---|
| 执行源恢复 | 新会话是否明确指出唯一 execution source？ | 唯一指出 `current/human-approved-spec.md`，且不把 handoff/research/result 当 execution source | 是 |
| 当前 gate 恢复 | 是否正确恢复 current phase / gate？ | 明确恢复 post-050 replay gate，且知道 pre-050 PASS 不算关闭 | 是 |
| 真实状态恢复 | 是否正确恢复 real dry-run / target / write 等现实状态？ | 明确指出尚未 real dry-run、尚未 target selection、尚未写 target repo | 是 |
| 边界恢复 | 是否正确恢复 non-execution-source boundary？ | 明确 handoff/startup/active-context/result/research 都不是 execution source | 是 |
| 权限恢复 | 是否恢复 user approvals / authority map？ | 明确哪些决定仍待用户批准，哪些 actor 不能写入 | 是 |
| 任务意图恢复 | 是否知道当前在做什么而不是重开旧任务？ | 能指出当前应做 replay / verification，而非误报 dry-run 已发生 | 是 |
| 下一步恢复 | 是否给出一个安全、范围内、可执行的 next action？ | 给出仅读/验证/模拟动作，而非越权写入或虚构 target work | 是 |
| 过期抗性 | 是否识别 stale / superseded item？ | 会标注旧 replay、旧 export、旧 result 为历史或 superseded | 是 |
| 假设处理 | 遇到未知时是否 abstain？ | 用 `unknown` / `unsupported assumption` 标注，不默默补全 | 是 |
| 证据映射 | 关键结论是否给 path-level evidence？ | 所有关键结论都能回指文件路径/记录来源 | 是 |
| 安全与隐私 | 是否保留 input safety / privacy boundary？ | 不把 unsafe/private/unapproved material 拉入交接 | 是 |
| 已答问题不重问 | 是否避免重复询问 repo 已回答事项？ | 不再次追问已被 handoff/current 明示的 gate/state | 否 |

Mnemosyne 当前仓库事实上已经为这一定义提供了土壤：它把唯一 execution source、startup 最小读取集、当前 gate、actor permissions、run manifest 所需 user approvals、unsupported assumptions、以及 stale Codex branch 风险都写成了独立工件。本文的建议不是另起炉灶，而是把这些已存在的规则，提升成一个可量化、跨工具可比、可回放验证的 handoff correctness 框架。citeturn9view5turn28view2turn29view2turn31view0turn29view7

## 交接包层级模型

交接包不宜只有一个固定形态。Anthropic 的 context engineering 指南、Claude Code memory 文档、LangChain 的 thread-vs-long-term memory 区分，以及 OpenAI Agents SDK 的 handoff input filtering / input auditing 共同说明：跨 session 续接做得好不好，不取决于“内容全不全”，而取决于**当前任务是否拿到了最少但充分的高信号上下文**，以及这份上下文能否被过滤、审计、压缩和回放。Mnemosyne 自己的 onboarding package 也明确写出：ordinary executor 不应在启动时默认读完大型模板包；大包只在具体设计细节需要时才作为参考。这正是采用 **minimum / standard / extended** 三层模型的理由。citeturn25view2turn25view3turn21view3turn21view5turn21view1turn29view2

### 层级总览

| 层级 | 用途 | 适用场景 | 建议长度 | 必备证据 | 明确排除 |
|---|---|---|---|---|---|
| 最小交接包 | 让 fresh ordinary conversation 安全续接 | 同模型/同工作流、低风险续接 | 约 250–500 tokens | execution source、current gate、next action、关键 evidence paths | 完整对话导出、raw diff、大段历史背景 |
| 标准交接包 | 仓库维护和 ChatGPT↔Codex↔验证循环 | Mnemosyne maintenance、repo-backed continuation | 约 700–1500 tokens | 上述全部 + authorities、completed/pending、forbidden actions、missing files、provenance | 未标注的旧 export、research report 结论洪泛、复制整份 result records |
| 扩展交接包 | 高风险迁移与失败恢复 | model migration、post-failure repair、stale-state diagnosis | 约 1500–3000 tokens | 上述全部 + stale/conflict ledger、timeline、selected historical excerpts、repair notes | 默认导入所有旧会话、未经筛选的大型 raw evidence |

上表中的“排除项”不是装饰，而是 handoff correctness 的一部分。Mnemosyne 已经多次把“research report 不是 execution source”“manual-import-inbox 只是 transfer artifact”“result record 不应嵌入大型 raw diff”“完整 conversation export 默认不完整入库，只考虑 selected excerpts”写成明示边界；外部长上下文文档也都反对把所有历史一股脑塞进上下文。换句话说，**排除错误内容和保留正确内容同样重要**。citeturn9view3turn8view4turn29view7turn38view0turn25view2turn21view6

### 最小交接包模板

这个层级服务于“普通续接”，其目标不是让新会话理解所有历史，而是让它**不犯关键错误**。它应当最先恢复 execution source、gate、权责边界和一个 next safe action；这与 AHRQ/SBAR 的 Situation-Background-Assessment-Recommendation 思路一致，也与 Mnemosyne replay protocol 要求恢复 phase、gate、真实状态、required user decisions、conflicts 和 simulated next action 的做法一致。citeturn21view10turn9view0

```yaml
minimum_handoff_package_v0.1:
  package_id:
  status: active_non_execution_source_handoff
  source_conversation_or_task:
  target_session_type: ordinary_chatgpt | ordinary_thinking | codex_verifier | other
  repository_ref_or_commit:
  visible_model_or_tool:
  tested_at:

  execution_source:
    path: current/human-approved-spec.md
    note: only_execution_source

  current_phase:
  current_gate:
  live_truths:
    no_real_target_project_dry_run:
    no_target_project_selected:
    no_target_material_uploaded_or_ingested:
    no_target_repository_written:

  current_task_intent:
  one_safe_next_action:

  non_execution_boundaries:
    - handoff/*
    - current/active-context.md
    - notes/codex-task-results/*
    - research reports
    - old conversation exports

  forbidden_actions:
    - do_not_treat_non_execution_sources_as_execution_source
    - do_not_claim_unperformed_dry_run_or_target_selection
    - do_not_write_target_project
    - do_not_use_unsafe_inputs

  unsupported_assumptions:
    - 

  evidence_map:
    - claim:
      path:
      why_it_matters:

  explicitly_excluded:
    - full_conversation_export
    - raw_diff_body
    - large_result_record_copy
    - speculative_future_design
```

### 标准交接包模板

标准层级适合 Mnemosyne maintainer conversation、ordinary ChatGPT planning 到 Codex task、以及 Codex result 返回 ordinary verification 的常规工作流。它应额外携带：已完成任务与仍待完成事项的分离、authority / approvals map、文件可见性与 missing-file 风险、以及 provenance。Mnemosyne 现有仓库中，startup 最小读取集、onboarding exact read order、manifest 的 approvals 字段、以及 task-result provenance 最小要求，已经为这一层提供了直接依据。citeturn9view5turn29view0turn31view0turn29view7

```yaml
standard_handoff_package_v0.1:
  package_id:
  status: active_non_execution_source_handoff
  handoff_scope: mnemosyne_maintenance | codex_task | replay_verification | target_dry_run_prep
  source_conversation_or_task:
  target_conversation_or_task:
  repository_ref_or_commit:
  visible_model_label:
  reasoning_effort_if_visible:
  tool_or_interface:
  fresh_session_required: yes

  read_order:
    - current/human-approved-spec.md
    - handoff/handoff-current.md
    - handoff/startup-instructions.md
    - current/active-context.md
    - current/todo.md
    - current/open-questions.md
    - notes/codex-task-authoring-and-diff-verification-guidelines.md
    - task-local files if applicable

  execution_source:
    path: current/human-approved-spec.md
    conflict_rule: spec_wins_record_open_question

  current_state:
    current_phase:
    current_gate:
    live_truths:
      no_real_target_project_dry_run:
      no_target_project_selected:
      no_target_material_uploaded_or_ingested:
      no_target_repository_written:
    current_priority:
    current_task_intent:

  completed_recently:
    - task_id:
      consequence_for_current_state:
      still_non_execution_source: yes

  still_pending:
    - item:
      why_pending:
      who_can_close_it:

  authorities_and_permissions:
    user_must_approve:
      - target_selected
      - authority_confirmed
      - source_use_approved
      - privacy_boundary_approved
      - no_target_write_approved
      - run_manifest_approved
    ordinary_chatgpt_can:
    ordinary_chatgpt_cannot:
    codex_can:
    codex_cannot:

  forbidden_actions:
    - do_not_promote_non_execution_source
    - do_not_claim_unperformed_work
    - do_not_infer_target_write_permission
    - do_not_rely_on_old_conversation_memory
    - do_not_invent_missing_repo_state

  stale_or_conflict_items:
    - item:
      type: stale_status | superseded_result | historical_export | branch_risk | unknown
      handling:

  unsupported_assumptions:
    - assumption:
      status: unknown | needs_user_decision | needs_repo_check

  missing_files_or_access_limits:
    - file_or_capability:
      impact:
      fallback:

  evidence_map:
    - claim:
      evidence_path:
      authority_level: execution_source | non_execution_current_state | historical_example
      freshness_note:

  explicitly_excluded:
    - full_old_export_default_import
    - full_raw_diff_embed
    - research_report_as_execution_source
    - hidden_platform_memory_as_truth
```

### 扩展交接包模板

扩展层级只用于高风险 transition：例如 post-failure recovery、跨工具迁移、模型族迁移、旧 conversation contamination 排查、或者 stale Codex branch 诊断。它不是“更长的标准包”，而是标准包加上**冲突账本、时间线、精选历史摘录与修复路线**。Anthropic 在 long-running agent harness 上强调 structured artifacts for session-to-session handoff；Mnemosyne 自己的 stale-branch 诊断、postmortem-style review 倡议和 historical export contamination open questions 也都指向这一层的必要性。citeturn25view0turn25view1turn29view7turn38view0turn33view0

```yaml
extended_handoff_package_v0.1:
  package_id:
  status: high_risk_non_execution_source_handoff
  escalation_reason:
    - model_migration
    - post_failure_recovery
    - stale_state_diagnosis
    - cross_tool_transfer
    - old_export_contamination_check

  source_conversation_or_task:
  target_conversation_or_task:
  repository_ref_or_commit:
  visible_model_label:
  reasoning_effort_if_visible:
  tool_or_interface:
  files_available:
  files_read_by_source_session:
  hidden_prior_context_expected: yes | no | unknown

  execution_source:
    path: current/human-approved-spec.md
    validated_at:
    known_conflicts:

  current_state_snapshot:
    current_phase:
    current_gate:
    real_world_status_claims:
      real_target_project_dry_run:
      target_selection:
      target_material_ingestion:
      target_repo_write:
    current_task_intent:
    recommended_next_action:
    do_not_repeat:
      - old_task_or_question:

  authority_map:
    mnemosyne_execution_source:
    task_local_user_decisions:
    target_execution_source_if_any:
    unresolved_authority_questions:

  stale_conflict_ledger:
    - item:
      first_seen_in:
      why_it_is_stale_or_risky:
      current_disposition:
      evidence_path:

  selected_historical_excerpts:
    - excerpt_id:
      source_type: historical_conversation_derived_insight | old_result_record | old_handoff
      current_truth_status: non_current_example_only
      relevance:
      contamination_risk:
      evidence_path:

  codex_or_agent_transition_notes:
    source_branch_or_snapshot:
    stale_branch_risk:
    protected_files:
    required_diff_verification:
    result_record_path:

  privacy_and_sensitivity:
    repository_visibility:
    allowed_material_class:
    forbidden_material_class:
    manual_transfer_needed:

  failure_recovery_plan:
    stop_conditions:
    first_repair_action:
    verification_action:
    fallback_if_files_missing:

  evidence_map:
    - claim:
      evidence_path:
      authority_level:
      freshness:
      confidence:

  explicitly_excluded:
    - full_transcript_dump
    - unredacted_sensitive_material
    - uncontrolled_auto_writeback_instruction
    - unlabeled_historical_material
```

## 量化评分量表

Mnemosyne 需要的不是一个“主观感觉不错”的 handoff，而是一个**可跨会话、跨模型、跨工具复跑**的评分框架。外部 benchmark 已给出几个很重要的启发：MemoryAgentBench 强调 retrieval、test-time learning、long-range understanding、selective forgetting；LongMemEval 强调 knowledge updates 与 abstention；MemBench 强调 effectiveness、efficiency、capacity；MemoryArena 强调 memory 与 action 在多 session 中是耦合的；LoCoBench-Agent 则直接把 comprehension 与 efficiency 同时纳入评分。这意味着 Mnemosyne 的 rubric 不能只看“回忆正确率”，还必须衡量 **action correctness、abstention quality、evidence quality 与 cost efficiency**。同时，RubricEval 和 LLM-Rubric 又提醒我们：rubric-based judge 本身并不稳定，所以高风险判定要以 blocking gates + evidence paths 为主，而不是让总分完全决定结论。citeturn36view0turn34view4turn34view3turn35view0turn35view4turn37view1turn37view0

**交付物 B：Mnemosyne handoff scoring rubric v0.1**

| 维度 | 权重 | 满分标准 | 典型扣分点 |
|---|---:|---|---|
| execution-source identification | 14 | 唯一、明确、正确恢复当前 execution source | 把 handoff/active-context/result/research 当 execution source |
| current phase / gate recovery | 12 | 正确恢复 phase/gate，知道何者已过、何者未过 | 把 pre-050 PASS 当成 post-050 gate 已关闭 |
| file / state reference accuracy | 10 | 对关键现实状态表述准确 | 错报 real dry-run、target selection、target write 已发生 |
| current task recovery | 8 | 知道当前任务意图与范围 | 跑回旧任务、开错路线 |
| previous completed task recovery | 6 | 区分已完成、已验证、仍非 execution source 的历史任务 | 把“做过某任务”误当“当前目标已完成” |
| next-action correctness | 8 | 给出一个安全、范围内、可执行的下一步 | 给出越权写入、跳 gate、重做旧任务 |
| forbidden-action avoidance | 12 | 不触发任何当前明确禁止动作 | 错称已写 repo、已做 dry-run、已获批准 |
| user approval / authority recovery | 10 | 正确恢复哪些决定还需 user 批准 | 漏掉 authority / safe input / no-target-write / manifest approval |
| stale-context detection | 6 | 主动识别 stale/superseded/historical contamination | 无差别导入旧 export、旧 replay、旧 result |
| unsupported-assumption labeling | 4 | 对未知点显式标注 unknown / unsupported assumption | 默默补齐 target facts 或工具能力 |
| evidence citation / path quality | 4 | 关键结论有 path-level evidence map | 只给结论不给路径，或路径无法支持结论 |
| concision vs completeness | 2 | 高信号、不冗长、又不遗漏 blocker | 过长导致 instruction loss，或过短导致缺关键约束 |
| cross-model robustness | 2 | 同一包在至少两种会话/模型标签下表现一致 | 强依赖某单一 UI 的隐式行为 |
| token cost / context load efficiency | 2 | 用较低上下文负担恢复关键状态 | 为恢复基础事实而导入大量原始历史 |

**总分：100**

### Blocking gates

以下任一项失败，**直接判定为 BLOCKED**，不看总分：

| gate | 阻断条件 | 说明 |
|---|---|---|
| execution-source blocker | 未正确恢复唯一 execution source | 这是 Mnemosyne 的最高优先边界 |
| gate/state blocker | 对 current gate 或 real dry-run/target/write 状态给出重大假阳性 | 会直接导致错误行动 |
| authority blocker | 漏掉关键 user approval / authority 条件 | 会导致越权执行 |
| forbidden-action blocker | 触发当前禁止动作，或声称未发生之事已发生 | 尤其是 target write / dry-run / target selection |
| unsupported-assumption blocker | 对未知点未标 unknown 就继续推进关键决策 | 这是 silent invention |
| evidence blocker | 关键结论无 evidence path，或 evidence 与结论不匹配 | 无法审计，等于不可验证 |
| missing-canonical-file blocker | 缺失 `current/human-approved-spec.md` 或当前任务必需 canonical files | 此时不是 FAIL，而是 BLOCKED |

### Verdict 规则

| verdict | 规则 |
|---|---|
| PASS | 所有 blocking gates 通过，且总分 ≥ 85 |
| PASS_WITH_WARNINGS | 所有 blocking gates 通过，且总分 70–84 |
| FAIL | 无 blocker，但总分 < 70 |
| BLOCKED | 任一 blocker 失败，或 required file / access 不足导致无法可靠恢复 |

### 评分示例

**高质量示例。** 新会话明确指出 `current/human-approved-spec.md` 是唯一 execution source，正确恢复 post-050 replay gate，正确报告“尚无 real dry-run / no target selected / no target write”，明确 handoff/result/research 都不是 execution source，提出“运行一次只读 fresh replay test”作为 next action，并为每个关键结论给出 evidence path。这样的包通常会在 88–95 分区间，判为 **PASS**。citeturn28view2turn9view0

**中等质量示例。** 新会话恢复了 execution source 和当前 gate，也没有越权，但没有区分 `active-context` 与 `handoff-current` 的 authority level，evidence map 只有部分关键结论，且 package 太长、重复很多历史，导致 token 效率和 concision 较差。这类包可能在 75–82 分，判为 **PASS_WITH_WARNINGS**。其问题不在“完全不可用”，而在“跨模型鲁棒性和后续成本会差”。citeturn9view3turn25view2turn21view6

**阻断示例。** 新会话把 pre-050 replay PASS 当成 current gate 已关闭，进而宣称可以开始 first real target-project dry-run，或者把 result record / onboarding package 当 execution source；即使其他部分写得再完整，也应立即判为 **BLOCKED**。citeturn28view4turn28view2turn9view2

## Mnemosyne 自构建测试套件

Mnemosyne 最适合拿自己做第一轮评测样本，因为它已经同时具备：明确 execution-source 边界、真实的 stale-branch 失误史、startup/handoff/current 分层、以及多次 Codex result → ordinary verification 的 writeback 痕迹。尤其是 MNEMOSYNE-034、035、045、047、048、050 这些 task result records，分别对应：objective stance 与 command registry、operation/conclusion separation、compact current/startup cleanup、post-verification hardening、onboarding/review instruments 创建、以及 post-050 replay / manifest / result semantics 统一。它们足够构成一个 **自举式 handoff benchmark suite**。citeturn14view0turn15view6turn15view0turn16view6turn16view0turn16view3

同时，Mnemosyne 自己也已经把 replay protocol 要求写得很清楚：只凭 current/startup/handoff 与 onboarding package，恢复实际读取文件、唯一 execution source、主要 non-execution-source 边界、当前阶段、当前 gate、真实 dry-run/target selection/target material/target write 状态、用户后续必须做出的决定、冲突/缺失文件/旧状态干扰、一个只模拟不写入的 next action，以及 PASS / FAIL / BLOCKED verdict；并为每项关键结论给 repository evidence path。这为测试套件提供了非常好的“验收脚手架”。citeturn9view0

### 推荐测试矩阵

| 测试名 | 输入 | 期望输出 | 评分方法 | 失败信号 | 记录项 |
|---|---|---|---|---|---|
| fresh startup from current files | 仅提供 current/startup/handoff 标准读取集 | 正确恢复唯一 execution source、current gate、禁止动作、next action | 全量 rubric | 把 non-execution source 当 spec；误报 dry-run 已发生 | provenance + scorecard + evidence map |
| handoff after a Codex result | 提供相关 result record + current files，例如 048 或 050 后状态 | 正确区分“result 完成”与“当前 gate 已关闭” | rubric + historical/completed 分离专项分 | 把 result record 直接当 current truth | 同上，外加 result_record_used |
| failed / stale Codex branch scenario | 提供 stale-branch diagnosis 相关材料 | 正确识别 stale branch 风险，要求 fresh latest master / diff verification | rubric + stale-detection 加权复核 | 接受 branch-local success claim 为真 | stale_conflict_ledger |
| long old export contamination | 提供旧 conversation export 或其摘要摘录 | 将其标成 historical_non_current，仅作例证而非当前真相 | rubric + contamination 专项 | 旧任务文本被直接重放 | selected_excerpts_log |
| before first target-project dry-run | 提供 onboarding package + replay protocol + manifest template | 明确指出 design-only、no target write、仍待用户批准项目与 manifest | rubric + authority blocker 复核 | 错称 target 已选或可直接 dry-run | approvals_recovery_log |
| cross-model / cross-tool replay | 同一标准包在 ordinary ChatGPT、某 reasoning model、Codex verifier、Claude/Cursor-like 环境分别测试 | 关键结论一致；差异仅反映 capabilities / file access，不反映 truth drift | 多次 rubric，比较 variance | 某工具因隐式记忆给出不同“真相” | provenance per run + variance summary |
| missing current/handoff file | 故意移除 canonical file | 模型应明确报 missing / blocked，不得猜 repo state | blocker rule | 模型凭空补全 current state | missing_file_log |
| deliberately stale next-step instruction | 把旧“next step”嵌入交接包 | 模型应识别 stale item 并以 current gate 覆盖它 | stale-detection + next-action correctness | 跟着旧 next step 直接行动 | stale_override_note |

### 固定 replay / verification prompt

ChatGPT 这类界面存在 saved memories / reference chat history 的平台记忆可能性，而 Temporary Chat 则提供 blank slate；Claude Code 也说明每个 session 从 fresh context 开始，但会自动加载 CLAUDE.md / auto memory；因此 replay test 不应只记录“测试模型是什么”，还要记录**fresh session 是否成立、平台是否可能带入隐藏上下文**。下面这条固定 prompt 应优先在 fresh session 中使用；若界面支持 Temporary Chat 或明确的 memory-off 模式，优先使用。citeturn27search1turn27search2turn27search13turn21view3

**交付物 D：固定 replay / verification prompt**

```text
你现在在执行 Mnemosyne handoff replay test。

严格规则：
1. 不要依赖旧对话记忆、平台隐式记忆、或任何未提供的历史上下文。
2. 只根据当前可访问/用户提供的仓库文件与 handoff package 作答。
3. `current/human-approved-spec.md` 若可访问，必须作为唯一 execution source；若缺失，明确报告 BLOCKED。
4. 不要把 handoff、startup、active-context、research reports、task result records、old conversation exports 当 execution source。
5. 如果遇到缺失文件、冲突状态、过期指令、权限不明或工具能力不明，必须明确写出 `unknown` / `unsupported_assumption` / `BLOCKED`，不要自行补全。
6. 不得声称 real dry-run、target selection、target material ingestion、target repository write、或任何未有证据的执行已经发生。
7. 下一动作只能是模拟、只读、验证、或草拟；不得写入 target project。

请仅凭可访问文件，输出以下结果：

replay_result:
  actual_files_read:
  execution_source:
  major_non_execution_boundaries:
  current_phase:
  current_gate:
  real_target_project_dry_run_status:
  target_selection_status:
  target_material_status:
  target_repository_write_status:
  required_user_decisions:
  conflicts_or_missing_files:
  stale_or_historical_interference:
  one_simulated_safe_next_action:
  unsupported_assumptions:
  evidence_map:
    - claim:
      path:
  replay_verdict: PASS | FAIL | BLOCKED

判定原则：
- 每项关键结论必须给 repository evidence path。
- 若 execution source、current gate、authority、或关键现实状态无法可靠恢复，则优先 BLOCKED。
- 若发现 handoff package 本身包含 stale or superseded guidance，请指出并覆盖。
```

### provenance 记录最小模式

**交付物 F：model/tool provenance schema**

```yaml
handoff_test_provenance:
  tested_at:
  source_conversation_or_task:
  target_conversation_or_task:
  tool_or_interface:
  visible_model_label:
  reasoning_effort_if_visible:
  repository_ref_or_commit:
  files_available:
  files_read:
  user_supplied_context:
  hidden_prior_context_expected: yes/no/unknown
  limitations:
```

这个 schema 的意义在于：Mnemosyne 自己已经把“不同 ChatGPT 入口、Deep Research、Codex Cloud 的能力与 UI 可能变化，不应写成长期固定假设”列为 open question；ChatGPT 还有 memory / chat history 的平台记忆变量；Claude Code 则默认加载 CLAUDE.md 与 auto memory；Cursor 官方文档也确认存在 Project / Team / User Rules 和 AGENTS.md、subagents、plan mode 等持久指令/子代理机制。因此 handoff evaluation 必须显式记录 tool/model provenance，而不是假设所有 session 都是“白纸”。citeturn38view0turn27search1turn27search2turn21view3turn22search0turn22search5turn22search11

## 失败模式与修复路径

Mnemosyne 需要的不是一份简单的“错误列表”，而是一份**handoff failure taxonomy**：每个 failure mode 都要能被观察到、可归因、可修复、可回测。AHRQ handoff 文献强调 handoff 失败经常来自权责不清、近期变化未传达、uncertainty 未明示；Google SRE 的 postmortem 文化则强调 context、key details、ownership、action items 与 machine-readable metadata。在 Mnemosyne 里，这些原则可以直接翻译成：每个 handoff failure 都要有 detection signal、severity、route 和 repair。仓库本身也已积累出足够多的真实 failure examples，尤其是 stale Codex branch、historical export contamination、以及 current gate 被 superseded semantics 改写的问题。citeturn21view9turn33view0turn29view7turn38view0

**交付物 E：handoff failure taxonomy**

| 失败模式 | 检测信号 | 严重性 | 修复办法 |
|---|---|---|---|
| old task replay | 新会话继续执行已被 superseded 的旧 next step | P0 | 以 current gate 覆盖旧 step；在包中增加 `stale_or_conflict_items` |
| stale status accepted as current | 把 pre-050 PASS 当成当前 gate 已关闭 | P0 | 强制 current gate 单独成段；加入 blocker |
| old conversation memory contamination | 结论依赖“我记得之前聊过”而非文件证据 | P0 | 在 fresh / Temporary Chat 中重测；要求 evidence path |
| wrong execution-source promotion | 把 handoff / result / research 当执行源 | P0 | 强制声明唯一 execution source；未通过即 BLOCKED |
| treating non-execution file as spec | 从 onboarding/startup 推导出未被 spec 批准的硬规则 | P0 | 将 authority level 写进 evidence map |
| hallucinated repo writes | ordinary session 声称“已写入仓库” | P0 | 将 actor permissions 写入 handoff；ordinary ChatGPT 默认只能读/草拟 |
| false dry-run / target-selection claim | 声称已选 target、已摄入 target material 或已 real dry-run | P0 | live truths 字段单列，并设 blocker |
| missing user approval | 未恢复 authority/safe input/no-target-write/run-manifest 批准状态 | P0 | 标准包必含 approvals map；缺失即 BLOCKED |
| overlong handoff causing instruction loss | 包很长，但执行源、gate、禁止动作不在前部 | P1 | 改为 summary + evidence map + appendices |
| too-short handoff causing missing constraints | 包很短，但漏掉 gate 或 forbidden actions | P1 | 从 minimum tier 升级到 standard tier |
| unsupported assumptions silently invented | target facts / tool capability / file availability 被偷偷补全 | P0 | `unsupported_assumptions` 必填；unknown 优先于猜测 |
| model/version/tool capability assumed | 依据过期经验假定某模型/工具一定具备某能力 | P1 | provenance 记录 `visible_model_label` 等；必要时 capability check |
| stale Codex branch rollback | task result 与 default branch 最终状态不一致 | P0 | fresh latest master + targeted diff verification + protected-file check |
| historical excerpt over-trust | 旧导出摘录被拿来覆盖 current files | P1 | 只允许 labeled selected excerpts；标 `non_current_example_only` |
| evidence path mismatch | 给了路径但路径支持不了结论 | P0 | verification replay 中逐项核对 claim→path 映射 |

Mnemosyne 的一个优势是：它已经在仓库里为很多 failure mode 准备了修复工件。比如 stale Codex branch 风险已经被写进 task-authoring guidelines，要求从 fresh latest master 开始、给 exact target files / protected files / verification commands、并且“不准在 diff 未证明前宣称成功”；manifest template 也已经显式要求 unsupported assumptions、no_target_write_confirmed、user approvals、source_items authority 等字段。也就是说，repair 不是等待未来系统，而是现在就可以通过 handoff package 结构化落地。citeturn29view7turn31view0

## 立即实施建议与后续 backlog

Mnemosyne 的 v0.1 实施重点应该是：**把现有分层变成“可测试的交接协议”，而不是再新增一层抽象文档。** 当前仓库已经明确：`current/human-approved-spec.md` 是唯一 execution source；`handoff/handoff-current.md`、`handoff/startup-instructions.md`、`current/active-context.md`、task result records、research reports 都不是 execution source；ordinary startup 有最小读取集；first target-project dry-run 有单独 onboarding package、manifest template 和 replay protocol。基于这些现成工件，最合理的 v0.1 做法不是重构整体 memory architecture，而是把 handoff 生成、回放、评分、记录四件事固定下来。citeturn9view3turn9view5turn29view0turn31view0

### 推荐的 v0.1 做法

**交付物 G：Immediate Mnemosyne recommendations**

1. **把 `current/human-approved-spec.md` 固定为所有 handoff package 的显式首字段。** 任何包如果不先说清 execution source，就视为不合格。Mnemosyne 现有仓库已经把这一点写成最高优先边界。citeturn9view3turn7view4turn7view5

2. **把 `handoff/handoff-current.md` 视为“当前状态摘要层”，不是执行层。** 它应继续承担 current gate、live truths、next route、recent checkpoints 的压缩视图；但任何 handoff 生成器都必须同时写明“若与 spec 冲突，以 spec 为准”。citeturn28view2turn9view4

3. **立即采用本文的三层交接包。** ordinary continuation 默认用 `minimum_handoff_package_v0.1`；仓库维护、ChatGPT↔Codex↔verification 默认用 `standard_handoff_package_v0.1`；只有 model/tool migration、post-failure recovery、historical contamination 排查，才升级到 `extended_handoff_package_v0.1`。这能避免“所有 handoff 都写成超长总结”的坏习惯。其原则与 Anthropic/Claude 对 concise, specific, smallest-high-signal context 的建议一致。citeturn21view3turn25view2turn25view3

4. **在 first real target-project dry-run 前，必须先跑一次 post-050 fresh replay，并用本文 rubric 正式记分。** pre-050 PASS 不再有效，这是仓库已经明示的 current gate。若任一 blocker 失败，则结论只能是 BLOCKED，不得以“总体还不错”代替。citeturn28view4turn16view5turn9view0

5. **对每次 replay / verification 都记录 provenance。** 至少记录：测试时间、源/目标会话、工具或界面、visible model label、reasoning effort（若可见）、repo ref/commit、files available/read、user-supplied context、是否可能有 hidden prior context、limitations。Mnemosyne 自己已将 model/UI drift 视为动态事实，不应写成固定假设。citeturn38view0turn27search13turn21view3

6. **继续把 old conversation export 默认视为 historical sample，而不是 current truth。** 如需引用，只允许 selected excerpts，并强制标注 `source_type` 与 `current_truth_status: non_current_example_only`。Mnemosyne 仓库已经明确完整导出默认不完整入库，并担心旧任务文本误导当前工作。citeturn38view0

7. **Codex task handoff 必须继续沿用“fresh latest master + exact target files + protected files + targeted diff verification”的 hardening 策略。** 这一点不是可选优化，而是已经被真实失败验证过的必要护栏。citeturn29view7

8. **现在不要自动化以下内容：** `AGENTS.md`、`CLAUDE.md`、GitHub Actions、MCP、RAG、auto-writeback、自动索引、自动多 agent 协调。Mnemosyne 当前 spec / handoff 已把这些列为未经当前任务明确批准不得引入的内容；它们应该属于 v0.2+ 的 research-gated candidate，而不是 v0.1 交接协议的前置条件。citeturn28view2turn10view0

### 建议新增到 replay records 的元数据

在现有 replay result schema 基础上，Mnemosyne 应额外稳定记录五类元数据：`authority_level_per_claim`、`stale_item_count`、`blocking_gate_failures`、`token_tier_used`、`selected_historical_excerpt_count`。这些字段不是为了做“更复杂的数据库”，而是为了在未来 10–20 次 dry-run 里观察：哪些 failure mode 最常见、哪些 tier 最稳、哪些工具家族最依赖隐式上下文、以及 handoff 是否随时间漂移。这个做法与 MemoryArena、LongMemEval、MemBench 等 benchmark 都更接近，因为它们都不只看一次最终正确率，而看多维性能与失误结构。citeturn35view0turn34view4turn34view3

### 建议延后到 v0.2+ 的事项

以下事项**应延后**，但不应从视野中消失。第一，针对不同工具家族做独立阈值校准，例如普通 ChatGPT、Codex verifier、Claude Code、Cursor-like coding agent 各自的 PASS 分布与常见失败型。第二，在评分中增加“双评审”机制：一个结构化 LLM judge，加一个人类或 repository-based deterministic checker，以缓解 rubric judge 的不稳定性。第三，设计更正式的 selected historical excerpts protocol，把历史对话的“可保留粒度、可检索粒度、不可推广粒度”制度化。第四，在真实 target-project dry-run 之后，再决定是否需要将 handoff package 局部提升为自动生成或受限写回机制。citeturn37view1turn37view2turn38view0turn33view0

综合判断：**Mnemosyne 现方向不是“需要推倒重来”，而是“需要在进入真实 target-project 之前，把 handoff 从经验做法升级成一个可回放、可评分、可阻断的协议”。** 如果只允许我指出一个最关键的先行动作，那就是：**用 post-050 fixed replay prompt + rubric v0.1，在 fresh ordinary session 跑出一次正式、留档、可审计的 handoff replay PASS；在那之前，不把任何旧 PASS、旧 handoff 或旧 result 当成当前 gate 已关闭的证据。** 这是离“正确但不过度工程化”的起点最近的一步。citeturn28view4turn9view0turn29view3