# Meta-Agent Post-MA-DR-09 — New Conversation Startup Prompt

@GitHub 请读取并严格执行：

```text
target-projects/meta-agent/handoff/meta-agent-post-ma-dr-09-handoff-package.md
```

第一轮只做 handoff receive：

1. 核验 `08822407d/Mnemosyne` 执行时最新 `master`；
2. 核验包含本 startup prompt 和 handoff package 的 repair PR 已合并；
3. 按 handoff 的 required reading order 读取 Meta-Agent target-local 文件；
4. 返回结构化 `handoff_receive_report`，至少包括：
   - handoff identity；
   - latest master/ref；
   - repair PR identity and merge state；
   - Meta-Agent target-truth path and operational status；
   - completed milestones；
   - MA-DR-09 original and final dispositions；
   - pending P0/P1 work；
   - separate dependencies；
   - deferred/prohibited actions；
   - missing/stale/conflicting artifacts；
   - recommended first post-receive action；
5. 不进行 Owner acceptance、candidate promotion、prototype implementation、
   benchmark/pilot planning or execution、private-material ingestion、
   operational activation 或 GitHub 写入；
6. 返回 receive report 后停止，等待我的下一条命令。

完成 receive report 后，我会单独发送下列增强版指导加载命令；不要用裸命令替代：

```text
@GitHub 加载 Mnemosyne 指导约束，但只作为 Meta-Agent bootstrap 审阅、
交接正确性和仓库操作的流程／安全约束刷新。

防误解附加要求：
- 当前对话的唯一工作主线是 META_AGENT_PRODUCT_BUILD，不是 Mnemosyne maintenance；
- 不导入、继续或接管 Mnemosyne maintenance route；
- 不把 Mnemosyne 的 current/active-context.md、handoff/handoff-current.md、
  current/todo.md 或 current/open-questions.md 当作本对话行动计划，
  除非某个 Meta-Agent 任务独立、明确要求读取它们；
- 不把 Mnemosyne 指导、维护状态、研究状态或 handoff 当作 Meta-Agent target truth；
- Meta-Agent 唯一 target truth 是
  target-projects/meta-agent/current/approved-spec.md；
- 加载指导只刷新行为、交接和仓库安全约束，不启动 handoff、研究、
  prototype、benchmark、pilot、activation 或仓库写入；
- 不因两个项目共用同一仓库而推断项目身份、权威、路线或当前任务合并；
- 如果 Mnemosyne 指导与 Meta-Agent Owner 已批准的 target-local 规则冲突，
  停止并报告冲突，不静默覆盖 Meta-Agent；
- 该兼容层在 Meta-Agent 迁入专属仓库或建立自身行为指导后重新审阅。
```
