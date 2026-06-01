# Decision Log

## DEC-0001
- 决策：仓库第一版仅采用 Markdown-first 最小文档结构。
- 理由：先固化记忆系统设计边界与信息分层，避免过早引入工程复杂度。
- 状态：accepted

## DEC-0002
- 决策：当前阶段以中文作为主要工作语言，不做中英双语并行。
- 理由：降低翻译歧义与维护成本，保持讨论与实施文档一致性。
- 状态：accepted

## DEC-0003
- 决策：将 Human-Approved Spec 定义为唯一执行源，其它文档作为证据、候选或上下文辅助。
- 理由：防止原文噪声或模型摘要误差直接影响执行。
- 状态：accepted

## DEC-0004
- 决策：自动化能力（GitHub Actions、自动查重、自动写回）延期。
- 理由：当前流程尚在建模阶段，应优先确保人工确认与可追溯性。
- 状态：accepted

## DEC-0005
- 决策：将 7 份研究报告作为 RC-2026Q2-initial 的原始证据入库。
- 理由：建立初始高权重研究证据基线，支撑后续能力边界判断。
- 来源：RAW-0013
- 状态：accepted

## DEC-0006
- 决策：不重命名原件，通过 report_id 建立稳定引用。
- 理由：保护原始证据完整性，同时提供结构化可追溯映射。
- 来源：RAW-0013
- 状态：accepted

## DEC-0007
- 决策：研究报告属于高权重证据层，但不是执行源。
- 理由：保证 evidence 与 execution 分离，避免静默覆盖实施版。
- 来源：RAW-0013
- 状态：accepted

## DEC-0008
- 决策：将 current-evidence-map 与 current-capability-boundaries 作为当前派生视图。
- 理由：提供稳定入口给后续任务，避免直接依赖原件分散读取。
- 来源：RAW-0013
- 状态：accepted

## DEC-0009
- 决策：后续新增设计机制必须尊重研究报告给出的能力边界约束。
- 理由：降低过度承诺与平台能力误判风险。
- 来源：RAW-0013
- 状态：accepted

## DEC-0010
- 决策：PDF 图表和图片证据需要人工复核后才能用于高影响结论。
- 理由：当前自动解析对图像与复杂版式不稳定。
- 来源：RAW-0013
- 状态：accepted

## DEC-0011
- 决策：研究报告通过新 cycle + delta report 演化，不覆盖旧报告。
- 理由：保留历史可追溯性并显式管理证据变化。
- 来源：RAW-0013
- 状态：accepted

## DEC-0012

- 决策：确认 MNEMOSYNE-019A 已完成接手层三文件修复。
- 理由：active-context、handoff-current、todo 已经不再停留在“执行 v0.1 接手能力修复”的过期状态。
- 状态：accepted
- 来源：RAW-0019

## DEC-0013

- 决策：将 active-context 定位为当前工作集，不是执行源。
- 理由：新会话需要快速理解当前阶段，但执行依据仍应来自 human-approved-spec。
- 状态：accepted
- 来源：RAW-0019

## DEC-0014

- 决策：将 handoff-current 定位为新会话接手卡，不是执行源。
- 理由：handoff-current 用于快速恢复工作状态，不应替代 human-approved-spec。
- 状态：accepted
- 来源：RAW-0019

## DEC-0015

- 决策：将 startup-instructions 作为下一项 v0.1-final 收尾工作。
- 理由：当前已有执行源、active-context、handoff 和研究证据入口，但还缺少固定启动说明来指导新 ChatGPT / Codex 任务读取文件。
- 状态：accepted
- 来源：RAW-0019

## DEC-0016

- 决策：在进入 v0.2 前应先完成一次新会话接手演练。
- 理由：需要验证 Mnemosyne 是否真的能从仓库文件接手当前工作，而不是依赖当前对话上下文。
- 状态：accepted
- 来源：RAW-0019

## DEC-0017

- 决策：新机制设计前应参考 current-evidence-map 和 current-capability-boundaries。
- 理由：7 份研究报告是当前高权重证据层，可降低平台能力误判和过度自动化承诺。
- 状态：accepted
- 来源：RAW-0019

## DEC-0018

