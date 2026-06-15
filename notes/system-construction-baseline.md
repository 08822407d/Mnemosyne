# System Construction Baseline / 系统建设基线

## 文件定位

本文件用于暂存截至当前已经基本确定的系统建设目标、能力边界、工作约定、后续路线和当前诊断。

本文件不是执行源。

当前执行源仍是：

- `current/human-approved-spec.md`

如果本文件与 `human-approved-spec` 冲突，应以 `human-approved-spec` 为准，并登记 open question。

## 1. 最终目标

Mnemosyne 的最终目标是成为“记忆系统元 Agent”工作仓库，用于设计、演化和交付外部持久记忆系统。

它应服务于：

- 长期 AI 工作；
- AI Agent 项目；
- 多 Agent 团队；
- 长期研究；
- 学习系统；
- 源码学习；
- 个人长期对话 / 知识管理；
- 未来目标项目的记忆系统交付。

它不是某个具体项目的普通记忆库。

## 2. 当前核心架构原则

当前核心架构原则包括：

- 模型负责计算，文件负责记忆；
- 模型是可替换计算单元，不是长期真相源；
- GitHub / Git / Markdown 是当前长期状态和审计基础；
- `current/human-approved-spec.md` 是执行源；
- raw、research reports、candidate、decision-log、active-context、handoff、startup-instructions、system-construction-baseline、template pack 和 review / scenario selection 文件都不是执行源；
- 新输入必须先进入 raw / candidate / review 流程，用户确认后才可更新执行源；
- 不默认全量读取 raw；
- 不默认自动写回；
- 不默认创建 AGENTS.md、CLAUDE.md、GitHub Actions、MCP、RAG 或自动化流程。

## 3. 当前已完成能力

截至本基线，已经完成或基本具备：

- v0.1 接手能力；
- `handoff/startup-instructions.md` 已创建；
- 新 ChatGPT / 新 Codex 接手演练已完成；
- v0.1 独立验证结论为 `PASS_WITH_WARNINGS`；
- v0.1 已被接受为可接手版本；
- 7 份研究报告已作为 `RC-2026Q2-initial` 研究证据层入库；
- `raw/research-reports/current/research-report-index.md` 已建立；
- `raw/research-reports/current/current-evidence-map.md` 已建立；
- `raw/research-reports/current/current-capability-boundaries.md` 已建立；
- `raw/research-reports/cycles/2026Q2-initial/report-summaries/` 已建立 7 份 report summaries；
- `raw/research-reports/current/current-report-summaries.md` 已建立；
- `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md` 已建立，PDF 图表 / 图片仍待人工复核；
- v0.2 第一方向已确定为 self-improvement workflow；
- `notes/self-improvement-workflow.md` 已创建；
- `notes/self-improvement-template-pack.md` 已创建，self-improvement workflow 已具备基础模板包；
- `notes/target-project-memory-system-template-pack.md` 已创建，目标项目 intake / memory system design spec 已具备基础模板包；
- `notes/delivery-manifest-template-pack.md` 已创建，delivery manifest / 目标项目交付包模板已具备基础版本；
- `notes/template-pack-review-and-first-scenario-selection.md` 已创建，三类模板包 review 清单与首个目标项目场景候选矩阵已具备基础版本。

## 4. 当前已知问题和最新诊断

当前已知问题和最新诊断包括：

- `notes/self-improvement-workflow.md` 仍可能需要 Markdown 格式清理；
- `notes/self-improvement-workflow.md` 默认占位符路径应统一为 `notes/codex-task-results/TASK_ID-result.md`，实际任务应将 `TASK_ID` 替换为真实任务编号；
- 相关说明文件中的 Codex Task Result Record 默认路径应统一为 `notes/codex-task-results/TASK_ID-result.md`；
- `notes/candidate-requirements.md` 中 self-improvement 相关候选需求状态可能需要校正；
- self-improvement workflow 模板设计已在 MNEMOSYNE-026 完成后进入用户 review 阶段；
- 目标项目 intake / memory system design spec 模板设计已在 MNEMOSYNE-027 完成后进入用户 review / 小修阶段；
- delivery manifest template pack 已在 MNEMOSYNE-028 完成后进入用户 review / 小修阶段；
- MNEMOSYNE-029 已创建三类模板包 review 清单与首个目标项目场景候选矩阵；
- MNEMOSYNE-030 / MNEMOSYNE-030A 已建立 report summaries、current-report-summaries 和 pdf-figure-review-index；
- 下一步应由用户 review report summaries，人工复核相关 PDF 图表 / 图片，并选择第一个目标项目场景或决定先做 Idea Capture Buffer / 小修模板。

## 5. self-improvement workflow 的目标

self-improvement workflow 要解决：

- 用户新构想如何进入仓库；
- 用户使用体验反馈如何处理；
- Codex 任务结果如何记录；
- ChatGPT 阶段总结如何保存；
- 研究报告 refresh 如何影响设计；
- 目标项目反馈如何回流；
- 新旧想法重复、冲突、细化、替换时如何处理；
- 哪些内容只进入 TODO；
- 哪些内容需要 open question；
- 哪些内容可以成为 candidate；
- 哪些内容经用户确认后更新 human-approved-spec；
- 何时更新 active-context 和 handoff；
- 何时回查 research evidence；
- 何时不能自动升级为执行源。

## 5.1 self-improvement template pack

当前模板入口：

- `notes/self-improvement-template-pack.md`

该模板包不是执行源。执行源仍为 `current/human-approved-spec.md`。模板填写结果需要经过用户确认后，才可能更新执行源。

## 5.2 target project memory system template pack

