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

- 决策：创建 `handoff/startup-instructions.md` 作为统一启动说明入口。
- 理由：新会话需要在不依赖旧上下文时，以固定读取顺序稳定接手 Mnemosyne。
- 状态：accepted
- 来源：RAW-0020

## DEC-0019

- 决策：startup-instructions 明确为非执行源，执行冲突统一回退到 `current/human-approved-spec.md`。
- 理由：避免启动说明在跨会话使用中被误当作执行依据，破坏执行源唯一性。
- 状态：accepted
- 来源：RAW-0020

## DEC-0020

- 决策：startup-instructions 完成后，v0.1-final 下一优先项为新 ChatGPT / 新 Codex 接手演练。
- 理由：需要验证“固定读取顺序 + 执行源边界 + 研究证据入口”是否足以支持真实接手。
- 状态：accepted
- 来源：RAW-0020

## DEC-0021

- 决策：startup-instructions 同时服务新 ChatGPT 对话和新 Codex Cloud 任务。
- 理由：两类接手入口都需要统一读取顺序、执行源边界和第一条回复结构，以降低接手漂移。
- 状态：accepted
- 来源：RAW-0020

## DEC-0022

- 决策：涉及能力边界、新机制设计、平台适配和目标项目设计时，启动流程必须读取 `current-evidence-map` 和 `current-capability-boundaries`。
- 理由：研究证据 current 视图是高权重边界入口，可降低能力误判和过度承诺风险。
- 状态：accepted
- 来源：RAW-0020
