# MNE-DR-003 能力归属 — Fable 5 独立研究任务

## 任务身份

- 正式任务 ID：`FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001`
- Claude Project 名称：`MNE-DR-003 能力归属`
- 研究类型：独立高能力架构研究
- 当前状态：Owner 已选择现在运行
- 自动重试：禁止
- 仓库写入：禁止
- 验证执行：禁止
- 目标项目修改：禁止

维护对话在生成本任务包时已经核验：

- `08822407d/Mnemosyne master = 930b5ed0c8d1db82e46fd9439035db3f2dd20c46`
- `08822407d/Meta-Agent master = 1fdbd7af9437f72f7c8106714ad1e64908983fb7`

这是维护对话提供的启动前版本凭据，不是要求 Fable 在 Project 中重新证明
commit SHA。Claude 的 Project GitHub 输入只应被当作按清单同步的文件内容。
Fable 不得声称自己从 Project knowledge 读取到了 Git commit history。

本任务只产出研究报告，不直接修改任何系统。

## 一、核心研究问题

Mnemosyne、Meta-Agent 和各目标自有仓库/存储，应如何分配“可复用 Agent 能力”的归属和生命周期责任，才能同时做到：

- 不产生多个竞争性的真相源；
- 不让 Mnemosyne 与 Meta-Agent 重复保存和维护同一类规则；
- 保持目标项目自己的权威与可迁移性；
- 能够进行版本演化、影响分析和目标侧采用；
- 不因为建立公共能力层而引入新的中心化瓶颈或过度复杂度。

至少研究以下对象分别应由谁拥有、保存和维护：

1. 可移植的 Agent 能力语义；
2. Agent 设计方法；
3. 原始证据、研究报告和设计理由；
4. provider / 产品适配层；
5. 目标项目的能力选择与本地适配；
6. 目标项目的实际实现和当前真相；
7. 验证与真实使用证据；
8. 从个案提升为公共方法的决策；
9. 版本、兼容、迁移、弃用与退役记录；
10. 上游变化引起的下游影响审查记录。

## 二、这项研究要帮助做出的决定

最终报告必须给出有证据约束的建议，至少回答：

- 每类对象的主要权威位置应该在哪里；
- 是否值得新增一个“公共能力仓库/公共包”；
- Mnemosyne 和 Meta-Agent 的职责边界如何划分；
- 目标项目应保留哪些本地内容，哪些只需引用上游；
- 一个能力如何经历提出、研究、评审、提升、版本化、选择、适配、验证、变更、弃用和退役；
- 上游能力变化怎样触发目标侧审查，但不能自动修改目标；
- 哪些索引/指针/依赖记录有用，哪些容易变成陈旧的“反向消费者数据库”；
- 从当前仓库结构迁移到推荐结构的最小方案是什么。

研究结果只是建议。不得因为报告给出建议，就认为已获得实施或迁移授权。

## 三、独立性要求

本任务文件是唯一的任务指令来源。

`MNE-DR-003-输入清单.yaml` 和列出的仓库文件只能按其角色作为：

- 权威约束；
- Meta-Agent 已接受的方法；
- 候选设计；
- 研究证据；
- 被挑战的研究对象。

不要读取或使用：

- 旧 Fable Greenfield 报告；
- FCV A1/A2 资料；
- 未列出的 Pro/Fable 结论；
- 无关 active-context / handoff；
- 私人对话、个人资料或目标业务真相。

不要因为某个候选文件已经很详细、已经过 Owner 讨论，就默认它正确。
必须独立重构问题，并主动寻找替代架构和失败模式。

## 四、输入资料核验阶段

**在任何外部网页研究和任何实质架构结论之前，先完成这一阶段。**

读取 `MNE-DR-003-输入清单.yaml`，核验全部 14 个逻辑文件。

允许 Claude Project 的 RAG/Search/分块检索。
不得声称逐字节完整读取了所有文件。

核验报告至少要说明：

