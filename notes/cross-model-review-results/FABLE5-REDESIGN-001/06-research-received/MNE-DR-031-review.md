# MNE-DR-031 · 盲评报告：GPT 侧对照设计稿（MNE-DR-029 / RAPW）

```yaml
record_type: blind_review_report
canonical_task_id: FABLE5-REDESIGN-001-BR2 / MNE-DR-031
reviewed_artifact: notes/cross-model-review-results/FABLE5-REDESIGN-001/06-research-received/MNE-DR-029-counterpart-design.md（RAPW，1554 行，全文读取）
rubric: project-knowledge/FABLE5-REDESIGN-001/MNE-DR-030-031-shared-review-rubric.md（预冻结版）
reviewer_surface: 全新 Claude Code 会话 · VSCode 扩展 · 模型 Fable 5（claude-fable-5，如实记录）
date: 2026-08-31
branch_confirmed: fable5-redesign-001-workspace（git branch --show-current 实测；只读，未提交未推送）
blind_condition_compliance: 未读取禁读清单任何文件；未做两稿比较；未使用本会话上下文之外的项目记忆作评审依据
verdict_summary: R1~R8 全部 PASS（R6 带保留）；16 处引证抽查全部命中；三大缺陷均属完善度问题，其中缺陷一（必填字段无分层）建议列为合成稿必须解决项
```

## 0. 输入面自证（实际读取清单）

| 文件 | 读取范围 |
|---|---|
| MNE-DR-030-031-shared-review-rubric.md | 全文 |
| MNE-DR-031-blind-review-pro-design-taskbook.md（本任务书） | 全文 |
| 06-research-received/MNE-DR-029-counterpart-design.md（被评稿） | 全文（1554 行，两次分页读取） |
| pro-counterpart-materials/01-goals-register.md | 全文 |
| pro-counterpart-materials/02a-contradiction-clarification-package.md | 全文 |
| pro-counterpart-materials/foundational-agent-antipattern-checklist-v1.md | 全文 |
| pro-counterpart-materials/MNE-DR-027-result.md | 全文（核证 §11.12） |
| pro-counterpart-materials/MNE-DR-028-report.md | 章节目录＋195-214 行（适配性总表与 Q2 结论，核证） |
| pro-counterpart-materials/MNE-DR-023-report.md | 章节目录＋101-135、226-285 行（Q4/Q7，核证） |
| pro-counterpart-materials/MNE-DR-024-report.md | 章节目录＋104-270 行（Q3/Q4/Q5，核证） |
| pro-counterpart-materials/MNE-DR-026-report.md | 章节目录＋75-142 行（Q4/Q6，核证） |
| pro-counterpart-materials/MNE-DR-021-report.md | 章节目录＋157-184 行（Q7，核证） |
| pro-counterpart-materials/MNE-DR-020-report.md | 章节目录＋136-170 行（Q6，核证） |

未读取：`04-redesign-fable.md`、`02-consistency-and-feasibility.md`、`05-pro-counterpart-package.md`、`05a*`、`06-research-received/01-ingest-digest.md`、`09-continuation/` 全部、`03-research-questions.md` 及其他一切与评审无关路径。证据库中 MNE-DR-022、025 未读（被评稿相关引证已由其他 14 处抽查间接覆盖判定面，未单独核证的引证不计入 VERIFIED）。

## 1. 逐项评审（R1~R8）