- 决策：确认 MNEMOSYNE-021 接手演练结果为 pass。
- 理由：`notes/startup-rehearsal-report.md` 已给出 pass 结论，且说明当前文件集足以支持新 ChatGPT / 新 Codex 任务仅依赖仓库文件接手。
- 状态：accepted
- 来源：RAW-0022；notes/startup-rehearsal-report.md

## DEC-0019

- 决策：将 v0.1 状态推进为“可接手，等待用户最终 review，并选择 v0.2 第一方向”。
- 理由：接手能力已通过演练验证，当前需要用户确认收口状态并决定下一阶段重点。
- 状态：accepted
- 来源：RAW-0022；notes/startup-rehearsal-report.md

## DEC-0020

- 决策：将接手演练从 v0.1-final TODO 中标记为完成。
- 理由：对应任务已执行且结论为 pass，不应继续列为未完成项。
- 状态：accepted
- 来源：RAW-0022；notes/startup-rehearsal-report.md

## DEC-0021

- 决策：进入 v0.2 前先由用户选择第一方向。
- 理由：v0.2 包含多条并行方向，需由用户按优先级确定首个落地点。
- 状态：accepted
- 来源：RAW-0022

## DEC-0022

- 决策：研究报告 summary 与 PDF 图表复核作为 v0.1-final 后续补强项保留，但不阻断“v0.1 可接手”成立。
- 理由：接手能力已验证通过，证据补强项仍重要但与“可接手”判定不构成阻断关系。
- 状态：accepted
- 来源：RAW-0022；notes/startup-rehearsal-report.md

## DEC-0023

- 决策：创建 `notes/v0.1-final-review.md`。
- 理由：需要集中向用户呈现 v0.1 可接手性、一致性检查结果与后续方向候选。
- 状态：accepted
- 来源：RAW-0022

## DEC-0024

- 决策：在进入 v0.2 前先让用户 review v0.1 可接手性。
- 理由：v0.1 接手能力虽已演练 pass，但仍需用户进行最终确认收口。
- 状态：accepted
- 来源：RAW-0022

## DEC-0025

- 决策：v0.2 第一方向由用户选择。
- 理由：v0.2 存在多候选方向，优先级应由用户目标驱动。
- 状态：accepted
- 来源：RAW-0022

## DEC-0026

- 决策：final review 不是执行源。
- 理由：执行源仍保持为 `current/human-approved-spec.md`，避免说明性文档越权。
- 状态：accepted
- 来源：RAW-0022

## DEC-0027

- 决策：接受 MNEMOSYNE-023 独立验证结论为 `PASS_WITH_WARNINGS`。
- 理由：验证报告未发现阻断接手的严重冲突，v0.1 已具备按仓库文件接手的最低可用能力，但仍存在非阻断警告。
- 状态：accepted
- 来源：notes/v0.1-independent-verification-report.md

## DEC-0028

- 决策：将 CAND-0020 与 CAND-0021 状态同步为 reflected。
- 理由：startup-instructions 已创建，接手演练已 pass，继续标记为 todo 会误导后续任务。
- 状态：accepted
- 来源：notes/v0.1-independent-verification-report.md

## DEC-0029

- 决策：研究报告 summary、PDF 图表人工复核与可选只读回归验证作为非阻断 v0.1-final 后续项保留。
- 理由：这些事项会提升质量与审计可靠性，但不阻断 v0.1 可接手结论。
- 状态：accepted
- 来源：notes/v0.1-independent-verification-report.md

## DEC-0030

- 决策：在用户最终 review 前不进入 v0.2 实施。
- 理由：v0.1 已具备接手能力，但 v0.2 第一方向仍需用户确认优先级。
- 状态：accepted
- 来源：notes/v0.1-final-review.md；notes/v0.1-independent-verification-report.md



## DEC-0031

- 决策：v0.2 第一方向定为 self-improvement workflow。
- 理由：优先建立 Mnemosyne 自身持续演化机制，避免输入回流无序化。
- 状态：accepted
- 来源：RAW-0025

## DEC-0032

- 决策：创建 `notes/self-improvement-workflow.md` 作为 v0.2 第一方向的流程说明。
- 理由：需要明确输入回流、人工确认点和更新边界。
- 状态：accepted
- 来源：RAW-0025

## DEC-0033

- 决策：Codex Task Result Record 定位为审计材料，不是执行源。
- 理由：执行判断应以 Git diff、仓库文件和用户 review 为准。
- 状态：accepted
- 来源：RAW-0025

