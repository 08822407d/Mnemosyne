# Current Evidence Map / 当前证据映射（派生视图）

> 说明：本文件是当前研究证据派生视图，不是原始报告，也不是执行源。  
> 当前 source cycle：`RC-2026Q2-initial`。  
> 上游映射来源：`raw/research-reports/cycles/2026Q2-initial/evidence-map.md`。

## 当前状态

- status: active
- source_cycle: RC-2026Q2-initial
- report_count: 7

## 当前采用的设计原则映射

### 1)
- design_principle: 模型负责计算，文件负责记忆
- supporting_reports: [RPT-2026Q2-0001, RPT-2026Q2-0004, RPT-2026Q2-0006]
- confidence: high
- volatility: medium
- notes: 综合研究与工程向报告共同支持外部文件化记忆路径。
- unresolved_questions: PDF 细节论据仍需人工复核。
- current_status: needs_review

### 2)
- design_principle: 外部文件 / Git 仓库作为长期真相源
- supporting_reports: [RPT-2026Q2-0001, RPT-2026Q2-0004, RPT-2026Q2-0005, RPT-2026Q2-0006]
- confidence: high
- volatility: medium
- notes: 本地开发 Agent 与 GitHub 工作流研究共同指向仓库化真相源。
- unresolved_questions: 各平台权限模型差异需持续更新。
- current_status: needs_review

### 3)
- design_principle: 普通 ChatGPT / Claude 对话窗口默认半自动
- supporting_reports: [RPT-2026Q2-0002, RPT-2026Q2-0003]
- confidence: high
- volatility: high
- notes: 纯对话场景不应默认具备稳定自动写回与系统级持久存储。
- unresolved_questions: 平台功能更新频繁，需在下一轮 refresh 复核。
- current_status: needs_review

### 4)
- design_principle: Codex / Claude Code / Cursor 更适合文件读写、Git diff 和仓库化记忆
- supporting_reports: [RPT-2026Q2-0001, RPT-2026Q2-0004]
- confidence: medium
- volatility: high
- notes: 结论基于文件式工作流主题与综合报告，PDF 细节需要人工复核。
- unresolved_questions: 各工具在沙箱/权限/上下文限制上的差异待复核。
- current_status: needs_review

### 5)
- design_principle: 云端 Coding Agent 和 GitHub 工作流适合 PR、review、审计式写回
- supporting_reports: [RPT-2026Q2-0001, RPT-2026Q2-0005]
- confidence: medium
- volatility: high
- notes: 初步支持“审计式写回优于隐式写回”的设计方向。
- unresolved_questions: 不同平台 CI/CD 与审批策略耦合方式待复核。
- current_status: needs_review

### 6)
- design_principle: Human-Approved Spec 是执行源
- supporting_reports: [RPT-2026Q2-0001]
- confidence: high
- volatility: low
- notes: 研究证据用于约束，不应直接覆盖执行源。
- unresolved_questions: 与 spec 冲突时的标准模板需补齐。
- current_status: active

### 7)
- design_principle: Raw / research reports 是证据层
- supporting_reports: [RPT-2026Q2-0001]
- confidence: high
- volatility: low
- notes: 证据层与执行源分离是当前治理基础。
- unresolved_questions: 循环刷新时的证据状态标注细则待补充。
- current_status: active

### 8)
- design_principle: Handoff / active-context 用于跨会话接手
- supporting_reports: [RPT-2026Q2-0001, RPT-2026Q2-0007]
- confidence: medium
- volatility: medium
- notes: 跨会话迁移依赖结构化上下文而非模型隐式记忆。
- unresolved_questions: 非开发场景的最小 handoff schema 待验证。
- current_status: needs_review

### 9)
- design_principle: 不默认全量加载 raw
- supporting_reports: [RPT-2026Q2-0001, RPT-2026Q2-0006]
- confidence: medium
- volatility: medium
- notes: 全量加载成本高且易引入噪声，应基于索引与任务相关性选择。
- unresolved_questions: 后续是否引入检索层（RAG/索引）待评估。
- current_status: needs_review

### 10)
- design_principle: 不默认全自动写回
- supporting_reports: [RPT-2026Q2-0003, RPT-2026Q2-0005]
- confidence: high
- volatility: high
- notes: 对话窗口与云端工作流研究共同提示需要审计和人工确认环节。
- unresolved_questions: 哪些低风险场景可放宽到更高自动化等级待定义。
- current_status: needs_review

### 11)
- design_principle: 长上下文不能替代外部持久记忆
- supporting_reports: [RPT-2026Q2-0001, RPT-2026Q2-0002, RPT-2026Q2-0006]
- confidence: high
- volatility: medium
- notes: 长上下文有上限且会漂移，外部记忆仍需结构化持久化。
- unresolved_questions: 面向学习/研究场景的长期检索策略待细化。
- current_status: needs_review

### 12)
- design_principle: 自动查重、RAG、MCP、GitHub Actions 属于后续增强
- supporting_reports: [RPT-2026Q2-0001, RPT-2026Q2-0005, RPT-2026Q2-0006]
- confidence: medium
- volatility: high
- notes: 目前仅有方向性证据，工程落地路径尚需进一步验证。
- unresolved_questions: 各增强机制的优先级与依赖关系待确定。
- current_status: needs_review

### 13)
- design_principle: 平台适配层不能假设所有工具能力相同
- supporting_reports: [RPT-2026Q2-0001, RPT-2026Q2-0003, RPT-2026Q2-0004, RPT-2026Q2-0005]
- confidence: high
- volatility: high
- notes: 工具能力、权限和可审计性差异显著，需要显式适配层。
- unresolved_questions: 适配层元数据 schema 需后续定义。
- current_status: needs_review

### 14)
- design_principle: 不同目标项目类型需要不同 memory schema
- supporting_reports: [RPT-2026Q2-0001, RPT-2026Q2-0002, RPT-2026Q2-0007]
- confidence: medium
- volatility: medium
- notes: 开发与非开发场景迁移并非等价，需要差异化结构设计。
- unresolved_questions: 首批场景分类与模板集合待确定。
- current_status: needs_review

## 人工复核标记

- RPT-2026Q2-0002 至 RPT-2026Q2-0007 为 PDF；涉及图表、图片或复杂版式时，当前映射均为 needs_review。

## 演化规则

- 未来 refresh 会更新 current 视图。
- 旧 cycle 保留，不覆盖、不删除。
