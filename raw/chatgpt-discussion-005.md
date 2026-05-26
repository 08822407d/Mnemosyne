---
raw_id: RAW-0005
source_type: user_and_chatgpt_handoff
status: preserved
sensitivity: private
language: zh-CN
---

# RAW-0005：对象模板与 ID / 状态规则设计

这不是完整原始对话，而是从早期 ChatGPT 讨论中整理出的第五阶段交接记录，用于建立 Mnemosyne 的对象模板与基础 ID / 状态规则。

## 1. 为什么需要模板

Mnemosyne 已经确认需要区分 Raw Record、Candidate Requirement、Similarity / Conflict Report、Human-Approved Spec Entry、Decision Record、Open Question、TODO Item、Handoff 等核心对象。

但如果没有模板，后续手工录入和 AI 辅助整理时容易出现这些问题：

- 字段不一致；
- ID 不连续；
- 状态值混乱；
- source_refs 缺失；
- 候选需求被误当成实施版；
- 原文、候选、实施版、决策记录之间无法追溯；
- 未来模型接手时难以判断对象含义。

因此第五阶段需要建立第一版对象模板和 ID / 状态规则。

## 2. 当前阶段的模板原则

当前模板只服务于手工维护和 Codex 小步写入，不实现自动化。

模板应满足：

- 人类可读；
- AI 容易填写；
- Git diff 清晰；
- 字段不要过多；
- 必须能追溯来源；
- 必须明确对象是否是执行源；
- 必须明确状态；
- 未确定内容可以填 TODO；
- 未来可以被脚本或 GitHub Actions 校验，但当前不实现。

## 3. 当前建议的 ID 前缀

当前阶段先使用这些 ID 前缀：

- IDEA-0001：临时点子速记项，未来功能。
- RAW-0001：原文记录。
- CAND-0001：候选需求。
- SIM-0001：查重和冲突报告。
- SPEC-0001：Human-Approved Spec Entry。
- DEC-0001：设计决策记录。
- OQ-0001：开放问题。
- TODO-0001：延期任务。
- HOFF-0001：handoff 记录。
- DIGEST-0001：模型专用摘要，未来功能。
- DELIV-0001：交付清单，未来功能。

这些前缀当前是草案，未来可以调整。

## 4. ID 规则

当前采用简单规则：

- ID 使用大写前缀 + 四位数字。
- 同一对象类型内编号递增。
- 不要求当前阶段自动生成 ID。
- 不要求跨文件自动校验 ID。
- 不复用已删除或废弃对象的 ID。
- 如果合并或替代旧对象，应保留旧 ID 并使用 merged_into、supersedes、replaced_by 等字段说明关系。
- 如果发现编号冲突，应作为 open question 或 TODO 记录，而不是静默修正。

## 5. 状态规则

状态值应尽量少而稳定。

Raw Record：
- preserved
- archived
- superseded
- sensitive

Candidate Requirement：
- pending
- reflected
- rejected
- deferred
- merged
- superseded

Similarity / Conflict Report：
- draft
- reviewed
- resolved
- deferred

Human-Approved Spec Entry：
- active
- deprecated
- replaced
- review_on_model_upgrade

Decision Record：
- accepted
- deferred
- rejected
- superseded

Open Question：
- open
- answered
- deferred
- blocked

TODO Item：
- todo
- in_progress
- blocked
- done
- deferred

Handoff：
- current
- archived
- superseded

未来对象 Model-Specific Digest 和 Delivery Manifest 的状态值暂不细化。

## 6. source_refs 规则

任何由其他材料派生出的对象都应尽量包含 source_refs。

- Candidate Requirement 应引用 Raw Record。
- Similarity / Conflict Report 应引用新对象和被比较的旧对象。
- Human-Approved Spec Entry 应引用 Candidate Requirement 和 Raw Record。
- Decision Record 应引用 Raw Record、Candidate Requirement、Approved Spec Entry 或 Open Question。
- TODO Item 应引用产生该任务的需求、决策或开放问题。
- Handoff 应引用当前 Active Context、Human-Approved Spec 和主要 Open Questions。

source_refs 不要求当前阶段机器可校验，但要写得清楚。

## 7. 执行源规则

必须明确区分：

- Raw Record：证据源，不是执行源。
- Candidate Requirement：候选，不是执行源。
- Similarity / Conflict Report：分析材料，不是执行源。
- Human-Approved Spec Entry：执行源。
- Decision Record：解释决策理由，不直接替代执行源。
- Open Question：未决事项，不是执行源。
- TODO Item：未来任务，不是执行源。
- Handoff：短上下文和交接材料，不是完整历史，也不是执行源。

## 8. 本阶段边界

当前只创建模板说明，不创建大量模板目录。
当前不为每个对象创建单独文件夹。
当前不实现自动生成、自动查重、自动索引或自动校验。
未来如果模板稳定，再考虑拆分到 templates/ 目录或引入 GitHub Actions 检查。
