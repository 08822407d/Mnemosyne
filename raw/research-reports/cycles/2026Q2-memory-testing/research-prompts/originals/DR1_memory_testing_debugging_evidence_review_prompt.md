# Pro Deep Research Prompt 1
# AI Agent 外部持久记忆系统的测试、调试、评估与失效诊断：证据综述

## 研究题目

请进行深度研究：

**AI Agent 外部持久记忆系统的测试、调试、评估与失效诊断：证据综述**

英文可理解为：

**Evidence review on testing, debugging, evaluation, and failure diagnosis for AI Agent external persistent memory systems**

## 明确排除范围

本课题不研究“通用目的元 Agent”或“为任意特定需求设计可靠 Agent 的通用元 Agent”的总体设计与建设。

本课题也不要求设计完整 Mnemosyne 测试框架、完整产品方案、完整模板包或 Codex 任务。

本课题只研究：

> 对 AI Agent 外部持久记忆系统进行测试、调试、评估和失效诊断时，目前有哪些研究、工程实践、评估方法和可迁移经验。

如果涉及多模型 / 多厂商独立评审，只能作为外部持久记忆系统评估方法的一部分简要讨论；不要扩展为通用元 Agent 研究。

## 背景

我正在建设一个名为 Mnemosyne 的持久记忆元 Agent / 记忆系统设计工厂。它用于为长期项目、研究项目、学习系统、源码学习、软件开发项目、AI Agent 项目、多 Agent 团队等设计外部持久记忆框架。

当前 Mnemosyne 的基本构想包括：

- 模型负责计算，文件负责记忆；
- 当前对话上下文类似短期工作内存；
- 外部 Markdown / Git / GitHub 仓库 / 文件系统保存长期状态；
- 目标项目应有自己的 execution source、active context、handoff、raw、candidate、decision、todo、open questions；
- 普通 ChatGPT / Claude 对话不默认具有自动写回能力；
- Codex / Claude Code / Cursor 等 coding agent 更适合通过 Git diff / PR / review 进行文件式写回；
- research reports、prompts、summaries、template packs 都不是执行源；
- 新对话 / 新任务需要通过 handoff 和 startup instructions 稳定接手；
- 当前阶段重点是验证 Mnemosyne 能否为真实目标项目设计可用的外部持久记忆框架。

现在需要研究：这种外部持久记忆系统应该如何测试、调试、评估和诊断失败。

## 研究目标

请重点研究以下问题：

1. 如何定义一个 AI Agent 外部持久记忆系统“工作正常”？
2. 外部持久记忆系统应测试哪些核心能力？
3. 有哪些典型失效模式？
4. 现有 agent memory eval、RAG eval、context engineering eval、long-horizon task eval、workflow eval、trace debugging、人类 review、软件工程测试等方法，哪些可以迁移？
5. 哪些方法已有成熟实践，哪些只是研究原型或合理推断？
6. 哪些方法适合 Mnemosyne 当前半自动阶段，哪些必须等自动化工具成熟后再考虑？

## 重点研究问题

### A. 测试目标

请研究外部持久记忆系统应测试哪些能力，包括但不限于：

- 跨对话接手；
- execution source 优先级；
- active context 更新；
- handoff 准确性；
- raw / evidence / candidate / decision / open question 分层；
- 长期任务状态恢复；
- 过期信息识别；
- 冲突信息处理；
- 用户确认边界；
- 隐私 / 敏感信息边界；
- 工具能力边界；
- 研究证据时效性；
- 目标项目 delivery / handoff 是否可落地。

### B. 失效模式 taxonomy

请建立一个外部持久记忆系统常见失效模式分类，至少覆盖：

1. stale handoff；
2. wrong source priority；
3. memory drift；
4. memory overwrite；
5. missing critical context；
6. over-retention；
7. under-retention；
8. hallucinated memory；
9. retrieval failure；
10. stale tool capability assumption；
11. implicit automation assumption；
12. privacy leakage；
13. inconsistent handoff vs active context；
14. user decision not recorded or not propagated；
15. first target-project dry-run 输出物看似完整但无法实际落地。

