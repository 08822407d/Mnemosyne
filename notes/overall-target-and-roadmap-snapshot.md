# Overall Target and Roadmap Snapshot / 总体目标与路线图快照

## 1. 文件定位

本文件是 Mnemosyne 当前阶段的总体目标与路线图快照。

它用于保存当前 ChatGPT 对话中已经形成、但可能尚未完整落入仓库的整体目标、完整需求、能力边界、后续路线和当前诊断。

本文件不是执行源。

当前执行源仍然是：

- `current/human-approved-spec.md`

如果本文件与 `human-approved-spec` 冲突，应以 `human-approved-spec` 为准，并登记 open question。

## 2. Mnemosyne 的最终目标

Mnemosyne 的最终目标是成为一个“记忆系统元 Agent”工作仓库。

它不是某个具体项目的普通记忆库，而是用于设计、演化和交付多种 AI 工作系统的外部持久记忆系统。

它应支持：

- 为不同项目或场景设计 memory schema；
- 为目标项目生成记忆系统设计说明；
- 为目标项目生成运行文件包和交付清单；
- 维护自身的自我改进流程；
- 接收用户新构想、使用反馈、Codex / ChatGPT 任务结果、研究报告更新和目标项目反馈；
- 将这些输入转为 raw、candidate、similarity/conflict、decision、todo、open question、human-approved-spec 更新；
- 支持跨对话、跨 Codex 任务、跨模型和跨工具的稳定交接；
- 基于研究报告证据约束平台能力判断和自动化边界；
- 在未来逐步引入模板、适配层和轻量自动化，但不在未验证前承诺全自动能力。

## 3. 核心架构原则

当前已经形成的核心架构原则包括：

1. 模型负责计算，文件负责记忆。
2. 模型是可替换计算单元，不是长期真相源。
3. GitHub / Git / Markdown 文件是当前长期状态和审计基础。
4. 当前执行源是 `current/human-approved-spec.md`。
5. raw、research reports、candidate、decision-log、active-context、handoff、startup-instructions 都不是执行源。
6. 研究报告是高权重证据层，用于约束能力边界判断，但不能直接覆盖执行源。
7. 新输入必须先进入 raw / candidate / review 流程，用户确认后才可更新 human-approved-spec。
8. 不默认全量读取 raw。
9. 不默认自动写回。
10. 不默认创建 AGENTS.md、CLAUDE.md、GitHub Actions、MCP、RAG 或自动化流程。

## 4. 当前已完成能力

截至本快照，Mnemosyne 已经基本具备：

### 4.1 v0.1 接手能力

- 新 ChatGPT 对话可以按 startup-instructions 接手。
- 新 Codex Cloud 任务可以按 startup-instructions 接手。
- current/human-approved-spec.md 已作为执行源。
- active-context 和 handoff-current 提供当前工作状态和交接卡。
- startup-instructions 提供新任务读取顺序。
- startup-rehearsal-report 记录接手演练已通过。
- v0.1 独立验证结果为 PASS_WITH_WARNINGS，但不阻断进入 v0.2。

### 4.2 研究证据层

- 7 份研究报告已作为 RC-2026Q2-initial 入库。
- research-report-index 已建立 report_id 到原件路径的映射。
- current-evidence-map 已建立当前研究证据派生视图。
- current-capability-boundaries 已建立当前能力边界派生视图。
- 研究报告具有时效性，未来应通过新 research cycle 和 delta report 更新。
- PDF 图表和图片仍需人工复核。
- MNEMOSYNE-030 / MNEMOSYNE-030A 已建立研究报告 summary 层、current-report-summaries 派生视图和 PDF 图表复核索引；这些文件不是执行源。

### 4.3 v0.2 第一方向已开始

v0.2 第一方向已经选择为：

- self-improvement workflow

当前已经创建：

- `notes/self-improvement-workflow.md`
- `notes/self-improvement-template-pack.md`

self-improvement workflow 已从流程说明推进到基础模板包。`notes/self-improvement-workflow.md` 用于描述用户新构想、使用反馈、Codex/ChatGPT 任务结果和研究更新如何进入 Mnemosyne 的自我改进流程；`notes/self-improvement-template-pack.md` 是模板入口，但不是执行源。

### 4.4 目标项目模板包已创建

当前已经创建：

- `notes/target-project-memory-system-template-pack.md`

该模板包用于 Mnemosyne 为目标项目设计外部持久记忆系统，覆盖 Target Project Intake、Target Project Type Classifier、Memory System Design Spec、目标项目文件结构、执行源规则、workflow、delivery package draft、handoff、unsupported assumptions、drift review、minimal runbook 和 completion criteria。该文件不是执行源，仍需用户 review。

