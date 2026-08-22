# 阶段1 专题06 — 单点风险评审

```yaml
track_id: FABLE5-REVIEW2-001
record_type: composite_review_theme_report
theme: single_point_risks
generated_by_model: claude-fable-5
surface: vscode
date: 2026-08-22
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
evidence_class: mixed_per_claim_labels
authority_level: non_execution_source_advisory_evidence
```

评审问题：哪些人、工具、账号、仓库、文件构成"坏一个、瘫一片"的单点；各自的现有缓解与残余风险。

## R2-SPOF-001 — Owner 单人：所有门、所有验收、所有合并

- severity: OBSERVATION（已知且可能是接受的风险）
- claim: VERIFIED_REPOSITORY_FACT（结构）
- 证据：全部 guard 与工作令把合并权、门批示、验收决定唯一绑定 Owner；owner-decision-results/ 14 份记录均单一决策人；第一轮 GF4-F08 与 GF5-OMIT-CUR-002 已点名 owner-continuity 缺位，Pro 裁定 GF5-TRIAGE-009 = P3 watch。
- 现状变化：两个月内 Owner 决策带宽的约束**加深**了——订阅计划（Issue #265）使高强度决策工具（GPT Pro）按月轮换可用；本轮验收债台账（专题04）显示 2 个 HIGH 级决策债正排队。单人不仅是连续性风险（长期不可用），也已是**吞吐瓶颈**（决策排队）。
- 建议方向：连续性问题维持 watch（或 Owner 显式记录"无方案、接受风险"完成销账）；吞吐问题可缓解——把待决事项按"需要 Owner 高强度判断 / 只需 Owner 点头"分流，后者用打包批示（本轨道门3 即为一次实践）。

## R2-SPOF-002 — 执行族依赖：从 GPT 单族到双通道的过渡态

- severity: OBSERVATION（改善中）
- claim: VERIFIED_REPOSITORY_FACT
- 证据：2026-08 之前全部建设类写入经 ChatGPT/Codex 族（README 首段自述；本轨道 00-orientation/02 存档的 Owner 指令确认）；本月起 Claude 通道打通（onboarding 243、本轨道权限配置与写入实践）；但 Claude 侧常态化被 D-17（署名方案联合确认）阻塞，且任务号/记录惯例的非 GPT 适配未成文（R2-CORE-004）。
- 残余风险：过渡期两族并行时的**规则解释分歧**——同一 guard 文本，两族模型可能执行出不同实践（例：result record 的颗粒度，见 R2-COST-002）。缓解在于署名方案确认时一并明确"跨族共同最小惯例"。
- [MODEL_INFERENCE] 按 Owner 订阅计划，未来一个月 Claude/Fable 将是主力——若 GPT 侧惯例文件此期间不维护，风险方向可能反转为"Claude 单族"。双通道的价值在于**保持两边都能随时接手**，建议把"任一族冷启动接手测试"列为定期演练候选。

## R2-SPOF-003 — 发布通道与本机：通道已双路，本机成新集中点

- severity: NON_BLOCKING
- claim: VERIFIED_REPOSITORY_FACT（通道史）+ MODEL_INFERENCE（本机风险）
- 证据：ChatGPT 平台发布通道在 235–239 连续失败（专题05 R2-COST-003）；恢复采用本地 git 通道；本轨道常态化了第二通道（Claude Code + SSH + gh）。
- 新集中点：本机现在持有 SSH 私钥、gh keyring 凭据、Claude 会话与权限配置——机器故障不损失仓库数据（GitHub 有全量），但会同时中断两条写入通道的**其中一条的全部凭据**并丢失未推送工作。现行纪律（每步 commit+push，本轨道全程执行）把未推送窗口压到分钟级。
- 建议：无需新机制；维持"落盘即推送"纪律即可。凭据重建成本低（gh 重登、SSH 重配），可接受。

## R2-SPOF-004 — 公开仓库：一次失误即永久暴露

- severity: OBSERVATION（固有风险，纪律良好）
- claim: VERIFIED_REPOSITORY_FACT（纪律在位）+ MODEL_INFERENCE（抽样局限）
- 证据：§14/§16 可见性 preflight 与 no-secrets 规则；manual-import 安全门（043）；本轮抽样读取的数十份文件未见敏感内容痕迹——但这是抽样非全量 [MODEL_INFERENCE]；Git 历史永久性已在 §14 明文承认。
- 残余风险集中在**人的单次失误**（贴错文件）与**新写入方不熟悉规则**。Claude 通道的权限允许清单已把强制覆盖推送、删除类操作排除（本机配置），但内容级失误无机械防线（v0.1 无自动扫描，by design）。
- 建议方向：在署名方案确认时给所有写入方的 preflight checklist 统一加一行"公开仓库内容自查"提醒即可，不建议引入自动扫描（违反 §10 边界）。

## R2-SPOF-005 — 外部仓库依赖：证据与真相源在 Mnemosyne 之外

- severity: NON_BLOCKING
- claim: VERIFIED_REPOSITORY_FACT
- 证据：Meta-Agent 真相源在 `08822407d/Meta-Agent`；TLR-V1 的 16 个证据分支与 F2 验证场在 `08822407d/mnemosyne-target-lifecycle-validation-002`；Mnemosyne 内保有关键 blob 哈希与 receipt（F2 status 的 blob 清单、V1 result_bundle_blob）但**不保有内容副本**。
- 风险：外部仓库误删/改写 → 哈希仍在、内容不可复原（哈希只能证伪不能恢复）。D-06 的"证据保全设计"正是为此排队。
- 建议方向：支持 first-three-systems status 列出的 optional route 3（保全设计）在 A/B 立项前完成——因为真实需求项目会产生更多这类外部证据依赖，保全模式宜先定。

## R2-SPOF-006 — 对话档案：最大的库外知识单点

- severity: OBSERVATION
- claim: MODEL_INFERENCE（结构判断）+ VERIFIED_REPOSITORY_FACT（Owner 已察觉）
- 内容：大量决策语境、失败细节、Owner 意图只存在于 ChatGPT/Claude 对话档案中，仓库只有其结晶（result record）。仓库的交接机制正是为对冲此风险而建，但其**真实效果从未被系统评估**——Owner 在 Issue #265 TODO 4 已亲自点名此缺口并给出完整评估方法论（分主线、交接点采样、"事后全档推断成功 ≠ 当时交接有效"的方法学警告）。该评估至今未执行（R2-FRESH-005）。
- 建议方向：TODO 4 是对冲本单点的最高杠杆动作，且与本轮评审天然衔接（本轨道即是一次跨族冷启动交接的活样本）。建议列入门3 选题。

## 小结

六个单点中：一个在改善（002 双通道成型）、一个已双路化（003）、两个纪律良好残余可接受（004/005）、真正需要 Owner 主动动作的是 **001（决策吞吐+连续性销账）**与 **006（交接效果评估）**。无 BLOCKING；无任何单点处于"无缓解"状态。
