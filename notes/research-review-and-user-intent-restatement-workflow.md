# Research Review and User Intent Restatement Workflow / 研究复核与用户构想重述流程

### 文件定位

本文件记录 MNEMOSYNE-031 系列 review 的工作协议。它不是执行源，不记录最终 review 结论；最终 review 结论应在用户确认后另行写入 review record。用户构想重述不是原始需求、不是最终设计、不是执行源，也不得直接覆盖 `current/human-approved-spec.md`。

### 关键前提：研究报告主要供元 Agent 使用

- 不假定用户已经通读、掌握并校验全部研究报告。
- 研究报告是 Mnemosyne 元 Agent 的高权重证据层，不是执行源。
- 元 Agent 应主动基于报告进行可行性评价、能力边界确认，并与已有实践和当前业界实践对照。
- 元 Agent 应指出用户构想中过时、低效、过于理想化或过于科幻的部分，而不是把这些构想直接升级为设计规范。
- 元 Agent 应给出更符合当前业界实践、能力边界和工程可落地路线的现代化优化建议。
- 用户接受 summaries、research motivation 和 prompt mapping 作为证据入口，不等于用户亲自验证全部研究结论。

### MNEMOSYNE-031 复核轮次

#### Round 1：research motivation review

复核 research motivation 的准确性、边界与用途。

输出：`MNEMOSYNE-031-R1 Review Result: Research Motivation`

#### Round 2：research prompts / report-topic mapping review

复核 research prompts、缺失 prompt 状态和 report-topic mapping 是否准确表达已知来源与边界。

输出：`MNEMOSYNE-031-R2 Review Result: Research Prompts and Topic Mapping`

#### Round 3：current-report-summaries 与 7 份 summaries review

复核 current-report-summaries 和 7 份 summaries 是否可作为暂用文本证据入口，并明确仍需人工复核的 PDF 图表 / 图片 / 版式证据。

输出：`MNEMOSYNE-031-R3 Review Result: Report Summaries`

#### Round 4A：AI 整理用户设计构想待重述清单

AI 不直接要求用户自由重述，而应按以下优先级整理待重述、待确认和待补充清单：

1. 用户已明确提出过的需求 / 构想；
2. 从已提出内容可合理推断的未澄清点；
3. AI 基于工程经验认为必须确认的设计维度；
4. 可能矛盾、过时、过于理想化或需要研究报告校验的点。

输出：`MNEMOSYNE-031-R4A User Design Intent Restatement Prompt List`

#### Round 4B：用户按清单口语化重述

用户可按清单口语化回答，不要求严格论证，不要求接近最终设计，可以保留不确定性。记录中必须标注这是用户当前重述，可能与最初版本不完全一致。

#### Round 4C：AI 整理用户重述结果

AI 将用户回答整理为以下类别，同时保留来源、疑问和不确定性：

- raw intent points
- explicit user needs
- desired meta-agent behavior
- user assumptions
- possible conflicts
- assumptions to check against research
- likely outdated assumptions
- speculative ideas
- candidate requirements
- open questions
- must remain raw idea

输出：`MNEMOSYNE-031-R4 Review Result: User Design Intent Restatement`

#### Round 5：汇总并等待确认

汇总 R1-R4 结果，清楚区分证据、用户当前重述、候选需求、冲突、open questions 和建议写回位置，然后等待用户明确确认。未经确认，不进入 Codex 写回。

### Codex 写回规则

- 只有用户明确确认后才能写回 review / restatement 结果。
- Codex 可在确认后创建 review record 和 user design restatement record。
- 不得修改研究报告原件、pro prompt 原文、缺失 prompt 或 PDF。
- 不得把用户重述直接写入 `current/human-approved-spec.md`。
- 不得把 review record 或用户重述写成执行源。
- 不得声称 PDF 图表已经复核；实际图表、图片和版式证据仍需人工复核。

### 推荐未来写入位置

- review record：`raw/research-reports/cycles/2026Q2-initial/review-records/MNEMOSYNE-031-research-review-record.md`
- user design restatement：`raw/user-design-restatements/MNEMOSYNE-031-user-design-intent-restatement.md`
