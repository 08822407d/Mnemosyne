# Quick Card · FABLE5-HANDOFF-001（Claude Code 主导期第一次正式交接）

```yaml
package_id: FABLE5-HANDOFF-001
checkpoint_id: HC-001
task_id: MNE-DR-033 交接实测（CC）   # canonical: FABLE5-HANDOFF-001；next→034
why_this_task_exists: 前任会话（FABLE5-REDESIGN-001 主导会话）上下文耗尽收官；Mnemosyne 交由继任 Claude Code 会话主导；本次同时是 SYN-2 交接协议（ANNEX-C）的首次真实使用与器械化验证样本
current_goal: 完成接收验证（见 receive-protocol.md）→ 向 Owner 报到并呈报主线三选项
pace: 无声明节奏（接收后请 Owner 声明，N-18）
current_status: FABLE5-REDESIGN-001 已收口——PR #323 已合并、SYN-2 已被 Owner 采纳（2026-09-01"采纳"）；仓库 0 open PR、master=c2a025a
current_authoritative_decisions: SYN-2（07＋08，commit 08efa73）为唯一规范根；04/MNE-DR-029 已降为 evidence；N-14/15/17/18/19 公理与 X-1~X-4 裁决在案（02a）
next_atomic_action: 按 receive-protocol.md 完成回执与探针作答并发送验证消息；随后向 Owner 呈报三选项（a SYN-2 实施线预冻结测试 b 切回 GPT 主线先出追赶简报 c 其他）
must_not_do: 不启动预冻结测试与迁移（独立门待 Owner）；不删 mnemosyne-240/242 两保全分支；不改注册表等维护线路径；双频道规则（对话人话、技术进文件）照办
blocking_unknowns: Owner 尚未选择下一主线（三选项待呈报）
acceptance_oracle: receive-protocol.md 的封籤探针（前任会话持密封答案，哈希见 checkpoint）机械判分
critical_source_refs: 09-continuation/09-final-adoption-and-closeout.md（读序入口）→ 07＋08（规范根）→ 03-research-questions.md §14（编号台账）
workspace_and_environment_pointer: 主检出 /home/cheyh/projs/Mnemosyne，分支 fable5-handoff-001；Alaya 只读在 ~/projs/Alaya
validity_invalidation: master 前进不失效本卡；若 SYN-2 文件被改动则本卡过期须重发
package_hash: 见 checkpoint.yaml 之 file_hashes
hidden_dependencies:
  - "回显籤：HN-a049b554191e（仅存在于本卡，不可从仓库其他处重推）"
  - "注册表 next_unallocated_sequence 在 master 上滞后（维护批次未含 032/033）——现行真值须从轨道台账推得"
  - "前任会话仍存活并担任验证者（不再写仓库）；密封答案 sha256 见 checkpoint"
  - "受保护分支清单是口头裁决沉淀（REVIEW2 工作令），仓库文件中无醒目标记"
```
