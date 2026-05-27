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
- 决策：确认 7 份研究报告已作为 RC-2026Q2-initial 原始证据入库。
- 理由：修复 current 视图与 cycle 状态不同步问题。
- 来源：RAW-0014
- 状态：accepted

## DEC-0013
- 决策：保留原文件名，通过 report_id 建立稳定引用。
- 理由：维持证据原件完整性并确保跨文档引用稳定。
- 来源：RAW-0014
- 状态：accepted

## DEC-0014
- 决策：将 current-evidence-map 作为当前研究证据派生视图。
- 理由：统一后续任务读取入口，避免直接散读原件。
- 来源：RAW-0014
- 状态：accepted

## DEC-0015
- 决策：将 current-capability-boundaries 作为当前能力边界派生视图。
- 理由：明确平台能力边界的当前共识与待复核项。
- 来源：RAW-0014
- 状态：accepted

## DEC-0016
- 决策：研究报告不是执行源。
- 理由：执行源仍为 human-approved-spec，避免证据直接覆盖执行规则。
- 来源：RAW-0014
- 状态：accepted

## DEC-0017
- 决策：PDF 图表和图片需要人工复核。
- 理由：当前自动解析对图像/图表可靠性有限。
- 来源：RAW-0014
- 状态：accepted

## DEC-0018
- 决策：后续为每份报告建立 summary。
- 理由：降低后续任务重复阅读成本，提高可追溯效率。
- 来源：RAW-0014
- 状态：accepted

## DEC-0019
- 决策：后续新增机制设计必须参考 current-evidence-map 与 current-capability-boundaries。
- 理由：避免脱离高权重证据层做能力越界承诺。
- 来源：RAW-0014
- 状态：accepted

## DEC-0020
- 决策：执行 v0.1 接手能力最终修复与当前状态同步。
- 理由：确保新会话可用最小文件集正确接手并继续工作。
- 状态：accepted
- 来源引用：RAW-0015

## DEC-0021
- 决策：将 human-approved-spec 更新为 v0.1 当前执行源。
- 理由：原实施版过短，无法完整承载当前阶段执行边界。
- 状态：accepted
- 来源引用：RAW-0015

## DEC-0022
- 决策：active-context 必须反映真实当前阶段。
- 理由：避免新会话误判阶段状态与下一步动作。
- 状态：accepted
- 来源引用：RAW-0015

## DEC-0023
- 决策：handoff-current 必须支持新会话直接接手。
- 理由：handoff 是跨会话恢复效率的关键入口。
- 状态：accepted
- 来源引用：RAW-0015

## DEC-0024
- 决策：研究报告 current 视图作为新机制设计前的能力边界依据。
- 理由：减少超出证据支持范围的设计承诺。
- 状态：accepted
- 来源引用：RAW-0015

## DEC-0025
- 决策：startup-instructions 作为下一批关键收尾工作。
- 理由：当前文档已基本齐备，下一步需固化启动步骤。
- 状态：accepted
- 来源引用：RAW-0015

## DEC-0026
- 决策：当前仍不引入 AGENTS.md、CLAUDE.md、GitHub Actions 或自动化流程。
- 理由：v0.1 目标是稳态接手能力，不是自动化扩展。
- 状态：accepted
- 来源引用：RAW-0015


## DEC-0027
- 决策：执行 RAW-0015 的落实修复，并以 current/handoff 实际状态作为完成判据。
- 理由：仅新增 raw 记录不足以完成接手能力修复，必须反映到执行与接手文件。
- 状态：accepted
- 来源引用：RAW-0016, RAW-0015

## DEC-0028
- 决策：当前阶段描述统一为“v0.1 接手能力最终修复已落实”。
- 理由：避免继续显示“下一步才修复”造成接手误判。
- 状态：accepted
- 来源引用：RAW-0016


## DEC-0029
- 决策：执行 v0.1 接手能力实际落地校正。
- 理由：修复 RAW-0016 与 current/handoff 实际状态不一致问题。
- 状态：accepted
- 来源引用：RAW-0017

## DEC-0030
- 决策：human-approved-spec 持续作为 v0.1 当前执行源。
- 理由：避免把证据层、候选层或交接层误当执行要求。
- 状态：accepted
- 来源引用：RAW-0017

## DEC-0031
- 决策：active-context 必须反映“已完成接手修复，等待 review”。
- 理由：保证新会话不会误读为仍在修复阶段。
- 状态：accepted
- 来源引用：RAW-0017

## DEC-0032
- 决策：handoff-current 必须支持新会话直接接手。
- 理由：确保跨会话可快速恢复状态并执行下一步。
- 状态：accepted
- 来源引用：RAW-0017

## DEC-0033
- 决策：研究报告 current 视图作为新机制设计前的能力边界依据。
- 理由：减少能力越界承诺与平台误判。
- 状态：accepted
- 来源引用：RAW-0017

## DEC-0034
- 决策：startup-instructions 作为下一批关键收尾工作。
- 理由：文档基线已具备，下一步需固化启动流程。
- 状态：accepted
- 来源引用：RAW-0017

## DEC-0035
- 决策：当前仍不引入 AGENTS.md、CLAUDE.md、GitHub Actions 或自动化流程。
- 理由：v0.1-final 目标是稳定接手，不是自动化扩展。
- 状态：accepted
- 来源引用：RAW-0017


## DEC-0036
- 决策：执行 MNEMOSYNE-018（v0.1 接手层强制覆盖修复）。
- 理由：前序任务与实际文件状态不一致，需强制覆盖校正。
- 状态：accepted
- 来源引用：RAW-0018

## DEC-0037
- 决策：直接重写 active-context 进入“接手能力已完成”状态。
- 理由：避免继续误导新会话认为仍在修复阶段。
- 状态：accepted
- 来源引用：RAW-0018

## DEC-0038
- 决策：直接重写 handoff-current 作为新会话接手卡。
- 理由：确保跨会话接手可读、可执行、可审阅。
- 状态：accepted
- 来源引用：RAW-0018

## DEC-0039
- 决策：从 TODO 中移除“执行 v0.1 接手能力修复”未完成项。
- 理由：该事项在本轮为已完成状态，不应继续作为未完成任务。
- 状态：accepted
- 来源引用：RAW-0018

## DEC-0040
- 决策：将 startup-instructions 作为下一步关键工作。
- 理由：当前接手层已完成校正，下一步应固化启动流程。
- 状态：accepted
- 来源引用：RAW-0018

## DEC-0041
- 决策：在 startup-instructions 前完成接手演练准备。
- 理由：先验证接手链路可用，再固化启动标准。
- 状态：accepted
- 来源引用：RAW-0018
