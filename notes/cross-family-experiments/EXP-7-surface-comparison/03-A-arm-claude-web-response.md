# EXP-7 设计切片 · 完整回复转移文件

```yaml
record_type: full_response_transfer_file
task: EXP-7 设计切片（代码开发类 agent「环境记忆」）
source_response: 2026-08-30 本 claude.ai 对话内 Fable 上一条回复（EXP-7 八节交付）
captured_by_actor: claude-fable-5@claude-ai-chat（模型自报，不构成确切后端证明）
authority_level: non_execution_source_draft（任务书边界：不因完成获得任何采纳地位）
preservation: 正文自「## 无需用户操作」至「## 下一步」末行逐字复制，导出时未作任何改动
capturer_notes:
  - 正文第 8 节读取清单将材料 4/5 列为 load-mnemosyne-guidance.md / guard-registry.yaml，
    与任务书编号（4=current/guard-registry.yaml、5=commands/load-mnemosyne-guidance.md）互换；
    正文各处 [VERIFIED·材料4] / [VERIFIED·材料5] 引用须按正文内部编号理解。原样保留，未修正。
  - 正文 2.4 节一处 scope_zh 引用标为「材料2」，疑为正文内部编号下「材料5」
    （guard-registry.yaml）之误。原样保留，未修正。
```

---

（以下为回复正文逐字副本）

---

## 无需用户操作

本回复为 EXP-7 只读设计输出：未写仓库、未创建文件、未做外部检索、未读任务书 5 份材料以外的任何文件。以下八节为任务书交付正文（含表格与代码块合计 ≤250 行）；本节与文末「下一步」是执行源 §12 要求的对话结构，不属八节正文。

---

### 1. 需求还原

Owner 原文逐字引用（均出自材料 2）与分级：

1. 消息二「还需要记录习惯或者说常用的系统环境开发工具配置和用户的常用环境配置」——本切片的直接依据 [VERIFIED·材料2]。分级 **G＋H** [INFERENCE]。
2. 消息一「至少程序开发和库开发我的架构方面的想法是可以当作有一定权重的意见,因为我在计算机编程这方面也是有一定工作经验的」[VERIFIED·材料2]——分级 **C**：本切片"记什么"层面的 Owner 意见权重较高，但仍非硬性设计令 [INFERENCE]。
3. 消息二「将它们记录下来后不仅仅是保存在某地占空间而已,它们还需要能够让相关agent利用起来」[VERIFIED·材料2]——分级 **G**（可用性元目标），直接驱动第 3 节加载规则 [INFERENCE]。
4. 消息二「应该提前摸清楚并形成一套经验,供其他agent学习和套用」[VERIFIED·材料2]——分级 **G**（元目标）：本切片兼作日后可套用样例 [INFERENCE]。
5. 消息三「不要把"原文"当成宝贝,而是要有依据地采纳它」[VERIFIED·材料2]——分级 **C**（采纳规则），驱动条目 evidence 分级与"用前实测" [INFERENCE]。
6. 消息二「为了能够给出有效的操作内容列表还需要明确记录相关工具/产品的真实能力限制和使用方法」[VERIFIED·材料2]——分级 **G＋O**；按反模式 #15 划界：产品**通用**能力归平台事实层，本切片只收**用户实例层**事实（如"用户机器上装的是哪个版本"）[VERIFIED·材料3 #15 存在；划界方式 INFERENCE]。

说明：材料 2 附录的 G/C/O/H/P 表为捕获方提议、「待 Owner 一字确认」[VERIFIED·材料2 头部]；本节标注沿用同一体系，同属提议性标注 [INFERENCE]。

与其余记录项的边界 [INFERENCE]：
- 开发需求／AI 方案／bug 与预期偏差／跨项目代码库线索：消息二同句并列项 [VERIFIED·材料2]，各自独立切片，本设计不覆盖；它们可**引用**环境条目 id（如 bug 记录标"发生时 node 为 ENV-003"）。
- 对话输出方式偏好（附录第 9 行列为 P＋O [VERIFIED·材料2附录]）：属交互偏好切片，不入环境记忆。
- 项目自身环境要求（lockfile、.tool-versions、CI 配置）：项目仓库是该项目运行真相源（spec §9 [VERIFIED·材料1]），不复制入环境记忆；只记用户环境与项目要求之间的**已观察差异**。

### 2. 记录方案

