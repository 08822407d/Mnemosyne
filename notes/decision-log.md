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

- 决策：建立 `notes/system-construction-baseline.md`。
- 理由：将当前相对确定的系统建设目标、工作约定、后续路线和诊断暂存为更明确的基线快照，降低长对话压缩后的路线偏移风险。
- 状态：accepted
- 来源：RAW-0027

## DEC-0047

- 决策：`notes/system-construction-baseline.md` 不是执行源。
- 理由：执行源仍为 `current/human-approved-spec.md`，基线快照仅用于路线回查和上下文恢复。
- 状态：accepted
- 来源：RAW-0027

## DEC-0048

- 决策：后续 Codex 任务是否必须新开，按“是否必须在全新任务中执行”判断。
- 理由：避免把“新开更好”误写为硬性要求；在现有任务干净、基于最新 master 且无未合并改动时可以继续使用。
- 状态：accepted
- 来源：RAW-0027

## DEC-0049

- 决策：后续 Codex 任务内容优先通过 txt 文件提供。
- 理由：减少聊天界面代码块嵌套导致任务描述复制不完整的风险。
- 状态：accepted
- 来源：RAW-0027

## DEC-0050

- 决策：Codex Task Result Record 默认路径为 `notes/codex-task-results/TASK_ID-result.md`。
- 理由：统一任务审计记录位置和命名，避免出现缺失 TASK_ID 的错误路径。
- 状态：accepted
- 来源：RAW-0027

## DEC-0051

- 决策：在进入模板设计前先修正 self-improvement workflow 的格式和路径问题。
- 理由：先稳定现有 workflow 文档和记录路径，避免后续模板继承错误。
- 状态：accepted
- 来源：RAW-0027


## DEC-0052

- 决策：执行 MNEMOSYNE-025F：任务结果路径纠偏与 self-improvement 工作流格式清理。
- 理由：进入模板设计前，需要先消除 task result record 路径错误并提高 workflow / baseline 的可 review 性。
- 状态：accepted
- 来源：RAW-0028

## DEC-0053

- 决策：Codex Task Result Record 默认路径统一为 `notes/codex-task-results/TASK_ID-result.md`。
- 理由：避免缺失 TASK_ID 的错误路径继续传播到后续任务和模板。
- 状态：accepted
- 来源：RAW-0028

## DEC-0054

- 决策：在进入 self-improvement workflow 模板设计前，先清理 workflow 与 baseline 的格式。
- 理由：先保证基础说明文件可读、可 diff、可局部维护，再进入模板设计。
- 状态：accepted
- 来源：RAW-0028

## DEC-0055

- 决策：修正 MNEMOSYNE-025E-result 中关于路径纠偏的错误表述。
- 理由：025E 实际仍残留错误路径，需要由 025F 如实记录纠偏。
- 状态：accepted
- 来源：RAW-0028

## DEC-0056

- 决策：执行 MNEMOSYNE-025G：错误结果路径全仓库硬纠偏。
- 理由：MNEMOSYNE-025F 后仍发现错误结果路径残留，需在进入模板设计前硬性纠偏。
- 状态：accepted
- 来源：RAW-0029

## DEC-0057

- 决策：Codex Task Result Record 默认路径统一为 `notes/codex-task-results/TASK_ID-result.md`。
- 理由：避免缺失 TASK_ID 的错误路径继续污染后续任务结果记录和模板设计。
- 状态：accepted
- 来源：RAW-0029

## DEC-0058

- 决策：路径纠偏必须先于 MNEMOSYNE-026。
- 理由：模板设计会复用路径约定，必须先保证路径正确。
- 状态：accepted
- 来源：RAW-0029

## DEC-0059

- 决策：Markdown 格式清理可以作为非阻断后续任务，但不应影响路径正确性。
- 理由：当前最小目标是硬纠偏错误路径；格式优化可独立后续处理。
- 状态：accepted
- 来源：RAW-0029

## DEC-0060

- 决策：执行 MNEMOSYNE-025H：Codex Task Result Record 路径占位符规范化。
- 理由：尖括号占位符在 Markdown、HTML、工具或模型改写中存在歧义，且此前多次出现缺失 TASK_ID 的错误路径。
- 状态：accepted
- 来源：RAW-0030

## DEC-0061

- 决策：Codex Task Result Record 默认占位符路径统一为 `notes/codex-task-results/TASK_ID-result.md`。
- 理由：使用无尖括号的 TASK_ID 占位符降低转义、渲染和自动改写风险。
- 状态：accepted
- 来源：RAW-0030

## DEC-0062

- 决策：不再使用 `<TASK_ID>` 作为默认占位符。
- 理由：尖括号形式容易被 Markdown、HTML、工具或模型处理为特殊标记，增加错误写回风险。
- 状态：accepted
- 来源：RAW-0030

## DEC-0063

- 决策：路径占位符规范化必须先于 MNEMOSYNE-026。
- 理由：self-improvement workflow 模板设计会复用任务结果记录路径，必须先稳定占位符规范。
- 状态：accepted
- 来源：RAW-0030

## DEC-0064

- 决策：Markdown 格式清理可以作为非阻断后续任务，但不应影响路径正确性。
- 理由：当前最小目标是路径占位符规范化；格式优化可独立后续处理。
- 状态：accepted
- 来源：RAW-0030
