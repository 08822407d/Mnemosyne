# Similarity / Conflict Notes

## 查重在需求进入流程中的角色

1. 查重发生在 Candidate Requirement 进入 Human-Approved Spec 之前。
2. 查重对象包括：
   - Raw Record
   - Candidate Requirement
   - Human-Approved Spec Entry
   - Decision Record
   - Open Question
   - TODO Item
3. 查重结果应形成 Similarity / Conflict Report。
4. 报告应提出 `relation_type` 与 `proposed_action`，并包含 `duplicate`、`similar`、`conflicts_with`、`refines`、`supersedes`、`merged_into` 等关系表达。
5. Similarity / Conflict Report 不直接修改 Human-Approved Spec。
6. 用户确认后才可能更新实施版。
7. 当前不实现自动语义查重，仅进行流程与模板设计。
