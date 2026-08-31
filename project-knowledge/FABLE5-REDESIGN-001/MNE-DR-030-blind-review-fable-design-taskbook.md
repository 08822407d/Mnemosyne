# 任务书 · MNE-DR-030 盲评 Fable 设计稿（GPT 侧，普通对话 Pro）

> 完整读取本任务书后执行；看不到最后一节"禁止与停止条件"即回复"输入不完整"并停止。

```yaml
display_name: MNE-DR-030 盲评Fable稿（普）
canonical_task_id: FABLE5-REDESIGN-001-BR1
execute_in: ChatGPT 官方入口 · 全新普通对话（不得复用 MNE-DR-029 对话）· 模型选 GPT-5.6 Pro
language: 中文
blind_condition: 你评审的是 Claude 侧设计稿。你不得抓取/回忆/参考 GPT 侧对照稿（MNE-DR-029*），也不得与你账号内其他对话内容互通；只依据本单材料与细则独立评审，不做两稿比较。
```

## 1. 材料（自行抓取，逐件报字节数与首行；任一失败即停）

1. 评审细则（判定标准，先读）：
   https://raw.githubusercontent.com/08822407d/Mnemosyne/fable5-redesign-001-workspace/project-knowledge/FABLE5-REDESIGN-001/MNE-DR-030-031-shared-review-rubric.md
2. 被评设计稿（Fable 稿 v2）：
   https://raw.githubusercontent.com/08822407d/Mnemosyne/fable5-redesign-001-workspace/notes/cross-model-review-results/FABLE5-REDESIGN-001/04-redesign-fable.md
3. 目标登记表 / Owner 裁决 / 反模式清单（判定依据）：
   https://raw.githubusercontent.com/08822407d/Mnemosyne/fable5-redesign-001-workspace/project-knowledge/FABLE5-REDESIGN-001/pro-counterpart-materials/01-goals-register.md
   https://raw.githubusercontent.com/08822407d/Mnemosyne/fable5-redesign-001-workspace/project-knowledge/FABLE5-REDESIGN-001/pro-counterpart-materials/02a-contradiction-clarification-package.md
   https://raw.githubusercontent.com/08822407d/Mnemosyne/fable5-redesign-001-workspace/project-knowledge/FABLE5-REDESIGN-001/pro-counterpart-materials/foundational-agent-antipattern-checklist-v1.md
4. 证据库（仅在核对 R3 引证时按需抓取对应件）：pro-counterpart-materials/ 目录下 MNE-DR-020~028 各 report/result（URL 规律同上）。

抓取边界：仅限上列 URL；**禁止**抓取该仓库其他路径（尤其 MNE-DR-029*、02-consistency*、05*、06-research-received/）。

## 2. 工作

按细则 R1~R8 逐项评审设计稿；交付：逐项表＋三优点/三缺陷（带节号证据）＋采纳建议清单＋标签纪律。

## 3. 交付方式（同一最终回复内两个下载文件）

`MNE-DR-030-review.md`（评审本体）＋ `MNE-DR-030-complete-response.md`（最终回复逐字副本）；聊天正文只给摘要。无法生成文件则如实声明并给最小操作请求。

## 4. 禁止与停止条件

不比较两稿；不重新设计（缺陷只指出不代拟完整替代方案，采纳建议限"该稿内已有机制"）；越界抓取即违例停止；材料缺失/主题被替换即停止。

## 5. 操作者收尾（给 Owner）

两个文件发回 Claude 侧会话。
