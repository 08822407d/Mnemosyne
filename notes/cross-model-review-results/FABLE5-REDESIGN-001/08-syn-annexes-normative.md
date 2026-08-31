# SYN 规范附件（NORMATIVE · 与 07 同 commit 构成唯一规范根）

```yaml
record_type: normative_annexes
version: ANNEX-1（随 SYN-2 发布；版本锚=本文件与 07-synthesis-design-v1.md 所在 commit SHA）
authority: 本文件为规范正文（closing MNE-DR-032 BLOCKER-01）；04 与 029 自本版本起降为 evidence/reference，其全部规范权由本附件与 07 承接（supersession 声明见 07 §1）
inference_policy: 凡数值阈值均标 [INF]=INFERENCE 待校准；未标者为结构性合同
```

## ANNEX-A · 需求生命周期状态机（承 029 §4.1-4.2，正文化）

**18 主状态**（每条需求唯一主状态；自由文本状态非法）：

`captured / triage_pending / analysis_pending / conflict_pending / blocked_unknown / owner_decision_pending / accepted / planned / implementing / verification_pending / verified_current / failed_validation / deferred / reassessment_pending / rejected / withdrawn / superseded / retired`

可执行性：仅 `accepted(设计) / planned / implementing / verified_current` 具执行权；`verification_pending` 不得宣称完成；`reassessment_pending` 源自 verified_current 且无 `quarantine_required` 时旧版暂保执行权。

**合法转换**（schema/lint 拒绝表外转换；新状态须先 schema migration）：

| From → To | 条件 |
|---|---|
| captured→triage_pending | 原始证据可定位＋敏感性已标 |
| triage_pending→analysis_pending / blocked_unknown | scope 初定 / 缺关键件 |
| analysis_pending→conflict_pending / owner_decision_pending / deferred / rejected | 同权威冲突 / 选项证据风险齐 / 有重启触发 / 有充分反证 |
| conflict_pending→owner_decision_pending | 冲突整理为可裁包（并列不调和） |
| owner_decision_pending→accepted/deferred/rejected/withdrawn | Owner 裁决或撤回 |
| accepted→planned→implementing→verification_pending | 计划齐（验收标准＋touch 预算）/ 执行闸门过 / 产物固定 |
| verification_pending→verified_current / failed_validation | 验收过 / 任一主 oracle 败 |
| failed_validation→analysis_pending/deferred/rejected | 记录失败证据后择向 |
| deferred→reassessment_pending | 命中已登记 revisit_trigger |
| verified_current→reassessment_pending / retired | 模型/平台/反馈/依赖/定期测试触发 / 生命周期终 |
| reassessment_pending→analysis_pending/owner_decision_pending/verified_current/deferred/superseded | 重评结果 |
| accepted/planned/implementing/verified_current→superseded | 新记录显式替代，禁原地改写 |
| 非终态→withdrawn | Owner 撤回 |

`defer_reason ∈ {model_capability, platform_capability, evidence_gap, owner_priority, resource, dependency, risk, other}`；能力类 deferred 由 MODEL-EVENT 批量转 reassessment_pending（不自动生效）；`rejected/deferred/blocked_unknown` 必附 Owner 可读人话说明（呈现面出口）。

**MODEL-EVENT** 核心档：`event_id / provider / model_label / surface / observed_at / identity_evidence(official_doc|surface_observed|owner_declared|self_report_only|unknown) / previous_generation / affected_requirement_query / regression_suite / owner_review_needed`。

## ANNEX-B · 装载算法与收据（承 029 §5.2-5.3，正文化＋分档）

**八步固定顺序**（次档模型照此执行，不得增删换序）：

1. 绑定任务（task_id/goal/declared_tempo/checkpoint/model+surface）；
2. 硬适用性过滤（canonical_status→authority_domain→scope→lifecycle_state→时间有效性 valid_from≤as_of<valid_to 或 review_trigger→model/surface binding→sensitivity/permission→source hash 完整性）——**先排除不适用，后排相关性；cosine 永不判"当前有效"**；
3. 装入 EXECUTION_CORE＋TASK_DIRECT（仅任务直接相关部分）；
4. 覆盖缺口检查（目标/约束/下一动作/验收/环境五项齐否；缺→步 5 或 blocked）；
5. 检索候选（目录 manifest→rg/ID/path→需要排名才 FTS/BM25→冻结 eval 证实词汇错配才 dense→双向互补缺口才 hybrid）；
6. 按毒性与 token 预算裁剪（短、权威、当前、直接优先；**预算未用完不是继续装载的理由**）；
7. 生成装载收据（档位见下）；
8. 作答后回填 used_source_refs（测量办法落地前为 non-gating [INF]）。

