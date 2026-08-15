# V1 Staged Operator Flow and Startup Messages

> Prepared operator flow only. **Do not run** until MNEMOSYNE-212 is merged and the Owner has explicitly confirmed `MNE-TARGET-LIFECYCLE-V1-RUN-DECISION-CANDIDATE-001`, producing an exact V1 authorization record. These messages do not themselves authorize V1, repository writes, model switching or quota use.

```yaml
execution_package_id: MNE-TARGET-LIFECYCLE-V1-EXECUTION-PACKAGE-001
file_role: staged_operator_flow_and_startup_messages
status: prepared_do_not_run
base_display_name: MNE-DR-003 生命周期验证
canonical_run_id: MNE-TARGET-LIFECYCLE-V1-001
```

## 1. Execution intent

```yaml
execution_intent:
  response_role: ANALYSIS_AND_PREPARATION
  task_id: MNE-TARGET-LIFECYCLE-V1-001
  execution_disposition: RUN_AFTER_GATE_OPTIONAL
  prerequisite_gates:
    - MNEMOSYNE_212_Ready_PR_merged
    - Owner_confirms_MNE_TARGET_LIFECYCLE_V1_RUN_DECISION_CANDIDATE_001
    - exact_V1_authorization_record_exists_on_latest_Mnemosyne_master
  external_execution_or_quota_authorized: false_until_gate
```

After those gates, the authorized flow uses six named conversations:

| Order | Chat/UI name | Model class | Reuse? |
|---:|---|---|---|
| 1 | `MNE-DR-003 Controller` | next-tier | keep open; return for closeout |
| 2 | `MNE-DR-003 Core` | next-tier | separate chat |
| 3 | `MNE-DR-003 S7` | next-tier | separate chat |
| 4 | `MNE-DR-003 S8` | next-tier | **mandatory fresh chat** |
| 5 | `MNE-DR-003 S11` | next-tier | separate chat |
| 6 | `MNE-DR-003 Review` | **Pro/frontier** | **mandatory fresh chat** |

Recommended next-tier visible selection, only if it remains available at launch:

```text
gpt-5.6 sol extra high
```

Always record the actual displayed model/mode and any separately displayed reasoning setting verbatim in each chat. Do not infer backend identity.

## 2. Common preparation

Before launching any V1 chat:

1. verify the exact V1 Owner authorization exists on execution-time latest `08822407d/Mnemosyne@master`;
2. verify `08822407d/mnemosyne-target-lifecycle-validation-002@master` still equals the authorized pinned base `e8e3296922185b4b70997c2351d6f39423f2cd4f` before controller writes begin;
3. keep GitHub connected; a separate ChatGPT repository-sync selection is not required when the connector can already resolve the repository, but each chat must perform its own access preflight;
4. do not attach private files or complete old conversations;
5. do not enable Web, Deep Research, Fable or other connected apps;
6. do not launch S8 in a chat that has seen S7 or the exact synthetic v2 migration facts;
7. do not delete V1 task branches until fresh Pro adjudication releases them.

If any precondition fails, stop before repository write.

---

# Cell 0 — `MNE-DR-003 Controller`

## 3. Controller launch message

