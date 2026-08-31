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
