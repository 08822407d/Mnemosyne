---
raw_id: RAW-0006
source_type: user_and_chatgpt_handoff
status: preserved
sensitivity: private
language: zh-CN
---

# RAW-0006：需求进入流程设计

这不是完整原始对话，而是从早期 ChatGPT 讨论中整理出的第六阶段交接记录，用于设计 Mnemosyne 的需求进入流程。

## 1. 为什么需要需求进入流程

Mnemosyne 需要长期接收来自不同来源的需求、反馈和想法，包括：

- 用户直接提出的新需求；
- 用户对现有设计的使用体验反馈；
- 用户突然想到的粗糙点子；
- 上游 Agent 或元 Agent 转交的记忆系统相关需求；
- 后续模型迁移、项目复盘、目标项目交付过程中产生的新约束；
- 对旧设计的修正、替换、反对或补充。

这些输入不能直接进入 Human-Approved Spec。原因是：

- 用户在不同时期可能反复提出相似想法；
- 新想法不一定比旧想法更好；
- 原文可能包含粗糙、临时、矛盾或未验证内容；
- 模型整理版可能产生误解或过度概括；
- 长期实施版必须稳定、可追溯、可审查。

因此，Mnemosyne 需要一个明确流程，把新输入从原文证据逐步转为候选需求，并在查重、对比和用户确认后，才允许进入实施版。

## 2. 基本流程

当前阶段采用以下半自动流程：

1. Capture / 保存输入
   将用户、上游 Agent 或当前 ChatGPT 讨论中的新需求、反馈、想法保存为 Raw Record。
   Raw Record 保留原始语言和上下文，作为历史证据。

2. Extract / 抽取候选需求
   从 Raw Record 中抽取 Candidate Requirement。
   Candidate Requirement 是模型整理出的候选需求，不是执行源。

3. Compare / 查重和对比
   将新的 Candidate Requirement 与已有 Raw Record、Candidate Requirement、Human-Approved Spec Entry、Decision Record、Open Question 和 TODO Item 进行对比。
   产出 Similarity / Conflict Report。

4. Present / 向用户呈现差异
   Similarity / Conflict Report 应说明：
   - 是否重复；
   - 是否相似；
   - 是否冲突；
   - 是否细化旧需求；
   - 是否替代旧需求；
   - 是否应合并；
   - 是否应保持为候选；
   - 是否应拒绝或延期。

5. Decide / 用户确认
   用户决定：
   - 合并进已有实施版；
   - 替换旧实施版；
   - 作为并列规则保留；
   - 暂时保留为候选；
   - 标记为 deferred；
   - 标记为 rejected；
   - 需要进一步讨论。

6. Apply / 更新实施版
   只有用户确认后，才更新 Human-Approved Spec Entry 或 current/human-approved-spec.md。
   更新时必须保留 source_refs，并记录相关 Decision Record。

7. Refresh / 更新工作上下文
   如果实施版发生变化，应同步更新 Active Context、Handoff、Open Questions 或 TODO。
   如果只是新增候选需求，不应更新执行源。

## 3. 输入来源

需求进入流程应支持至少三类来源：

### 3.1 用户直接输入

用户可能直接在 ChatGPT、Codex、Claude 或其他对话窗口中提出新想法。
这类输入应优先保存原文，不应直接改写成实施版。

### 3.2 上游 Agent 转交

未来可能存在其他元 Agent，例如“AI Agent 项目架构元 Agent”。
当它发现某个项目中出现持久记忆相关需求时，可以把结构化请求交给 Mnemosyne。
这类请求应包含来源、目标项目、需求摘要、原文引用、未决问题和约束。

### 3.3 临时点子速记

用户可能突然想到粗糙点子，需要先快速保存。
这类内容未来进入 Idea Capture Buffer。
当前只作为 TODO，不在本阶段实现。

## 4. 不同对象在流程中的角色

Raw Record：
- 记录原文。
- 是证据源。
- 不是执行源。

Candidate Requirement：
- 从 Raw Record 或上游材料抽取。
- 是候选。
- 不是执行源。

Similarity / Conflict Report：
- 比较新旧需求。
- 提供差异和合并建议。
- 不替用户做最终决定。
- 不是执行源。

Human-Approved Spec Entry：
- 用户确认后的实施版条目。
- 是执行源。

Decision Record：
- 记录为什么接受、拒绝、合并、延期或替换某个需求。
- 解释原因，不直接替代实施版。

Open Question：
- 记录流程中无法决定的问题。
- 不是执行源。

TODO Item：
- 记录明确延期的工作。
- 不是执行源。

Handoff：
- 记录当前进展和下一步。
- 帮助未来 AI 会话接手。
- 不是完整历史，也不是执行源。

## 5. 用户确认选项

当新需求与旧需求存在相似或冲突时，Mnemosyne 应向用户提供明确选项：

- merge：合并进已有需求或实施版；
- replace：替换旧版本；
- keep_parallel：保留为并列规则；
- defer：延期处理；
- reject：拒绝，但保留原文；
- keep_candidate：保留为候选需求；
- ask_followup：继续追问澄清。

模型可以提出建议，但不得替用户静默决定。

## 6. 当前阶段边界

当前只设计流程，不实现自动化。

当前不做：
- 自动从对话抓取原文；
- 自动写入 GitHub；
- 自动语义查重；
- 自动生成 Similarity Index；
- 自动更新 Human-Approved Spec；
- 自动生成 PR；
- 自动同步多 Agent 请求；
- GitHub Actions；
- MCP；
- AGENTS.md / CLAUDE.md。

当前只做：
- 建立流程说明；
- 更新候选需求和决策记录；
- 明确用户确认是进入实施版的必要条件；
- 为后续模板和自动化打基础。