**收据两档**（closing BLOCKER-03）：

- **minimal 档**（每次模型调用）：`receipt_id / task_id / mandatory_sources+hash / retrieved_sources+hash / toxicity_class_per_source / authority_per_source / hard_filters_applied / omitted_candidates(含原因) / conflicts_detected / status`（10 字段——足以计算 Stale Context 与 Rule Scope Error）。
- **audit 档**（触发即必填，机械判据）：任务满足下列任一 → 本任务全部调用用 audit 档：写入耐久核心；跨族交接；迁移 T 步；预冻结测试运行；规范条目变更；Owner 明示。audit 档=029 §5.3 全字段。
- **指标↔数据映射**：Token Pollution 需 audit 档（token 计数）；Stale Context/Rule Scope 需 minimal；Unused Mandatory 与 used_source_refs 绑定→non-gating [INF]；Projection Drift 由 hash 校验独立产生；Critical Miss 由测试 oracle 产生。**字段不可得的指标状态=not_measurable，禁止估算。**

**投影四不变量**：可删可重建；逐条回 source path+revision/hash+span；stale 只降检索/性能不改 authority；模型生成投影不得反写规范层。

**双闸门触发与停止**（承 029 §6.2/6.4，正文化）：目的核查九触发点=新主线前/局部升全局前/新组件前/长期工件前/touch 预超前/冻结结论前/迁移权威根前/连续两周期仅形式变化 [INF]/包装 UNKNOWN 前。十条自动停止规则=无法指向 Owner goal；仅格式合规；单次事故无局部性分析即立全局规则；新组件未购买已测失败面；成本未受预算约束；已有更简机制；仅"看起来完备"；研究无 disposition；平台限制升永久规则；为避认 UNKNOWN 而建模。触发即 STOP_PURPOSE 或 PROCEED_NARROW；ESCALATE_OWNER 仅限价值/授权/不可逆。

## ANNEX-C · 交接合同（承 029 §8＋04 §8，正文化＋修正）

**Quick Card 15 字段**（核心档；任何交接必备）：`package_id/checkpoint_id/task_id · why_this_task_exists · current_goal · pace(declared_tempo) · current_status · current_authoritative_decisions · next_atomic_action · must_not_do · blocking_unknowns · acceptance_oracle · critical_source_refs · workspace_and_environment_pointer · validity/invalidation · package_hash · hidden_dependencies`——最后一项**条件核心**：存在不可重推事实必填；确无则显式写 `none`（空缺=不合格）（closing BLOCKER-04/D-05）。每一隐藏事实过"三问不可重推审计"（后续输入泄漏？工作区可重发现？常识/检索可推出？）。

**Portable Checkpoint 全集**（029 §8.2）为条件档，触发：跨族交接 / 挂起超 1 个 declared_tempo 周期 / 迁移 / 存在环境-工件状态依赖。

**Full Package 分区**（029 §8.4 全表采纳）；execution_history 只留有诊断价值的失败。

**Receiver Receipt**（029 §8.5 字段全集采纳）＋判定：
- **Fatal（拒收）**：task/checkpoint 不符；hash/schema 破坏；缺 current goal/next_atomic_action/关键 oracle；当前决定不可判定；关键 secret/证据缺失；权限不足却要求写入。
- **Warning（收下继续）**：可选说明缺失；背景较旧但 current 标记清楚；冗余历史；非关键主观项不全。
- **反陷阱**：B 显式 supersedes A → 接受并用 B；无 provenance 的 A/B 冲突才拒。"一律拒绝"不合格（TRR/FRR 双报见 ANNEX-D）。

**分层选择规则**（closing D-04/BLOCKER-04）：发送方按二维矩阵在 load_plan 指定——任务风险（低/中/高：以是否触 audit 档判据）×接收方能力类（以**模型适配层登记**为准，未登记=按次档处理，不得按名称猜测）。默认=Quick+Full 指针模式；次档接收 或 高风险 → 加完整轨迹层；强模型接乱局（前任 failed_validation 或 integrity stop 后）→ 允许 fresh-restart＋要点层。接收方升档：Receipt 中列明缺口字段即可升档一次，无需 Owner。

**返场规则**（closing D-10/BLOCKER-08）：离场超过该主线 declared_tempo 的 **2 个周期** [INF] → 先消费追赶简报（自 git log＋裁决层生成：期间裁决/冻结/编号/规范变更/在场写者与串行声明），无简报不开工。**无全局天数上限**；Owner 可为任一主线声明附加上限。同机多会话：worktree 分离＋写者串行声明（hard，强制层=preflight 脚本已实装）。