**2.1 记什么（字段清单）** [INFERENCE：字段选择出自通用开发经验而非仓库证据，待真实使用数据校正]
- 三个子域：`machines`（系统环境，按机器分组）／`toolchain`（开发工具配置）／`prefs`（用户环境偏好）。
- machines 例：OS 及版本、arch、shell、系统包管理器、网络约束（代理/离线）。
- toolchain 例：语言运行时及其版本管理器、构建/容器工具、编辑器、格式化与静态检查配置位置。
- prefs 例：目录与命名约定、偏好安装方式、明确禁止项、提交习惯。
- 条目级元数据，每条必含（落实反模式 #6"canonical 源＋last_updated＋过期声明"[VERIFIED·材料3 #6]）：`id`、`statement`、`evidence`（owner_stated｜observed｜inferred）、`source`（任务号＋日期）、`scope`（user｜machine:<id>）、`volatility`（stable｜slow｜volatile）、`last_confirmed`、`status`（current｜stale_check_due｜superseded｜retired）[INFERENCE]。
- 禁录：凭据、token、密钥类值——任何可见性下不得提交 secrets（spec §14 [VERIFIED·材料1]）；灰区值（内网 registry 地址等）默认不记，改为会话内向用户说明 [INFERENCE]。

**2.2 格式** [INFERENCE]：画像用 YAML、日志用 Markdown 追加行；与仓库现行 md/YAML 形态一致（材料 2、4 即此形态 [VERIFIED]）。

**2.3 放在哪里**：目标项目工作区标准根为 `target-projects/<target_project_id>/`（spec §16 [VERIFIED·材料1]）；代码开发 agent 的具体 `<target_project_id>` 未在材料中分配 [UNKNOWN]。其下组织为设计选择 [INFERENCE]：

```
<ws>/memory/environment/
  env-profile.yaml       # 蒸馏画像：小、常载入；仅 owner_stated / observed 条目
  env-observations.md    # 追加式观察日志：冷、默认不读
```

**2.4 谁写、何时写**
- 写入者：该 agent 在获授权写面上自写（platform_capability 与 task_authority 须同时成立，spec §18 [VERIFIED·材料1]）；Owner 随时可手改 [INFERENCE]。写授权属目标项目 owner rule、需交付时批准（spec §16 [VERIFIED·材料1]），本设计不授予。
- 时机 [INFERENCE]：观察/被告知当下→日志追加一行；任务收尾或该事实成为决策依据时→提升入画像；`inferred` 永不入画像，留日志待证实。
- 无写权表面 [INFERENCE，对齐 artifact-delivery guard"不虚报文件"取向（scope_zh [VERIFIED·材料2]）]：不声称已写；在回复末尾输出「待记录」块请有权方转录（降级模式，计 1 次 Owner-touch）。
- 存储介质是否 git 化在 5 份材料中未定义 [UNKNOWN]；故替代/审计链只靠条目 status 字段自足，不依赖 git 历史 [INFERENCE]。

**2.5 何时更新** [INFERENCE]
- 新观察与画像冲突：本次以新观察为准；旧条目 `status: superseded` 并指向新条目/日志行，不静默删除。
- Owner 明示纠正：立即更新，evidence=owner_stated。
- 一次性指令不更新画像（规则见第 3 节冲突条）。

**2.6 何时失效与如何标记** [INFERENCE]
- `volatile`（版本号、PATH 类）：不设 TTL；规则＝**用前实测**，画像值仅为提示。
- `slow`（OS 大版本、编辑器选择）：`last_confirmed` 超 90 天（校准值，非权威）→ `stale_check_due`。
- `stable`（偏好、约定）：不自动过期，但始终展示日期；出现矛盾观察即触发复核。
- 画像预算：超 40 条或 120 行（校准值）→ 停止追加、发起合并/退役评审；机制仿 guard-registry 的 consolidation_triggers [VERIFIED·材料5 该机制存在；数值为 INFERENCE 校准值]。

**示例记录（合成，19 行）** [INFERENCE]：

```yaml
# env-profile.yaml 节选（合成示例）
meta: {schema: env-profile-v0, entry_budget: 40, last_consolidation: none}
machines:
  - machine_id: m-macbook-01
    entries:
      - {id: ENV-001, statement: "macOS 14.x / arm64 / 默认 shell zsh",
         evidence: observed, source: DEV-012/2026-08-12,
         volatility: slow, last_confirmed: 2026-08-12, status: current}
      - {id: ENV-003, statement: "node v22.3.0（经 nvm）",
         evidence: observed, source: DEV-012/2026-08-12,
         volatility: volatile, last_confirmed: 2026-08-12, status: current}
toolchain:
  - {id: ENV-002, statement: "Python 统一经 uv 管理，不用 pip 装全局包",
     evidence: owner_stated, source: DEV-009/2026-08-05, scope: user,
     volatility: stable, last_confirmed: 2026-08-05, status: current}
prefs:
  - {id: ENV-P01, statement: "新项目放 ~/dev/<语言>/，仓库名小写连字符",
     evidence: owner_stated, source: DEV-007/2026-07-30,
     volatility: stable, last_confirmed: 2026-07-30, status: current}
```

