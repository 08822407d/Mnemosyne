# Report Summary: RPT-2026Q2-0001

## 文件定位

- 本文件是研究报告摘要，不是原始报告；
- 本文件不是执行源；
- 当前执行源仍是 `current/human-approved-spec.md`；
- 如果本摘要与原始报告冲突，应以原始报告为证据来源，并登记 review note；
- 如果本摘要与 `human-approved-spec` 冲突，应以 `human-approved-spec` 为执行准则。

## 元数据

- report_id: RPT-2026Q2-0001
- source_file: raw/research-reports/cycles/2026Q2-initial/originals/AI agent 长期记忆系统 pro深度研究.txt
- cycle_id: RC-2026Q2-initial
- report_type: pro
- topic: AI agent 长期记忆系统综合深度研究
- readability: TXT，可直接读取；本摘要基于可读取文本整理。
- summary_status: completed_from_readable_txt
- figure_review_status: not_applicable_txt
- created_by_task: MNEMOSYNE-030

## 摘要

本报告是 RC-2026Q2-initial 中的综合深度研究，核心判断是：AI Agent 外部持久记忆系统作为工程模式是现实可行的，但不应被理解为普通聊天窗口已经天然具备的完整功能。最稳健的实现路径是把规则、状态、任务、交接、原始材料和评估记录外部化到 Git / Markdown / 数据库 / RAG 等可审计介质中，让模型负责计算与整理，让外部文件或仓库负责长期记忆和版本治理。报告区分了开发场景与普通对话场景：Codex、Claude Code、Cursor、GitHub Copilot cloud agent 等 coding agent 场景更适合读写仓库、生成 diff、提交或 PR；普通 ChatGPT / Claude 纯对话场景更多依赖 Projects、Memory、NotebookLM、连接器和人工复制，不能默认自动写回外部仓库。报告还讨论了非开发长期对话、学习、研究、源码阅读、多 Agent 协作等场景，认为开发场景的文件式状态、handoff、ADR、任务清单和审计写回理念可以迁移，但需要针对学习进度、研究结论、个人隐私和资料来源做差异化 schema。

## 关键结论

- 外部持久记忆系统成立，但当前应作为跨工具工作流和治理架构，而不是单一聊天产品内置能力。
- 当前最强可审计路径在本地 / 云端 coding agent + Git/GitHub 工作流。
- 普通 ChatGPT / Claude 对话窗口默认不应承诺自动写回外部记忆仓库。
- 长期记忆价值在于可读规则、可检索记忆、可审计写回、可恢复交接、可迁移格式和人工复核。
- 多 Agent 或自动化增强需要权限、审计、角色分离和人工确认，不应在 v0.1 / 当前基础阶段默认启用。

## 对 Mnemosyne 设计的影响

支持 Mnemosyne 将自身定位为“记忆系统元 Agent 工作仓库”，以 Git / Markdown 文件作为长期状态和审计基础，并以半自动流程处理新输入、候选需求、决策、handoff 与目标项目交付。

## 对能力边界的影响

强化“模型负责计算，文件负责记忆”的边界；普通对话窗口、Projects、NotebookLM、连接器、Codex、Claude Code、GitHub 等能力必须分层声明，不可混同。

## 对目标项目模板 / delivery manifest 的影响

目标项目模板应包含 intake、memory schema、执行源规则、unsupported assumptions、handoff、delivery manifest 和 drift review；真实交付前必须确认目标项目运行真相源与权限。

## 风险与限制

- 平台能力变化快，涉及 ChatGPT / Claude / Codex / GitHub 等产品时需要定期 refresh。
- 自动写回、RAG、MCP、GitHub Actions、多 Agent 协调都需要额外工具与治理。
- 敏感记忆、密钥、客户数据和个人信息不应无审查暴露给云端 agent。

## 需要人工复核的内容

无 PDF 图表复核要求；仍建议用户抽样核对原 TXT 的关键结论与引用。

## 可引用锚点

- 总体可行性结论
- 非开发长期对话场景实践
- 开发经验迁移到普通长期对话 / 教学 / 研究 / 源码学习
- 多 Agent 团队协作与记忆治理
- 主要工具能力边界
- 半自动 / 需额外工具 / 不建议机制

## open questions / review notes

- 本摘要需要用户 review。
- 本摘要不得直接升级为执行源或最终规范。
- 如后续目标项目设计依赖本报告中的具体产品能力、表格、图示、图片或引用编号，应回查原始报告；PDF 报告还必须先完成人工图表 / 图片 / 版式复核。
