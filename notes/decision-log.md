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

- 决策：确认 `handoff/startup-instructions.md` 已创建。
- 理由：该文件为新 ChatGPT 对话、新 Codex Cloud 任务或未来其他 Agent 提供固定启动说明。
- 状态：accepted
- 来源：RAW-0020B

## DEC-0019

- 决策：确认 startup-instructions 不是执行源。
- 理由：startup-instructions 只负责启动读取顺序和接手流程，执行源仍是 `current/human-approved-spec.md`。
- 状态：accepted
- 来源：RAW-0020B

## DEC-0020

- 决策：startup-instructions 同时服务新 ChatGPT 对话和新 Codex Cloud 任务。
- 理由：Mnemosyne 需要跨对话、跨任务接手能力，不能依赖当前会话上下文。
- 状态：accepted
- 来源：RAW-0020B

## DEC-0021

- 决策：涉及能力边界、新机制设计、平台适配和目标项目记忆系统设计时，启动流程必须读取 current-evidence-map 和 current-capability-boundaries。
- 理由：7 份研究报告是当前高权重证据层，可降低平台能力误判和过度自动化承诺。
- 状态：accepted
- 来源：RAW-0020B

## DEC-0022

- 决策：startup-instructions 完成后，下一步是接手演练。
- 理由：需要验证新 ChatGPT / 新 Codex 任务能否只依赖仓库文件接手当前工作。
- 状态：accepted
- 来源：RAW-0020B

## DEC-0023

- 决策：创建 `notes/startup-rehearsal-report.md` 记录接手演练结果。
- 理由：需要形成可审阅、可追溯的接手验证证据。
- 状态：accepted
- 来源：RAW-0021

## DEC-0024

- 决策：将接手演练作为进入 v0.2 前的验证步骤。
- 理由：先确认新会话可按仓库文件稳定接手，再进入新阶段设计。
- 状态：accepted
- 来源：RAW-0021

## DEC-0025

- 决策：接手演练报告不是执行源。
- 理由：报告用于验证与说明，不替代 `current/human-approved-spec.md` 的执行地位。
- 状态：accepted
- 来源：RAW-0021

## DEC-0026

- 决策：接手演练通过后仍需要用户 review。
- 理由：用户 review 是 v0.1-final 的必要收尾控制点。
- 状态：accepted
- 来源：RAW-0021

## DEC-0027

- 决策：若接手演练发现阻断问题，应先修复再进入 v0.2。
- 理由：避免带着关键不一致进入下一阶段，降低后续返工风险。
- 状态：accepted
- 来源：RAW-0021

## DEC-0028

- 决策：将 MNEMOSYNE-021 接手演练结论记录为 pass。
- 理由：演练报告确认当前文件集足以支持新 ChatGPT / 新 Codex 仅依赖仓库文件接手。
- 状态：accepted
- 来源：RAW-0022；notes/startup-rehearsal-report.md

## DEC-0029

- 决策：startup-rehearsal-report 不是执行源。
- 理由：该报告用于验证和审计，不替代 `current/human-approved-spec.md` 的执行地位。
- 状态：accepted
- 来源：RAW-0022；notes/startup-rehearsal-report.md

## DEC-0030

- 决策：接手演练通过后更新 active-context、handoff-current 和 todo。
- 理由：需要将“等待接手演练”状态切换为“接手演练已通过，等待用户 review 和 v0.2 方向选择”。
- 状态：accepted
- 来源：RAW-0022

## DEC-0031

- 决策：v0.1 接手能力通过初步验证后，进入用户 review 与 v0.2 方向选择。
- 理由：先完成用户确认，再进入下一阶段方向性设计，降低误判和返工风险。
- 状态：accepted
- 来源：RAW-0022

## DEC-0032

- 决策：在正式进入 v0.2 前，不默认创建 AGENTS.md、CLAUDE.md、GitHub Actions 或自动化流程。
- 理由：这些事项仍属于后续方向选择与治理决策范围，不应在本次状态校正中提前实现。
- 状态：accepted
- 来源：RAW-0022
