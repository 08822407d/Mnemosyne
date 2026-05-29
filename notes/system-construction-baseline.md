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
- raw、research reports、candidate、decision-log、active-context、handoff、startup-instructions、system-construction-baseline 都不是执行源；
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
- v0.2 第一方向已确定为 self-improvement workflow；
- `notes/self-improvement-workflow.md` 已创建；
- `notes/self-improvement-template-pack.md` 已创建，self-improvement workflow 已具备基础模板包；
- `notes/target-project-memory-system-template-pack.md` 已创建，目标项目 intake / memory system design spec 已具备基础模板包；
- `notes/delivery-manifest-template-pack.md` 已创建，delivery manifest / 目标项目交付包已具备基础模板包。

## 4. 当前已知问题和最新诊断

当前已知问题和最新诊断包括：

- `notes/self-improvement-workflow.md` 仍可能需要 Markdown 格式清理；
- `notes/self-improvement-workflow.md` 默认占位符路径应统一为 `notes/codex-task-results/TASK_ID-result.md`，实际任务应将 `TASK_ID` 替换为真实任务编号；
- 相关说明文件中的 Codex Task Result Record 默认路径应统一为 `notes/codex-task-results/TASK_ID-result.md`；
- `notes/candidate-requirements.md` 中 self-improvement 相关候选需求状态可能需要校正；
- self-improvement workflow 模板设计已在 MNEMOSYNE-026 完成后进入用户 review 阶段；
- 目标项目 intake / memory system design spec 模板设计已在 MNEMOSYNE-027 完成后进入用户 review / 小修阶段；
- delivery manifest 深化已在 MNEMOSYNE-028 完成后进入用户 review / 小修阶段；
- MNEMOSYNE-028A 已完成 delivery manifest template pack 状态同步与结果记录补账；
- 下一步应在第一个目标项目场景选择与 Idea Capture Buffer 之间确认优先级。

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

## 5.3 delivery manifest template pack

当前模板入口：

- `notes/delivery-manifest-template-pack.md`

该模板包用于为目标项目交付记忆系统运行文件提供交付清单、文件创建 / 更新清单、运行真相源检查、手工落地步骤、unsupported assumptions linkage、delivery review、handoff package、rollback / revision plan、delivery result record 和 minimal delivery runbook。该模板包不是执行源，执行源仍为 `current/human-approved-spec.md`。真实目标项目交付必须经用户确认并落地到目标项目仓库 / 目录。

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
- 研究证据具有时效性，未来通过新 research cycle 和 delta report 更新；
- 涉及工具能力、平台适配、自动化、目标项目设计、模型迁移、MCP/RAG/GitHub Actions 等时，必须读取：
  - `raw/research-reports/current/research-report-index.md`
  - `raw/research-reports/current/current-evidence-map.md`
  - `raw/research-reports/current/current-capability-boundaries.md`

## 8. 后续路线

建议后续路线：

1. self-improvement workflow 清理；
2. self-improvement workflow 模板设计（已完成，下一步为 template pack review / 小修）；
3. 目标项目 intake 与 memory system design spec 模板（已完成，下一步为目标项目模板包 review / 小修）；
4. delivery manifest 深化（已完成，下一步为 delivery manifest template pack review / 小修）；
5. 第一个目标项目场景选择或 Idea Capture Buffer；
6. 研究报告 summary / PDF 图表复核；
7. AGENTS.md / CLAUDE.md；
8. GitHub Actions / 自动查重 / similarity index / MCP / RAG 等后续增强。

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