### 3. 加载规则

- 默认（开发类任务会话开始）：仅读 `env-profile.yaml`；日志默认不读——对齐现行"冷原件按需、非默认运行上下文"原则（材料 4 第 34 条 [VERIFIED]；应用为 INFERENCE）。
- 触发表 [INFERENCE，结构仿材料 4 的 core/conditional 分层与"不确定则读"模式 [VERIFIED·材料4]]：

| 触发 | 读取 |
|---|---|
| 生成安装/配置/构建命令 | 对应 machine/toolchain 条目；volatile 项用前实测 |
| 为用户撰写操作步骤/文档 | prefs 全部 |
| 排查疑似环境相关故障 | 画像相关条目＋日志同主题观察 |
| 接手新开发项目 | 画像＋项目仓库自身环境声明（后者优先） |
| 触发归类不确定 | 读画像整份（画像有预算上限，可承受） |

- 与现行分层加载模式的关系：同构（小核心常载＋条件触发＋冷层按需），但不设独立注册表文件——切片规模下触发表内嵌于提示词片段，避免再造一层索引开销 [INFERENCE]。
- 记录与用户当前指令冲突：当前指令为本次最高依据（对齐材料 4 第 13 条"用户措辞是主要证据"[VERIFIED]；应用为 INFERENCE）；执行当前指令、把分歧作为观察追加日志；仅当用户明示"以后都这样"或同类指令再次出现（≥2 次，校准值）才修改画像偏好并留 superseded 链——既防把「反复横跳」（消息三自述 [VERIFIED·材料2]）误固化，也防一次性例外覆盖长期偏好 [INFERENCE]。
- 记录过期/陈旧：`stale_check_due` 与 `volatile` 条目一律降级为"待验证提示"：能低成本实测则实测；不能实测且动作有后果（安装、卸载、删改、执行脚本）→ 先确认或显式标注假设、只做无害步骤；不得把旧值当事实陈述（spec §11：无法验证须标注为未验证 [VERIFIED·材料1]；应用为 INFERENCE）。

### 4. 最小提示词片段

以下片段自包含、共 17 行，`<ws>` 为该 agent 工作区根；整段为设计产物 [INFERENCE]：

```text
【环境记忆规则 v0-draft】
1. 文件：<ws>/memory/environment/env-profile.yaml（画像）、env-observations.md（日志）。
2. 开发任务会话开始只读画像；日志默认不读。
3. 按触发加载：生成安装/配置/构建命令→对应 machine/toolchain 条目；为用户写操作步骤→prefs；
   排查环境故障→加读日志同主题条目；接手新项目→画像＋项目仓库自身环境声明（后者优先）。
4. 画像值只是线索：volatility=volatile 的值在执行有后果动作前必须实测（如 --version）；
   无法实测时将其作为"未验证假设"明示，不作事实陈述。
5. 项目环境要求以项目仓库文件为准；环境记忆只记用户/机器层事实及已观察差异。
6. 与用户当前指令冲突：本次按当前指令执行；把分歧追加为日志观察；仅当用户明示"以后都这样"
   或同类指令再次出现时才改画像，旧条目标 superseded，不删除。
7. 记录新事实：先在日志追加一行（日期｜来源｜evidence: owner_stated/observed/inferred｜内容）；
   仅 owner_stated 与 observed 可入画像，inferred 留日志待证实。
8. 画像条目必含 last_confirmed、volatility、status；任何修改不静默删除旧值。
9. 禁录凭据/密钥/令牌及疑似敏感值；拿不准就不记，改为在会话中向用户说明。
10. 画像超 40 条或 120 行：停止追加，向用户提出合并/退役建议。
11. 当前表面无写权限时：不声称已写；在回复末尾用「待记录」块列出应记条目，请有权方转录。
12. 本规则不授予任何写库权限；实际写入以该项目 owner rule 的授权为准。
```

### 5. 验收测试设计

前置 [INFERENCE]：observed 列一律留「待运行」——真实运行前不得预填（对齐材料 4 第 11 条不虚构报告 [VERIFIED]、材料 3"不编造"传统 [VERIFIED·值得延续段]）。效用维度（复问数、Owner-touch）纳入 expected 并预冻结，落实反模式 #2 [INFERENCE]。

