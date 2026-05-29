# ChatGPT Discussion RAW-0037

```yaml
raw_id: RAW-0037
task_id: MNEMOSYNE-028
task_name: delivery manifest / 目标项目交付包模板深化
source_type: codex_task_prompt
status: captured
```

## 说明

本记录用于保存 MNEMOSYNE-028 的任务来源摘要，不是完整原始对话。

本任务用于深化 delivery manifest / 目标项目交付包模板，使 Mnemosyne 在未来将记忆系统设计交付到目标项目时，有稳定的交付清单、复制清单、落地检查、handoff package、rollback / revision plan、delivery result record 和 drift review 入口。

本任务只设计模板，不为任何真实目标项目生成交付包。

本任务不创建 `AGENTS.md`、`CLAUDE.md`、GitHub Actions、MCP、RAG 或自动化脚本。

当前执行源仍是：

- `current/human-approved-spec.md`

本任务将创建的 delivery manifest 模板包不是执行源。若 delivery manifest 模板包或其他文件与 `current/human-approved-spec.md` 冲突，应以 `current/human-approved-spec.md` 为准，并登记 open question。

## 研究证据边界

本任务涉及目标项目交付、工具能力边界和自动化承诺，执行时应参考：

- `raw/research-reports/current/research-report-index.md`
- `raw/research-reports/current/current-evidence-map.md`
- `raw/research-reports/current/current-capability-boundaries.md`

研究报告是高权重证据层，不是执行源。不得把 PDF 图表和图片内容写成已验证证据，不得承诺当前系统不具备的自动化能力，不得默认普通对话窗口可以自动写回目标项目仓库，也不得默认 GitHub Actions、RAG、MCP、自动查重或自动写回已经可用。
