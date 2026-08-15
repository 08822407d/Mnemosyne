# MNE-DR-005 跨仓库并发 — 操作说明

## 当前状态

- 正式任务 ID：`FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001`
- Claude Project 名称：`MNE-DR-005 跨仓库并发`
- 当前状态：任务包已经准备，但**本文件本身不要求现在启动**。
- 研究模型：Claude 界面中实际显示的 `Fable 5`。
- 模式：`Research`。
- 自动重试：禁止。
- GitHub 或其他连接服务写入：禁止。
- 本次研究只产出建议报告，不执行验证、不修改候选架构、不改任何仓库。

本包生成时核验的输入身份：

- Mnemosyne `master`：`4198d18352a071cbdcc7dc97734e65886da0621b`
- 生命周期 V1 controller 分支：`e892749fc9e242b24908f89b6a78f1c0f0bed75e`
- V1 结果包 blob：`8a5f3644707ae518182ed352174e58d1ca419067`

V1 的 fresh Pro 裁决可与本研究并行，但本研究必须把 V1 场景结论视为**临时执行者结论**，不能提前当成已接受事实。

## 什么时候可以启动

满足以下条件即可：

1. 本任务包所在的 Mnemosyne PR 已合并；
2. `tlr-v1-controller` 仍能读取清单中列出的 V1 文件；
3. 没有收到“V1 结果整体失效、需要重跑”的新通知；
4. 你明确选择使用一次 Fable 5 Research 运行。

如果 V1 的 fresh Pro 裁决已经完成，应把裁决结果一并带回后续 Mnemosyne 复核；但它不是本次 Fable 启动的强制前置条件。

## 你需要做的操作

### 1. 新建 Claude Project

在 Claude 网页版或桌面端进入 `Projects`，点击 `+ New Project`。

项目名称：

```text
MNE-DR-005 跨仓库并发
```

必须是全新 Project：

- 没有旧对话；
- 没有旧 Project knowledge；
- 不复用 MNE-DR-004、生命周期验证或其他研究 Project。

### 2. 添加两个本地文件

把以下两个文件加入 Project knowledge：

- `MNE-DR-005-最终任务.md`
- `MNE-DR-005-输入清单.yaml`

本操作说明是给你看的，不需要交给 Fable。

### 3. 从 Mnemosyne 添加文件

在 Project knowledge 中点击 `+` / `Add content`，选择 `GitHub`，从：

```text
08822407d/Mnemosyne
```

添加输入清单中列出的 14 个文件。使用 `master`。

### 4. 从生命周期验证仓库添加文件

从：

```text
08822407d/mnemosyne-target-lifecycle-validation-002
```

选择分支：

```text
tlr-v1-controller
```

添加输入清单中列出的 14 个文件。

不要加入其他 `tlr-v1-*` 场景分支，也不要加入未列出的文件。

### 5. 最小人工核对

点击 `Sync` 后，只需确认：

- Project 名称正确；
- 旧对话数为 0；
- Project knowledge 逻辑文件总数为 **30**；
- 没有误加文件；
- `Sync` 已完成。

不需要你自己验证 Git commit SHA。任务文件会要求 Fable 诚实区分：维护对话提供的版本凭据、它实际能检索到的文件内容，以及它不能从 Project knowledge 独立证明的 Git 历史。

### 6. 选择运行表面

打开该 Project 中第一段也是唯一计划内的研究对话：

- 模型：`Fable 5`；
- 若界面有独立思考强度：选择最高可见档，并记下界面原文；
- 模式：`Research`；
- `Web search`：开启；
- 对话层 `GitHub` 和其他 connectors：关闭。

Project knowledge 中的文件是输入；不要启用 live GitHub 连接器。

### 7. 只发送一次启动消息

不要先发送“能否看见文件”的测试消息。直接发送：

```text
请严格执行 Project knowledge 中的《MNE-DR-005-最终任务.md》。

任务文件是本次研究唯一的任务指令来源；《MNE-DR-005-输入清单.yaml》和其余文件只是按任务文件规定角色使用的输入证据。

先完成“输入资料核验阶段”。核验失败立即停止，并只返回失败原因和完整核验结果。只有核验通过后，才进入正式研究阶段。

输入核验完成前不得进行外部网页研究。不得写入 GitHub 或任何连接服务，不得执行验证，不得修改或采用候选架构。失败、中断、模型切换或资料访问异常时不要自动重试。
```

### 8. 出现以下情况就停止

- 30 个逻辑文件缺失或多出；
- 无法读取 `tlr-v1-controller`；
- 输入核验前开始网页研究或实质结论；
- 把 V1 provisional pass 写成已获 Pro/Owner 接受；
- Project knowledge 丢失；
- 明确发生模型 fallback；
- 要求启用额外连接器或写 GitHub；
- Research 中断或额度不足；
- 任务试图执行新验证、修改架构或处理真实目标。

停止后不要重跑同一配置。

### 9. 结果返回

带回 Mnemosyne Pro 对话：

1. 完整最终报告；
2. 完整输入核验结果；
3. Claude 界面实际显示的模型、思考强度（若有）和 Research 状态；
4. 是否观察到 Project Search/RAG；
5. 是否出现 fallback、额度警告、中断或其他异常；
6. 如果 Claude 提供报告导出，附上同一报告的 Markdown / Word / PDF 导出。

不要自行判断报告是否合格，也不要为了生成文件再发第二次 Research。
