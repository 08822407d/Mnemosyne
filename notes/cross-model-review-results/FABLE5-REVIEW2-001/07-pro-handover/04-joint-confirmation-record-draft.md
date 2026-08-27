# 《多写入方合作方案联合确认记录》草案（供 Owner 终审）

```yaml
track_id: FABLE5-REVIEW2-001
record_type: joint_confirmation_record_draft
generated_by_model: claude-fable-5
surface: vscode_via_remote_control
date: 2026-08-23
evidence_class: JOINT_POSITIONS_CONSOLIDATED_pending_owner_adjudication
parties:
  gpt_side: MNE-FABLE5-REVIEW2-JOINT-COOPERATION-ADJUDICATION-001（received/ 目录，哈希在 03 号收据）
  claude_side: 03-receipt-and-fable-response.md（本目录）
convergence_status: 六项显式分歧全部收敛，双方无遗留对立立场
owner_action: 逐节批 ACCEPT / 修改后批 / 驳回；本记录经你批准即为合作方案的确认基线
adoption_note: 批准本记录不自动执行任何仓库修改；实施按第六节任务清单另行授权
```

> 阅读方式：每节是双方已收敛的定稿候选，你只需对每节给一个字（准/改/驳）。全部"准"则合作方案生效基线确立。

## 第一节 · 署名与溯源方案（原草案 + Pro MODIFY + Fable 接受 = 定稿候选）

1. **提交尾注四行**（重要仓库写入强制）：`Agent-Action-Actor:`（实际调用写入的执行者@表面）、`Agent-Task:`、`Agent-Run-Context:`（指向记录）、`Agent-Content-Producer:`（实际内容生成者；多值写 multiple-see-run-context；不明写 unknown；**不得继承主会话模板**）。
2. **文件头**：重要文档类新文件记 task/actor/surface/provenance_ref；重要修改追加 last_updated 三件；脚本/数据/分片不强制；date 仅在语义需要时写。
3. **PR 来源区块**：重要写入强制（含授权、复核、机械验证、限制四类字段）；低风险机械改动可精简但不省 task 与 action source。
4. **无尾注解释为 legacy_or_unattributed_or_unknown**，不推定人类；Owner 手工普通提交不加负担。
5. **历史不迁移**；新规则生效后按内容组织文件，不按厂商隔离。
6. **ChatGPT 侧尾注**：在支持 caller-supplied message 的 action 上使用，首次提交后 readback 验证；不支持时 PR 区块+run-context 为强制 fallback。尾注可行性不构成任何单点门。

## 第二节 · §18 泛化（方向确认）

采纳 Pro 的表面无关案文方向（十条要点含："Agent 不得自行修改自身权限配置"——C-02 实证入法）；surface 细节外置至 `notes/platform-guides/` 事实文件族＋目录索引（L3 导航层，非第二执行源）。**具体执行源案文并入设计稿B 修订族，待你按第四节批准后由单独授权任务实施。**

## 第三节 · 任务号命名空间（现状追认 + 五条附加约束）

MNEMOSYNE-NNN 留主线维护；长轨道/研究轨道用自有稳定前缀；目标项目用目标侧命名空间；验证运行用父任务下的 run ID。附加：建分支前三重检索照旧；轨道 ID 不自带主线写入权；机械重试不耗新主线号；轨道改正式内容需明确主线实施任务或 Owner 声明；不建全局锁分配器。

## 第四节 · 评审/设计稿修正的采纳基线

- 设计稿A 按 Pro 四点修改采纳（注册表仅索引不赋权、分层先 shadow pilot、整编参数为校准值不入执行源、状态新鲜度另行处理）；
- 设计稿B 七条修订按 Pro 裁定版采纳（修订2 原文；1/3/4/6/7 用 Pro 候选文本；5 用 Pro 精简替代文本）；
- 设计稿E 按六点修改采纳（风险分档跑三条件、隔离声明降级为 operator-reported、预冻结 rubric、成本计量、94% 不作通用阈值、私档限制声明）；
- 九条 REPAIR 发现按 2 ACCEPT + 7 ACCEPT_WITH_MODIFICATION 的口径进入修复排期依据；
- 两族对照表改题为"本仓库在特定时期、任务和表面中观察到的 GPT/Claude 执行风险分布"，未来条目带 8 个上下文字段。

## 第五节 · 跨族协作惯例（D-01~D-10 + clean_failure_contract）

采纳 Pro 的风险自适应惯例包：六条强制（终态合同冻结、机械域 expected/observed、干净失败、多角色署名、新表面预检、状态变更负向 stale 检查）+ 四条默认（终态合同+执行自主的边界版、风险触发异族抽检、core+conditional 加载 shadow pilot、规则新增须答整编四问）+ 八条 clean_failure_contract（与 D-03 合并）。异族抽检最低触发清单照 Pro D.4。

## 第六节 · 批准后的实施任务清单（每项仍需单独授权）

| # | 任务 | 优先级 | 依赖 |
|---|---|---|---|
| 1 | 署名方案落地：更新署名草案为定稿、建 run-context 字段对接 | P1 | 本记录批准 |
| 2 | 执行源修订（设计稿B 修订族，含 §18 泛化案文）走 §6 流程 | P1 | 本记录批准 + 你逐条终批 |
| 3 | 规范层改造任务一（注册表[仅索引]+loader 分层 shadow pilot） | P1 | 本记录批准 |
| 4 | 三处过期状态文件修复（含 §7 死条款联动） | P1 | 任务2 定 §7 方向 |
| 5 | platform-guides 表面事实文件族补齐（Claude Code 首份） | P2 | — |
| 6 | 两族风险分布登记簿定稿（改题+字段） | P2 | — |
| 7 | GPT 侧 EXP-3/EXP-5 对照重复（shadow pilot 一部分） | P2 | Pro 额度 |
| 8 | PR #306 处置：合并（隔离解除）或继续挂起 | **你单独定** | 本记录批准后才有意义 |

## 边界

本草案是双方立场的整合陈述，非执行源；你批准前无任何条目生效；批准后亦不自动执行任何写入——第六节每项按现行授权惯例走。
```