当前模板入口：

- `notes/target-project-memory-system-template-pack.md`

该模板包用于为目标项目设计外部持久记忆系统，覆盖 intake、目标项目分类、memory system design spec、文件结构、执行源规则、workflow、delivery package draft、handoff、unsupported assumptions、drift review、minimal runbook 和 completion criteria。该模板包不是执行源，执行源仍为 `current/human-approved-spec.md`。真实目标项目设计和交付仍需用户 review 与目标项目落地确认。

## 6. Codex 任务执行约定

后续 Codex 任务执行约定如下：

- 后续任务说明必须带任务编号；
- 后续任务开头必须写明是否“必须新开 Codex Cloud 任务”；
- 判断标准是“是否必须在一个全新的 Codex 任务中开展”，不是“新开更好”；
- 如果现有任务干净、基于最新 master、没有未合并改动，可以继续使用；
- 如果任务目标是验证新任务能否接手、现有任务状态不明、已有未合并改动、分支不是最新，或需要隔离上下文，则必须新开；
- 后续 Codex 任务内容应优先作为 `.txt` 文件提供，避免聊天代码块嵌套导致复制不完整；
- 任务完成后必须写入 Codex Task Result Record：`notes/codex-task-results/TASK_ID-result.md`；
- Codex Task Result Record 不是执行源；
- 最终判断仍以 Git diff、仓库文件、用户 review 和必要验证为准。

## 7. 研究证据与能力边界

研究证据与能力边界约定如下：

- 当前研究轮次为 `RC-2026Q2-initial`；
- 7 份研究报告是高权重证据层；
- 研究报告不是执行源；
- PDF 图表和图片仍需人工复核；
- 后续目标项目 dry-run 若依赖 PDF 图表 / 图片证据，应先完成相关人工复核并更新 `pdf-figure-review-index.md`；
- 研究证据具有时效性，未来通过新 research cycle 和 delta report 更新；
- 涉及工具能力、平台适配、自动化、目标项目设计、模型迁移、MCP/RAG/GitHub Actions 等时，必须读取：
  - `raw/research-reports/current/research-report-index.md`
  - `raw/research-reports/current/current-evidence-map.md`
  - `raw/research-reports/current/current-capability-boundaries.md`

## 8. 后续路线

建议后续路线：

1. 用户 review report summaries；
2. 人工复核相关 PDF 图表 / 图片；
3. 选择第一个目标项目场景；
4. 第一轮 dry-run intake；
5. Idea Capture Buffer；
6. AGENTS.md / CLAUDE.md；
7. 自动化增强。

## 9. 当前不应直接做的事

当前不应直接：

- 进入自动查重；
- 进入自动写回；
- 创建 AGENTS.md；
- 创建 CLAUDE.md；
- 创建 GitHub Actions；
- 上 MCP / RAG；
- 做目标项目正式交付；
- 把 self-improvement workflow 的未清理草案当成完全稳定规范；
- 把目标项目模板包当成执行源；
- 在用户确认第一个目标项目场景前生成真实目标项目交付包。

## 10. 使用方式

未来新 ChatGPT 对话或新 Codex 任务，如果担心当前对话上下文丢失，可以读取本文件理解总体建设路线。

本文件用于保持路线不跑偏。

本文件不是执行源。

与 human-approved-spec 冲突时，以 human-approved-spec 为准。

## MNEMOSYNE-030C 更新：研究动机入库

- `RC-2026Q2-initial` 的研究动机已保存到 `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`。
- 该 motivation 文件用于解释 7 份研究报告为什么存在、服务什么设计问题、如何约束 Mnemosyne，以及为什么研究报告是高权重证据层但不是执行源。
- 当前执行源仍是 `current/human-approved-spec.md`；motivation、研究报告、summary、candidate、decision、active-context、handoff 和 task result records 都不是执行源。
- 当前路线保留：用户 review research motivation / report summaries、PDF 图表复核、首个目标项目 dry-run、Idea Capture Buffer、AGENTS.md / CLAUDE.md、自动化增强。
- 后续研究 refresh 应创建新 cycle 和 delta report，不覆盖 `RC-2026Q2-initial` 的历史研究动机。

## MNEMOSYNE-031A 更新：研究复核与用户构想重述

- MNEMOSYNE-031 review 不假定用户已通读、掌握或验证全部研究报告；研究报告主要供元 Agent 作为高权重证据层使用。
- 元 Agent 应基于研究证据进行可行性评价、能力边界确认、已有实践对照和现代化优化建议，并标记过时、低效、过于理想化或过于科幻的构想。
- MNEMOSYNE-031 扩展为 R1-R3 研究材料复核与 R4A-R4C 用户设计构想重述，之后汇总并等待用户确认。
- 用户重述是 raw user intent evidence，不是原始需求、最终设计或执行源，不得直接写入 `current/human-approved-spec.md`。
- 后续路线为：普通 ChatGPT 完成 R1-R4；用户确认后再写入 review / restatement records；之后决定 PDF 图表复核、首个 dry-run 或 Idea Capture Buffer。
- 本次更新只同步规划 / 建设基线，不表示 MNEMOSYNE-031 review 已完成。

## MNEMOSYNE-031 final checkpoint non-execution principles

- Mnemosyne is a persistent-memory-system meta-agent.
- Model computes; external state remembers.
- Original-source materials must be preserved as durable source layer.
- Evidence layers and execution source must remain separate.
- Handoff is task-local continuation context, not global project law.
- Ordinary project Agents may maintain authorized memory content but cannot redesign public memory-system rules.
- Memory-system testing/debugging is an important research-gated candidate capability.