### 4.5 delivery manifest 与 review / scenario selection 已创建

当前已经创建：

- `notes/delivery-manifest-template-pack.md`
- `notes/template-pack-review-and-first-scenario-selection.md`

`notes/delivery-manifest-template-pack.md` 用于目标项目交付清单、目标项目运行真相源、人工设置、交付 review、handoff、回滚和结果记录。`notes/template-pack-review-and-first-scenario-selection.md` 用于 review 三类模板包，并帮助用户准备首个目标项目场景选择。两者都不是执行源，仍需用户 review。

## 5. 当前最新诊断

当前 ChatGPT 对仓库的最新诊断包括：

1. `notes/self-improvement-workflow.md` 主体已经创建。
2. `notes/self-improvement-template-pack.md` 已创建，作为 self-improvement workflow 的模板入口。
3. v0.2 第一方向 self-improvement workflow 已从流程说明推进到基础模板包。
4. `notes/target-project-memory-system-template-pack.md` 已创建，作为目标项目 intake / memory system design spec 模板入口。
5. 目标项目 intake / memory system design spec 模板包已创建，等待用户 review。
6. delivery manifest template pack 已创建，等待用户 review。
7. `notes/template-pack-review-and-first-scenario-selection.md` 已创建，用于三类模板包 review 与首个目标项目场景选择准备。
8. Codex Task Result Record 默认占位符路径统一为 `notes/codex-task-results/TASK_ID-result.md`。
9. 实际任务应将 `TASK_ID` 替换为真实任务编号，例如 `notes/codex-task-results/MNEMOSYNE-027-result.md`。
10. template pack 不是执行源，仍需用户 review。
11. 每个后续重要 Codex 任务都应要求写入 Codex Task Result Record。
12. Codex Task Result Record 不是执行源，只是审计材料。
13. 最终判断仍以仓库文件、Git diff、用户 review 和必要验证为准。

## 6. self-improvement workflow 的目标

self-improvement workflow 是 v0.2 的第一核心能力。

它应解决：

- 用户提出的新构想如何进入仓库；
- 用户反馈某个设计不好用时如何处理；
- Codex 任务完成后的总结和警告如何保存；
- ChatGPT 对话阶段性结论如何保存；
- 研究报告 refresh 后如何影响设计；
- 目标项目使用反馈如何反馈到 Mnemosyne；
- 新想法和旧想法重复或冲突时如何处理；
- 哪些内容只进入 TODO；
- 哪些内容需要 open question；
- 哪些内容可以形成 candidate；
- 哪些内容经用户确认后可以更新 human-approved-spec；
- 何时更新 active-context 和 handoff；
- 何时需要回查 research evidence；
- 何时不能自动升级为执行源。

## 7. self-improvement workflow 的基础流程

自我改进流程应保持半自动：

1. Capture / 保存输入

   - 用户新构想；
   - 使用反馈；
   - Codex Task Result Record；
   - ChatGPT 阶段总结；
   - research refresh；
   - 目标项目反馈；
   - 失败案例或冲突案例。
2. Classify / 分类

   - 新需求；
   - 设计反馈；
   - 工具能力边界；
   - 证据更新；
   - 错误修复；
   - 文档格式问题；
   - 模板需求；
   - 自动化候选；
   - open question；
   - future idea。
3. Extract / 抽取 candidate

   - 将输入整理为 Candidate Requirement。
   - Candidate 不是执行源。
4. Compare / 查重和冲突检查

   - 与 human-approved-spec；
   - candidate-requirements；
   - decision-log；
   - open-questions；
   - todo；
   - research evidence；
   - relevant raw 进行对比。
5. Decide / 用户确认

   - reflected；
   - accepted；
   - rejected；
   - deferred；
   - keep_candidate；
   - ask_followup。
6. Apply / 应用

   - 更新 human-approved-spec；
   - 或更新 todo；
   - 或更新 open-questions；
   - 或更新 decision-log；
   - 或更新 active-context / handoff；
   - 或仅保存 raw / candidate。
7. Record / 记录任务结果

   - Codex Task Result Record；
   - ChatGPT 阶段总结；
   - follow-up task；
   - known gaps。

## 7.1 模板入口

self-improvement workflow 的模板入口为：

- `notes/self-improvement-template-pack.md`

执行实际自我改进时，应优先使用该模板包。模板包不是执行源；当前执行源仍是 `current/human-approved-spec.md`。

## 8. Codex Task Result Record 规则

从当前阶段开始，每个 Codex 任务都应要求写入任务结果记录。

默认路径：

- `notes/codex-task-results/TASK_ID-result.md`

该记录不是执行源。