```text
@GitHub 请执行已获 Owner 授权的 MNE-TARGET-LIFECYCLE-V1-001 Controller / Fixture 阶段。

从执行时最新的 08822407d/Mnemosyne@master 读取并严格执行：

1. notes/target-agent-container-evolution-and-dependency-model-candidate-v0.2.md
2. notes/validation-designs/target-agent-container-evolution-and-dependency-model-validation-v0.2.md
3. notes/target-agent-lifecycle-validation-package-v0.2/README.md
4. notes/target-agent-lifecycle-validation-package-v0.2/01-synthetic-fixture-and-scenario-contracts.md
5. notes/target-agent-lifecycle-validation-package-v0.2/02-next-tier-executor-taskbook.md
6. notes/target-agent-lifecycle-validation-package-v0.2/03-mechanical-checks-and-rubric.md
7. notes/target-agent-lifecycle-validation-package-v0.2/04-run-manifest-and-result-template.md
8. notes/validation-adjudications/MNE-TARGET-LIFECYCLE-V0-ADJUDICATION-001.md
9. notes/validation-run-decisions/MNE-TARGET-LIFECYCLE-V1-RUN-DECISION-CANDIDATE-001.md
10. Owner 已确认的 MNE-TARGET-LIFECYCLE-V1-RUN-AUTHORIZATION-001
11. notes/target-agent-lifecycle-v1-execution-package-001/README.md
12. notes/target-agent-lifecycle-v1-execution-package-001/00-controller-fixture-and-branch-contract.md
13. notes/target-agent-lifecycle-v1-execution-package-001/05-mechanical-closeout-and-return.md
14. notes/target-agent-lifecycle-v1-execution-package-001/07-integrity-checklist.md

当前界面显示的模型/模式原文是：<启动时原样填写>。
如果另有独立的推理设置，也原样填写：<填写或写无独立设置>。

第一轮只返回 v1_controller_receive，列出：
- 所有 ID 与 exact source commit/blob；
- Owner V1 authorization ref 和 selected scenarios；
- synthetic repository、visibility、当前 master 与授权 pinned base 是否一致；
- V0 evidence 是否完整且未变；
- 计划创建的 controller / fixture / task branches；
- Mnemosyne 与 Meta-Agent before refs；
- S8 隔离方法；
- allowed/prohibited writes；
- product surface、可见模型/模式原文、backend unknown_or_not_attestable；
- disposition PASS 或 BLOCKED。

若 receive 通过，才创建 controller、fixture 和 execution-package 指定的 task branches，生成冻结 fixture、任务合同、S8 sanitized input 和 controller receipt。不要运行任何场景；不要创建 PR；不要合并任务分支；不要写 Mnemosyne、Meta-Agent 或真实目标。

完成 controller setup 后返回所有 branch/base/head/tree/blob 身份和每个后续 cell 的 exact launch input refs，然后停止并等待各 cell 结果。
```

Controller receive 通过标准：V1 授权、Mnemosyne 输入、V0 pinned base、可见性、材料、branch map、no-write baseline 和 S8 firewall 全部完整。

---

# Cell 1 — `MNE-DR-003 Core`

## 4. Core launch message

仅在 Controller 返回 `PASS` 并给出 exact fixture/task refs 后，在单独 chat 中发送：

```text
@GitHub 请执行 MNE-TARGET-LIFECYCLE-V1-001 的 Core Cell，只运行 S1、S2、S3、S4、S5、S6、S9。

从执行时最新的 08822407d/Mnemosyne@master 读取：
1. candidate v0.2
2. validation v0.2
3. frozen package README、01、02、03、04
4. MNE-TARGET-LIFECYCLE-V1-RUN-AUTHORIZATION-001
5. notes/target-agent-lifecycle-v1-execution-package-001/README.md
6. notes/target-agent-lifecycle-v1-execution-package-001/00-controller-fixture-and-branch-contract.md
7. notes/target-agent-lifecycle-v1-execution-package-001/01-core-cell-s1-s6-s9.md

并读取 Controller 返回的 exact controller receipt、fixture commit、branch/task map 和本 cell 输入 refs。

当前界面模型/模式原文：<启动时原样填写>。

第一轮只返回 core_cell_receive，核验 selected scenarios、每个 task ID/branch/base/write set、权限、材料、禁止仓库和输出合同。任何不一致只返回 BLOCKED，不写入。

Receive 通过后按冻结合同执行 S1、S2、S3、S4、S5、S6、S9；每个 task 只写自己的 canonical branch，保存 exact input/output/blob/commit、失败和重试。不要运行 S7、S8、S10、S11；不要创建 PR；不要写真实仓库；不要修改架构。

完成后返回完整 core_cell_result 和所有 branch/result refs，停止。
```

---

# Cell 2 — `MNE-DR-003 S7`

## 5. Positive documentation launch message

在单独 chat 中发送：

