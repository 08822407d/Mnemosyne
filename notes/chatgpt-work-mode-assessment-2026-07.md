# ChatGPT Work 模式对 Mnemosyne 的适用性评估（2026-07）

```yaml
record_type: platform_mode_assessment_and_candidate_guidance
created_by_task: MNEMOSYNE-114
authority_level: non_execution_source_candidate_guidance
consulted_at: 2026-07-13
execution_source_modified: false
candidate_guidance_promoted: false
```

## 1. 目的

本文件评估 OpenAI 新推出的 ChatGPT Work 是否适合 Mnemosyne 自身建设、跨模型复核、目标项目记忆系统设计和长周期维护任务。

它是平台能力评估和候选行为指导，不是执行源。`current/human-approved-spec.md` 仍是 Mnemosyne 唯一执行源。

## 2. 已核实的官方产品事实

根据 OpenAI 官方产品页、Help Center 和 release notes：

- ChatGPT 现在区分 Chat、Work 和 Codex 三种工作体验。
- Chat 适合提问、搜索、讨论和快速协作。
- Work 面向更长、更复杂的研究与交付任务，可分析信息、使用已连接应用和文件，并产出文档、表格、演示文稿、报告和 Sites。
- Work 允许用户跟踪进度、回答问题、改变方向并批准重要动作。
- Work 支持一次性、定时、触发式或监控型 Scheduled Tasks。
- Codex 仍是软件开发、代码、命令、测试和 repository 工作的专用体验。
- Web/mobile Work 在云端运行；桌面 Work 在获得许可后还可使用本地文件和桌面应用。
- 截至发布时，cloud Work conversations 不会出现在 desktop Work；desktop Work threads 和本地文件留在该电脑上。普通 Chat conversations 会在 web 和 desktop 间同步。
- Project 可以把相关 conversations、files 和 instructions 放在一起，但这不能替代显式的 Mnemosyne handoff。
- Plan mode 会先收集上下文、提问并形成步骤计划，用户可以修改或批准后再开始执行。
- Plugin Directory 在 ChatGPT web/desktop、Work 和 Codex 中可用；具体 plugin/app 是否可读、可写、是否需要确认，仍取决于 plan、workspace、role、surface、region、app 配置和源系统权限。
- Work 使用与 Codex 相同的 usage structure；实际消耗随任务而变化。

官方来源：

- https://openai.com/chatgpt-work/
- https://help.openai.com/en/articles/20001275
- https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- https://help.openai.com/en/articles/20001276
- https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex

## 3. 当前结论

### 3.1 新维护对话的 handoff 接收与路径选择

推荐使用：**普通 Chat，GPT-5.6 Sol + Pro**。

理由：

- 第一步是读取 handoff、核验仓库状态、解释权限边界并让用户选择路线；这是交互式治理和决策任务，不需要 Work 的长自主执行能力。
- 当前仓库维护依赖精确的 execution-source / authority / frozen-artifact 边界；普通 Chat 更适合逐步确认和小范围 GitHub 文档 PR。
- 引入 Work 会额外增加 context/surface 迁移问题，而当前任务尚未需要多应用整合、长时运行或成套交付物。

### 3.2 适合考虑 Work 的 Mnemosyne 任务

Work 候选场景：

1. read-only comprehensive health review：需要读取许多报告和状态文件，形成完整审计报告、矩阵和建议包；
2. 大型独立设计或对照设计：需要多文件综合、计划、分阶段产出多个可交付 artifact；
3. 跨应用证据整合：需要同时使用 GitHub、Drive、Gmail、Notion 或其他授权来源；
4. 周期性监控：例如平台能力变化、研究 delta、依赖更新或固定节奏状态报告；
5. 需要 Plan mode 先审阅方案，再让 agent 长时间执行的任务。

这些任务应优先是 read-only 或严格限定写入范围。任何 external action 仍须单独满足 platform permission 与 Mnemosyne task authority。

### 3.3 更适合普通 Chat 的任务

