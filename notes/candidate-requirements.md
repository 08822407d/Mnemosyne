# Candidate Requirements

> 说明：以下为从交接材料抽取的候选需求，不等同于最终实施版。

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
- 内容：research-report-index 必须反映 originals 中实际文件，而非占位状态。
- 状态：accepted_for_evidence_layer
- 来源：RAW-0014

## CAND-0017
- 内容：current-evidence-map 应作为当前设计证据派生视图，并标注 active/needs_review。
- 状态：accepted_for_evidence_layer
- 来源：RAW-0014

## CAND-0018
- 内容：current-capability-boundaries 应作为当前能力边界派生视图，并标注时效性。
- 状态：accepted_for_evidence_layer
- 来源：RAW-0014

## CAND-0019
- 内容：后续需要为每份报告生成 summary，必要时将 PDF 转换为 Markdown / TXT。
- 状态：pending
- 来源：RAW-0014

## CAND-0020
- 内容：后续需要 Evidence Item 模板与 delta report 模板，支持跨轮次证据比较。
- 状态：pending
- 来源：RAW-0014

## CAND-0021
- 内容：新增机制设计前应检查 current-evidence-map 与 current-capability-boundaries。
- 状态：pending
- 来源：RAW-0014

## CAND-0022
- 标题：支持新 ChatGPT / 新 Codex 任务接手
- 状态：reflected
- 说明：Mnemosyne 需要通过执行源 + active-context + handoff + current research 视图支持新会话接手。
- 来源引用：RAW-0015
- 已反映位置：human-approved-spec / active-context / handoff

## CAND-0023
- 标题：human-approved-spec 覆盖 v0.1 当前执行原则
- 状态：reflected
- 说明：执行源应明确定位、边界、研究证据层关系与 v0.1 能力边界。
- 来源引用：RAW-0015
- 已反映位置：human-approved-spec

## CAND-0024
- 标题：active-context 反映真实当前阶段
- 状态：reflected
- 说明：active-context 需要准确描述已完成/未完成与下一步建议，避免误导新会话。
- 来源引用：RAW-0015
- 已反映位置：active-context

## CAND-0025
- 标题：handoff-current 支持未来 AI 会话接手
- 状态：reflected
- 说明：handoff 应提供简洁读取顺序、边界提醒与下一步动作。
- 来源引用：RAW-0015
- 已反映位置：handoff

## CAND-0026
- 标题：新机制设计前读取研究报告 current 视图
- 状态：reflected
- 说明：新机制设计前应读取 `research-report-index`、`current-evidence-map`、`current-capability-boundaries`。
- 来源引用：RAW-0015
- 已反映位置：human-approved-spec / handoff / active-context

## CAND-0027
- 标题：近原文核心构想摘录作为 raw 证据按需回查
- 状态：reflected
- 说明：`raw/concept-origin-extract-001.md` 作为动机与边界证据，默认按需回查而非全量加载。
- 来源引用：RAW-0015, RAW-0001
- 已反映位置：active-context / handoff

## CAND-0028
- 标题：需要 startup-instructions 或启动包
- 状态：todo
- 说明：为新会话提供标准启动指引，降低接手成本。
- 来源引用：RAW-0015
- 已反映位置：todo（待实现）

## CAND-0029
- 标题：需要接手演练
- 状态：todo
- 说明：完成一次新 ChatGPT / 新 Codex 接手演练以验证文档可用性。
- 来源引用：RAW-0015
- 已反映位置：todo（待实现）

## CAND-0030
- 标题：需要目标项目记忆系统设计模板
- 状态：pending
- 说明：作为 v0.2 的核心交付入口，支持多场景复用。
- 来源引用：RAW-0015
- 已反映位置：todo（v0.2）

## CAND-0031
- 标题：需要 self-improvement workflow 或继续完善需求进入流程
- 状态：pending
- 说明：将用户反馈、候选需求与实施版更新形成可持续闭环。
- 来源引用：RAW-0015
- 已反映位置：todo（v0.2）

## CAND-0032
- 标题：当前仍不做自动化
- 状态：reflected
- 说明：v0.1 阶段不引入自动查重、自动索引、自动写回、Actions、多 Agent 自动协调。
- 来源引用：RAW-0015
- 已反映位置：human-approved-spec / handoff / todo


## CAND-0033
- 标题：执行 RAW-0015 的落实修复检查
- 状态：reflected
- 说明：除写入 RAW 外，current/handoff/notes 关键文件必须同步落地，才能算完成。
- 来源引用：RAW-0016, RAW-0015
- 已反映位置：human-approved-spec / active-context / handoff / v0.1-scope-check

## CAND-0034
- 标题：v0.1 接手状态应标记为“已落实”
- 状态：reflected
- 说明：active-context 与 handoff 不应继续写“下一步才修复”，应反映已落实状态。
- 来源引用：RAW-0016
- 已反映位置：active-context / handoff


## CAND-0035
- 标题：v0.1 接手能力实际落地校正
- 状态：reflected
- 说明：RAW-0016 之后需要再次校正，确保 current / handoff / notes 与执行状态一致。
- 来源引用：RAW-0017
- 已反映位置：active-context / handoff / v0.1-scope-check

## CAND-0036
- 标题：接手卡必须支持新会话直接上手
- 状态：reflected
- 说明：handoff-current 必须提供可执行读取顺序、边界提醒与下一步动作。
- 来源引用：RAW-0017
- 已反映位置：handoff
