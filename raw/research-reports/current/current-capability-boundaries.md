# Current Capability Boundaries / 当前能力边界（派生视图）

> 说明：本文件是当前能力边界派生视图，不是原始报告，也不是执行源。  
> 当前 source cycle：`RC-2026Q2-initial`。  
> 上游边界来源：`raw/research-reports/cycles/2026Q2-initial/capability-boundaries.md`。

## 当前状态

- status: active
- source_cycle: RC-2026Q2-initial
- volatility_note: 平台能力具有时效性，未来 research refresh 后需要复核

## 当前能力边界

- capability_area: 普通 ChatGPT / Claude 对话窗口
  supported_use: 对话推理、手工复制粘贴的半自动记忆整理、人工确认后摘要更新
  not_assumed: 自动写回外部仓库、稳定长期持久化、跨会话无损记忆继承
  automation_level: semi_auto
  evidence_reports: [RPT-2026Q2-0002, RPT-2026Q2-0003]
  volatility: high
  notes: 平台更新快；若无额外工具，不应承诺自动化持久记忆
  current_status: needs_review

- capability_area: ChatGPT / Claude Projects
  supported_use: 项目级资料组织与上下文复用（待复核）
  not_assumed: 等同于可审计 Git 写回与完整版本治理
  automation_level: semi_auto
  evidence_reports: [RPT-2026Q2-0001, RPT-2026Q2-0003]
  volatility: high
  notes: 具体能力依平台版本变化，当前结论待复核
  current_status: needs_review

- capability_area: Codex Cloud
  supported_use: 在受控任务中读写仓库文件、生成 diff、配合提交流程
  not_assumed: 默认拥有跨平台持久权限、默认全自动长期记忆编排
  automation_level: agent_assisted
  evidence_reports: [RPT-2026Q2-0001, RPT-2026Q2-0005]
  volatility: high
  notes: 能力依运行环境与权限配置，待持续复核
  current_status: needs_review

- capability_area: Codex / 本地开发 Agent
  supported_use: 文件式记忆维护、结构化文档更新、Git diff 审计
  not_assumed: 自动理解所有 PDF 图表、零人工监督的策略更新
  automation_level: agent_assisted
  evidence_reports: [RPT-2026Q2-0001, RPT-2026Q2-0004]
  volatility: medium
  notes: 对文本类证据更友好，图像/图表仍需人工复核
  current_status: needs_review

- capability_area: Claude Code
  supported_use: 本地仓库文档读写、变更审计、半自动执行文档流程
  not_assumed: 与其他工具完全同构的权限与记忆能力
  automation_level: agent_assisted
  evidence_reports: [RPT-2026Q2-0001, RPT-2026Q2-0004]
  volatility: high
  notes: 细节依版本与产品策略，待复核
  current_status: needs_review

- capability_area: Cursor
  supported_use: 代码/文档编辑辅助、上下文引用、仓库内变更建议
  not_assumed: 原生提供跨仓库长期记忆真相源治理
  automation_level: agent_assisted
  evidence_reports: [RPT-2026Q2-0001, RPT-2026Q2-0004]
  volatility: high
  notes: 可用作执行层助手，不等于完整记忆治理层
  current_status: needs_review

- capability_area: GitHub
  supported_use: 版本管理、diff、PR、review、审计追踪
  not_assumed: 自动生成高质量记忆 schema、自动判定研究证据冲突
  automation_level: agent_assisted
  evidence_reports: [RPT-2026Q2-0001, RPT-2026Q2-0005]
  volatility: low
  notes: 适合作为审计式写回与协作治理底座
  current_status: active

- capability_area: GitHub Actions
  supported_use: 可用于后续自动化流程编排（待复核）
  not_assumed: 当前 Mnemosyne v0.1 默认启用
  automation_level: automated_possible
  evidence_reports: [RPT-2026Q2-0005]
  volatility: medium
  notes: 当前仓库阶段不启用，属于后续增强
  current_status: needs_review

- capability_area: MCP
  supported_use: 可作为后续工具能力扩展与检索接入（待复核）
  not_assumed: 当前默认可用且跨平台一致
  automation_level: automated_possible
  evidence_reports: [RPT-2026Q2-0001, RPT-2026Q2-0006]
  volatility: high
  notes: 需要额外工程接入与治理策略
  current_status: needs_review

- capability_area: RAG / 向量索引
  supported_use: 可用于后续证据检索增强、去全量加载（待复核）
  not_assumed: 当前无需设计即可直接替代结构化文档
  automation_level: automated_possible
  evidence_reports: [RPT-2026Q2-0006, RPT-2026Q2-0007]
  volatility: medium
  notes: 需结合 Evidence Item 设计与质量评估
  current_status: needs_review

- capability_area: NotebookLM / 资料库问答
  supported_use: 文档问答与研究辅助总结（待复核）
  not_assumed: 可直接替代可审计写回与执行源治理
  automation_level: semi_auto
  evidence_reports: [RPT-2026Q2-0002, RPT-2026Q2-0007]
  volatility: high
  notes: 适合研究辅助，不等于执行链路
  current_status: needs_review

- capability_area: 普通 Markdown / Git 仓库
  supported_use: 长期持久化、可追溯历史、跨会话 handoff 与上下文接手
  not_assumed: 自动语义检索与自动冲突消解
  automation_level: manual
  evidence_reports: [RPT-2026Q2-0001, RPT-2026Q2-0006]
  volatility: low
  notes: 作为当前最稳健的基础记忆介质
  current_status: active