- handoff receive 与路线选择；
- 小范围 maintainer triage；
- 用户决策问答；
- 单个或少量文档的证据核验；
- 低范围文档修补与 ready PR；
- 需要频繁人工判断、暂缓和改变优先级的维护工作。

### 3.4 更适合 Codex 的任务

- 软件开发、脚本、测试、命令和 repository implementation；
- 多文件 deterministic patch；
- 需要 shell、git diff、test suite、编译或本地环境的工作；
- 大范围 repository refactor。

Work 不应因为“任务很长”就自动替代 Codex；任务本质仍是首要判断依据。

## 4. 候选 surface-selection 规则

以下仅为候选规则，尚未进入执行源：

```yaml
candidate_surface_selection:
  Chat:
    default_for:
      - interactive_governance
      - route_selection
      - bounded_repository_review
      - small_documentation_repairs
      - user_decision_loops
  Work:
    consider_when_at_least_two_are_true:
      - multi_source_context
      - long_running_research_or_analysis
      - multiple_finished_deliverables
      - cross_app_workflow
      - scheduled_or_monitoring_requirement
      - plan_review_before_execution_is_valuable
  Codex:
    default_for:
      - software_development
      - repository_commands_and_tests
      - deterministic_multi_file_patch
      - local_or_remote_codebase_work
```

在建议启动 Work 前，Agent 应显式告诉用户：

- `recommended_surface: Chat | Work | Codex`；
- 为什么当前任务适合该 surface；
- 使用 web/cloud Work 还是 desktop/local Work；
- 需要连接哪些 apps、files 或 project；
- 哪些动作是 read-only，哪些动作会改变外部状态；
- 预期交付物；
- 完成后如何汇报和交接。

## 5. Work 结果的建议汇报与交接格式

Work 任务结束时应返回一个可迁移的高信号 package，至少包括：

```yaml
work_result_handoff:
  work_context_id_or_title:
  execution_surface: web_cloud_work | mobile_cloud_work | desktop_local_work
  model_and_reasoning_setting:
  objective:
  inputs_used:
  connected_apps_used:
  external_actions_attempted_or_completed:
  approvals_requested_and_received:
  deliverables:
  repository_or_file_changes:
  checks_performed:
  unresolved_questions:
  limitations:
  safe_next_action:
  canonical_storage_status:
```

不得假设 Chat、cloud Work、desktop Work 和 Codex 自动共享完整历史。跨 surface 继续工作时，应使用 repository-backed handoff、明确的 artifact 路径或用户提供的文件。

## 6. 当前不立即写入行为执行源的原因

ChatGPT Work 刚刚发布并仍在逐步 rollout。以下问题尚需实测或 delta research：

- 同一 Project 中 Chat 与 Work 的实际可见上下文范围；
- web/mobile cloud Work 与 desktop Work 的 artifact、thread 和 file 迁移行为；
- GitHub plugin 在 Work 中的实际 read/write action 列表和确认行为；
- Work 的 usage、长任务中断、恢复和结果持久化方式；
- Work 产出的文件如何最可靠地进入 Mnemosyne repository；
- Work 与普通 Chat/GitHub App/Codex 在 PR、diff 和审计上的分工边界。

因此，现阶段只保留候选指导。建议先做一次受限、read-only 的 Work pilot，再决定是否将 surface-selection 规则写入 `current/human-approved-spec.md`。

## 7. 建议的受限 Work pilot

```yaml
pilot:
  surface: ChatGPT_Work_web_or_desktop_as_available
  objective: produce_read_only_Mnemosyne_health_review_package
  repository_access: read_only
  required_sources:
    - README.md
    - current/human-approved-spec.md
    - current/review-and-validation-status.md
    - notes/codex-task-results/MNEMOSYNE-113-result.md
  prohibited:
    - repository_write
    - execution_source_update
    - target_workspace_or_material_actions
    - regression_formalization
    - paused_route_resumption
  required_output:
    - source_manifest
    - findings_with_evidence_paths
    - surface_behavior_observations
    - limitations_and_handoff_package
```

Pilot 通过后，仍需在普通维护 Chat 中审查其结果，再决定是否创建执行源更新任务。
