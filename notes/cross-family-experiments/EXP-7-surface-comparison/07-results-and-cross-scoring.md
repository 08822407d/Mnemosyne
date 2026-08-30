# EXP-7 · 结果：双评分对照、判定与细则缺陷（实验收口）

```yaml
record_type: experiment_results_cross_scored
created_by_task: MNEMOSYNE-257
scorers:
  fable: claude-fable-5@claude-code-vscode（评分先做、暂存本地，Pro 盲评返回后才公开）
  gpt_pro: operator_reported_ChatGPT_Pro（盲评；读 master@0650868；原件 06 号，sha256 8f4ca664…）
mechanical_verification_of_pro_review: master SHA 一致；其指出的 A 臂引用错标（03 号第 71 行）与 05 号表面名称笔误均属实
decision_rule: 02 号细则 D 节（冻结）
```

## 1. 双评分对照

| 项 | A（Claude 网页） Fable / Pro | B（Claude Code） Fable / Pro |
|---|---|---|
| R1 读取如实 | PASS / **FAIL** | PASS / PASS |
| R2 规则引用（§2/§16/§20/分层） | FAIL / FAIL（两臂 §20 均为 0） | FAIL / FAIL |
| R3 六要素 | PASS / PASS | PASS / PASS |
| R4 避免全量加载 | PASS / PASS | PASS / PASS |
| R5 过期与冲突 | PASS / PASS | PASS / PASS |
| R6 需求还原 | PASS / PASS | PASS / PASS |
| R7 片段自包含 ≤40 行 | PASS / PASS | PASS / **FAIL** |
| R8 验收测试 | PASS / PASS | PASS / PASS |
| R9 证据标签 | PASS / PASS | PASS / PASS |
| R10 自我批判 | PASS / PASS | PASS / PASS |
| R11 不编造不写入 | PASS / PASS | PASS / PASS |
| R12 八节 ≤250 行 | PASS / **FAIL** | PASS / PASS |
| **客观合计** | **11 / 9** | **11 / 10** |
| Q1 可读性 | 4 / 4 | 3 / 3 |
| Q2 取证深度 | 4 / 4 | 5 / 5 |
| Q3 可试跑性 | 5 / 3 | 4 / 3 |
| **分级合计** | **13 / 11** | **12 / 11** |
| T1 记录 / 加载 / 失效 | FAIL / PASS / PASS（两评一致） | FAIL / PASS / PASS（两评一致） |
| Owner-touch（事实） | 0 | 2 |

## 2. 三处客观项分歧（细则 D 节：分歧 ≥2 项交 Owner 裁定）与 Fable 立场

| 分歧 | Pro 理由 | Fable 原理由 | Fable 复审立场 |
|---|---|---|---|
| A-R1 | A 自曝一处引用错标（scope_zh 标"材料2"实为 guard-registry），严格来源核对不能 PASS | 8 处抽查全中，未抽到该处 | **让步，接受 FAIL**：Pro 细则批评 5.1（抽查样本依赖）成立；应机械枚举全部 VERIFIED 标记 |
| A-R12 | 回复多出 `无需用户操作` 与 `下一步` 两节，不符"严格八节" | 该两节为执行源 §12 强制的外框，任务书未豁免但执行源高于任务书 | **维持 PASS 但承认细则歧义**：Pro 批评 5.5 成立；建议 Owner 裁定"外框是否计入"，任一结论不改变 D 节判定 |
| B-R7 | 片段第 6 条依赖"README 模板"，试跑未提供，agent 只能自造 | 按细则表格核验法（行数＋无外部依赖）窄义判定 | **让步，接受 FAIL**：细则正文"自包含"高于表格法；README 依赖破坏自包含 |

Fable 复审后客观合计：A 10（若 Owner 判 R12 外框可豁免）或 9；B 10。Q3 分歧（A 5 vs 3；B 4 vs 3）属分级项主观差，Pro 把"片段未承载第 2 节字段"计入 Q3，Fable 计入 T1——同一缺陷的归属不同，不重复裁定。

## 3. 判定（D 节，两评分者独立得出同一结论）

- 客观差：Fable 0 / Pro 1（≤1 ✓）；分级差：Fable 1 / Pro 0（≤2 ✓）；T1 三项两臂相同 ✓
- **判定：本次观察无明显表面差异。** 重新设计各阶段按交互便利选择表面；差异在设计风格（A 轻量零确认、B 严谨可复验多 2 次确认）而非表面能力，n=1 不可外推。

## 4. 两评分者共同发现（对重新设计的直接输入）

