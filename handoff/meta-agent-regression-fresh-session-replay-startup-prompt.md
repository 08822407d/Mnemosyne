# Meta-Agent Regression Fresh-Session Replay — Startup Prompt

Use the text below in a **genuinely new ChatGPT Chat conversation with no prior Mnemosyne task context**, after the MNEMOSYNE-119 repair PR containing this file has been merged.

## Recommended execution selection

- Mode: **Chat** — do not use Work for the primary replay.
- Preferred model: **GPT-5.6 Sol Pro**.
- Intelligence/reasoning: **the highest setting available in Chat**.
- If the exact label is unavailable, use the strongest visible GPT-5.6 Chat model and record its exact label without inferring hidden equivalence.

```markdown
Receive Mnemosyne handoff.

Use this authorized replay handoff package:

- `handoff/meta-agent-regression-fresh-session-replay-package-v3.md`

This is an explicit handoff receive for a read-only behavioral replay. It is not permission to build Meta-Agent or write any repository.

First use:

- `commands/receive-mnemosyne-handoff.md`

After reporting the handoff receive, separately execute:

- **加载 MNEMOSYNE 约束指导**
- command path: `commands/load-mnemosyne-guidance.md`

Confirm that the guidance refresh preserves the received replay task and does not import unrelated Mnemosyne maintenance live state.

Then execute the v3 package exactly as written:

- confirm the current surface is Chat and record the exact visible model/reasoning labels;
- resolve and pin current `master` before substantive evidence reading;
- capture complete branch-head and open-PR snapshots before and after;
- try connected GitHub branch enumeration first;
- if it returns empty despite known `master`, is inconsistent, or cannot prove complete pagination, use these official public GitHub REST fallback URLs exactly:

  - `https://api.github.com/repos/08822407d/Mnemosyne/branches?per_page=100&page=1`
  - `https://api.github.com/repos/08822407d/Mnemosyne/pulls?state=open&per_page=100&page=1`
  - `https://api.github.com/repos/08822407d/Mnemosyne/branches/master`

- follow the v3 page-completion rule and repeat the same method at the end;
- run REG-META-DRYRUN-001, 002, 004, 005, and 007 using read-only evidence at the pinned ref;
- do not inherit any previous PASS label as the new result;
- make no repository or target-project writes;
- return the complete required schema in the final response;
- do not close the final acceptance gate yourself.

If complete mechanical coverage remains unavailable after the explicit REST fallback, report the no-write proof and overall replay as BLOCKED. No exception is authorized.
```

## 中文简介

这段 prompt 用于第二次独立重放。上一轮五项行为判断均正确，但因为连接器没有返回完整 branch heads，整体按协议正确报告了 `BLOCKED`。

本版本增加 GitHub 官方只读 REST endpoint 作为明确 fallback。它仍然不是 Meta-Agent 构建任务，也不授权任何写入。完整结果必须带回当前 Mnemosyne 维护对话复核。