它应包含：

- task_id；
- task_name；
- files_created；
- files_modified；
- files_not_modified；
- codex_summary；
- known_gaps；
- manual_review_required；
- follow_up_tasks；
- limits_or_uncertainties；
- whether_task_claims_completion；
- whether_user_or_follow_up_verification_needed。

如果任务本身已经生成专门报告，例如 independent verification report，可以将结果写入该报告，不必重复创建额外结果文件。

## 9. 目标项目记忆系统设计能力

Mnemosyne 的后续重要能力之一，是为具体目标项目设计记忆系统。

目标项目可能包括：

- 软件开发 Agent 项目；
- 多 Agent 团队；
- 长期研究项目；
- 语言学习项目；
- 源码学习项目；
- 普通长期对话 / 个人知识管理项目。

当前已经建立基础模板：

- target project intake template；
- memory system design spec template；
- target project type classifier；
- target project memory file layout template；
- target project execution source rule template；
- unsupported assumptions template；
- drift review template；
- target project handoff template。

后续仍需深化：

- delivery manifest template；
- target project memory package template；
- post-delivery feedback workflow；
- 第一个目标项目场景验证。

交付原则：

- Mnemosyne 仓库是设计工厂和设计档案；
- 目标项目仓库或目录是运行真相源；
- 交付前 Mnemosyne 设计为主；
- 交付后目标项目运行文件为主；
- 目标项目反馈应回到 Mnemosyne 的 self-improvement workflow。

## 10. 研究证据与时效性

研究报告应按 research cycle 管理。

当前轮次：

- `RC-2026Q2-initial`

未来可能有：

- quarterly refresh；
- ad-hoc research cycle；
- delta report；
- deprecated evidence；
- current evidence map 更新；
- current capability boundaries 更新。

新机制设计前应读取：

- `raw/research-reports/current/research-report-index.md`
- `raw/research-reports/current/current-evidence-map.md`
- `raw/research-reports/current/current-capability-boundaries.md`

特别是在涉及以下内容时：

- ChatGPT / Claude / Codex / Claude Code / Cursor / GitHub 等平台能力；
- 自动化可行性；
- MCP / RAG；
- GitHub Actions；
- 平台适配层；
- 目标项目 memory schema；
- 模型迁移；
- 长上下文是否能替代外部记忆。

## 11. 后续阶段建议

MNEMOSYNE-031 final checkpoint 已完成。旧路线中“先 review report summaries”的状态已经被 MNEMOSYNE-031 R1-R3/R4/R5 checkpoint 覆盖：report summaries 已被用户接受为暂用文本证据入口，但 PDF 图表 / 图片 / 版式仍待人工复核。

当前建议路线由用户选择：

1. PDF figure/table/image review decision；
2. first dry-run using Mnemosyne itself or a small target scenario；
3. Idea Capture Buffer / candidate requirements cleanup；
4. template pack review / small fixes as needed。

如果后续设计依赖 PDF visual/table evidence，应先执行相关 PDF 图表 / 图片人工复核并更新 `pdf-figure-review-index.md`。
如果目标是验证 MNEMOSYNE-031 新确认的记忆层原则，优先考虑小型 Mnemosyne self-validation dry-run。

### MNEMOSYNE-025C 或后续清理任务

目标：

- 清理 self-improvement-workflow.md 的 Markdown 格式；
- 修正 Codex Task Result Record 默认路径；
- 补齐 candidate / decision 中 self-improvement 相关状态；
- 保持不引入新机制。

### MNEMOSYNE-026：self-improvement workflow 模板设计（已完成 / 等待用户 review）

目标：

- 设计 raw input template；
- 设计 candidate extraction template；
- 设计 similarity/conflict check template；
- 设计 user decision record template；
- 设计 Codex Task Result Record template；
- 设计 ChatGPT handoff / feedback template；
- 设计 open question / todo update template；
- 创建 `notes/self-improvement-template-pack.md`。

### MNEMOSYNE-027：目标项目 intake 与 memory system design spec 模板（已完成 / 等待用户 review）

目标：

- 设计目标项目需求采集模板；
- 设计 memory system design spec 模板；
- 支持不同项目类型；
- 创建 `notes/target-project-memory-system-template-pack.md`。

### MNEMOSYNE-028：delivery manifest 与目标项目交付包模板（已完成 / 等待用户 review）

目标：

- 深化 delivery manifest；
- 设计 target project memory package；
- 衔接已创建的 unsupported assumptions 与 drift review 模板。

### 后续任务：Idea Capture Buffer

目标：

- 支持用户快速记录临时想法；
- 不直接进入执行源；
- 后续通过 self-improvement workflow 处理。

