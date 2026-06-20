# 轻度研究子课题 1：非开发长期对话记忆是否已有真实实践

## 研究目标

请研究：在非开发场景中，是否已经存在以“长期围绕相同话题或话题族持续讨论，并稳定记住先前对话内容”为目的的持久记忆系统、产品实践、研究项目或用户工作流。

本研究不要求设计完整方案，而是要查找真实案例、官方文档、产品能力、论文或高质量技术报告，判断普通非开发长期对话是否也已经出现类似“外部持久记忆系统”的实践。

## 背景

我正在构想一种“AI Agent 外部持久记忆系统”。核心思想是：不要把长期记忆主要依赖在模型内部或单次聊天窗口，而是将规则、状态、原文归档、学习进度、评估报告、主题索引、handoff 等保存在外部持久存储中，例如 GitHub 仓库、本地 Markdown、数据库或知识库。

这个问题不仅存在于软件开发，也存在于普通长期对话、学习、研究、语言训练、源码学习、个人知识管理和持续讨论中。

## 重点研究问题

1. 在非开发场景中，是否已有类似“长期话题记忆”或“持续对话记忆”的真实案例？
2. ChatGPT、Claude、Gemini、NotebookLM、Khanmigo、Google LearnLM、MemGPT、AI tutor、AI coach、个人知识管理加 LLM 等方向，是否有类似外部持久记忆、学习者画像、主题记忆、学习进度、会话 handoff、原文归档、检索式记忆的成熟或半成熟实践？
3. 当前是不是主要只有开发者和 coding agent 场景最明确地注意到“长期记忆、handoff、规则文件、项目状态”的问题，而普通对话用户较少系统化建立外部持久记忆体系？
4. 如果非开发场景也有类似案例，它们的记忆系统通常保存什么？
5. 如果非开发场景缺少成熟案例，开发场景中的持久记忆经验是否可以迁移过来？

## 请优先查找的资料类型

- OpenAI 关于 ChatGPT memory、Projects、custom instructions、connectors 的官方文档；
- Anthropic 关于 Claude Projects、Claude memory、Claude Code memory 或 sessions 的官方文档；
- Google NotebookLM、LearnLM、Khanmigo 等教育或学习型 AI 案例；
- MemGPT、long-term conversational agents、AI tutor、AI coach、personal knowledge management with LLM 等论文或项目；
- Obsidian、Notion、Logseq、PKM + LLM 的高质量实践；
- RAG、memory store、long-term memory、conversation summary、checkpoint 等技术资料。

## 输出要求

请输出：

1. 总体结论：非开发长期对话记忆是否已有成熟实践。
2. 真实案例清单，每个案例说明：
   - 它支持哪种记忆机制；
   - 是官方产品、论文、开源项目还是用户实践；
   - 是否支持外部持久存储；
   - 是否支持跨对话恢复；
   - 自动化程度；
   - 局限性。
3. 非开发场景与开发场景的差异。
4. 哪些经验可以从开发型 AI agent 迁移到普通长期对话、教学、研究和源码学习。
5. 哪些地方目前仍缺少成熟实践，需要用户半自动维护。

## 注意事项

不要设计完整系统。重点是查找和评价真实案例与资料。不要预测未来能力。若没有明确官方或可靠资料支持，请标明“不确定”或“缺少证据”。
