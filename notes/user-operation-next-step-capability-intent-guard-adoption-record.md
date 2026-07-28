# User Operation, Next-Step, Capability, and Intent Guard — Adoption Record

> User-approved behavior-guidance adoption record. This file is not execution source; `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
decision_id: MNEMOSYNE-USER-OPERATION-NEXT-STEP-CAPABILITY-INTENT-001
implementation_task: MNEMOSYNE-177
decision_date: 2026-07-28
decision_source: current_Mnemosyne_maintenance_conversation
status: pending_MNEMOSYNE_177_merge
active_guard: current/user-operation-next-step-capability-and-intent-guard.md
guidance_loader: commands/load-mnemosyne-guidance.md
execution_source_modified: false
```

## 1. User request

The user requested that Mnemosyne make three behavior requirements durable:

1. keep current user operations at the top of substantial replies and give later work an equally visible closing `## 下一步` section;
2. estimate in advance which planned stages genuinely require a frontier/open-ended reasoning model and state explicitly whether the next step must use Pro-class capability;
3. treat human wording as necessarily incomplete evidence rather than an infallible final specification, while helping the user reconstruct and correct the real intent without overriding it.

The user stated that these requirements are relevant not only to Mnemosyne but also to Meta-Agent, future meta-Agent-like projects, and long-lived business Agents.

## 2. Adopted operational rule

MNEMOSYNE-177 creates an active behavior guard that:

- requires an opening `操作内容（需要你手动执行）` or `无需用户操作` section for substantial work;
- requires a closing `下一步` section when a meaningful follow-on exists;
- prohibits hiding current mandatory actions in the closing section;
- requires an explicit next-step capability estimate and a direct statement about whether Pro/frontier capability is required, recommended, unnecessary, or unknown;
- requires stage-by-stage re-estimation after research, validation failure, safety changes, or scope changes;
- separates frontier reasoning, next-tier bounded execution, mechanical verification, and human decision;
- preserves literal user wording, candidate restatement, competing interpretations, Agent assumptions, and user correction rights;
- uses low-burden clarification when interpretations materially change high-impact work;
- prohibits mind-reading, stable profiling, or silent replacement of confirmed user goals.

## 3. Why this is a guard rather than an execution-source amendment

The adopted content operationalizes existing execution-source principles:

- raw input before approved requirements;
- objective evidence-bound engineering style;
- operation/explanation separation;
- model validation and migration;
- dependency-aware Pro / Deep Research staging.

The task therefore adds a user-approved behavior guard and updates the guidance loader without modifying `current/human-approved-spec.md`.

This avoids treating a detailed response template or provisional model-capability vocabulary as a new standalone execution source. Controlled validation of next-tier adequacy remains open under `MODEL-CAPABILITY-PLANNING-001`.

## 4. Target-project propagation boundary

The guard should inform future Mnemosyne-generated behavior guidance for target projects, but it does not automatically modify any existing target-project truth source.

```yaml
propagation:
  Mnemosyne_conversations: active_after_merge_and_guidance_refresh
  new_target_project_designs: candidate_default_to_consider
  existing_Meta_Agent_target_files_modified: false
  existing_target_execution_sources_modified: false
  target_owner_decision_still_required: true
```

## 5. Boundary

This adoption does not:

- authorize model switching or quota consumption;
- establish a provider/model routing table;
- prove a next-tier model is adequate;
- attest any hidden backend;
- authorize repository or target-project writes outside MNEMOSYNE-177;
- permit the Agent to overrule a confirmed user decision;
- create a psychological, cognitive, or preference profile;
- modify Meta-Agent or other target-project files.
