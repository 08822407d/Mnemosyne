# V2-A A1 — Operator Flow and Startup Messages

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-OPERATOR-FLOW-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-001
status: templates_not_authorization
```

Do not use these messages until this package is merged, post-merge identities are verified, a Pro execution-time review supplies every placeholder, and the Owner explicitly issues G2A.

## 1. Required operator flow

1. Ensure no known Mnemosyne or Meta-Agent write route is expected during the A1 window.
2. Open one fresh controller conversation with only GitHub enabled.
3. Select the exact controller label bound by G2A.
4. Send the filled controller G2A/startup message once.
5. If controller preflight blocks, stop; do not launch workers.
6. If controller creates the three initial branches and returns the already frozen worker messages, open two fresh worker conversations.
7. Select the exact Alpha label and send the Alpha message once.
8. Select the exact Beta label and send the Beta message once.
9. The messages must have been frozen before either worker result. The workers may be launched sequentially; no wall-clock concurrency claim follows.
10. Return both complete worker outputs to the original controller conversation in one message without editing them.
11. Let the controller independently verify GitHub, construct both order branches, write the ten-file bundle and stop.
12. Send the full controller result to a fresh Pro adjudicator. Do not create a PR or clean branches.

If any selected visible label is absent or differs from the authorized raw string, do not substitute a near match. Return to Pro.

## 2. Dynamic values supplied by future Pro/Owner

```text
<RUN_DECISION_CANDIDATE_001_BLOB>
<PACKAGE_SOURCE_MANIFEST_001_BLOB>
<PROTECTED_MNEMOSYNE_MASTER>
<PROTECTED_META_AGENT_MASTER>
<CONTROLLER_AUTHORIZED_VISIBLE_LABEL>
<CONTROLLER_OPERATOR_SELECTED_VISIBLE_LABEL>
<ALPHA_AUTHORIZED_VISIBLE_LABEL>
<ALPHA_OPERATOR_SELECTED_VISIBLE_LABEL>
<BETA_AUTHORIZED_VISIBLE_LABEL>
<BETA_OPERATOR_SELECTED_VISIBLE_LABEL>
```

The three `operator_selected` values are current operator-observed/reported UI labels, not assistant inferences.

## 3. Controller G2A and startup message

```text
@GitHub

这是 MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001 的 Owner G2A 授权，也是 fresh A1 controller 的唯一正式启动消息。

绑定：
- run-decision-candidate-001 blob = <RUN_DECISION_CANDIDATE_001_BLOB>
- package source-manifest-001 blob = <PACKAGE_SOURCE_MANIFEST_001_BLOB>
- protected Mnemosyne master = <PROTECTED_MNEMOSYNE_MASTER>
- protected Meta-Agent master = <PROTECTED_META_AGENT_MASTER>
- controller Owner-authorized visible label = <CONTROLLER_AUTHORIZED_VISIBLE_LABEL>
- controller operator-selected visible label = <CONTROLLER_OPERATOR_SELECTED_VISIBLE_LABEL>
- Alpha Owner-authorized visible label = <ALPHA_AUTHORIZED_VISIBLE_LABEL>
- Alpha operator-selected visible label = <ALPHA_OPERATOR_SELECTED_VISIBLE_LABEL>
- Beta Owner-authorized visible label = <BETA_AUTHORIZED_VISIBLE_LABEL>
- Beta operator-selected visible label = <BETA_OPERATOR_SELECTED_VISIBLE_LABEL>

只授权执行 V2-A 的 A1 positive independent pair；不授权 A2–A7、V2-B、V2-C 或真实目标。

先执行完全只读 preflight，严格读取并执行 package 001：
notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/

必须验证 source/package blobs、A0 accepted state、protected refs、validation master、fixture、A0 controller head、16 个 tlr-v1-* refs、完整 branch/PR inventory、五个 A1 branch absence、材料边界、工具能力和三组模型标签原文。

任一必需条件不一致、缺失或未知时，返回 CONTROLLER_BLOCKED 并停止；不得创建分支、刷新预期值、修包、换模型或重试。

只有 preflight PASS 后，才允许创建：
- v2a-a1-001-controller from validation master@e8e3296922185b4b70997c2351d6f39423f2cd4f
- v2a-a1-001-alpha from fixture@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
- v2a-a1-001-beta from fixture@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6

