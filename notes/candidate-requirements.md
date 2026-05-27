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
