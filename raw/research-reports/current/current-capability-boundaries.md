# Current Capability Boundaries / 当前能力边界（派生视图）

> 说明：本文件是当前能力边界派生视图，不是原始报告，也不是执行源。  
> 当前来源轮次：`RC-2026Q2-initial`；补充当前证据轮次：`RC-2026Q2-memory-testing`。  
> 详细边界见：`raw/research-reports/cycles/2026Q2-initial/capability-boundaries.md`。

## 当前最重要边界（摘要）

1. 普通对话窗口不应假设自动写回外部持久层。
2. Codex / Claude Code 更适合仓库文件写入与可审计变更。
3. GitHub 适合版本管理、diff、PR、review 与审计追踪。
4. 自动化增强（如 GitHub Actions、MCP、RAG）需要额外工具与治理，不是默认能力。
5. 研究报告具有时效性，平台变化后可能过期，需按 cycle refresh。

## 复核提示

- PDF 报告（RPT-2026Q2-0002 ~ RPT-2026Q2-0007）中的图表与图片证据需人工复核。


## DR1 memory-testing boundary additions

6. Do not assume a mature end-to-end industry standard exists for testing external persistent memory systems; combine mature sub-practices instead.
7. Do not rely on final-answer correctness alone; memory evaluation must also inspect state correctness, source priority, temporal correctness, decision propagation, handoff executability, and delivery landability.
8. Multi-model independent review is an auxiliary second-opinion method, not truth voting, execution source, or automatic writeback authority.
9. Current-stage Mnemosyne should prefer half-automatic, file-backed, human-reviewable, traceable evaluation loops over fully automated meta-agent/test frameworks.

## DR2 handoff-strategy boundaries — RC-2026Q2-handoff-strategy

- A handoff replay PASS is bounded evidence for that package, session, repository ref, and evaluation setup; it does not prove permanent cross-model or cross-tool reliability.
- Longer handoff packages are not automatically better. Overlong packages can increase stale-context exposure, token cost, and attention dilution.
- Handoff tests should record visible model/tool label, interface/session type, repository ref/commit, memory/history setting, accessible file set, and known limitations where available.
- Old conversation exports, old replay results, old task result records, and research reports are historical evidence or research input; they are contamination risks if promoted into current truth without current-file verification.
- Handoff scoring can guide verification and candidate template updates, but it does not itself update `current/human-approved-spec.md` or any execution source.
- Replay tests are evidence. Their claims must be checked against current repository state, especially current gate, target selection, target-material ingestion, and target-repository write status.
- Model/judge scoring should not be the sole authority for high-risk handoff decisions; evidence paths, traceability, and human/user review remain necessary for promotion or gate changes.

## DR4 user-input governance boundary — RPT-2026Q2-UIG-0001

- DR4 is evidence only, not execution source.
- Visibility-unverified or possibly-changing visibility must be treated as public-equivalent / public-risk for storage decisions unless a user-approved policy says otherwise within safe boundaries.
- Mnemosyne should not assume Git is safe for originals, raw requirements, sensitive customer/project material, secrets, credentials, private source, or unredacted personal/confidential data.
- AI/human restatements cannot be treated as original requirements or user-approved baseline.
- Redaction manifests and external source pointers are recommended governance instruments before real target material intake.
- Git history exposure persists beyond ordinary delete/move/revert; private repositories do not automatically authorize storing originals.

## DR5 first real dry-run boundary additions — RC-2026Q2-first-target-dry-run-evaluation

- First real dry-run success must be evidence-backed, authority-bounded, no-target-write validation in a real target context; artifact polish is insufficient.
- Synthetic smoke test, tabletop dry-run, real target dry-run, target delivery, and target repository write must not be conflated.
- Critical blockers override scoring; a blocked run cannot be evaluated as real target-project dry-run evidence.
- Deterministic checks should establish boundary and evidence completeness; LLM-as-judge is limited to quality review; user confirmation remains required for usefulness/risk acceptance.
- PASS does not mean production-ready, target repository write approved, target delivery accepted, or global Mnemosyne rule update approved.
- DR5 is evidence only, not execution source.
