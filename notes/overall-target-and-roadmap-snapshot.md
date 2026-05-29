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

### 4.3 v0.2 第一方向已开始

v0.2 第一方向已经选择为：

- self-improvement workflow

当前已经创建：

- notes/self-improvement-workflow.md

该文件用于描述用户新构想、使用反馈、Codex/ChatGPT 任务结果和研究更新如何进入 Mnemosyne 的自我改进流程。

## 5. 当前最新诊断

当前 ChatGPT 对仓库的最新诊断包括：

1. `notes/self-improvement-workflow.md` 主体已经创建。
2. 该文件仍可能接近单行 Markdown，需要格式清理。
3. 该文件中 Codex Task Result Record 默认路径曾存在缺失 TASK_ID 的错误写法。
4. 默认占位符路径应为 `notes/codex-task-results/TASK_ID-result.md`，实际任务应替换 TASK_ID。
5. `notes/candidate-requirements.md` 中可能仍有 self-improvement 相关孤立条目或 pending 状态需要清理。
6. 在进入模板设计前，应先完成 self-improvement workflow 清理。
7. 每个后续 Codex 任务都应要求写入 Codex Task Result Record。
8. Codex Task Result Record 不是执行源，只是审计材料。
9. 最终判断仍以仓库文件、Git diff、用户 review 和必要验证为准。
10. 后续 Codex 任务是否需要新开，应按“是否必须在全新 Codex 任务中执行”判断，而不是按“新开更好”判断。
11. 后续任务内容应优先以 txt 文件提供，避免聊天代码块嵌套导致复制不完整。
12. `notes/system-construction-baseline.md` 是当前更明确的系统建设基线快照，同样不是执行源。

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

未来需要建立：

- target project intake template；
- memory system design spec template；
- delivery manifest template；
- target project memory package template；
- unsupported assumptions template；
- drift review template；
- post-delivery feedback workflow。

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

建议后续路线按以下顺序推进：

### 当前下一步：格式清理或 MNEMOSYNE-026

目标：

- 如仍需要，继续进行 self-improvement workflow Markdown 格式清理；
- 或进入 MNEMOSYNE-026：self-improvement workflow 模板设计。

### MNEMOSYNE-026：self-improvement workflow 模板设计

目标：

- 设计 raw input template；
- 设计 candidate extraction template；
- 设计 similarity/conflict check template；
- 设计 user decision record template；
- 设计 Codex Task Result Record template；
- 设计 ChatGPT handoff / feedback template；
- 设计 open question / todo update template。

### MNEMOSYNE-027：目标项目 intake 与 memory system design spec 模板

目标：

- 设计目标项目需求采集模板；
- 设计 memory system design spec 模板；
- 支持不同项目类型。

### MNEMOSYNE-028：delivery manifest 与目标项目交付包模板

目标：

- 设计 delivery manifest；
- 设计 target project memory package；
- 设计 unsupported assumptions；
- 设计 drift review。

### MNEMOSYNE-029：Idea Capture Buffer

目标：

- 支持用户快速记录临时想法；
- 不直接进入执行源；
- 后续通过 self-improvement workflow 处理。

### MNEMOSYNE-030：研究报告 summary / PDF 图表复核

目标：

- 为每份报告建立 summary；
- 对 PDF 图表进行人工复核；
- 必要时转换为 Markdown / TXT；
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