| # | 评审项 | 判定 | 短评（两句内） |
|---|---|---|---|
| R1 | 十二节齐全且实质 | **PASS** | 十二节与 §1 架构、§2 文件组织、§3 三态循环、§4 状态机、§5 加载投影、§6 目的核查、§7 Owner-touch、§8 交接＋预冻结测试、§9 迁移、§10 反模式自检、§11 自我批判、§12 证据引用一一对应。全部为字段级/算法级/阶段级实质内容，无空壳节。 |
| R2 | 公理遵从（N-14/15/17/18/19、X-1~X-4） | **PASS** | N-14（§3.3 S0"完整捕获但不信任"、无执行权）、N-15（§2 两层结构）、N-17（§2.4 唯一写权＋rule_id 引用＋整体迁移 manifest＋旧址仅重定向）、N-18（§4.6/§7.2 无全局节奏、逐任务声明）、N-19（§5 六级装载类＋清单化硬过滤，含"弱模型照单执行"）逐条落实，X-1 按裁定 A 处理（类比降为可推翻默认、以 028 证据提出后继模型、PRE-FREEZE 不自行生效）。逐条对照 02a 裁决原文与登记表 §7/§8，未发现违背任一裁定。 |
| R3 | 证据接地 | **PASS** | 抽查 16 处关键主张（10 处对研究报告原文、6 处对登记表/裁决包原文，见 §5 抽查表），全部命中，无虚构引证、无标签错用。§12.3 显式列 10 项 INFERENCE、§12.4 列 14 项 UNKNOWN，无据断言的诚实标注纪律为全稿强项。 |
| R4 | 核心目标方案质量（交接＋预冻结测试） | **PASS** | 五元恢复（§8.3 Quick Card：goal/status/decisions/must_not_do/next_atomic_action 五字段齐）、不可重推隐藏依赖（§8.6 两 case＋hidden-fact oracle）、按接收方分层（§8.6 三类接手者＋§8.4 load_plan）、拒收与反陷阱（§8.5 fatal/warning＋反"一律拒绝"＋§8.7 TRR/FRR 双报）全覆盖，测试具备样本配额/冻结判分/统计纪律（McNemar、配对 delta、禁提前停止），可执行。缺口：登记表 §4.1 的 Owner 体感指标与 ≤5 文件/≤2 步阈值、失败归因"用户操作"轴未纳入（见缺陷二），按 R4 列明子项判 PASS。 |
| R5 | 反模式自检真实性 | **PASS** | 16 条均落到具体机制而非口号（如 #4→scope_locality＋promotion gate、#11→晋升时重新绑定 goal 与 outcome、#16→blocked_unknown 合法终态），且逐条附残余风险与验证需求。§10.2 明言"表格全打勾≠验收完成"，自检真实性高。 |
| R6 | Owner 负担 | **PASS（带保留）** | touch 计数口径清晰（含 failure_touch 与手工搬运单列）、预算逐任务声明且默认值诚实标 INFERENCE 待校准、超支前五步阶梯内建"合并提问＋推荐默认＋各选项后果"三件套（§7.2）。保留意见：人话呈现仅落在 §5.4 人类投影与 §12.2 一行映射，是对 N-09 最薄弱的落实（展开见缺陷三）。 |
| R7 | 可实施性 | **PASS** | 12 个迁移阶段各带退出条件，影子运行＋逐阶段回滚（inverse steps）＋"不重写 Git 历史"齐备，与现状兼容路径清楚（阶段 1 只读盘点不移动、阶段 3 section-level manifest 不破坏历史）。成本诚实体现为承认 UNKNOWN 而非给假数字，但各阶段无工作量/Owner-touch 量级估算，实施节奏需靠影子运行校准。 |
| R8 | 自我批判质量 | **PASS** | 13 项盲区触及真风险：§11.1 复杂度反噬（引 028 Q4 警告自己，对应反模式 #3/#9）、§11.5 状态机僵化、§11.7 测试过拟合、§11.8 裁判偏置、§11.13 "没做的事"清单。同族偏置在机制层有对冲（§8 跨家族接手者、§8.7 第 8 条同家族分裂不冻结），但对"本稿自身由单一家族起草"的反身性批判仅隐含于 §11.13，未正面展开。 |

## 2. 三大优点（带节号与证据位置）

**优点一 · N-19 的机械化落地是全稿最强设计（§5.1–§5.3）。** Owner 的毒性哲学被编译为六级装载类（L0~L5）、八步固定顺序装载算法、逐次 load receipt，显式满足 N-19 末条"次档模型照单执行而无需理解哲学"的设计要求；且"硬适用性过滤先于相关性排序、cosine 不判当前有效"有 MNE-DR-023 Q4 的直接实证支撑（VersionRAG 90% vs naive 58%；temporal-contradiction AUROC 0.59）。【VERIFIED】

**优点二 · 预冻结测试设计达到可执行水准且系统性防作弊（§8.5–§8.7）。** 反陷阱 case（supersession 明确时应接受，"看到冲突就一律拒绝也不合格"）、TRR/FRR 双报防"一律拒绝刷分"、开发折/确认折分离防"越评越好"，逐项对应 MNE-DR-024 Q4/Q5 的实证建议；§8.7 第 8 条"不同模型结论分裂时不以同家族多数票冻结"超出材料明文要求、主动加固独立性（对冲反模式 #14）。【VERIFIED】

