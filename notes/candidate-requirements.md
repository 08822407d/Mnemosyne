# Candidate Requirements

> 说明：以下为从本次交接抽取的候选需求，不等同于最终实施版。

## CAND-0001
- 内容：Mnemosyne 应被定义为“记忆系统元 Agent”，服务多个项目/研究/团队场景，而非单一项目内部记忆库。
- 状态：reflected
- 备注：已在 `current/human-approved-spec.md` 高层原则中体现。

## CAND-0002
- 内容：采用“模型负责计算，文件负责记忆”的外部持久记忆原则。
- 状态：reflected
- 备注：已在 README 与实施版中体现。

## CAND-0003
- 内容：建立分层结构（raw、candidate、similarity/conflict、human-approved-spec、active-context/handoff）的职责边界。
- 状态：reflected
- 备注：当前仅完成最小结构，细节规则待补充。

## CAND-0004
- 内容：新需求进入实施版前，应执行查重、相似性分析与冲突分析，并提供合并/替换/拒绝/延期选项供用户决策。
- 状态：pending
- 备注：机制存在方向性共识，但流程模板与判定标准尚未定稿。

## CAND-0005
- 内容：引入自动化能力（自动写回、自动查重索引、多 Agent 自动协调等）。
- 状态：pending
- 备注：明确属于后续阶段，不在本次初始化范围。

## CAND-0006
- 内容：7 份研究报告应作为 Mnemosyne 的高权重证据层。
- 状态：accepted_for_evidence_layer
- 来源：RAW-0013

## CAND-0007
- 内容：研究报告应按 research cycle 管理，并保留历史轮次。
- 状态：accepted_for_evidence_layer
- 来源：RAW-0013

## CAND-0008
- 内容：即使不重命名原件，也应通过 report_id 建立稳定引用。
- 状态：accepted_for_evidence_layer
- 来源：RAW-0013

## CAND-0009
- 内容：研究报告不是执行源；执行源仍为 human-approved-spec。
- 状态：accepted_for_evidence_layer
- 来源：RAW-0013

## CAND-0010
- 内容：新设计机制应先检查 current-evidence-map 与 current-capability-boundaries。
- 状态：pending
- 来源：RAW-0013

## CAND-0011
- 内容：PDF 图表与图片证据需要人工复核后再用于高影响决策。
- 状态：accepted_for_evidence_layer
- 来源：RAW-0013

## CAND-0012
- 内容：研究报告具有时效性，需要 refresh policy 与轮次治理。
- 状态：accepted_for_evidence_layer
- 来源：RAW-0013

## CAND-0013
- 内容：后续需要设计 Evidence Item 模板，支撑细粒度证据复用。
- 状态：pending
- 来源：RAW-0013

## CAND-0014
- 内容：后续需要为每份报告生成 summary。
- 状态：pending
- 来源：RAW-0013

## CAND-0015
- 内容：后续需要 delta report 比较新旧研究轮次，避免静默覆盖。
- 状态：pending
- 来源：RAW-0013

## CAND-0016
- 内容：Mnemosyne 需要支持新 ChatGPT 对话或新 Codex 任务直接接手当前工作。
- 状态：reflected
- 来源：RAW-0019
- 反映位置：current/active-context.md；handoff/handoff-current.md

## CAND-0017
- 内容：active-context 必须反映真实当前阶段，不能停留在过期的“待修复”状态。
- 状态：reflected
- 来源：RAW-0019
- 反映位置：current/active-context.md

## CAND-0018
- 内容：handoff-current 必须作为新会话接手卡，包含执行源、研究证据层状态、推荐读取顺序、不要做的事项和下一步建议。
- 状态：reflected
- 来源：RAW-0019
- 反映位置：handoff/handoff-current.md

## CAND-0019
- 内容：current/todo.md 应按 v0.1-final、v0.2、future 分组，避免把已经完成的接手层修复继续列为未完成任务。
- 状态：reflected
- 来源：RAW-0019
- 反映位置：current/todo.md

