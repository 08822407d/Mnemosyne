---
raw_id: RAW-0008
source_type: user_and_chatgpt_handoff
status: preserved
sensitivity: private
language: zh-CN
---

# RAW-0008：模型迁移与约束生命周期

这不是完整原始对话，而是从早期 ChatGPT 讨论中整理出的第八阶段交接记录，用于设计 Mnemosyne 的模型迁移与约束生命周期机制。

## 1. 为什么需要模型迁移机制

Mnemosyne 的核心原则之一是：AI 模型是可替换的计算单元，不是长期真相源。

一个项目可能先用某个模型工作一段时间，后续再迁移到新模型、新工具或新的正式 AI 工作入口。迁移时不能简单采用以下两种极端做法：

- 完全丢弃旧模型加工版，从全部 raw 原文重新分析；
- 完全继承旧模型加工版，不回查原文，也不复审旧约束。

第一种方式可能消耗大量算力和时间，也可能引入新模型的新解释偏差。
第二种方式可能让旧模型的误解、过度摘要、旧能力限制和旧行为补丁长期固化。

因此，Mnemosyne 需要一个“继承为主、重点回查、约束复审、能力验证”的模型迁移流程。

## 2. 三层记忆区分

模型迁移时应区分三层：

1. Raw Evidence / 原文证据层
   包括 raw 记录、原始需求、原始反馈、上游 Agent 请求、完整交接材料等。
   它是最高证据源，但不应默认每次完整加载。

2. Canonical Memory / 模型无关正式记忆层
   包括 human-approved-spec、decision-log、core-object-model、requirement-intake-workflow、handoff-active-context-review 等用户确认或当前认可的设计成果。
   它是迁移时的默认基线。

3. Model-Specific Digest / 模型专用摘要层
   未来用于记录某个模型或工具的专用提示、行为补丁、上下文压缩策略、已知弱点和使用建议。
   当前只作为未来对象，不在本阶段实现具体文件。

## 3. 默认迁移策略

默认策略不是全量重分析，而是：

- 继承 Canonical Memory；
- 阅读当前 handoff 和 active-context；
- 阅读 open questions 和 TODO；
- 根据需要抽样或定向回查 Raw Evidence；
- 对旧模型专用约束进行复审；
- 生成迁移评估；
- 用户确认后才更新 human-approved-spec、handoff 或未来 model-specific digest。

## 4. 重分析等级

为控制算力和工作量，模型迁移时应分级：

### Level 0：不重分析

只继承当前 Canonical Memory。
适用于低风险、稳定、长期确认过的内容。

### Level 1：索引级复核

读取 human-approved-spec、active-context、handoff、decision-log、open-questions、todo 和 candidate-requirements。
适合作为默认迁移起点。

### Level 2：关键原文回查

只回查高风险、高价值、低置信度、曾被用户纠正过、涉及隐私/权限/执行源/自动化边界的 raw 记录。
适用于模型升级、重要流程调整或存在争议时。

### Level 3：全量重分析

重新读取大量 raw 或完整历史，重建需求理解。
只适合重大重构、旧整理版严重失真、安全事故、长期项目大复盘或迁移到完全不同能力范式的模型。

默认应使用 Level 1 + 局部 Level 2。
不应默认 Level 3。

## 5. 约束生命周期

Mnemosyne 后续会有许多规则和约束，例如：

- 不自动更新 human-approved-spec；
- 不默认全量读取 raw；
- 正文使用中文；
- Codex Cloud 当前只作为远程保存助手；
- 不提前创建 AGENTS.md / CLAUDE.md；
- 某些旧模型需要更强的防跑题约束；
- 某些模型需要更明确的“不要过度总结”指令。

其中有些约束是长期原则，有些只是旧模型能力不足时的补丁。

因此每条重要约束应有生命周期状态：

- active：当前生效；
- deprecated：已废弃；
- replaced：被新规则替代；
- model_specific：仅适用于某些模型或工具；
- review_on_model_upgrade：模型升级时必须复审；
- experimental：试运行；
- rejected：明确不采用。

重要约束应尽量说明：
- 约束内容；
- 适用范围；
- 为什么存在；
- 来源引用；
- 是否模型专用；
- 何时需要复审；
- 替代关系；
- 当前状态。

## 6. 新模型能力不能直接默认启用

新模型发布后，不能直接假设它：

- 一定更可靠；
- 一定能更好遵守指令；
- 一定能正确处理更长上下文；
- 一定不需要旧 handoff；
- 一定能减少 raw / index / active-context；
- 一定能自动维护用户画像或长期记忆；
- 一定适合直接写回 GitHub。

新能力必须通过小规模验证后，再进入正式工作流。

候选验证方向包括：
- 是否能稳定遵守 human-approved-spec；
- 是否能区分 raw / candidate / spec；
- 是否会把 candidate 当执行源；
- 是否会过度推断用户意图；
- 是否会在长上下文中遗漏关键约束；
- 是否能生成清晰 diff；
- 是否适合做需求查重；
- 是否适合做模型迁移复审。

## 7. 模型迁移输出

未来一次模型迁移可以产生：

- migration plan；
- migration review；
- constraint review；
- capability validation notes；
- raw recheck list；
- digest diff；
- new model-specific digest；
- human-approved-spec update proposal；
- handoff update proposal；
- open questions；
- TODO updates。

当前阶段只设计流程，不创建完整迁移目录或自动化机制。

## 8. 当前阶段边界

当前不做：
- 自动模型评测；
- 自动 raw 重分析；
- 自动约束清理；
- 自动生成 model-specific digest；
- 自动切换主力模型；
- 自动修改 AGENTS.md / CLAUDE.md；
- GitHub Actions；
- MCP；
- RAG；
- 多 Agent 自动协调。

当前只做：
- 建立迁移原则；
- 建立重分析等级；
- 建立约束生命周期状态；
- 记录未来模型迁移需要的输出；
- 更新当前候选需求、决策和 handoff。
