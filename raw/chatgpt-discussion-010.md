---
raw_id: RAW-0010
source_type: user_and_chatgpt_handoff
status: preserved
sensitivity: private
language: zh-CN
---

# RAW-0010：Mnemosyne v0.1 收束与一致性检查

这不是完整原始对话，而是从早期 ChatGPT 讨论中整理出的第十阶段交接记录，用于收束 Mnemosyne v0.1。

## 1. 为什么需要 v0.1 收束

Mnemosyne 已经经过多个阶段，逐步建立了：

- 最小仓库结构；
- 当前操作约定；
- 第一批核心业务需求；
- 核心对象模型；
- 对象模板与 ID / 状态规则；
- 需求进入流程；
- handoff / active-context / 阶段性回顾机制；
- 模型迁移与约束生命周期；
- 面向目标项目的交付包结构。

现在需要做一次收束，避免仓库内容继续扩散而没有明确的 v0.1 边界。

v0.1 的目标不是完成全部自动化，而是让 Mnemosyne 具备一个可读、可审查、可继续迭代的最小设计工作仓库。

## 2. v0.1 应包含的内容

Mnemosyne v0.1 应至少包含：

1. 清晰定位
   Mnemosyne 是“记忆系统元 Agent”工作仓库，不是具体项目普通记忆库。

2. 外部记忆架构原则
   模型负责计算，文件负责记忆。
   模型是可替换计算单元，不是长期真相源。
   外部文件 / Git 仓库是长期记忆和审计基础。

3. 语言策略
   当前阶段中文为主要工作语言。
   文件名、路径名、ID、状态值、YAML key、命令、工具名和 Git/GitHub 固有术语可以使用英文。

4. 执行源原则
   Raw Record 是证据源，不是执行源。
   Candidate Requirement 是候选，不是执行源。
   Similarity / Conflict Report 是分析材料，不是执行源。
   Decision Record 解释理由，不直接替代执行源。
   Active Context 和 Handoff 是短上下文，不是执行源。
   Human-Approved Spec 是当前执行源。

5. 核心对象模型
   至少覆盖：
   - Raw Record；
   - Candidate Requirement；
   - Similarity / Conflict Report；
   - Human-Approved Spec Entry；
   - Decision Record；
   - Open Question；
   - TODO Item；
   - Handoff；
   - 未来对象：Idea Capture Item、Model-Specific Digest、Delivery Manifest。

6. 需求进入流程
   新输入必须先保存为 Raw Record，再抽取 Candidate Requirement，再进行查重 / 对比，用户确认后才可能进入 Human-Approved Spec。

7. handoff 和 active-context 机制
   用于未来 AI 会话快速接手。
   不默认全量读取 raw。
   发生冲突时以 human-approved-spec 为准，并记录 open question。

8. 模型迁移原则
   默认继承 Canonical Memory，不默认全量重读 raw。
   高风险内容按需回查 raw。
   旧模型专用约束需要复审。
   新模型能力需要验证后再启用。

9. 交付包原则
   Mnemosyne 仓库是设计工厂和设计档案。
   目标项目仓库或目录是目标项目运行真相源。
   交付包应包含设计说明、运行文件包、Delivery Manifest、Handoff Package、Unsupported Assumptions 和 Drift Review TODO。

10. 当前阶段半自动
   用户继续负责重要确认。
   Codex Cloud 当前主要作为远程 GitHub 文件写入和版本保存助手。
   自动查重、自动索引、GitHub Actions、AGENTS.md、CLAUDE.md、MCP、RAG、多 Agent 自动协作等均延期。

## 3. v0.1 不应包含的内容

Mnemosyne v0.1 不应声称已经完成：

- 自动查重；
- 自动索引；
- 自动 ID 生成；
- 自动 schema 校验；
- 自动写回；
- 自动交付；
- 自动 drift 检查；
- 自动模型迁移；
- 自动 raw 重分析；
- GitHub Actions；
- AGENTS.md；
- CLAUDE.md；
- MCP；
- RAG；
- 多 Agent 自动协调；
- 面向具体目标项目的真实交付实施。

这些应全部保留为 v0.2 或后续 TODO。

## 4. 一致性检查目标

本阶段应检查：

- README 是否准确描述 Mnemosyne；
- human-approved-spec 是否覆盖当前已经确认的高层原则；
- active-context 是否反映当前阶段；
- handoff-current 是否足以让未来 AI 会话接手；
- open-questions 是否只保留真正未解决的问题；
- todo 是否包含延期事项；
- candidate-requirements 是否没有把候选误标为执行源；
- decision-log 是否记录了关键决策；
- 是否有文件把未来功能误写成已完成；
- 是否有文件把 raw、candidate、handoff 或 active-context 写成执行源；
- 是否有英文正文或双语内容不符合当前中文策略；
- 是否存在明显互相冲突的描述。

## 5. v0.1 之后的建议路线

v0.1 完成后，建议下一轮不要继续无限扩展基础机制，而是进入一个明确方向：

方向 A：建立正式版 ChatGPT 对话启动包；
方向 B：设计 AGENTS.md / CLAUDE.md 适配；
方向 C：设计第一套目标项目记忆系统交付模板；
方向 D：设计 Idea Capture Buffer；
方向 E：设计 GitHub Actions 轻量文档检查；
方向 F：设计自动查重和 similarity index。

当前阶段只记录这些方向，不实现。
