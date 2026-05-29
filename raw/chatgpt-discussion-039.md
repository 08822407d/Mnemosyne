# ChatGPT Discussion RAW-0039

```yaml
raw_id: RAW-0039
task_id: MNEMOSYNE-028B
task_name: delivery manifest 状态硬同步与路线图纠偏
source_type: codex_task_prompt
status: captured
```

## 说明

本记录用于保存 MNEMOSYNE-028B 的状态硬同步任务来源摘要，不是完整原始对话。

本任务用于修复 MNEMOSYNE-028 / MNEMOSYNE-028A 后状态层没有真正同步的问题，确保 active-context、handoff、todo、open-questions、candidate、decision、roadmap、baseline 与 Codex Task Result Record 都指向 delivery manifest template pack 已创建、等待用户 review 的状态。

`notes/delivery-manifest-template-pack.md` 已创建。

当前需要把 active-context、handoff、todo、open-questions、candidate、decision、roadmap、baseline 同步到 delivery manifest template pack 已创建状态。

本任务只做状态硬同步和记录纠偏，不新增模板、不修改 delivery manifest 模板主体、不为真实目标项目生成交付包、不创建 AGENTS.md、CLAUDE.md、GitHub Actions、MCP、RAG 或自动化脚本。

当前执行源仍是：

- `current/human-approved-spec.md`

Delivery manifest template pack 不是执行源。若 delivery manifest template pack 或其他状态层文件与 `current/human-approved-spec.md` 冲突，应以 `current/human-approved-spec.md` 为准，并登记 open question。
