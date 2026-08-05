# Meta-Agent Post-MA-DR-09 — New Conversation Startup Prompt

@GitHub 请读取并严格执行：

```text
target-projects/meta-agent/handoff/meta-agent-post-ma-dr-09-handoff-package.md
```

第一轮只做 handoff receive：

1. 核验 `08822407d/Mnemosyne` 执行时最新 `master`；
2. 核验 handoff package 中列出的 PR #249 repair merge 与 post-merge finalization PR 均已合并；
3. 按 handoff 的 required reading order 读取 Meta-Agent target-local 文件；
4. 返回结构化 `handoff_receive_report`，至少包括：
   - handoff identity；
   - latest master/ref；
   - PR #249 repair identity and merge state；
   - post-merge finalization PR identity and merge state；
   - Meta-Agent target-truth path and operational status；
   - completed milestones；
   - MA-DR-09 original and final dispositions；
   - pending P0/P1 work；
   - separate dependencies；
   - deferred/prohibited actions；
   - missing/stale/conflicting artifacts；
   - recommended first post-receive action；
5. 不进行 Owner acceptance、candidate promotion、prototype implementation、benchmark/pilot planning or execution、private-material ingestion、operational activation 或 GitHub 写入；
6. 返回 receive report 后停止，等待我的下一条命令。

完成 receive report 后，我会单独发送 compatibility guard 中的增强版 Mnemosyne 指导加载命令；不要用裸命令替代。
