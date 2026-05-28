---
raw_id: RAW-0026
task_id: MNEMOSYNE-025A
source_type: user_and_chatgpt_handoff
status: preserved
sensitivity: public_repo_but_personal_design_content
language: zh-CN
---

# RAW-0026：self-improvement workflow 一致性清理与记录补账

这不是完整原始对话，而是从当前 ChatGPT 对仓库的核对结果中整理出的修复记录。

## 当前状态

MNEMOSYNE-025 已经创建 `notes/self-improvement-workflow.md`，并将 v0.2 第一方向推进为 self-improvement workflow。

但当前检查发现：

- `notes/self-improvement-workflow.md` 接近单行 Markdown，需要恢复正常标题、段落和列表；
- Codex Task Result Record 默认路径误写为 `notes/codex-task-results/-result.md`，需要改为 `notes/codex-task-results/<TASK_ID>-result.md`；
- `notes/candidate-requirements.md` 中 self-improvement workflow 相关候选需求存在孤立条目或 ID 缺口，需要补齐或校正；
- 本任务只做一致性清理和记录补账，不创建新模板，不引入自动化。

## 本次目标

完成后：

- self-improvement workflow 文件应可读、可 review；
- Codex Task Result Record 路径规则应正确；
- candidate-requirements 不应存在没有 CAND ID 的孤立条目；
- decision-log 应记录本次清理决策；
- todo / open-questions 应继续把 self-improvement 模板设计作为后续事项，而不是标成已完成。