## ANNEX-D · 预冻结效果测试协议（closing BLOCKER-05/06）

**样本**：12-case [INF·pilot]——真实历史检查点 6（跨 ≥3 主线）＋隐藏事实 2＋current/superseded 2＋应拒坏包 1＋应收反陷阱 1。case 选择、顺序在运行前冻结；**学习残留控制**：每臂使用独立新会话实例，同一 case 的各臂随机顺序、互不共享上下文。

**六臂条件**：A Same-session oracle（连续上限，非部署方案）；B 仅当前文件冷启动（基线）；C 仅 Quick Card；D Quick+Full+Receipt（候选）；E 故意降级包（测拒收灵敏度）；**F 全档审计**（closing D-11：审计者获交接前后完整档案与仓库状态，产出交接包缺陷清单——对应设计稿 E 条件 2，与 A 无关）。主比较 B vs D。

**接收者三类**：同模型 fresh / 次档或受限 / 异族（条件允许时）。主 pass/fail 全部机械/闭池 oracle；LLM 仅次级主观备注。

**通过门十条**（029 八条＋修订二条）：
1. D 相对 B 不新增 critical stale/must-not 违规；2. D 无未解释 candidate-worse 对；3. D 至少一条结果轴可观察收益，否则 STOP_PURPOSE；4. TRR/FRR 双报，不得靠一律拒绝；5. 全部 fatal 缺陷触发拒收或干净停止；6. 包制作成本与 touch 未超预算；7. 结果可由冻结 raw log 重算；8. 模型间结论分裂不以同族多数票冻结；9.（新）**登记表 §4.1 映射表全项达标**（下表）；10.（新）条件 F 缺陷清单为空或仅 cosmetic（cosmetic 定义：不改变任何 oracle 判定与接收方行动选择的表述性差异）。

**§4.1 全量映射**（closing M-02/D-12）：

| 登记表条件 | 测法 |
|---|---|
| 体感1 背景补充为零 | D 臂 Owner 参与 case（≥2 [INF]）中 Owner 补充背景次数=0 |
| 体感2 手工动作 ≤2 | **owner_manual_actions 计数**（含发起/上传/复制/核对/纠错——与 agent_touch 分账，closing D-12） |
| 体感3 前三轮无既视感 | Owner 参与 case 主观判定（记录，不入主门） |
| 体感4 遮住边界测试 | Owner 盲抽 1 case [INF] 判"可否看出换会话"（记录，不入主门） |
| 机械1 五元恢复全对 | 闭池＋executable oracle 逐项 |
| 机械2 ≤5 文件一次会话恢复 | minimal 收据的 mandatory+retrieved 计数 |
| 机械3 首任务无纠正 | 首个实质任务 failure_touch=0 且 owner 纠正=0 |
| 机械4 全档审计仅 cosmetic | **条件 F** 缺陷分级 |
| 机械5 归因可判定 | 双层归因：Owner 四轴（交接包/接收方/仓库残留/用户操作）×工程子因（源证据/投影/loader/package/receiver/模型能力/工具）矩阵（closing D-13） |
| 机械6 fail-closed 正反例 | E 臂 TRR=100%目标、F RR=0 目标＋反陷阱通过 |
| 11 项评估问题 | 逐项 PASS/PARTIAL/FAIL：目标恢复/阶段恢复/已确认决定与禁止项保留/执行源-证据-候选-历史层级区分/安全下一步/依赖遗漏/历史路线误激活/旧上下文污染/授权边界保持/重复读取成本/交接后效率提升 |

**统计**：配对呈现全部结果＋discordant counts＋exact McNemar；连续量 paired delta＋exact/sign-flip；n 小不谎称显著也不谎称无效；事前定 N 不因效果方向早停；原始 counts 优先。

## ANNEX-E · 字段三档矩阵（closing BLOCKER-02/D-01/D-02）

**档位定义**：核=核心必填（缺即 blocked）；条=条件必填（触发条件成立缺即 blocked，条件注于行内）；选=可选。**次档模型规则**：只按"核"清单执行；遇"条"触发词查本表，查不到=按核处理（fallback，closing D-04）。

**通用记录头**（029 §2.5 全 24 字段分档）：

| 档 | 字段 |
|---|---|
| 核（12） | artifact_id · artifact_type · schema_version · canonical_status · authority_domain · lifecycle_state · scope · created_at · source_refs · supersedes · **valid_from＋(valid_to 或 review_trigger)** · integrity_status（closing D-02：hard filter 全部所需字段入核） |
| 核-分类（2） | sensitivity · toxicity_class（装载硬过滤所需） |
| 条 | source_hashes（写耐久核心时）；model_binding/surface_binding（非 model-neutral 时）；change_id（经变更集产生时）；verified_by/last_verified_at（声称已验证时）；superseded_by（被替代时） |
| 选 | created_by · notes_on_unknowns（无 UNKNOWN 可省，有则必写） |

