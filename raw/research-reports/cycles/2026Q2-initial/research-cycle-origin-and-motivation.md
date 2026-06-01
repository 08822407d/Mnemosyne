# Research Cycle Origin and Motivation: RC-2026Q2-initial / 研究轮次起点与动机

## 文件定位 / Status

本文件记录 `RC-2026Q2-initial` 这轮研究的起点、动机和问题背景。它用于帮助后续 ChatGPT / Codex / Claude / Claude Code 理解这 7 份研究报告为什么存在、分别试图验证什么、为什么它们是 Mnemosyne 设计的高权重证据层，以及为什么它们仍然不是执行源。

本文件不是研究报告原件，不是 report summary，不是执行源，也不替代任何原始报告。当前执行源仍是：

- `current/human-approved-spec.md`

如果本文件与原始报告冲突，应以原始报告作为证据来源，并登记 review note / follow-up review。如果本文件、原始报告或 summary 与 `current/human-approved-spec.md` 冲突，应以 `current/human-approved-spec.md` 作为执行准则，并登记 open question。未复核的 PDF 图表 / 图片 / 版式不得作为已验证证据使用。

## 1. 研究起点

`RC-2026Q2-initial` 不是一次普通资料收集，也不是为了追逐某个单一工具的新功能。它的起点是：用户希望建立一个“记忆系统元 Agent”仓库，用于设计、演化和交付 AI Agent 外部持久记忆系统。Mnemosyne 不是某个具体目标项目的普通记忆库，而是用于帮助其他项目、长期研究、学习系统、开发 Agent、多 Agent 团队等建立外部持久记忆结构的设计工厂和设计档案。

这轮研究背后的核心架构直觉是：“模型作为 CPU + 临时上下文作为内存”与“指令 / 数据 / 持久状态”需要分离。模型可以计算、归纳、改写、规划和执行，但模型本身不应被当作长期真相源。单个 ChatGPT 对话、Codex 任务、Claude Code session 或其他 Agent session 的上下文会变长、被压缩、被截断、丢失、重开，或者因为平台策略变化而表现不同。即使某些工具在某些场景下可以读写文件，也不能直接推出“所有对话和所有 Agent 都天然具备可靠长期记忆”。

如果没有外部持久记忆，长期项目会被迫依赖旧对话上下文。这样会导致新会话难以接手：后续模型可能看不到早期动机，不知道哪些方案已被否决，不理解当前文件结构为什么存在，也无法判断哪些内容是执行源、哪些只是候选或证据层。更严重的是，模型可能把临时讨论、未确认候选、研究摘要或工具能力假设误当作当前项目规范，造成设计漂移。

因此，GitHub 仓库被设想为外部持久状态源、审计源和交接源。仓库文件可以承载执行源、raw input、candidate requirements、decision log、active context、handoff、task result records、research evidence、capability boundaries 和 delivery manifest 等不同层级的材料。Git diff、commit、PR、review 与文件历史可以提供可审计性，帮助用户和后续模型比较“任务声称完成了什么”与“仓库实际发生了什么”。

本轮研究的目的不是证明某一个工具已经完美支持长期记忆，而是验证“文件式、仓库式、可审计的外部记忆系统”是否有工程和理论依据。它需要回答：为什么外部持久记忆必要；哪些场景可以依赖文件系统和 Git；哪些场景只能把平台 memory 当作辅助；哪些能力不能被假设；以及 Mnemosyne 在 v0.1 / v0.2 阶段应该把哪些承诺写成执行源、哪些只保留为证据层或后续研究问题。

## 2. 核心担忧

这轮研究被发起，是因为 Mnemosyne 的设计不能只建立在“模型应该记得”或“工具看起来能读写文件”的乐观假设上。核心担忧包括：

