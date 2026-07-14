# Handoff Guidance Loading — Open Question

> Non-execution-source live open-question record. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
open_question_id: HO-GUIDANCE-001
record_type: live_non_execution_source_open_question
created_by_task: MNEMOSYNE-116
latest_updated_by_task: MNEMOSYNE-117
status: open_requires_deliberate_review
user_decision_recorded: true
settled_behavior:
  authority_after_MNEMOSYNE_116_merge: current/human-approved-spec.md#15-交接与续接正确性原则
  mnemosyne_owned_handoff:
    receiving_sequence:
      - receive_authorized_handoff_package
      - execute_Load_Mnemosyne_guidance_as_a_separate_operation
      - continue_received_task_under_refreshed_constraints
    explicit_package_instruction_required: true
  target_project_business_handoff:
    load_target_project_confirmed_constraints_or_owner_rule: true
unsettled_behavior:
  question: should_a_target_project_business_conversation_also_load_Mnemosyne_guidance
  current_answer: undecided
  universal_default_approved: false
  required_task_local_field: yes | no | unknown_requires_user_decision
  task_local_choice_is_global_precedent: false
execution_source: current/human-approved-spec.md
```

## 中文说明

已经确定的规则有两条：

1. Mnemosyne 自身的交接包必须显式要求新对话在接收交接包之后，单独执行“加载 Mnemosyne 指导约束”，然后再继续交接任务。
2. 如果交接的是具体目标项目中的业务对话，并且该项目已有确认过的约束指导、owner rule 或 execution source，新对话应先加载该项目自己的约束。

第一条以及第二条中“先加载项目自身约束”的部分，已由用户明确批准写入 `current/human-approved-spec.md` §15；本文件不重复承担执行源角色，只记录相邻未决问题。

仍未决定的问题是：

> 具体目标项目的业务对话在加载项目自身约束后，是否还应同时加载 Mnemosyne 的约束指导？

## 为什么不能直接默认回答“是”

- Mnemosyne 可能只是设计该项目记忆系统的方法论来源，而不是目标项目业务对话的运行真相源。
- 直接加载 Mnemosyne 维护约束可能把元仓库的维护路线、治理术语或边界错误地带入业务任务。
- 目标项目自己的 owner rule、execution source 和业务安全规则应优先决定业务对话行为。

## 为什么也不能直接默认回答“否”

- 某些目标项目仍可能依赖 Mnemosyne 提供的交接正确性、证据分层、安全、用户操作分离或 no-write 约束。
- 如果项目约束包没有完整吸收这些规则，完全不加载 Mnemosyne 指导可能降低续接一致性。

## 当前处理方式

在该问题正式裁决前，每一份目标项目业务交接包必须显式记录：

```yaml
receiver_guidance_load:
  project_guidance: required
  mnemosyne_guidance: yes | no | unknown_requires_user_decision
```

并遵守：

- `project_guidance` 不能被省略；
- `mnemosyne_guidance` 不得静默推断；
- `unknown_requires_user_decision` 表示该次交接在继续前需要明确的 task-local 决定；
- 一次 `yes` 或 `no` 只适用于该次交接，不构成全局先例；
- 不得仅因为 Mnemosyne 参与过设计，就把 Mnemosyne maintenance live state 当成目标项目业务对话的行动计划；
- 若任务本身同时属于 Mnemosyne 维护或验证工作，可以基于该明确范围另行加载 Mnemosyne 指导。

## 后续评估建议

未来裁决应至少比较：

- 仅加载目标项目约束；
- 目标项目约束加一份经过裁剪的 Mnemosyne 通用约束；
- 完整加载 Mnemosyne 指导但显式禁止 maintenance-route import。

评估维度应包括任务污染风险、authority 冲突、交接正确性、上下文成本、业务可用性和可审计性。本记录本身不选择任何方案。
