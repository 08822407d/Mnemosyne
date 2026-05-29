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
- 状态：reflected
- 来源：RAW-0019
- 反映位置：handoff/startup-instructions.md；current/todo.md；notes/v0.1-independent-verification-report.md

## CAND-0021

- 内容：需要进行一次新 ChatGPT / 新 Codex 接手演练，以验证 startup-instructions、handoff-current、active-context 和 human-approved-spec 是否足以支持接手。
- 状态：reflected
- 来源：RAW-0019
- 反映位置：notes/startup-rehearsal-report.md；current/todo.md；notes/v0.1-independent-verification-report.md

## CAND-0022

- 内容：新机制设计前应读取 current-evidence-map 与 current-capability-boundaries，以尊重 7 份研究报告给出的能力边界。
- 状态：reflected
- 来源：RAW-0019
- 反映位置：handoff/handoff-current.md；raw/research-reports/current/current-evidence-map.md；raw/research-reports/current/current-capability-boundaries.md

## CAND-0023

- 内容：Mnemosyne 需要记录 MNEMOSYNE-021 接手演练结果为 pass，并将该结论写入当前状态层。
- 状态：reflected
- 来源：RAW-0022；notes/startup-rehearsal-report.md
- 反映位置：current/active-context.md；handoff/handoff-current.md；notes/v0.1-scope-and-consistency-check.md

## CAND-0024

- 内容：active-context 应在接手演练通过后进入“v0.1 最终 review / v0.2 方向选择”状态。
- 状态：reflected
- 来源：RAW-0022；notes/startup-rehearsal-report.md
- 反映位置：current/active-context.md

## CAND-0025

- 内容：handoff-current 应明确 startup-instructions 已创建、接手演练已通过，且当前文件集足以支持新 ChatGPT / 新 Codex 任务仅依赖仓库文件接手。
- 状态：reflected
- 来源：RAW-0022；notes/startup-rehearsal-report.md
- 反映位置：handoff/handoff-current.md

## CAND-0026

- 内容：v0.1-final TODO 应将“做一次新 ChatGPT / 新 Codex 接手演练”标记为完成，并保留用户最终 review 与研究证据补强项为未完成。
- 状态：reflected
- 来源：RAW-0022；notes/startup-rehearsal-report.md
- 反映位置：current/todo.md

## CAND-0027

- 内容：open-questions 应将“v0.1 是否足以支持新对话接手”标记为 answered，并引用接手演练 pass 结论。
- 状态：reflected
- 来源：RAW-0022；notes/startup-rehearsal-report.md
- 反映位置：current/open-questions.md

## CAND-0028

- 内容：v0.1-scope-and-consistency-check 应删除“startup-instructions 待完成 / 接手演练待完成”的旧状态，并改为“v0.1 接手能力已覆盖、等待用户最终 review”。
- 状态：reflected
- 来源：RAW-0022；notes/startup-rehearsal-report.md
- 反映位置：notes/v0.1-scope-and-consistency-check.md

## CAND-0029

- 内容：Mnemosyne 需要 v0.1 final review 文件帮助用户最终确认可接手性。
- 状态：reflected
- 来源：RAW-0022
- 反映位置：notes/v0.1-final-review.md

## CAND-0030

- 内容：v0.2 第一方向应由用户在 final review 后选择。
- 状态：pending
- 来源：RAW-0022

## CAND-0031

- 内容：v0.1 final review 不是执行源。
- 状态：reflected
- 来源：RAW-0022
- 反映位置：notes/v0.1-final-review.md；notes/decision-log.md

## CAND-0032

- 内容：final review 应列出已完成内容、未完成内容、v0.2 候选方向和用户需决定的问题。
- 状态：reflected
- 来源：RAW-0022
- 反映位置：notes/v0.1-final-review.md

## CAND-0033

- 内容：self-improvement workflow 应优先设计“用户新构想 / 使用反馈 / Codex 或 ChatGPT 结果 → raw → candidate → similarity/conflict → 用户确认 → spec/todo/open question”的半自动流程。
- 状态：reflected
- 来源：RAW-0024
- 反映位置：notes/self-improvement-workflow.md


## CAND-0034

- 内容：v0.2 第一方向已选择 self-improvement workflow。
- 状态：reflected
- 来源：RAW-0024
- 反映位置：current/active-context.md；current/todo.md

## CAND-0035

