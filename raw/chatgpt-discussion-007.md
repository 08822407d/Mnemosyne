---
raw_id: RAW-0007
source_type: user_and_chatgpt_handoff
status: preserved
sensitivity: private
language: zh-CN
---

# RAW-0007：handoff / active-context / 阶段性回顾机制

这不是完整原始对话，而是从早期 ChatGPT 讨论中整理出的第七阶段交接记录，用于设计 Mnemosyne 的 handoff、active-context 和阶段性回顾机制。

## 1. 为什么需要 handoff 和 active-context

Mnemosyne 的目标之一是让新旧 AI 对话、新旧模型、不同工具和不同工作入口能够稳定交接工作。

模型内部 memory 不能作为唯一真相源。普通对话窗口、Codex Cloud、未来的正式 ChatGPT 对话、Claude Code、Cursor 或其他工具都可能接手同一个仓库。因此必须有外部可读、简短、稳定的交接材料。

Handoff 和 active-context 的目标不是保存完整历史，而是让未来 AI 会话快速恢复当前工作状态。

## 2. active-context 的定位

active-context 是当前工作集。

它应回答：

- 当前项目处于哪个阶段？
- 当前主要目标是什么？
- 当前已经确认的关键原则是什么？
- 当前不要做什么？
- 当前最相关的文件有哪些？
- 当前下一步最应该推进什么？

active-context 不是完整历史，不是原文证据，不是执行源。
它是短期工作上下文，类似当前会话要装入“工作内存”的状态摘要。

## 3. handoff-current 的定位

handoff-current 是给未来 AI 会话的交接卡。

它应比 active-context 更面向“新会话启动”，帮助新 AI 立刻知道：

- 这个仓库是什么；
- 当前阶段是什么；
- 已经完成了哪些阶段；
- 当前要继续做哪一步；
- 哪些内容是执行源；
- 哪些内容只是证据、候选、TODO 或开放问题；
- 不能误做哪些事情；
- 下一步建议是什么。

handoff-current 不应复制全部 raw，也不应复制所有 candidate requirements。
它只保留恢复工作所需的最小上下文，并通过文件路径引用详细内容。

## 4. 读取顺序建议

未来 AI 会话接手 Mnemosyne 时，建议按以下顺序读取：

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
12. 只在需要核实时读取 raw/

原则：
- 先读执行源和当前上下文；
- 再读对象模型、流程和决策；
- 最后按需回查 raw；
- 不要默认全量读取 raw。

## 5. 什么时候更新 active-context

active-context 应在以下情况后更新：

- 阶段推进；
- Human-Approved Spec 发生变化；
- 当前目标发生变化；
- 重要 TODO 被新增、完成或延期；
- 重要开放问题被回答；
- 重要设计决策被接受或废弃；
- 准备开启新的正式对话或新的工具入口；
- 准备把阶段成果交给 Codex、Claude Code 或其他 Agent 处理。

active-context 应保持短小。
如果内容过长，应把细节移到 notes 或 raw，并在 active-context 中保留路径引用。

## 6. 什么时候更新 handoff-current

handoff-current 应在以下情况后更新：

- 每个阶段结束；
- 准备切换到新 ChatGPT 对话；
- 准备切换模型；
- 准备把任务交给 Codex Cloud 或其他 Agent；
- Human-Approved Spec 有重要变化；
- 当前工作主线发生明显变化；
- 准备暂停一段时间后再恢复。

handoff-current 应明确“下一步建议”，让未来 AI 不需要重新猜测当前任务。

## 7. 阶段性回顾机制

Mnemosyne 需要阶段性回顾，但当前不实现自动化。

阶段性回顾的目标是：

- 检查 raw 是否已经抽取为 candidate；
- 检查 candidate 是否有长期 pending；
- 检查 open questions 是否长期未处理；
- 检查 TODO 是否需要拆分、关闭或延期；
- 检查 human-approved-spec 是否仍然反映当前决定；
- 检查 handoff 是否还能让新会话顺利接手；
- 检查是否出现重复需求或冲突需求；
- 检查是否有内容应被标记为隐私敏感；
- 检查是否有旧模型约束需要在模型升级时复审。

## 8. 阶段性回顾触发条件

当前建议的触发条件：

- 每完成一个阶段；
- 每新增一批 raw 记录；
- 每次准备建立正式版 ChatGPT 对话；
- 每次准备切换主力模型；
- 每次准备把 Mnemosyne 的设计交付到某个目标项目；
- 每次发现需求重复、冲突或用户纠正旧结论；
- 每次长期暂停后恢复工作；
- 每次仓库结构明显变复杂。

当前只记录触发条件，不实现自动提醒或自动扫描。

## 9. 回顾输出

阶段性回顾可以产生以下输出：

- updated active-context；
- updated handoff-current；
- candidate cleanup notes；
- open question review；
- TODO review；
- decision review；
- similarity/conflict notes；
- human-approved-spec update proposal；
- model migration review TODO。

当前阶段只设计流程，不生成单独自动化文件。

## 10. 与执行源的关系

active-context 不是执行源。
handoff-current 不是执行源。
阶段性回顾报告不是执行源。
只有 Human-Approved Spec Entry / current/human-approved-spec.md 中用户确认后的内容是执行源。

如果 handoff、active-context 或 review 结果与 human-approved-spec 冲突，应以 human-approved-spec 为准，并把冲突登记为 open question。

## 11. 当前阶段边界

当前不做：
- 自动生成 handoff；
- 自动压缩 raw；
- 自动重建 active-context；
- 自动扫描 TODO；
- 自动查重；
- 自动索引；
- 自动提醒回顾；
- GitHub Actions；
- AGENTS.md / CLAUDE.md。

当前只做：
- 设计 handoff 和 active-context 的职责；
- 设计未来 AI 会话读取顺序；
- 设计阶段性回顾触发条件；
- 更新当前 handoff 和 active-context；
- 为未来模板和自动化打基础。
