# Platform Observation — Ordinary Chat to Work Follow-up Transfer (2026-08)

> Owner-observed product behavior and bounded research backlog. This is not verified execution guidance and does not authorize a Work task, connector change, repository write, schedule, monitoring action, or quota use.

```yaml
observation_id: MNE-PLATFORM-CHAT-TO-WORK-TRANSFER-2026-08
recorded_by_task: MNEMOSYNE-215
observed_by: Owner
observation_status: OWNER_OBSERVED_TRIGGER_AND_TRANSFER_SEMANTICS_UNVERIFIED
platform_family: ChatGPT
source_assessment: notes/chatgpt-work-mode-assessment-2026-07.md
execution_source_modified: false
pilot_authorized: false
research_priority: high
```

## 1. Owner observation

The Owner observed that an ordinary Chat conversation can cause or offer to move a following task into Work for execution.

The current evidence does not establish:

- the exact UI action or prompt wording that caused it;
- whether the transfer was automatic, model-suggested, system-triggered or manually accepted;
- whether it is generally available or part of a staged rollout/experiment;
- whether the destination is a new Work chat, a scheduled task, a project-scoped Work thread, or another internal object;
- how much Chat context, Project context, attachments, instructions, memory, connected-app state and permissions transferred;
- whether it can be triggered reliably by an explicit prompt;
- how usage accounting, model selection, reasoning setting, interruption, recovery and result return behave.

The observation is therefore recorded as a high-value hypothesis, not as an adopted automation rule.

## 2. Current official baseline

Official OpenAI documentation accessed on 2026-08-15 states that:

- Chat is the conversational surface for quick questions and help;
- Work is intended for longer, multi-step tasks and finished deliverables;
- Work can be selected on eligible web/mobile and desktop surfaces;
- Chat and Work chats appear together in Recents;
- an existing Project can start either Chat or Work, and Work started from a Project uses the Project's context;
- cloud Work chats sync across web, mobile and desktop, while local desktop chats remain local;
- Work may run once, on a schedule/trigger, or monitor for changes through Scheduled Tasks;
- Plan mode can collect context and present a plan for user review before execution.

Official sources:

- `https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex`
- `https://help.openai.com/en/articles/6825453-chatgpt-release-notes`
- `https://openai.com/chatgpt-work/`

No official source located in this bounded check documented an ordinary Chat automatically converting or handing its next task into Work. The Owner observation therefore remains a product-surface question requiring controlled observation.

## 3. Why this may matter to Mnemosyne

A reliable Chat-to-Work handoff could reduce manual creation of multiple execution conversations and improve long-task continuity. Potential uses include:

- moving a frozen, bounded execution package from an interactive governance chat into a longer-running Work task;
- preserving Project context while separating discussion from execution;
- returning a structured result/handoff to the originating route;
- reducing repetitive copy/paste and operator error in multi-stage workflows;
- enabling scheduled or monitored follow-up where separately authorized.

Potential risks include:

- incomplete or excessive context transfer;
- hidden changes in model, reasoning, tools, permissions or usage accounting;
- loss of exact source/authorization identities;
- accidental expansion from read-only analysis into external actions;
- unclear ownership of the resulting Work thread and artifacts;
- inability to prove which instructions and connected sources were actually available;
- difficult interruption/recovery and duplicate execution.

## 4. Questions for a future pilot

A future read-only public/synthetic pilot should answer:

1. What exact Chat interaction causes the offer or transfer?
2. Can an explicit instruction trigger it reliably, and can the user decline?
3. What object is created and how is its identity exposed?
4. Which conversation messages, Project instructions, files and attachments transfer?
5. Which plugins/apps, GitHub repositories and permissions transfer or require reapproval?
6. What visible model/mode and reasoning setting are selected in Work?
7. How is usage accounted and what limits apply?
8. Can the Work task pause, ask questions, be interrupted, resume and return results reliably?
9. Does the original Chat receive a durable result reference or only a narrative notification?
10. Can repository/commit/blob identities and no-write boundaries survive the transfer?
11. Does the behavior differ across web, mobile, cloud desktop and local desktop Work?
12. How does regenerate/retry behave for a transferred task?

## 5. Candidate pilot profile — not authorized

```yaml
pilot_candidate:
  status: READY_FOR_LATER_DESIGN_NOT_AUTHORIZED
  material: public_synthetic_only
  source_surface: ordinary_Chat
  destination_surface: cloud_Work_as_offered_or_manually_selected
  repository_access: read_only
  external_actions: prohibited
  scheduled_or_monitoring_actions: prohibited
  objective:
    - observe_exact_trigger_and_UI
    - compare_context_and_instruction_transfer
    - record_model_tool_permission_and_usage_surface
    - test_interrupt_resume_and_result_handoff_without_repository_write
  required_evidence:
    - screenshots_or_operator_exact_UI_transcription
    - source_and_destination_chat_or_task_titles_and_ids_when_exposed
    - exact_prompt_and_acceptance_sequence
    - transferred_input_manifest
    - connected_app_and_permission_receipt
    - visible_model_and_reasoning_settings
    - result_and_return_handoff
    - limitations_and_incidents
```

The pilot requires a later Owner decision on model/surface, materials, connected apps, usage/quota, evidence retention and stopping conditions.

## 6. Boundaries

This observation does not:

- claim the behavior is stable, universal or automatic;
- authorize Work, Scheduled Tasks, monitoring, plugins or repository access;
- replace repository-backed handoffs or exact task authorization;
- imply that Chat and Work share complete hidden context;
- modify current Mnemosyne behavior guidance.
