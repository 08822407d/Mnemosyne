# ChatGPT Discussion 040

```yaml
raw_id: RAW-0040
task_id: MNEMOSYNE-028C
task_name: delivery manifest 状态四文件硬替换与记录补账
source_type: codex_task_instruction_summary
status: captured
```

## 说明

本记录不是完整原始对话，而是对本次 Codex 任务来源和边界的精简记录。

本任务用于修复 MNEMOSYNE-028B 后关键状态文件仍未同步的问题。

`notes/delivery-manifest-template-pack.md` 已创建，但人工核查发现关键状态层仍存在残留：

- `current/active-context.md` 仍可能显示目标项目模板包阶段；
- `handoff/handoff-current.md` 仍可能缺少 delivery manifest template pack 推荐读取入口；
- `current/todo.md` 仍可能把 delivery manifest 模板深化列为未完成；
- `current/open-questions.md` 仍可能把“是否先深化 delivery manifest”留在 open 区域。

本任务需要硬替换 active-context、handoff-current、todo、open-questions 中的状态，并补齐 candidate、decision、roadmap、baseline 与 task result record 的审计记录。

当前执行源仍是：

- `current/human-approved-spec.md`

`notes/delivery-manifest-template-pack.md` 不是执行源。

本任务不新增模板、不修改 delivery manifest 模板主体、不为真实目标项目生成交付包、不创建 AGENTS.md / CLAUDE.md / GitHub Actions / MCP / RAG 或自动化脚本。
