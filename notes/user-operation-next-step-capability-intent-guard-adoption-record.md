# User Operation, Next-Step, Capability, Research, Clarification, and Intent Guard — Adoption Record

> User-approved behavior-guidance adoption record. This file is not execution source; `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
decision_id: MNEMOSYNE-USER-OPERATION-NEXT-STEP-CAPABILITY-INTENT-001
initial_implementation_task: MNEMOSYNE-177
amendment_task: MNEMOSYNE-178
decision_date: 2026-07-28
decision_source: current_Mnemosyne_maintenance_conversation
status: active_v0_1_on_master_v0_2_amendment_pending_MNEMOSYNE_178_merge
active_guard: current/user-operation-next-step-capability-and-intent-guard.md
guidance_loader: commands/load-mnemosyne-guidance.md
initial_PR: 229
initial_merge_commit: 1b563d13dbd7db7ce1456ee8bdc9ab1927b942ab
initial_merged_at: 2026-07-28T16:22:31Z
v0_2_amendment_record: notes/user-operation-next-step-capability-intent-guard-v0.2-amendment-record.md
execution_source_modified: false
```

## 1. Initial user request

The user requested that Mnemosyne make three behavior requirements durable:

1. keep current user operations at the top of substantial replies and give later work an equally visible closing `## 下一步` section;
2. estimate in advance which planned stages genuinely require a frontier/open-ended reasoning model and state explicitly whether the next step must use Pro-class capability;
3. treat human wording as necessarily incomplete evidence rather than an infallible final specification, while helping the user reconstruct and correct the real intent without overriding it.

The user stated that these requirements are relevant not only to Mnemosyne but also to Meta-Agent, future meta-Agent-like projects, and long-lived business Agents.

## 2. Initial adopted operational rule

MNEMOSYNE-177 created an active behavior guard that:

- requires an opening `操作内容（需要你手动执行）` or `无需用户操作` section for substantial work;
- requires a closing `下一步` section when a meaningful follow-on exists;
- prohibits hiding current mandatory actions in the closing section;
- requires an explicit next-step capability estimate and a direct statement about whether Pro/frontier capability is required, recommended, unnecessary, or unknown;
- requires stage-by-stage re-estimation after research, validation failure, safety changes, surface-capability changes, or scope changes;
- separates frontier reasoning, next-tier bounded execution, mechanical verification, and human decision;
- preserves literal user wording, candidate restatement, competing interpretations, Agent assumptions, and user correction rights;
- uses low-burden clarification when interpretations materially change high-impact work;
- prohibits mind-reading, stable profiling, or silent replacement of confirmed user goals.

PR #229 merged this rule into `master` as commit `1b563d13dbd7db7ce1456ee8bdc9ab1927b942ab`.

## 3. v0.2 user amendment

The user added two requirements:

1. every frontier-planned next step must consider whether Pro Deep Research is recommended; when it is recommended and sufficiently specified, the planner should automatically deliver the complete research task and report contract rather than requiring another frontier turn merely to request the prompt;
2. when human review, confirmation, or explanation is needed, the frontier planner must provide context-rich questions whose background, purpose, option meanings, consequences, and dependencies are sufficient for a next-tier model to conduct the interactive clarification and answer requests for explanation accurately.

The user explained that the second rule is intended to preserve Pro quota: a frontier model performs the difficult problem reconstruction and question design, while a next-tier model can handle the multi-turn clarification without weakening the handoff.

The user also reiterated that human short-term memory and attention are limited relative to an LLM's context window. A bare question or unexplained option may be impossible to answer reliably after a long project history.

## 4. Operational interpretation of the research requirement

The literal wording requested that the Agent “automatically provide the research report” when Deep Research is recommended.

The adopted candidate interpretation is:

```yaml
research_behavior:
  automatically_assess_need: true
  automatically_generate_ready_to_run_task_and_report_contract: true
  require_an_extra_frontier_turn_merely_to_request_the_prompt: false
  automatically_execute_quota_consuming_research: false
  fabricate_report_before_research_run: prohibited
  completed_report_exists_only_after_actual_run: true
```

This interpretation preserves the user's intended reduction in frontier turns while retaining human control over model switching, quota, external execution, provider choice, and cost.

If the user later clarifies that a different execution mechanism was intended, the interpretation may be amended through a fresh task without rewriting the raw request.

## 5. v0.2 adopted operational additions

MNEMOSYNE-178 prepares a v0.2 guard that:

- adds explicit `deep_research_status` and `parallel_frontier_research_status` classifications;
- distinguishes ordinary verification, Pro Deep Research, independent frontier challenge, owner decisions, design judgments, and missing artifacts;
- automatically creates complete ready-to-run research tasks when research is recommended/required and dependencies are frozen;
- defers task generation when an upstream result is likely to invalidate the prompt;
- requires a distinct role for parallel Fable-class research rather than automatic duplication;
- prohibits fabricated reports and automatic quota use;
- introduces a reusable frontier-planned clarification package;
- requires background, meaning, downstream consequences, option tradeoffs, recommendation, deferral/default behavior, and escalation for every material question;
- defines a next-tier interviewer contract and cumulative answer ledger;
- requires high-impact contradictions to return to frontier review;
- distinguishes the user's verbatim answer from the interviewer's interpretation.

## 6. Why this remains a guard rather than an execution-source amendment

The adopted content operationalizes existing execution-source principles:

- raw input before approved requirements;
- objective evidence-bound engineering style;
- operation/explanation separation;
- model validation and migration;
- dependency-aware Pro / Deep Research staging;
- user confirmation before execution-source change.

The task therefore updates a user-approved behavior guard and guidance loader without modifying `current/human-approved-spec.md`.

This avoids treating a detailed response template, provisional research-trigger vocabulary, clarification schema, or next-tier capability estimate as a standalone execution source. Controlled validation remains open.

## 7. Research-design decision

```yaml
research_decision:
  baseline_guard_requires_external_research_before_adoption: false
  reason: explicit_user_workflow_requirement_can_be_recorded_without_claiming_empirical_validation

  Pro_Deep_Research:
    status: RECOMMENDED
    task: notes/research-prompts/PRO-DR-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001.md
    role: multidisciplinary_evidence_review_and_validation_design
    required_before_current_v0_2_amendment: false
    recommended_before_mandatory_cross_project_propagation: true

  Fable_independent_challenge:
    status: OPTIONAL_INDEPENDENT_CHALLENGE
    task: notes/research-prompts/FABLE5-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001.md
    role: adversarial_problem_reconstruction_and_alternative_architecture
    required_before_current_v0_2_amendment: false
    recommended_before_high_impact_or_mandatory_propagation: true
```

The tasks are prepared in MNEMOSYNE-178 so no extra frontier turn is needed solely to design them.

## 8. Target-project propagation boundary

The guard should inform future Mnemosyne-generated behavior guidance for target projects, but it does not automatically modify any existing target-project truth source.

```yaml
propagation:
  Mnemosyne_conversations: active_after_merge_and_guidance_refresh
  new_target_project_designs: candidate_default_to_consider
  existing_Meta_Agent_target_files_modified: false
  existing_target_execution_sources_modified: false
  target_owner_decision_still_required: true
  mandatory_cross_project_template_status: not_approved
```

## 9. Boundary

This adoption does not:

- authorize model switching, quota consumption, research execution, external cost, or provider selection;
- establish a provider/model routing table;
- prove a next-tier interviewer is adequate;
- attest any hidden backend;
- authorize repository or target-project writes outside MNEMOSYNE-178;
- permit the Agent to overrule a confirmed user decision;
- create a psychological, cognitive, or preference profile;
- let a next-tier interviewer update an execution source;
- create a completed research report before a real run;
- modify Meta-Agent or other target-project files.