- 14 个文件是否全部可访问；
- 两个仓库名称、全部必需路径和文件内身份/版本标记是否一致；
- 正确说明 commit SHA 由维护对话在启动前核验，Fable 自身不能从 Project
  GitHub knowledge 独立证明该 SHA；
- Mnemosyne 的执行源是什么；
- Meta-Agent 的当前目标真相是什么；
- Meta-Agent 方法文件和 authority map 分别是什么角色；
- 能力目录、三目标选择、target-local operating model、
  target-lifecycle candidate v0.2、frontier adjudication 和 F1 roadmap
  是否都已识别；
- 哪些文件是权威，哪些是方法，哪些只是候选或证据；
- 是否存在任何输入缺口或身份冲突；
- 在核验完成前外部网页来源数量必须为 0；
- 在核验完成前不得给出实质推荐；
- 不得调用任何连接器写入或修改外部服务。

如果核验失败：

1. 只返回完整核验结果；
2. 明确失败原因；
3. 不进入正式研究；
4. 不自动重试。

可使用的失败标签：

- `INPUT_OR_PROJECT_KNOWLEDGE_COVERAGE_FAILURE`
- `WRONG_SOURCE_IDENTITY_OR_VERSION`
- `PROJECT_CONTAMINATION`
- `MODEL_OR_SURFACE_MISMATCH`
- `RUN_INVALIDATED_BY_PROJECT_KNOWLEDGE_ACCESS_LOSS`
- `PROVIDER_QUOTA_INTERRUPTION`

## 五、正式研究阶段

只有输入资料核验明确通过后，才能开始。

### 5.1 先独立重构问题

不要直接在现有候选上“修修补补”。

先回答：

- 当前真正存在的 ownership / truth / lifecycle 问题是什么；
- 哪些问题是仓库拓扑问题；
- 哪些是权威问题；
- 哪些是版本和依赖问题；
- 哪些只是证据保存问题；
- 哪些是 provider adapter 问题；
- 哪些不应该被放进同一个系统解决。

### 5.2 至少比较四种实质不同的架构

至少研究以下方向：

**方案 A：Mnemosyne 为主要公共能力所有者**

Mnemosyne 保存 portable capability definitions 及其生命周期；
Meta-Agent 把这些能力作为设计方法输入。

**方案 B：Meta-Agent 为主要公共能力所有者**

Meta-Agent 保存通用 Agent capability / methodology；
Mnemosyne 只保存持久记忆领域的设计和证据。

**方案 C：按对象角色联邦分工，不新建公共仓库**

Mnemosyne、Meta-Agent 和目标仓库分别拥有不同类别对象，
通过稳定引用连接，不增加第四个权威层。

**方案 D：新建独立公共能力仓库或版本化公共包**

portable capability semantics / provider adapters 等进入一个单独的
shared package/repository。

还要研究至少一个“更去中心化”的方案，例如：

**方案 E：目标本地拥有大部分能力内容，中央只保留发现/索引信息。**

可以增加或合并方案，但必须说明为什么仍保留了足够不同的设计空间。

### 5.3 每种架构至少比较

- 真相源和 authority 是否清晰；
- 重复、漂移与不一致风险；
- 跨仓库循环依赖；
- 目标自治和 destination-only recovery；
- 版本升级和迁移成本；
- provider lock-in；
- 隐私、证据和原始来源保存；
- 可验证性和审计性；
- 并发工作和 no-dual-writer；
- 人类和 Agent 能否理解；
- 实际维护复杂度；
- 出错后的恢复；
- 从当前状态迁移的难度。

## 六、外部网页研究要求

只有输入核验通过后才能使用网页。

网页研究必须服务于具体架构判断，不要为了“看起来研究充分”而追求来源数量。

优先使用：

- 官方标准和规范；
- 官方 package / version / governance 文档；
- 原始工程设计资料；
- 同行评审论文或原创技术研究。

可参考但不得机械照搬的类比包括：

- package registry；
- schema registry；
- protocol specification；
- plugin / extension ecosystem；
- monorepo / multi-repo governance；
- ADR / provenance；
- dependency / compatibility management。

