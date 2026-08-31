# 研究成果双仓归档制度 · 记录（2026-08-31 Owner 指示）

```yaml
record_type: archiving_institution_record
track_id: FABLE5-REDESIGN-001
owner_instruction_verbatim: "同时注意把它们在Alaya中归档，并且这个归档动作应该形成制度，也就是每个确认无误的研究结论文件都应该及时地随研究课题文件归档到Alaya中正确的位置同时要给它一个符合Alaya规则的文件名。当然如果要在所属agent仓库里归档的话也要在所属仓库中改成符合自己仓库规则的文件名。"
effective_scope: 本轨道自本日起执行；全局化为正式规范（落章程/guard/loader 哪一层）列为候选，交维护线与后续规范层任务裁定
alaya_write_authorization: 本条 Owner 指示即授权（覆盖工作令 §4"Alaya 只读"于此动作范围内）
```

## 制度内容（操作化）

1. **触发**：任一研究结论文件（深度研究报告导出件、前沿研究回传件等）经机械校验（哈希/编码/完整性/任务号一致）确认无误时。
2. **动作**：确认当日内——
   - 归档 **Alaya** `research/<项目码>/`，文件名 `<统一号>-<主题>-<角色>-<归档日期>.md`（角色=report/taskbook/…），**随课题任务书一并归档**；来源表面、原始文件名、哈希记入 `indexes/archive-inventory-research.yaml`；
   - 归档**所属 agent 仓库**（本轨道即 Mnemosyne），按该仓命名规则改名（本例 `MNE-DR-NNN-report.md`），附收据（bytes/sha256/preservation_level）。
3. **两侧哈希必须一致**并双向可查（收据互引）。
4. **命名规则出处**：Alaya 侧新增 `indexes/research-archiving-convention.md`（本次一并建立）；Mnemosyne 侧沿用统一号命名（09-continuation/04 §5 号表）。

## 首次执行实例

MNE-DR-020/021 两报告＋两任务书，四件入 Alaya `research/MNE/`；两报告入本轨道 `06-research-received/`；收据见 `06-research-received/00-receipts-and-integrity.md`。
