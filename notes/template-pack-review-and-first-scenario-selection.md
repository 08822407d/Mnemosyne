# Template Pack Review and First Scenario Selection / 模板包 review 与首个场景选择

## 文件定位

本文件用于 review 已创建的三类模板包，并帮助用户选择第一个试用场景。

本文件不是执行源。当前执行源仍是：

- `current/human-approved-spec.md`

本文件不代表已经选择目标项目，也不生成真实目标项目交付包。如果本文件与 `current/human-approved-spec.md` 冲突，以 `current/human-approved-spec.md` 为准，并登记 open question。

本文件只提供 review 清单、候选场景矩阵、第一轮 dry-run 的最小输入要求和用户决策选项。真实目标项目交付前，仍必须由用户确认输入材料、隐私边界和落地方式。

## 1. Review Scope

本次 review 覆盖三类已创建模板包：

1. `notes/self-improvement-template-pack.md`
   - 负责 Mnemosyne 自身如何吸收用户新构想、反馈、Codex / ChatGPT 任务结果、研究更新和目标项目反馈。
2. `notes/target-project-memory-system-template-pack.md`
   - 负责如何为目标项目设计外部持久记忆系统，包括 intake、项目分类、设计说明、文件结构、执行源规则、handoff、风险假设和 drift review。
3. `notes/delivery-manifest-template-pack.md`
   - 负责如何把设计安全地交付到目标项目，包括交付范围、目标项目运行真相源、人工设置步骤、交付 review、handoff、回滚和结果记录。

这三类模板包都不是执行源。在真实使用前，它们都需要用户 review，并根据用户意见决定是否小修、拆分或暂时接受为 v0.2 可用基础版本。

## 2. Review Checklist for Self-Improvement Template Pack

请 review `notes/self-improvement-template-pack.md` 时检查：

- [ ] Raw Input Entry Template 是否足够保存用户新构想、反馈、任务结果和研究更新？
- [ ] Candidate Requirement Template 是否足够表达候选需求、状态、来源和反映位置？
- [ ] Similarity / Conflict Check Template 是否足够处理重复、冲突、替换、细化和需要用户确认的情况？
- [ ] User Decision Record Template 是否足够记录用户决策、理由、状态和后续动作？
- [ ] Codex Task Result Record Template 是否足够记录任务声称与实际 diff 的偏差？
- [ ] ChatGPT Stage Summary Template 是否足够支持长对话阶段性交接？
- [ ] Research Refresh Intake Template 是否足够处理季度研究 refresh、delta report 和能力边界更新？
- [ ] Target Project Feedback Template 是否足够支持目标项目反馈回流到 Mnemosyne？
- [ ] Open Question / TODO Template 是否足够支撑未决事项和计划项？
- [ ] Apply Result Checklist 是否足够避免误把候选内容、raw、decision 或 task result 升级为执行源？
- [ ] Minimal Self-Improvement Runbook 是否足够可操作，能指导一次最小半自动自我改进流程？
- [ ] 是否需要拆成多个独立模板文件？
- [ ] 是否需要小修字段、标题、路径占位符或示例？
- [ ] 是否可以暂时接受为 v0.2 可用基础版本？

## 3. Review Checklist for Target Project Memory System Template Pack

请 review `notes/target-project-memory-system-template-pack.md` 时检查：

