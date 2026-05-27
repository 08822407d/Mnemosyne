# Human-Approved Spec（v0.1 当前执行源）

本文档是 Mnemosyne 当前唯一执行源（source of execution）。

## 1. Mnemosyne 的定位

- Mnemosyne 是记忆系统元 Agent 工作仓库。
- 用于为其他项目、长期研究、学习系统、开发 Agent、多 Agent 团队等设计外部持久记忆系统。
- 不是某个具体项目的普通记忆库。

## 2. 外部记忆架构

- 模型负责计算，文件负责记忆。
- 模型是可替换计算单元，不是长期真相源。
- 外部文件 / Git 仓库是长期记忆和审计基础。
- 模型内部 memory 只作为缓存或辅助上下文。

## 3. 语言策略

- 当前阶段中文为主要工作语言。
- 文件名、目录名、ID、状态值、YAML key、命令、Git/GitHub 术语、工具名和产品名可以使用英文。

## 4. 执行源原则

- `current/human-approved-spec.md` 是当前执行源。
- Raw Record 不是执行源。
- Research Reports 不是执行源。
- Candidate Requirement 不是执行源。
- Similarity / Conflict Report 不是执行源。
- Decision Record 不是执行源。
- Active Context 不是执行源。
- Handoff 不是执行源。
- 如果其他文件与 `human-approved-spec` 冲突，应以 `human-approved-spec` 为准，并登记 open question。

## 5. 研究证据层原则

- 7 份研究报告已经作为 `RC-2026Q2-initial` 轮次证据入库。
- 研究报告是高权重证据层，用于约束能力边界判断、平台适配和新机制设计。
- `current-evidence-map` 和 `current-capability-boundaries` 是当前研究证据派生视图。
- PDF 报告中的图表和图片需要人工复核。
- 研究证据具有时效性，未来通过新 research cycle 和 delta report 更新。
- 研究报告不能直接覆盖执行源。

## 6. 需求进入原则

- 新输入先保存为 Raw Record。
- 再抽取 Candidate Requirement。
- 进入实施版前需要查重、对比和用户确认。
- 用户确认后才可更新 Human-Approved Spec。

## 7. handoff / active-context 原则

- active-context 是当前工作集，不是执行源。
- handoff-current 是跨会话交接卡，不是完整历史，也不是执行源。
- 新会话应优先读取 human-approved-spec、active-context 和 handoff-current。
- raw 和 research reports 按需回查，不默认全量读取。

## 8. 模型迁移原则

- 默认继承 Canonical Memory。
- raw 是最高证据源，但不默认全量重读。
- 高风险、高价值、低置信度内容按需回查 raw。
- 旧模型专用约束需要复审。
- 新模型能力需要验证后再启用。

## 9. 交付包原则

- Mnemosyne 仓库是设计工厂和设计档案。
- 目标项目仓库或目录是目标项目运行真相源。
- 交付包应包含设计说明、运行文件包、Delivery Manifest、Handoff Package、Unsupported Assumptions 和 Drift Review TODO。
- 不同目标项目需要不同 memory schema。

## 10. 当前 v0.1 边界

- 当前是半自动设计仓库。
- Codex Cloud 当前主要作为远程 GitHub 文件写入和版本保存助手。
- v0.1 不包含自动查重、自动索引、自动 ID、自动 schema 校验、自动写回、自动交付、自动 drift 检查、自动模型迁移、GitHub Actions、AGENTS.md、CLAUDE.md、MCP、RAG、多 Agent 自动协调。
- 这些属于 v0.2 或 future。