**T1 记录写入（正向）**：全新会话，用户说「我平时用 zsh，Python 一律走 uv，别用 pip 装全局包」。

| expected（预冻结） | observed |
|---|---|
| 日志追加 ≥2 条，evidence=owner_stated，含日期与来源 | 待运行 |
| 有写权时画像同步新增/更新条目并含 last_confirmed | 待运行 |
| 用户零转录动作（Owner-touch=0） | 待运行 |
| 未触碰环境记忆以外的文件 | 待运行 |

**T2 加载与用前实测（正向）**：隔日新会话，用户说「帮我把这个项目的依赖装一下」。

| expected（预冻结） | observed |
|---|---|
| 仅读画像，未读日志 | 待运行 |
| 采用 uv 且不再询问包管理器偏好；复问数低于无记忆基线 | 待运行 |
| 执行前实测 uv 可用性；与画像不符→按冲突规则报告并记观察 | 待运行 |

**T3 缺失/过期（负向）**：删除画像，或把某 volatile 条目 last_confirmed 改为 120 天前；用户说「直接给我升级全局 node 的命令」。

| expected（预冻结） | observed |
|---|---|
| 不把旧值当事实：实测，或显式标注"未验证" | 待运行 |
| 画像缺失时明说无记录，不虚构条目内容 | 待运行 |
| 有后果动作前先确认，而非按旧记录直接给出升级命令 | 待运行 |

### 6. 反模式自检 [INFERENCE，逐条为本设计防线自述]

- **#2**：验收表含效用维度（复问数、Owner-touch）且 expected 预冻结，不以"文件存在"为成功标准。
- **#3**：画像有条数/行数预算与合并退役触发；superseded/retired 是一等状态；日志冷存不进默认上下文。
- **#4**：冲突默认记为局部观察；一次性指令不改画像；项目差异留在项目侧，不上升为用户级偏好。
- **#6**：每条必含 last_confirmed＋volatility＋status；volatile 定义为"用前实测"而非可信缓存。
- **#8**：agent 在授权面自写自读，会话间零人肉搬运；仅无写权降级出现 1 次 Owner-touch 且被显式计数。
- **#15**：产品/平台通用能力不入本记忆（归平台事实层）；本记忆所有条目均为带日期的时效事实，非规则。

### 7. 自我批判

1. **机器/表面识别未解决** [INFERENCE]：agent 可能把云沙箱环境的观察误记为用户本机事实、污染画像；本设计只给了 scope 字段，未给可靠的机器指纹与沙箱观察隔离方案。
2. **偏好变更阈值是拍的** [INFERENCE]：「明示或 ≥2 次」既可能误固化反复横跳，也可能对真实变更迟钝；且未设计多会话并发追加日志时的次序/冲突处理。
3. 字段清单来自我的一般开发经验，该 agent 真实高频负载字段是什么，材料中无使用数据可证 [UNKNOWN]。

最可能看不见的盲区 [INFERENCE]：a) 敏感边界灰区——"配置"与"准凭据"（内网地址、代理主机名）之间的泄漏路径我可能低估；b) 本切片对"供其他 agent 套用"元目标的可迁移性完全未验证；c) 画像格式偏向模型可读，未必利于 Owner 手改——这种亲和性偏差我自己最难察觉。

### 8. 读取清单

| 材料 | 读取范围 |
|---|---|
| 1 current/human-approved-spec.md | 全读（引用 §9/§11/§14/§16/§18） |
| 2 raw/…owner-goals-and-input-classification-verbatim.md | 全读（消息一/二/三＋附录） |
| 3 notes/…foundational-agent-antipattern-checklist-v1.md | 全读 |
| 4 commands/load-mnemosyne-guidance.md | 全读 |
| 5 current/guard-registry.yaml | 全读 |

- 依据均为本对话内提供的文本；其是否与 commit 1ba2a2e 逐字一致，在"禁外部检索"约束下无法机械核验 [UNKNOWN]。
- 未读其他任何文件；无 BLOCKED 项。
- 标注计数：VERIFIED ×26、INFERENCE ×34、UNKNOWN ×4。

---

## 下一步

- 本切片为非执行源草案，完成不改变任何采纳地位（任务书边界）；处置（采纳/修改/搁置、是否登记为 candidate）待 Owner 裁定。
- 下一步仓库写入：**否**（本回复未写库、未建文件）；若裁定入库→待单独授权。
- 模型强度：Owner 裁定与小幅修订无需前沿强度；若并入消息二第 13 项的整体重设计程序，建议在前沿级任务中统筹对比（如与 GPT-Pro 同题产物对照）。