- [ ] Target Project Intake Template 是否足够收集目标项目约束、项目类型、工具、隐私、资料和风险？
- [ ] Target Project Type Classifier 是否覆盖长期研究、学习系统、源码学习、软件开发、AI Agent、多 Agent、个人长期对话 / 知识管理和混合场景？
- [ ] Memory System Design Spec Template 是否足够描述目标项目记忆系统的目的、边界、文件结构、执行源和工作流？
- [ ] Target Project Memory File Layout Template 是否足够可裁剪，能适配不同目标项目规模？
- [ ] Target Project Execution Source Rule Template 是否能防止执行源混乱，明确目标项目自己的运行真相源？
- [ ] Target Project Workflow Template 是否适合半自动工作流，而非默认承诺自动写回？
- [ ] Delivery Package Draft Template 是否和 delivery manifest template pack 衔接清楚？
- [ ] Target Project Handoff Template 是否足够支持跨对话 / 跨任务 / 跨工具接手？
- [ ] Unsupported Assumptions Template 是否足够暴露工具能力、隐私、自动化、PDF / 图片读取等风险？
- [ ] Target Project Drift Review Template 是否足够支持后续检查是否偏离原设计？
- [ ] Minimal Target Project Design Runbook 是否足够指导实际设计？
- [ ] Completion Criteria 是否足够判断设计草案是否完成？
- [ ] 是否需要更正式的隐私分级字段？
- [ ] 是否需要小修字段、示例、分类或风险提示？
- [ ] 是否可以暂时接受为 v0.2 可用基础版本？

## 4. Review Checklist for Delivery Manifest Template Pack

请 review `notes/delivery-manifest-template-pack.md` 时检查：

- [ ] Delivery Manifest Template 是否足够记录交付范围、目标项目、文件、状态和确认点？
- [ ] Files To Create / Update Checklist 是否足够避免覆盖风险、误写目标项目文件或混淆新建 / 更新？
- [ ] Target Project Runtime Truth Source Checklist 是否足够区分 Mnemosyne 设计档案和目标项目运行真相源？
- [ ] Manual Setup Steps Template 是否足够表达人工落地步骤、权限、命令和验证方式？
- [ ] Unsupported Assumptions Linkage Template 是否足够连接风险假设和具体交付动作？
- [ ] Delivery Review Checklist 是否足够支持交付前 review？
- [ ] Handoff Package Template 是否足够支持交付后接手？
- [ ] Rollback / Revision Plan Template 是否足够覆盖回滚、修订和停止使用？
- [ ] Delivery Result Record Template 是否足够记录实际交付结果、偏差和未完成项？
- [ ] Minimal Delivery Runbook 是否足够可操作？
- [ ] Delivery Completion Criteria 是否足够避免未确认即声称交付完成？
- [ ] 是否需要小修字段、状态值、风险提示或路径占位符？
- [ ] 是否可以暂时接受为 v0.2 可用基础版本？

## 5. First Scenario Candidate Matrix

以下矩阵用于帮助用户选择第一个试用场景。它不是最终选择，也不代表已经开始真实目标项目交付。

初步建议排序应优先考虑：低风险、可手工执行、输入材料容易控制、能验证 `intake → design spec → delivery manifest → handoff → review` 模板链路的场景。

