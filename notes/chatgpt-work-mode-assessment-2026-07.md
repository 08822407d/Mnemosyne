# ChatGPT Work 模式对 Mnemosyne 的适用性评估（2026-07，2026-08 修订）

```yaml
record_type: platform_mode_assessment_and_candidate_guidance
created_by_task: MNEMOSYNE-114
last_amended_by_task: MNEMOSYNE-215
authority_level: non_execution_source_candidate_guidance
first_consulted_at: 2026-07-13
last_official_delta_check: 2026-08-15
status: candidate_guidance_with_owner_observation_and_pending_read_only_pilot
execution_source_modified: false
candidate_guidance_promoted: false
chat_to_work_observation_ref: notes/platform-observations/chat-to-work-follow-up-transfer-observation-2026-08.md
```

## 1. 目的

本文件评估 Chat、Work 与 Codex 对 Mnemosyne 自身建设、跨模型复核、目标项目记忆系统设计和长周期维护任务的适用性。

它是平台能力评估和候选行为指导，不是执行源。`current/human-approved-spec.md` 仍是 Mnemosyne 唯一执行源。

## 2. 2026-08 官方产品事实增量

根据 2026-08-15 访问的 OpenAI 官方资料：

- Chat 仍适合快速问答、搜索、讨论和交互式协作；
- Work 面向更长、多步骤的任务和可交付成果，可以分析信息并生成文档、表格、演示、报告或网站等；
- Codex 仍偏向代码、命令、测试和 repository 开发工作；
- Work 在符合条件的 web、mobile 和 desktop 表面可用；
- Chat 与 cloud Work 对话会共同出现在 Recents 中；
- 现有 Project 中可以选择启动 Chat 或 Work，Work 会使用该 Project 的上下文；
- **cloud Work 对话现在会在 web、mobile 与 desktop 间同步**；local desktop chats 仍保留在本机；
- Work 可以一次性运行，也可以通过 Scheduled Tasks 重复、按触发器运行或监控变化；
- Plan mode 可以先收集上下文、提问并形成计划，再由用户修改或批准后执行。

这修正了本文件 2026-07 初版中的旧说法：cloud Work conversations 不会出现在 desktop Work。该说法已被当前官方产品状态取代。

官方来源：

- `https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex`
- `https://help.openai.com/en/articles/6825453-chatgpt-release-notes`
- `https://openai.com/chatgpt-work/`

## 3. Owner 新观察：Chat 可能把后续任务转移到 Work

Owner 观察到，普通 Chat 对话中可能出现将接下来的任务转移到 Work 执行的能力。

当前尚不清楚：

- 由什么界面动作、提示词或任务特征触发；
- 是系统自动触发、模型建议，还是用户点击接受；
- 是否可以通过明确指令稳定触发；
- 转移的是完整上下文、Project context、附件、连接器权限还是一个摘要；
- Work 中的模型、推理强度、工具、用量、中断、恢复和结果返回如何确定；
- 是否在所有 plan、workspace、region 和 surface 上一致。

当前官方资料说明了如何选择 Work、如何从 Project 启动 Work 和 cloud Work 的跨设备同步，但没有说明普通 Chat 会自动或主动把“下一项任务”转换成 Work。因此这仍是 Owner-observed、待实验的平台能力，而不是已核实的操作规则。

详细记录和 pilot 问题：

```text
notes/platform-observations/chat-to-work-follow-up-transfer-observation-2026-08.md
```

## 4. 当前 surface-selection 候选规则

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
      - a_reliable_auditable_Chat_to_Work_handoff_is_available
  Codex:
    default_for:
      - software_development
      - repository_commands_and_tests
      - deterministic_multi_file_patch
      - local_or_remote_codebase_work
```

任务本质仍优先于时长。Work 不应仅因“内容很多”就替代 Chat 或 Codex。

## 5. 目前仍适合普通 Chat 的任务

- handoff receive、路线选择和 Owner 决策；
- 需要频繁澄清、暂停或改方向的治理工作；
- 小范围仓库核验和文档修补；
- 明确的 Ready PR 交付；
- 对 Work/Codex/外部研究结果的审查和采用决定。

普通 Chat 中出现 Work 转移建议时，不应自动接受。先说明目标、上下文、权限、材料、外部动作、用量、停止条件和结果交接。

## 6. 适合考虑 Work 的任务

- 大型 read-only health review 或多文件综合；
- 多个成品 artifact 的设计与交付；
- 跨 GitHub、Drive、Gmail、Notion 等已授权来源的证据整合；
- 计划先审后执行的长任务；
- 经明确授权的定时、触发或监控任务；
- 能从普通 Chat 可靠交接并返回可审计结果的冻结执行包。

这些任务应优先使用公开/合成或低敏感材料开始，严格区分 read-only 和 external action。

## 7. 更适合 Codex 的任务

- 软件开发、脚本、测试、命令和 repository implementation；
- 需要 shell、git diff、test suite、编译或本地环境；
- deterministic multi-file patch 或大范围 refactor。

Work 与 Codex 的选择不应只根据“agentic”程度，而应根据任务所需环境、工具、可复现性和审计边界。

## 8. Work 结果建议交接格式

```yaml
work_result_handoff:
  work_context_id_or_title:
  source_Chat_or_Project_ref:
  transfer_or_launch_method:
  execution_surface: web_cloud_work | mobile_cloud_work | desktop_cloud_work | desktop_local_work
  visible_model_and_reasoning_setting:
  backend_status: unknown_or_not_attestable
  objective:
  transferred_context_manifest:
  inputs_used:
  connected_apps_used:
  permissions_and_approvals:
  external_actions_attempted_or_completed:
  deliverables:
  repository_or_file_changes:
  checks_performed:
  usage_or_quota_observation:
  interruption_and_recovery_events:
  unresolved_questions:
  limitations:
  safe_next_action:
  canonical_storage_status:
```

不得仅因 Chat 与 Work 出现在统一 Recents 中，就假设它们自动共享完整隐藏上下文。跨 surface 的关键任务仍需要精确 handoff、artifact path、repository ref 或输入清单。

## 9. 当前不写入行为执行源的原因

仍需实测：

- Chat→Work 的真实触发方式和稳定性；
- 转移上下文、Project 指令、附件和连接器状态的精确范围；
- GitHub plugin/app 在 Work 中的实际 read/write/confirmation 行为；
- 用量、长任务中断、恢复和重复执行；
- Work 输出进入 Mnemosyne 的可靠 provenance；
- Chat、Work、Codex 的 PR、diff、测试和审计分工。

因此当前只保留候选指导和高优先级平台观察。

## 10. 建议的受限 pilot — 尚未授权

```yaml
pilot:
  status: CANDIDATE_NOT_AUTHORIZED
  surface: ordinary_Chat_to_cloud_Work_as_available
  objective: measure_trigger_context_permission_and_result_handoff
  material: public_synthetic_only
  repository_access: read_only
  external_actions: prohibited
  scheduled_or_monitoring_actions: prohibited
  required_outputs:
    - exact_UI_and_prompt_sequence
    - source_and_destination_identity_receipt
    - transferred_context_manifest
    - model_tool_permission_and_usage_observation
    - interruption_resume_result
    - limitations_and_handoff_package
```

Pilot 完成后，仍需在普通维护 Chat 中审查结果，再决定是否更新活动指导。
