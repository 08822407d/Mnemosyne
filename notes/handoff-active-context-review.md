# Handoff, Active Context, and Review Workflow / 交接、当前上下文与回顾机制

这是 Mnemosyne 当前阶段用于跨对话、跨模型、跨工具恢复工作的交接和回顾机制草案。

## 1) active-context 定义

### 用途
- 作为当前工作集，帮助会话快速进入“正在做什么”。

### 应包含什么
- 当前阶段；
- 当前目标；
- 已确认原则（简要）；
- 当前边界（不要做什么）；
- 最相关文件；
- 下一步建议。

### 不应包含什么
- 全量 raw 原文；
- 大量历史细节；
- 未确认内容的执行化结论。

### 是否执行源
- 否。

### 何时更新
- 阶段推进后；
- Human-Approved Spec 变更后；
- 当前目标变化后；
- 关键 open question / TODO / decision 变化后；
- 切换工具或会话入口前。

### 内容长度原则
- 保持短小、可快速读取；
- 细节转移到 notes/raw，并保留路径引用。

## 2) handoff-current 定义

### 用途
- 作为新会话启动时的交接卡，帮助 AI 快速接手。

### 应包含什么
- 仓库定位；
- 当前阶段与主线；
- 已完成里程碑；
- 执行源与非执行源边界；
- 当前不能误做事项；
- 下一步建议。

### 不应包含什么
- 全量 raw 内容复制；
- 全量 candidate 列表逐条复述；
- 与当前主线无关的长历史。

### 是否执行源
- 否。

### 何时更新
- 每阶段结束后；
- 切换模型/工具/对话前；
- Human-Approved Spec 重要变更后；
- 长时间暂停前后。

### 与 active-context 的区别
- active-context 更偏“当前工作内存”；
- handoff-current 更偏“新会话启动卡”。

## 3) 未来 AI 会话推荐读取顺序

1. README.md
2. current/human-approved-spec.md
3. current/active-context.md
4. handoff/handoff-current.md
5. current/open-questions.md
6. current/todo.md
7. notes/core-object-model.md
8. notes/object-templates-and-id-rules.md
9. notes/requirement-intake-workflow.md
10. notes/decision-log.md
11. notes/candidate-requirements.md
12. raw/ 按需回查

## 4) 阶段性回顾机制

### 回顾目标
- 检查 raw 抽取覆盖率；
- 检查 candidate 长期 pending；
- 检查 open questions 和 TODO 的积压；
- 检查 spec 是否仍与已接受决策一致；
- 检查 handoff/active-context 可接手性；
- 检查重复或冲突需求；
- 检查隐私敏感标记；
- 检查模型迁移相关旧约束。

### 触发条件
- 每阶段结束；
- 新增一批 raw；
- 切换主力模型；
- 切换主要工具入口；
- 交付目标项目前；
- 长暂停后恢复；
- 需求冲突明显增加时。

### 回顾对象
- raw
- candidate requirements
- open questions
- todo
- decision log
- human-approved-spec
- handoff / active-context

### 可能输出
- updated active-context
- updated handoff-current
- candidate cleanup notes
- open question review
- TODO review
- decision review
- similarity/conflict notes
- human-approved-spec update proposal
- model migration review TODO

### 当前不自动化
- 仅手工触发与更新，不实现自动提醒、自动扫描、自动摘要。

## 5) 冲突处理

如果 active-context、handoff 或回顾记录与 human-approved-spec 冲突，应以 human-approved-spec 为准，并将冲突登记为 open question。

## 6) 当前阶段边界

当前不实现：
- 自动生成 handoff；
- 自动压缩 raw；
- 自动索引；
- 自动提醒回顾；
- GitHub Actions；
- AGENTS.md；
- CLAUDE.md。


## 模型迁移场景补充

- 模型迁移前应检查 `handoff-current` 是否足以让新模型接手。
- 模型迁移时应复核 `active-context` 是否过期。
- 模型迁移后应更新 `handoff-current`。
- 若新模型对旧 handoff 理解有偏差，应登记为 open question 或 candidate requirement。
- raw 仍按需回查，不默认全量加载。


## 交付场景补充

- 交付给目标项目前，应生成或更新 Handoff Package。
- 目标项目启动时应读取其自己的 handoff / active-context。
- Mnemosyne 的 handoff 不应直接替代目标项目 handoff。
- 交付后若目标项目独立演化，应在 drift review 中检查 handoff 是否偏离原设计。