先在 controller branch 写入 package 冻结的 00、01、02 三个 pre-worker 输出，并把本消息下面两份 worker message 原文完整保存进 02。两份 worker message 必须在任何 worker result 返回前冻结。

然后停止主动工作，把 package 中的 Alpha/Beta worker message 交给 Owner。不要在后台监控，不要自行执行 worker 任务。

Owner 返回两份 worker 输出后，独立读取 GitHub 验证。只有两名 worker 都精确 PASS，才创建：
- v2a-a1-001-order-alpha-beta
- v2a-a1-001-order-beta-alpha

严格按 controller task 构造两个顺序；两者最终 root tree 必须都等于 2b919544aecfbd1634e5f136af22571f2e8d9fd0。只写 controller branch 冻结的十个结果路径，不得创建第十一个输出。

不得创建 PR；不得修改 validation master、fixture、任何 tlr-v1-*、v2a-sentinel-001-controller、Mnemosyne、Meta-Agent 或真实目标；不得使用 Web、Deep Research、Fable、其他 app、私有材料或 external quota；失败后不要重试。

完成 final bundle 和 after checks 后停止，并把所有 branch heads、commits、trees、blobs、模型收据、protected refs、incident ledger 与限制返回给 fresh Pro 裁决。
```

## 4. Alpha worker startup message

The controller must preserve and return this exact filled message; it may not rewrite it after Beta/Alpha runtime evidence appears.

```text
@GitHub

这是 MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001 的 Alpha worker 授权。

绑定：
- task = MNE-V2A-A1-ALPHA-001
- repository = 08822407d/mnemosyne-target-lifecycle-validation-002
- branch = v2a-a1-001-alpha
- required current branch head = 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
- Owner-authorized visible label = <ALPHA_AUTHORIZED_VISIBLE_LABEL>
- operator-selected visible label = <ALPHA_OPERATOR_SELECTED_VISIBLE_LABEL>

严格执行：
notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/03-alpha-worker-task.md

只允许在预创建的 Alpha branch 上，用一个 commit 写入两个冻结 Alpha 路径。不得创建 branch/PR/evidence file；不得读取 Beta final head/output；不得写任何其他路径或仓库；不得使用 Web、Deep Research、Fable、其他 app 或 external quota；失败后不得重试。

完成后返回 exact head/tree/blob/diff/model/incident receipt 并停止。controller 会独立复核。
```

## 5. Beta worker startup message

```text
@GitHub

这是 MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001 的 Beta worker 授权。

绑定：
- task = MNE-V2A-A1-BETA-001
- repository = 08822407d/mnemosyne-target-lifecycle-validation-002
- branch = v2a-a1-001-beta
- required current branch head = 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
- Owner-authorized visible label = <BETA_AUTHORIZED_VISIBLE_LABEL>
- operator-selected visible label = <BETA_OPERATOR_SELECTED_VISIBLE_LABEL>

严格执行：
notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/04-beta-worker-task.md

只允许在预创建的 Beta branch 上，用一个 commit 写入两个冻结 Beta 路径。不得创建 branch/PR/evidence file；不得读取 Alpha final head/output；不得写任何其他路径或仓库；不得使用 Web、Deep Research、Fable、其他 app 或 external quota；失败后不得重试。

完成后返回 exact head/tree/blob/diff/model/incident receipt 并停止。controller 会独立复核。
```

## 6. Worker-return message to controller

After both workers stop, the Owner sends one message:

```text
Alpha 和 Beta worker 均已停止。以下是两份完整原始输出；不得把其中自报 PASS 当作权威，请按 package 独立读取 GitHub 后继续或停止。

--- ALPHA RAW OUTPUT ---
<PASTE_COMPLETE_ALPHA_OUTPUT>

--- BETA RAW OUTPUT ---
<PASTE_COMPLETE_BETA_OUTPUT>
```

If one worker is blocked/failed, paste that exact output and state that the other worker was or was not launched. Do not ask the controller to repair or retry.

## 7. Stop conditions visible to the Owner

Return to Pro without retry when any conversation reports:

- source/manifest/ref/model/branch mismatch;
- controller branch creation ambiguity;
- worker branch not at fixture base;
- unexpected path/tree/blob/commit count;
- peer runtime-output dependency;
- order tree mismatch;
- protected ref movement;
- request to create a PR, repair package/fixture or run another cell;
- inability to enforce exact tool and branch scope.
