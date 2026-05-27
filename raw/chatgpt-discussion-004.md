---
raw_id: RAW-0004
source_type: user_and_chatgpt_handoff
status: preserved
sensitivity: private
language: zh-CN
---

# RAW-0004：Mnemosyne 核心对象模型设计

这不是完整原始对话，而是从早期 ChatGPT 讨论中整理出的第四阶段交接记录，用于建立 Mnemosyne 的核心对象模型。

## 1. 为什么需要对象模型

Mnemosyne 不是一次性模板生成器，而是一个持续演进型“记忆系统元 Agent”。

它需要长期处理：
- 用户原始需求；
- 用户使用体验反馈；
- 上游 Agent 转交的记忆系统需求；
- 临时粗糙点子；
- 候选需求；
- 新旧需求查重结果；
- 用户确认后的实施版；
- 设计决策；
- TODO；
- 开放问题；
- handoff；
- 未来交付给具体目标项目的记忆系统设计书。

如果没有清晰对象模型，仓库会很快变成一堆散乱 Markdown 文件，后续 AI 会话也难以判断哪些内容是证据、哪些是候选、哪些是真正执行依据。

## 2. 核心分层原则

Mnemosyne 当前需要至少区分以下对象层级：

1. Idea Capture Item
   临时点子速记项。用于保存突然冒出的粗糙想法。
   当前只作为未来 TODO，不在本阶段完整实现。

2. Raw Record
   原文记录。保存用户、ChatGPT、Codex、上游 Agent 或其他来源给出的原始需求、反馈、交接和讨论材料。
   Raw Record 是历史证据，不是执行源。

3. Candidate Requirement
   候选需求。由模型从 Raw Record 或其他材料中整理出的可能需求。
   Candidate Requirement 不是执行源，必须经过查重、对比和用户确认后才可能进入 Human-Approved Spec。

4. Similarity / Conflict Report
   查重和冲突报告。用于比较新想法与已有 raw、candidate、decision、approved spec、open question、TODO 之间的关系。
   它应说明相同点、差异、冲突、可能合并方式和建议动作，但不替用户做最终决定。

5. Human-Approved Spec Entry
   人类确认实施版条目。代表当前项目真正采用的需求、原则、约束或设计规则。
   它是执行源，应能追溯到 raw 和 candidate。

6. Decision Record
   设计决策记录。记录为什么选择某个方案、拒绝某个方案、延期某个功能。
   它与 Human-Approved Spec 不同：Decision Record 解释“为什么”，Approved Spec 规定“现在按什么执行”。

7. Open Question
   开放问题。记录尚未解决、需要用户或未来模型进一步确认的问题。

8. TODO Item
   延期任务。记录明确知道以后要做，但当前阶段不做的事项。

9. Handoff
   交接记录。给未来 AI 会话快速恢复当前工作状态。
   Handoff 应短，不应复制全部历史。

10. Model-Specific Digest
   模型专用摘要。未来用于给不同模型或工具生成不同压缩视图。
   当前只作为 TODO，不在本阶段实现。

11. Delivery Manifest
   交付清单。未来当 Mnemosyne 为某个具体目标项目生成记忆系统时，用于记录交付版本、目标路径、来源设计和未支持假设。
   当前只作为 TODO，不在本阶段实现。

## 3. 关键关系

对象之间应具备这些关系：

- Raw Record 可以产生多个 Candidate Requirement。
- Candidate Requirement 必须引用来源 Raw Record。
- Candidate Requirement 可以与旧 Candidate、Approved Spec、Decision、TODO、Open Question 发生 similar、duplicate、conflicts_with、refines、supersedes、merged_into 等关系。
- Human-Approved Spec Entry 应引用相关 Candidate Requirement 和 Raw Record。
- Decision Record 应解释某个 Approved Spec、TODO 或 rejected alternative 背后的理由。
- Handoff 应引用当前 Active Context、Approved Spec 和主要 Open Questions，而不是复制全部原文。
- TODO 可以由Candidate Requirement、Decision Record 或 Open Question 派生。
- 未来 Delivery Manifest 应引用 Approved Spec、Design Spec 和目标项目路径。

## 4. 状态值建议

当前可以先使用简单状态值：

- raw 状态：
  - preserved
  - superseded
  - sensitive
  - archived

- candidate 状态：
  - pending
  - reflected
  - rejected
  - deferred
  - merged
  - superseded

- approved spec 状态：
  - active
  - deprecated
  - replaced
  - review_on_model_upgrade

- decision 状态：
  - accepted
  - deferred
  - rejected
  - superseded

- TODO 状态：
  - todo
  - in_progress
  - blocked
  - done
  - deferred

- open question 状态：
  - open
  - answered
  - deferred
  - blocked

这些状态值当前只是草案，未来可以在模板阶段进一步规范。

## 5. 设计边界

本阶段只建立核心对象模型说明，不实现自动化。

当前不做：
- 自动生成 ID；
- 自动查重；
- 自动索引；
- 自动 schema 校验；
- 自动同步到目标项目；
- 自动生成 delivery manifest；
- GitHub Actions；
- AGENTS.md / CLAUDE.md。

当前只做：
- 建立对象说明；
- 明确对象关系；
- 记录初步字段建议；
- 为后续模板设计打基础。