| 候选场景 | 场景描述 | 为什么适合作为第一试用场景 | 为什么不适合作为第一试用场景 | 需要的输入材料 | 隐私注意点 | 是否依赖研究报告 summary | 是否依赖 PDF 图表人工复核 | 是否依赖自动化 | 风险等级 | 推荐程度 | 试用输出物 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 长期研究项目 | 为一个长期研究主题建立外部记忆、证据、问题和阶段总结结构。 | 能验证研究证据层、summary、open question、handoff 与 drift review；与 Mnemosyne 原始研究背景贴近。 | 可能过早依赖研究报告 summary 或 PDF 图表复核，材料多时 review 成本较高。 | 研究主题、已有资料、报告路径、研究问题、期望输出。 | 研究资料可能包含未公开信息，应区分可保存原文与只保存摘要。 | 是，建议有 summary 后更稳。 | 可能依赖；若论证依赖 PDF 图表，需人工复核。 | 否，第一轮可手工执行。 | 中 | 中 | 研究项目 intake、memory design spec 草案、delivery manifest 草案、handoff 草案。 |
| 学习系统 | 为学习计划、知识点、练习、复盘和长期进度建立记忆结构。 | 输入可控、隐私可降级、容易 dry-run，能验证长期进度与反馈回流。 | 如果目标太泛，容易变成个人知识库而非目标项目记忆系统。 | 学习主题、阶段目标、资料列表、复习方式、输出格式。 | 学习记录可能包含个人弱项和日程，应明确保存粒度。 | 否，通常不依赖。 | 否。 | 否。 | 低 | 中高 | 学习系统 intake、文件结构建议、handoff 与 review TODO。 |
| 源码学习 | 为阅读某个代码库建立模块笔记、问题、概念、决策和学习进度。 | 与开发 Agent 文件式记忆能力较匹配，可用公开仓库降低隐私风险。 | 若代码库太大，第一轮范围容易失控；若涉及私有代码，隐私与权限风险上升。 | 仓库路径或说明、学习目标、重点模块、当前理解程度。 | 私有源码不可默认保存全文；需确认可引用范围。 | 否，通常不依赖。 | 否。 | 否，第一轮可只生成设计。 | 中低 | 中高 | 源码学习 memory layout、execution source rule、handoff 草案。 |
| 软件开发项目 | 为一个软件项目建立执行源、任务、决策、handoff、风险和交付清单。 | 与 Git / diff / PR / review 审计路径匹配，容易验证三类模板链路，适合半自动人工闭环。 | 真实项目可能存在未合并改动、权限、隐私和落地风险；不应直接生成交付包。 | 项目名称、仓库状态、README / docs、目标、当前痛点、期望 AI 工具。 | 私有仓库、客户数据、密钥、issue 内容需分级处理。 | 否，通常不依赖。 | 否。 | 否，第一轮 dry-run 不依赖自动化。 | 中低 | 高 | 目标项目 intake、design spec 草案、delivery manifest 草案、handoff 草案。 |
| AI Agent 项目 | 为一个 Agent 项目设计外部持久记忆、能力边界、工具假设和交付包。 | 贴近 Mnemosyne 的核心用途，可验证 unsupported assumptions 与能力边界。 | 容易诱发对自动写回、MCP、RAG、多 Agent 协调的过度承诺；需要严格边界。 | Agent 目标、工具栈、运行环境、现有 prompt / docs、记忆痛点。 | 可能涉及 API key、日志、用户数据、工具权限，需严格不保存敏感原文。 | 可选；若依赖能力判断，建议参考 evidence map。 | 通常不依赖，除非使用 PDF 证据。 | 不应依赖；第一轮只做设计和风险登记。 | 中 | 中 | Agent memory design spec、unsupported assumptions、delivery manifest 草案。 |
| 多 Agent 团队 | 为多个 Agent 的角色、共享记忆、交接、冲突和协调规则设计记忆系统。 | 能覆盖未来复杂目标，检验 schema 可扩展性。 | 第一轮复杂度和风险偏高，容易引入未实现的多 Agent 自动协调假设。 | Agent 角色、协作流程、共享资料、冲突处理规则、工具边界。 | 多方上下文可能混有敏感任务、凭据或个人信息，需要严格隔离。 | 可选。 | 通常不依赖。 | 不应依赖；当前不新增多 Agent 自动协调机制。 | 高 | 低 | 多 Agent 设计草案和风险清单，不建议作为首个真实试用。 |
| 个人长期对话 / 知识管理 | 为个人长期对话、想法、决策、知识条目和阶段总结建立外部记忆结构。 | 低自动化依赖，容易半真实 / 玩具 dry-run，能验证跨对话 handoff 和隐私策略。 | 隐私边界容易模糊；如果范围过大，容易变成泛知识库。 | 主题范围、允许保存内容、阶段目标、历史资料摘要、期望工具。 | 个人信息、健康、财务、关系、账号等内容需默认最小化保存。 | 否，通常不依赖。 | 否。 | 否。 | 中低 | 高 | 个人长期对话 intake、memory layout、handoff、review checklist。 |
| 混合或未知场景 | 用户尚未确定项目类型，或目标项目同时包含研究、学习、开发和知识管理。 | 能测试 intake 和 classifier 是否足够处理不确定输入。 | 第一轮输出可能过泛，难以判断模板链路是否有效。 | 初步目标、已有材料、可能类型、最小试用边界。 | 需要先做隐私分级和范围收缩。 | 视具体内容而定。 | 视具体内容而定。 | 否。 | 中 | 中低 | 场景澄清 intake、分类建议、下一步选择问题。 |