1. 普通对话记忆、模型内置 memory 或上下文窗口不足以承载长期工程状态。它们可能适合保存偏好、少量背景或局部上下文，但不适合承担项目执行源、决策历史、交付清单、风险边界和审计记录。
2. 长上下文被压缩后，模型可能遗忘动机、边界、早期决策和失败经验。即使压缩摘要保留了结论，也可能丢失“为什么做这个选择”“哪些方案被排除”“哪些前提未验证”等高价值上下文。
3. Codex / Claude Code / Cursor 等工具能操作文件，但不应被假设为自动可靠记忆系统。文件可写能力只是基础条件，可靠记忆还需要明确执行源、写回流程、审计、冲突处理、用户确认和交接机制。
4. 云端 Coding Agent 和 GitHub 工作流适合审计，但可能出现“声称完成但实际 diff 不一致”的情况。Mnemosyne 因此需要 Codex Task Result Record、Git diff 审计、manual review 和必要验证，而不是只相信任务完成回复。
5. 不同工具的能力边界不同，不能把某一工具在某个上下文中的能力泛化到所有对话和任务。普通 ChatGPT / Claude 对话、带项目文件的本地开发 Agent、云端 Coding Agent、IDE Agent、多 Agent 系统和 GitHub workflow 需要分别判断。
6. PDF 图表 / 图片 / 版式在没有人工复核前，不应作为已验证设计证据。即使 PDF 文本可读，图表、图片、表格布局或视觉层级仍可能影响含义，必须通过 `pdf-figure-review-index.md` 追踪人工复核状态。
7. 如果研究动机不入库，后续模型可能只看到报告结论，不知道这些结论为什么对 Mnemosyne 架构重要。这样会降低研究报告作为高权重证据层的可用性，并增加把研究结论误用为执行规则的风险。

## 3. 为什么是 1 份 Pro 深度研究 + 6 份轻度研究

`RC-2026Q2-initial` 采用 1 份 Pro 深度研究加 6 份轻度研究的结构，是为了同时获得总体框架和分场景边界。

Pro 深度研究覆盖 AI Agent 外部持久记忆系统的总体问题：必要性、已有实践、架构模式、风险、工具边界、可行路线和对 Mnemosyne 的总体启发。它为 Mnemosyne 的定位提供高层证据：模型不是长期真相源，外部文件 / Git 仓库可以作为长期记忆和审计基础，但需要明确边界和流程。

6 个轻度研究则拆分验证更具体的问题：

- 非开发长期对话是否已有真实长期记忆实践；
- ChatGPT / Claude 纯对话工具和平台内置 memory 的边界；
- Codex / Claude Code / Cursor 等本地开发 Agent 的文件式记忆能力；
- 云端 Coding Agent + GitHub 工作流下的记忆写回和审计；
- 外部持久记忆的理论与工程依据；
- 开发场景中的持久记忆经验能否迁移到普通学习、研究和长期对话场景。

这种拆分是为了避免泛泛结论。Mnemosyne 需要服务多类目标项目，如果只得到“外部记忆有用”这一类笼统结论，无法支撑模板包设计。拆分后的报告分别支撑三类模板包：self-improvement template pack、target project memory system template pack、delivery manifest template pack。它们帮助判断哪些机制应保留为通用骨架，哪些机制必须根据目标项目类型裁剪，哪些能力必须标记为 unsupported assumption 或 manual setup step。

## 4. 7 份报告分别试图回答什么问题

### 4.1 RPT-2026Q2-0001：AI agent 长期记忆系统 pro 深度研究

- 意图：总体研究 AI Agent 外部持久记忆系统的必要性、实践、架构模式、风险和可行路线。
- 用途：支撑 Mnemosyne 的总体定位，即 Mnemosyne 是用于设计、演化和交付外部持久记忆系统的元 Agent 工作仓库，而不是依赖单次对话上下文的普通项目笔记。
- 对 Mnemosyne 的约束：它提醒设计必须区分执行源、证据层、候选需求、决策记录、活动上下文和交接记录，不能把模型内部记忆或上下文窗口当作长期真相源。

### 4.2 RPT-2026Q2-0002：非开发长期对话记忆是否已有真实实践

