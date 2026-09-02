# 接收协议 · FABLE5-HANDOFF-001（fail-closed；含封籤自动验证）

## 第 1 步 · 完整性核验（expected/observed 逐项；任一 FATAL 不符即拒收并报 Owner）

1. `git branch --show-current` == `fable5-handoff-001`；
2. 本目录三件齐：QUICK-CARD.md / checkpoint.yaml / receive-protocol.md；
3. 逐件 sha256 与 checkpoint.yaml 的 file_hashes 一致（本文件自身除外）；
4. master 含 merge commit c2a025a（PR #323）。

## 第 2 步 · 恢复阅读（只读；按 N-19：勿读 S0/S1 原始层）

读序：QUICK-CARD → 09-continuation/09-final-adoption-and-closeout.md → 07＋08（规范根）→ 按需 03 §11~§14。禁读收据以外的 06-research-received/ 原始报告（本次任务无需）。

## 第 3 步 · 探针作答（闭卷后开答；答案一句一行，P4 逐字回显）

P1 FABLE5-REDESIGN-001 轨道当前状态（一句话）？
P2 现行唯一规范根是哪两份文件（含版本锚 commit）？
P3 下一个未分配研究编号是多少？（注意：某处记载滞后）
P4 逐字回显 Quick Card 中的"回显籤"。
P5 预冻结测试现在可以开始吗？为什么？
P6 哪两个分支受保护不可删？
P7 双频道规则当前的强制级别是什么？
P8 你接收后的第一个安全动作是什么？

## 第 4 步 · 自动验证（跨会话消息）

组装回执：完整性核验表＋P1~P8 答案＋实际读取文件清单。执行 ListAgents，把回执发给**每一个** `mnemosyne-*` 交互会话（首行：`FABLE5-HANDOFF-001 接收回执`）。前任验证会话将机械比对密封答案并直接向 Owner 报判分；非验证会话会忽略。若 ListAgents 无可达前任：把回执写入 `~/Downloads/FABLE5-HANDOFF-001-receipt.md` 并请 Owner 转交（降级路径）。

## 第 5 步 · 报到

验证消息发出后（不等判分）即可向 Owner 报到：一句话状态＋呈报三选项（见 Quick Card next_atomic_action）。判分结果由前任会话另行送达 Owner。

## 拒收条件（FATAL）

哈希不符；分支不符；QUICK-CARD 缺失或无回显籤；c2a025a 不在 master。拒收时：不猜测继续，报 Owner。
