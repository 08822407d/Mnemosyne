# Model Migration and Constraint Lifecycle / 模型迁移与约束生命周期

这是 Mnemosyne 当前阶段用于处理模型升级、工具切换和约束复审的流程草案。

## 1) 三层记忆区分

1. Raw Evidence / 原文证据层
   - 保存原文、反馈、交接、上游请求。
   - 是最高证据源，但不默认全量加载。

2. Canonical Memory / 模型无关正式记忆层
   - 包括 human-approved-spec、decision-log、core-object-model、requirement-intake-workflow、handoff-active-context-review 等。
   - 作为迁移默认基线。

3. Model-Specific Digest / 模型专用摘要层
   - 未来用于模型/工具专用提示、补丁、压缩策略。
   - 当前是未来对象，不在本阶段实现。

## 2) 默认迁移策略

- 继承 Canonical Memory。
- 按需回查 Raw Evidence。
- 复审旧模型专用约束。
- 先验证新模型能力，再决定是否启用新能力。
- 不默认全量重分析。

## 3) 重分析等级

### Level 0：不重分析
- 仅继承 Canonical Memory。
- 用于低风险、稳定内容。

### Level 1：索引级复核
- 读取 spec/context/handoff/decision/open-questions/todo/candidate。
- 作为默认迁移起点。

### Level 2：关键原文回查
- 回查高风险、高价值、低置信度、曾被纠正、涉及权限与执行边界的 raw。
- 用于升级、争议或关键流程变更。

### Level 3：全量重分析
- 大范围回读 raw 或完整历史。
- 用于重大重构、严重失真、安全事故或范式级迁移。

默认推荐：**Level 1 + 局部 Level 2**。

## 4) 约束生命周期状态

- `active`
- `deprecated`
- `replaced`
- `model_specific`
- `review_on_model_upgrade`
- `experimental`
- `rejected`

## 5) 约束条目建议字段（草案）

- `constraint_id`
- `title`
- `statement`
- `status`
- `applies_to`
- `rationale`
- `source_refs`
- `review_trigger`
- `replaced_by`
- `notes`

## 6) 新模型能力验证

新模型能力不能自动假设，需要小规模验证后再进入正式流程。

候选验证方向：
- 是否稳定遵守 human-approved-spec；
- 是否区分 raw / candidate / spec；
- 是否误把 candidate 当执行源；
- 是否过度推断用户意图；
- 是否在长上下文遗漏关键约束；
- 是否能产出清晰 diff；
- 是否适合需求查重；
- 是否适合模型迁移复审。

## 7) 模型迁移可能输出

- migration plan
- migration review
- constraint review
- capability validation notes
- raw recheck list
- digest diff
- new model-specific digest
- human-approved-spec update proposal
- handoff update proposal
- open questions
- TODO updates

## 8) 当前阶段边界

当前不实现：
- 自动评测；
- 自动重分析；
- 自动约束清理；
- 自动模型切换；
- GitHub Actions；
- MCP；
- RAG。


## 目标项目交付场景补充

- 不同目标项目可能使用不同模型或工具。
- 交付包应记录目标项目假定使用的模型 / 工具环境。
- 若目标项目后续迁移模型，应走目标项目自己的模型迁移流程。
- Mnemosyne 可为目标项目生成迁移建议，但不默认自动修改目标项目运行文件。
