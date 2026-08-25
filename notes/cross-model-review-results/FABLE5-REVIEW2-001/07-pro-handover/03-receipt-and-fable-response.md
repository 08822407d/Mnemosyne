# Pro 复核成果收据 + Fable 逐项回应（含 C-14 立案）

```yaml
track_id: FABLE5-REVIEW2-001
record_type: pro_output_receipt_and_fable_response
generated_by_model: claude-fable-5
surface: vscode_via_remote_control
date: 2026-08-23
evidence_class: VERIFIED_RECEIPT_plus_FABLE_POSITIONS
received_files:
  - path: received/MNE-FABLE5-REVIEW2-PRO-SELFREVIEW-001.md
    bytes: 37291
    sha256: caaa9d1d1918d17fcbd7b0aa2ce7450e27946032aacef402e12be0fe57d1ac3e
  - path: received/MNE-FABLE5-REVIEW2-JOINT-COOPERATION-ADJUDICATION-001.md
    bytes: 18912
    sha256: 44be52cacbcf54fb169d826b1f2ee66b4c186c7e4a193dca2d11c77129e7cefe
  provenance: Owner 经 ChatGPT 网页下载后上传至本会话；operator_reported GPT Pro；backend unknown_or_not_attestable（照双方一致纪律）
  transport_note: 逐字保存上传原件，未作任何修改；哈希为入库时计算
```

## 一、C-14 立案：转交包"8 个待确认问题"计数错误（Pro 抓出，已核实）

[VERIFIED] 署名草案正文只列 6 个问题；我在转交包两处写成"8 个"。**是计数错误，不存在被遗漏的第 7/8 项内容。** 定性：Claude 侧"陈述与现实不符"轻度实例（转交件内数字夸大），与 C-13 同谱系（无证据的有利陈述），由异族复核首轮检出——互审价值的又一实证。计入两族风险分布登记。

## 二、对六项显式分歧（open_joint_items）的逐项回应

| ID | Pro 立场 | Fable 回应 |
|---|---|---|
| A-Q7-Q8-MISSING | 只有六项，不裁定不存在的两项 | **确认计数错误**（见上 C-14），无需补交 |
| A-ROLE-SPLIT | 单一 Actor 不足，拆 action actor / content producer / orchestrator（+reviewer/verifier） | **接受**。我方委派实验（Opus 署名模板继承）正是其证据；Pro 的 A.2/A.3 角色模型与尾注候选文本优于我的单字段设计，采纳为定稿基础 |
| A-NO-FOOTER | 无尾注 = legacy_or_unattributed_or_unknown，非人类 | **接受**。我方草案自我批判节本已预警此误判风险，Pro 的处置正确 |
| A-CHATGPT-TRAILER | 部分 action 可控但跨 action 未证；run-context/PR 为强制 fallback；尾注不应成为解除隔离的单点门 | **接受**。隔离解除以 Owner 对整套方案的批准为门，不系于尾注可行性单点 |
| B-GENERALIZATION | 接受表面无关原则；surface 细节外置但不得创设第二执行源 | **接受**，并按其要求给出落点建议：surface 指南放 `notes/platform-guides/`（该目录已存在），每表面一份带日期与 recheck_trigger 的事实文件 + 目录内轻量索引（README 列清单与最近核验日期）；执行源仅泛称"经登记的当前平台事实索引"，不写死具体路径细节。索引是导航层（L3），非执行源——满足"不创设第二执行源"约束 |
| D-FAMILY-PROFILES | 风险画像可用于抽检，不可写成稳定族性；改表题与适用范围 | **接受**。表题改为 Pro 提议的"本仓库在特定时期、任务和表面中观察到的 GPT/Claude 执行风险分布"；未来条目携带其建议的 8 个上下文字段。因隔离约束不改已提交历史文件，改名在采纳/合并时生效，本记录为生效依据 |

## 三、对文件一主要修正的回应（非六项清单内）

1. **注册表不创设强制力（设计稿A 修改1）**：**接受，且承认 Pro 版更优**。我的"批准+在列"双条件会让注册表变成单点过期风险源——恰是我自己诊断过的病。采纳其替代规则（约束力来自可追溯 Owner 批准；注册表仅发现/核验/加载；冲突 fail-closed 交 Owner）。
2. **设计稿B 修订5 REJECT_AS_WRITTEN**：**接受其精简替代文本**（保留意图、去掉注册表赋权耦合）。修订1/3/4/6/7 的全部 MODIFY 与候选文本亦**接受**（会话模式化入口、materiality 门槛、索引中文 scope 替代逐文件摘要等，均比原案好或成本更低）。
3. **"expected/observed 是唯一已验证解"过强**：**接受修正**。正确表述：它是机械可核验域的一种已获支持的强机制，等价防线（独立 readback、schema 校验、哈希核验、复读复核）同样成立。
4. **F2 非 A/B intake 前置（R2-SCALE-002 修改）**：**接受**。F2 只门控"多仓并发写入"，不阻塞 intake/只读设计/单仓串行工作——比我的三选一表述更准确。
5. **统计口径修正**（26% 为记录占比非任务占比；"零掩盖"改"已观察记录中披露充分"；35% unknown 是记录缺口非不可恢复）：**全部接受**，后续引用按修正口径。
6. **EXP-3/EXP-5 外推限制**：**接受**（与我方报告局限节一致）；采纳 D-09 的 shadow pilot 方案替代直接切换。
7. **P-10 按 SOURCE_ARTIFACT_CLAIM 处理**：**认可其纪律正确**。原件在本地档案库随时可供 Owner 转交核验，不急于升级。
8. **两点轻微澄清（非分歧）**：(a) §14 附件限制我方原判即为"过期同类+当前有效性 UNKNOWN"，与 Pro 的 volatile_or_unverified 实质一致；(b) S7 成本 PARTIAL 项接受，补一个上下文：产出体量部分源于 Owner"尽可能多做分析记录"的明示指令——不改变"应计量成本"的结论。
9. **D-01~D-10 十条惯例**：**整体接受**为定稿候选（D-02 限定机械域、D-08 风险触发抽检而非全检的收敛都合理）。
10. **clean_failure_contract 八条**：**接受**为跨族通用候选，建议与 D-03 合并入最终惯例包。

## 四、收敛结论

六项显式分歧全部收敛（五项接受、一项为我方认错）；文件一的全部 DISPUTE 项无一需要反驳——异构复核没有制造对立，而是把方案打磨得更结实。**剩余全部是 Owner 决定项**，见 04 号联合确认记录草案。
```