每一类请说明：

- 定义；
- 触发原因；
- 可观察症状；
- 可用测试方法；
- 可能的修复策略；
- 证据成熟度。

### C. 可迁移的评估方法

请查找并评价下列方向：

- agent memory evaluation；
- long-horizon agent task evaluation；
- RAG / retrieval evaluation；
- context engineering evaluation；
- prompt / instruction following evaluation；
- workflow / process compliance evaluation；
- trace-based debugging；
- human-in-the-loop review；
- regression tests for agents；
- scenario-based dry-runs；
- red-team / adversarial review；
- multi-model independent review；
- software engineering testing / CI / code review / ADR / incident review / postmortem；
- knowledge management / PKM / Zettelkasten / Obsidian / Notion 等长期知识系统健康检查方法。

请对每类方法说明：

- 有哪些代表性资料 / 工具 / 论文 / 官方文档；
- 能解决哪些外部记忆系统问题；
- 不能解决哪些问题；
- 适合当前半自动阶段还是未来自动化阶段；
- 对 Mnemosyne 的可迁移价值。

### D. First target-project dry-run 的高层建议

请只给高层建议，不要设计完整模板。

重点说明：

- 第一次真实目标项目 dry-run 应观察哪些现象；
- 需要记录哪些失败或成功信号；
- 如何判断模板缺陷、模型失误、用户需求不完整、工具能力边界问题；
- 哪些问题应进入 candidate / open question / TODO；
- 哪些问题应触发 Codex 小修；
- 哪些问题应回到用户澄清；
- 哪些问题应触发新的 Deep Research 或 capability delta review。

## 优先查找资料

请优先查找：

- 2025-2026 年 agent memory evaluation、long-context agent evaluation、long-horizon task evaluation 的论文和技术报告；
- RAG evaluation、retrieval quality、context engineering evaluation 的官方文档和高质量实践；
- LangSmith / LangGraph / LlamaIndex / OpenAI / Anthropic / Google / Microsoft / GitHub 等关于 agent evaluation、trace、memory、context、workflow debugging 的官方资料；
- multi-model review / critique / red-team 的研究与工程实践，限于评估和审查用途；
- software engineering 的 ADR、postmortem、incident review、regression testing、CI、code review、audit log；
- knowledge management / PKM / learning record / long-term project documentation 的健康检查方法；
- 真实案例：AI agent 项目如何评估记忆、上下文恢复、长期状态、handoff、tool use 和 external memory。

## 输出要求

请输出结构化研究报告，至少包含：

1. Executive Summary / 总体结论
2. 该问题当前是否已有成熟实践
3. 外部持久记忆系统的核心测试目标
4. 典型失效模式 taxonomy
5. 可迁移的评估方法和来源证据
6. RAG / retrieval eval 对外部记忆系统的意义
7. Agent trace / workflow debugging 的意义
8. Multi-model independent review 的可行性、价值和限制（仅限评估方法）
9. First target-project dry-run 的高层测试建议
10. 哪些方法适合当前半自动阶段
11. 哪些方法必须等工具或自动化成熟后再考虑
12. 对 Mnemosyne 后续工作的具体建议
13. Open questions / 不确定项
14. Sources / 资料来源，尽量给出链接和日期

## 输出约束

- 不要设计完整产品；
- 不要研究通用目的元 Agent 总体架构；
- 不要假设普通 ChatGPT / Claude 对话可以自动写回 GitHub；
- 不要假设 MCP、RAG、GitHub Actions、多 Agent 自动协调已经可用；
- 不要把模型内部 memory 当作长期真相源；
- 不要把多模型意见当作事实证据；
- 对依赖当前工具 / 平台能力的结论必须标注资料日期和不确定性；
- 区分“成熟实践”“研究原型”“合理推断”“不建议当前使用”；
- 最终建议要服务 Mnemosyne 的近期目标：尽快为真实目标项目设计和测试外部持久记忆框架。