## 6. Recommended First Trial Strategy

以下只是初步建议，不替用户最终决定。

- 若用户想以低风险、可手工执行、能验证模板链路为主，优先考虑“软件开发项目”或“个人长期对话 / 知识管理”。
- 若用户想验证研究证据链、summary、open question 和证据边界，则选择“长期研究项目”。
- 若用户想验证 AI Agent 外部记忆交付能力，则选择“AI Agent 项目”，但必须严格登记 unsupported assumptions，避免承诺未具备的自动化能力。
- 若用户想降低隐私风险，则先用一个半真实 / 玩具目标项目 dry-run，只使用脱敏资料或合成材料。

第一轮试用目标不是追求完整自动化，也不是直接落地真实项目交付。第一轮试用目标是验证：

`intake → design spec → delivery manifest → handoff → review`

这一人工闭环是否清晰、可操作、可审计。

真实目标项目交付前，必须由用户确认：

- 输入材料；
- 隐私边界；
- 是否允许保存原文；
- 目标项目运行真相源；
- 交付位置；
- 落地方式；
- 人工 review 和回滚要求。

## 7. Trial Run Minimal Input Request

用户选择第一个场景后，第一轮 dry-run 至少需要提供：

- 目标项目名称；
- 项目类型；
- 当前项目状态；
- 项目目标；
- 为什么需要记忆系统；
- 当前已有文件 / 仓库 / 资料；
- 期望 AI 工具；
- 是否允许保存原文；
- 隐私级别；
- 期望交付位置；
- 是否需要跨对话 / 跨工具接手；
- 是否有已有 AGENTS.md / CLAUDE.md / README / docs；
- 当前最担心的风险；
- 希望第一轮 dry-run 输出什么。

建议用户也说明：第一轮是否只生成 Mnemosyne 内部设计草案，还是允许准备一个不写入目标项目的 delivery manifest 草案。

## 8. Decision Options for User

用户接下来可以选择：

1. 接受三类模板包，选择第一个目标项目场景
   - 适合条件：用户认为当前三类模板包足够作为 v0.2 基础版本。
   - 代价：可能会在试用中暴露模板缺口，需要后续补丁式小修。
2. 先小修 delivery manifest template pack
   - 适合条件：用户最担心真实交付、覆盖风险、回滚和交付完成声明。
   - 代价：首个场景试用会延后。
3. 先小修 target project template pack
   - 适合条件：用户认为 intake、项目分类、隐私字段或 design spec 还不够稳定。
   - 代价：delivery manifest 与 self-improvement 暂时不动。
4. 先小修 self-improvement template pack
   - 适合条件：用户更担心新构想、反馈、任务结果和研究更新进入 Mnemosyne 的流程。
   - 代价：目标项目试用会延后。
5. 先做 Idea Capture Buffer
   - 适合条件：用户有大量临时想法，需要先建立低摩擦暂存区。
   - 代价：三类模板包真实试用继续等待。
6. 先做研究报告 summary / PDF 图表复核
   - 适合条件：用户希望首个场景强依赖研究证据链，或要用研究结论支持能力边界。
   - 代价：投入较大，首个目标项目 dry-run 延后。
7. 先设计 AGENTS.md / CLAUDE.md
   - 适合条件：用户希望改善仓库内工具接手说明。
   - 代价：当前任务明确不创建这些文件；需另开后续任务并重新确认边界。
8. 暂停 v0.2 施工，做一次只读回归验证
   - 适合条件：用户担心当前状态文件、候选需求、decision log 或 handoff 已经偏离执行源。
   - 代价：不新增能力，只验证一致性并整理问题。

## 9. Completion Criteria

本 review / selection 准备文件完成后，应至少满足：

- 三类模板包 review 范围明确；
- 每类模板包都有 review checklist；
- 首个场景候选矩阵已建立；
- 用户下一步可在几个明确选项中选择；
- 没有声称已选择真实目标项目；
- 没有生成真实交付包；
- 没有引入自动化；
- 没有修改执行源。
