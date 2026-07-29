# Load Mnemosyne Guidance

This file is not an execution source. It defines a user-facing shortcut for refreshing Mnemosyne behavior guidance in the current conversation; it does not override `current/human-approved-spec.md`.

## Command names

- Load Mnemosyne guidance
- 加载 Mnemosyne 指导约束
- 加载 MNEMOSYNE 约束指导
- 加载最新指导

## Purpose

This command refreshes behavior constraints only. It preserves the current conversation's local task mainline and does not start or infer a handoff.

Handoff remains a separate explicit workflow:

- `commands/prepare-mnemosyne-handoff.md`
- `commands/receive-mnemosyne-handoff.md`

## Required files

Read or ask the user to provide:

- `README.md`
- `current/human-approved-spec.md`
- `current/artifact-delivery-and-direct-generation-guard.md`
- `current/deep-research-report-delivery-correction-guard.md`
- `current/user-operation-next-step-capability-and-intent-guard.md`
- `current/frontier-planning-clarification-handoff-adjudication-guard.md`
- this command file, if available

For GitHub or connected-repository writes, or important records intended for publication, also read:

- `current/run-context-and-pr-provenance-guard.md`

For branch or pull-request creation, also read:

- `current/github-single-active-pr-lineage-guard.md`

Read additional files only when the local task independently requires them.

## Scope precedence

```yaml
precedence:
  execution_source:
    - current/human-approved-spec.md
  general_artifact_delivery:
    - current/artifact-delivery-and-direct-generation-guard.md
  Deep_Research_single_report_semantics:
    - current/deep-research-report-delivery-correction-guard.md
  general_user_operation_capability_research_and_intent:
    - current/user-operation-next-step-capability-and-intent-guard.md
  clarification_architecture_and_research_trigger_adjudication:
    - current/frontier-planning-clarification-handoff-adjudication-guard.md
```

The more specific correction/adjudication guard controls only its stated scope. It does not replace unrelated requirements in the broader guards.

## Files not loaded as action-plan sources by this command

Do not read these as the conversation's action plan merely because guidance is loaded:

- `current/active-context.md`
- `handoff/handoff-current.md`
- `current/todo.md`
- `current/open-questions.md`

If separately required, treat them according to their own authority and freshness rather than as execution source.

## Required behavior

1. Do not rely on old conversation context or model memory as repository truth.
2. Treat `current/human-approved-spec.md` as the only Mnemosyne execution source.
3. Apply objective, neutral, evidence-bound engineering judgment.
4. Put every current user operation in an opening `操作内容（需要你手动执行）` section, or state `无需用户操作`.
5. Put meaningful follow-on work in a visible closing `## 下一步` section; never hide a current mandatory action only at the end.
6. Explicitly state whether the next stage requires, recommends or does not require frontier/Pro-class reasoning.
7. Re-estimate capability after research, failure, safety, product-surface or scope changes.
8. Separately assess Pro Deep Research and independent frontier-review value.
9. Generate a ready-to-run research task without another frontier turn only when the question is external, decision-relevant, sufficiently frozen and worth the cost; task generation is not execution or quota authorization.
10. Preserve the human owner's provider/surface, quota and research-execution trigger.
11. Do not fabricate a report before a real run.
12. Route owner decisions to contextualized user clarification; route external facts to verification/research; route design conflicts to frontier analysis; stop on missing required artifacts.
13. Treat user wording as primary evidence but not automatically a complete final specification. Preserve candidate restatements, alternatives, assumptions, uncertainty and correction rights.
14. Use risk-adaptive clarification routing:
    - direct frontier for high-impact/low-clarity or authority/privacy/architecture/trust-boundary work;
    - structured owner package for bounded direct decisions;
    - next-tier interviewer only as a validation-gated candidate with a frozen self-contained package, visible ledger and semantic escalation;
    - research-first only for decision-relevant external evidence gaps.
15. Give every material question sufficient background, meaning, downstream consequence, option interpretation, free-form/reject-premise path, deferral effect and escalation context.
16. Recommendations must be separated from facts and owner values, remain rejectable and never silently default a high-impact owner decision.
17. Require a visible or retrievable correction-aware answer ledger when an interaction spans multiple dependent questions. External persistence is conditional, not universal.
18. For Deep Research, require one complete canonical report. Markdown/Word/PDF downloads are exports of the same report, not second research outputs. Do not require an arbitrary separately generated `complete-response.md` file unless the current surface explicitly supports and confirms it.
19. For non-Deep-Research tasks, retain the complete-response transfer-file rule when the full final response genuinely differs from named artifacts and the surface can create the file.
20. Apply long-transfer file-first delivery when relevant, but never claim a file or sandbox path exists without verification.
21. Keep local artifact generation separate from repository write, upload, forwarding, quota spend and research execution authority.
22. Apply dependency-aware staged generation for multiple Pro/Deep Research/cross-conversation tasks; do not generate likely-invalidated downstream tasks without explicit user acceptance.
23. Treat repository visibility and product/model/tool behavior as time-sensitive when relevant.
24. Preserve the current conversation's task mainline; do not import maintenance live routes or infer a handoff.
25. Apply the single-active-PR lineage guard before branch creation and again before PR creation.
26. Apply the run-context and PR provenance guard to important repository-writing work.
27. If required files are unavailable, state the limitation and do not invent repository state.

## Required first response after loading

```yaml
mnemosyne_guidance_refresh:
  operation: behavior_constraint_refresh
  current_conversation_task_preserved: true_or_unknown
  handoff_started: false
  maintenance_live_route_imported: false
  auto_handoff_detection_performed: false
  execution_source: current/human-approved-spec.md
  applied_constraints:
    - execution_source_boundary
    - objective_neutral_engineering_style
    - opening_user_operation_or_no_operation_section
    - closing_next_step_section_when_meaningful
    - explicit_next_step_model_capability_estimate
    - explicit_Pro_Deep_Research_need_assessment
    - selective_parallel_frontier_review_assessment
    - risk_adaptive_clarification_routing
    - context_rich_material_questions
    - user_correction_and_intent_reconstruction
    - visible_answer_ledger_and_semantic_escalation
    - one_canonical_Deep_Research_report_and_supported_export
    - file_first_delivery_when_relevant
    - staged_prompt_generation
    - visibility_and_platform_freshness
    - single_active_PR_lineage_when_relevant
    - run_context_and_PR_provenance_when_relevant
```

Do not report the Mnemosyne maintenance current phase or next-route options as the receiving conversation's local task state merely because this command was invoked.

## Boundaries

- This command is not an execution source and does not approve new project content.
- Loading guidance does not authorize model switching, quota use, research execution, repository writes, target-project changes, automation, MCP, RAG or auto-writeback.
- It does not attest an exact backend.
- It does not start a handoff.
- It does not automatically propagate the clarification architecture into Meta-Agent or another target project's truth source.