## DEC-0034

- 决策：self-improvement workflow 当前保持半自动。
- 理由：先固化可审查流程，再考虑自动化。
- 状态：accepted
- 来源：RAW-0025

## DEC-0035

- 决策：用户确认仍是更新 `current/human-approved-spec.md` 的必要条件。
- 理由：防止建议性内容直接越权覆盖执行源。
- 状态：accepted
- 来源：RAW-0025

## DEC-0036

- 决策：自动查重、自动写回、自动索引继续延期。
- 理由：当前阶段只做半自动流程设计，不进入自动化实现。
- 状态：accepted
- 来源：RAW-0025


## DEC-0037

- 决策：将 v0.2 第一方向设为 self-improvement workflow，并确认该工作流已建立。
- 理由：优先保证 Mnemosyne 自身演化输入有稳定回流路径，并同步当前状态层。
- 状态：accepted
- 来源：RAW-0024；RAW-0025；MNEMOSYNE-025C

## DEC-0038

- 决策：self-improvement workflow 当前保持半自动，不引入自动查重、自动写回、AGENTS.md、CLAUDE.md、GitHub Actions。
- 理由：当前阶段目标是先固化可维护流程和记录一致性，自动化延后。
- 状态：accepted
- 来源：RAW-0024；RAW-0025；MNEMOSYNE-025C

## DEC-0039

- 决策：Codex Task Result Record 是审计材料，不是执行源；后续重要 Codex 任务应记录 task result。
- 理由：避免任务总结与仓库状态不一致时误判，以可审计记录补强追溯。
- 状态：accepted
- 来源：RAW-0025；MNEMOSYNE-025C

## DEC-0040

- 决策：将 MNEMOSYNE-026（self-improvement workflow 模板设计）设为下一步。
- 理由：workflow 主体已建立，下一阶段应进入模板化以提升复用与一致性。
- 状态：accepted
- 来源：MNEMOSYNE-025C

## DEC-0041

- 决策：创建 `notes/overall-target-and-roadmap-snapshot.md`。
- 理由：将当前长期目标与路线图固化入库，避免只存在于长对话上下文。
- 状态：accepted
- 来源：RAW-0026；MNEMOSYNE-025D

## DEC-0042

- 决策：`notes/overall-target-and-roadmap-snapshot.md` 作为规划快照，不作为执行源。
- 理由：执行源仍为 `current/human-approved-spec.md`，避免说明性文件越权。
- 状态：accepted
- 来源：RAW-0026；MNEMOSYNE-025D

## DEC-0043

- 决策：后续任务可按路线图快照检查是否偏离长期目标。
- 理由：为跨会话/跨任务持续一致性提供统一回查锚点。
- 状态：accepted
- 来源：RAW-0026；MNEMOSYNE-025D

## DEC-0044

- 决策：在进入 self-improvement 模板设计前，先清理 self-improvement workflow 的格式和路径问题。
- 理由：先修复现有记录一致性，再进入模板化，降低错误扩散。
- 状态：accepted
- 来源：RAW-0026；MNEMOSYNE-025D

## DEC-0045

- 决策：后续 Codex 任务默认写入 task result record。
- 理由：增强任务可追溯性与审计一致性，降低“口头完成”风险。
- 状态：accepted
- 来源：RAW-0026；MNEMOSYNE-025D

## DEC-0046

- 决策：执行 MNEMOSYNE-026：self-improvement workflow 模板设计。
- 理由：self-improvement workflow 已有流程说明，需要推进为可复制、可审计的模板包。
- 状态：accepted
- 来源：RAW-0031

## DEC-0047

- 决策：创建 `notes/self-improvement-template-pack.md`。
- 理由：为 raw、candidate、conflict check、user decision、task result、stage summary、research refresh、target project feedback、open question、todo、apply checklist 和 runbook 提供统一入口。
- 状态：accepted
- 来源：RAW-0031

## DEC-0048

- 决策：template pack 不是执行源，当前执行源仍为 `current/human-approved-spec.md`。
- 理由：模板只用于记录与整理，不能越权成为执行规则。
- 状态：accepted
- 来源：RAW-0031

## DEC-0049