**优点三 · 证据纪律与不确定性披露（§12.3/§12.4、§11.13、材料完整性核验表）。** 四级标签贯穿全文，10 项 INFERENCE 与 14 项 UNKNOWN 显式列出，"完整设计≠效果已证实"明言；开篇材料核验表逐件报字节数与首行。本次抽查 16 处引证全部命中，未发现一处把 INFERENCE 伪装成 EVIDENCE 或把 UNKNOWN 猜补成事实。【VERIFIED】

## 3. 三大缺陷（带节号与证据位置）

**缺陷一 · 必填字段最大化与自身"轻量"承诺相矛盾，且无最小核心层级（§2.3、§2.5、§4.3、§4.5、§5.3、§6.3、§8.2–§8.4）。** 九张 schema 合计约 190 个"必需/不能删除"字段；load receipt 要求"每次模型调用或任务阶段"生成约 23 字段记录；§2.3 规定任何字段缺失即 rebuild_required/blocked。这与 §1.4 自称"轻量语义账本"、反模式 #9（记账开销无上限）及 §11.1 自认的复杂度风险直接紧张——§11.1 说允许"最小子集"，全稿却从未指明哪些字段构成最小子集。【INFERENCE：单 Owner 项目按全量执行大概率触发其自身 #9 红线；建议合成稿把"字段分层（核心必填/条件必填/可选）"列为必须解决项】

**缺陷二 · 对登记表 §4.1 验收标准草案的对齐不完整（§8.6 指标集、§9 阶段 9）。** Owner 体感四指标（背景补充为零、手工动作 ≤2 步、前三轮无既视感、"遮住边界看不出两个对话"）、机械指标中"恢复所需读取 ≤5 文件"与 11 项评估问题框架均未纳入或映射；失败归因四来源中"用户操作流程"轴在 §9 阶段 9 的归因分类（源证据/投影/loader/package/receiver/模型能力）中缺位。自建指标体系质量不低，但作为对唯一指定验收草案的响应缺少显式 reconciliation。【VERIFIED：与登记表 §4.1 原文逐项比对】

**缺陷三 · 呈现面是三面公理中落实最薄的一面（§5.4、§12.2 N-09 行；对照登记表 §4.3、§4.5）。** N-09 的"开篇列操作/正文无内部术语/人话讲解"只被映射为"human projections"一行；状态机（§4）对"不可行沟通须有 Owner 可读的人话说明"（登记表 §4.3）只有状态字段、没有人话出口；N-11 的套用成本度量（登记表 §4.5：新项目就位的 Owner 动作数与耗时逐代下降）亦无对应机制。"记录≠加载≠呈现"公理在本稿中前两面强、第三面弱。【VERIFIED：呈现面相关登记表条目逐项比对】

## 4. 采纳建议清单（建议进入最终合成稿的具体机制，逐条注明出处节号）

1. 六级毒性/装载类＋L4/L5 装载时的 `data_only / instruction_authority=false` 机器可见边界（§5.1）。
2. 八步固定顺序装载算法，尤其"硬适用性过滤先于相关性排序""预算未用完不是继续装材料的理由"（§5.2）。
3. Load receipt 与六项污染/失效指标（§5.3、§5.6）。附加条件：`used_source_refs` 依赖模型自报 span，采集可靠性无机制保障，采纳前需先解决测量办法【INFERENCE】。
4. 双闸门设计：Purpose Gate 与 Integrity Gate 同级、九个触发时点、十条自动停止规则（§6.1–§6.4）——直接回应反模式 #11 的"设计题"。
5. "删除也是设计动作"：每个 review 周期必须允许 merge/replace/archive/delete 四类结果，"只有新增没有退休即 purpose drift 信号"（§6.5）。
6. Owner-touch 计数口径（含 failure_touch、手工搬运单列、不计 Owner 自愿追加）与超支前五步阶梯（§7.1–§7.2）。
7. Receiver Receipt＋fatal/warning 分级＋"B 明确 supersedes A 时应接受而非拒收"反陷阱规则（§8.5）。
8. 12-case 配额中的反陷阱 case、TRR/FRR 双报、开发折/确认折分离（§8.6）。
9. 预冻结通过门八条，尤其第 3 条"至少一个结果轴有可观察收益，否则 STOP_PURPOSE"与第 8 条"同家族分裂不冻结"（§8.7）。
10. MODEL-EVENT 记录结构＋"新模型只触发重评、不自动激活 deferred、不自动废止 current"＋quarantine_required 例外（§4.1、§4.4）。
11. N-17 规则单元工程化：唯一写权目录、rule_id 引用、migration-manifest、旧位置仅留重定向、规则晋升五条件（§2.4）。
12. 检索升级阶梯按冻结 query/eval 集触发而非按仓库规模；每次升级同测任务成功/critical recall/污染率/维护成本（§5.5）。
13. "耐久≠常驻加载"判定标准：以"删除后是否丢失不可安全重建的事实"定耐久，与是否常驻无关（§2.2 首段）。
14. 投影四不变量：可删可重建、逐条回源、stale 只降性能不改 authority、模型生成投影不反写规范（§5.4）。
15. 迁移方法论："先标注后分层、影子运行、通过测试再切换"＋逐阶段退出条件＋回滚原则（§9，尤其阶段 1/8 与回滚原则节）。

