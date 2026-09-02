# 会话档案（脱敏可读层）

```yaml
record_type: conversation_archive_charter
established: 2026-09-02
established_by: Owner 批示（"Alaya 完整存档；agent 所属仓库保存有效内容，脱敏由执行方决定"）——对 FABLE5-REVIEW2-001/03-independent-design/08 号设计札记"永不入公开仓库"条款的修正
rule: 本仓库（公开）只存"脱敏可读转录＋归档收据"；jsonl 原件与未脱敏转录只入 Alaya（私有）conversations/claude-code/；两侧哈希在收据与 Alaya 索引中互引
desensitization_standard: 家目录路径→~；本机用户名→USER；逐件扫描凭据/邮箱/电话/IP（须为零）；发布前经独立审查代理放行
```

目录：`claude-code/<轨道或任务号>-<角色>-<uuid前8>-readable-desensitized.md`；逐件收据见 `00-receipts.md`。

设计脉络：FABLE5-REVIEW2-001/03-independent-design/08 号札记的默认方案"专门私有档案库"已于 2026-08-28 落地为 **Alaya**（私有；本机工作副本 `~/projs/Alaya`；命名决定见 `notes/alaya-archive-repository-naming-decision.md`）。早先的本地暂存目录 `~/projs/mnemosyne-archives/` 已整体迁入 Alaya 并退役（Owner 2026-09-02：不再为其建 git 仓库）。研究结论件的 Alaya 归档规则另见 FABLE5-REDESIGN-001/09-continuation/06-archiving-institution-record.md。