- 意图：验证非开发场景是否已有真实长期对话记忆实践。
- 用途：避免把开发仓库记忆经验错误套用到普通长期对话 / 学习场景。
- 对 Mnemosyne 的约束：非开发长期对话、学习、研究陪伴和个人知识管理可能需要更轻量的 intake、handoff、topic history、learning state 或 review cadence，不能默认使用完整软件开发仓库流程。

### 4.3 RPT-2026Q2-0003：ChatGPT / Claude 纯对话场景的外部记忆能力边界

- 意图：确认纯自然语言对话和平台内置记忆的边界。
- 用途：提醒不能假设普通聊天自动写回仓库，也不能把内置 memory 当项目真相源。
- 对 Mnemosyne 的约束：当目标环境只是普通对话窗口时，外部记忆写回可能需要人工复制、显式导出或额外工具；交付包不能承诺平台会自动同步仓库状态。

### 4.4 RPT-2026Q2-0004：Codex / Claude Code / Cursor 等本地开发 Agent 的文件式记忆能力

- 意图：研究开发 Agent 通过文件系统、项目文档、仓库结构形成持久上下文的能力。
- 用途：支撑文件式模板、handoff、active-context、todo、decision-log 等结构。
- 对 Mnemosyne 的约束：文件式记忆可行，但需要清晰命名、目录结构、执行源声明、任务结果记录和 review 流程；开发 Agent 能修改文件不等于它会自动保持语义一致。

### 4.5 RPT-2026Q2-0005：云端 Coding Agent 与 GitHub 工作流下的记忆写回和审计

- 意图：研究云端 Coding Agent、GitHub PR、diff、commit、review 如何支持外部记忆写回和审计。
- 用途：支撑 Codex task result record、Git diff 审计，以及“不要只信任务声称完成”的原则。
- 对 Mnemosyne 的约束：云端工作流适合形成可审计轨迹，但必须把 task result record、PR / commit diff、用户 review 和必要验证组合起来判断完成情况。

### 4.6 RPT-2026Q2-0006：外部持久记忆的理论与工程依据

- 意图：寻找外部持久记忆必要性的理论和工程依据。
- 用途：支撑“模型上下文不是长期真相源”，以及仓库文件 / 执行源 / 证据层需要分离。
- 对 Mnemosyne 的约束：设计应把可持久化、可审计、可迁移、可复核的文件结构作为长期状态基础，同时承认研究证据具有时效性，需要后续 research refresh / delta report。

### 4.7 RPT-2026Q2-0007：开发场景的持久记忆经验能否迁移到普通长期对话和学习场景

- 意图：验证开发场景中成功的文件式记忆和交接实践能否迁移到学习、研究、长期对话等非开发场景。
- 用途：支撑 target project type classifier 和不同场景模板裁剪。
- 对 Mnemosyne 的约束：开发场景经验可以提供结构化启发，但不应原样搬运；目标项目类型、隐私要求、交互频率、用户维护成本和工具能力都会影响 memory schema。

## 5. 研究结果在 Mnemosyne 中的地位

7 份研究报告是高权重证据层，不是执行源。当前执行源仍是 `current/human-approved-spec.md`。

研究报告的作用是约束设计方向、能力边界、风险提示和模板演进。例如：它们可以提示 Mnemosyne 不要承诺自动写回、不要把平台 memory 当项目真相源、不要把未复核 PDF 图表作为证据、不要把开发工具能力泛化到普通对话场景。它们也可以为后续模板包提供证据基础，例如为什么需要 active-context、handoff、decision-log、unsupported assumptions、drift review 和 delivery result。

但研究报告不能直接覆盖执行源。若研究报告、summary、motivation、candidate、decision、active-context 或 handoff 与 `current/human-approved-spec.md` 冲突，应以执行源为准，并登记 open question。若未来研究发现现有判断过时，应通过新的 research refresh / delta report 更新证据层，而不是覆盖 `RC-2026Q2-initial` 的历史研究动机。