- 内容：self-improvement workflow 仍保持半自动，不引入自动写回、自动查重、GitHub Actions、AGENTS.md 或 CLAUDE.md。
- 状态：reflected
- 来源：RAW-0024；RAW-0025
- 反映位置：notes/self-improvement-workflow.md

## CAND-0036

- 内容：进入 self-improvement workflow 设计时仍不引入自动写回、自动查重、GitHub Actions、AGENTS.md 或 CLAUDE.md。
- 状态：reflected
- 来源：RAW-0024
- 反映位置：current/active-context.md；handoff/handoff-current.md


## CAND-0037

- 内容：Mnemosyne 需要 self-improvement workflow 支持自身持续演化。
- 状态：reflected
- 来源：RAW-0025
- 反映位置：notes/self-improvement-workflow.md

## CAND-0038

- 内容：用户新构想和使用反馈必须先进入 raw / candidate，不得直接更新执行源。
- 状态：reflected
- 来源：RAW-0025
- 反映位置：notes/self-improvement-workflow.md

## CAND-0039

- 内容：Codex Task Result Record 应作为审计材料，不是执行源。
- 状态：reflected
- 来源：RAW-0025
- 反映位置：notes/self-improvement-workflow.md

## CAND-0040

- 内容：新机制设计前应按需回查 research evidence。
- 状态：reflected
- 来源：RAW-0025
- 反映位置：notes/self-improvement-workflow.md

## CAND-0041

- 内容：self-improvement workflow 当前是半自动流程，不实现自动查重或自动写回。
- 状态：reflected
- 来源：RAW-0025
- 反映位置：notes/self-improvement-workflow.md

## CAND-0042

- 内容：后续可能需要 self-improvement 模板、similarity/conflict 模板和 user decision 模板。
- 状态：pending
- 来源：RAW-0025

## CAND-0043

- 内容：需要保存总体目标与路线图快照，防止长期规划只留在当前对话上下文。
- 状态：pending
- 来源：RAW-0026；MNEMOSYNE-025D

## CAND-0044

- 内容：总体目标与路线图快照不是执行源。
- 状态：pending
- 来源：RAW-0026；MNEMOSYNE-025D

## CAND-0045

- 内容：后续任务应根据路线图快照检查是否偏离长期目标。
- 状态：pending
- 来源：RAW-0026；MNEMOSYNE-025D

## CAND-0046

- 内容：self-improvement workflow 清理应先于模板设计。
- 状态：pending
- 来源：RAW-0026；MNEMOSYNE-025D

## CAND-0047

- 内容：每个后续 Codex 任务应写入 Codex Task Result Record。
- 状态：pending
- 来源：RAW-0026；MNEMOSYNE-025D

## CAND-0048

- 内容：需要创建 `notes/self-improvement-template-pack.md`，作为 self-improvement workflow 的可操作模板入口。
- 状态：reflected
- 来源：RAW-0031
- 反映位置：notes/self-improvement-template-pack.md

## CAND-0049

- 内容：self-improvement template pack 不是执行源；当前执行源仍是 `current/human-approved-spec.md`。
- 状态：reflected
- 来源：RAW-0031
- 反映位置：notes/self-improvement-template-pack.md；notes/self-improvement-workflow.md

## CAND-0050

- 内容：template pack 应包含 raw、candidate、conflict check、user decision、codex task result、ChatGPT summary、research refresh、target project feedback、open question、todo、apply checklist 和 runbook。
- 状态：reflected
- 来源：RAW-0031
- 反映位置：notes/self-improvement-template-pack.md

## CAND-0051

- 内容：Codex Task Result Record 默认路径使用 `notes/codex-task-results/TASK_ID-result.md`，实际任务将 `TASK_ID` 替换为真实任务编号。
- 状态：reflected
- 来源：RAW-0031
- 反映位置：notes/self-improvement-template-pack.md；notes/self-improvement-workflow.md；notes/codex-task-results/MNEMOSYNE-026-result.md

## CAND-0052

- 内容：完成 self-improvement template pack 后需要用户 review，并根据 review 决定是否小修模板。
- 状态：pending
- 来源：RAW-0031
- 反映位置：current/todo.md；current/active-context.md；handoff/handoff-current.md

## CAND-0053

- 内容：self-improvement template pack 完成后，后续应进入目标项目 intake / memory system design spec 模板设计。
- 状态：pending
- 来源：RAW-0031
- 反映位置：current/todo.md；current/active-context.md；handoff/handoff-current.md
