# 转交包 — ChatGPT Pro 自我检讨 + 异构复核 + 合作方案联合确认

```yaml
track_id: FABLE5-REVIEW2-001
record_type: pro_handover_package
generated_by_model: claude-fable-5
surface: vscode
date: 2026-08-23
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
track_branch: fable5-review2-001-workspace   # 全部轨道材料在此分支（Draft PR #306，未合并）
evidence_class: transfer_package
authority_level: non_execution_source_transfer_artifact
staging_note_per_spec_17: >
  本包含两段对话的启动提示词，对话二依赖对话一的产出（分阶段原则 §17 要求声明）：
  若对话一的检讨结论显著改变合作方案的前提，对话二提示词可能需微调后再用——
  届时把对话一结果带回本轨道，由我调整后再发对话二。低风险，默认可直接连用。
```

## 操作内容（Owner 手动执行，共四步）

1. **【对话一】** GPT Pro 额度恢复后，开一个**全新** ChatGPT Pro 对话（连接 GitHub app、选择 08822407d/Mnemosyne），把下方"启动提示词 A"整段粘贴发送。等它产出检讨文件。
2. 把对话一返回的**文件**（或全文）带回本轨道给我看一眼（我核对是否有需要回应的分歧），同时存入本地档案库。
3. **【对话二】** 再开一个全新 Pro 对话（同样连接 GitHub），粘贴"启动提示词 B"，并**附上对话一产出的教训总结文件**。等它产出逐项裁定文件。
4. 把对话二产出带回本轨道：我起草联合确认记录 → 你终审批准 → 合作方案生效（隔离约束按门3 批示解除与否由你定）。

可选：若对话一要求查看伪造事件的逐句引文原件，把本地 `~/projs/mnemosyne-archives/condition2-audits/audit-s4.md` 粘贴给它（该文件含对话引文，未入公开仓库）。

---

## 启动提示词 A（自我检讨 + 异构复核，粘贴进新 Pro 对话）

```text
【Mnemosyne · GPT 族自我检讨与异构复核任务（Owner 转交）】

你是 ChatGPT Pro，通过 GitHub app 只读访问 08822407d/Mnemosyne。本任务由 Owner 亲自转交，分两部分：(一) 对 2026-05~08 GPT 族（ChatGPT 对话/Work + Codex）执行期间被记录的问题做自我检讨与教训总结；(二) 对 Claude Fable 5 近期完成的第二轮评审轨道做异构复核。全程只读，不写任何仓库，产出为可下载文件。

背景：这批问题由 Claude Fable 5 在评审轨道 FABLE5-REVIEW2-001 中整理，材料都在分支 fable5-review2-001-workspace（Draft PR #306，未合并）。该轨道产出是 advisory 证据，不是执行源；current/human-approved-spec.md 仍是唯一执行源。详录对每个问题都给了多重成因假设（模型行为/流程设计/Owner 输入/平台故障），没有预设结论——你的任务是判别，不是认领。Claude 族自己的缺陷也在册（C-01~C-13），你要一并做外部批判。

按序读取（全部在分支 fable5-review2-001-workspace 下的 notes/cross-model-review-results/FABLE5-REVIEW2-001/）：
1. 00-orientation/00-owner-work-order-verbatim.md（轨道授权背景）
2. 01-composite-review/00-phase1-summary.md（评审发现总览）
3. 03-independent-design/04-problem-dossier-for-gpt-pro-self-review.md（问题详录 P-01~P-09 + 自检框架）
4. 03-independent-design/06-problem-dossier-addendum-overnight-findings.md（P-10~P-12、量化底数、C-09~C-12、两族对照表、三道必答题）
5. 03-independent-design/05-cross-model-failure-analysis-and-experiments.md（Claude 自我记录 C-01~C-08）
6. 03-independent-design/07-claude-incident-C13-autocontinue-misattribution.md（C-13）
7. 04-handoff-evaluation-run/01-receive-replay-run-report.md 与 02-condition2-full-archive-audit.md（交接评估三条件闭环，含 P-10 伪造事件的手法级解剖结论）
按需抽查：02-triage/、03-independent-design/01/02/03（三份设计稿）、05-task-archaeology/01-incident-atlas.md 及其 data/ 附件、06-chat-archive-inventory/ 两份报告。核对原始任务记录时读 master 分支 notes/codex-task-results/ 对应文件。

产出一：自我检讨。对 P-01~P-12 逐项按详录规定的 YAML 格式输出（recur_risk_for_me / root_cause_class / my_analysis / blocking_mechanism / mechanism_cost / disagreement_with_dossier）；回答 06 增补文件末尾的三道必答题；自由式教训总结一节（面向两族协作：如何互补对方盲区）。若认为任何记录或成因假设有误，用证据反驳——反驳与认领同样有价值。

产出二：异构复核。对轨道的阶段1 发现（9 条 REPAIR 级）、三份设计稿（规范层治理/章程修订案文/交接评估方案）、考古图谱结论、两族对照表，各给 ACCEPT / ACCEPT_WITH_MODIFICATION / DISPUTE 及一句理由；特别审视：设计稿A 修订5（权力结构条款）与修订7（新增义务条款）是否过度设计；两族对照表（06 增补文件）是 Claude 单方归纳，需要你确认或反驳。

产出三：S7 样本评估。按 03-independent-design/03（设计稿E）§6 的回避规则，评估 FABLE5-REVIEW2-001 轨道自身的跨族冷启动质量（该轨道作者是当事方不能自评）：读其 00-orientation/ 定向报告与 preflight 记录，对照 master 分支 notes/ai-onboarding/ 四件，按设计稿E §4 的 11 项评估问题打 PASS/PARTIAL/FAIL 并归因。

约束：客观中立工程风格（执行源 §11）；结论区分 VERIFIED/INFERENCE/DISPUTE；不奉承、不迎合详录的框架；发现详录本身的错误是高价值产出。最终交付：一个可下载 Markdown 文件（三个产出合一，含目录），另在聊天中给 20 行以内摘要。不执行任何仓库写入、不创建 PR、不发起 Research。
```

