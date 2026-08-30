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

## Required files (layered loading — shadow pilot, MNEMOSYNE-245)

Loading is layered per `current/guard-registry.yaml` (navigation index; authority still comes from Owner approval and each guard's own declared scope, per execution-source §20).

**Core set (read on every guidance refresh):**

- `README.md`
- `current/human-approved-spec.md`
- `current/user-operation-next-step-capability-and-intent-guard.md`
- this command file, if available

**Conditional set (read when a trigger matches; when uncertain, read):**

| Trigger | Read |
|---|---|
| Branch or PR creation, or repository write planning | `current/github-single-active-pr-lineage-guard.md` |
| GitHub/connected-repository write, or important publication record | `current/run-context-and-pr-provenance-guard.md` |
| Artifact generation or file delivery | `current/artifact-delivery-and-direct-generation-guard.md` |
| Cross-conversation task design/delivery, or external task launch — including authoring any taskbook to be executed by another conversation (also read the complete-response transfer-file clause of `current/artifact-delivery-and-direct-generation-guard.md`) | `current/cross-conversation-execution-intent-and-operator-flow-guard.md` |
| Naming an external research run | `current/external-research-display-name-guard.md` |
| Deep Research task design or delivery | `current/deep-research-report-delivery-correction-guard.md` |
| Material source-file intake, or major design choice | `current/source-artifact-preservation-and-design-rationale-guard.md` |
| Substantial closing next-step section with potential write | `current/next-step-repository-write-visibility-guard.md` |
| PR readiness decision, frontier segment closure, post-merge closeout | `current/agent-product-ready-pr-and-frontier-efficiency-guard.md` |
| Clarification routing design, or interviewer delegation | `current/frontier-planning-clarification-handoff-adjudication-guard.md` |
| Asking the Owner to merge, or branch retention decision | `current/pr-merge-branch-disposition-guard.md` |
| Branch-backed multi-step Owner review | `current/owner-review-branch-ledger-guard.md` |

Shadow-pilot rules (first cycle):

- The trigger table above (mirroring the registry) is the operative dispatch; when trigger applicability is uncertain, read the guard.
- Full-set reading remains the shadow baseline: a task may be sampled (by Owner request or self-check) to read the full former list and record, in its result record, any guard the dispatch would have missed plus the loading cost.
- Any discovered miss must be recorded and routed to registry maintenance; repeated misses of the same guard escalate it toward the core set via Owner approval.
- New guards default to the conditional set; entering the core set requires an explicit Owner-approved reason recorded in the registry.
- Check the registry header's consolidation triggers; if a consolidation review is due, say so in the refresh response.

Read additional files only when the local task independently requires them.

## Scope precedence

```yaml
precedence:
  execution_source:
    - current/human-approved-spec.md
  general_artifact_delivery:
    - current/artifact-delivery-and-direct-generation-guard.md
  cross_conversation_execution_intent_and_operator_flow:
    - current/cross-conversation-execution-intent-and-operator-flow-guard.md
  Agent_product_PR_readiness_Owner_review_frontier_efficiency_and_post_merge_closeout:
    - current/agent-product-ready-pr-and-frontier-efficiency-guard.md
  PR_merge_and_post_merge_branch_retention:
    - current/pr-merge-branch-disposition-guard.md
  external_research_display_names:
    - current/external-research-display-name-guard.md
  Deep_Research_single_report_semantics:
    - current/deep-research-report-delivery-correction-guard.md
  source_artifact_preservation_and_design_rationale:
    - current/source-artifact-preservation-and-design-rationale-guard.md
  next_step_repository_write_visibility:
    - current/next-step-repository-write-visibility-guard.md
  general_user_operation_capability_research_and_intent:
    - current/user-operation-next-step-capability-and-intent-guard.md
  clarification_architecture_and_research_trigger_adjudication:
    - current/frontier-planning-clarification-handoff-adjudication-guard.md
```

The more specific correction/adjudication/readiness guard controls only its stated scope. It does not replace unrelated requirements in the broader guards.

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
21. Whenever a Deep Research, Fable, Codex, new-ChatGPT-conversation, replay, review, validation, handoff, or other cross-conversation task is designed or delivered, mirror the complete user-executable operator flow directly in the same design/launch response. Repository paths, `OPERATOR.md`, taskbooks, manifests, and downloadable files are supporting artifacts, not substitutes for visible operating steps. Include exact surface/model/mode where selected, preparation, files or links, preflight, launch message or downloadable task, return route, stop conditions, and separate-chat requirements.
22. For every cross-conversation or external task discussed or delivered, explicitly declare whether the response is analysis only, preparation only, an optional launch, or a required launch; distinguish `DO_NOT_RUN`, `READY_NOT_SELECTED`, `RUN_NOW_*`, and `RUN_AFTER_GATE_*` semantics before long analysis. When a run is requested or a complete future flow is supplied, provide a dedicated `## <TASK_ID> 操作流程（时机）` major section immediately after the opening operation/intent section, keep all executable steps together there, and do not rely on a later explanation or closing `下一步` to reveal execution intent.
23. Keep local artifact generation separate from repository write, upload, forwarding, quota spend and research execution authority.
24. Apply dependency-aware staged generation for multiple Pro/Deep Research/cross-conversation tasks; do not generate likely-invalidated downstream tasks without explicit user acceptance.
25. Treat repository visibility and product/model/tool behavior as time-sensitive when relevant.
26. Preserve the current conversation's task mainline; do not import maintenance live routes or infer a handoff.
27. Apply the single-active-PR lineage guard before branch creation and again before PR creation.
28. Apply the run-context and PR provenance guard to important repository-writing work.
29. If required files are unavailable, state the limitation and do not invent repository state.
30. Before asking the user to create or name a GPT Deep Research run, Fable-class research, one-run Project, or equivalent external research/review workspace, allocate and display a compact registered UI alias in the form `<PROJECT_ABBR>-DR-<SEQUENCE> <SHORT_TOPIC>`. Keep the canonical task ID separate, preserve established project numbering, expose the alias in the dedicated operator-flow section, and stop with `DISPLAY_NAME_ALLOCATION_BLOCKED` if the registry cannot be verified.
31. Whenever a response asks the user to review or merge a PR, internally verify whether its head branch has a real post-merge dependency. If retention is required, prominently say `合并后请保留分支`, name the exact branch, explain the dependency, and state the release gate. If no retention dependency exists, do not add a branch-deletion notice; the Owner default is deletion after merge. Unknown retention blocks the merge instruction. When a previously retained branch reaches its release gate, explicitly state that the earlier retained branch can now be deleted, and close the durable retention obligation. Apply `current/pr-merge-branch-disposition-guard.md`.
32. For a material user-supplied task, research, conversation-export or source file, record an explicit preservation level. Preserve exact bytes when safe, authorized, proportionate and mechanically verifiable; never call a normalized copy or hash-only receipt an exact original. Use manual import or an approved outside-Git exact store when the current surface cannot prove exact preservation.
33. For important architecture, behavior, authority, methodology, schema or migration choices, create or reference a compact externally stated design-rationale record covering the problem, decisive alternatives, selection reason, assumptions, risks, validation and affected existing artifacts. Do not request or claim hidden chain-of-thought, and normally explain the result to the user in concise natural language rather than a large English-key YAML block.
34. Preserve material originals without loading them routinely. Treat complete old conversations, research prompts/reports, historical handoffs and completed-task records as default `DO_NOT_READ` / `ON_DEMAND` evidence unless the current task has a specific reconstruction, dispute, migration, incident, citation or full-history-review trigger. State which cold originals were actually read.
35. For Mnemosyne and similar Agent-product work, completed scope with required Agent semantic review and mechanical checks defaults to one Ready PR (`draft: false`). Draft is an exception for incomplete work, content-changing pending decisions/reviews, expected substantive commits, or an explicit Owner request. Do not use Draft as a substitute for comprehensive human review.
36. Treat Owner merge as an authority/acceptance gate, not evidence that the Owner read every changed file or line. The responsible Agent must complete substantive review, state known risks and deferrals, and give a clear merge disposition; the Owner may inspect or sample but does not carry the default full-diff review burden.
37. Before ending a scarce Pro/frontier segment, apply the frontier-turn completion check. Complete all authorized frontier-level work that can safely proceed, honor an explicit request to continue, and route only bounded/mechanical follow-up to a lower-cost model with an explicit model requirement.
38. After a PR merge, verify the merge commit and latest `master`, repair stale route/status records through a new follow-up lineage when needed, close the old PR gate, and state the next true route and model requirement. Merge does not authorize validation, target adoption or another separately gated action.
39. In every substantial closing `## 下一步` section, adjacent to the model recommendation, explicitly state `下一步仓库写入：是 / 否 / 待单独授权 / 待确认`. When a write is known, name the repository and write type; when another conversation may write the same repository, state the serialization or independence gate. Apply `current/next-step-repository-write-visibility-guard.md`.
40. Before finishing a task, check which domains' state the task changed and whether the corresponding live status files were updated; if a relevant live file was not updated, state why in the result record.

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
    - explicit_next_step_repository_write_visibility
    - explicit_Pro_Deep_Research_need_assessment
    - selective_parallel_frontier_review_assessment
    - risk_adaptive_clarification_routing
    - context_rich_material_questions
    - user_correction_and_intent_reconstruction
    - visible_answer_ledger_and_semantic_escalation
    - one_canonical_Deep_Research_report_and_supported_export
    - exact_source_artifact_preservation_levels
    - compact_external_design_rationale_capture
    - cold_originals_on_demand_not_default_runtime_context
    - file_first_delivery_when_relevant
    - same_response_inline_operator_flow_for_cross_conversation_tasks
    - explicit_execution_intent_and_dedicated_operator_flow_section
    - completed_Agent_product_Ready_PR_default
    - Draft_PR_exception_only
    - Owner_merge_not_comprehensive_human_review
    - Agent_pre_merge_semantic_and_mechanical_review
    - frontier_turn_completion_and_quota_efficiency
    - mandatory_post_merge_route_closeout
    - prominent_PR_branch_retention_only_when_required
    - explicit_release_of_previously_retained_branches
    - compact_registered_external_research_display_names
    - staged_prompt_generation
    - visibility_and_platform_freshness
    - single_active_PR_lineage_when_relevant
    - run_context_and_PR_provenance_when_relevant
    - layered_core_conditional_loading_shadow_pilot
    - state_change_live_file_update_check
```

Do not report the Mnemosyne maintenance current phase or next-route options as the receiving conversation's local task state merely because this command was invoked.

## Boundaries

- This command is not an execution source and does not approve new project content.
- Loading guidance does not authorize model switching, quota use, research execution, repository writes, target-project changes, merge, branch retention, branch deletion, automation, MCP, RAG or auto-writeback.
- It does not authorize automatic capture or upload of every conversation/task artifact, and it does not require routine reading of preserved cold originals.
- It does not attest an exact backend.
- It does not start a handoff.
- It does not automatically propagate the clarification architecture, source-preservation guard, Ready-PR guard, next-step repository-write visibility guard or branch-retention guard into Meta-Agent or another target project's truth source.