## 5. 证据标签纪律

本报告标签口径：**VERIFIED** = 本次已对照材料原文核实；**INFERENCE** = 评审者基于材料的判断，未经实测；**UNKNOWN** = 材料不足以判定。上文 §1–§4 中未带标签的描述性内容均为对被评稿文本的直接转述（可回溯至被评稿节号）。

### 引证抽查记录（R3，共 16 处）

| # | 被评稿主张（位置） | 核对材料 | 结果 |
|---|---|---|---|
| 1 | 类比降为可推翻默认，属 Owner 裁定（§1.5、§12.1） | 02a X-1 附录裁定原文（A＋复核指令） | VERIFIED |
| 2 | 修正方向"概率处理器＋确定性治理＋显式耐久状态"（§12.1） | 028 Q2 结论（原文同表述） | VERIFIED |
| 3 | 类比五行"可保留教学意义/不得作为保证"表（§1.5） | 028 适配性总表 | VERIFIED（一致，无歪曲） |
| 4 | 规则单元设计属 Owner 裁定（§2.4） | 02a X-2 逐字答复＋N-17 | VERIFIED |
| 5 | 三态对应 O-13 且收窄"真相"用词（§3.1） | 登记表 O-13、N-14 | VERIFIED |
| 6 | 六级装载类对 N-19 的映射（§5.1） | 登记表 N-19 全文（§8 新增条目） | VERIFIED（四类语义＋默认读取集＋弱模型机械执行逐项对应） |
| 7 | "先硬过滤后排序、cosine 不判当前有效"（§5.2） | 023 Q4（VersionRAG 90% vs 58%；AUROC 0.59；检索顺序四步） | VERIFIED |
| 8 | 检索升级阶梯与触发条件（§5.5） | 023 Q7 阶梯表（rg→FTS5→dense→hybrid→version-aware，按 eval 非按 MB） | VERIFIED |
| 9 | "同家族不得独占最终自证"（§8 接手者、§11.8） | 024 Q3（self-preference 实验；"不要让同一模型族独占主观评分权"） | VERIFIED |
| 10 | 统计纪律：配对、exact McNemar、原始 counts 优先（§8.6） | 024 Q4 | VERIFIED |
| 11 | "看到冲突就一律拒绝不合格"＋反陷阱（§8.5） | 024 Q5 故障矩阵（B supersedes A 应接受）＋TRR/FRR | VERIFIED |
| 12 | 对抗折冻结、开发折可增 trap（§8.6） | 024 Q5 "对抗折必须冻结" | VERIFIED |
| 13 | "反馈→复现→test/hook→必要时规则"晋升序（§3.6、§2.4） | 026 Q4（bug→reproducer→regression；两次同错→retrospective；规则编译为可执行检查） | VERIFIED |
| 14 | 实验条件 A/B 双基线与结果指标面（§8.6） | 021 Q7（Same-Session Oracle / Cold Restart 双基线＋四互补面） | VERIFIED |
| 15 | "模型自报≠运行时遥测"＋identity_evidence 分级（§4.4、§2.3、开篇边界声明） | 020 Q6（无官方自然语言自省保证；UI 选择≠实际路由） | VERIFIED |
| 16 | GitHub 写能力为局部事实、不作永久保证（§11.12） | 027 实测结果（本账户/本连接/当日三写 action 成功；结论明确限定范围） | VERIFIED |

抽查结论：16/16 命中；未发现虚构引证、张冠李戴或标签升级（把推断标成证据）现象。

---

**本报告状态：** 交付完成。按任务书 §2/§3：仅写入 ~/Downloads/，未写仓库、未 commit、未 push；未读取禁读清单文件；未做两稿比较；不含重新设计内容。
