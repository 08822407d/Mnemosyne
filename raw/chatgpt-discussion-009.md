---
raw_id: RAW-0009
source_type: user_and_chatgpt_handoff
status: preserved
sensitivity: private
language: zh-CN
---

# RAW-0009：面向目标项目的交付包结构

这不是完整原始对话，而是从早期 ChatGPT 讨论中整理出的第九阶段交接记录，用于设计 Mnemosyne 面向目标项目的记忆系统交付机制。

## 1. 为什么需要交付包结构

Mnemosyne 不是某个具体项目的普通记忆系统，而是“记忆系统元 Agent”。

它的最终用途之一，是为具体目标项目设计和交付外部持久记忆系统。

目标项目可能包括：

- 某个 AI Agent 开发项目；
- 某个多 Agent 团队项目；
- 某个长期研究项目；
- 某个语言学习系统；
- 某个源码学习系统；
- 某个普通长期对话或个人知识管理项目。

因此，Mnemosyne 需要区分：

- Mnemosyne 自己仓库中的设计原本；
- 目标项目实际运行的记忆系统文件；
- 一次交付时输出的交付包；
- 交付后目标项目发生变化时的 drift / 漂移复查。

## 2. 双层仓库原则

当前采用双层模式：

### 2.1 Mnemosyne 仓库

Mnemosyne 仓库保存：

- 原始需求和反馈；
- 候选需求；
- human-approved-spec；
- 对象模型；
- 设计决策；
- 模板草案；
- 交付设计；
- 目标项目交付记录；
- 跨项目经验和模式。

Mnemosyne 仓库是“设计工厂”和“设计档案”。

### 2.2 目标项目仓库或目录

目标项目仓库保存：

- 该项目实际运行需要的记忆系统文件；
- 该项目自己的 handoff；
- 该项目自己的 active context；
- 该项目自己的 raw / candidate / approved spec / decision log；
- 该项目对应工具需要读取的 AGENTS.md、CLAUDE.md、rules 或 project instructions；
- 该项目运行中的状态和反馈。

目标项目仓库是“运行真相源”。

## 3. 主副本原则

在不同阶段，权威位置不同：

### 3.1 设计孵化期

如果目标项目尚未建立，或记忆系统尚未交付：

- Mnemosyne 仓库保存主设计；
- 目标项目可以不存在；
- 设计文档、需求归纳、对象模型和候选模板都保存在 Mnemosyne。

### 3.2 交付后运行期

一旦记忆系统交付给目标项目并开始运行：

- 目标项目仓库中的运行文件是该项目的运行真相源；
- Mnemosyne 仓库保存设计档案、交付记录、版本记录和后续改进建议；
- Mnemosyne 不应默默维护一个与目标项目运行文件冲突的第二真相源。

### 3.3 后续改动

交付后的改动应通过 change proposal 或 delivery update 处理：

- 用户或目标项目反馈问题；
- Mnemosyne 记录需求或反馈；
- 生成变更建议；
- 用户确认；
- 生成新的交付包或补丁说明；
- 目标项目接收后再成为运行真相源的一部分。

## 4. 交付包应包含什么

一次面向目标项目的记忆系统交付，至少应包含：

1. Memory System Design Spec
   说明该目标项目的记忆系统设计：
   - 场景类型；
   - 工具环境；
   - 需要记住什么；
   - 不需要记住什么；
   - 记忆层级；
   - 更新规则；
   - handoff 机制；
   - raw archive 策略；
   - candidate / approved spec 策略；
   - TODO 和 open questions。

2. Target Project Memory Package
   目标项目实际需要放入仓库或目录的运行文件清单。
   例如：
   - README 或说明文件；
   - active-context；
   - handoff-current；
   - human-approved-spec；
   - raw archive 入口；
   - candidate requirements；
   - decision log；
   - open questions；
   - todo；
   - tool-specific instructions。