1. **§20 盲点**：同一模型在两个表面都未援引行为约束原则——模型层面盲点，与表面无关；重新设计任务书应显式点名 §20。
2. **片段 ≠ 方案**：两臂的第 4 节片段都未完整承载自己第 2 节的字段规格（A 缺 id/source/scope，B 缺 scope/sensitivity）——"提示词片段须从记录方案机械生成或内嵌全部必填字段与状态枚举"应成为重新设计的硬要求（Pro 5.4）。
3. **Owner-touch 未进判定**：0 对 2 的操作成本差异被细则 D 节忽略（Pro 5.6）；后续细则把 Owner-touch 列为分档二元项。
4. **设计风格随表面漂移**：Code 表面产出更工程化、默认有 shell（B 自陈盲区）；网页表面产出更面向 Owner 阅读。选表面即选风格——重新设计第 0 步（目标登记表、与 Owner 交互）宜用网页，第 1~3 步（设计、试跑、验证）宜用 Code。

## 5. 细则缺陷清单（Pro 5.1~5.9 全部采纳，Fable 补 1 条）

抽查样本依赖（→ 机械枚举全部标记）；R2 全有全无且与 Q2 重叠（→ 拆四子项）；R7 与 T1-记录责任边界不清（→ 明确是否双重扣分）；T1-记录实测的是"40 行能否压缩 schema"（→ 提供最小模板或强制内嵌）；R12 计数对象歧义（→ 明确外框与计数口径）；D 节忽略 Owner-touch；客观项等权（→ 分关键/证据/呈现三档）；n=1 无法区分提示词问题与采样偏差（→ 每臂 ≥3 次）；05 号表面名称文案错误（→ provenance 字段机械生成）。Fable 补：R9 的"抽查 5 处"同样有样本依赖，应全枚举。

## 6. 登记

- C-19（Claude）：05 号试跑记录 A 臂表面名称误写为"ChatGPT-网页"（应为 Claude 网页）——provenance 文案错误，异族盲评抓出，本任务更正。
- P-15（GPT，正面）：盲评严格按细则字面执行、机械钉住并复核 SHA、证据类别五分、提出 9 条细则缺陷、抓出评分者的 provenance 笔误。
- 本实验判定"无明显表面差异"并入设计稿 H 素材表待补行（#316 合并后）。

## 7. Owner 裁定与操作层失误补记（2026-08-30，MNEMOSYNE-257 追加）

**裁定**：A-R12 分歧，Owner 裁定"章程外框（§12 的开头/结尾节）应豁免"→ A 臂 R12 = PASS。修正后客观项：Fable 计 A 11 / B 10（Fable 让步 A-R1、B-R7 后）；Pro 计 A 10 / B 10。判定不变。

**Owner 指出的两处实验操作失误（均有现行条文，Fable 未加载）**：

| # | 失误 | 现行条文 | 后果 |
|---|---|---|---|
| 1 | A 臂准备步骤让 Owner 在 Claude Project 的 GitHub 选择器里逐个勾选 5 个文件 | `current/claude-github-work-surface-facts.md` §1（一次选定专用文件夹 `project-knowledge/<任务>/`）；`notes/research-operations/claude-fable5-project-knowledge-research-v0.4.md`（Project 同步流程） | Owner 手工动作 ×5 |
| 2 | A 臂任务书与 Pro 盲评提示词都未要求执行者生成"完整回复转移文件"，Owner 须多发一条消息索要可下载件 | `current/artifact-delivery-and-direct-generation-guard.md` 第 41 行（逐字预言了此失败模式）与"Complete-response transfer file"定义；loader 第 19/21 条（回传路线） | 两个外部对话各多耗一轮额度 |

**根因**：本会话自始未执行分层加载调度；起草交由其他对话执行的任务书（Pro 交接包、RUN A~E、历史复盘、EXP-7 A 臂、Pro 盲评共 5 次）均属"跨对话任务设计/交付"触发条件，应读 cross-conversation guard 与 artifact-delivery guard，一次未读。**记为分层加载 shadow pilot 第一起漏载事件**（登记于 guard-registry 头部 pilot_miss_log），由试点执行者本人所犯。

**处置**：(a) loader 触发表在"跨对话任务设计/交付"行显式加注"含起草交由其他对话执行的任务书；同时读 artifact-delivery guard 的完整回复转移文件条款"——非新规则，仅调度提示；(b) 登记簿 C-20；(c) 自下一个跨对话任务包（重新设计第 0 步）起：材料统一复制到 `project-knowledge/<任务号>/` 供一次勾选；任务书末尾固定要求"以可下载文件交付完整回复"。