- 决策：先使用单文件模板包，后续如有需要再拆分为多个模板文件。
- 理由：当前阶段优先降低入口复杂度，待用户 review 后再决定是否拆分。
- 状态：accepted
- 来源：RAW-0031

## DEC-0050

- 决策：Codex Task Result Record 默认路径使用 `notes/codex-task-results/TASK_ID-result.md`。
- 理由：统一无尖括号占位符，减少路径写法歧义。
- 状态：accepted
- 来源：RAW-0031

## DEC-0051

- 决策：完成 self-improvement template pack 后，下一方向优先考虑目标项目 intake / memory system design spec 模板。
- 理由：自我改进入口稳定后，应转向 Mnemosyne 面向目标项目交付的核心模板能力。
- 状态：accepted
- 来源：RAW-0031

## DEC-0052

- 决策：执行 MNEMOSYNE-027：目标项目 intake / memory system design spec 模板设计。
- 理由：self-improvement workflow 模板包完成后，Mnemosyne 需要推进面向目标项目交付的核心模板能力。
- 状态：accepted
- 来源：RAW-0035

## DEC-0053

- 决策：创建 `notes/target-project-memory-system-template-pack.md`。
- 理由：需要为目标项目 intake、项目类型分类、memory system design spec、文件结构、执行源规则、handoff、unsupported assumptions、drift review 和最小 runbook 提供统一模板入口。
- 状态：accepted
- 来源：RAW-0035

## DEC-0054

- 决策：目标项目模板包不是执行源。
- 理由：模板包只用于设计目标项目记忆系统；当前执行源仍是 `current/human-approved-spec.md`。
- 状态：accepted
- 来源：RAW-0035

## DEC-0055

- 决策：intake 与 memory system design spec 在同一模板包中一起创建。
- 理由：两者强相关；intake 收集约束，design spec 基于 intake 生成设计草案，同一入口有利于保持设计闭环。
- 状态：accepted
- 来源：RAW-0035

## DEC-0056

- 决策：当前仍不做真实目标项目交付。
- 理由：本任务只创建模板，不为任何真实目标项目生成交付包，也不假设用户已经确定第一个目标项目场景。
- 状态：accepted
- 来源：RAW-0035

## DEC-0057

- 决策：完成目标项目模板包后，下一步是用户 review、选择第一个目标项目场景或深化 delivery manifest。
- 理由：目标项目模板包需要人工确认；后续可在交付清单闭环和首个场景验证之间选择优先级。
- 状态：accepted
- 来源：RAW-0035

## DEC-0058

- 决策：执行 MNEMOSYNE-029：三类模板包 review 清单与首个目标项目场景选择准备。
- 理由：三类基础模板包已创建，下一步需要为用户 review 和首个试用场景选择提供清晰检查清单与决策矩阵。
- 状态：accepted
- 来源：RAW-0041

## DEC-0059

- 决策：创建 `notes/template-pack-review-and-first-scenario-selection.md`。
- 理由：需要集中呈现三类模板包 review checklist、首个场景候选矩阵、trial run minimal input request 和用户决策选项。
- 状态：accepted
- 来源：RAW-0041

## DEC-0060

- 决策：`notes/template-pack-review-and-first-scenario-selection.md` 不是执行源。
- 理由：该文件只用于 review 和场景选择准备；当前执行源仍是 `current/human-approved-spec.md`。
- 状态：accepted
- 来源：RAW-0041

## DEC-0061

- 决策：当前不直接选择真实目标项目。
- 理由：本任务只做 review / selection 准备，不替用户最终选择，也不生成真实目标项目交付包。
- 状态：accepted
- 来源：RAW-0041

## DEC-0062

- 决策：第一轮试用目标是验证 `intake → design spec → delivery manifest → handoff → review` 的人工闭环。
- 理由：当前 Mnemosyne 仍是半自动设计仓库，第一轮试用应优先验证模板链路，而不是追求完整自动化。
- 状态：accepted
- 来源：RAW-0041

## DEC-0063

- 决策：MNEMOSYNE-029 不进入自动化，不创建 AGENTS.md / CLAUDE.md / GitHub Actions。
- 理由：当前任务边界明确禁止新增自动化脚本、GitHub Actions、RAG、MCP、多 Agent 自动协调，以及 AGENTS.md / CLAUDE.md。
- 状态：accepted
- 来源：RAW-0041

## DEC-0064