必须明确区分：

- 仓库内部证据；
- 外部事实；
- 基于两者做出的推理。

## 七、必须重点寻找的失败模式

至少主动检查：

- 新的公共仓库反而成为第四个竞争真相源；
- Mnemosyne 和 Meta-Agent 相互引用形成循环；
- target selection 与 portable capability 的版本漂移；
- provider adapter 被误升格为 portable semantic；
- 中央 consumer registry 很快陈旧；
- capability split / merge / retire 后 ID 或影响关系难以追踪；
- 目标项目无法脱离上游仓库独立恢复；
- 上游“主动发起”演变成未经授权的自动传播；
- 为了审计保存太多目标内容，重新形成双写/重复存储；
- 过度复杂的 dependency graph 比实际问题更贵；
- 过度轻量的 pointer/index 又漏掉真实影响；
- 已完成工作的重新评估被误当成普通数据迁移。

## 八、最终报告结构

完整报告至少包含：

1. 执行摘要与结论
2. 输入资料核验结果
3. 独立问题重构
4. 已固定的 Owner / authority 边界
5. 需要管理的对象和生命周期清单
6. 当前仓库职责关系与主要张力
7. 方案 A
8. 方案 B
9. 方案 C
10. 方案 D
11. 其他实质不同方案
12. 横向比较矩阵
13. 对抗性失败模式和反例
14. 推荐的对象归属图
15. 能力提出/提升/版本/弃用生命周期
16. 目标选择/适配/验证/采用生命周期
17. 上游变化与目标侧影响审查机制
18. 证据、设计理由、隐私和保留边界
19. provider adapter 与 anti-lock-in 边界
20. 从当前结构迁移的最小方案
21. 如何证伪推荐方案以及最低验证计划
22. 被否决方案及其最强支持理由
23. 未知项、置信度和还缺什么证据
24. 最终建议状态

最终建议状态只能选择一个：

- `RECOMMEND_ROLE_SPLIT_NO_NEW_SHARED_REPOSITORY`
- `RECOMMEND_DEDICATED_COMMON_CAPABILITY_REPOSITORY`
- `RECOMMEND_SINGLE_PRIMARY_OWNER_WITH_BOUNDED_SECONDARY_RECORDS`
- `RETAIN_CURRENT_DIRECTION_PENDING_REAL_USE_EVIDENCE`
- `INPUT_OR_EVIDENCE_INSUFFICIENT_FOR_OWNERSHIP_CHANGE`

最终建议必须明确指出哪些决定仍只能由 Owner 作出。

## 九、运行记录

报告末尾自然语言说明：

- Claude 界面实际显示的模型；
- 若有单独思考强度，记录界面原文；
- `Research` 是否开启；
- 是否观察到 Project RAG / Search；
- 是否发生 fallback、额度中断或其他警告；
- 外部资料使用范围和限制；
- 是否写入任何仓库或连接服务（应为否）；
- 是否执行任何验证（应为否）。

不要声称知道不可验证的隐藏 backend identity。

## 十、停止规则

出现任何一项都停止且不要自动重试：

- 缺少或多出必需文件；
- 仓库名称、路径、文件身份或版本标记与输入清单矛盾；
- Project 被旧对话或旧报告污染；
- 输入核验完成前开始外部网页研究；
- 输入核验完成前开始给出实质结论；
- Claude 明确提示本次请求由其他模型处理；
- Project knowledge 丢失；
- 出现连接器写入或其他外部修改动作；
- 研究中断或额度不足；
- 任务开始执行验证、修改架构或采用结论。

## 十一、交付要求

最终回答本身必须包含完整研究报告。

如果 Claude 提供 Markdown / Word / PDF 报告导出，可同时导出，
但这些只是同一报告的辅助表示，不是第二份研究结论。

不要为了另外制作一个文件而再发起第二次 Research。

研究完成后停止，等待 Mnemosyne Pro/frontier 对报告进行实质裁决。
