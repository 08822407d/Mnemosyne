# Requirement Intake Workflow / 需求进入流程

这是 Mnemosyne 当前阶段处理新需求、新反馈、新想法和上游 Agent 请求的半自动流程草案。

## 流程总览

Raw Record  
→ Candidate Requirement  
→ Similarity / Conflict Report  
→ 用户确认  
→ Human-Approved Spec Entry  
→ Active Context / Handoff 更新

## 流程步骤

### 1) Capture / 保存输入
- 目标：把新输入先保存为 Raw Record，保留原始语言和上下文。
- 产物：`RAW-xxxx`。
- 说明：Raw 是证据源，不是执行源。

### 2) Extract / 抽取候选需求
- 目标：从 Raw 中抽取 Candidate Requirement。
- 产物：`CAND-xxxx`。
- 说明：Candidate 是候选，不是执行源。

### 3) Compare / 查重和对比
- 目标：将新 Candidate 与历史对象比较。
- 比较对象：Raw Record、Candidate Requirement、Human-Approved Spec Entry、Decision Record、Open Question、TODO Item。
- 产物：Similarity / Conflict Report（`SIM-xxxx`）。

### 4) Present / 向用户呈现差异
- 目标：用可审阅方式说明重复、相似、冲突、细化、替代、合并建议。
- 产物：可供用户决策的摘要与关系说明。

### 5) Decide / 用户确认
- 目标：由用户明确给出处理决定。
- 可选动作：`merge`、`replace`、`keep_parallel`、`defer`、`reject`、`keep_candidate`、`ask_followup`。

### 6) Apply / 更新实施版
- 目标：仅在用户确认后更新 Human-Approved Spec Entry。
- 要求：保留 `source_refs`，并同步记录相关 Decision Record。

### 7) Refresh / 更新工作上下文
- 目标：当实施版变化时，同步更新 `current/active-context.md`、`handoff/handoff-current.md`、`current/open-questions.md`、`current/todo.md`。
- 说明：若仅新增候选，不更新执行源。

## 输入来源

- 用户直接输入（ChatGPT / Codex / 其他对话入口）。
- 上游 Agent 转交（含来源、目标项目、摘要、引用、约束）。
- 临时点子速记（未来进入 Idea Capture Buffer，当前仅 TODO）。
- 模型迁移、项目复盘、目标项目交付产生的新需求或新约束。

## 用户确认选项

- `merge`
- `replace`
- `keep_parallel`
- `defer`
- `reject`
- `keep_candidate`
- `ask_followup`

## 执行源规则

- Raw Record 不是执行源。
- Candidate Requirement 不是执行源。
- Similarity / Conflict Report 不是执行源。
- 只有 Human-Approved Spec Entry 是执行源。

## 当前阶段边界

- 当前不实现自动化。
- 当前不做自动查重。
- 当前不做自动写回。
- 当前不做 AGENTS.md / CLAUDE.md / GitHub Actions。


## 流程同步规则（补充）

- 当 Human-Approved Spec 更新后，应检查是否需要同步更新 `current/active-context.md` 和 `handoff/handoff-current.md`。
- 当 candidate 只是新增但未被用户确认时，不应自动更新执行源。
- 当需求进入流程结束后，应视情况更新 `current/open-questions.md`、`current/todo.md`、`notes/decision-log.md` 和 `handoff/handoff-current.md`。


## 模型迁移相关补充

- 模型迁移过程中产生的新需求或反馈，仍必须走 requirement intake workflow。
- 新模型提出的改进建议不能直接进入 human-approved-spec。
- 迁移中发现的旧约束问题，应先形成 Candidate Requirement、Decision Record 或 Open Question。
- 用户确认后才更新 Human-Approved Spec。


## 目标项目交付后的反馈回流补充

- 目标项目使用反馈应回到 Mnemosyne 的 requirement intake workflow。
- 交付后发现的 drift、缺陷、新需求应先保存为 Raw Record。
- 目标项目中的改动不应自动覆盖 Mnemosyne 的 human-approved-spec。
- 目标项目反馈经 candidate、similarity report、用户确认后，才可能更新 Mnemosyne 的设计模式或下一版交付包。
