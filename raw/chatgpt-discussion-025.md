---
raw_id: RAW-0025
task_id: MNEMOSYNE-025
source_type: user_and_chatgpt_handoff
status: preserved
sensitivity: public_repo_but_personal_design_content
language: zh-CN
---

# RAW-0025：self-improvement workflow 设计

这不是完整原始对话，而是从当前 ChatGPT 对仓库的核对结果和用户决策中整理出的交接记录。

## 当前状态

Mnemosyne v0.1 已经具备可接手能力，并且用户已接受独立验证 `PASS_WITH_WARNINGS`。

当前 v0.2 第一方向选择为：

self-improvement workflow

即：设计 Mnemosyne 如何根据用户新构想、使用反馈、Codex / ChatGPT 任务结果、研究更新和目标项目反馈来持续增强自身。

## 为什么优先做 self-improvement workflow

Mnemosyne 的核心定位是“记忆系统元 Agent”工作仓库，而不是一次性文档模板。

用户会持续提出新想法、修正旧想法、反馈使用体验、引入新工具和新研究结果。
如果没有明确的自我改进流程，仓库会逐渐变成散乱文件，或者让候选需求、raw、decision、todo 和 human-approved-spec 的边界再次混乱。

因此 v0.2 第一阶段需要设计一个半自动、可审查、可回滚的自我改进工作流。

## 设计边界

本阶段只设计工作流，不实现自动化。

当前不做：

- 自动抓取 ChatGPT 对话；
- 自动解析 Codex 完成回复；
- 自动查重；
- 自动更新 human-approved-spec；
- 自动合并 PR；
- 自动索引；
- GitHub Actions；
- AGENTS.md；
- CLAUDE.md；
- RAG / MCP。

当前要做：

- 定义输入来源；
- 定义自我改进流程；
- 定义人工确认点；
- 定义 Codex Task Result Record 的使用规则；
- 定义什么时候更新 human-approved-spec、todo、open-questions、decision-log、active-context、handoff；
- 定义什么时候必须回查 research evidence；
- 定义当前仍然不自动化的边界。
