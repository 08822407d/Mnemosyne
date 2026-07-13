# Meta-Agent Five-Regression Fresh Replay — Startup Prompt

Copy the text below into a **new ordinary ChatGPT conversation** after this file is merged into `master`.

```markdown
加载 Mnemosyne 指导约束。

然后执行以下仓库内的只读 fresh-session behavioral replay package：

- repository: `08822407d/Mnemosyne`
- package: `handoff/meta-agent-five-regression-fresh-replay-package.md`

这是一次新的、隔离的 Mnemosyne 行为回归测试，不是 Meta-Agent 产品建设，也不是让你接管其他维护路线。

严格要求：

1. 不要使用任何旧 Mnemosyne 对话内容、平台隐式记忆或未由仓库文件支持的记忆作为事实。
2. 先按 `commands/load-mnemosyne-guidance.md` 完成行为约束刷新并输出其规定的 `mnemosyne_guidance_refresh` schema。
3. 在读取实质测试证据前，把当前 `master` 解析为精确 commit SHA，并按 package 记录完整的机械 repository-state before snapshot。
4. 所有实质证据必须按该 pinned commit 读取。
5. 严格只读；不得调用任何 GitHub 写入 action，不得创建 branch/file/commit/issue/PR/comment/review/label/reaction，不得修改任何 repository 或 target state。
6. 按 package 完成 `REG-META-DRYRUN-001`、`002`、`004`、`005`、`007` 五项行为重放。
7. 结束时执行 package 规定的机械 before/after repository-state comparison。无法完成机械证明且没有新用户单次例外时，必须报告 `BLOCKED`，不得只用“我没有调用写工具”的自然语言声明代替。
8. 完整结果必须出现在最终回答正文中，并严格采用 package 的 `meta_agent_five_regression_fresh_replay` schema。
9. 每项关键结论都必须给出 repository evidence path 及 authority role。
10. 你的 claimed verdict 不是最终 reviewed verdict；不要写回仓库。维护对话会另行复核。

不要先向用户复述计划或询问是否继续；在边界内直接完成只读 replay。若关键文件、隔离条件或机械证明不可用，按 package 报告 `BLOCKED` 并准确列出原因。
```

## Return instruction

把新对话的完整最终回答原样带回当前普通 Mnemosyne 维护对话，由维护对话依据 `notes/handoff-replay-scorecard-v0.1.md` 独立复核。