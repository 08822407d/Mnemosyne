# MNE-DR-005 跨仓库并发 — Fable 5 独立研究任务

## 任务身份

- 正式任务 ID：`FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001`
- Claude Project 名称：`MNE-DR-005 跨仓库并发`
- 对应 roadmap：F2 — Cross-repository target work and safe concurrency
- 研究类型：独立高能力架构与治理研究
- 自动重试：禁止
- 仓库写入：禁止
- 验证执行：禁止
- 真实目标访问：禁止

维护对话在生成本任务包时记录：

- Mnemosyne `master = 4198d18352a071cbdcc7dc97734e65886da0621b`；
- V1 controller `head = e892749fc9e242b24908f89b6a78f1c0f0bed75e`；
- V1 结果包 blob = `8a5f3644707ae518182ed352174e58d1ca419067`；
- V1 的 fresh Pro 最终裁决当时仍为 pending。

这些是维护对话提供的版本凭据。Fable 不得声称从 Project knowledge 独立证明了 Git 历史或 served backend identity。

## 一、核心研究问题

当 Mnemosyne、Meta-Agent 和多个目标仓库需要协同工作时，什么是**最低但足够安全**的治理与验证机制，使得：

- 一个 Agent/对话可以在目标仓库完成有界设计或构建；
- 只有另行授权时，才向 Mnemosyne 或 Meta-Agent 写入有界证据/方法反馈；
- 多个真正相互独立的目标可以并行；
- shared/global/unknown scope 能够正确串行、协调或阻止；
- stale ref、merge ordering、partial failure、privacy、rollback、no-dual-writer 和 provenance 都有可检查的处理；
- 不因为追求安全而建立比问题本身更昂贵的中央编排系统。

## 二、这项研究应改变的决定

报告必须帮助判断：

1. target-local operating model 是否适合作为默认候选；
2. task-local write contract 至少要包含哪些语义；
3. 哪些并发可仅凭 write-set/依赖证明放行；
4. 哪些情况需要 lock、serialization、reconciliation 或 human gate；
5. 一个任务跨两个以上仓库时，如何排序写入、验证前一步身份、处理后一步失败；
6. no-dual-writer 应如何证明，而不是仅靠声明；
7. 是否需要 central orchestrator、dependency graph、transaction log 或更轻的派生视图；
8. 哪些工作必须保持手工或 Owner 触发；
9. 当前 V1 合成验证还缺哪些反例和故障注入。

报告只是建议，不构成实施、验证、迁移或任何仓库写入授权。

## 三、独立性与证据角色

本任务文件是唯一任务指令来源。

输入分为：

- **权威约束**：Mnemosyne 执行源和精确 V1 授权边界；
- **活动防护**：PR 谱系与运行上下文/来源防护；
- **候选设计**：target-local model、lifecycle candidate、validation design、V1 execution package、F1 修正候选；
- **临时执行证据**：V1 controller 结果、cell 结果和机械检查。

V1 结果包中的 scenario pass 是 executor/controller provisional result。除非输入中明确加入了后续 fresh Pro 裁决，否则不得把它写成已获 Pro 或 Owner 接受。

不要使用：

- 旧 Fable F1 报告；
- 未列出的 V1 场景分支；
- 无关 Pro/Fable 结论；
- 私人/真实目标材料；
- 旧 Project 对话或隐藏 memory；
- live GitHub connector。

## 四、输入资料核验阶段

在任何网页研究和任何实质结论之前，读取 `MNE-DR-005-输入清单.yaml` 并核验全部 30 个逻辑文件。

允许 Project Search/RAG 和分块检索；不得声称逐字节完整读取所有文件。

核验至少说明：

- 30/30 文件是否可访问；
- 两个仓库、所用分支和路径是否正确；
- Mnemosyne 执行源及 V1 Owner 授权的精确角色；
- 候选架构、验证设计、执行包和临时 V1 结果的角色区别；
- V1 result bundle 仍写明 fresh Pro disposition pending；
- 全部 selected scenarios、M0–M11 状态、no-write、S8 isolation、S11 restore 和 incident ledger 是否识别；
- `V1-PROTOCOL-DISCREPANCY-001` 是否保留为争议，不得自行改写；
- 核验前外部网页来源必须为 0；
- 核验前不得给出实质推荐；
- 不得调用连接器或写外部服务。

若失败，只返回完整核验结果和失败状态，停止且不自动重试。

允许的失败状态：

- `INPUT_OR_PROJECT_KNOWLEDGE_COVERAGE_FAILURE`
- `WRONG_SOURCE_IDENTITY_OR_VERSION`
- `PROJECT_CONTAMINATION`
- `V1_EVIDENCE_ROLE_CONFUSION`
- `MODEL_OR_SURFACE_MISMATCH`
- `RUN_INVALIDATED_BY_PROJECT_KNOWLEDGE_ACCESS_LOSS`
- `PROVIDER_QUOTA_INTERRUPTION`

## 五、正式研究阶段

只有输入核验明确 PASS 后才能进入。

### 5.1 独立重构问题

先区分：

- authority ownership；
- task writer permission；
- same-repository concurrency；
- cross-repository ordered work；
- shared object / global object / generated object；
- repository cutover；
- evidence/provenance；
- backup/restore；
- provider/tool permission。