**需求记录**（029 §4.3 增补字段分档）：核=requirement_text_verbatim · goal_refs · request_class · state · scope · acceptance_oracles · next_required_action；条=defer_reason＋revisit_triggers＋quarantine_required（state=deferred 时）· conflicts_with（conflict_pending 时）· decision_refs（裁决后）· implementation_refs/verification_refs（planned 起）· must_include/must_not_include（有负约束时）· priority/risk_class（Owner 定或高风险时）；选=normalized_intent · dependencies · unknowns · closure_reason（终态必填→条）。

**收据**：见 ANNEX-B 两档（即本矩阵的收据行）。

**检查点/交接**：见 ANNEX-C（Quick Card=核；Checkpoint 全集=条，触发已列）。

**投影清单**（029 §2.3 分档）：核=generation_id · built_for_model_label · built_for_surface · source_revision · integrity_status · rebuild_triggers；条=model_identity_evidence（label 非 official_doc 时）· source_hash_manifest（audit 档任务）· scope_included/omitted（部分投影时）· expires_at_or_review_trigger（长期投影）· supersedes/superseded_by（换代时）；选=其余。

**命名去冲突**（closing D-06）：架构层改记 **A0~A6**（A0 Owner 目的与授权…A6 确定性闸门）；装载类保留 **L0~L5**；权限态 **S0~S2**。三套坐标正交：A=系统层，L=单次装载分类，S=知识权限状态。全文与日志引用须带前缀。

## ANNEX-F · 29＋7 一对一追踪（closing M-07）

| 项 | 落位 | 状态 |
|---|---|---|
| F-01 三面骨架 | 07 §1＋A0-A6 | 落实 |
| F-02 norms 字段 | 07 §3（字段全文列出） | 落实（修） |
| F-03 预算/减法 | 07 §3 | 落实 |
| F-04 三态通道 | 07 §4 | 落实 |
| F-05 状态机 | ANNEX-A | 落实（修） |
| F-06 加载表/四单 | 07 §6＋ANNEX-B | 落实 |
| F-07 回链/单向写/快车道 | ANNEX-B 四不变量＋07 §1 快车道条款 | 落实（修） |
| F-08 purpose 三件 | 07 §7 | 落实 |
| F-09 交接三件套 | ANNEX-C | 落实 |
| F-10 返场/worktree | ANNEX-C | 落实（修） |
| F-11 测试纪律 | ANNEX-D | 落实 |
| F-12 迁移骨架 | 07 §10 | 落实 |
| F-13 风险登记 | 07 §12（压缩失义与自报美化恢复登记） | 落实（修） |
| F-14 hard/advisory | 07 §3＋§8（双频道改 advisory 待强制层） | 落实（修） |
| P-01 装载类/机器边界 | ANNEX-B | 落实 |
| P-02 八步算法 | ANNEX-B 正文 | 落实（修） |
| P-03 收据/指标 | ANNEX-B 两档＋映射 | 落实（修） |
| P-04 双闸门九触发十停止 | ANNEX-B 末节正文 | 落实（修） |
| P-05 删除是设计动作 | 07 §3 | 落实 |
| P-06 touch 口径/阶梯 | 07 §8 | 落实 |
| P-07 接收回执 | ANNEX-C 正文 | 落实（修） |
| P-08 12-case/TRR-FRR/折 | ANNEX-D | 落实 |
| P-09 通过门 | ANNEX-D 十条正文 | 落实（修） |
| P-10 MODEL-EVENT | ANNEX-A | 落实 |
| P-11 规则单元 | 07 §3 | 落实 |
| P-12 检索阶梯 | ANNEX-B 步5＋07 §6 | 落实 |
| P-13 耐久判定 | 07 §1 | 落实 |
| P-14 投影四不变量 | ANNEX-B 正文 | 落实（修） |
| P-15 迁移退出条件 | 07 §10 | 落实 |
| M-01 三档字段 | ANNEX-E 逐字段 | 闭合（修） |
| M-02 §4.1 全闭合 | ANNEX-D 映射表＋条件 F＋11 问题 | 闭合（修） |
| M-03 三件套 | 07 §8 | 闭合 |
| M-04 touch 口径 | 07 §8（双账分记） | 闭合（修） |
| M-05 呈现面 | 07 §9 | 闭合（enforcement 修） |
| M-06 返场阈值 | ANNEX-C | 闭合（修） |
| M-07 引用追踪 | 本表＋07 §13 | 闭合（修） |
