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

- 决策：接受 MNEMOSYNE-023 独立验证结论为 PASS_WITH_WARNINGS。
- 理由：独立验证未发现阻断性问题，Mnemosyne v0.1 已具备新 ChatGPT / 新 Codex 任务按仓库文件接手的基础能力；剩余问题属于非阻断补强项。
- 状态：accepted
- 来源：notes/v0.1-independent-verification-report.md；MNEMOSYNE-023A；MNEMOSYNE-023B

## DEC-0028

- 决策：将 CAND-0020 与 CAND-0021 同步为 reflected。
- 理由：startup-instructions 已创建，接手演练已通过，继续保留 todo 状态会误导后续任务。
- 状态：accepted
- 来源：MNEMOSYNE-023B

## DEC-0029

- 决策：保留研究报告 summary、PDF 图表人工复核和 Evidence Item 模板为后续补强项。
- 理由：这些事项有助于提高证据层质量，但不阻断 v0.1 可接手性。
- 状态：accepted
- 来源：notes/v0.1-independent-verification-report.md；MNEMOSYNE-023B

## DEC-0030

- 决策：将“只读回归验证”作为可选非阻断项，而不是进入 v0.2 的硬性前置条件。
- 理由：MNEMOSYNE-023 已经完成独立验证并给出 PASS_WITH_WARNINGS；如用户需要更强信心，可再执行只读回归验证。
- 状态：accepted
- 来源：MNEMOSYNE-023B