不要把所有问题都简化成“加一把锁”或“建一个中心 orchestrator”。

### 5.2 至少比较六种机制

**A — Task-local contract + exact write-set + mechanical diff check**

**B — Repository/target lock or lease**

**C — Central orchestrator / transaction log**

**D — Derived dependency graph / DAG-based scheduling**

**E — Repository-per-target isolation + human coordination**

**F — Hybrid model**：task-local contracts 为基线，只在 shared/global/unknown scope 使用锁、协调器或显式 reconciliation。

可以增加方案，但不得减少实质不同的设计空间。

### 5.3 必须主动分析的故障

至少包括：

- 两个任务路径不重叠但共同修改 generated index/lockfile/root config；
- read-set stale，write-set 虽不重叠但语义依赖失效；
- 第一仓库提交成功、第二仓库写入失败；
- 第二步失败后补偿写又失败；
- PR merge order 改变结果；
- branch/ref 在计划与执行之间移动；
- 同一任务意外产生两个 PR；
- target authority cutover 后旧 writer 未退役；
- shared library change 影响未知 consumer；
- private material 或 connector 权限跨仓库泄漏；
- backup 被提升为 live writer；
- no-write proof 只证明命名仓库、却被夸大到所有真实目标；
- 机械检查全绿但 semantic interference 仍存在；
- 中央 orchestrator 本身陈旧、不可用或权限过大。

### 5.4 V1 证据的使用方式

- 识别 V1 已覆盖的 positive/negative/boundary cases；
- 识别它没有覆盖的真实分布式故障；
- 把 `V1-PROTOCOL-DISCREPANCY-001` 当作 profile/contract 边界案例；
- 不因所有场景 provisional pass 就默认候选架构正确；
- 给出下一轮最低故障注入与 acceptance 条件。

## 六、外部网页研究

仅在输入核验 PASS 后使用。

优先使用：

- Git/GitHub 官方 ref、merge、branch protection、API 或 Actions concurrency 文档；
- 分布式事务、saga、2PC、lease、optimistic concurrency 的原始论文/标准/官方设计资料；
- 构建系统/monorepo 对依赖图和 remote execution 的官方设计；
- 软件供应链 provenance、least privilege 和 change-control 的正式规范；
- 可靠工程事故复盘。

外部类比不能机械转成 Mnemosyne 规则。必须分开标注仓库证据、外部事实和推理。

## 七、最终报告结构

至少包含：

1. 执行摘要与最终建议
2. 完整输入核验结果
3. 独立问题重构
4. 已固定的 authority/Owner 边界
5. V1 证据覆盖与限制
6. 故障与风险分类
7. 方案 A
8. 方案 B
9. 方案 C
10. 方案 D
11. 方案 E
12. 方案 F
13. 横向比较矩阵
14. 同仓库安全并发规则
15. 跨仓库有序写入协议
16. stale ref 与 merge-order 处理
17. partial failure 与 compensation
18. no-dual-writer、cutover 与 rollback
19. privacy、connector 与最小权限
20. provenance 与证据要求
21. 自动化边界：什么不应自动化
22. 推荐的最低默认机制
23. 对现有候选的必要修正
24. 下一轮验证/故障注入计划
25. 迁移与兼容策略
26. 被否决方案的 strongest case
27. 未知项、置信度和停止条件
28. 一个最终建议状态

最终建议状态只能选一个：

- `RECOMMEND_TASK_LOCAL_CONTRACTS_WITH_DERIVED_CONFLICT_CHECKS`
- `RECOMMEND_HYBRID_LOCK_AND_TASK_CONTRACT_MODEL`
- `RECOMMEND_CENTRAL_ORCHESTRATION_FOR_SHARED_WRITES`
- `RETAIN_CURRENT_CANDIDATE_PENDING_MORE_FAILURE_EVIDENCE`
- `INPUT_OR_EVIDENCE_INSUFFICIENT_FOR_SAFE_DEFAULT`

必须明确哪些决定仍只能由 Owner 作出。

## 八、运行记录

报告末尾说明：

- 界面实际模型和思考强度；
- Research 是否开启；
- 是否观察到 Project Search/RAG；
- 是否发生 fallback、额度中断或警告；
- 外部来源范围与限制；
- repository write performed（应为 false）；
- validation executed（应为 false）；
- exact backend identity（通常 unknown/not attestable）。

## 九、停止规则

出现以下任一项就停止且不自动重试：

- 输入缺失、身份冲突或 Project 污染；
- 把 provisional V1 结论冒充为已接受；
- 输入核验前开始网页或实质研究；
- Project knowledge 丢失；
- 明确模型 fallback；
- 连接器写入或其他外部副作用；
- 需要修改 candidate/validation package 才能继续；
- 研究中断或额度不足；
- 任务开始处理私有/真实目标材料。

## 十、交付要求

最终回答本身包含完整报告。若 Claude 提供 Markdown/Word/PDF 导出，可一并导出，作为同一报告的表示。

不要为了另做文件发起第二次 Research。报告完成后停止，等待 Mnemosyne Pro/frontier 裁决。
