# V2-A A0 Sentinel — Future G2A and Startup Message v3

> This exact message is both the Owner's task-local G2A authorization and the only substantive startup message sent to the fresh controller. Do not use it before package 003 is merged and fresh Pro supplies every placeholder.

## 1. Required operator setup

1. Wait until no known Mnemosyne write route is expected to publish during the A0 execution window.
2. Open one fresh ChatGPT conversation with the GitHub connector.
3. Select the exact UI label inserted into `<AUTHORIZED_VISIBLE_MODEL_LABEL>`.
4. Preserve the exact selected label through an operator-visible record or report it verbatim in the message.
5. Do not enable web search, Deep Research, Fable, another connector/app or private-file access.

If the exact option is absent, do not substitute it. Return to Pro.

## 2. Six exact values

Fresh Pro must fill:

```text
<RUN_DECISION_CANDIDATE_003_BLOB>
<PACKAGE_003_SOURCE_MANIFEST_BLOB>
<PROTECTED_MNEMOSYNE_MASTER>
<PROTECTED_META_AGENT_MASTER>
<AUTHORIZED_VISIBLE_MODEL_LABEL>
<OPERATOR_SELECTED_VISIBLE_MODEL_LABEL>
```

The last value is the operator's actual selected UI label, not an assistant inference. It may equal the authorized label only after both raw strings are preserved.

## 3. Single G2A/startup message

```text
@GitHub

这是本次 MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001 的 Owner G2A 授权，同时也是发给 fresh controller 的唯一正式启动消息。

确认并绑定：
- RUN-DECISION-CANDIDATE-003 blob = <RUN_DECISION_CANDIDATE_003_BLOB>
- package-003 source-manifest blob = <PACKAGE_003_SOURCE_MANIFEST_BLOB>
- execution-window protected Mnemosyne master = <PROTECTED_MNEMOSYNE_MASTER>
- execution-window protected Meta-Agent master = <PROTECTED_META_AGENT_MASTER>
- Owner 授权的可见模型标签原文 = <AUTHORIZED_VISIBLE_MODEL_LABEL>
- 我在本对话实际选择的可见模型标签原文 = <OPERATOR_SELECTED_VISIBLE_MODEL_LABEL>

只授权运行 V2-A 的 A0 sentinel。先执行完全只读 preflight：

1. 验证 candidate-003、manifest-003 及 manifest 中全部 package-003、package-002 和 load-bearing source blobs；
2. 对授权标签与实际选择标签做原文精确比较；
3. 验证上述两个 protected master refs；
4. 验证 validation master、fixture tree、完整 tlr-v1-* inventory、controller branch absence、开放 PR/等价 lineage、材料与工具边界；
5. 验证没有已知会在本次 A0 窗口内写入 Mnemosyne 的并行路线。

任一必需条件不一致、缺失或未知时，返回 BLOCKED 并停止；不得创建分支、刷新预期值、替换模型、repair package 或重试。

只有 receive PASS 后，才允许在
08822407d/mnemosyne-target-lifecycle-validation-002
从 master@e8e3296922185b4b70997c2351d6f39423f2cd4f 创建
v2a-sentinel-001-controller。

仅读取 tlr-v1-fixture-base@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6；不得修改 fixture、validation master 或任何 tlr-v1-* ref。只写 parent package 002 冻结的七个 A0 结果路径，并按 package 003 把模型授权/选择收据写入现有结果文件；不得创建第八个输出文件。

不要创建 worker/fixture branch 或 PR；不要运行 A1–A7、V2-B 或 V2-C；不要写 Mnemosyne、Meta-Agent 或任何真实目标；不要使用 Web、Deep Research、Fable、其他 app、私有材料或 external quota；失败后不要重试。

完成七文件 bundle 和 protected-ref after checks 后立即停止，把 controller branch final head、每个输出 blob/commit、两项模型标签原文及其证据、incident ledger、before/after refs 与全部限制返回给一段全新的 Pro 对话裁决。
```

## 4. Stop conditions visible to the Owner

Stop and return to Pro if the controller reports:

- candidate-003/manifest-003 or inherited blob mismatch;
- authorized label absent;
- actual selected label unavailable;
- exact model-label mismatch;
- protected-ref mismatch;
- validation dependency/ref mismatch;
- existing controller branch or competing lineage;
- expected concurrent Mnemosyne publication;
- uncertain material classification;
- inability to enforce exact branch/path boundary;
- request to edit package, use another app or access a private/real target;
- any attempt to run A1–A7 or create worker/PR.

Do not authorize a retry in the same conversation.

## 5. Backend claim limit

Even when the two visible labels match:

```yaml
backend_identity: unknown_or_not_attestable
```

The receipt proves only the bounded Owner authorization and operator-reported/observed UI selection, not the hidden served backend.