## CAND-0020
- 内容：startup-instructions 应作为下一项 v0.1-final 收尾工作，用于让新 ChatGPT 对话或新 Codex 任务按固定读取顺序接手 Mnemosyne。
- 状态：todo
- 来源：RAW-0019
- 反映位置：current/todo.md；handoff/handoff-current.md

## CAND-0021
- 内容：需要进行一次新 ChatGPT / 新 Codex 接手演练，以验证 startup-instructions、handoff-current、active-context 和 human-approved-spec 是否足以支持接手。
- 状态：todo
- 来源：RAW-0019
- 反映位置：current/todo.md；handoff/handoff-current.md

## CAND-0022
- 内容：新机制设计前应读取 current-evidence-map 与 current-capability-boundaries，以尊重 7 份研究报告给出的能力边界。
- 状态：reflected
- 来源：RAW-0019
- 反映位置：handoff/handoff-current.md；raw/research-reports/current/current-evidence-map.md；raw/research-reports/current/current-capability-boundaries.md

## CAND-0023

- 内容：Mnemosyne 需要 startup-instructions 指导新 ChatGPT 对话、新 Codex Cloud 任务或未来其他 Agent 接手仓库。
- 状态：reflected
- 来源：RAW-0020B
- 反映位置：handoff/startup-instructions.md

## CAND-0024

- 内容：startup-instructions 必须明确自身不是执行源，当前执行源仍为 current/human-approved-spec.md。
- 状态：reflected
- 来源：RAW-0020B
- 反映位置：handoff/startup-instructions.md

## CAND-0025

- 内容：startup-instructions 应包含新 ChatGPT 对话启动提示，要求新对话按固定读取顺序接手。
- 状态：reflected
- 来源：RAW-0020B
- 反映位置：handoff/startup-instructions.md

## CAND-0026

- 内容：startup-instructions 应包含新 Codex Cloud 任务启动提示，要求新任务只根据仓库文件接手，不依赖旧任务上下文。
- 状态：reflected
- 来源：RAW-0020B
- 反映位置：handoff/startup-instructions.md

## CAND-0027

- 内容：startup-instructions 应规定在能力边界判断、新机制设计、平台适配和目标项目设计前读取研究证据 current 视图。
- 状态：reflected
- 来源：RAW-0020B
- 反映位置：handoff/startup-instructions.md；raw/research-reports/current/current-evidence-map.md；raw/research-reports/current/current-capability-boundaries.md

## CAND-0028

- 内容：startup-instructions 创建后仍需要进行新 ChatGPT / 新 Codex 接手演练，以验证仓库是否能脱离当前对话上下文继续工作。
- 状态：todo
- 来源：RAW-0020B
- 反映位置：current/todo.md；notes/v0.1-scope-and-consistency-check.md

## CAND-0029

- 内容：Mnemosyne 需要进行 startup rehearsal / 接手演练，以验证新会话可仅依赖仓库文件接手。
- 状态：reflected
- 来源：RAW-0021
- 反映位置：notes/startup-rehearsal-report.md

## CAND-0030

- 内容：接手演练报告应识别执行源和非执行源，并在冲突时回退到 `current/human-approved-spec.md`。
- 状态：reflected
- 来源：RAW-0021
- 反映位置：notes/startup-rehearsal-report.md

## CAND-0031

- 内容：接手演练应检查 startup-instructions、active-context、handoff 和 todo 是否一致。
- 状态：reflected
- 来源：RAW-0021
- 反映位置：notes/startup-rehearsal-report.md

## CAND-0032

- 内容：接手演练后应由用户 review，再决定是否进入 v0.2。
- 状态：todo
- 来源：RAW-0021
- 反映位置：current/todo.md；handoff/handoff-current.md

## CAND-0033

- 内容：如果接手演练发现阻断问题，应先修复再进入 v0.2。
- 状态：reflected
- 来源：RAW-0021
- 反映位置：notes/startup-rehearsal-report.md；notes/v0.1-scope-and-consistency-check.md