### 后续任务：研究报告 summary / PDF 图表复核

目标：

- 用户 review 已建立的 7 份 report summaries；
- 对相关 PDF 图表 / 图片进行人工复核；
- 根据人工复核结果更新 `pdf-figure-review-index.md`；
- 为 Evidence Item / delta report 打基础。

### 后续 v0.2 / v0.3 方向

- AGENTS.md；
- CLAUDE.md；
- GitHub Actions 文档检查；
- 自动查重；
- similarity index；
- 自动索引；
- MCP / RAG；
- 多 Agent 自动协调；
- 自动 drift review；
- 模型迁移辅助。

## 12. 当前不应做的事

当前不应直接进入：

- 自动查重；
- 自动写回；
- GitHub Actions；
- AGENTS.md；
- CLAUDE.md；
- MCP；
- RAG；
- 多 Agent 自动协调；
- 目标项目正式交付。

在进入这些方向前，应先让 self-improvement workflow 稳定，并建立必要模板。

## 13. 验证原则

每个阶段完成后，应尽量验证：

- 文件是否真实修改；
- 状态是否一致；
- TODO 是否落账；
- candidate / decision 是否补齐；
- 是否误把非执行源写成执行源；
- 是否需要新 open question；
- 是否需要 Codex Task Result Record；
- 是否需要独立验证或接手演练。

Codex 的完成总结不能作为最终依据。
最终依据应是：

- Git diff；
- 仓库文件；
- 用户 review；
- 必要的独立验证报告。

## 14. 本快照的使用方式

未来新 ChatGPT 对话或新 Codex 任务，如果对 Mnemosyne 的长期目标、当前路线或后续任务不清楚，可以按需读取本文件。

本文件用于防止长期规划只保存在某一次对话上下文中。

本文件不是执行源。
如与 `current/human-approved-spec.md` 冲突，以 `human-approved-spec` 为准。

## MNEMOSYNE-030C 更新：研究动机入库

- `RC-2026Q2-initial` 的研究动机已保存到 `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`。
- 该 motivation 文件用于解释 7 份研究报告为什么存在、服务什么设计问题、如何约束 Mnemosyne，以及为什么研究报告是高权重证据层但不是执行源。
- 当前执行源仍是 `current/human-approved-spec.md`；motivation、研究报告、summary、candidate、decision、active-context、handoff 和 task result records 都不是执行源。
- 当前路线保留：用户 review research motivation / report summaries、PDF 图表复核、首个目标项目 dry-run、Idea Capture Buffer、AGENTS.md / CLAUDE.md、自动化增强。
- 后续研究 refresh 应创建新 cycle 和 delta report，不覆盖 `RC-2026Q2-initial` 的历史研究动机。

## MNEMOSYNE-031A 更新：研究复核与用户构想重述

> Supersession note: this section records the earlier MNEMOSYNE-031A state before the final R4B/R4C/R5 checkpoint. For current continuation, use `raw/research-reports/cycles/2026Q2-initial/review-records/MNEMOSYNE-031-research-review-record.md` and the `MNEMOSYNE-031 final checkpoint roadmap update` section below.

- MNEMOSYNE-031 review 不假定用户已通读、掌握或验证全部研究报告；研究报告主要供元 Agent 作为高权重证据层使用。
- 元 Agent 应基于研究证据进行可行性评价、能力边界确认、已有实践对照和现代化优化建议，并标记过时、低效、过于理想化或过于科幻的构想。
- MNEMOSYNE-031 扩展为 R1-R3 研究材料复核与 R4A-R4C 用户设计构想重述，之后汇总并等待用户确认。
- 用户重述是 raw user intent evidence，不是原始需求、最终设计或执行源，不得直接写入 `current/human-approved-spec.md`。
- 后续路线为：普通 ChatGPT 完成 R1-R4；用户确认后再写入 review / restatement records；之后决定 PDF 图表复核、首个 dry-run 或 Idea Capture Buffer。
- 本次更新只同步规划 / 建设基线，不表示 MNEMOSYNE-031 review 已完成。

## MNEMOSYNE-031 final checkpoint roadmap update

Near-term route options:

1. Repository checkpoint of MNEMOSYNE-031 records.
2. PDF figure/table/image review decision.
3. First dry-run using Mnemosyne itself or a small target scenario.
4. Idea Capture Buffer / candidate requirements cleanup.
5. Small fixes to tracking files if consistency issues are found.

Medium-term candidate roadmap:

- execution-source promotion workflow;
- layered memory architecture;
- public/private workspace layout;
- index/summary minimal schema;
- capability versioning;
- memory-system feedback/testing/debugging research;
- first reusable target-project memory template.
