# V2-A A0 Sentinel — Future Startup Message

> Operator instructions for a future G2A-authorized run. Do not use this message before the run-decision candidate and package are merged, execution-time identities are rechecked, and the Owner explicitly authorizes A0.

## 1. Future user operation

Open one fresh ChatGPT conversation with the GitHub connector.

Select the visible option exactly as authorized. The current recommendation is:

```text
gpt-5.6 sol extra high
```

Record the visible model and reasoning labels verbatim. If that option is absent, do not substitute another option; return to the Pro planning conversation.

Do not enable web search, Deep Research, Fable, another connector/app or private-file access.

## 2. Single startup message

Send exactly one substantive startup message:

```text
@GitHub 请严格执行已合并的
MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-001，
仅运行 A0 sentinel。

Owner authorization 必须与
MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-001
的 exact merged identities 一致。先完成完全只读的 receive/preflight；任一来源、ref、blob、模型、权限、材料或 branch-lineage 不一致时，返回 BLOCKED 并停止，不得创建分支或重试。

只有 receive PASS 后，才允许在
08822407d/mnemosyne-target-lifecycle-validation-002
从 master@e8e3296922185b4b70997c2351d6f39423f2cd4f
创建 v2a-sentinel-001-controller。

仅读取
 tlr-v1-fixture-base@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6；
不得修改 fixture、master 或任何 tlr-v1-* ref。
只写 run decision 中列出的七个 A0 结果路径。

不要创建 worker branch、fixture branch 或 PR；不要运行 A1–A7、V2-B 或 V2-C；不要写 Mnemosyne、Meta-Agent 或任何真实目标；不要使用 Web、Deep Research、Fable、其他 app、私有材料或 external quota；失败后不要重试。

完成七文件结果 bundle 和 protected-ref after checks 后立即停止，并把 controller branch head、每个输出 blob/commit、可见模型/推理标签、incident ledger 与全部限制返回给一段全新的 Pro 对话裁决。
```

Do not first send a visibility probe or ask the controller to “inspect and decide what to do.” The frozen package already defines the only task.

## 3. Operator-visible stop conditions

Stop the run and return to Pro if the controller reports:

- any source or ref mismatch;
- missing required package file;
- existing controller branch or related PR;
- model/surface mismatch;
- uncertain public/synthetic material classification;
- inability to enforce the exact branch/path boundary;
- need to repair the package;
- request to enable another app or access a private/real target;
- any attempt to run A1–A7 or create worker branches/PRs.

Do not authorize a retry in the same conversation.

## 4. Return to fresh Pro

Return:

- the complete seven-file output set;
- controller branch and final head;
- every output path/blob/commit identity;
- protected before/after refs;
- visible product/model/reasoning labels;
- any provider or connector warning;
- all incidents and unresolved gaps.

Fresh Pro, not the controller, decides whether A0 is valid and whether a full V2-A package should later be prepared.