```text
@GitHub 请执行 MNE-TARGET-LIFECYCLE-V1-001 的 S7 Positive Documentation Cell。

从执行时最新的 08822407d/Mnemosyne@master 读取：
1. candidate v0.2
2. validation v0.2
3. frozen package README、01、02、03、04
4. MNE-TARGET-LIFECYCLE-V1-RUN-AUTHORIZATION-001
5. notes/target-agent-lifecycle-v1-execution-package-001/README.md
6. notes/target-agent-lifecycle-v1-execution-package-001/00-controller-fixture-and-branch-contract.md
7. notes/target-agent-lifecycle-v1-execution-package-001/02-positive-documentation-cell-s7.md

并读取 Controller 返回的 exact fixture、S7 library/Alpha branch refs 和 task inputs。

当前界面模型/模式原文：<启动时原样填写>。

第一轮只返回 s7_cell_receive，核验两个 task lineage、依赖顺序、write sets、Owner rebuild trigger、输出和禁止项。任何不一致只返回 BLOCKED，不写入。

Receive 通过后先在 S7 library branch 完成 CommonLib v2 的 API、测试、人类版变化说明、Agent 版迁移说明和文档总览；机械核验充分后，才从该 library final commit 创建/使用已分配的 Alpha migration branch，执行 Owner 触发的 Alpha 按需迁移。

不要运行 S8；不要把 S7 输出发送给 S8；不要创建消费者总数据库；不要修改 Beta、共享对象、真实仓库或架构；不要创建 PR。

完成后返回完整 positive_documentation_cell_result、两个 branch head 和所有文档/代码/测试/result blob+commit identities，停止。
```

---

# Cell 3 — `MNE-DR-003 S8`（必须全新对话）

## 6. Fresh negative documentation launch message

创建一段**从未见过 S7 或具体 v2 迁移事实**的新对话。不要把本文件其他 cell 的正文、S7 输出或 frozen package `01` 提供给它。只发送下面的消息，并填写 Controller 提供的 sanitized refs：

```text
@GitHub 请执行 MNE-TARGET-LIFECYCLE-V1-001 的 S8 Fresh Negative Documentation Cell。

这是全新隔离对话。你不得读取或搜索 S7 branch/output、充分的 Agent 迁移说明、frozen package 的具体 v2 contract 段落或其他包含隐藏迁移答案的材料。

只允许从执行时最新的 08822407d/Mnemosyne@master 读取：
1. MNE-TARGET-LIFECYCLE-V1-RUN-AUTHORIZATION-001
2. notes/target-agent-lifecycle-v1-execution-package-001/README.md
3. notes/target-agent-lifecycle-v1-execution-package-001/03-fresh-negative-documentation-cell-s8.md

只允许从 08822407d/mnemosyne-target-lifecycle-validation-002 读取 Controller 指定的：
- S8 branch：tlr-v1-s8-insufficient-docs
- exact base/head：<Controller 填写>
- sanitized worker input refs：<Controller 填写>
- Alpha 当前 v1 项目文件；
- S8 isolation receipt。

当前界面模型/模式原文：<启动时原样填写>。

第一轮只返回 s8_fresh_receive，声明：
- 当前对话未接收 S7 或隐藏迁移答案；
- exact allowed files/branch；
- forbidden sources；
- Alpha write prohibition；
- isolation receipt PASS/BLOCKED；
- backend unknown_or_not_attestable。

若隔离不能证明，只返回 S8_RECEIVE_BLOCKED，不做写入。

通过后判断现有变化说明是否足以安全迁移 Alpha。不得根据版本号、惯例、名称或外部知识猜测新合同。信息不足时应停止，说明缺少哪些信息类别，并且只写 run-evidence/S8/output/。不得修改 Alpha、CommonLib 或其他路径；不得读取其他 branch；不得创建 PR。

完成后返回完整 negative_documentation_cell_result、Alpha before/after unchanged 证明、输出 blob+commit 和任何 contamination/invention finding，然后停止。
```

如果 S8 对话受到污染，不得在同一对话重试；保留失败证据，另行交 Pro 判断是否授权 clean rerun。

---

# Cell 4 — `MNE-DR-003 S11`

## 7. Backup/restore launch message

在单独 chat 中发送：

```text
@GitHub 请执行 MNE-TARGET-LIFECYCLE-V1-001 的 S11 Synthetic Backup and Restore Cell。

从执行时最新的 08822407d/Mnemosyne@master 读取：
1. candidate v0.2 backup section
2. validation v0.2 S11 section
3. frozen package README、01、02、03、04
4. MNE-TARGET-LIFECYCLE-V1-RUN-AUTHORIZATION-001
5. notes/target-agent-lifecycle-v1-execution-package-001/README.md
6. notes/target-agent-lifecycle-v1-execution-package-001/00-controller-fixture-and-branch-contract.md
7. notes/target-agent-lifecycle-v1-execution-package-001/04-backup-restore-cell-s11.md

并读取 Controller 返回的 exact fixture source and S11 branch refs。

当前界面模型/模式原文：<启动时原样填写>。

第一轮只返回 s11_cell_receive，核验 source commit/tree/target identity、branch/write set、synthetic-only material、snapshot and restore contract。任何缺失只返回 BLOCKED，不写入。

通过后只在 S11 canonical branch 创建 source-identified backup A/B，模拟 primary loss 与 backup A failure，并从 backup B 恢复 Alpha。验证 restored identity 和 authority；保存每次尝试、failure、snapshot、restore blob+commit。不要配置真实备份，不要写任何真实仓库，不要创建 PR。

完成后返回完整 backup_restore_cell_result，然后停止。
```

