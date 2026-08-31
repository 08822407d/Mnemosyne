# 任务书 · MNE-DR-032 合成稿异族复核（GPT 侧，普通对话 Pro）

> 完整读取本任务书后执行；看不到最后一节"禁止与停止条件"即回复"输入不完整"并停止。

```yaml
display_name: MNE-DR-032 合成稿复核（普）
canonical_task_id: FABLE5-REDESIGN-001-SR1
execute_in: ChatGPT 官方入口 · 全新普通对话 · 模型选 GPT-5.6 Pro
language: 中文
nature: 开卷复核（盲评阶段已结束）——你可以、也应该同时阅读两份源设计稿与两份盲评
```

## 1. 任务

Mnemosyne 项目已将 Claude 侧设计稿（04）与 GPT 侧设计稿（MNE-DR-029/RAPW）按双盲评审的采纳清单合成为 **SYN-1**。你受 Owner 委托做**采纳前最后一道异族复核**，回答四个问题：

**Q1 蓝图符合性**：SYN-1 是否落实了合成蓝图（05b）的 29 项采纳与 7 项必修？逐项核对（29+7 清单在 05b §3，SYN-1 §16 自称的落位表须逐条验证，不轻信）。

**Q2 优点保全**：SYN-1 是否丢失或弱化了两源稿各自被盲评认可的最强机制？特别检查：Pro 稿的装载算法/双闸门/接收回执/12-case 设计在合成中是否被简化到失效；Fable 稿的双频道/返场简报/purpose 账单是否完整。

**Q3 新缺陷**：合成本身引入的新问题（三档字段制的边界含糊处、两源机制拼接的矛盾、[INFERENCE] 阈值的合理性）。

**Q4 采纳裁决建议**：给 Owner 的最终建议——ADOPT / ADOPT_WITH_CHANGES（列出必改项）/ REJECT（说明理由），并列出采纳后进入预冻结测试前必须先解决的事项清单。

## 2. 材料（自行抓取，逐件报字节数与首行；任一失败即停）

基址 `https://raw.githubusercontent.com/08822407d/Mnemosyne/fable5-redesign-001-workspace/`：

1. 被审稿：`notes/cross-model-review-results/FABLE5-REDESIGN-001/07-synthesis-design-v1.md`
2. 合成蓝图：`notes/cross-model-review-results/FABLE5-REDESIGN-001/05b-synthesis-blueprint-and-divergence.md`
3. 源稿一（Fable）：`notes/cross-model-review-results/FABLE5-REDESIGN-001/04-redesign-fable.md`
4. 源稿二（Pro/RAPW）：`notes/cross-model-review-results/FABLE5-REDESIGN-001/06-research-received/MNE-DR-029-counterpart-design.md`
5. 盲评一：`notes/cross-model-review-results/FABLE5-REDESIGN-001/06-research-received/MNE-DR-030-review.md`
6. 盲评二：`notes/cross-model-review-results/FABLE5-REDESIGN-001/06-research-received/MNE-DR-031-review.md`
7. 细则：`project-knowledge/FABLE5-REDESIGN-001/MNE-DR-030-031-shared-review-rubric.md`
8. 目标登记表：`project-knowledge/FABLE5-REDESIGN-001/pro-counterpart-materials/01-goals-register.md`
9. Owner 裁决包：`project-knowledge/FABLE5-REDESIGN-001/pro-counterpart-materials/02a-contradiction-clarification-package.md`

抓取边界：仅限上列 9 件；不得抓取该仓库其他路径。

## 3. 交付方式（同一最终回复内两个下载文件）

`MNE-DR-032-review.md`（Q1~Q4 逐项＋必改清单）＋`MNE-DR-032-complete-response.md`（最终回复逐字副本）；正文只给摘要。

## 4. 禁止与停止条件

不重写设计（必改项须落到 SYN-1 节号，改法只给方向不代拟全文）；材料缺失/主题被替换即停止；标签纪律 VERIFIED/INFERENCE/UNKNOWN。

## 5. 操作者收尾

两个文件发回 Claude 侧会话。