- 决策：执行 MNEMOSYNE-030A：研究报告 summary 状态同步与 PDF 图表复核索引补账。
- 理由：MNEMOSYNE-030 后核查发现 PDF 图表复核索引、任务结果记录和状态同步仍需补齐。
- 状态：accepted
- 来源：RAW-0044 / MNEMOSYNE-030A

## DEC-0065

- 决策：补齐 `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`，并将 RPT-2026Q2-0002 ~ RPT-2026Q2-0007 登记为 `pending_manual_review`。
- 理由：PDF 图表 / 图片 / 版式证据尚未人工复核，需要明确索引和状态，避免误用。
- 状态：accepted
- 来源：RAW-0044 / MNEMOSYNE-030A

## DEC-0066

- 决策：report summaries / current-report-summaries / figure review index 不是执行源，当前执行源仍是 `current/human-approved-spec.md`。
- 理由：summary 与索引均为派生视图或复核登记文件，不能直接覆盖用户批准的执行源。
- 状态：accepted
- 来源：RAW-0044 / MNEMOSYNE-030A

## DEC-0067

- 决策：MNEMOSYNE-030A 不修改研究报告原件，不做 OCR，不声称 PDF 图表 / 图片已经被复核。
- 理由：本任务只做补账和状态同步，研究报告原件与 PDF 图表内容复核均超出本任务边界。
- 状态：accepted
- 来源：RAW-0044 / MNEMOSYNE-030A

## DEC-0068

- 决策：未人工复核的 PDF 图表 / 图片不得作为已验证设计证据；后续目标项目设计如果依赖 PDF 图表，应先进行人工复核。
- 理由：避免将仅基于可读取文本的 summary 扩展为图表 / 图片 / 版式已验证事实。
- 状态：accepted
- 来源：RAW-0044 / MNEMOSYNE-030A

## DEC-0069

- 决策：执行 MNEMOSYNE-030C：RC-2026Q2-initial 研究动机 raw 补充与索引。
- 理由：当前仓库已有 7 份研究报告、summaries、evidence map、capability boundaries 和 PDF figure review index，但缺少显式说明这轮研究为什么被发起。
- 状态：accepted
- 来源：RAW-0046 / MNEMOSYNE-030C

## DEC-0070

- 决策：创建 `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`。
- 理由：需要帮助后续 ChatGPT / Codex / Claude / Claude Code 理解 7 份报告为什么存在、分别服务什么设计问题、如何约束 Mnemosyne。
- 状态：accepted
- 来源：RAW-0046 / MNEMOSYNE-030C

## DEC-0071

- 决策：research motivation 不是执行源，也不替代研究报告原件或 report summaries。
- 理由：当前执行源仍是 `current/human-approved-spec.md`；研究报告和 motivation 都属于证据 / 背景 / 审计材料。
- 状态：accepted
- 来源：RAW-0046 / MNEMOSYNE-030C

## DEC-0072

- 决策：后续模型接手时应使用 motivation 理解研究报告作用，推荐先读 motivation，再读 current report summaries，再按需回查原始报告。
- 理由：只读结论可能丢失研究问题、边界和使用方式，增加误把研究证据当执行规则的风险。
- 状态：accepted
- 来源：RAW-0046 / MNEMOSYNE-030C

## DEC-0073

- 决策：后续研究周期也应保留研究动机 / 起点说明。
- 理由：研究动机是设计演化审计材料；新研究或三个月后的 refresh 应创建新 cycle 和 delta report，而不是覆盖历史动机。
- 状态：accepted
- 来源：RAW-0046 / MNEMOSYNE-030C

## DEC-0074

- 决策：执行 MNEMOSYNE-030D：研究课题 prompt 原文入库约定与 report-topic mapping。
- 理由：在研究动机之外，还需要明确本轮研究输入 prompt 与 7 份 report 的对应关系，避免后续模型混淆 prompt、report、summary、motivation 和执行源。
- 状态：accepted
- 来源：RAW-0047 / MNEMOSYNE-030D

## DEC-0075

- 决策：pro prompt 文件约定路径为 `raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/AI_agent_external_persistent_memory_deep_research_prompt_pro.md`，且不重命名用户提供的 pro prompt 文件。
- 理由：prompt 原文是用户提供的研究输入材料，应保持原文件名和可追溯路径。
- 状态：accepted
- 来源：RAW-0047 / MNEMOSYNE-030D