---

# Cell 5 — 回到 `MNE-DR-003 Controller`

## 8. Mechanical closeout continuation message

所有 selected cells 已结束后，回到原 Controller chat，提供每个 cell 的完整最终回复或 exact result refs，然后发送：

```text
@GitHub 现在执行 MNE-TARGET-LIFECYCLE-V1-001 的 Mechanical Closeout。

已返回的 exact cell results：
- Core：<填写 refs>
- S7：<填写 refs>
- S8：<填写 refs>
- S11：<填写 refs>

严格执行：
- notes/target-agent-lifecycle-v1-execution-package-001/05-mechanical-closeout-and-return.md
- frozen package 03-mechanical-checks-and-rubric.md
- frozen package 04-run-manifest-and-result-template.md

先核验所有 branch/base/head/blob/commit、S8 isolation、incident/retry 和 selected scenario completeness。再执行 M0–M11 适用检查、declared-vs-actual write-set 汇总，以及 Mnemosyne/Meta-Agent exact before/after no-write comparison。

不得修复 scenario 语义、运行 S10/V2、重跑失败 cell、写 Mnemosyne/Meta-Agent/真实目标、创建 PR 或作出全局架构接受结论。

完成后把完整 V1 result bundle 写入 synthetic repository 的授权路径，并在最终回复正文中给出完整 decision-relevant summary 和 fresh Pro return package，然后停止。
```

---

# Cell 6 — `MNE-DR-003 Review`（必须全新 Pro 对话）

## 9. Fresh Pro adjudication launch message

创建一段没有执行任何 V1 cell 的新 Pro 对话。加载 GitHub 后发送：

```text
@GitHub 请作为 fresh Pro adjudicator 复核 MNE-TARGET-LIFECYCLE-V1-001。

从执行时最新的 08822407d/Mnemosyne@master 读取：
1. candidate v0.2
2. validation v0.2
3. frozen package README、03、04
4. MNE-TARGET-LIFECYCLE-V0-ADJUDICATION-001
5. MNE-TARGET-LIFECYCLE-V1-RUN-DECISION-CANDIDATE-001
6. MNE-TARGET-LIFECYCLE-V1-RUN-AUTHORIZATION-001
7. notes/target-agent-lifecycle-v1-execution-package-001/README.md
8. notes/target-agent-lifecycle-v1-execution-package-001/05-mechanical-closeout-and-return.md

然后只从 08822407d/mnemosyne-target-lifecycle-validation-002 读取 Controller return package 列出的 exact V1 result bundle、cell results、task branches/commits/blobs 和争议所必需的具体文件。不要先 broad-read 全仓库。

第一轮返回 v1_adjudication_receive，列出 exact inputs、review criteria、context independence、缺失项和 PASS/BLOCKED。

通过后区分 candidate defect、validation protocol defect、executor defect、contamination、missing evidence 和 noncritical observation；复核 S8 firewall、no-write proof、S11 restore、全部 baseline-critical scenarios 和 TLR-03/TLR-04 deferral fidelity。

选择冻结 package 允许的一个 Pro disposition，并清楚说明证据、限制、建议 amendments（未采用）和需要 Owner 决定的事项。

不得修改 candidate/validation/execution source/Meta-Agent/真实目标；不得运行 rerun、S10、V2、Deep Research 或 Fable；不得把结果写回 Mnemosyne，除非收到另行明确的 repository-write authorization。
```

## 10. Return and stop contract

The fresh Pro response returns to the Owner/Mnemosyne maintenance route with:

- one exact Pro disposition;
- candidate/protocol/executor findings;
- scenario summary and critical evidence;
- unresolved disputes;
- proposed non-adopted amendments;
- whether an independent heterogeneous review would add non-duplicative value before global acceptance;
- the exact Owner architecture decision now required.

No V1 cell, controller or Pro adjudicator may proceed to architecture adoption, real target migration, S10, V2, cleanup or Mnemosyne ingestion without the later explicit gates.