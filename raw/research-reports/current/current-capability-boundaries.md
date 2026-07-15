# Current Capability Boundaries / 当前能力边界（派生视图）

> 说明：本文件是当前能力边界派生视图，不是原始报告，也不是执行源。  
> 当前来源轮次：`RC-2026Q2-initial`；补充当前证据轮次：`RC-2026Q2-memory-testing`、`RC-2026Q2-handoff-strategy`、`RC-2026Q2-user-input-governance`、`RC-2026Q2-first-target-dry-run-evaluation`、`RC-2026Q3-platform-context-apps-delta`。  
> 详细边界见各 cycle 的 report summary / maintainer review。

## 当前最重要边界（摘要）

1. 普通对话窗口不应假设自动写回外部持久层。
2. Codex / coding-agent surfaces 更适合仓库文件写入与可审计变更。
3. GitHub 适合版本管理、diff、PR、review 与审计追踪。
4. 自动化增强（如 GitHub Actions、MCP、RAG）需要额外工具与治理，不是默认能力。
5. 研究报告具有时效性，平台变化后可能过期，需按 cycle refresh。

## 复核提示

- PDF 报告（RPT-2026Q2-0002 ~ RPT-2026Q2-0007）中的图表与图片证据需人工复核。
- 2026Q3 platform facts must be rechecked before operational use when plan, surface, role, region, workspace or app configuration may have changed.

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

## DR6 platform / context / apps boundary additions — RC-2026Q3-platform-context-apps-delta

10. A newly opened chat is not automatically a cleanroom. Record plan, Project memory mode, prior Project chats/files, saved-memory settings, connected apps and operator-visible configuration.
11. Existing default-memory Projects cannot be converted in place to project-only. Strict Project-based cleanroom tests require a new private Project.
12. Project-only prevents outside-Project chat references but still permits references to other chats within the same Project; use one test chat per cleanroom Project when independence matters.
13. Plugin availability, app enablement, user authentication, sync/indexing, source-system permission, app action control, approval policy, per-chat invocation and current task authority are separate layers.
14. Connected/synced app data can create additional context and Memory-retention risks. Disconnecting an app does not erase prior conversations that used the data.
15. GitHub repository authorization and sync selection are distinct; search/index availability can lag and can omit results.
16. Standard GitHub-app documentation may describe a read-only integration, while upgraded/custom/plugin surfaces can expose actions. Verify the actual action list and approval surface for the current account.
17. Deep Research is the preferred current surface for read-only, multi-source research because connected-app actions are read-only during research; it is not an execution-source or repository-write surface.
18. Chat, Project Chat, Deep Research, Work, Agent and Codex must not be treated as interchangeable. Select by task type, context boundary, action risk and evidence requirements.
19. Visible model/reasoning labels are provenance observations, not complete proof of the hidden runtime model or effort.
20. Connector search/sync results are not complete-enumeration guarantees. Empty or relevance-ranked results cannot by themselves prove that branches, refs, PRs or objects do not exist.
21. No-write evidence should distinguish at least:
   - no write detected in available logs/search;
   - observed default branch unchanged;
   - complete branch/PR scope unchanged;
   - execution surface technically restricted to read-only;
   - observer/log-backed run attestation.
22. Long transfer artifacts should be file-first. Immediate generation of a requested low-risk file artifact is a separate workflow requirement from target-project guidance-loading policy.
23. Research evidence does not resolve `HO-GUIDANCE-001`; target-project business guidance remains a separate user-approved design question.

## DR6 unresolved boundaries

- Complete GitHub connector branch/ref enumeration guarantees are not documented.
- Public documentation does not expose a complete evidence-grade Enterprise Compliance API field schema.
- Project-chat GitHub sync semantics, Library/project-only interaction, and model self-observation of reasoning settings require live or authenticated testing.
- Surface availability varies by plan, role, workspace, region, app configuration and rollout state.