## 6. 研究动机与三类模板包的关系

### 6.1 self-improvement template pack

这轮研究支持 self-improvement template pack 中的 raw / candidate / conflict check / user decision / task result record 链路。研究动机强调：新想法、用户反馈、研究更新和 Codex 任务结果不能直接升级为执行源。它们应先作为 raw 或 task result record 保存，再抽取候选需求，检查重复和冲突，经用户确认后才可能更新 `human-approved-spec`。

研究也支持保存 Codex 声称与实际 diff 的偏差。云端 Coding Agent 可能生成合理的完成说明，但最终判断应看仓库文件、Git diff、用户 review 和必要验证。因此，Codex Task Result Record 是审计材料，而不是执行源。

### 6.2 target project memory system template pack

这轮研究支持 target project memory system template pack 的核心前提：每个目标项目都要明确自己的 execution source。目标项目需要 intake、memory system design spec、file layout、handoff、unsupported assumptions、drift review、minimal runbook 和 completion criteria。

不同场景不能使用完全相同结构。开发项目可以更自然地依赖 Git diff、issue、PR 和文件系统；长期学习或研究项目可能更需要阶段目标、学习状态、资料来源、复习节奏和主题边界；普通长期对话可能需要更低维护成本的摘要和交接机制。研究动机要求后续模型不要把开发场景的文件式记忆经验未经裁剪地套用到所有目标项目。

### 6.3 delivery manifest template pack

这轮研究支持 delivery manifest template pack 中“设计档案”和“目标项目运行真相源”分离的原则。Mnemosyne 仓库可以保存设计说明、模板和交付记录，但目标项目自己的仓库或目录才是目标项目运行真相源。

交付前需要明确 files-to-create / files-to-update、manual setup steps、rollback、handoff package、delivery result 和 unsupported assumptions。不能默认自动写回、自动触发、自动同步，也不能默认目标项目已经拥有与 Mnemosyne 相同的工具能力。若交付依赖目标项目中的 GitHub Actions、AGENTS.md、CLAUDE.md、MCP、RAG 或其他自动化能力，应先作为明确设计和人工确认事项，而不是从研究报告中直接推导为当前能力。

## 7. 对后续模型接手的提示

后续 ChatGPT / Codex / Claude / Claude Code 接手 `RC-2026Q2-initial` 相关材料时，建议按以下顺序使用：

1. 先读本文件，理解 7 份报告为什么存在、分别服务什么设计问题，以及为什么它们是高权重证据层但不是执行源。
2. 再读 `raw/research-reports/current/current-report-summaries.md`，获得当前激活研究轮次的摘要入口。
3. 再按需回查原始报告，尤其是在设计依赖某个具体能力判断、风险判断或理论依据时。
4. 若设计依赖 PDF 图表 / 图片 / 版式，先查看 `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`。
5. 不要把未复核图表 / 图片当作已验证证据。
6. 不要把研究动机当执行规则。
7. 不要把研究结果当当前工具能力的实时保证。工具能力、平台规则、产品功能和工作流可能变化，未来需要 research refresh / delta report。

## 8. 后续更新策略

本文件记录 `RC-2026Q2-initial` 的原始研究动机。后续每个研究周期可以有自己的 motivation / origin 文件，用于说明新一轮研究为什么被发起、试图回答什么问题、与旧研究相比新增或修正了什么。

不应覆盖旧研究动机。历史动机是审计材料的一部分：它说明当时为什么提出那些研究问题、为什么选择那些报告主题、为什么形成当前的证据层结构。若三个月后重新研究，应创建新的 cycle，并用 delta report 说明工具能力、理论依据、实践案例或 Mnemosyne 设计需求发生了哪些变化。

当新研究问题产生时，应新增 research prompt / motivation，而不是改写历史动机。这样可以保留 Mnemosyne 设计演化的可追溯性，并帮助后续模型区分“当时为什么这样研究”和“现在根据新证据应如何调整”。
