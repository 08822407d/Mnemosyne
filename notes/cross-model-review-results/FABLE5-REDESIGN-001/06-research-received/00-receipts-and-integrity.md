# 研究回收 · 收据与完整性核验（MNE-DR-020 / MNE-DR-021）

```yaml
record_type: research_return_receipts
track_id: FABLE5-REDESIGN-001
date: 2026-08-31
producer: operator_reported_ChatGPT_Deep_Research（官方入口，智能程度 Owner 报告选 "Pro"）；backend unknown_or_not_attestable
transfer_route: Owner 经 Claude 远程控制上传本机（.claude/uploads/），非聊天正文粘贴——上次乱码事故（MNEMOSYNE-254 传输记录）的对策路线，本次干净
receipts:
  - artifact_id: MNE-DR-020-report
    operator_filename: d1eb19aa-MNEDR020_deepresearchreport.md
    repository_path: 06-research-received/MNE-DR-020-report.md
    bytes: 42042
    sha256: ef43f64893140e6a628b1039bace47e642ffe115c20d64fb2585608c1018bb12
    preservation_level: EXACT_FILE_IN_REPOSITORY
    byte_identity_verified: true   # cp 后 sha256 复核一致；仅改文件名（rename-only, bytes unchanged）
  - artifact_id: MNE-DR-021-report
    operator_filename: f5e7f028-MNEDR021_deepresearchreport.md
    repository_path: 06-research-received/MNE-DR-021-report.md
    bytes: 50638
    sha256: 0f2236602acd07524e66c6ab4c07cd48a14aa0a9f4a5a0581be96db5d0ac7405
    preservation_level: EXACT_FILE_IN_REPOSITORY
    byte_identity_verified: true
integrity_checks:
  encoding: 两件均 UTF-8、无 CR、无 U+FFFD 替换符、无乱码迹象
  identity: 首行任务号/题目与任务书要求逐字一致（020/RQ1、021/RQ2）
  completeness: 020 含 Q1~Q8 全节＋来源表 S01~S42；021 含 Q1~Q7 全节＋来源表 S01~S25；结尾完整
  known_artifact: 正文含 ChatGPT 引用标记残迹（"citeturnNsearchM/viewM"样式，020 约 175 处、021 约 190 处）——深度研究 Markdown 导出的已知伪影（DR6 同款），不影响正文语义；权威引用以文末来源表为准
  contract_conformance: 中文、逐条截至日期、UNKNOWN 显式标注（020 对配额/后台模型等 6 处、021 对多处普及度/收益）、无编造迹象抽查通过（来源表 URL 抽 6 条域名/路径格式合理；未逐条访问复核，标 not_fully_reviewed）
verdict: 两件确认无误，正式入证据层；效力=研究证据（非执行源）
alaya_archive: research/MNE/ 四件（两报告＋两任务书），哈希同上，见 Alaya indexes/archive-inventory-research.yaml

---

## 批次二收据（2026-08-31，MNE-DR-022/023/024）

```yaml
receipts_batch_2:
  - artifact_id: MNE-DR-022-report
    operator_filename: 086c16d4-MNEDR022_deepresearchreport.md
    repository_path: 06-research-received/MNE-DR-022-report.md
    bytes: 43904
    sha256: 9fd6e64a39b7b1c4061f6fe173d0e4fab1dac2dd2db8d2176f2731f58b3d4169
    preservation_level: EXACT_FILE_IN_REPOSITORY
    byte_identity_verified: true
  - artifact_id: MNE-DR-023-report
    operator_filename: 0acf5921-MNEDR023_deepresearchreport.md
    repository_path: 06-research-received/MNE-DR-023-report.md
    bytes: 49489
    sha256: a72845a6962d6d6c965f1a4338c8f84ede1611f9f2ce031e3fb304d5ca5f7c03
    preservation_level: EXACT_FILE_IN_REPOSITORY
    byte_identity_verified: true
  - artifact_id: MNE-DR-024-report
    operator_filename: d8cebdd6-MNEDR024_deepresearchreport.md
    repository_path: 06-research-received/MNE-DR-024-report.md
    bytes: 47826
    sha256: 28dc7fb4fef13149c795f0d485fa59d54622df8c7fdb534d6593fa6f9a5f2b3d
    preservation_level: EXACT_FILE_IN_REPOSITORY
    byte_identity_verified: true
integrity_checks_batch_2:
  encoding: 三件均 UTF-8、无 CR、无 U+FFFD
  identity: 三件首行任务号/题目与任务书一致（022/RQ3、023/RQ6、024/RQ7）；024 首行为纯文本未作标题（cosmetic，非缺陷）
  completeness: 022 Q1~Q8＋来源表 S01~S28；023 Q1~Q7＋来源表（37 行）；024 Q1~Q7＋来源表（24 行）；结尾均完整
  known_artifact: ChatGPT 引用标记残迹 202/232/191 处（已知导出伪影）
  contract_conformance: 中文；UNKNOWN 显式（022 对行业标准枚举/采用率等、023 对 MB 阈值/懒加载因果收益等、024 对多个基准 license）；未逐条访问来源 URL（not_fully_reviewed）
