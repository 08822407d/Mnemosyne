# V2-A A1 Package 002 — Revised Operator Flow and Startup Messages

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-OPERATOR-FLOW-002
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-002
status: templates_not_authorization
```

Do not use these messages until package 002 is merged, exact post-merge identities are verified, a fresh Pro execution-time review passes, and the Owner explicitly issues A1 G2A.

## 1. Repaired operator flow

1. Confirm no known Mnemosyne or Meta-Agent route will move protected refs during the bounded A1 window.
2. Open one fresh controller conversation with only GitHub enabled.
3. Select the exact controller label authorized by the Owner and record the current UI raw string.
4. Send the filled controller G2A/startup message once.
5. If controller preflight blocks, stop; do not launch workers.
6. If preflight passes, controller creates the controller, Alpha and Beta branches, writes `00`, `01` and `02`, freezes both immutable worker task payloads, then returns two worker launch templates.
7. Open one fresh Alpha conversation. Select the Owner-authorized Alpha label and record the actual current UI raw string.
8. Fill only `<ALPHA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH>` in the already frozen Alpha runtime wrapper and send it once.
9. If Alpha blocks or fails, do not open or launch Beta. Return Alpha's complete raw output to controller and stop.
10. If Alpha completes, open one fresh Beta conversation. Select the Owner-authorized Beta label and record the actual current UI raw string.
11. Fill only `<BETA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH>` in the already frozen Beta runtime wrapper and send it once.
12. Return both complete raw worker outputs to the original controller conversation in one message without editing them.
13. Controller independently verifies GitHub. Only if both workers exactly pass may it construct the two order branches, complete the ten-file result bundle and stop.
14. Send the full controller result to a fresh Pro adjudicator. Do not create a PR or clean branches.

The immutable Alpha/Beta task payloads and runtime-wrapper templates must both be preserved by the controller before Alpha is launched. A runtime selected-label field is evidence about the new worker conversation; it does not revise the task.

## 2. Dynamic fields supplied by future Pro/Owner

### Controller G2A fields

```text
<RUN_DECISION_CANDIDATE_002_BLOB>
<PACKAGE_SOURCE_MANIFEST_002_BLOB>
<PROTECTED_MNEMOSYNE_MASTER>
<PROTECTED_META_AGENT_MASTER>
<CONTROLLER_OWNER_AUTHORIZED_VISIBLE_LABEL>
<CONTROLLER_OPERATOR_SELECTED_VISIBLE_LABEL>
<ALPHA_OWNER_AUTHORIZED_VISIBLE_LABEL>
<BETA_OWNER_AUTHORIZED_VISIBLE_LABEL>
```

### Worker-launch fields

These do not exist until their specific worker conversations are opened:

```text
<ALPHA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH>
<BETA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH>
```

They may come only from current operator-observed or operator-reported UI evidence for that exact conversation.

## 3. Controller G2A and startup message

```text
@GitHub

这是 MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001 的 Owner G2A 授权，也是 fresh A1 controller 的唯一正式启动消息。

控制身份：
- run-decision-candidate-002 blob = <RUN_DECISION_CANDIDATE_002_BLOB>
- package-002 source-manifest blob = <PACKAGE_SOURCE_MANIFEST_002_BLOB>
- inherited candidate-001 blob = bb140196a38d8b14f6eba9e2175cd45744efb23b
- inherited package-001 source-manifest blob = 12a480449b1dac45cd265864a812f399d19ec15c
- protected Mnemosyne master = <PROTECTED_MNEMOSYNE_MASTER>
- protected Meta-Agent master = <PROTECTED_META_AGENT_MASTER>

模型授权与当前证据：
- controller Owner-authorized visible label = <CONTROLLER_OWNER_AUTHORIZED_VISIBLE_LABEL>
- controller operator-selected visible label = <CONTROLLER_OPERATOR_SELECTED_VISIBLE_LABEL>
- Alpha Owner-authorized visible label = <ALPHA_OWNER_AUTHORIZED_VISIBLE_LABEL>
- Alpha operator-selected visible label = NOT_YET_OBSERVED_UNTIL_ALPHA_LAUNCH
- Beta Owner-authorized visible label = <BETA_OWNER_AUTHORIZED_VISIBLE_LABEL>
- Beta operator-selected visible label = NOT_YET_OBSERVED_UNTIL_BETA_LAUNCH

只授权执行 V2-A 的 A1 positive independent pair；不授权 A2–A7、V2-B、V2-C 或真实目标。

先执行完全只读 preflight，严格读取并执行：
- MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-002
- notes/cross-repository-safe-concurrency-v2a-a1-execution-package-002/
- package 002 明确继承的 package 001 exact path/blob 内容。

必须验证 source/package blobs、A0 accepted state、protected refs、validation master、fixture、A0 controller head、16 个 tlr-v1-* refs、完整 branch/PR inventory、五个 A1 branch absence、材料边界、工具能力、controller 标签原文和 Alpha/Beta authorized 标签。

不得要求或推断 Alpha/Beta selected label 已经存在。它们只在各 worker 对话实际打开时绑定。

任一必需条件不一致、缺失或未知时，返回 CONTROLLER_BLOCKED 并停止；不得创建分支、刷新预期值、修包、换模型或重试。

只有 preflight PASS 后，才允许创建：
- v2a-a1-001-controller from validation master@e8e3296922185b4b70997c2351d6f39423f2cd4f
- v2a-a1-001-alpha from fixture@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
- v2a-a1-001-beta from fixture@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6

在 controller branch 写入 package 001 冻结的 00、01、02 三个 pre-worker 输出。按 package 002 记录：
- controller 的 authorized/selected exact match；
- Alpha/Beta authorized labels；
- Alpha/Beta selected labels = runtime_pending；
- package 001 的 Alpha/Beta immutable task path/blob；
- 本消息下方两份 worker runtime-wrapper template 原文。