3. Delivery Manifest
   交付清单。
   用于记录：
   - delivery_id；
   - target_project；
   - delivery_version；
   - source_design_refs；
   - generated_at；
   - target_paths；
   - included_files；
   - excluded_items；
   - unsupported_assumptions；
   - manual_steps_required；
   - review_required；
   - post_delivery_notes。

4. Handoff Package
   供目标项目中的 AI 会话或 Agent 接手的简短交接包。
   它不是完整设计书，而是启动材料。

5. Unsupported Assumptions
   明确哪些能力当前不支持，不能隐含承诺。
   例如：
   - 普通 ChatGPT 网页端不能自动写回 GitHub；
   - 目标项目未配置 Codex / Claude Code 时不能自动改文件；
   - 自动查重、RAG、MCP、GitHub Actions 需要后续工具支持；
   - 敏感原文不能默认交给云端 Agent。

6. Post-Delivery Drift Review TODO
   交付后可能出现目标项目实际文件和 Mnemosyne 设计档案不一致。
   需要记录未来如何复查 drift。

## 5. 交付流程草案

当前建议的手工 / 半自动流程：

1. Intake
   收集目标项目需求、工具环境、隐私约束、自动化期望。

2. Design
   Mnemosyne 生成 Memory System Design Spec 草案。

3. Review
   用户审查设计，确认哪些进入实施版。

4. Package
   Mnemosyne 生成 Target Project Memory Package 和 Delivery Manifest。

5. Deliver
   用户或 Codex / Claude Code 将交付文件复制或提交到目标项目仓库。

6. Activate
   目标项目开始使用该记忆系统。
   目标项目中的运行文件成为该项目的运行真相源。

7. Monitor
   目标项目反馈使用体验、漂移、缺陷或新增需求。

8. Iterate
   反馈回到 Mnemosyne 的 requirement intake workflow。
   经用户确认后产生下一版交付。

## 6. Drift / 漂移问题

交付后可能出现：

- 目标项目手动改了记忆文件；
- 目标项目 Agent 改了 handoff 或 active-context；
- 目标项目新增了本地规则；
- Mnemosyne 后续升级了模板；
- 目标项目没有同步 Mnemosyne 的新设计；
- 目标项目实际使用方式偏离原始设计。

这类差异称为 drift / 设计漂移。

当前阶段不实现自动 drift 检查，只记录未来需要：

- drift report；
- target snapshot；
- delivery manifest comparison；
- user review；
- whether to absorb target changes back into Mnemosyne patterns。

## 7. 目标项目类型差异

不同目标项目不应使用完全相同记忆系统。

例如：

### 软件开发项目

可能需要：
- project-state；
- tasks；
- ADR；
- memory-ledger；
- test / CI 记录；
- code review notes；
- AGENTS.md / CLAUDE.md。

### 语言学习项目

可能需要：
- learning-profile；
- course-state；
- mistake-log；
- vocabulary-review；
- grammar weaknesses；
- weekly evaluation。

### 源码学习项目

可能需要：
- source-study-state；
- subsystem-map；
- call-chain-notes；
- struct-function-index；
- unresolved-questions；
- reading tasks。

### 长期研究项目

可能需要：
- research-state；
- hypothesis log；
- source index；
- decision log；
- open questions；
- literature notes。

Mnemosyne 未来应根据目标项目类型生成不同 memory system design spec。

## 8. 当前阶段边界

当前不做：

- 自动交付；
- 自动同步目标项目；
- 自动 drift 检查；
- 自动生成目标项目 PR；
- 自动生成 AGENTS.md / CLAUDE.md；
- 自动配置 GitHub Actions；
- 自动部署 RAG / MCP；
- 多 Agent 自动协调。

当前只做：

- 建立交付包概念；
- 明确双层仓库原则；
- 明确交付后目标项目运行文件是运行真相源；
- 设计 delivery manifest 的作用；
- 记录未来 drift review 需求；
- 为 v0.1 收束做准备。