verdict_batch_2: 三件确认无误，入证据层；已按双仓归档制度入 Alaya（哈希同上）

---

## 批次三收据（2026-08-31 深夜，MNE-DR-025/026/027）

```yaml
receipts_batch_3:
  - {artifact_id: MNE-DR-025-report, operator_filename: acdff536-MNEDR025_deepresearchreport.md, repository_path: 06-research-received/MNE-DR-025-report.md, bytes: 42582, sha256: 9a7612eb6e6b1fc2799ead5b09fd66be35cae325c1eb19b7d88e30510e1186c5, preservation_level: EXACT_FILE_IN_REPOSITORY, byte_identity_verified: true}
  - {artifact_id: MNE-DR-026-report, operator_filename: 00a20f67-MNEDR026_deepresearchreport.md, repository_path: 06-research-received/MNE-DR-026-report.md, bytes: 40770, sha256: cd7c9a2cad90dc1a6e7405a8a839524b351c278b728f0210e0f477c15f163e66, preservation_level: EXACT_FILE_IN_REPOSITORY, byte_identity_verified: true}
  - {artifact_id: MNE-DR-027-result, operator_filename: 9719e79f-MNEDR027_ChatGPT_GitHub__________.md, repository_path: 06-research-received/MNE-DR-027-result.md, bytes: 2520, sha256: d1697fc07953f374807799d59ca9d6723b7c1945538979622057d4d4b1736c02, preservation_level: EXACT_FILE_IN_REPOSITORY, byte_identity_verified: true, note: 非深度研究——普通对话 Pro 实测结果记录（run_surface 与类别问题见 PF-002）}
integrity_checks_batch_3:
  encoding: 三件均 UTF-8、无 CR、无 U+FFFD
  identity: 025/026 首行任务号一致且完整（Q1~Q7＋来源表）；027 首行含任务号、四步结果表齐全、含 ChatGPT file-cite 标记残迹（已知伪影）
  producer: operator_reported——025/026 深度研究 Pro；027 普通对话（选择器 Pro，自报 GPT-5.6 Pro，自报不作身份证据）
verdict_batch_3: 三件确认无误入库；027 类别标注问题另立 PF-002
side_effects_of_027_run: 仓库新增测试分支 chatgpt-write-capability-test-20260831 与 Draft PR #326（DO NOT MERGE；处置待 Owner——建议留档后关闭 PR，分支删留均可）

---

## 批次四收据（2026-08-31，MNE-DR-028）

```yaml
receipts_batch_4:
  - {artifact_id: MNE-DR-028-report, operator_filename: 8e0d1ae7-deepresearchreport_8.md, repository_path: 06-research-received/MNE-DR-028-report.md, bytes: 67746, sha256: 36a9c6707d7fadf1e49b1417d6faf95b9b90fd608b5d2411bf944253ac2c094f, preservation_level: EXACT_FILE_IN_REPOSITORY, byte_identity_verified: true}
integrity_checks_batch_4:
  encoding: UTF-8、无 CR、无 U+FFFD；引用标记残迹为已知伪影
  identity: 首行任务号一致；Q1~Q5 全节＋来源表＋UNKNOWN 清单齐全（575 行，本批最长）
verdict_batch_4: 确认无误入库；双仓归档同批完成

---

## 批次五收据（2026-08-31，MNE-DR-029 对照设计——防火墙封存）

```yaml
receipts_batch_5:
  - {artifact_id: MNE-DR-029-counterpart-design, repository_path: 06-research-received/MNE-DR-029-counterpart-design.md, lines: 1553, bytes: 78839, sha256: 4fdbc27abc81a878fc3c38f74ab3e28d61a3234e49db89bb6b97d352e4cd39dc, preservation_level: EXACT_FILE_IN_REPOSITORY, byte_identity_verified: true}
  - {artifact_id: MNE-DR-029-complete-response, repository_path: 06-research-received/MNE-DR-029-complete-response.md, lines: 8, bytes: 1325, sha256: dca19a576ed4aa69f2cd80ea193d670a6d9b0b9482993eb5097f71866974dfc6, preservation_level: EXACT_FILE_IN_REPOSITORY, byte_identity_verified: true}
integrity_checks_batch_5:
  content_review_scope: identity_line_and_stats_only（防火墙：本会话不读两件正文；首行任务号一致"MNE-DR-029 · GPT-5.6 Pro 对照总体方案"/状态行 COMPLETE；编码净）
  note: 回复副本仅 8 行——与任务书"正文只给摘要、全文进设计文件"一致；其内容完整性在防火墙下不可核验，如实登记
  firewall_status: 本会话未读正文；消化留待盲评流程（030/031）完成后按 Owner 批示进行
producer: operator_reported_GPT-5.6_Pro_normal_conversation_via_self-fetch_mode（§2B 直链模式）