两份 immutable task payload 与 wrapper template 必须在任何 worker result 返回前冻结。然后停止主动工作，把两份 worker launch payload 交给 Owner；不要自行打开或执行 worker。

Owner 返回 worker 输出后，独立读取 GitHub 验证。只有两名 worker 都精确 PASS，才创建：
- v2a-a1-001-order-alpha-beta
- v2a-a1-001-order-beta-alpha

严格按 package 001 controller task 构造两个顺序；两者最终 root tree 必须都等于 2b919544aecfbd1634e5f136af22571f2e8d9fd0。只写 controller branch 冻结的十个结果路径，不得创建第十一个输出。

不得创建 PR；不得修改 validation master、fixture、任何 tlr-v1-*、v2a-sentinel-001-controller、Mnemosyne、Meta-Agent 或真实目标；不得使用 Web、Deep Research、Fable、其他 app、私有材料或 external quota；失败后不要重试。

完成 final bundle 和 after checks 后停止，并把所有 branch heads、commits、trees、blobs、三组模型收据、protected refs、incident ledger 与限制返回给 fresh Pro 裁决。
```

## 4. Frozen Alpha runtime-wrapper template

The controller preserves this template before Alpha begins. The operator may replace only the selected-label placeholder at actual launch.

```text
@GitHub

这是 MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001 的 Alpha worker 授权与运行时模型收据。

不可变任务绑定：
- task = MNE-V2A-A1-ALPHA-001
- task contract path = notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/03-alpha-worker-task.md
- task contract blob = 9cb67f6e8b007941779326509db0b2d07fd035dd
- repository = 08822407d/mnemosyne-target-lifecycle-validation-002
- branch = v2a-a1-001-alpha
- required current branch head = 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
- Owner-authorized visible label = <ALPHA_OWNER_AUTHORIZED_VISIBLE_LABEL>

本次 worker 对话的动态收据：
- operator-selected visible label = <ALPHA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH>

在任何写入前，先逐字比较 Owner-authorized 与 operator-selected label。缺失、未知或不一致时返回 WORKER_BLOCKED_BEFORE_WRITE 并停止，不得写仓库、换模型或重试。

匹配后，严格执行上述 immutable task contract。只允许在预创建的 Alpha branch 上，用一个 commit 写入两个冻结 Alpha 路径。不得创建 branch/PR/evidence file；不得读取 Beta final head/output；不得写任何其他路径或仓库；不得使用 Web、Deep Research、Fable、其他 app 或 external quota；失败后不得重试。

完成后返回 exact head/tree/blob/diff/model receipt/incident receipt 并停止。controller 会独立复核。
```

## 5. Frozen Beta runtime-wrapper template

The controller preserves this template before Alpha begins. The operator may replace only the selected-label placeholder at actual Beta launch.

```text
@GitHub

这是 MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001 的 Beta worker 授权与运行时模型收据。

不可变任务绑定：
- task = MNE-V2A-A1-BETA-001
- task contract path = notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/04-beta-worker-task.md
- task contract blob = 9544963bc40face1eb3caca190de6fe5f96802f5
- repository = 08822407d/mnemosyne-target-lifecycle-validation-002
- branch = v2a-a1-001-beta
- required current branch head = 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
- Owner-authorized visible label = <BETA_OWNER_AUTHORIZED_VISIBLE_LABEL>

本次 worker 对话的动态收据：
- operator-selected visible label = <BETA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH>

在任何写入前，先逐字比较 Owner-authorized 与 operator-selected label。缺失、未知或不一致时返回 WORKER_BLOCKED_BEFORE_WRITE 并停止，不得写仓库、换模型或重试。

匹配后，严格执行上述 immutable task contract。只允许在预创建的 Beta branch 上，用一个 commit 写入两个冻结 Beta 路径。不得创建 branch/PR/evidence file；不得读取 Alpha final head/output；不得写任何其他路径或仓库；不得使用 Web、Deep Research、Fable、其他 app 或 external quota；失败后不得重试。

完成后返回 exact head/tree/blob/diff/model receipt/incident receipt 并停止。controller 会独立复核。
```

## 6. Worker-return messages to controller

### Alpha blocked or failed

```text
Alpha worker 已停止。以下是完整原始输出。不要启动或等待 Beta，不得把 worker 自报结论当作权威；请按 package 002 记录 partial/blocked state 并停止。

--- ALPHA RAW OUTPUT ---
<PASTE_COMPLETE_ALPHA_OUTPUT>

Beta worker launched: false
```

### Both workers completed or Beta stopped after Alpha

```text
Alpha 和 Beta worker 均已停止。以下是两份完整原始输出；不得把其中自报 PASS 当作权威，请按 package 独立读取 GitHub 后继续或停止。

--- ALPHA RAW OUTPUT ---
<PASTE_COMPLETE_ALPHA_OUTPUT>

--- BETA RAW OUTPUT ---
<PASTE_COMPLETE_BETA_OUTPUT>
```

If Beta is blocked/failed, controller preserves Alpha's committed evidence but must not construct order branches.

## 7. Owner-visible stop conditions

Return to Pro without retry when any conversation reports:

- source/manifest/ref/branch mismatch;
- controller label mismatch;
- missing worker authorized label;
- worker selected-label mismatch or uncertainty;
- controller branch creation ambiguity;
- worker branch not at fixture base;
- unexpected path/tree/blob/commit count;
- peer runtime-output dependency;
- order tree mismatch;
- protected ref movement;
- request to create a PR, repair package/fixture or run another cell;
- inability to enforce exact tool and branch scope.
