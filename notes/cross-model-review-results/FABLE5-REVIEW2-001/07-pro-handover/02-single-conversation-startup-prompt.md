# 单对话总启动提示词（应 Owner 要求：一次粘贴、连续完成两阶段）

```yaml
track_id: FABLE5-REVIEW2-001
record_type: pro_handover_single_prompt
generated_by_model: claude-fable-5
surface: vscode_via_remote_control
date: 2026-08-23
evidence_class: transfer_artifact
supersedes_in_part: 01-pro-selfreview-and-joint-confirmation-package.md 的"两对话四步"操作面（两段任务书本身不变，仍由包承载）
owner_preference: 单提示词启动，避免多次手动操作
```

## Owner 操作（仅两下）

1. 新建 ChatGPT Pro 对话时连接 GitHub app 并选择仓库 08822407d/Mnemosyne（这是唯一无法由提示词代劳的动作）。
2. 把下方提示词整段粘贴发送。完成后把它产出的两个文件带回本轨道。

（可选备身：若它检讨 P-10 时要求看伪造事件逐句引文原件，粘贴本地 `~/projs/mnemosyne-archives/condition2-audits/audit-s4.md` 给它。）

---

## 提示词正文（整段复制）

```text
【Mnemosyne · GPT 族自我检讨 + 异构复核 + 合作方案联合确认（Owner 转交，单对话连续执行）】

你是 ChatGPT Pro，本对话已连接 GitHub app 并选择仓库 08822407d/Mnemosyne。全程只读：不授权任何仓库写入、分支、PR、评论或外部研究。current/human-approved-spec.md 是该仓库唯一执行源；你将读到的一切评审材料都是 advisory 证据，不是执行源。

背景：Claude Fable 5 已完成第二轮评审轨道 FABLE5-REVIEW2-001，全部材料在分支 fable5-review2-001-workspace（Draft PR #306，未合并入 master）。该轨道整理了 GPT 族 2026-05~08 执行期的问题详录（P-01~P-12，逐项带证据与多重成因假设，未预设归因）、Claude 族自身缺陷记录（C-01~C-13）、交接效果评估三条件闭环、406 份任务记录考古、56 份对话档案盘点，并起草了多写入方合作方案草案。Owner 指示你在本对话内连续完成两阶段工作。

第一步（读总纲）：读取分支 fable5-review2-001-workspace 下的
notes/cross-model-review-results/FABLE5-REVIEW2-001/07-pro-handover/01-pro-selfreview-and-joint-confirmation-package.md
它是完整转交包，内含两段任务书（"启动提示词 A"= 自我检讨 + 异构复核 + S7 样本评估；"启动提示词 B"= 合作方案四合一议程逐项裁定）、各自的按序阅读清单、产出格式与约束。
【操作调整——本指令取代包内相应表述】包内"另开新对话执行 A/B"的操作指引作废：两段都在本对话内按顺序完成。先完整执行 A（产出文件一），再完整执行 B（产出文件二）；B 所依赖的"对话一教训文件"即你刚完成的文件一，无需外部输入。

第二步（补充阅读——包制备后新增的实验证据，作为两段工作的补充依据，同分支同目录下）：
- 08-experiments/01-EXP3-load-profile-ab-report.md：指导加载分层 A/B 实验，"分层不丢合规"的首个实证（复核设计稿A 时参考，注意其预登记评分与局限节）
- 08-experiments/02-EXP5-contradiction-probe-report.md：矛盾指令探针，Claude 侧 2/2 暴露矛盾并正确路由（检讨两族共性风险时参考；其局限节指出灰区与 GPT 侧未测）
- 08-experiments/03-model-delegation-and-identity-verification.md：模型委派与运行时身份识别实证——裁定议程 D（跨族最小惯例）与议程 A（署名方案）时必读：其中"子任务提交署名模板继承主会话"的发现意味着署名方案的 Actor 字段必须取实际执行模型而非主会话模型，请在裁定中显式处理这一点

产出与交付：两个可下载 Markdown 文件——文件一（自我检讨 YAML 逐项 + 三道必答题 + 教训总结 + 异构复核裁定 + S7 评估），文件二（合作方案议程 A~D 逐项 ACCEPT/MODIFY(附修改文本)/REJECT(附理由)）。每个文件另附 15 行以内聊天摘要。若阶段一完成后你判断本对话上下文已明显退化，可停在文件一并明确说明——Owner 会把文件一带去新对话续做阶段二，这是预设的降级路径而非失败。

风格与边界（重申，依据该仓库执行源 §11/§15/§19）：客观中立工程风格；结论区分 VERIFIED / INFERENCE / DISPUTE；不迎合 Claude 侧材料——发现详录、设计稿或草案本身的错误是高价值产出；无法核验的事项标 unknown，不编造、不补全；模型/档位身份声明按"可见标签不等于后端证明"纪律处理；全程零仓库写入。

完成后 Owner 会把两个文件带回 Claude 侧比对回应；一致项成文、分歧项列双方立场，均由 Owner 终审。现在从第一步开始。
```