## DEC-0076

- 决策：6 个轻度研究 prompt 原文缺失时不得编造。
- 理由：缺失 prompt 只能记录 report title / topic title / inferred topic，并标记 `missing_original_prompt`；伪造原文会污染研究输入层。
- 状态：accepted
- 来源：RAW-0047 / MNEMOSYNE-030D

## DEC-0077

- 决策：建立 `research-prompt-index.md`、`report-topic-and-prompt-map.md` 和 `current-research-prompts.md`。
- 理由：需要索引 prompt availability、report-topic mapping 和 current 派生视图，帮助后续模型理解研究输入层。
- 状态：accepted
- 来源：RAW-0047 / MNEMOSYNE-030D

## DEC-0078

- 决策：research prompts / mapping 不是执行源。
- 理由：当前执行源仍是 `current/human-approved-spec.md`；prompt / mapping 仅用于理解研究输入和 report-topic 关系。
- 状态：accepted
- 来源：RAW-0047 / MNEMOSYNE-030D

## DEC-0079

- 决策：prompt 是研究输入，report / summary / evidence map 是研究结果 / 派生证据，不得混淆。
- 理由：prompt 可帮助理解研究问题，但不代表研究结论，也不能直接覆盖执行源。
- 状态：accepted
- 来源：RAW-0047 / MNEMOSYNE-030D

## DEC-0080

- 决策：执行 MNEMOSYNE-030E：research motivation / research prompts 状态同步与索引补账。
- 理由：MNEMOSYNE-030C / 030D 主体文件已创建，但 current 索引、状态文件和 task result records 仍需要补齐同步说明。
- 状态：accepted
- 来源：RAW-0048 / MNEMOSYNE-030E

## DEC-0081

- 决策：确认 research motivation 已入库，pro prompt 文件已放入约定路径，6 个轻度研究 prompt 原文缺失且不得编造。
- 理由：这些状态需要进入 answered / todo / handoff / active-context，作为后续接手入口的稳定事实。
- 状态：accepted
- 来源：RAW-0048 / MNEMOSYNE-030E

## DEC-0082

- 决策：补齐 current 索引、active-context、handoff、todo、open-questions、candidate / decision、roadmap / baseline 和 030C / 030D task result reviewer notes。
- 理由：后续模型接手需要从 current 视图和交接文件中看到 research motivation / prompt mapping 已建立，而不是只在主体文件中存在。
- 状态：accepted
- 来源：RAW-0048 / MNEMOSYNE-030E

## DEC-0083

- 决策：motivation / prompts / mapping 不是执行源。
- 理由：当前执行源仍是 `current/human-approved-spec.md`；motivation / prompts / mapping 只用于解释研究动机、研究输入和 report-topic 关系。
- 状态：accepted
- 来源：RAW-0048 / MNEMOSYNE-030E

## DEC-0084

- 决策：执行 MNEMOSYNE-030F：research prompt mapping 硬同步与 030E 结果纠偏。
- 理由：MNEMOSYNE-030E 声称完成状态同步，但后续核查仍发现 current 索引和接手文件需要硬同步。
- 状态：accepted
- 来源：RAW-0049 / MNEMOSYNE-030F

## DEC-0085

- 决策：确认 research motivation 已入库，pro prompt 文件已放入约定路径，6 个轻度研究 prompt 原文缺失且不得编造。
- 理由：这些状态需要作为 answered / todo / handoff / active-context 的稳定接手事实。
- 状态：accepted
- 来源：RAW-0049 / MNEMOSYNE-030F

## DEC-0086

- 决策：补齐 current 索引、active-context、handoff、todo、open-questions，并纠偏 MNEMOSYNE-030E result。
- 理由：后续模型接手需要在 current 视图中直接看到 research motivation / prompt mapping，而不是只依赖主体文件存在。
- 状态：accepted
- 来源：RAW-0049 / MNEMOSYNE-030F

## DEC-0087

- 决策：motivation / prompts / mapping 不是执行源。
- 理由：当前执行源仍是 `current/human-approved-spec.md`；motivation / prompts / mapping 只用于解释研究动机、研究输入和 report-topic 关系。
- 状态：accepted
- 来源：RAW-0049 / MNEMOSYNE-030F
