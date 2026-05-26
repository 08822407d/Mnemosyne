# Human-Approved Spec（当前实施版）

本文档是当前项目的执行源（source of execution）。

## v0.1 已确认高层执行原则

1. Mnemosyne 是“记忆系统元 Agent”工作仓库，不是具体项目普通记忆库。
2. 外部记忆架构原则：模型负责计算，文件负责记忆；模型是可替换计算单元，不是长期真相源。
3. 当前阶段中文正文为主；文件名、ID、状态值、术语等可用英文。
4. Human-Approved Spec 是当前执行源。
5. Raw Record 不是执行源。
6. Candidate Requirement 不是执行源。
7. Similarity / Conflict Report 不是执行源。
8. Decision Record 不是执行源。
9. Active Context 不是执行源。
10. Handoff 不是执行源。
11. 新需求进入实施版前，必须经过 raw 保存、candidate 抽取、查重/对比与用户确认。
12. active-context 与 handoff 用于跨会话接手，raw 按需回查，不默认全量读取。
13. 模型迁移默认继承 Canonical Memory；高风险内容按需回查 raw；旧模型专用约束需复审；新模型能力先验证后启用。
14. Mnemosyne 支持面向目标项目的交付包设计：交付前以 Mnemosyne 设计为主，交付后以目标项目运行文件为主。
15. 当前阶段为半自动流程：用户负责关键确认，Codex Cloud 主要作为远程保存和文件写入助手。
16. v0.1 是最小可用设计仓库，不是完整系统。
17. 自动化能力延期：自动查重、自动索引、自动迁移、自动交付、GitHub Actions、AGENTS.md、CLAUDE.md 等均未实现。

## TODO（机制细化）

- TODO：新需求查重与差异报告模板（人工/半自动）定义。
- TODO：Idea Capture Buffer 的对象字段与流转规则。
- TODO：model migration review 的触发条件与审阅步骤。
- TODO：实施版更新流程的字段模板与最小审阅步骤。
