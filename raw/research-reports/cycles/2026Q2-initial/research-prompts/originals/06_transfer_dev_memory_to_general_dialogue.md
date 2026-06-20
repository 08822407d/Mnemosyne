# 轻度研究子课题 6：开发场景的持久记忆经验能否迁移到普通长期对话和学习场景

## 研究目标

请研究：软件开发和 coding agent 场景中的外部持久记忆经验，是否可以迁移到普通长期对话、教学、研究、语言学习和源码学习等非开发场景。

## 背景

在开发场景中，AI agent 越来越多地使用：

- AGENTS.md / CLAUDE.md；
- repo instructions；
- project-state；
- tasks；
- ADR；
- memory-ledger；
- handoff-current；
- artifact refs；
- PR / CI / review；
- Git 版本管理。

我想知道这些经验能否改造成普通对话或学习场景中的长期记忆系统。

例如：

- AGENTS.md / CLAUDE.md 可否改造成“对话行为规则”；
- project-state 可否改造成“主题状态”；
- tasks 可否改造成“学习任务”；
- ADR 可否改造成“长期结论与决策记录”；
- memory-ledger 可否改造成“主题记忆账本”；
- handoff-current 可否改造成“跨对话交接卡”；
- archive 可否改造成“原文对话归档”。

## 重点比较场景

### 1. 语言学习

需要记忆：

- 教学进度；
- 词汇和语法点；
- 听说读写能力画像；
- 错题；
- 反应时间；
- 提示次数；
- 复犯率；
- 阶段性评估报告。

### 2. 大型开源项目源码学习

例如 Linux 内核、数据库、编译器。

需要记忆：

- 当前研究的子系统；
- 源码版本；
- 关键文件路径；
- 关键结构体和函数；
- 调用链；
- 设计思想；
- 已讨论内容；
- 未理解问题；
- 子系统依赖图。

### 3. 长期技术研究或方案讨论

需要记忆：

- 主题索引；
- 当前结论；
- 有效假设；
- 已废弃前提；
- 争议点；
- 待验证问题；
- 参考资料；
- handoff。

## 核心问题

1. 开发项目记忆与普通长期对话记忆有哪些共同点？
2. 开发项目记忆与语言学习记忆有哪些差异？
3. 开发项目记忆与源码学习记忆有哪些差异？
4. 哪些文件结构可以直接迁移？
5. 哪些文件结构需要改造？
6. Git / Markdown / GitHub 仓库是否适合非开发记忆？
7. 主题卡、学习画像、长期结论记录、原文归档是否可以借鉴开发项目的 project-state / ADR / memory-ledger / archive？
8. 是否需要为不同 AI 工作系统设计不同 memory schema？
9. 是否有必要建立“记忆架构元 Agent”，专门为不同 AI 工作系统生成和维护记忆结构？

## 请优先查找的资料

- AGENTS.md、CLAUDE.md、repo instructions 的官方或高质量资料；
- 软件开发中 project-state、ADR、tasks、handoff、memory-ledger 的实践；
- PKM、Zettelkasten、Obsidian、Notion、Logseq 等非开发知识管理实践；
- AI tutor、learning profile、Khanmigo、LearnLM、NotebookLM 等学习场景资料；
- RAG、external memory、topic maps、knowledge graphs 相关资料。

## 输出要求

请输出：

1. 总体结论：开发场景经验能否迁移到普通长期对话和学习场景。
2. 可直接复用的机制。
3. 需要改造的机制。
4. 不适合迁移的机制。
5. 语言学习场景的记忆结构建议依据。
6. 源码学习场景的记忆结构建议依据。
7. 长期技术研究场景的记忆结构建议依据。
8. 是否需要“记忆架构元 Agent”的证据和理由。
9. 后续让 ChatGPT / Codex / Claude Code 起草具体方案时可用的参考要点。

## 注意事项

不要给出最终完整实施方案。重点是比较、迁移可行性和依据。若某个迁移只是合理推断而非已有案例，请明确说明。