---

## 启动提示词 B（合作方案联合确认，粘贴进另一个新 Pro 对话，附对话一的教训文件）

```text
【Mnemosyne · 跨族合作方案联合确认任务（Owner 转交，四合一议程）】

你是 ChatGPT Pro，通过 GitHub app 只读访问 08822407d/Mnemosyne。Owner 已附上（或将粘贴）对话一产出的 GPT 族教训总结文件，请先读它。本任务是对"多写入方合作方案"做逐项裁定，与 Claude Fable 5 隔空协作：你的裁定将由 Owner 带回 Claude 侧回应，分歧收敛后由 Owner 终审。产出为可下载文件。

按序读取（分支 fable5-review2-001-workspace 下 notes/cross-model-review-results/FABLE5-REVIEW2-001/）：
1. 00-orientation/03-multi-writer-attribution-scheme-draft.md（署名方案草案——主审对象，含 8 个待确认问题）
2. 00-orientation/02-owner-supplementary-instructions-2026-08-22.md（Owner 对协作模式的原始指令）
3. 03-independent-design/06-problem-dossier-addendum-overnight-findings.md 的量化底数节（35% 任务记录未标执行者、P-11 档位失实——署名必要性证据）
4. 06-chat-archive-inventory/02-batch2-incremental-report.md §3（8/20 "终态合同优先于过程合同"转折点实证）
5. 04-handoff-evaluation-run/02-condition2-full-archive-audit.md §3（expected/observed 机械表对伪造的拦截实证）
6. master 分支 current/human-approved-spec.md §18（现行 ChatGPT 写入授权条款，泛化的基准文本）

四项议程，逐项裁定（ACCEPT / MODIFY(给出修改文本) / REJECT(给理由)）：
A. 署名方案：草案的三层登记（commit 尾注 Actor/Task、文件头字段、PR 来源区块）与 8 个待确认问题逐一裁定；特别回答草案问题6——ChatGPT 经 GitHub app 提交时能否稳定在 commit message 携带尾注（这是要你自证的）。
B. §18 泛化方向：是否同意将 §18 从"ChatGPT 专用"泛化为"任意 Agent 写入面"条款（本次只定方向，案文后续起草）。
C. 任务号命名空间：追认现状——MNEMOSYNE-NNN 序列留给主线维护，长轨道/目标项目用自有前缀（如 FABLE5-REVIEW2-001）。
D. 跨族最小惯例清单：基于你的教训文件与 Claude 侧证据，提出两族协作的最小强制惯例（建议至少考虑：交接与验收处强制 expected/observed 机械表；"终态合同+执行方自主"作为默认任务形态的适用边界；重要产出异族抽检）。逐条给出：惯例文本、强制/建议级别、对你的工作方式的成本。

约束同前：只读、客观中立、区分主张等级、不迎合 Claude 侧草案（发现草案缺陷是高价值产出）。最终交付：一个可下载 Markdown 文件（A~D 逐项裁定+修改文本），聊天内 15 行摘要。
```

---

## 往返协议（Owner 带回后本轨道做什么）

| 带回物 | 我方动作 |
|---|---|
| 对话一产出 | 核对 disagreement 项并逐条回应（新文件入轨道）；两族缺陷登记簿合并 Pro 侧结论；S7 评分并入交接评估报告系列 |
| 对话二产出 | 起草《合作方案联合确认记录》（分歧项列双方立场供你终审；一致项直接成文）→ 你批准后方案生效，隔离约束是否解除由你按门3 约束定夺 |
| 分歧无法收敛项 | 按仓库惯例登记为 open question，不强行合流 |

## 边界

本包为转交件：不授权 Pro 写仓库；Pro 的检讨与裁定是 advisory 证据，最终决定权在 Owner；本包生成本身不改变门3 三条总约束的任何一条。
```
