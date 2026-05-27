---
raw_id: RAW-0017
source_type: user_and_chatgpt_handoff
status: preserved
sensitivity: public_repo_but_personal_design_content
language: zh-CN
---

# RAW-0017：v0.1 接手能力实际落地校正

这不是完整原始对话，而是从当前 ChatGPT 对仓库的核对结果中整理出的修复记录。

## 当前问题

RAW-0016 已经写入仓库，human-approved-spec 的内容也已经扩展到 v0.1 执行源原则。

但实际检查发现：

- current/human-approved-spec.md 仍接近单行压缩格式；
- current/active-context.md 仍提示“下一步建议执行 v0.1 接手能力修复与当前状态同步”；
- handoff/handoff-current.md 仍提示“下一步建议执行 v0.1 接手能力修复与状态同步”；
- current/todo.md 仍未按 v0.1-final / v0.2 / future 分组；
- candidate-requirements 和 decision-log 仍未补齐 RAW-0016 / RAW-0017 相关接手能力条目；
- v0.1-scope-and-consistency-check 中部分“已完成”描述与实际文件不完全一致。

## 本次目标

本次任务必须真正更新 current/、handoff/ 和 notes/ 中的接手相关文件。

完成后，新 ChatGPT 对话或新 Codex 任务应能通过读取仓库文件接手 Mnemosyne 当前工作。
